# -*- coding: utf-8 -*-
import re, html

SRC='/home/xiachen/Desktop/BP辩论稿沙盘_教育辩题.html'
DST='/home/xiachen/Desktop/BP辩论稿沙盘_教育辩题_中英切换.html'

ZH = {
'“Education isn’t as good as it used to be.” (p. 75)':'“教育不如从前了。”（教材第 75 页）',
'Opening Government':'开幕政府','Opening Opposition':'开幕反对','Closing Government':'闭幕政府','Closing Opposition':'闭幕反对',
'Here is my evaluative argument claim:':'以下是我的评价型论点主张：',
'Here is my relational argument claim:':'以下是我的关系型论点主张：',
'Here is my evidence:':'以下是我的证据：',
'Here is my warrant:':'以下是我的论证依据：',

'Madam Speaker, we are not mourning a golden age; we are asking what a qualification now certifies. I will set a standard, then test it against one incentive.':
 '主席女士，我们不是在哀悼黄金时代，而是在追问学历今天究竟证明什么。我先立标准，再用一项激励去检验它。',
'First, fix what counts as good.':'第一，先确定什么算「好」。',
'Education now certificates recall more reliably than transfer.':'如今的教育，证明记忆复现比证明迁移能力更可靠。',
'World Bank data show':'世界银行数据显示，',
'world adult literacy rose from 74.6% in 1990 to 87.6% in 2023 while the primary net enrolment rate moved from 82.0% to 89.2% — access improved on both measures':
 '全球成人识字率从 1990 年的 74.6% 升至 2023 年的 87.6%，小学净入学率从 82.0% 升至 89.2%——两项指标都显示入学机会改善',
'Those figures measure participation and basic skill, not the ability to apply knowledge in a new situation; a system can expand access and simultaneously narrow what its credentials certify. Definition of the object and Standard of judgement must therefore be fixed before any decline is asserted, and on the standard of durable transfer the burden falls on Government to show the incentive changed. This is a claim about an institutional signal, not about teachers\' effort.':
 '这些数据测的是参与程度与基础技能，而非在新情境中运用知识的能力；一个体系完全可能同时扩大入学机会、又收窄其学历所证明的东西。因此在断言任何下降之前，必须先用「定义」确定对象、用「标准」确定评判尺度；以「可持久迁移」为标准，举证责任在于政府方证明激励确实变了。这是关于制度信号的主张，不是关于教师是否努力的主张。',
'In this evaluative claim, Definition fixes the object and Standard supplies the yardstick.':'在这条评价型主张中，「定义」确定对象，「标准」提供尺子。',
'Second, compare two assessment regimes.':'第二，比较两种评价制度。',
'Where high-stakes scoring dominates, coursework narrows toward rehearsal; where open problems are assessed, comparable cohorts show more transfer. The recurrence across systems makes the mechanism structural rather than a story about individual failure.':
 '凡高利害分数占主导，课程便收窄为反复操练；凡以开放性问题评价，可比群体表现出更多迁移。跨制度反复出现，说明这一机制是结构性的，而非个别教师失职的故事。',
'On that standard, the House should support.':'按此标准，本场应支持我方。',

'Madam Speaker, Government sets a new yardstick, then calls the old one a decline. Two answers.':
 '主席女士，政府方先立一把新尺子，再把旧尺子称为下降。两点回应。',
'First, the curriculum changed shape.':'第一，课程的形状变了。',
'Expansion of aims is a better explanation of the same observations than decay.':'对于同样的观察，目标扩容比「衰败」是更好的解释。',
'UNESCO learning domains and World Bank series show':'联合国教科文组织的学习领域框架与世界银行序列表明，',
'tertiary gross enrolment rose from 13.3% in 1990 to 43.2% in 2023, while syllabuses added digital, civic and collaborative competences':
 '高等教育毛入学率从 1990 年的 13.3% 升至 2023 年的 43.2%，课程纲要在读写之外加入了数字、公民与合作能力',
"Fixed hours spread over more goals redistribute attention rather than destroy it; cohort composition also shifts when participation nearly triples. Both are alternative causes of any apparent change, and neither requires learning to have fallen. Judging today's broader curriculum by yesterday's narrower syllabus mistakes a change of object for a change of quality.":
 '固定课时分摊到更多目标，是注意力的重新分配而非毁损；参与规模接近三倍时，群体构成也会改变。两者都是任何表观变化的替代原因，且都不要求学习真的下降。用过去更窄的纲要去评判今天更宽的课程，是把「对象变了」误当成「质量变了」。',
'Here, Definition and Alternativity supply competing causes.':'此处由「定义」与「替代原因」给出竞争性成因。',
'Second, ask who is in the average.':'第二，追问均值里都有谁。',
'An average over a near-universal cohort is not comparable with one over the selected minority in secondary school a generation ago; a description omitting that shift is not thorough.':
 '近乎全民化群体的均值，与上一代经过筛选才进入中学的少数人均值不可比；遗漏这一构成变化的描述并不周全。',
'The fixed-standard argument treats recall as optional, yet recall is the substrate of transfer; defining good as transfer alone begs the question.':
 '固定标准的主张把记忆当成可有可无，但记忆是迁移的基础；只把「好」定义为迁移，本身已预设结论。',
'The cross-regime comparison lists coexistences, not a counterfactual with ability and cohort held fixed.':
 '跨制度比较列出的只是共存关系，而非在能力与群体均固定情况下的反事实。',
'Neither a fair comparison nor a measured fall has been offered. We oppose.':'公平比较与实测下降，两者都未被给出。我方反对。',

'Madam Speaker, I will answer the composition objection, rebuild our standard, then add a mechanism you can observe in one classroom.':
 '主席女士，我将回应群体构成反驳、重建我方标准，再补上一个在一间教室里就能观察到的机制。',
'First, reduce the claim to one decision.':'第一，把主张缩减为一次选择。',
'Equal rewards flip one student from understanding to rehearsal.':'同等奖励会把一个学生从理解推向操练。',
'Behavioural research on incentives, cited as Authority here, finds':'此处以「权威」援引的激励行为研究发现，',
'when a reproducible answer and an unseen problem earn identical credit, students shift effort toward the cheaper, more predictable task':
 '当可复现答案与陌生问题得到相同学分时，学生会转向更便宜、更可预期的任务',
'One student compares two costs for the same credit: understanding takes time and risks failure, rehearsal is cheap and predictable. Repeated across a term the cheaper choice becomes a habit and crowds out practice in transfer before any examination is sat. That micro-level mechanism produces the aggregate pattern PM described, and it survives the access objection, since a change in cohort composition does not change the choice facing any individual student.':
 '一个学生在相同学分下比较两种成本：理解耗时且有失败风险，操练便宜且可预期。一学期反复下来，更便宜的选择成为习惯，并在考试之前就挤掉了迁移练习。这一微观机制产生了首相所描述的总体图景，且不受「入学面扩大」反驳影响，因为群体构成的变化并不改变任何单个学生面对的选择。',
'In this relational claim, Reduction narrows the causal link and Authority supports it.':'在这条关系型主张中，「缩减」收窄因果链，「权威」为其提供支撑。',
'The broader-aims objection answers a claim about effort, not one about transfer: adding goals does not explain why equal credit still selects the cheaper route.':
 '目标扩容的反驳回应的是关于投入的主张，而非关于迁移的主张：增加目标并不能解释为何同等学分仍会选择更便宜的路径。',
'The access objection shows averages moved, not that transfer within any group fell; composition cannot rescue the standard we set.':
 '入学面扩大的反驳只说明均值移动了，并未说明任一群体内部的迁移下降；群体构成救不了我方所设定的标准。',
'I reaffirm the fixed standard: transfer is what makes a qualification worth having.':'我重申既定标准：迁移才是学历值得拥有之处。',
'The standard and the mechanism stand. We support.':'标准与机制均成立。我方支持。',

'Madam Speaker, the individual calculus assumes what it must prove. Three things: answer it, rebuild our tests, add one more.':
 '主席女士，个体权衡把有待证明的东西当成了前提。三件事：回应它、重建我方检验、再补一点。',
'First, learning survives without the old regime.':'第一，旧制度缺席时，学习依然存在。',
'Transferable learning persists where old-style drilling has disappeared.':'在旧式操练消失之处，可迁移的学习仍然存在。',
'In curriculum case studies reported by OECD reviews,':'经合组织评述所载的课程案例研究显示，',
'students in systems that replaced rote repetition with open tasks still read unfamiliar texts and handle arithmetic in new settings':
 '在以开放性任务取代机械重复的体系中，学生仍能阅读陌生文本，并在新情境中完成运算',
'An effect should be absent when its alleged cause is absent. If application survives without rehearsal, rehearsal was never necessary for learning, and the chain from assessment to lost transfer breaks. Government may still show a marginal shift in what is rewarded, but a marginal shift is not the across-the-board decline the motion asserts; Absence defeats the strong version while leaving the weaker one unproven.':
 '原因缺席时，结果本应缺席。若没有操练仍有应用能力，操练就从来不是学习的必要条件，从评价制度到「迁移丧失」的链条由此断裂。政府方或许仍能证明「被奖励之物」发生了边际变化，但边际变化不等于辩题所断言的全面下滑；「缺席检验」否定了强版本，同时使弱版本仍未被证明。',
'In this relational claim, Absence tests whether the alleged cause is necessary.':'在这条关系型主张中，「缺席检验」检验所声称的原因是否必要。',
'The equal-reward calculus assumes transfer is harder to grade; where unseen problems are scored, rehearsal is no longer the cheaper route.':
 '同等奖励的权衡预设了迁移更难评分；若陌生问题本身计分，操练就不再是更便宜的路径。',
'The fixed standard measures one capacity and ignores literacy, access and collaboration, so even a real fall in transfer cannot show education as a whole is worse.':
 '既定标准只测一种能力，忽略读写、入学与协作；即便迁移确有下降，也不能说明教育整体更差。',
'I develop the access point: a wider cohort makes any single yardstick less comparable over time.':
 '我发展「入学面」这一点：群体更广，使任何单一尺子的跨期可比性都下降。',
'The mechanism and the standard remain unproven. We oppose.':'机制与标准均未被证明。我方反对。',

"Madam Speaker, I take Opening Government's direction as settled. Our extension concerns institutions rather than individuals.":
 '主席女士，我方接受开幕政府既定方向。我们的扩展落在制度层面，而非个体层面。',
'Our extension: incentives, not ability.':'我方扩展：起作用的是激励，不是能力。',
'Holding ability constant, the assessment regime alone changes what is learned.':'在能力保持不变时，仅评价制度本身就会改变所学之物。',
'Cross-system assessment studies report that':'跨制度评价研究指出，',
'comparable cohorts produce more transfer under open-problem regimes than under reproducible-item regimes, with intake held constant':
 '在入学生源固定的条件下，可比群体在开放性问题制度下比在可复现题目制度下表现出更多迁移',
'The same students respond to whatever signal is rewarded. With ability held fixed, the remaining variable is the incentive, so the difference is attributable to the regime rather than to cohort quality or to individual teachers. This extends the individual calculus from one choice to a standing institutional pattern without contradicting it, and it answers the absence objection: transfer surviving without drilling is compatible with transfer falling when rewards change.':
 '同样的学生会对被奖励的信号作出反应。能力固定后，剩下的变量就是激励，因此差异应归因于制度，而非群体质量或个别教师。这把个体权衡从一次选择扩展为稳定的制度模式，且并不与之冲突；它也回应了缺席反驳：没有操练时迁移仍存在，与奖励改变后迁移下降可以并存。',
'In this relational claim, Comparison isolates the incentive by holding ability constant.':'在这条关系型主张中，「比较」通过固定能力来隔离激励。',
'The absence test targets drilling, not incentives; learning without rehearsal is compatible with learning falling once rewards change.':
 '缺席检验针对的是操练而非激励；没有操练仍有学习，与奖励改变后学习下降并不矛盾。',
'I develop the individual calculus: repeated choices under the same rewards become the institutional pattern.':
 '我发展个体权衡：同一奖励下的反复选择，会累积为制度模式。',
'Government still explains the change. We support.':'政府方仍能解释这一变化。我方支持。',

"Madam Speaker, I take Opening Opposition's line as settled. We add one independent gap and answer the institutional extension.":
 '主席女士，我方接受开幕反对既定路线。我们补上一个独立缺口，并回应制度层面的扩展。',
'Our extension: a proxy is not an outcome.':'我方扩展：代理变量不是结果。',
'Government proves a change in what is rewarded, not a fall in learning.':'政府方证明的是「被奖励之物变了」，不是「学习下降了」。',
'The very World Bank series Government cites':'政府方援引的世界银行同一序列',
'reports enrolment and literacy, but contains no before-and-after measure of transfer; the case rests on scoring rules and reported coursework':
 '只报告入学率与识字率，不含迁移能力的前后测；其论证依赖评分规则与所报告的课程安排',
'The motion names a decline in educational quality, which is an outcome. Rewards, rehearsal and course breadth are intermediate proxies; unless they are linked to measured transfer across the same cohort over time, the chain stops before the effect. This gap is independent of the opening-half tests: even if the incentive mechanism is real, its size and direction remain unmeasured, so Opposition need not deny the mechanism to deny the conclusion.':
 '辩题所指的是教育质量下降，那是结果。奖励、操练与课程广度只是中间代理；除非把它们与同一群体跨时期的迁移测量结果相连，推理链就停在结果之前。这一缺口独立于前半场的各项检验：即便激励机制为真，其规模与方向仍未被测量，因此反方无需否认机制也可否认结论。',
'In this evaluative claim, Measurement challenges the proof offered against the standard.':'在这条评价型主张中，「测量」质疑按该标准提供的证明。',
'The institutional extension holds ability constant but not the yardstick; a cohort judged by open problems will look different by construction.':
 '制度层面的扩展固定了能力，却没有固定尺子；以开放性问题评判的群体，按构造就会显得不同。',
'The cross-system comparison lists coexistences, not a counterfactual with assessment held fixed.':
 '跨制度比较列出的只是共存关系，而非在评价制度固定的情况下的反事实。',
'The causal chain stops before the claimed effect. We oppose.':'因果链停在所声称的效果之前。我方反对。',

"Madam Speaker, education here means the transferable capability that the schooling forms; I reaffirm PM's standard and weigh the record.":
 '主席女士，辩题中的教育指学校所塑造的可迁移能力；我重申首相的标准，再衡量全场记录。',
'We reaffirm the standard: what a qualification certifies on unseen tasks.':'我们重申该标准：学历在陌生材料上还能证明什么。',
"On that standard, education is not as good as it used to be: a qualification now certifies less transferable learning.":'按此标准，教育不如从前：学历现在证明的可迁移学习更少了。',
'Three findings are on the record:':'全场记录中有三项发现：',
'literacy rose from 74.6% to 87.6% and tertiary enrolment from 13.3% to 43.2% since 1990; equal credit for reproducible and unseen tasks shifted effort to the cheaper one; intake-matched cohorts transferred more under open-problem regimes':
 '自 1990 年起，识字率由 74.6% 升至 87.6%，高等教育入学率由 13.3% 升至 43.2%；可复现任务与陌生任务同分时，努力转向更便宜的任务；生源匹配的群体在开放问题制度下迁移更多',
"A qualification certifies what schools train students to do, not how many they admit: when assessment rewards reproducible answers, students rehearse recall, and the credential certifies rehearsal rather than transfer. That is the link to the claim — literacy and enrolment can rise while what a qualification proves about unfamiliar work narrows — and the incentive shift and open-problem comparison show that substitution. Opposition's figures track the object, not this certification function.":
 '学历证明的是学校训练学生做的事，而非招了多少人：当评价奖励可复现答案，学生反复操练记忆，学历于是证明的是操练而非迁移。这正是与主张的连接——识字率与入学率可以上升，而学历对陌生工作的证明力却在收窄——激励转移与开放题比较正显示了这种替代。反方的数字追踪的是对象，而非这一证明功能。',
'The measurement objection asks for better transfer data, not another rubric; a gap in size cannot reverse the direction.':
 '测量反驳索要的是更好的迁移数据，而不是另一把尺子；幅度上的缺口无法推翻方向。',
'I reaffirm the institutional extension: incentives, not ability, do the explanatory work.':
 '我重申制度层面的扩展：起解释作用的是激励，不是能力。',

'Madam Speaker, I want to do two things in closing: weigh the standard, then show why a proxy cannot carry the motion.':
 '主席女士，结辩做两件事：衡量标准，再说明为何代理变量承载不了本辩题。',
'The measure never reaches the effect.':'测量始终没有抵达结果。',
'We deny that the case isolates a decline in education rather than a change in how it is measured.':
 '我方否认该论证分离出了「教育下降」，而非「测量方式变化」。',
'The record before the House contains':'本场已有材料包含',
'broader aims, a near-tripling of tertiary participation, survival of transfer without drilling, and no comparable before-and-after transfer data':
 '目标更广、高等教育参与接近三倍、没有操练时迁移仍存在，以及缺乏可比的前后测迁移数据',
'An evaluative claim needs a stable object and a stable measure. Government changed the object by defining good as one capacity, while every link from rewards to that capacity has an alternative explanation or an unmeasured outcome: curriculum expansion, cohort composition and the absence test each survive. Relational argumentation requires the alleged cause to be the best explanation of the effect; the accumulated doubts leave the motion unproven.':
 '评价型主张需要稳定的对象与稳定的测量。政府方把「好」定义为一种能力，已经改动了对象；而从奖励到该能力的每一环，都存在替代解释或未被测量的结果：课程扩容、群体构成与缺席检验都仍然成立。关系型论证要求所声称的原因是结果的最佳解释；累积的疑点使本辩题未获证明。',
'In this evaluative claim, an unstable measure cannot carry a value judgement.':'在这条评价型主张中，不稳定的测量无法承载价值判断。',
'The fixed-standard argument defines away literacy, access and collaboration; a definition that excludes most of education cannot establish that education is worse.':
 '固定标准的主张把读写、入学与协作排除在外；一个排除了教育大部分内容的定义，无法证明教育整体更差。',
'I reaffirm the measurement gap: no comparable before-and-after result was ever offered.':
 '我重申测量缺口：对方从未给出可比的前后测结果。',
'The alleged decline is not the best explanation. We oppose.':'所谓下降并非最佳解释。我方反对。',
}

