from pathlib import Path
import json, re, html

ROOT = Path(__file__).parent
forums = {'LoRAM':'s7DkcgpRxL','FloE':'i5aHAkkhJH','LVSpec':'xyXsaQEmCu','LVLMSurvey':'wvlizZdYc1','HybridKV':'jFuN2yI2D7'}
notes = {name:json.loads((ROOT/'sources'/f'{name}.json').read_text()) for name in forums}
def esc(s): return html.escape(s or '')
def inline(s):
    # Parse inline code before emphasis so asterisks inside code stay literal.
    pattern=r'`[^`]*`|\*\*\*.+?\*\*\*|\*\*.+?\*\*|\*[^*\n]+?\*|\[[^\]]+\]\([^)]+\)'
    out=[];pos=0
    for m in re.finditer(pattern,s):
        out.append(esc(s[pos:m.start()]));t=m[0]
        if t.startswith('`'):out.append('<code>'+esc(t[1:-1])+'</code>')
        elif t.startswith('***'):out.append('<strong><em>'+inline(t[3:-3])+'</em></strong>')
        elif t.startswith('**'):out.append('<strong>'+inline(t[2:-2])+'</strong>')
        elif t.startswith('*'):out.append('<em>'+inline(t[1:-1])+'</em>')
        else:
            a=re.fullmatch(r'\[([^\]]+)\]\(([^)]+)\)',t)
            out.append('<a href="'+esc(a[2])+'" target="_blank" rel="noreferrer">'+inline(a[1])+'</a>')
        pos=m.end()
    out.append(esc(s[pos:]));return ''.join(out)
def md(text):
    out=[]; code=[]; incode=False; table=False; listing=False
    for line in text.splitlines()+['']:
        if line.startswith('```'):
            if incode: out.append('<div class="template"><button class="copy">复制模板</button><pre>'+esc('\n'.join(code))+'</pre></div>');code=[]
            incode=not incode; continue
        if incode: code.append(line); continue
        if line.startswith('|'):
            if not table: out.append('<div class="tablewrap"><table>');table=True
            if re.match(r'^\|[\s:|\-]+\|$',line):continue
            cells=line.strip('|').split('|');out.append('<tr>'+''.join('<td>'+inline(c.strip())+'</td>' for c in cells)+'</tr>');continue
        if table:out.append('</table></div>');table=False
        if line.startswith('- ') or re.match(r'^\d+\. ',line):
            if not listing:out.append('<ul>');listing=True
            out.append('<li>'+inline(re.sub(r'^(- |\d+\. )','',line))+'</li>');continue
        if listing:out.append('</ul>');listing=False
        if line.startswith('#'):
            level=min(4,len(line)-len(line.lstrip('#')));out.append(f'<h{level}>'+inline(line.lstrip('# '))+f'</h{level}>')
        elif line.startswith('> '):out.append('<blockquote>'+inline(line[2:])+'</blockquote>')
        elif line.strip():out.append('<p>'+inline(line)+'</p>')
    return '\n'.join(out)

