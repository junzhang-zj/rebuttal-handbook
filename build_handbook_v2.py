"""Build the stage-first handbook, including authentic browser screenshots."""
from pathlib import Path
import runpy, re, html, base64, json

ROOT=Path(__file__).parent
runpy.run_path(str(ROOT/'audit_patterns.py'))
audit=json.loads((ROOT/'sources'/'systematic_audit.json').read_text())
lib=runpy.run_path(str(ROOT/'build_handbook.py'))
old=(ROOT/'Rebuttal实战手册.html').read_text()
(ROOT/'Rebuttal实战手册_第一版备份.html').write_text(old)
md,esc=lib['md'],lib['esc']
notes,forums=lib['notes'],lib['forums']
topics=[('overview','先看全周期',None),('initial','逐条回复的共性格式','initial'),('general','General Response 的共性骨架','general'),('followup','跟进与提分后回复','followup'),('reminders','催 reviewer 与请 AC 协调','reminder'),('summary','Summary 的共性骨架','summary'),('reports','反馈问题与举报的共性格式','report'),('recommend','自信推荐与决定后回应',None),('novelty','回应 novelty 质疑的共性套路','novelty'),('human','人味表达与自信邀请',None),('formatting','重点标注与组合格式',None)]
content=(ROOT/'共性阶段写作拆解.md').read_text()
sections={a:b for a,b in re.findall(r'^## ([^\n]+)\n(.*?)(?=^## |\Z)',content,re.M|re.S)}
supplement={a:b for a,b in re.findall(r'^## ([^\n]+)\n(.*?)(?=^## |\Z)',(ROOT/'技术与跟进套路补全.md').read_text(),re.M|re.S)}
shotids={
('LoRAM','general'):'PTFataqOVS',('FloE','general'):'Yq7RSYACyP',('LVSpec','general'):'oyZOtIyQda',('LVLMSurvey','general'):'f7Q0oRBCoF',('HybridKV','general'):'eoLnTsSl9a',
('LoRAM','summary'):'LOqBNMH4rT',('FloE','summary'):'Yq7RSYACyP',('LVSpec','summary'):'cFiTQe4Qzv',('LVLMSurvey','summary'):'hTxjH5dpzj',('HybridKV','summary'):'ExRPio1aqV',
('LoRAM','initial'):'gTCmz3GdfG',('FloE','initial'):'N798t55dFZ',('HybridKV','initial'):'1aQJexXi8Z',('LoRAM','followup'):'p286v6AOeJ',('HybridKV','followup'):'fvJp5PEkq3',
('LoRAM','reminder'):'f9IQX7Q7jk',('LVLMSurvey','reminder'):'qTn9iPv6n3',('LVSpec','reminder'):'X9AWIlsrAl',('LoRAM','ac'):'tADNgyR0Fh',('LVLMSurvey','ac'):'g4B5ttNFK4',('FloE','ac'):'gmurpB5fE0',
('LVSpec','report'):'71IfCXBEhd',('LVLMSurvey','report'):'Y3lcL4XJgx',('LoRAM','strengths-R4'):'0nttRrpLqp',('LoRAM','strengths-R5'):'0cPZuYx5ct'}
additional=json.loads((ROOT/'screenshots'/'additional_manifest.json').read_text())
for shot in additional:shotids[(shot['paper'],shot['group'])]=shot['id']
def uri(file):return 'data:image/jpeg;base64,'+base64.b64encode(file.read_bytes()).decode()
def gallery(group,papers=None):
    cards=[]
    for paper in forums:
        if papers and paper not in papers:continue
        file=ROOT/'screenshots'/f'{paper}-{group}.jpg'
        if not file.exists():continue
        nid=shotids[(paper,group)];n=next(n for n in notes[paper] if n['id']==nid)
        url=f'https://openreview.net/forum?id={forums[paper]}&noteId={nid}'
        cards.append(f'<figure><figcaption><b>{paper}</b> <a href="{url}" target="_blank" rel="noreferrer">原帖</a><br><span>{esc(n["title"])}</span></figcaption><button class="shot" aria-label="放大 {paper} {group} 截图"><img loading="lazy" src="{uri(file)}" alt="{esc(paper+" "+n["title"]+" 原帖截图")}"></button><p class="shotnote">浏览器原帖截图，点击放大；长帖为顶部摘录。</p></figure>')
    return '<div class="gallery">'+''.join(cards)+'</div>'