def attr(s): return html.escape(s,quote=True)
src=open(SRC,encoding='utf-8').read()
pat=re.compile(r'(<(?:p|span)\s+class="[^"]*"[^>]*>)([^<]*)(</(?:p|span)>)')
seen=[]
def repl(m):
    o,text,c=m.group(1),m.group(2),m.group(3)
    key=html.unescape(text).strip()
    if key not in ZH:
        # 结构性小标签：Mode: / Method: 前缀双语化，方法名保留课本原词
        zhkey=None
        if key.startswith('Mode: '): zhkey='模式：'+key[6:]
        elif key.startswith('Method: '): zhkey='方法：'+key[8:]
        if zhkey is None: return m.group(0)
        seen.append(key)
        return (o[:-1]+' data-en="'+attr(key)+'" data-zh="'+attr(zhkey)+'">'
                +'<span class="lang-en">'+html.escape(key)+'</span>'
                +'<span class="lang-zh">'+html.escape(zhkey)+'</span>'+c)
    seen.append(key)
    return (o[:-1]+' data-en="'+attr(key)+'" data-zh="'+attr(ZH[key])+'">'
            +'<span class="lang-en">'+html.escape(key)+'</span>'
            +'<span class="lang-zh">'+html.escape(ZH[key])+'</span>'+c)
