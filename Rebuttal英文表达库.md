# Rebuttal 英文表达库

这份表达库补充《Rebuttal 时间线与模板指南》，重点是自然交流、自信陈述贡献、争取正面评价，以及向 chairs 反映评审问题。以下均为原创可改写句式，不是从论文或评审中摘录的原话。

**有人味来自回应对方的具体问题，自信来自说清证据能支持什么。** 不需要每一段都 sincerely thank，也不需要用 believe、kindly、respectfully 层层缓冲。通常一句感谢、一句直接回答，再给证据，就足够自然。

这些句式不能突破会议的回复次数、读者权限和投诉规则。方括号为待替换内容；示例中的实验、认可、评分变化和程序事实只有核实后才能使用。

## 1 自然地接住对方的问题

| 表达 | 语感与适用场景 |
| --- | --- |
| “Thank you for pointing this out.” | 简洁承认遗漏或值得澄清的点，无须夸大 |
| “This is a fair question.” | 对方的疑问合理；不等于承认负面结论正确 |
| “We see why this was unclear.” | 承认读者为何困惑，适合表述歧义 |
| “We should have made this distinction clearer.” | 对表达负责，随后准确说明区别 |
| “You are right that the original version did not explain this choice.” | 对确实存在的遗漏直接认账 |
| “This helped us identify a gap in the explanation.” | 感谢有具体对象，比空泛赞美更自然 |
| “The short answer is yes, under [condition].” | 直接回答并限定条件 |
| “The key point is [X].” | 将讨论带回决定性问题 |
| “To make this concrete, consider [example].” | 用具体例子解释抽象论证 |
| “It may help to separate two questions here.” | 对方混合了两类问题时，用于拆解 |
| “We agree on the importance of [X]. Where we differ is [Y].” | 先确认共识，再定位真实分歧 |
| “Thank you for taking another look.” | reviewer 已经回看或追加反馈时使用 |
| “That clarifies the concern. Our answer is [X].” | 收到追问后自然接续，不重复开场套话 |
| “We appreciate the chance to clarify this point.” | 对方指出关键误解、愿意继续讨论时使用 |

可以使用 “we’re” 等缩写，但不必为了口语感刻意使用。技术部分保持明确、平实；“Great catch!”、“You nailed it!” 在正式 rebuttal 中往往太随意，尤其不适合重大错误。

### 可直接套用的短段落

**承认表述歧义，但保留技术结论：**

> We see why this was unclear. The reported latency includes both [A] and [B], but excludes [C]. We should have stated this explicitly. Under this definition, the comparison in Table [X] uses the same measurement procedure for all methods.

**承认确实没有做过某项实验：**

> This is a fair question. We have not evaluated [setting], so we cannot claim that the same gains hold there. What our results do establish is [bounded conclusion]. We will make this scope explicit in the final version, if accepted.

**真正听懂追问后继续回答：**

> Thank you for clarifying. We now understand that your concern is about [X], rather than [Y]. The relevant comparison is therefore [Z], which is reported in [location].

## 2 有分寸地不同意

礼貌不意味着把每个批评都写成正确。先说具体分歧，再给足以裁决的证据；不要用态度词替代论证。

| 强度 | 表达 | 适用条件 |
| --- | --- | --- |
| 温和 | “We read this result differently.” | 对同一结果的解释不同 |
| 温和 | “We agree with the premise, but it does not imply [conclusion].” | 接受前提，但不同意推论 |
| 明确 | “This concern appears to rest on the assumption that [X]. Our method instead [Y].” | 能指出对方具体假设 |
| 明确 | “That description does not match the method evaluated in the paper.” | reviewer 对方法的描述确实有误；下一句立即给原稿位置 |
| 明确 | “The comparison is already included in Table [X] of the original submission.” | 对方称缺少的比较原稿已有 |
| 坚定 | “We do not think this conclusion is supported by the evidence cited in the review.” | 能逐项解释证据与结论为何不匹配 |
| 坚定 | “The claim that [X] is factually incorrect: [specific evidence].” | 可客观证伪的事实错误，而非创新性判断 |
| 坚定 | “We disagree with this characterization because it overlooks [specific mechanism or result].” | 对工作的定位失准，有明确遗漏 |