# Curated teaching cases point to exact notes; original prose remains in the archive.
cases=[
('LoRAM','nav3lXeI5L','回答成本问题，要给实际成本','审稿人问 throughput。回复先区分一次性 offline alignment 与用户 online fine-tuning，再给 tokens 和实际资源表。','讲解时强调：解释成本由谁承担之后，仍要给 peak memory、latency、throughput。只说硬件无关的 tokens，不能替代吞吐测量。','成本归属 → 一次性与重复成本 → 同条件资源表 → 有限结论'),
('LoRAM','p286v6AOeJ','抓住 reviewer 明确给出的修改条件','BSMa 要求澄清 large/small 对应关系，并补 unchanged weights 分析。作者说明术语修改与 Appendix C.5 的位置；后续 reviewer 明确决定提分。','这是“追问—定点修订—确认”的闭环。不要把所有正面结局都解释成某句话的效果；这里可核查的是具体对话顺序。','复述剩余 concern → 逐项变更 → 精确位置 → 请求反馈'),
('LoRAM','KOH4WWWgjp','创新性争论要比较训练与推理的对象','asc9 引用 pruning 工作并维持评分。作者进一步解释：训练在小模型上，推理恢复低秩矩阵维度并使用完整模型，与始终在剪枝模型上训练推理不同。','这是仍存在的科学分歧。适合教如何坚定解释贡献；不能把“少数低分”本身当成违规证据。','既有方法的目标 → 本文目标 → 机制差异 → 可观察结果'),
('HybridKV','1aQJexXi8Z','把 heuristic 质疑拆成证据链','JEeP W1 质疑 head 分类依靠视觉观察。回复从 visual intuition、statistical verification 推进到 text-centric sparsity score，并列出阈值对应的静态/动态 head 数量。','好处是把“看图发现”与“算法如何执行”分开。跨任务性能支撑经验有效性，但不能单独充当统计关联或理论证明。','观察 → 定量定义 → 分类规则 → 泛化实验'),
('HybridKV','zvjkab94s5','缺关键 baseline 时，先交代怎样公平比较','mmBU W3.1 的回复说明使用 TailorKV 官方实现、10% KV budget、改用多模态校准数据，以及 GPU/PCIe 条件，再给质量和效率表。','讲解要保留不利结果：并非每个 benchmark 都赢。后续分析承认 TailorKV 在部分视频指标上的优势，再解释所选 operating point。','官方实现 → 匹配预算 → 必要适配 → 质量与速度 → 权衡'),
('HybridKV','61w09XZ6rP','提分记录与“问题已解决”要分开','mmBU 的后续评论明确说将提分；4Xp9 也有独立的 Increase Score 帖。','可以如实写有两位 reviewer 表达提分；但不能由提分自动推定每一个 concern 都被明确确认解决。','记录原话 → 对应 reviewer → 讨论日期 → 不扩大认可范围'),
('FloE','N798t55dFZ','开销给绝对值，也给分母','ZXAh 问 predictor latency。回复给 inter/intra predictor 的 0.11 ms / 0.27 ms，与单个 block 的 5.74 ms 比较。','具体数字比 negligible 更有说服力。1.9% 与 4.7% 是相对单个 block 的比例，讲解时不能说成端到端总时长占比。','测量协议 → 绝对时间 → 明确分母 → 实际影响'),
('FloE','kyvWCY4VKH','自信推荐前先把替代方案摆上桌','bhnT 问：允许质量下降时，为什么不用更小模型？回复增加 Mistral-7B、Llama-3.2-3B 比较，解释内存配置，最后推荐 FloE 用于资源受限部署。','可学习“面向谁、解决什么限制”的推荐方式。表中 FloE-90 并非每项都胜过 Mistral-7B；不要照搬 across all tasks 之类过强概括。','替代方案 → 匹配资源 → 逐项结果 → 面向明确用户推荐'),
('FloE','tMGh2O3Vqc','Acknowledgement 只代表已读','oREx 的 acknowledgement 是标准确认文本；ZXAh 另有评论明确说明 concern addressed 并提分。','这对例子很适合讲“已读”和“被说服”的区别。后续催审应询问残留 concern，不要求把 acknowledgement 解释为认可。','已读 / 已回答 / 明确认可 / 仍有分歧分别记录'),
('FloE','w7CDFcOnM9','给 AC 的请求要能执行','作者 4 月 6 日请求协调，AC 4 月 7 日回复已向 reviewers 发提醒。','可观察的结果是 AC 确实协调了；不能由此推定 reviewer 提分或录用由这次催促造成。历史 AC 摘要的用法仍需服从新一年的渠道规则。','已提交时间 → 尚缺反馈 → 相关 concern → 请求协调'),
('LVLMSurvey','1SehoIZzEV','面对实证不足，用验证矩阵组织补充','yhsG 质疑样本小、缺 variance、模型与硬件覆盖窄。回复扩至 3 模型、11 任务、3 硬件、多个样本量和 seeds，并提供数据表。','不要只说做了更多实验。每个实验维度都对应一项质疑；mean ± std 不应被自动说成完成了显著性检验。','质疑维度 → 实验维度 → protocol → 结果 → 原结论是否保留'),
('LVLMSurvey','Y3lcL4XJgx','正式报告：类别、证据与请求','sNUJ 的 Review Issue Report 勾选 I3 Score Mismatch 和 I11 Non Response，正文按问题展开。','可复用表单化组织方式。高 soundness / excitement 与较低 overall 并非自动逻辑矛盾：应询问哪些未解决问题驱动 overall，并指向关键证据。','当前类别 → review 陈述 → 原稿/回复位置 → 实质影响 → 请求核查'),
('LVSpec','Ht5E13p9bY','边界问题要解释，也要验证','Hhmf 问 text-only 和无关视频输入是否导致退化。作者解释 visual grounding 范围，并补充 GSM8K、无关视频及保守 λ 的结果。','范围说明回答“主张适用哪里”，实验回答“边缘条件下发生什么”。原文安全性是生成质量语境，不能扩大为所有安全问题均已验证。','定义主张范围 → 接受合理风险 → 边界测试 → fallback / 限制'),
('LVSpec','KviDBegIW5','先读 chairs 的上下文，再解释迟到评审','SAC 在 2 月 17 日表示正协调 emergency reviews；后续 2 月 26 日又出现 fFe1 review，作者随即提出迟到和无法回应的问题。','这说明迟到 review 可能有紧急补审背景。准确的诉求是回应机会和评审依据；是否违规、是否忽略由 chairs 按当轮程序判定。','时间线 → 可用回应窗口 → 新 concern → 对公平回应的实际影响'),
('LVSpec','71IfCXBEhd','报告事实错误时，逐条给原稿位置','作者对 fFe1 的 W1–W3 分别指向原稿理论/实证对应、PST 评估和 Table 6。','这里标题叫 Review Issue Report，实际类型是 Author–Editor Confidential Comment。不要仅看标题推定它就是正式 issue-report 表单，也不要用低 confidence 代替事实核查。','原话 → 原稿定位 → 影响哪个结论 → 要求独立核查'),
]