extra='''
body{background:#f7f8fb}.chapter{display:none;border:0;padding:20px 0 70px}.chapter.active{display:block}body.continuous .chapter{display:block}main{max-width:1500px;padding-top:20px}header{padding:12px 0 20px}h1{font-size:38px;letter-spacing:-1px;margin:15px 0;max-width:none}.lead{font-size:17px;margin:12px 0}h2{font-size:30px}h3{padding-top:24px;border-top:1px solid var(--line);margin-top:34px}.chapter>p{max-width:900px}aside{width:250px;background:#e9ecf5}main{margin-left:250px}nav a{padding:8px 7px;border:0;border-radius:5px;font-size:13px}nav a.selected{background:#5143a5;color:white}.chapter-title{display:flex;gap:18px;align-items:baseline}.chapter-title .step{font-size:32px;color:#8376be}.chapter-title h2{margin-top:12px}.gallery{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin:18px 0 28px}figure{margin:0;border:1px solid var(--line);background:white;border-radius:8px;overflow:hidden}figcaption{padding:12px 16px;background:#edf0f7;font-size:14px;line-height:1.6}figcaption span{font-size:12px;color:var(--muted)}figcaption a{float:right}.shot{display:block;width:100%;padding:0;border:0;border-radius:0;height:250px;overflow:auto;text-align:left}.shot img{display:block;width:100%;height:auto}.shotnote{padding:0 15px;font-size:12px;color:var(--muted);margin:8px 0}.gallery-heading{margin-top:24px;font-size:17px;font-weight:650}.template{background:#edf2f7;border:1px solid #d8e1eb}.copy{position:relative}.localnav{display:flex;flex-wrap:wrap;gap:8px;padding:12px 0;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:3;background:#f7f8fb}.localnav a{font-size:12px;padding:4px 9px;background:white;border:1px solid var(--line);border-radius:5px;text-decoration:none}.source-chain{border-left:4px solid #8679bd;background:#eeebf9;padding:20px;margin:18px 0}.source-chain small{display:block;color:#626a82}.source-chain q{font-family:Georgia,serif;display:block;margin:10px 0;font-size:18px}.source-chain .rewrite{color:#276f66;font-size:17px}.introbar{padding:14px 18px;background:#e8f2ee;border-left:4px solid #287a6a;font-size:14px}.more{margin-top:25px}.more summary{color:#5143a5}dialog{width:min(1500px,96vw);max-height:94vh;padding:48px 12px 12px;border:0;border-radius:8px;background:#eef1f7}dialog::backdrop{background:#161c36b8}dialog img{display:block;width:100%;height:auto}dialog button{position:fixed;right:4vw;top:4vh;z-index:10;background:white}.bottomnav{display:flex;justify-content:space-between;margin-top:35px}.controls{margin-top:15px}.manual{font-size:12px}.phrase-source{font-size:12px;color:#696279}.chapter pre{font-size:14px}.chapter td:first-child{min-width:100px}.statusbar{font-size:12px;color:#626a82}.continuous header{display:block} @media(max-width:850px){main{margin-left:0}aside{width:auto}.gallery{grid-template-columns:1fr}.shot{height:280px}h1{font-size:30px}.localnav{position:static}nav{gap:6px}nav a{font-size:12px}}@media print{.chapter{display:block!important}.gallery{grid-template-columns:1fr 1fr}.shot{height:auto;overflow:visible}.localnav,.bottomnav{display:none}.gallery img{max-height:none}header{display:block}main{margin:0}}
'''
extra += '''.chapter code{color:#a32921;background:#f4eaea}.chapter em{font-style:italic}.chapter strong code{font-weight:700}
.stage-tabs{display:flex;gap:8px;flex-wrap:wrap;margin:18px 0 25px;position:sticky;top:0;background:#f7f8fb;padding:10px 0;z-index:4;border-bottom:1px solid var(--line)}.stage-tabs button[aria-selected=true]{background:#5143a5;color:white;border-color:#5143a5}.stage-panel[hidden]{display:none!important}.pattern-card{background:white;border:1px solid var(--line);padding:20px 23px;margin:15px 0;border-radius:8px}.pattern-card h4{margin:0 0 10px}.pattern-card blockquote{font-family:Georgia,serif;font-size:18px;line-height:1.65;margin:14px 0}.source-badges{display:flex;gap:6px;flex-wrap:wrap;font-size:12px}.source-badges a{background:#edf0f8;border-radius:4px;padding:2px 7px;text-decoration:none}.pattern-card .pattern-kind{font-size:12px;color:#4e4093}.pattern-card details{background:#fafbfe;font-size:13px}.expression-filter{width:100%;padding:11px;border:1px solid var(--line);border-radius:6px}.stage-corpus-note{background:#e9f2ee;padding:15px 20px;font-size:14px;border-left:4px solid #287a6a}.origin{font-size:12px;color:#6b628c}.scope-count{font-size:12px;color:#626a82}.overview-facts{display:flex;gap:12px;flex-wrap:wrap;margin:18px 0}.overview-facts span{padding:10px 18px;background:white;border:1px solid var(--line);border-radius:7px}nav .navlabel{font-size:12px;color:#69718a;margin-top:15px}.shotcount{font-size:13px;color:#626a82}.tpl-label{margin:24px 0 8px;font-size:17px;font-weight:600}.skeleton-box{margin:18px 0;padding:20px 23px;background:white;border:1px solid var(--line)}.source-toc{display:flex;gap:6px;flex-wrap:wrap;margin:15px 0}.source-toc a{padding:3px 8px;background:#edf0f7;text-decoration:none;font-size:12px}.copy-original{font-size:12px;float:right;padding:3px 8px}@media print{.stage-tabs{display:none}.stage-panel[hidden]{display:block!important}.pattern-card{break-inside:avoid}.expression-filter{display:none}}
'''
parts=['<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Rebuttal 全周期写作手册 · 同阶段截图与共性模板</title><style>'+lib['css']+extra+'</style><body>']
navitems=[(i,t) for i,t,_ in topics]+[('appendix','附录：模板与完整档案')]
navhtml=''
for i,t in navitems:
 if i=='overview':navhtml+='<div class="navlabel">全周期</div>'
 if i=='novelty':navhtml+='<div class="navlabel">贯穿各阶段的写作工具</div>'
 navhtml+=f'<a href="#{i}">{t}</a>'