out=pat.sub(repl,src)
missing=[k for k in ZH if k not in seen]
print('已挂双语节点',len(seen),'字典中未出现',len(missing))
for k in missing[:10]: print('  MISSING',repr(k[:90]))

CSS_ADD='''
  /* 语言切换：一次 class 切换，不写 textContent，避免整页重绘/字体闪烁 */
  [data-zh]>.lang-zh{display:none}
  body.lang-zh [data-zh]>.lang-en{display:none}
  body.lang-zh [data-zh]>.lang-zh{display:inline}
  /* 按钮文字不进 DOM 文本，避免双串拼接 */
  #langToggle::before{content:"中"}
  body.lang-zh #langToggle::before{content:"EN"}
  body.lang-zh .method::before{content:"方法："}
  @media (max-width:600px){ body.lang-zh .method::before{content:"法："} }
  .win .lang-zh,.cmpGrid .lang-zh,#compare .lang-zh{display:none}
  body.lang-zh .win .lang-en,body.lang-zh .cmpGrid .lang-en,body.lang-zh #compare .lang-en{display:none}
  body.lang-zh .win .lang-zh,body.lang-zh .cmpGrid .lang-zh,body.lang-zh #compare .lang-zh{display:inline}
  /* 滚动条槽常驻：浮层打开时 hidden 不会让整页宽度跳变 */
  html{scrollbar-gutter:stable}
  /* 按钮是标题行内的普通 flex 项：位置由 header 布局决定，与滚动无关 */
  #langToggle{flex:0 0 auto; align-self:center; margin-left:auto;
    font:700 12px/1 "Noto Sans CJK SC","Microsoft YaHei",system-ui,sans-serif;
    color:#fff; background:var(--ink); border:1px solid #8b95a5; border-radius:6px;
    width:46px; height:28px; padding:0; text-align:center; line-height:26px;
    cursor:pointer; letter-spacing:.04em}
  #langToggle:hover{background:#fff; color:var(--ink)}
  @media print{#langToggle{display:none!important}}
'''
# 清理浮层 open() 里的一次性中文写入：全部交给 tagTitles 在显示前一次性生成双语 span
out=out.replace("    ttl.textContent=num(t)+' · '+(t.dataset.title||'')+'   ⇄   '+seat(reb)+(sup?' 的声援':' 的驳论');\n",'')
out=out.replace("left.innerHTML='<div class=\"cmpSeat\">'+seat(t)+(sup?' · 被声援立论 ':' · 被驳立论 ')+num(t)+'</div>'+t.innerHTML;",
                "left.innerHTML='<div class=\"cmpSeat\"></div>'+t.innerHTML;")