stages=[
('准备','收到 reviews 后','内部工作表','不发布','把每个 W/Q 拆成可以回答的问题，标出致命问题、共性问题与小修。先建立证据台账，再决定哪些实验值得做。','记录 B 初始截止、V 开放可见、D 互动截止、issue-report 窗口；检查篇幅、次数、附件和改稿政策。','问题｜原稿证据｜需补充内容｜负责人｜回复位置｜状态'),
('首轮逐条回复','初始截止 B 前','对应 review 的 Rebuttal / 指定入口','按该会议 Readers','逐条先给答案，再给证据。不要把关键论点留到讨论最后，也不要只让 reviewer 去另一个帖找答案。','每段一个问题；结论 → 原稿定位 → 允许的新证据 → 修订或局限。','T1'),
('General Response','首轮同期或允许更新时','指定 general-response 入口','同稿 reviewers 与 chairs；是否公开看会议','统一贡献定位，合并重复 concern，列重要更新和逐条回应导航。','常用结构：一句贡献、共性问题、实验更新、讨论更新、修订位置。历史拆帖不等于当前允许。','T2'),
('后续讨论','V 后收到具体追问时','原讨论串','沿原线程权限','识别 reviewer 真正在意的剩余问题。先回答新的疑问；对认同的建议落实到可核查修改。','区分新问题、原问题未答清、对贡献的科学分歧。不要把每一轮都写成第二篇 introduction。','T3'),
('催 reviewer','V 后合理等待且规则允许','原 review 线程','目标 reviewer 需可见','一次简短跟进，指向关键回应，询问是否还有未解决 concern。','不要从提交日算沉默时长；先核实回复是否已开放。受限流程不能加帖。','T5'),
('请求 AC 协调','临近互动截止，重要问题仍无反馈','指定 AC 保密入口','作者与对应 chairs；核对实际 Readers','给日期、线程和具体协调动作。AC 不必对每份正常总结单独回复。','催 reviewer、催 AC、报告违规是三个不同动作。涉及 AC 本人时使用上级或正式申诉渠道。','T6 / T7'),
('讨论期总结','允许的总结窗口，尽量留阅读时间','允许的 Summary / 正常评论入口','面向 AC 时按规则设置','说明贡献、关键 concern 的最终状态、剩余分歧以及已提交证据。','General Response 总结内容；Summary 总结讨论状态。AC 私信不能用于绕过篇幅和截止。','T4'),
('评审问题与举报','按专门窗口；严重问题及时报告','Issue Report / 指定诚信渠道','依正式表单；避免误发 Everyone','事实错误用事实核对，程序问题用时间线，严重违规请求正式调查。','不要从低分、低 confidence 或一句符号错误直接推定恶意或 LLM 违规。','T8 / T9 / T10 / T11'),
('决定与后续','作者窗口结束及决定后','等待 / commitment / 申诉 / camera-ready','依阶段规定','内部讨论关闭后不绕道追加 rebuttal。ARR meta-review 与会议 commitment decision 分开处理。','若有 response to meta-review 字段：回应建议、列修订承诺、说明贡献；程序申诉只用允许的理由与窗口。','T12'),
]