parts.append('<aside><b>Rebuttal 写作手册</b><p>原句有出处，模板按阶段</p><nav>'+navhtml+'</nav><div class="controls"><button id="viewmode">连续阅读</button><button onclick="window.print()">打印 / PDF</button></div><p class="manual">左右方向键切换阶段。<br>每阶段含骨架、截图、原句和模板。<br>截图可放大，文字可复制。</p><p class="statusbar" id="position"></p></aside><main><header><h1>Rebuttal 全周期写作手册</h1><p class="lead">从五篇原帖提炼：什么时候写、按什么顺序写、怎样强调、怎样说得自然而自信</p><p class="small">LoRAM / FloE / LVSpec / LVLM Survey / HybridKV · 系统复核版</p></header>')

def source_cards(sid):
    selected=[p for p in audit['patterns'] if p['stage']==sid]
    if sid=='human':selected=[p for p in audit['patterns'] if any(x in p['quote'].lower() for x in ['happy','welcome','excited','delighted','recommend','proud','feedback has','early experiments','further explanations','share the results'])]
    if sid=='formatting':return formatting_examples()
    if not selected:return '<p>本节为阶段说明与派生模板；当前语料未据此标成五篇共同原句。</p>'
    out=['<p class="stage-corpus-note">下面均为作者原帖片段。跨篇范围按本次可读作者帖中的字面匹配统计（合并空白、忽略大小写），近义表达不合并计算；点击出处可核对完整上下文。</p><input class="expression-filter" aria-label="筛选本阶段原句" placeholder="筛选本阶段：句式、功能、论文名称">']
    for k,p in enumerate(selected):
        hits=p['hits'];kind='跨篇重复' if len(p['papers'])>1 else ('同篇复用' if len(hits)>1 else '单篇特色')
        badge_hits=[next(h for h in hits if h['paper']==paper) for paper in p['papers']]
        badge_hits += [h for h in hits if h not in badge_hits][:max(0,8-len(badge_hits))]
        out.append(f'<article class="pattern-card"><button class="copy-original">复制原句</button><div class="pattern-kind">{kind} · {len(p["papers"])} 篇 / {len(hits)} 个作者帖</div><h4>{esc(p["label"])}</h4><blockquote class="original-quote">{esc(p["quote"])}</blockquote><p>{esc(p["use"])}</p><div class="source-badges">'+''.join(f'<a href="{h["url"]}" target="_blank" rel="noreferrer">{h["paper"]} · 原帖</a>' for h in badge_hits)+'</div><details><summary>原帖上下文与模板替换</summary>')
        for h in hits[:2]:out.append(f'<p class="origin">{esc(h["paper"])} / {esc(h["title"])}</p><div class="raw">{esc(h["context"])}</div>')
        out.append('<p class="origin">派生模板，非原帖逐字引文</p><div class="template"><button class="copy">复制模板</button><pre>'+esc(p['template'])+'</pre></div></details></article>')
    return ''.join(out)