不要习惯性写 “With all due respect”。它常带有对抗感。“Obviously”“Clearly”“As we already explained” 也容易显得责备对方。

**坚定但不攻击人的完整示例：**

> The concern appears to assume that [operation] is performed for every generated token. It is performed once during [stage], as stated in Section [X]. Its cost is included in our end-to-end measurements. The review’s conclusion about a recurring per-token overhead therefore does not apply to the evaluated implementation.

## 3 自信地表达工作的价值

### 3.1 说清贡献，而不是堆形容词

| 目的 | 推荐表达 |
| --- | --- |
| 明确核心贡献 | “Our central contribution is [X], which makes [Y] possible under [constraint].” |
| 区分已有方法 | “The contribution lies in [specific mechanism], rather than in the use of [known component] itself.” |
| 说明为什么重要 | “This matters in practice because [deployment consequence].” |
| 承认组件已有但强调组合必要性 | “The individual components are established; the new result is that [specific design] enables [capability].” |
| 用消融支撑技术区别 | “The ablation in Table [X] shows that [component] is necessary to obtain [result] under [conditions].” |
| 突出新的适用条件 | “The method addresses a regime that prior approaches do not cover: [precise regime].” |
| 指出实用价值 | “The benefit is not only a reduction in [metric], but the ability to run [workload] within [resource budget].” |
| 对简单方法保持自信 | “The simplicity of the method is a practical advantage: it requires [minimal requirement] while delivering [measured benefit].” |
| 解释增量中真正的新意 | “The technical advance is [X]. Existing methods cannot obtain this behavior without [missing capability].” |
| 限定“首次” | “To our knowledge, this is the first study to [precisely bounded claim].” |

“To our knowledge” 不能替代文献检索。若无法支持首次主张，改成 “Our study provides [specific contribution]”。

### 3.2 对结果有信心

| 情况 | 推荐表达 | 避免过度外推 |
| --- | --- | --- |
| 证据直接支持主张 | “These results support the claim that [X] under [Y].” | 不必全部改成 suggests 来显得谦虚 |
| 多种设置一致 | “The improvement is consistent across the evaluated [models/tasks/settings].” | 保留 evaluated，不宣称所有模型都成立 |
| 稳定性确有统计支持 | “The effect persists across [N] seeds, with [uncertainty measure].” | 没有统计分析时不写 statistically significant |
| 新证据回应质疑 | “The additional comparison directly addresses the concern about [X].” | 表示实验回答了问题，不声称 reviewer 已被说服 |
| 局限不推翻主结论 | “This limits the scope of the claim, but does not change the result established in [setting].” | 必须确认局限未影响该 setting 的证据 |
| 对贡献总体有信心 | “We remain confident in the contribution because [specific evidence].” | because 后面给证据，不给自我评价 |
| 结果并非全面领先 | “The method offers a favorable trade-off in [regime], while [baseline] remains stronger in [other regime].” | 坦率说明权衡，本身可以增强可信度 |

### 3.3 用效率论文的语言具体表达价值

> Our central contribution is to make [workload] feasible within [memory budget]. Under the matched setup in Table [X], the method reduces [memory/latency] by [amount], with [quality change]. This is a useful operating point for [deployment scenario], where [constraint] prevents the baseline from running at the same scale.

> The advance is the ability to [new capability], not simply a faster implementation of the same computation. The ablation in Section [X] isolates this distinction: removing [mechanism] eliminates [benefit] even when the remaining optimizations are retained.

> We agree that [component] is not new by itself. The contribution is [specific design and its consequence]. We evaluate this contribution directly through [comparison], rather than relying on the use of that component as evidence of novelty.

这些表述可以有力，但不能凭空加入 “baseline cannot run” 或 “eliminates the benefit”；只有实验真支持才使用。

## 4 推荐我们的工作并争取正面评价

作者可以清晰地说明为什么工作值得接收。最有说服力的推荐通常包括：**贡献是什么、决定性 concern 如何被回应、仍有什么限制、为什么仍具有发表价值。** 不必反复要求 reviewers 提分。

