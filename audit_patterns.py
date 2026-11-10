"""Trace every extracted expression back to the captured author posts."""
from pathlib import Path
import json,re,hashlib,collections
ROOT=Path(__file__).parent
PAPERS=['LoRAM','FloE','LVSpec','LVLMSurvey','HybridKV']
FORUMS=dict(zip(PAPERS,['s7DkcgpRxL','i5aHAkkhJH','xyXsaQEmCu','wvlizZdYc1','jFuN2yI2D7']))
def norm(s):return re.sub(r'\s+',' ',s or '').strip()
def phase(n):
 t=n['title'].lower();m=n['meta'] or ''
 if not re.search(r'by\s*Authors',m):return '评审与 chairs 的上下文'
 if '[Deleted]' in (n['body'] or ''):return '已删除的作者帖'
 if 'general response' in t and 'summary' in t:return 'General Response 与 Summary 合并'
 if 'general response' in t:return 'General Response'
 if 'summary of the discussion' in t:return 'Summary'
 if 'report' in t or 'formal feedback' in t:return '评审问题反馈与报告'
 if 'confidential' in m and 'last day' in t:return '请 AC 协调'
 if 'area chair' in t or 'author ac confidential' in m.lower():return '请 AC 协调'
 if 'deadline' in t:return '提醒与最后一轮跟进'
 if 'follow' in t or 'reply rebuttal' in t:return '后续讨论与感谢'
 if 'sum up' in t:return '面向 reviewer 的阶段小结'
 return '逐条技术回复'
allnotes=[];authors=[]
for p in PAPERS:
 for n in json.loads((ROOT/'sources'/f'{p}.json').read_text()):
  d=dict(n,paper=p,phase=phase(n),url=f'https://openreview.net/forum?id={FORUMS[p]}&noteId={n["id"]}',sha256=hashlib.sha256((n['body'] or '').encode()).hexdigest())
  allnotes.append(d)
  if re.search(r'by\s*Authors',n['meta'] or '') and '[Deleted]' not in (n['body'] or ''):authors.append(d)

