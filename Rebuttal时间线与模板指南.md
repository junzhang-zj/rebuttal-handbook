# Rebuttal 时间线与模板指南

适用对象：ML、CV、NLP 论文作者。覆盖逐条 rebuttal、General Response、讨论期总结、催审、请求 AC 协调、评审质量反馈、正式举报以及迟到评审。规则核对日期：2026 年 11 月 10 日。

补充核对：已通过 Jun Zhang 登录会话读取五个原始论坛的 145 条帖子。以《Rebuttal实战手册.html》的逐帖案例与索引为详细原始依据；本文第 7 节保留截图层面的结构归纳。完整记录显示，LoRAM 的 asc9 后续有实质讨论并维持意见；LVSpec 的迟到评审还存在 SAC 协调 emergency reviews 的背景。HybridKV 原始论坛为 https://openreview.net/forum?id=jFuN2yI2D7，ACL commitment 页面与它分属不同阶段。

核心顺序是：**先回答技术问题，再跟进尚未解决的问题，临近结束时归纳证据；出现程序问题时走指定的保密渠道。** General Response 帮所有审稿人快速了解共同问题和回应，Summary 帮 AC 看清讨论后的状态；两者都不自动获得额外篇幅或额外提交次数。

配套的《Rebuttal 英文表达库》进一步整理自然交流、自信陈述贡献、推荐录用、坚定反驳和举报审稿人的分级表达及完整段落。

本文的时间安排、篇幅建议和英文模板是写作建议；明确标注会议和年份的规则才是该会议规则。方括号均为待替换项，实验、评分、认可和完成状态只能填写真实记录。

## 1 先确定会议规则

### 1.1 不同会议的关键差异