### 4.1 不同强度的推荐表达

| 强度与对象 | 表达 |
| --- | --- |
| 克制，面向 reviewer | “We hope this clarification makes the contribution and its scope easier to assess.” |
| 自信，面向 reviewer | “We believe the evidence now addresses the concern about [X] and supports a positive reassessment of this aspect of the work.” |
| 自信，面向 AC | “Taken together, the technical contribution and the evidence in [locations] make a strong case for acceptance.” |
| 明确推荐，面向 AC | “We believe this work merits acceptance on the strength of [contribution] and [evidence].” |
| 强调社区价值 | “We believe the paper would be a useful contribution to [community] because it enables [specific research or practical use].” |
| 对剩余小问题作判断 | “In our view, the remaining issues concern presentation and scope, rather than the validity of the main result.” |
| 请求基于完整记录判断 | “We ask that the final assessment reflect both the original submission and the clarifications provided during the response period.” |
| reviewer 明确认可后 | “Thank you for confirming that [issue] is resolved. If no substantive concern remains, we would appreciate an updated assessment reflecting the discussion.” |

“The remaining issues concern presentation” 只有在确实没有未解决的正确性或关键实证问题时才成立。其他 reviewer 高分可以是背景，不能代替独立证据。

### 4.2 给 AC 的推荐段落

**贡献明确，关键问题已有充分回应：**

> We believe the paper makes a strong case for acceptance. Its contribution is [X], supported by [evidence]. During the discussion, we clarified [A] and provided [B] in response to the main concerns. The remaining limitation is [C], which bounds the scope of the result without undermining [validated claim]. We hope this contribution and the supporting evidence will weigh positively in the final assessment.

**仍有一位 reviewer 不同意时：**

> A disagreement remains about [issue]. Our case rests on [specific evidence], rather than on the balance of reviewer scores. We ask the AC to assess whether this evidence establishes [claim]. In our view, [contribution] remains a substantive advance for [setting], even with the acknowledged limitation of [X].

**正面但不夸张的期末收尾：**

> Thank you for the careful consideration of our work. We remain confident that [specific contribution] will be useful to [community], and that the evidence in [locations] supports the main claim. We would welcome a positive assessment based on that contribution and the discussion record.

这里的 “We believe this work merits acceptance” 是作者的有依据主张；“The reviewers agree that this work merits acceptance” 是关于他人立场的事实陈述，必须有明确记录。ARR 阶段应改为请求准确评估贡献和问题，不向 ARR reviewers 要求会议录用。

## 5 向 AC 反馈评审问题的表达

### 5.1 先区分三种事

| 情况 | 怎么称呼 | 合适目标 |
| --- | --- | --- |
| 对创新性、重要性或充分性的正常分歧 | Scientific disagreement | 请 AC 根据技术论证独立判断 |
| 错误事实、忽略关键证据、迟到后无法回应等 | Factual discrepancy / Review quality concern / Procedural concern | 纠正记录、澄清、获得回应机会 |
| 有证据涉及泄密、利益冲突、胁迫等 | Potential policy violation / Potential misconduct | 正式调查及按政策处理 |

“举报”可以坚定，但标题最好点出具体问题。不要直接把每次低分都命名为 misconduct。正式 issue report 应遵循会议表单；以下表达适用于相应的保密渠道。

### 5.2 自然但明确的开头

- “We would like to bring a specific review issue to the AC’s attention.”
- “We are concerned that the assessment may rely on a factual error.”
- “We are writing to request a procedural review of [issue].”
- “This concern relates to the opportunity to respond, rather than to the reviewer’s choice of score.”
- “We are reporting a potential violation of [policy] and ask the committee to assess the evidence below.”

不必先写一整段感谢，也不必用 “We humbly beg”。直接写清问题往往更专业。

### 5.3 陈述问题与证据