css='''
:root{--bg:#f4f5fb;--paper:#fff;--ink:#252b45;--muted:#626a82;--line:#dce0ed;--accent:#5143a5;--teal:#206e66}*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:30px}body{margin:0;color:var(--ink);background:var(--bg);font:16px/1.85 -apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif}a{color:var(--accent);text-underline-offset:4px}button,input,select{font:inherit}button{cursor:pointer;border:1px solid var(--line);border-radius:7px;background:#fff;color:var(--ink);padding:7px 13px}button:hover{border-color:var(--accent);color:var(--accent)}button:focus-visible,a:focus-visible,input:focus-visible{outline:3px solid #9a8fe4;outline-offset:3px}aside{position:fixed;inset:0 auto 0 0;width:235px;background:#e9ebf6;padding:32px 23px;overflow:auto}aside b{font-size:20px}aside p{font-size:13px;color:var(--muted)}nav a{display:block;text-decoration:none;padding:9px 0;border-bottom:1px solid #d8ddec;font-size:14px}.controls{display:flex;gap:8px;flex-wrap:wrap;margin-top:20px}main{margin-left:235px;max-width:1390px;padding:40px 6vw 100px}.chapter{padding:35px 0 55px;border-bottom:1px solid var(--line)}header{padding:30px 0 40px}h1{font-size:clamp(36px,5vw,66px);line-height:1.2;letter-spacing:-2px;max-width:850px;margin:20px 0}h2{font-size:29px;line-height:1.4;margin:30px 0 18px}h3{font-size:21px;margin:28px 0 12px}h4{font-size:18px}p{max-width:850px}.lead{font-size:21px;max-width:760px}.small,.meta{color:var(--muted);font-size:13px}.pill{display:inline-block;background:#e6e1fb;color:#4e4093;font-size:13px;padding:3px 10px;border-radius:30px;margin:3px 5px 3px 0}.notice{padding:18px 22px;background:#e7f1ef;border-left:4px solid var(--teal);margin:22px 0}.route{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border:1px solid var(--line);background:#fff}.route a{padding:20px;border-right:1px solid var(--line);text-decoration:none}.route strong{display:block;font-size:18px}.stage{display:grid;grid-template-columns:65px 1fr;gap:18px;padding:28px 0;border-top:1px solid var(--line)}.num{font-size:32px;color:var(--accent)}.stage h3{margin-top:0}.stage p{margin:8px 0}.case{margin:24px 0;padding:28px;background:#fff;border:1px solid var(--line);border-radius:12px}.case h3{margin-top:0}.formula{color:var(--teal);font-weight:600;margin:18px 0}.quote{background:#f0eef9;padding:18px 23px;border-radius:5px;white-space:pre-wrap;font-family:Georgia,"Times New Roman",serif;line-height:1.65;font-size:17px}.tablewrap{overflow:auto}table{border-collapse:collapse;background:#fff;width:100%;font-size:14px;margin:18px 0}td,th{padding:12px 14px;text-align:left;vertical-align:top;border:1px solid var(--line);min-width:100px}tr:first-child{font-weight:600;background:#e9ebf7}.template{background:#edf0f7;border-radius:8px;padding:17px 20px;margin:16px 0}.copy{float:right;font-size:12px;padding:4px 10px}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:14px/1.7 ui-monospace,SFMono-Regular,monospace;clear:both}code{font-size:.9em;background:#e8eaf4;padding:2px 5px}details{background:#fff;border:1px solid var(--line);padding:14px 18px;margin:10px 0}summary{cursor:pointer;font-weight:600}blockquote{border-left:3px solid #8a7bc5;margin:18px 0;padding:12px 22px;background:#f0eef9}.searchbar{position:sticky;top:0;background:var(--bg);padding:12px 0;display:flex;gap:10px;z-index:2}.searchbar input{width:100%;padding:11px;border:1px solid var(--line);border-radius:6px}.raw{white-space:pre-wrap;font:14px/1.8 -apple-system,"PingFang SC",sans-serif;max-height:65vh;overflow:auto}.noteitem .meta{overflow-wrap:anywhere}.checks label{display:block;padding:9px 0}.checks input{margin-right:10px}.present .chapter{display:none}.present .chapter.active{display:block}.present main{max-width:none}.present header{display:none}.present .chapter.active h2{font-size:40px}.present .controls{position:fixed;bottom:25px;left:25px;max-width:190px}footer{padding:35px 0}.toast{position:fixed;bottom:30px;right:30px;background:var(--ink);color:#fff;padding:10px 20px;border-radius:7px;display:none}.archive-warning{background:#fff1d8;padding:15px 20px} @media(max-width:850px){aside{position:static;width:auto;padding:18px}nav{display:flex;flex-wrap:wrap;gap:15px}nav a{padding:0}.controls{margin:10px 0}main{margin:0;padding:20px}.route{grid-template-columns:1fr}.stage{grid-template-columns:40px 1fr}.case{padding:20px}.present .controls{position:static;max-width:none}h1{letter-spacing:-1px}}@media print{aside,.controls,.copy,.searchbar,.toast{display:none!important}main{margin:0;padding:0}.chapter,.present .chapter{display:block!important;break-before:page}details{break-inside:avoid}.raw{max-height:none}body{background:white;font-size:11pt}header{display:block!important}a{color:inherit}.case{break-inside:avoid}}
'''