# quote is always a literal excerpt, not a rewritten template.
# Each proposed template is separately labeled in the viewer.
rows=[
('initial','将一问拆成几个子问题','We address the question in three parts for clarity:','We address this question in [N] parts for clarity: [subquestions].','先列子问题，再按相同顺序逐项回答。'),
('initial','主动给回答路线','We will address this in two parts:','We address this in two parts: first, [A]; second, [B].','让 reviewer 在读论证前先知道回答路径。'),
('initial','从实际使用场景解释比较','Our comparison reflects practical use cases where resource constraints often guide model selection.','Our comparison reflects [target use case], where users choose between [A] and [B] under [constraint].','先解释要帮助谁作什么决策，再交代 baseline。'),
('initial','直接承认性能上界','Certainly, LoRAM is designed to trade some performance for significant memory reduction','Certainly, [method] trades [cost/quality] for [benefit] under [setting].','不回避单项劣势，转入本文要解决的约束。'),
('initial','不寻找普遍最优参数','We did not seek a universally optimal parameter reduction ratio; this choice fundamentally depends on user-specific memory constraints.','We do not seek a universally optimal [parameter]; the choice depends on [user constraint].','说明选择准则，避免把特定设置称为普适最优。'),
('initial','肯定比较的必要性','Comparing with smaller non-compressed models is indeed crucial.','Comparing with [baseline] is indeed important for assessing [claim].','承认具体评价需求，而非只写泛泛感谢。'),
('initial','说明约束并给替代方案','due to time and resource constraints, we were unable to distill smaller models','Due to [constraint], we could not reliably evaluate [X]. We instead provide [Y], which addresses [part of the question].','资源限制后面接可执行的证据；替代方案不冒充原实验。'),
('initial','解释合理的质量速度权衡','this slight trade-off in latency for a considerable gain in accuracy is well-justified and acceptable','For [target scenario], the trade-off of [cost] for [benefit] is justified by [evidence].','把优劣势放在同一 operating point 上比较。'),
('initial','先讲机制再给观测','Our analysis, combining both theoretical analysis and empirical results','We explain [effect] through [mechanism], then evaluate it using [measurement].','机制解释与实测结果分栏，形成可查证链条。'),
('initial','早在设计阶段做过','we have conducted early experiments during the method design stage','We explored this during method design and compared [A] with [B].','区分设计时研究、原稿报告与本轮补充的时间。'),
('initial','原文已有，愿意再说明','We are happy to provide further explanations below.','This is discussed in [original location]. We are happy to explain the reasoning here.','指向原稿后，在当前帖子把答案重述清楚。'),
('initial','乐意补上所需结果','We are happy to provide additional results for more choices of N','We are happy to provide additional results for [settings], as shown in [table].','表达配合并立刻给出具体证据。'),
('initial','承认范围与可迁移原则','Transferable Innovation.','Our current implementation is designed for [scope]; the transferable principle is [X].','分开当前可用范围与未来可迁移的想法。'),
('initial','解释合理局限','We acknowledge that a task-adaptive threshold could potentially further improve performance.','We acknowledge that [extension] could improve [aspect]. Our current design prioritizes [constraint].','承认进一步可能性，并说明当前设计取舍。'),
('initial','给 corner case 的修正路径','a simple fallback to strict verification can be used to avoid performance degradation','When [failure condition] occurs, [fallback] can be used; [state whether it has been evaluated].','区分已验证 fallback 与潜在改进。'),
('initial','给出修改前后的具体措辞','we will revise "effectively salvaging rejected mismatches into valid semantic equivalents"','We will revise “[old wording]” to “[new wording]” in [location].','使呈现修改一眼可核对。'),
('initial','承诺把分析放进正文','We will add this comprehensive analysis to Section 4.3.','We will add [analysis/results] to [specific section].','不只说会改进，写明加什么、放哪里。'),
('initial','承认并修正 typo','We have corrected the typo in Table 3','We have corrected [error] to [correction] in [location].','小问题简明处理，状态如实。'),
('initial','感谢带来更好的定位','which helps us to better frame the contributions and future potential of our work','Thank you for this suggestion, which helps us clarify [specific aspect].','感谢说明对方建议具体怎样改善论文。'),
('novelty','重新组织创新的评价维度','While novelty is a multifaceted concept in academic research','We clarify our contribution along two dimensions: [empirical finding] and [technical mechanism].','之后迅速落到本文证据，不停留在一般性定义。'),
('novelty','创新不是组件本身','Our core innovation, however, is not a new compression primitive','Our core innovation lies in [new principle/framework], while [component] builds on existing work.','承认组件复用，准确定位贡献层次。'),
('novelty','区别研究粒度和对象','Distinct Scope and Granularity','The distinction lies in [scope] and [granularity]: [precise comparison].','把 related work 拉到相同轴上比较。'),
('novelty','承认互补并说明结合方式','We consider these techniques orthogonal and complementary to our work.','These techniques are complementary: [concrete integration].','互补必须紧跟实际可如何结合。'),
('novelty','肯定简单设计的价值','We intentionally keep the method as simple as possible','We intentionally keep the design simple, enabling [practical benefit] with [evidence].','将简单与效果、可用性、部署成本相连。'),
('general','稳定映射 Reviewer 编号','For clarity','For clarity, we refer to Reviewers [IDs] as [R labels], respectively.','全文使用同一套 ID 映射。'),
('general','先表达受到认可的鼓舞','We are encouraged by their recognition of the key contributions and strengths of our work.','We are encouraged by the reviewers’ recognition of [specific strengths].','下一段逐项对应 review 原话及 R 编号。'),
('general','从认可转到更新','We have carefully addressed each individual comment provided by the reviewers.','We have responded to each comment. Below, we summarize [contributions], [experiments], and [clarifications].','这是认可段与更新目录之间的过渡。'),
('general','贡献栏目','Core Contributions of Our Work','Core Contributions of Our Work\n1. [Finding]\n2. [Mechanism]\n3. [Validation]','分清已有贡献与本轮新增回应。'),
('general','争取正面评价','We look forward to the reviewers\' favorable consideration.','We look forward to the reviewers’ favorable consideration.','正面但不替 reviewer 宣布立场。'),
('followup','带日期的增量更新','Update 11.23 (Peformance of Domain-Specific Task):','Update [date] — [topic]\n[What is new, main result, and location].','保留原帖旧拼写用于核对；模板标题应改正拼写。'),
('followup','分享新结果的兴奋感','We are excited to share','We are excited to share [specific completed result].','轻松语气后立刻给设置和结果。'),
('followup','分享可执行代码','We are delighted to share that an anonymous version of the LoRAM execution code has been uploaded','We are delighted to share that [available implementation] is now provided in [permitted location].','只报告已上传、可访问的实现。'),
('followup','欢迎合适用户采用','LoRAM is definitely worth recommending!','For [users] facing [constraint], [method] is worth considering because [evidence].','推荐面向明确受众，并与实证相连。'),
('followup','欢迎反馈与使用交流','Your feedback and suggestions are always welcome','Your feedback and suggestions are always welcome.','邀请反馈自然地接在代码/部署讨论之后。'),
('followup','愿意为呈现做调整','we would be more than happy to make adjustments','We would be more than happy to make [specific adjustments].','欢迎具体改进意见，同时保持技术判断。'),
('followup','提分后仍愿继续交流','we are willing to continue the discussion','We are willing to continue the discussion if [specific concern] remains unclear.','感谢支持后仍保留技术对话空间。'),
('followup','感谢修改后的评价','Thank you for your updated evaluation and for raising the score','Thank you for the updated assessment and for your constructive suggestions.','把感谢与已落实的修改相连。'),
('reminders','礼貌接续对话','We hope this message finds you well.','We hope this message finds you well.','你的常用开头；可按篇幅保留。'),
('reminders','指出反馈时间窗口','With the discussion deadline approaching','With the discussion closing on [exact deadline], we welcome feedback on [point].','统一标题与正文的日期和时区。'),
('reminders','邀请继续指出问题','Please feel free to share any thoughts you may have.','Please feel free to share any remaining questions about [issue].','给对方继续参与的入口。'),
('reminders','有交流感的收尾','Looking forward to hearing from you!','Looking forward to hearing from you!','与你的 Best regards / Authors 搭配。'),
('reminders','最后一轮先列更新','We have meticulously resolved the points you raised through the following strategic updates:','We summarize our responses to your concerns as follows: [items].','将作者已做工作与 reviewer 是否认可分开。'),
('reminders','有条件地请求更新评价','we kindly invite you to consider re-evaluating and updating your score','If our response resolves [concern], we invite you to update your assessment accordingly.','以 concern 是否解决为条件，不指定分数。'),
('reminders','先体谅 chairs 的组织难度','We fully understand the difficulty of recruiting a sufficient number of reviewers within a limited timeframe.','We appreciate the difficulty of [specific coordination task].','不是泛泛恭维，紧接具体缺 review 的事实。'),
('reminders','请求补足评审','only one review is available until now','At present, [N] review(s) are available. Could you advise on [additional review / response window]?','缺评审与已有评审不回帖是两种不同情况。'),
('reminders','请 AC 鼓励参与','encouraging their participation in the discussion phase','We would appreciate your assistance in inviting feedback from [reviewer] on [issue].','日期、线程、请求三个元素写全。'),
('summary','固定感谢 AC','We sincerely thank the Area Chairs for their diligent oversight','We sincerely thank the Area Chairs for overseeing the review process.','你的 Summary 稳定开头，之后进入具体状态。'),
('summary','记录提分','raised their ratings','Reviewers [IDs] explicitly [raised their ratings / acknowledged X] on [date].','区分初始支持、已读确认、提分和逐项认可。'),
('summary','自信提出进一步正面评价','we respectfully submit that the quality of our manuscript merits a further positive assessment','We respectfully submit that [contribution and evidence] merit a positive assessment.','把评价请求放在贡献和证据之后。'),
('summary','请求公平评价','we hope our manuscript will receive a fair evaluation.','We hope the final assessment will consider [key evidence] and the full discussion record.','明确希望 AC 考虑什么。'),
('summary','固定祝福','Wishing you a pleasant day ahead.','Wishing you a pleasant day ahead.','五篇 Summary 均使用；单独成段，位于署名前（如有）。'),
('reports','指出评分与文字的张力','Contradiction Between Qualitative Praise and Quantitative Rating','Could the AC clarify how [stated strengths] and [remaining concern] support the overall assessment?','保留作者质疑并让请求聚焦理由；不把分项评分当固定换算公式。'),
('reports','用原稿定位反驳缺失指控','already provided in Table 6 in the original manuscript','The comparison is provided in [original table]. We ask that the claim of its absence be checked against the submission.','核对被引用的原稿版本，原文已有与新添分开。'),
('reports','请求 chairs 考虑报告事实','We respectfully ask the Area Chairs to take these factors into account when making the final decision.','We respectfully ask the Area Chairs to consider [documented issue] in the final assessment.','用事实、影响和请求收束。'),
('reports','指出关键证据未被回应','remained silent and did not acknowledge this critical evidence','We have not received further feedback on [evidence]. We ask the AC to assess it directly.','报告反馈状态，不从沉默推定 reviewer 同意。'),
('reports','请求判断评分是否反映贡献','consider whether this rating accurately reflects the manuscript\'s contribution','We ask the AC to assess whether [recommendation] remains supported after considering [evidence].','将问题交给 AC 独立核查。'),
('recommend','对合适用户明确推荐','we highly recommend FloE as an efficient and practical alternative','For [target users], we recommend [method] as a practical option supported by [evidence].','原句来自 FloE；不是泛称五篇都这样写。'),
('initial','用层次清晰的小标题解释机制','We address the reviewer’s question by analyzing performance at two stages','We analyze [phenomenon] at two stages: [before X] and [after X].','相反实验趋势先检查所比较的阶段是否一致。'),
('initial','将专业指标转成用户价值','To bridge this gap, we have introduced a detailed discussion','To bridge this gap, we provide [framework] connecting [technical metric] with [practical criterion].','把“有何实际价值”落实到具体框架和评价维度。'),
('initial','用领域与会议内容回应范围质疑','We appreciate the opportunity to clarify the alignment of our work with the ACL community.','We appreciate the opportunity to clarify how [contribution] aligns with [community].','具体对应 topic、研究问题和该社区已有工作。'),
('initial','把模糊贡献改成具体陈述','Thank you for the suggestion on better articulating our contributions','Thank you for the suggestion on clarifying [claim]. We will replace [old wording] with [concrete wording].','不仅辩护贡献，也愿意修改让贡献更明显。'),
('initial','限制内做可靠的补充','Due to time and resource constraints, we evaluate','Within the available time and resources, we evaluate [clearly stated subset] under [settings].','说清模型、样本范围、protocol，不把子集扩大成全面验证。'),
('followup','邀请社区使用与继续构建','enabling the community to leverage and build upon our approach','We hope the community can leverage and build upon [available contribution].','将开源与长期研究价值相连。'),
('followup','愿意继续分享实验结果','We will share the results as soon as they become available.','We are evaluating [X] and will share the results when available within the response window.','承诺尚在进行时，后续用 Update 日期完成闭环。'),
('followup','把 reviewer 的建议写成具体帮助','Your feedback has been instrumental in enhancing the quality of our manuscript','Your feedback has helped us improve [specific part].','说明被改善的内容，使感谢有人情味而非套话。'),
('reminders','强调对工作的自信与投入','We are proud that these enhancements have solidified the paper’s contribution','We are proud that [completed changes] strengthen [specific contribution], as supported by [evidence].','作者自信单独标明，不冒充 reviewer 的评价。'),
('general','说明修订可查找','All revisions are highlighted in blue text for ease of reference.','The changes are highlighted in [permitted revision format] for ease of reference.','这里的颜色指修订稿标记，不是 OpenReview 自定义文本颜色。'),
('summary','让 AC 综合多份评价','We appreciate the reviewers\' recognition of our research\'s significance','We appreciate the reviewers’ recognition of [contribution] ([R IDs]).','引用其他人的肯定须对应到同一具体评价维度。'),
('reports','陈述回应机会受损','This directly prevented us from providing an effective rebuttal','This left us no authorized opportunity to respond to [new issue] before [deadline].','从时间线说明程序影响，请求回应机会。'),
]
patterns=[]
for sid,label,quote,template,use in rows:
 hits=[]
 for n in authors:
  text=norm(n['body'])
  if quote.lower() in text.lower():
   paragraphs=[norm(p) for p in (n['body'] or '').split('\n\n') if quote.lower() in norm(p).lower()]
   hits.append({k:n[k] for k in ['paper','id','title','url','phase']}|{'context':paragraphs[0] if paragraphs else text})
 assert hits,('Unverified original',quote)
 patterns.append(dict(stage=sid,label=label,quote=quote,template=template,use=use,hits=hits,papers=list(dict.fromkeys(h['paper'] for h in hits))))
report={'total_notes':len(allnotes),'author_notes_including_deleted':sum(bool(re.search(r'by\s*Authors',n['meta'] or '')) for n in allnotes),'available_author_notes':len(authors),'deleted':[{'paper':n['paper'],'id':n['id'],'title':n['title']} for n in allnotes if '[Deleted]' in (n['body'] or '')], 'papers':{p:{'notes':sum(n['paper']==p for n in allnotes),'available_author_notes':sum(n['paper']==p for n in authors)} for p in PAPERS},'patterns':patterns,'coverage':[{k:n[k] for k in ['paper','id','title','phase','url','sha256']} for n in allnotes]}
(ROOT/'sources'/'systematic_audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print('Verified',len(patterns),'original-expression patterns;',len(authors),'available author posts;',len(allnotes),'total records')