def formatting_examples():
    fa=json.loads((ROOT/'sources'/'formatting_audit.json').read_text())
    choices=[('LoRAM','PTFataqOVS','General Response 的评价与来源'),('HybridKV','ExRPio1aqV','Summary 的结论、评分与回复定位'),('HybridKV','uJyQ8V8HPs','超参回复的原问题、机制与参数表')]
    out=['<p>以下标记直接来自已登录网页的实际 strong / em / code 元素，不根据纯文本推测排版。截图中可查看它们所在的段落。</p>']
    for paper,nid,title in choices:
        entry=next(n for x in fa if x['paper']==paper for n in x['notes'] if n['id']==nid)
        marks=[m for m in entry['marks'] if m['text']!='Comment:'][:18]
        out.append('<h3>'+esc(paper+' · '+title)+'</h3><div class="tablewrap"><table><tr><td>实际格式</td><td>原帖标注内容</td></tr>')
        for m in marks:
            tag=m['tag'].lower();out.append('<tr><td>'+esc(tag+('，外层 '+m['parent'].lower() if m['parent'] in ['STRONG','EM'] else ''))+'</td><td><'+tag+'>'+esc(m['text'])+'</'+tag+'></td></tr>')
        out.append('</table></div>')
    return ''.join(out)

def screenshot_panel(sid,group):
    out=[]
    if group:out.append(gallery(group))
    if sid=='general':out.extend(['<h3>优点段的上游：审稿人原话</h3><p>先摘录 review 的肯定，再按研究意义、方法、实验、兼容性和写作归类；转述保留具体 reviewer 归属。</p>',gallery('strengths-R4'),gallery('strengths-R5')])
    extras={'initial':['tradeoff','already-considered','specific-revision','scope-fallback','venue-fit'],'novelty':['novelty-related'],'human':['code-invitation','already-considered'],'followup':['dated-update','code-invitation'],'reminders':['ac','last-hours','missing-review'],'formatting':[]}
    if sid=='formatting':out.extend([gallery('general',['LoRAM']),gallery('summary',['HybridKV'])])
    for g in extras.get(sid,[]):out.append(gallery(g))
    return '<p>同阶段或同功能的原帖放在一起。点击截图放大；标题链接回对应 note。长帖为截图顶部节选，完整内容仍可在出处查阅。</p>'+''.join(out) if out else '<p>本节为总体路线或派生阶段说明；相关原帖截图位于对应的逐条回复、跟进和 Summary 阶段。</p>'