parts=['<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>如何完成一轮 Rebuttal · 五篇论文实战手册</title><style>'+css+'</style><body>']
chapters=[('start','如何使用'),('cycle','全周期怎么推进'),('visibility','入口与可见性'),('cases','五篇案例拆解'),('templates','全周期模板'),('phrases','语气与表达'),('finish','交稿前检查'),('archive','145 条原始帖子')]
parts.append('<aside><b>Rebuttal 实战手册</b><p>Jun Zhang 的五篇论文案例<br>ICLR / ICML / ACL ARR</p><nav>'+''.join(f'<a href="#{i}">{t}</a>' for i,t in chapters)+'</nav><div class="controls"><button id="mode">讲解模式</button><button id="prev">上一节</button><button id="next">下一节</button><button onclick="window.print()">打印 / PDF</button></div><p id="position"></p></aside><main>')
parts.append('<header><span class="pill">从 review 到最终决定</span><h1>把 Rebuttal 写成<br>一段有证据的对话</h1><p class="lead">读懂 concern，给出回答，跟进分歧，让 AC 看清贡献。用五篇论文的真实讨论，走完每一步。</p><p class="small">已在 Jun Zhang 登录会话中核对五个原始论坛 · 2026 年 11 月 10 日 · 独立 HTML，可离线查阅</p></header>')
parts.append('<section class="chapter" id="start"><h2>先知道这份手册怎么用</h2><div class="route"><a href="#cycle"><strong>准备写 rebuttal</strong>先看全周期，再逐项套模板。</a><a href="#cases"><strong>准备给人讲解</strong>用案例讲 concern、回应与后续。</a><a href="#archive"><strong>想核对原话</strong>搜索全部帖子、日期和 Readers。</a></div><p>讲解建议：先用 LoRAM 展示“追问—修订—明确反馈”，再用 HybridKV 展示证据组织，用 FloE 讲认可与协调，最后用 LVSpec 和 Survey 讲边界与评审问题报告。</p><div class="notice">原文摘录、中文拆解、建议模板分别标注。历史上发过的内容不自动等于当前政策允许；当前页面显示的 Readers 也不能还原该帖当年每个阶段的权限。</div><p>档案含登录作者账号可见的 chairs 保密评论，适合本地备课核对；向外分享时应使用你确认适合公开的案例摘录。这里没有发布到外部网站。</p></section>')
parts.append('<section class="chapter" id="cycle"><h2>一轮 rebuttal 的九个动作</h2><p>时间以会议的三个节点为准：B 是初始回复截止，V 是回复对 reviewer 开放的时刻，D 是作者互动截止。每一步是否有独立入口和次数，以本轮通知为准。</p>')
for k,(title,time,where,readers,goal,key,template) in enumerate(stages,1):
    parts.append(f'<article class="stage"><div class="num">{k:02}</div><div><h3>{title}</h3><span class="pill">{time}</span><p><b>写什么：</b>{goal}</p><p><b>怎么组织：</b>{key}</p><p class="meta">入口：{where}<br>可见性：{readers}<br>模板：{template}</p></div></article>')