| 问题 | 可用表达 |
| --- | --- |
| review 称原稿缺少已有内容 | “The review states that [X] is absent. It is present in Section [Y] of the original submission.” |
| 事实错误仍未修正 | “As of [date], the review still contains this statement despite the clarification submitted on [date].” |
| 无反馈，避免指控动机 | “We have not received a response to the clarification, so we cannot tell whether this evidence has been considered.” |
| 结论依赖错误前提 | “This discrepancy is material because the recommendation explicitly relies on [premise].” |
| 评分理由不清楚 | “The written justification does not explain which remaining concern supports the overall assessment.” |
| 审稿对象似乎混淆 | “Several comments refer to [method/dataset] that is not part of this submission.” |
| 评价标准发生变化 | “The follow-up introduces [new criterion], which was not raised in the original review.” |
| 迟到且窗口关闭 | “The concern was first raised after the author response window had closed, leaving no opportunity to address it.” |
| 非技术性攻击 | “The statement [brief exact quotation] concerns the authors personally and does not identify a technical issue with the submission.” |
| 可能违反引用政策 | “The request makes a favorable assessment conditional on citing [work]. We ask the chairs to assess whether this is consistent with the citation policy.” |
| 怀疑泄密但尚未证实 | “The record suggests a possible disclosure of non-public submission material. We cannot establish the source of the disclosure and request an investigation.” |

“标准发生变化”不是自动违规；后续问题可能是合理追问。要说明新标准的内容、提出时间、为何实质改变评价，以及作者是否有机会回应。

### 5.4 明确请求处理

从轻到重，选择与证据和影响相称的动作：

1. “Could you ask the reviewer to clarify the basis for this conclusion?”
2. “We request that this factual statement be checked against the original submission.”
3. “We ask that the cited evidence be considered explicitly in the final assessment.”
4. “We request an opportunity to respond to the newly introduced concern.”
5. “An independent assessment of this technical point would help resolve the discrepancy.”
6. “We ask that no adverse inference be drawn from the absence of an author response to a concern raised after the response deadline.”
7. “If this factual error is confirmed, we ask that the recommendation be reassessed without relying on that premise.”
8. “If a conflict of interest is confirmed, we request reassignment in accordance with the venue’s policy.”
9. “We request that this matter be referred to the designated integrity or ethics process.”

若确有充分证据认为某份 review 不可靠，可以写得更明确：

> Given the documented factual errors in [A] and [B], we ask the AC to assess the reliability of this review before relying on it in the final decision.

比直接要求“删除这个低分”更聚焦，也给 chairs 留出依据政策采取行动的空间。

## 6 举报或投诉的完整段落

### 6.1 原稿已有实验却被当成关键缺失

> Dear Area Chair, we would like to flag a factual issue in Reviewer [ID]’s assessment. The review states that the paper lacks [comparison], and cites this absence as a primary reason for its recommendation. The comparison is included in Table [X] of the original submission under [conditions]. We pointed this out in our response on [date], but the statement remains unchanged as of [date]. We ask that this premise be checked against the original submission and that the final assessment reflect the evidence actually provided.

### 6.2 审稿人没有反馈

> Our response to Reviewer [ID] has been available since [date]. We have not received feedback on the clarification of [issue], which appears central to the review’s recommendation. We cannot tell whether the response has been considered. If the process permits, we would appreciate your help in obtaining clarification; otherwise, we ask that the evidence in [response item] be considered in the final assessment.

若该会议不要求 reviewer 回帖，不能把这一段升级成“违反回应义务”。若有明确 acknowledgement 规定，可准确补充规则和截止记录。

### 6.3 迟到评审或最后时刻新增理由

> The concern about [X] was first introduced on [date and time], after the author response window closed on [date and time]. We therefore had no opportunity to address it through the normal process. We request an authorized opportunity to respond before this concern is used in the final assessment. In particular, we ask that the lack of a response not be interpreted as an inability to address the issue.

### 6.4 怀疑 review 针对另一篇论文

> Several statements in the review appear to concern a different submission. In particular, it refers to [dataset] and [method], neither of which appears in our paper, and evaluates a task different from the one defined in Section [X]. We ask the AC to verify whether the review was attached to the intended submission and, if necessary, arrange an appropriate reassessment.

### 6.5 怀疑使用了不合规的 LLM