for idx,(sid,title,group) in enumerate(topics):
    body=sections[title]+('\n'+supplement[sid] if sid in supplement else '')
    intro,sep,rest=body.partition('### ')
    parts.append(f'<section class="chapter" id="{sid}"><div class="chapter-title"><span class="step">{idx+1:02}</span><h2>{title}</h2></div>')
    if sid!='overview':
        introfirst=intro.strip().split('\n\n')[0]
        parts.append(md(introfirst))
        parts.append('<div class="stage-tabs" role="tablist" aria-label="本阶段内容">'+''.join(f'<button role="tab" aria-selected="{str(k==0).lower()}" data-panel="{key}">{label}</button>' for k,(key,label) in enumerate([('structure','写作骨架'),('screens','截图对照'),('originals','原句提取'),('ready','直接套用')]))+'</div>')
        prose=re.sub(r'```[^\n]*\n.*?```','\n',body,flags=re.S)
        prose=prose.replace(introfirst,'',1)
        prose=re.sub(r'(^### [^\n]+\n)\s*(?=### |\Z)','',prose,flags=re.M)
        parts.append('<div class="stage-panel" data-panel="structure">'+md(prose)+'</div>')
        parts.append('<div class="stage-panel" data-panel="screens" hidden>'+screenshot_panel(sid,group)+'</div>')
        parts.append('<div class="stage-panel" data-panel="originals" hidden>'+source_cards(sid)+'</div>')
        tpl=[]
        for m in re.finditer(r'```[^\n]*\n(.*?)```',body,re.S):
            heads=re.findall(r'^### ([^\n]+)',body[:m.start()],re.M)
            tpl.append('<div class="tpl-label">'+esc(heads[-1] if heads else title)+'</div><div class="template"><button class="copy">复制模板</button><pre>'+esc(m[1].rstrip())+'</pre></div>')
        parts.append('<div class="stage-panel" data-panel="ready" hidden><p class="stage-corpus-note">这些是从本节原句和论证顺序整理的可替换模板；方括号填写你论文的真实信息。原帖逐字片段请看“原句提取”。</p>'+(''.join(tpl) or '<p>本节的格式示例和结构表可直接参考；对应英文模板位于逐条回复、跟进和 Summary。</p>')+'</div>')
    else:parts.append(md(intro))
    if sid=='overview':
        parts.append('<div class="overview-facts"><span>5 篇原始讨论</span><span>104 条可读作者帖</span><span>69 条可追溯原句条目</span></div><div class="introbar">每个阶段固定四个入口：写作骨架、截图对照、原句提取、直接套用。优点段摘录 review 的认可；贡献主张与 reviewer 反馈分别归属。正文保留你的固定句式，包括五篇 Summary 共用的祝福收尾。</div>')
        # overview has no ###, so content already rendered; add stage shortcuts.
        parts.append('<div class="route">'+''.join(f'<a href="#{i}"><strong>{t}</strong>截图、结构、表达、模板</a>' for i,t,_ in topics[1:])+'</div>')
    if False and group:
        parts.append('<div class="gallery-heading">同阶段原帖截图对照</div>'+gallery(group))
    if False and sid=='formatting':parts.append('<div class="gallery-heading">直接对照原帖的加粗、斜体与彩色定位</div>'+gallery('general',['LoRAM'])+gallery('summary',['HybridKV']))
    if False and sid=='reminders':parts.append('<div class="gallery-heading">请 AC 协调的原帖截图</div>'+gallery('ac'))
    if sid=='overview' and sep:parts.append(md('### '+rest))
    if False and sid=='general':
        # Add a traceable demonstration rather than an invented positive claim.
        parts.append('<h3>对照审稿人的原话看“优点段”怎么生成</h3>'+gallery('strengths-R4')+gallery('strengths-R5'))
        chains=[('R5 / BSMa','Memory efficient training is an important topic in LLM-related fields.','研究意义','We appreciate the recognition of the importance of memory-efficient LLM training (R5).'),('R5 / BSMa','This paper proposes an easy but effective method to reduce the number of parameters which need to be finetuned.','方法简洁有效','We are grateful for the acknowledgment of our method’s simplicity and effectiveness (R5).'),('R4 / H1mX','The proposed method is complementary with other memory reduction techniques such as quantization and pruning strategies.','兼容性','The method’s compatibility with quantization and pruning strategies was also recognized (R4).')]
        for reviewer,quote,theme,rewrite in chains:
            # Verify each original against the actual captured review text.
            assert any(quote in (n['body'] or '') for n in notes['LoRAM']),quote
            parts.append(f'<div class="source-chain"><small>Review 原话 · LoRAM {reviewer}</small><q>{esc(quote)}</q><b>归类：{theme}</b><p class="rewrite">{esc(rewrite)}</p><small>上面英文为推荐转述，非原帖逐字引用；保留具体 R 归属。</small></div>')
    if False and sid=='summary':
        parts.append('<h3>从截图中提取的原句</h3>')
        phrases=[('HybridKV','ExRPio1aqV','We sincerely thank the Area Chairs for their diligent oversight of the review process, which has greatly contributed to a thorough and constructive discussion of our submission.','感谢 AC 的投入和主持'),('HybridKV','ExRPio1aqV','Given that we have diligently addressed all stated weaknesses, we respectfully submit that the quality of our manuscript merits a further positive assessment.','以已完成的回应为依据，主动争取正面评价'),('LoRAM','LOqBNMH4rT','We are grateful that the majority of reviewers (three) raised their ratings, reflecting their positive assessment and high confidence in the manuscript (Rating: 8, 8, 6 & Confidence: 5, 4, 4).','记录明确提分与评分归属')]
        for p,nid,q,role in phrases:
            n=next(n for n in notes[p] if n['id']==nid);assert q in n['body']
            parts.append(f'<div class="source-chain"><small>{p} 原帖 · {role}</small><q>{esc(q)}</q></div>')
    parts.append('<div class="bottomnav"><button class="previous">上一阶段</button><button class="next">下一阶段</button></div></section>')