parts.append('<h3>五篇案例实际采用的节奏</h3><p>下列日期来自帖子创建时间，按页面显示保留，未转换时区；不是会议官方截止。后续修改时间与正文对截止的描述可能不同，不能用来反推当时的可用窗口。</p>')
from datetime import datetime
for name,arr in notes.items():
    selected=[]
    for n in arr:
        if any(t in n['title'] for t in ['Initial Response','Rebuttal by Authors','General Response','Summary of the','Comments to the Area Chair','Review Issue Report','Formal Feedback','Seeking Further Feedback','Author AC Confidential Comments by Area']):
            match=re.search(r'\d{2} [A-Z][a-z]{2} \d{4}, \d{2}:\d{2}',n['meta'] or '')
            if match:selected.append((datetime.strptime(match[0],'%d %b %Y, %H:%M'),n))
    selected.sort(key=lambda x:x[0])
    # Keep the first technical response, then the distinct coordination/summary/report posts.
    first=next((n['id'] for _,n in selected if 'Initial Response' in n['title'] or n['title']=='Rebuttal by Authors'),None)
    rows=[]
    for dt,n in selected:
        if ('Initial Response' in n['title'] or n['title']=='Rebuttal by Authors') and n['id']!=first:continue
        rows.append(f'<tr><td>{dt:%Y-%m-%d %H:%M}</td><td><a href="https://openreview.net/forum?id={forums[name]}&noteId={n["id"]}" target="_blank" rel="noreferrer">{esc(n["title"])}</a></td></tr>')
    parts.append(f'<details><summary>{name} 实际发帖时间线</summary><div class="tablewrap"><table><tr><td>页面创建时间</td><td>动作与原帖</td></tr>'+''.join(rows)+'</table></div></details>')
parts.append('</section>')
guide=(ROOT/'Rebuttal时间线与模板指南.md').read_text()
vis=guide.split('## 3 可见性怎么判断')[1].split('## 4 不同回复')[0]
parts.append('<section class="chapter" id="visibility"><h2>入口与可见性：发对地方才算回应</h2>'+md(vis)+'<div class="notice">LoRAM 的 General Response 显示 Everyone，Summary 显示作者与 chairs；FloE 普通回复目前显示 Everyone，AC 评论仍显示作者与 chairs；ARR 案例的评论还包括 Commitment Readers。以上是当前读取到的权限，不假设从创建起始终如此。</div></section>')
parts.append('<section class="chapter" id="cases"><h2>五篇论文，十五个讲解切口</h2><p>每个例子都链接到具体帖子；展开可阅读该帖完整正文和当前元数据。中文说明是教学分析，不把作者的指控写成委员会调查结论。</p>')
for name,nid,title,context,lesson,formula in cases:
    n=next(n for n in notes[name] if n['id']==nid)
    url=f'https://openreview.net/forum?id={forums[name]}&noteId={nid}'
    parts.append(f'<article class="case"><span class="pill">{name}</span><h3>{esc(title)}</h3><p>{esc(context)}</p><p><b>讲解重点：</b>{esc(lesson)}</p><div class="formula">{esc(formula)}</div><a href="{url}" target="_blank" rel="noreferrer">在 OpenReview 核对该帖</a><details><summary>原帖全文与当前 Readers</summary><p class="meta">{esc(n["title"])}<br>{esc(n["meta"])}</p><div class="raw">{esc(n["body"])}</div></details></article>')