单凭语言流畅、泛泛而谈、符号看错或虚构一个引用，无法确定使用了 LLM，更不能直接确定违反了当轮政策。**报告可验证的内容问题；只有额外证据支持时才提出工具使用的疑虑。**

> We cannot determine how this review was produced. Our concern is that it attributes [claim] to the paper, although the paper states [actual content] in Section [X], and cites [reference] that we have been unable to verify through [checks]. We ask that these substantive issues be assessed directly. If the chairs find evidence relevant to the venue’s tool-use policy, we would appreciate review through the appropriate process.

如果有 reviewer 明确自述等独立证据：

> The reviewer’s statement on [date] indicates [exactly what was disclosed]. This appears potentially relevant to [specific current policy provision]. We request that the chairs verify the circumstances and determine whether a policy violation occurred.

### 6.6 AC 的总结遗漏了决定性回应

> Dear [SAC / designated contact], the meta-review states that [issue] was left unanswered. Our response on [date], submitted before the deadline, addresses this point in [item] using [evidence]. We understand that the response may not have been persuasive; however, that differs from the statement that no response was provided. We request that the record be checked and that the assessment distinguish an unanswered concern from a response judged insufficient.

这段能保留一个重要区别：**AC 有权认为回应不足，但“不足”和“没有回应”是不同事实。**

### 6.7 有证据的严重不当行为

> We are reporting a potential violation of [policy]. On [date], [observable event]. The supporting record is [identifier], and the relevant passage is [brief quotation]. This affected the review process by [specific impact]. We can verify these facts, but we cannot determine intent or any undisclosed relationships. We request a confidential investigation and guidance on the appropriate procedural remedy.

### 6.8 举报信的坚定收尾

- “We are asking for this specific issue to be examined on its merits.”
- “We request a correction of the record and an assessment based on the corrected facts.”
- “Please let us know if further documentation is needed to assess this concern.”
- “We would appreciate confirmation that this report has reached the appropriate chair.”
- “Given the approaching deadline of [date], timely guidance would allow us to participate meaningfully in the process.”

避免用 “We demand acceptance”“This reviewer must be punished”“We will expose this publicly” 收尾。请求应指向评审程序和证据，不以录用结果作为举报是否得到处理的标准。

## 7 把机械表达改得自然且有力

| 机械、过软或过满的表达 | 更自然的改写 |
| --- | --- |
| “We sincerely and deeply thank the esteemed reviewer for the invaluable comments.” | “Thank you for pointing out the ambiguity in our evaluation setup.” |
| “We humbly believe that our method may potentially be useful.” | “Our method enables [capability] under [constraint].” |
| “Our groundbreaking and highly innovative framework significantly advances the field.” | “The framework reduces [cost] by [amount] while maintaining [quality] under [conditions].” |
| “We believe that we have successfully and comprehensively addressed all concerns.” | “We answered W1–W4; R2 confirmed that W1 is resolved, and feedback on W2–W4 is pending.” |
| “We kindly and respectfully request the AC to kindly consider our concerns.” | “We ask the AC to check [specific discrepancy] against Table [X].” |
| “The reviewer maliciously ignored our response.” | “The review still relies on [premise], which our response on [date] addresses.” |
| “The score is unfair because the other reviewers gave high scores.” | “The recommendation relies on [premise], whereas [evidence] shows [fact].” |
| “Our paper deserves acceptance because we worked very hard.” | “We believe the paper merits acceptance because [contribution] is supported by [evidence].” |
| “Wishing you a pleasant day ahead.” 在每条回复重复出现 | “Thank you for your time.” 或直接结束于技术结论 |

## 8 最值得保留的三段

**自然回应：**

> This is a fair question. The key distinction is [X]. Under [conditions], [evidence] supports [claim]. We should have made this scope clearer in the original text.

**自信推荐：**

> We believe the work merits a positive assessment on the strength of [contribution] and [evidence]. The remaining limitation is [X], which restricts the scope but does not undermine [validated result].

**有力投诉：**

> The review’s conclusion relies on [premise]. The original submission shows [contrary fact] in [location]. We clarified this on [date]. We ask that the discrepancy be checked and that the final assessment be based on the corrected record.