def oldsection(sid):
    return re.search(r'<section class="chapter" id="'+sid+r'">(.*?)</section>',old,re.S)[1]
parts.append('<section class="chapter" id="appendix"><h2>附录：按需展开</h2><p>主线按阶段直接使用。这里保留第一版的完整资料，便于深入核对。</p>')
parts.append('<details class="more"><summary>本次逐帖复核范围与原句统计口径</summary><p>共 145 条记录：104 条可读作者帖、40 条审稿人与 chairs 的上下文记录、1 条已删除作者帖。仅核对目前可见版本，不把已删除内容或历史修改补写为原文。69 条是精选原句条目，部分功能互有关联，不代表 69 个互不重叠的套路。跨篇计数按字面匹配，不把同义改写合并。</p><div class="tablewrap"><table><tr><th>论文</th><th>全部记录</th><th>可读作者帖</th></tr>'+''.join('<tr><td>'+esc(p)+'</td><td>'+str(v['notes'])+'</td><td>'+str(v['available_author_notes'])+'</td></tr>' for p,v in audit['papers'].items())+'</table></div><p>原帖的 Readers 在附录档案中逐帖保留。不同年份、不同会场与阶段的入口权限不能互相套用。HybridKV 使用有完整讨论的 ARR 原始论坛 jFuN2yI2D7。</p><a href="sources/systematic_audit.json">逐帖索引、原句命中出处与内容校验值</a></details>')
for title,sid in [('12 类补充模板，包括迟到评审与程序申诉','templates'),('更多自然、自信与投诉表达','phrases'),('15 个技术案例的深入解读','cases'),('入口、Readers 与年份规则','visibility'),('145 条原帖全文搜索','archive')]:
    parts.append('<details class="more"><summary>'+title+'</summary>'+oldsection(sid)+'</details>')