parts.append('<div class="notice"><b>完整阅读后需要纠正的三个印象</b><p>LoRAM 的 asc9 并非完全没有参与讨论：11 月 27 日有两条实质回应，并维持创新性分歧。FloE 的标准 acknowledgement 不等于认可所有 concern 已解决。LVSpec 的 typo 回复提到 τ，而期末 Summary 提到 λ；引用时应保留各帖原意，不能把两者合并为已证实的 LLM 违规证据。</p></div></section>')
templates=guide.split('## 5 可直接改写的英文模板')[1].split('## 6 有用表达')[0]
parts.append('<section class="chapter" id="templates"><h2>每个阶段，照着写的模板</h2><p>先选模板，再替换事实和定位。模板表达不包含你尚未完成的实验，也不预设 reviewer 已认可。复制后删除所有不适用的句子。</p>'+md(templates)+'</section>')
phrases=(ROOT/'Rebuttal英文表达库.md').read_text()
parts.append('<section class="chapter" id="phrases"><h2>自然、自信，也可以坚定</h2><div class="notice">原帖常用 “Thanks for raising the score, it’s a huge recognition of our work!”；更自然的推荐改写是 “Thank you for the updated assessment. We appreciate your careful consideration.” 原文与润色版本不要混称。</div>'+md(phrases.split('## 1 自然地接住对方的问题')[1].join(['## 1 自然地接住对方的问题','']))+'</section>')
parts.append('<section class="chapter" id="finish"><h2>交稿前，用这十项收尾</h2><div class="checks">')
for i,t in enumerate(['每个 W/Q 都有对应答案，最重要的结论在开头。','引用原稿、回复新增结果、修订计划的状态准确。','baseline、硬件、预算、任务和指标可比较。','每个结果都有单位、条件和明确分母。','已读、提分、明确认可和沉默分别记录。','General Response 讲内容，Summary 讲状态。','没有用额外评论或 AC 私信绕过字数、次数或截止。','技术分歧、事实错误和严重违规使用合适入口。','Readers、匿名身份、链接和附件符合当轮要求。','没有占位符残留，已保存最终文本和时间记录。']):
    parts.append(f'<label><input type="checkbox" data-check="{i}">{t}</label>')