| 场景 | 回复机制及可见性 | 对模板使用的影响 |
| --- | --- | --- |
| ICLR 2027 | 公开讨论，可按系统选项限制评论读者；讨论期允许修订论文 | 适合逐条回复、共性总结及后续讨论；私密反馈仍需核对 Readers。大幅改变原稿的内容可能被忽略。[作者指南](https://iclr.cc/Conferences/2027/AuthorGuidelines) |
| NeurIPS 2026 主赛道 | 初始回复阶段 AC 和 reviewer 尚不可见，之后开放互动，再进入作者不可见的内部讨论；每个 review 的 rebuttal 上限 10,000 characters | 不要在第一阶段催 reviewer 看回复。不允许更新论文或补充文件；回复可含新结果。普通回复禁止链接，审稿人要求代码时有向 AC 提交匿名链接的限定例外。[官方手册](https://neurips.cc/Conferences/2026/MainTrackHandbook) |
| ICML 2026 | 每份 review 一次初始回复，5,000 characters；截止后审稿人可见。审稿人追加问题后，作者有一次最终回复机会 | 不是无限往返讨论；AC confidential comment 不能充当额外或迟交 rebuttal。论文及补充文件不能修订；匿名链接只在官方限定用途内使用。[Peer Review FAQ](https://icml.cc/Conferences/2026/PeerReviewFAQ) |
| CVPR 2026 | 一页官方模板 PDF；另有给 AC 的 confidential comment。评审与作者回复不公开 | General Response 和逐条回应要安排在同一页内；不能改模板挤版面或放外链。官方限制新贡献及新实验结果，尤其是未经请求的新增内容。[作者指南](https://cvpr.thecvf.com/Conferences/2026/AuthorGuidelines) |
| ARR | 所查作者指南规定：一次 general response、每份 review 一次 author response，每条最多 5K characters；文本回复，不允许外链；另有 review issue report | 不照搬旧截图中的拆成多帖和反复催审。ARR 提供评审，录用由 commitment 会议决定。页面仍注明适用至 August 2026 cycle，后续周期必须再核对通知和表单。[作者指南](https://aclrollingreview.org/authors) |

这些上限是**字符数 characters**，不是英文词数 words。格式标记等如何计数，以提交表单的校验为准。

### 1.2 当前 ICLR 2027 日期示例

若这次目标是 ICLR 2027，官方日程列出：2026 年 11 月 5 日发布 reviews 并开始作者讨论，11 月 18 日结束作者讨论，11 月 19 日至 12 月 16 日为 reviewer–AC 内部讨论，12 月 16 日通知结果。不要把 ICLR 2026 或截图中的历史日期直接套用。[ICLR 2027 Dates](https://iclr.cc/Conferences/2027/Dates)

该日程对上述讨论节点未明确列出截止时刻和时区，因此本文不自行换算北京时间。应以当轮通知、OpenReview 表单的精确截止时间为准。如果某截止明确写为当日 23:59 AoE，则对应北京时间次日 19:59。

### 1.3 开始前填写这张卡

| 必填项 | 本轮记录 |
| --- | --- |
| 会议、年份、track 或 ARR cycle | [填写] |
| reviews 发布时间 | [日期、时区] |
| 初始 rebuttal 截止 B | [日期、时刻、时区] |
| reviewers 实际可见时间 V | [不要默认等于提交时间] |
| 作者互动截止 D | [可能与 B 不同] |
| 改稿、general response、AC comment 的各自截止 | [分别填写] |
| review issue / meta-review issue 截止 | [分别填写] |
| 字符、页数、次数限制 | [填写] |
| 新实验、修订稿、附件、链接是否允许 | [逐项填写] |
| 当前与最终公开范围 | [填写] |
| 官方通知和表单位置 | [填写] |

## 2 按时间推进

以下为允许互动的会议的建议节奏；单轮 rebuttal 或 ARR 等受限流程，只采用允许的动作。B 为初始回复截止，V 为回复对审稿人开放时间，D 为作者讨论结束时间。

| 阶段 | 什么时候 | 回复什么 | 位置和读者 | 完成标准 |
| --- | --- | --- | --- | --- |
| 拆解 reviews | 收到后当天至次日 | 内部列出每个 concern、原稿证据、所需补充和负责人 | 合作者内部 | 每项批评有对应条目，先识别决定录用的关键疑问 |
| 第一轮 rebuttal | B 前完成；实时讨论可在证据齐备后尽早发 | 按 reviewer 逐条回答，优先正确性、创新性、关键基线及结论范围 | 对应 review 下的指定入口 | 主要论点全部进入正式回复，不能押到后续私信 |
| General Response | 与首轮同步，或允许互动时在主要证据齐备后更新 | 共性问题、贡献定位、重要补充、逐条回复导航 | 指定 general response 入口；无此入口时确认是否允许顶层 comment | 不重复粘贴全部回复，也不以它替代逐条回答 |
| 后续技术讨论 | V 后，收到具体问题时 | 只回应新增疑问、澄清误解或补充已讨论事项 | 对应讨论串 | 一条评论聚焦一个主题；可在约 24 小时内先回复已确认部分 |
| 轻量催 reviewer | V 后等待合理时间，例如 2–3 天；且规则允许 | 指向一个关键问题，询问是否仍有顾虑 | 原 review 线程，reviewer 可见 | 通常一次简短提醒；不要每天催或复制到多个线程 |
| 请求 AC 协调 | 接近 D，关键问题仍无反馈，例如 D 前 2–3 天 | 时间线、相关问题定位、需要 AC 协调的动作 | AC 保密入口 | 请求促进讨论或独立审视证据，不要求强制提分 |
| Summary of the Rebuttal Period | D 前 24–48 小时，且允许提交此类总结 | 已回应事项、明确认可、残留分歧、证据位置 | 允许的总结/评论入口；面向 AC 时按规则设置读者 | AC 能快速理解还有什么决定性问题 |
| 正式 review issue report | 按当轮专门窗口；严重问题及时上报 | 具体事件、原话、证据、影响、请求处理 | 指定 issue report 或保密渠道 | 每项问题有可核查依据，不混入普通技术争论 |
| 内部讨论期 | D 后至决定前 | 通常等待；只处理受邀补充或允许上报的新程序问题 | 指定渠道 | 不绕过作者回复关闭机制追加学术论证 |
| 结果后 | 决定发布后 | 接收则落实修订；拒稿则整理不足；存在严重程序问题时查申诉政策 | camera-ready、下一轮投稿或正式申诉入口 | 申诉窗口及理由需符合该会议规定 |

**催审的计时起点是 V。** 即使作者提前一周交了 rebuttal，reviewer 昨天才获得访问权限，也不应描述为“已忽略我们一周”。

**不要把所有问题都放到最低分 reviewer 身上。** 先判断哪些问题直接动摇核心结论，再解决跨 reviewer 的共同疑问，最后处理小修；支持者的具体问题也要完整回应。

## 3 可见性怎么判断

### 3.1 标题、身份和权限是三回事

OpenReview 中，Reply Type 来自所用 invitation；Signature 表示发帖身份；Readers 表示该帖对谁可见。帖子标题写着 “Confidential” 不会自动变成私密；回复在某位 reviewer 下，也不意味着其他 reviewer 看不到。[OpenReview Forum 文档](https://docs.openreview.net/getting-started/using-the-new-forum-page)

| 内容 | 建议受众 | 提交时要核对 |
| --- | --- | --- |
| 逐条技术 rebuttal | 对应 reviewer，并按会议机制开放给同稿其他评审及 chairs | 使用规定入口；不要擅自缩小受众导致目标 reviewer 看不到 |
| General Response | 同稿所有 reviewers 和 chairs；公开会议可为 Everyone | General Response 是内容用途，不是通用的权限类型 |
| reviewer 催回复 | 原 reviewer 讨论串的正常受众 | 不把点名催促额外扩散到无关受众 |
| 给 AC 的总结 | 允许的 AC/chairs 渠道；公开总结也可使用正常技术讨论范围 | 会议是否允许独立总结；不得用保密渠道扩充 rebuttal 配额 |
| 请求 AC 协调 | AC 及系统规定的上级 chairs | 不向所有 reviewers 广播对某一 reviewer 的投诉 |
| review issue report | 表单规定的读者 | 正式报告与普通 AC comment 可能是两个入口 |
| AC 自身存在问题 | 规定的 SAC、PC 或申诉渠道 | 默认“AC and up”可能仍含被报告 AC；需要时使用不含该 AC 的正式入口 |
| 严重伦理或利益冲突报告 | 会议指定诚信/伦理负责人或 chairs | 描述已知事实，不自行调查匿名 reviewer 身份 |

系统可能自动保留作者组、PC、SAC 等读者，表单名称也随会议变化。不能为了追求“只有 AC”而随意删改系统必需角色。当前 Readers 也不保证永久不公开：ICML 2026、NeurIPS 2026 的录用论文评审和普通作者讨论存在后续公开安排，拒稿论文有相应 opt-in 机制。[ICML FAQ](https://icml.cc/Conferences/2026/PeerReviewFAQ) · [NeurIPS 手册](https://neurips.cc/Conferences/2026/MainTrackHandbook)

“我登录后能看到作者姓名”也不等于 reviewer 能看到；群组成员的展开显示会受到查看者自身权限影响。不要仅凭作者视角截图判断双盲失效。[OpenReview Forum 文档](https://docs.openreview.net/getting-started/using-the-new-forum-page)

### 3.2 每次提交前后检查

1. 确认入口：Rebuttal、Official Comment、General Response、Author–AC Confidential Comment 还是 Review Issue Report。
2. 确认父线程：给哪份 review 的回答，是否误发成顶层评论。
3. 查看实际 Readers，确认目标读者包含在内，保密内容没有发给 Everyone。
4. 确认匿名作者身份；正文、URL、文件元数据不意外暴露身份。
5. 发布后回看 Readers、排版、正文和提交时间，并保存记录。

读者权限、通知邮件和“已经读过”是不同概念。不要因没有收到回复就推定对方已读而拒不回应，也不要把页面修改时间当成提分时间。

## 4 不同回复的功能与格式

| 类型 | 回答的核心问题 | 推荐组织方式 | 建议篇幅，服从官方限制 |
| --- | --- | --- | --- |
| 正常 rebuttal | 这条质疑是否成立，证据是什么 | 问题标题 → 直接结论 → 证据与定位 → 修改/边界 | 每个关键问题约 100–200 英文词，小问题 1–3 句 |
| General Response | 所有评审共同需要知道什么 | 贡献定位 → 2–3 个共同问题 → 主要补充 → 分项导航 | 约 200–350 英文词 |
| Summary | 讨论结束后应如何理解现状 | 核心贡献 → concern 状态 → 剩余分歧 → 请 AC 审视的证据 | 约 200–350 英文词 |
| 催 reviewer | 对某个已回答问题是否仍有顾虑 | 原回应时间 → 一句话重点 → 具体询问 | 约 50–90 英文词 |
| 催 AC / 请求协调 | 需要 AC 采取什么具体动作 | 时间线 → 尚缺反馈 → 截止影响 → 请求 | 约 100–180 英文词 |
| 评审质量反馈 | 哪个判断可能依赖错误事实 | review 陈述 → 原稿证据 → 已回应记录 → 请求核查 | 一事一段，约 150–250 英文词 |
| 正式举报 | 哪种规则或程序可能被违反 | 事实时间线 → 原始证据 → 对应规则 → 实际影响 → 请求处理 | 按表单，不靠长篇情绪描述 |

### 4.1 技术回应最有效的单位

**Concern → Answer → Evidence → Action / Limitation。** 第一两句就回答问题。先给原稿中已经存在的证据，再给规则允许的补充。用“原稿 Sec. 4.2 / Table 3”和“回复中新增 Table R1”区分证据来源。

如果可以修订，写明版本日期和位置；如果不能修订，用 “We will clarify … in the final version, if accepted.”。不要把计划写成已经完成。

对于效率类论文，补实验至少交代：模型、硬件、batch size、输入/输出长度、精度或量化设置、基线版本，以及收益是 kernel、decode 还是端到端指标。比较速度时同时写质量变化，避免拿不等价设置支撑结论。

### 4.2 General Response 与 Summary 的区别

General Response 以**问题和内容**组织，告诉大家共同疑问怎么回答、补了什么。Summary 以**讨论状态和决策依据**组织，告诉 AC 哪些问题已有明确反馈，哪些仍有分歧。

Summary 中只使用以下状态：

- **Acknowledged as resolved**：审稿人明确说该问题已解决；附对应记录。
- **Response provided; awaiting feedback**：作者已回答，尚未收到反馈。
- **Disagreement remains**：双方理解了事实，但对创新性、重要性或充分性仍有分歧。
- **Limitation acknowledged**：作者承认局限，并收窄结论或安排后续修订。

提分可如实记录，但提分不代表所有 concern 都解决。审稿人认可某项实验，也不等于支持整篇录用。

### 4.3 排版

在线回复使用简短加粗标题、稳定的问题编号和紧凑段落。例如 `**W1 — Comparison with baseline X**`。不要每句加粗，不要重复整段 review。表格只保留判定问题所需的列，标出单位、↑/↓ 和实验条件。

PDF rebuttal 使用当年官方模板。可将版面分为简短共性回应与按 reviewer 组织的主体，但不要先写满半页感谢和贡献陈述。页数上限包括表格、图和正文的具体规则应按会议确认。

一个问题太长时优先删冗余和重复背景。只有会议允许多帖时才拆成 Part 1/2、Part 2/2；不得利用拆帖绕过字符或次数上限。

## 5 可直接改写的英文模板

### T1 正常逐条 rebuttal

用途：首轮正式回复。位置：对应 review 的指定回复入口。新实验和改稿句仅在规则允许且确已完成时保留。

```text
Title: Response to Reviewer [ID]

Thank you for the careful review. We address your concerns below.

W1 — [Short description of the concern]
[Direct answer in one or two sentences.]
The original submission provides [specific evidence] in [section/table].
Under [evaluation conditions], [result] supports [narrow conclusion].
[If permitted: We additionally evaluated X and report the results below.]
[Revision made / clarification planned / limitation acknowledged.]

W2 — [Short description of the concern]
We agree that [valid part of the criticism]. Our current claim is limited
to [scope]. [Evidence and explanation.] We have therefore [specific action].

Q1 — [Question]
[Answer, with an exact reference and any necessary qualification.]

We hope these clarifications help assess [the central issue].
```

### T2 General Response

用途：跨 reviewer 的共同问题与总体更新。不要以“全体 reviewer 都认可创新性”开场，除非逐份 review 确实支持这句话。只有一个 general response 名额时应把关键内容一次写完整。

```text
Title: General Response

We thank the reviewers for their feedback. Our main contribution is
[specific contribution under a defined setting]. Below we summarize
the issues shared across the reviews and our responses.

1. [Shared concern; reviewer IDs]
[Direct clarification and supporting evidence.]

2. [Shared concern; reviewer IDs]
[Direct clarification and supporting evidence.]

3. Main updates
[List only completed and permitted additions, each with its location.]

The detailed responses address [R1: topics], [R2: topics], and [R3: topics].
[If relevant: The remaining limitation is X; our conclusions are restricted
to Y.]
```

这里的导航优先用 reviewer ID、问题编号和表格号；只有允许链接时才放链接。单独给某 reviewer 的回复中仍应保留最关键的结论，避免只写 “see general response”。

### T3 后续回复与确认剩余问题

用途：允许往返讨论且 reviewer 已提出追问时。不要在受限流程里额外开帖套用。

```text
Title: Follow-up on [topic]

Thank you for clarifying the concern. The key distinction is [X versus Y].
Under [conditions], [evidence] shows [result]. This supports [claim],
while [limitation] remains outside the evidence we currently have.

Does this address your concern about [specific issue], or is there an
additional assumption or comparison that remains unclear?
```

### T4 Summary of the Rebuttal Period

用途：作者讨论结束前给决策者的简短归纳。面向 AC 的版本仅在该渠道允许此类内容时使用；ICML 2026 的 AC 私信不能承担额外 rebuttal 功能。

```text
Title: Summary of the Rebuttal Period

Dear Area Chair,

Thank you for overseeing the review process. As the author discussion
period concludes, we summarize the main issues and their current status.

1. [Concern A]
We provided [evidence; response location]. Reviewer [ID] explicitly
acknowledged that [precise issue] was resolved on [date].

2. [Concern B]
We responded with [evidence; location] on [date]. We have not received
further feedback, so the reviewer's assessment of this response is unknown.

3. [Remaining disagreement or limitation]
The remaining question is [specific issue]. Our position is supported by
[existing evidence], and we acknowledge [boundary or limitation].

We respectfully ask that the final assessment consider these responses,
particularly [decisive evidence already submitted]. Our central contribution
remains [one-sentence contribution].

Thank you for your consideration.
The Authors
```

若本轮没有任何明确认可，就删掉第一种状态，全部按真实情况写。Summary 不应首次引入决定性新实验或新论点。

这组五篇案例共同使用的 Summary 收尾句是 “Wishing you a pleasant day ahead.”，单独成段，放在署名前。上方为通用模板；按作者原帖风格写作时，使用这句固定祝福收尾。

### T5 轻量催促审稿人

用途：实时互动流程中，回复已可见且等待合理时间后，至多先做一次简短跟进。ARR 等不鼓励反复催审的流程，不直接沿用旧截图做法。

```text
Title: Follow-up on [specific concern]

Dear Reviewer [ID],

We are following up on our response posted on [date], particularly the
clarification of [issue] in [response section/table]. In brief, [one-sentence
answer]. If time permits before the discussion closes on [deadline],
could you let us know whether any concern remains on this point?

Thank you for your time.
```

如果目标只是确认是否还存在技术障碍，这个模板比直接请求提分更合适。

### T6 请 AC 协助催审

用途：关键 reviewer 尚无反馈，且会议允许向 AC 请求协调。先核对 V 和官方 acknowledgement 截止，不以“没有回帖”直接定性失职。

```text
Title: Request for Assistance with Reviewer Discussion

Dear Area Chair,

We submitted our response to Reviewer [ID] on [date], and it became
available to reviewers on [date]. We have not yet received feedback on
[specific concern]. Our response is located at [thread title / item number].

As the author discussion closes on [deadline], we would appreciate your
help in inviting feedback on this point, if appropriate. Clarifying the
remaining concern would allow us to respond within the available window.

Thank you for your assistance.
The Authors
```

### T7 跟进 AC 尚未处理的程序问题

用途：此前已经提出具体问题，临近相关截止仍未收到处理信息。不要把 AC 没有单独回复普通总结视为必须催促的理由。

```text
Title: Follow-up on [procedural issue] before [deadline]

Dear Area Chair,

We are following up on our confidential comment of [date] concerning
[issue]. The relevant deadline is [date/time/time zone]. The practical
impact is [for example, no available opportunity to address a late review].

Could you please advise whether [specific requested action] is possible,
or direct us to the appropriate channel? The relevant records are
[comment title, review ID, timestamps].

Thank you for your help.
```

若问题涉及 AC 本人或该渠道已关闭，按当轮正式说明联系 SAC/PC；不要给所有 chairs 重复群发同一封信。

### T8 向 AC 反馈关键事实错误

这是俗称“打小报告”中最常见、也最适合事实化处理的情形：指出影响评价的具体误解，请 AC 核查。它不等于正式指控 reviewer 违规。

```text
Title: Request for AC Assessment of a Factual Discrepancy

Dear Area Chair,

We would like to flag a factual discrepancy that may affect the assessment
of [specific criterion]. Reviewer [ID] states that [accurate short paraphrase
or brief quotation]. However, the original submission includes [evidence]
in [section/table/page].

We clarified this in our response on [date; item number]. The review still
states [specific claim / or: we have not received feedback on this point].
This matters because [explain the connection to the review's conclusion].

We respectfully ask you to assess this point using the cited evidence and,
if appropriate, invite the reviewer to clarify or correct the factual claim.

Thank you for your consideration.
```

如果证据只存在于 rebuttal 新增结果，不能写 “the original submission includes”。学术分歧则改用 “We interpret the evidence differently”，并说明双方分歧的前提。

### T9 正式 Review Issue Report

用途：有明确评审质量或程序问题，且存在指定报告机制时。优先填正式表单及其当前类别；不要猜测 I1、I2 等编号的含义。

```text
Title: Review Issue Report — [Reviewer ID] — [Issue type]

Submission: [paper ID]
Review: [review ID]
Applicable rule or issue category: [current official category / rule]

Observed issue:
[Neutral description of one specific problem.]

Evidence:
- Review statement and location: [exact relevant passage / field].
- Original submission evidence: [section/table/page, where applicable].
- Author clarification: [date and response item].
- Subsequent review status: [observable fact as of date].

Impact:
[Why this materially affects the evaluation or the opportunity to respond.]

Requested action:
Please assess this issue under [applicable procedure] and consider
[correction / clarification / an opportunity to respond / independent assessment].
```

ARR 的 review issue report 应按周期通知的专门窗口提交；它与 meta-review issue report 不是同一表单。不要把合理的学术分歧包装成违规。[ARR 作者指南](https://aclrollingreview.org/authors)

### T10 严重违规或利益冲突报告

用途：具体证据涉及保密泄露、利益冲突、胁迫、歧视性言论或其他正式伦理问题。使用会议指定的保密报告渠道；若被报告者是 AC，不把报告仅发给该 AC。

```text
Title: Confidential Report of a Potential [Issue] — Submission [ID]

Dear [Designated Chair / Integrity Officer],

We are reporting a potential [issue] for your assessment.

On [date], [specific observable event occurred]. The relevant records are
[identifiers and evidence, provided through the permitted channel].
This may be relevant to [specific policy provision] because [reason].

We can establish [verified facts]. We cannot establish [uncertain point],
and we ask the committee to investigate rather than infer intent.

The impact on the review process is [specific impact]. We request
[appropriate procedural remedy] and guidance on any further information
needed. Please handle this report through the designated confidential process.

The Authors of Submission [ID]
```

匿名阶段不写姓名、单位或真实身份线索，除非正式调查渠道明确要求。

### T11 迟到评审导致无法回应

用途：评审在作者回复关闭后才出现，或新增实质性拒稿理由时已无回应窗口。先查当轮是否已有 late-review 专门安排；ICML 2026 曾规定具体例外窗口，不能跨年份照搬日期。

```text
Title: Request for an Opportunity to Respond to a Late Review

Dear [Area Chair / Designated Chair],

A new review from [reviewer ID] became available on [timestamp and time zone],
after the author response deadline of [timestamp and time zone]. We currently
have no available reply mechanism for the new concerns regarding [topics].

We respectfully request guidance on how to submit a concise response through
an authorized channel, so that the new concerns and our response can both
be considered before the final assessment.

The relevant review and deadline records are [identifiers].
Thank you for your assistance.
```

优先请求恢复回应机会、转交回应或独立核查；“迟到”不自动推出“该 review 必须作废”，因为可能是 chairs 正式征集的补充评审。

### T12 决定后的程序申诉

用途：会议允许申诉，且理由属于规定范围。对创新性判断不同、分数不够高，本身通常不能证明程序失当。

```text
Title: Procedural Appeal — Submission [ID]

Dear [Appeals Contact],

Under [applicable appeal policy], we request a review of [specific procedural
issue] in the assessment of Submission [ID].

The relevant sequence is [brief dated timeline]. The decision refers to
[specific premise], while the record shows [verifiable discrepancy].
This issue is material because [effect on the assessment or response process].

We request [remedy permitted by the appeal policy]. Supporting records are
[identifiers / permitted attachments].

Thank you for considering this request.
```

## 6 有用表达及容易失效的措辞

| 场景 | 可复用表达 | 使用边界 |
| --- | --- | --- |
| 开门见山回答 | “The short answer is …” | 后面立刻给结论，避免空转 |
| 澄清定义 | “Here, X refers to …” | 定义需要与原稿一致 |
| 指向原稿 | “The original submission reports this comparison in Table 3.” | 只有原稿确实存在才使用 |
| 承认表述问题 | “Our wording was ambiguous; the intended claim is …” | 承认歧义，不必把正确结果也否定 |
| 认可合理批评 | “We agree that this comparison is needed to support the broader claim.” | 随后补证据或收窄 claim |
| 有依据地不同意 | “We interpret this result differently because …” | 聚焦前提和数据，不评价 reviewer 能力 |
| 说明贡献区别 | “The distinction from X is …, which enables … under …” | 给具体差异、作用和条件 |
| 限定结论 | “Our evidence supports X under Y; we do not claim Z.” | 主动消除超出证据的推断 |
| 新实验回应 | “To address this specific question, we evaluated …” | 新实验须符合该会议政策 |
| 实验无法完成 | “We cannot provide a reliable evaluation of X within this response window.” | 接着提供已有证据和限制，不承诺不存在的结果 |
| 对比不等价 | “A direct comparison would require matching …” | 解释条件，不以此回避合理基线 |
| 询问残留疑问 | “Could you clarify which part of this concern remains unresolved?” | 适用于允许往返讨论的流程 |
| 温和请求重新评估 | “If this resolves the concern underlying your assessment, we would appreciate an updated evaluation.” | 条件式、最多适度使用，不要求具体分数 |
| 记录沉默 | “We have not received further feedback on this point.” | 不写成 reviewer 拒绝阅读或已接受 |
| 请 AC 独立判断 | “We ask that this point be assessed against the evidence in …” | 让请求指向证据 |
| 保留不确定性 | “This raises a concern about X, but we cannot determine Y from the available record.” | 适用于程序/伦理报告 |

以下替换尤其重要：

| 少用或避免 | 为什么 | 更准确的写法 |
| --- | --- | --- |
| “You misunderstood our paper.” | 人身指向强，且跳过事实 | “The distinction we intended is …” |
| “All concerns have been resolved.” | 作者回应与 reviewer 认可不是一回事 | “We responded to all listed concerns; feedback on W2 is pending.” |
| “All reviewers agree.” | 局部正面评价不代表整体共识 | “R1 and R3 acknowledged X; disagreement remains on Y.” |
| “The low score is an outlier and should be ignored.” | 少数意见也可能正确 | 指出该评分依据中的具体事实问题 |
| “High soundness requires a high overall score.” | 不同维度并非固定换算关系 | “Could the remaining concern driving the overall assessment be clarified?” |
| “The reviewer clearly used an LLM.” | 风格、错字、符号识别错误均不足以证明 | 报告具体错误；有独立证据时再请求按政策核查 |
| “The reviewer is unqualified.” | 低 confidence 不等于不具资格 | “This technical point may benefit from an additional expert assessment.” |
| “Please increase your score to 6.” | 把技术讨论变成施压 | 请求重新评估具体 concern，不指定分数 |
| “We have revised …” 但不能上传修订稿 | 完成状态不真实 | “We will clarify … in the final version, if accepted.” |
| 大段感谢、祝福与重复赞美 | 挤占证据和结论的空间 | 一句感谢，立即进入问题 |

## 7 从五份截图提炼的做法

截图呈现的是历史记录和截图时权限，不保证覆盖整段讨论，也不能据此证明某种措辞导致录用。以下提炼的是结构和可改进之处，不将其中的指控视为已核实结论。

| 材料 | 可观察的组织方式 | 值得复用 | 不宜照搬 |
| --- | --- | --- | --- |
| [LoRAM.png](./LoRAM.png) | 按 reviewer / W / Q 回答；General Response 为 Everyone；Comments to the Area Chair 和 Summary 的 Readers 为作者及 chairs | 技术回应、跨 reviewer 总结和 AC 沟通分开 | 反复催促、依赖 outlier rating 论证，以及未获确认却称全部解决 |
| [HybridKV.png](./HybridKV.png) | General Response 分为两条，列贡献、实验和讨论更新；Summary 为 Author–Editor Confidential Comment | 把实验补充与解释性补充分组，注明位置 | 新规则不一定允许拆两条；软件/数据评分不能直接推出整篇应录用 |
| [LVLMSurvey.png](./LVLMSurvey.png) | General Response、请 AC 促进反馈、Summary 中按 reviewer 总结分歧 | 把 survey 的范围、文献筛选和实证问题分别回答 | 将 soundness/excitement 与 overall assessment 的差异直接认定为程序矛盾 |
| [LVSpec.png](./LVSpec.png) | 有 General Response、期末总结、迟到 review 的保密反馈及独立 Review Issue Report | 将“来不及回应”的时间线和原稿已有证据提交给 chairs | 将迟到自动称为违规；用符号识别错误推定 LLM 使用；以低 confidence 要求排除评审 |
| [FloE.png](./FloE.png) | 有面向 AC 的 concern–response 摘要；AC 回复表示已提醒 reviewers；另有合并 General Response 与 Summary 的历史做法 | 请求 AC 采取具体协调动作，简洁归纳尚未获反馈的 concern | 历史上发过 AC 技术总结不代表现行 ICML 允许用此渠道追加 rebuttal |

这批材料可沉淀为三个常用稿件：**逐条回复底稿、共性问题与更新摘要、讨论状态摘要**。催促和报告则按事实需要使用，不必每篇论文机械地把所有模板发一遍。

## 8 内部工作表与提交检查

### 8.1 Concern 台账

| Reviewer / 问题 | 影响 | 原稿证据 | 拟采取动作 | 负责人 | 回复位置 | 讨论状态 |
| --- | --- | --- | --- | --- | --- | --- |
| [R1 / W1] | [动摇核心结论 / 重要 / 小修] | [Sec./Table] | [解释 / 补实验 / 收窄结论] | [姓名] | [帖名 / 条目] | [待写 / 已回复待反馈 / 明确认可 / 仍有分歧] |

优先保住直接影响结论的实验和论证。内部“认为已经解决”可以用于管理，但对外不能据此写 reviewer confirmed。

### 8.2 证据与措辞检查

- 每个主张是否有原稿、实验或讨论记录支持？“first”“SOTA”“significant”“all”是否有充分依据？
- 每个结果是否写清条件、单位、基线和质量代价？是否把百分比与百分点混用？
- 补充材料是否属于允许新增的内容？是否误把新结果说成原稿已有？
- 修改、实验、代码、上传的完成状态是否真实？未来计划是否被写成完成时？
- 正面评价和提分是否忠实反映原文？是否将沉默当作认可？
- 科学分歧是否被误写成违规？投诉是否有原话、位置、时间和明确请求？

### 8.3 发布检查

- 时间：B、V、D 与 issue report 截止均已核对；时区没有混用。
- 配额：字符、页数、次数、拆帖限制都满足。
- 入口：回复在正确线程；保密报告使用正式入口。
- 权限：Readers 正确；匿名身份与外链合规。
- 排版：预览中的表格、公式和编号可读；没有残留方括号占位符。
- 记录：保存最终文本和时间戳；重要 claim 能定位到具体证据。

## 9 官方规则来源

- [ICLR 2027 Author Guidelines](https://iclr.cc/Conferences/2027/AuthorGuidelines)
- [ICLR 2027 Dates](https://iclr.cc/Conferences/2027/Dates)
- [NeurIPS 2026 Main Track Handbook](https://neurips.cc/Conferences/2026/MainTrackHandbook)
- [ICML 2026 Peer Review FAQ](https://icml.cc/Conferences/2026/PeerReviewFAQ)
- [CVPR 2026 Author Guidelines](https://cvpr.thecvf.com/Conferences/2026/AuthorGuidelines)
- [ARR Author Guidelines](https://aclrollingreview.org/authors)，注意页面的适用周期提示及后续 cycle 通知。
- [OpenReview Using the New Forum Page](https://docs.openreview.net/getting-started/using-the-new-forum-page)

官方规则决定能否发、发给谁、何时发；截图提供历史写作案例；模板提供可替换的表达结构。