parts.append('</section><footer>截图采自 Jun Zhang 登录会话中的 OpenReview 原帖，保留原始排版；长技术帖仅展示顶部，正文与原帖链接可在附录核对。<br>档案含作者与 chairs 可见内容，按实际分享范围选用。所有图片已嵌入 HTML，可离线打开。<br><a href="共性阶段写作拆解.md">下载共性写作骨架 Markdown</a></footer></main><dialog id="zoom"><button id="closezoom">关闭截图 ×</button><img id="zoomimage" alt="原帖放大截图"></dialog><div class="toast" role="status" id="toast"></div>')
archive=re.search(r'<script id="archive-data".*?</script>',old,re.S)[0]
parts.append(archive)
parts.append('''<script>
const chapters=[...document.querySelectorAll('.chapter')];let current=0;
function select(i,scroll=true){current=(i+chapters.length)%chapters.length;chapters.forEach((x,k)=>x.classList.toggle('active',k===current));document.querySelectorAll('nav a').forEach(a=>a.classList.toggle('selected',a.hash==='#'+chapters[current].id));document.getElementById('position').textContent=(current+1)+' / '+chapters.length;if(scroll&&!document.body.classList.contains('continuous'))window.scrollTo({top:0,behavior:'instant'})}
function hashchange(){let key=location.hash.slice(1);let i=chapters.findIndex(c=>c.id===key);select(i<0?0:i)}window.addEventListener('hashchange',hashchange);hashchange();
document.querySelectorAll('a[href^="#"]').forEach(a=>a.addEventListener('click',()=>{let i=chapters.findIndex(c=>'#'+c.id===a.hash);if(i>=0)select(i)}));
document.querySelectorAll('.previous').forEach(b=>b.onclick=()=>location.hash=chapters[(current-1+chapters.length)%chapters.length].id);document.querySelectorAll('.next').forEach(b=>b.onclick=()=>location.hash=chapters[(current+1)%chapters.length].id);
document.getElementById('viewmode').onclick=e=>{let enabled=document.body.classList.toggle('continuous');e.target.textContent=enabled?'按阶段阅读':'连续阅读';select(current)};
document.addEventListener('keydown',e=>{if(/INPUT|TEXTAREA|SELECT/.test(e.target.tagName)||document.getElementById('zoom').open)return;if(e.key==='ArrowRight')location.hash=chapters[(current+1)%chapters.length].id;if(e.key==='ArrowLeft')location.hash=chapters[(current-1+chapters.length)%chapters.length].id});
document.querySelectorAll('.shot').forEach(b=>b.onclick=()=>{document.getElementById('zoomimage').src=b.querySelector('img').src;document.getElementById('zoom').showModal()});document.getElementById('closezoom').onclick=()=>document.getElementById('zoom').close();
function toast(t){let e=document.getElementById('toast');e.textContent=t;e.style.display='block';setTimeout(()=>e.style.display='none',1800)}
document.querySelectorAll('.stage-tabs').forEach(t=>t.querySelectorAll('button').forEach(b=>b.onclick=()=>{t.querySelectorAll('button').forEach(x=>x.setAttribute('aria-selected',String(x===b)));t.closest('.chapter').querySelectorAll('.stage-panel').forEach(x=>x.hidden=x.dataset.panel!==b.dataset.panel)}));
document.querySelectorAll('.expression-filter').forEach(i=>i.oninput=()=>i.parentElement.querySelectorAll('.pattern-card').forEach(c=>c.hidden=!c.textContent.toLowerCase().includes(i.value.toLowerCase())));
document.querySelectorAll('.copy-original').forEach(b=>b.onclick=async()=>{let el=b.closest('.pattern-card').querySelector('.original-quote');try{await navigator.clipboard.writeText(el.textContent);toast('已复制原句')}catch{let s=getSelection(),r=document.createRange();r.selectNodeContents(el);s.removeAllRanges();s.addRange(r);toast('已选中，请按 Ctrl/Cmd+C')}});
document.querySelectorAll('.copy').forEach(b=>b.onclick=async()=>{let pre=b.parentElement.querySelector('pre');try{await navigator.clipboard.writeText(pre.textContent);toast('已复制模板')}catch{let s=getSelection(),r=document.createRange();r.selectNodeContents(pre);s.removeAllRanges();s.addRange(r);toast('已选中，请按 Ctrl/Cmd+C')}});
const all=JSON.parse(document.getElementById('archive-data').textContent),escape=s=>(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function render(){let q=document.getElementById('search').value.toLowerCase(),p=document.getElementById('paper').value;let arr=all.filter(n=>(!p||n.paper===p)&&(!q||[n.title,n.meta,n.body,n.paper].join(' ').toLowerCase().includes(q)));document.getElementById('results').textContent=arr.length+' / '+all.length+' 条帖子';document.getElementById('notes').innerHTML=arr.map(n=>'<details><summary>'+escape(n.paper+' / '+n.title)+'</summary><p class="meta">'+escape(n.meta)+'</p><a target="_blank" rel="noreferrer" href="https://openreview.net/forum?id='+n.forum+'&noteId='+n.id+'">在线原帖</a><div class="raw">'+escape(n.body)+'</div></details>').join('')};document.getElementById('search').oninput=render;document.getElementById('paper').onchange=render;render();
</script></body></html>''')
(ROOT/'Rebuttal实战手册.html').write_text('\n'.join(parts))
print('V2 built:',len(shotids),'source screenshot references;',len(re.findall(r'class="copy"',''.join(parts))),'copy buttons (including repeated templates)')