parts.append('</div><h3>规则速查与适用年份</h3>'+md(guide.split('### 1.1 不同会议的关键差异')[1].split('### 1.2')[0])+'<p>本手册的历史案例是 ICLR 2025、ICML 2025、ARR October 2025 / January 2026。上表是另行核对的规则示例，不能混用年份。ARR 页面存在适用周期提示，须结合本轮通知。</p></section>')
parts.append('<section class="chapter" id="archive"><h2>原始帖子索引</h2><p>145 条已登录账号可见帖子，按五个论坛分别索引。保留全文便于备课；技术表格的纯文本结构以在线原帖排版为准。元数据记录当前版本与当前 Readers，没有推断初始分数或历史权限。</p><div class="searchbar"><input id="search" placeholder="搜索主题、reviewer、原句或日期" aria-label="搜索帖子"><select id="paper" aria-label="选择论文"><option value="">全部论文</option>'+''.join(f'<option>{n}</option>' for n in notes)+'</select></div><p id="results" class="meta"></p><div id="notes"></div></section><footer>基于作者提供的五个 OpenReview 论坛整理。HybridKV 原始评审地址为 jFuN2yI2D7；ACL commitment 页为 mDVM1qiIWH。<br>附带：<a href="Rebuttal时间线与模板指南.md">Markdown 指南</a> / <a href="Rebuttal英文表达库.md">英文表达库</a>。<br>本手册包含作者视角的保密评审内容，请按实际使用场景选择分享范围。</footer></main><div class="toast" role="status" id="toast"></div>')
data=[dict(n,paper=name,forum=forums[name]) for name,arr in notes.items() for n in arr]
parts.append('<script id="archive-data" type="application/json">'+json.dumps(data,ensure_ascii=False).replace('<','\\u003c')+'</script>')
parts.append('''<script>
const chapters=[...document.querySelectorAll('.chapter')];let current=0,present=false;
function show(i){current=(i+chapters.length)%chapters.length;chapters.forEach((s,k)=>s.classList.toggle('active',k===current));document.getElementById('position').textContent=(current+1)+' / '+chapters.length;if(present)scrollTo(0,0)}
document.getElementById('mode').onclick=()=>{present=!present;document.body.classList.toggle('present',present);document.getElementById('mode').textContent=present?'连续阅读':'讲解模式';show(current)};
document.getElementById('prev').onclick=()=>{show(current-1);if(!present)chapters[current].scrollIntoView()};document.getElementById('next').onclick=()=>{show(current+1);if(!present)chapters[current].scrollIntoView()};
document.querySelectorAll('nav a,.route a').forEach(a=>a.addEventListener('click',()=>{let idx=chapters.findIndex(c=>'#'+c.id===a.hash);if(idx>=0)show(idx)}));
document.addEventListener('keydown',e=>{if(/INPUT|TEXTAREA|SELECT/.test(e.target.tagName))return;if(present&&e.key==='ArrowRight')show(current+1);if(present&&e.key==='ArrowLeft')show(current-1);if(e.key==='Escape'&&present)document.getElementById('mode').click()});
function toast(t){let e=document.getElementById('toast');e.textContent=t;e.style.display='block';setTimeout(()=>e.style.display='none',1800)}
document.querySelectorAll('.copy').forEach(b=>b.onclick=async()=>{const t=b.parentElement.querySelector('pre').textContent;try{await navigator.clipboard.writeText(t);toast('已复制模板')}catch{let s=getSelection(),r=document.createRange();r.selectNodeContents(b.parentElement.querySelector('pre'));s.removeAllRanges();s.addRange(r);toast('模板已选中，请按 Ctrl/Cmd+C')}});
const all=JSON.parse(document.getElementById('archive-data').textContent);const esc=s=>(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function render(){const q=document.getElementById('search').value.toLowerCase(),p=document.getElementById('paper').value;let filtered=all.filter(n=>(!p||n.paper===p)&&(!q||[n.title,n.meta,n.body,n.paper].join(' ').toLowerCase().includes(q)));document.getElementById('results').textContent=filtered.length+' / '+all.length+' 条帖子';document.getElementById('notes').innerHTML=filtered.map(n=>'<details class="noteitem"><summary>'+esc(n.paper)+' / '+esc(n.title)+'</summary><p class="meta">'+esc(n.meta)+'</p><a target="_blank" rel="noreferrer" href="https://openreview.net/forum?id='+n.forum+'&noteId='+n.id+'">查看在线原帖</a><div class="raw">'+esc(n.body)+'</div></details>').join('')}
document.getElementById('search').oninput=render;document.getElementById('paper').onchange=render;render();show(0);
document.querySelectorAll('[data-check]').forEach(c=>{try{c.checked=localStorage.getItem('rebuttal-check-'+c.dataset.check)==='true'}catch{}c.onchange=()=>{try{localStorage.setItem('rebuttal-check-'+c.dataset.check,c.checked)}catch{}}});
</script></body></html>''')
(ROOT/'Rebuttal实战手册.html').write_text('\n'.join(parts))
print('Built Rebuttal实战手册.html:',len(data),'notes;',len(''.join(parts)),'characters')