out=out.replace("right.innerHTML='<div class=\"cmpSeat\">'+seat(reb)+(sup?' · 本席声援</div>':' · 本席驳论</div>')+reb.innerHTML;",
                "right.innerHTML='<div class=\"cmpSeat\"></div>'+reb.innerHTML;")
assert 'ttl.textContent' not in out and "被驳立论 '+num(t)" not in out
out=out.replace('</style>',CSS_ADD+'</style>',1)
BTN='  <button id="langToggle" type="button" aria-label="切换中英 / Switch language" title="切换中英 / Switch language"></button>\n'
out=out.replace('</header>',BTN+'</header>',1)

JS_ADD='''
  var btn=document.getElementById('langToggle'), zh=false;
  function syncAria(){
    document.querySelectorAll('.lang-en').forEach(function(e){e.setAttribute('aria-hidden',zh?'true':'false')});
    document.querySelectorAll('.lang-zh').forEach(function(e){e.setAttribute('aria-hidden',zh?'false':'true')});
  }
  btn.addEventListener('click',function(){
    zh=!zh;
    document.body.classList.toggle('lang-zh',zh);
    syncAria();
    document.documentElement.lang = zh ? 'zh-CN' : 'en';
    btn.title = zh ? '切换为英文 / Switch to English' : '切换为中文 / Switch to Chinese';
  });
  function tagTitles(t,reb,sup){
    var id=num(t), title=(t.dataset.title||'');
    ttl.innerHTML='<span class="lang-en">'+id+'   ⇄   '+seat(reb)+(sup?' · Support':' · Rebuttal')+'</span>'
                 +'<span class="lang-zh">'+id+' · '+title+'   ⇄   '+seat(reb)+(sup?' 的声援':' 的驳论')+'</span>';
    var lc=left.querySelector('.cmpSeat'), rc=right.querySelector('.cmpSeat');
    if(lc) lc.innerHTML='<span class="lang-en">'+seat(t)+(sup?' · supported point ':' · rebutted point ')+id+'</span>'
                       +'<span class="lang-zh">'+seat(t)+(sup?' · 被声援立论 ':' · 被驳立论 ')+id+'</span>';
    if(rc) rc.innerHTML='<span class="lang-en">'+seat(reb)+(sup?' · support':' · rebuttal')+'</span>'
                       +'<span class="lang-zh">'+seat(reb)+(sup?' · 本席声援':' · 本席驳论')+'</span>';
  }
  syncAria();
'''
old="    ov.hidden=false;document.body.style.overflow='hidden';"
new="    tagTitles(t,reb,sup);\n    syncAria();\n    ov.hidden=false;document.body.style.overflow='hidden';"
assert old in out
out=out.replace(old,new,1)
idx=out.rfind('})();')
out=out[:idx]+JS_ADD+out[idx:]
open(DST,'w',encoding='utf-8').write(out)
print('written',DST,'bytes',len(out))
