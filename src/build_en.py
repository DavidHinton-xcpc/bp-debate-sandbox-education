# -*- coding: utf-8 -*-
import re, html, io

# seat, order, name, team, side, whip, role
# op / cl / point(claimType, mode3, technique, tagline, claim, evLead, evidence, warrant, warrantModeNote, avoid)
# plain(tagline,text, methodTag)
# rebs: (target,title,text, methodTag)  methodTag 用课本「Opposing ...」原词
# support: (target,title,text, methodTag) 方法按课本「Creating ...」原词
DATA = [
dict(seat="PM",order=1,name="房俊杰",team="Opening Government",side="gov",whip=False,role="定义 · 立论 · 分工",
 op="Madam Speaker, we are not mourning a golden age; we are asking what a qualification now certifies. I will set a standard, then test it against one incentive.",
 cl="On that standard, the House should support.",
 point=dict(id="PM1",title="标准先行",claimType="evaluative",mode3="Evaluative",tech="Definition / Standard",avoid="规避 · 因果简化",
  tagline="First, fix what counts as good.",
  claim="Education now certificates recall more reliably than transfer.",
  evLead="World Bank data show",
  evidence="world adult literacy rose from 74.6% in 1990 to 87.6% in 2023 while the primary net enrolment rate moved from 82.0% to 89.2% — access improved on both measures",
  warrant="Those figures measure participation and basic skill, not the ability to apply knowledge in a new situation; a system can expand access and simultaneously narrow what its credentials certify. Definition of the object and Standard of judgement must therefore be fixed before any decline is asserted, and on the standard of durable transfer the burden falls on Government to show the incentive changed. This is a claim about an institutional signal, not about teachers' effort.",
  wmode="In this evaluative claim, Definition fixes the object and Standard supplies the yardstick.",
  avoidTxt="not about teachers' effort"),
 plain=[dict(id="PM2",title="制度复现",mode3="Relational",tech="Comparison",avoid="规避 · 后此谬误",
  tagline="Second, compare two assessment regimes.",
  text="Where high-stakes scoring dominates, coursework narrows toward rehearsal; where open problems are assessed, comparable cohorts show more transfer. The recurrence across systems makes the mechanism structural rather than a story about individual failure.",
  method="Comparison")],
 rebs=[],support=None),

dict(seat="LO",order=2,name="耿韵清",team="Opening Opposition",side="opp",whip=False,role="反对立场 · 驳 PM · 立论 · 分工",
 op="Madam Speaker, Government sets a new yardstick, then calls the old one a decline. Two answers.",
 cl="Neither a fair comparison nor a measured fall has been offered. We oppose.",
 point=dict(id="LO1",title="目标扩容",claimType="relational",mode3="Relational",tech="Definition / Alternativity",avoid="规避 · 共因谬误",
  tagline="First, the curriculum changed shape.",
  claim="Expansion of aims is a better explanation of the same observations than decay.",
  evLead="UNESCO learning domains and World Bank series show",
  evidence="tertiary gross enrolment rose from 13.3% in 1990 to 43.2% in 2023, while syllabuses added digital, civic and collaborative competences",
  warrant="Fixed hours spread over more goals redistribute attention rather than destroy it; cohort composition also shifts when participation nearly triples. Both are alternative causes of any apparent change, and neither requires learning to have fallen. Judging today's broader curriculum by yesterday's narrower syllabus mistakes a change of object for a change of quality.",
  wmode="Here, Definition and Alternativity supply competing causes.",
  avoidTxt=""),
 plain=[dict(id="LO2",title="测量人群",mode3="Descriptive",tech="Thoroughness",avoid="规避 · 假类比",
  tagline="Second, ask who is in the average.",
  text="An average over a near-universal cohort is not comparable with one over the selected minority in secondary school a generation ago; a description omitting that shift is not thorough.",
  method="Thoroughness")],
 rebs=[
  dict(target="PM1",title="标准先行",tag="对象错位",text="The fixed-standard argument treats recall as optional, yet recall is the substrate of transfer; defining good as transfer alone begs the question.",method="Intrinsicality"),
  dict(target="PM2",title="制度复现",tag="共存非因果",text="The cross-regime comparison lists coexistences, not a counterfactual with ability and cohort held fixed.",method="Correlativity")],
 support=None),

dict(seat="DPM",order=3,name="海涵",team="Opening Government",side="gov",whip=False,role="驳 LO · 重建 PM · 新增论点 · 小结 OG",
 op="Madam Speaker, I will answer the composition objection, rebuild our standard, then add a mechanism you can observe in one classroom.",
 cl="The standard and the mechanism stand. We support.",
 point=dict(id="DPM1",title="个体权衡",claimType="relational",mode3="Relational",tech="Reduction / Authority",avoid="规避 · 因果简化",
  tagline="First, reduce the claim to one decision.",
  claim="Equal rewards flip one student from understanding to rehearsal.",
  evLead="Behavioural research on incentives, cited as Authority here, finds",
  evidence="when a reproducible answer and an unseen problem earn identical credit, students shift effort toward the cheaper, more predictable task",
  warrant="One student compares two costs for the same credit: understanding takes time and risks failure, rehearsal is cheap and predictable. Repeated across a term the cheaper choice becomes a habit and crowds out practice in transfer before any examination is sat. That micro-level mechanism produces the aggregate pattern PM described, and it survives the access objection, since a change in cohort composition does not change the choice facing any individual student.",
  wmode="In this relational claim, Reduction narrows the causal link and Authority supports it.",
  avoidTxt=""),
 plain=[],
 rebs=[
  dict(target="LO1",title="目标扩容",tag="对象错位",text="The broader-aims objection answers a claim about effort, not one about transfer: adding goals does not explain why equal credit still selects the cheaper route.",method="Absence"),
  dict(target="LO2",title="测量人群",tag="构成不等于结果",text="The access objection shows averages moved, not that transfer within any group fell; composition cannot rescue the standard we set.",method="Measurement")],
 support=dict(target="PM1",title="标准先行",text="I reaffirm the fixed standard: transfer is what makes a qualification worth having.",method="Definition")),

dict(seat="DLO",order=4,name="季佳慧",team="Opening Opposition",side="opp",whip=False,role="驳 DPM 新论点 · 重建 LO · 新增论点 · 小结 OO",
 op="Madam Speaker, the individual calculus assumes what it must prove. Three things: answer it, rebuild our tests, add one more.",
 cl="The mechanism and the standard remain unproven. We oppose.",
 point=dict(id="DLO1",title="缺席检验",claimType="relational",mode3="Relational",tech="Absence",avoid="规避 · 后此谬误",
  tagline="First, learning survives without the old regime.",
  claim="Transferable learning persists where old-style drilling has disappeared.",
  evLead="In curriculum case studies reported by OECD reviews,",
  evidence="students in systems that replaced rote repetition with open tasks still read unfamiliar texts and handle arithmetic in new settings",
  warrant="An effect should be absent when its alleged cause is absent. If application survives without rehearsal, rehearsal was never necessary for learning, and the chain from assessment to lost transfer breaks. Government may still show a marginal shift in what is rewarded, but a marginal shift is not the across-the-board decline the motion asserts; Absence defeats the strong version while leaving the weaker one unproven.",
  wmode="In this relational claim, Absence tests whether the alleged cause is necessary.",
  avoidTxt=""),
 plain=[],
 rebs=[
  dict(target="DPM1",title="个体权衡",tag="前提不成立",text="The equal-reward calculus assumes transfer is harder to grade; where unseen problems are scored, rehearsal is no longer the cheaper route.",method="Intrinsicality"),
  dict(target="PM1",title="标准先行",tag="标准不完整",text="The fixed standard measures one capacity and ignores literacy, access and collaboration, so even a real fall in transfer cannot show education as a whole is worse.",method="Thoroughness")],
 support=dict(target="LO2",title="测量人群",text="I develop the access point: a wider cohort makes any single yardstick less comparable over time.",method="Measurement")),

dict(seat="MG",order=5,name="李佳琪",team="Closing Government",side="gov",whip=False,role="承 OG · 续驳 DLO · 扩展",
 op="Madam Speaker, I take Opening Government's direction as settled. Our extension concerns institutions rather than individuals.",
 cl="Government still explains the change. We support.",
 point=dict(id="MG1",title="制度边际",claimType="relational",mode3="Relational",tech="Comparison",avoid="规避 · 假类比",
  tagline="Our extension: incentives, not ability.",
  claim="Holding ability constant, the assessment regime alone changes what is learned.",
  evLead="Cross-system assessment studies report that",
  evidence="comparable cohorts produce more transfer under open-problem regimes than under reproducible-item regimes, with intake held constant",
  warrant="The same students respond to whatever signal is rewarded. With ability held fixed, the remaining variable is the incentive, so the difference is attributable to the regime rather than to cohort quality or to individual teachers. This extends the individual calculus from one choice to a standing institutional pattern without contradicting it, and it answers the absence objection: transfer surviving without drilling is compatible with transfer falling when rewards change.",
  wmode="In this relational claim, Comparison isolates the incentive by holding ability constant.",
  avoidTxt=""),
 plain=[],
 rebs=[dict(target="DLO1",title="缺席检验",tag="对象错位",text="The absence test targets drilling, not incentives; learning without rehearsal is compatible with learning falling once rewards change.",method="Alternativity")],
 support=dict(target="DPM1",title="个体权衡",text="I develop the individual calculus: repeated choices under the same rewards become the institutional pattern.",method="Reduction")),

dict(seat="MO",order=6,name="李思涵",team="Closing Opposition",side="opp",whip=False,role="承 OO · 续驳 OG · 驳 MG · 扩展",
 op="Madam Speaker, I take Opening Opposition's line as settled. We add one independent gap and answer the institutional extension.",
 cl="The causal chain stops before the claimed effect. We oppose.",
 point=dict(id="MO1",title="测量缺口",claimType="evaluative",mode3="Evaluative",tech="Measurement",avoid="规避 · 共因谬误",
  tagline="Our extension: a proxy is not an outcome.",
  claim="Government proves a change in what is rewarded, not a fall in learning.",
  evLead="The very World Bank series Government cites",
  evidence="reports enrolment and literacy, but contains no before-and-after measure of transfer; the case rests on scoring rules and reported coursework",
  warrant="The motion names a decline in educational quality, which is an outcome. Rewards, rehearsal and course breadth are intermediate proxies; unless they are linked to measured transfer across the same cohort over time, the chain stops before the effect. This gap is independent of the opening-half tests: even if the incentive mechanism is real, its size and direction remain unmeasured, so Opposition need not deny the mechanism to deny the conclusion.",
  wmode="In this evaluative claim, Measurement challenges the proof offered against the standard.",
  avoidTxt=""),
 plain=[],
 rebs=[
  dict(target="MG1",title="制度边际",tag="标尺未固定",text="The institutional extension holds ability constant but not the yardstick; a cohort judged by open problems will look different by construction.",method="Measurement"),
  dict(target="PM2",title="制度复现",tag="无反事实",text="The cross-system comparison lists coexistences, not a counterfactual with assessment held fixed.",method="Correlativity")],
 support=None),

dict(seat="GW",order=7,name="梁程",team="Closing Government",side="gov",whip=True,role="政府方全场总结 · 凸显 MG",
 op="Madam Speaker, education here means the transferable capability that the schooling forms; I reaffirm PM's standard and weigh the record.",
 cl="The direction at the transfer margin is ours. We support.",
 point=dict(id="GW1",title="按标准称重",claimType="evaluative",mode3="Evaluative",tech="Definition / Standard",avoid="规避 · 后此谬误",
  tagline="We reaffirm the standard: what a qualification certifies on unseen tasks.",
  claim="On that standard, education is not as good as it used to be: a qualification now certifies less transferable learning.",
  evLead="Three findings are on the record:",
  evidence="literacy rose from 74.6% to 87.6% and tertiary enrolment from 13.3% to 43.2% since 1990; equal credit for reproducible and unseen tasks shifted effort to the cheaper one; intake-matched cohorts transferred more under open-problem regimes",
  warrant="A qualification certifies what schools train students to do, not how many they admit: when assessment rewards reproducible answers, students rehearse recall, and the credential certifies rehearsal rather than transfer. That is the link to the claim — literacy and enrolment can rise while what a qualification proves about unfamiliar work narrows — and the incentive shift and open-problem comparison show that substitution. Opposition's figures track the object, not this certification function.",
  wmode="",
  avoidTxt=""),
 plain=[],
 rebs=[dict(target="MO1",title="测量缺口",tag="同一尺内之争",text="The measurement objection asks for better transfer data, not another rubric; a gap in size cannot reverse the direction.",method="Standard")],
 support=dict(target="MG1",title="制度边际",text="I reaffirm the institutional extension: incentives, not ability, do the explanatory work.",method="Comparison")),

dict(seat="OW",order=8,name="梁涵",team="Closing Opposition",side="opp",whip=True,role="反方全场总结 · 凸显 MO",
 op="Madam Speaker, I want to do two things in closing: weigh the standard, then show why a proxy cannot carry the motion.",
 cl="The alleged decline is not the best explanation. We oppose.",
 point=dict(id="OW1",title="测量未达",claimType="evaluative",mode3="Evaluative",tech="Definition / Measurement",avoid="规避 · 因果简化",
  tagline="The measure never reaches the effect.",
  claim="We deny that the case isolates a decline in education rather than a change in how it is measured.",
  evLead="The record before the House contains",
  evidence="broader aims, a near-tripling of tertiary participation, survival of transfer without drilling, and no comparable before-and-after transfer data",
  warrant="An evaluative claim needs a stable object and a stable measure. Government changed the object by defining good as one capacity, while every link from rewards to that capacity has an alternative explanation or an unmeasured outcome: curriculum expansion, cohort composition and the absence test each survive. Relational argumentation requires the alleged cause to be the best explanation of the effect; the accumulated doubts leave the motion unproven.",
  wmode="In this evaluative claim, an unstable measure cannot carry a value judgement.",
  avoidTxt=""),
 plain=[],
 rebs=[dict(target="PM1",title="标准先行",tag="定义排除过多",text="The fixed-standard argument defines away literacy, access and collaboration; a definition that excludes most of education cannot establish that education is worse.",method="Thoroughness")],
 support=dict(target="MO1",title="测量缺口",text="I reaffirm the measurement gap: no comparable before-and-after result was ever offered.",method="Measurement")),
]

W=lambda t: re.findall(r"[A-Za-z]+(?:['’-][A-Za-z]+)*",t)
print('每席英文词数（含开场/收尾/tagline/标签/引导词/方法小字/驳论/声援）：')
tot=0
for d in DATA:
    p=d['point']
    parts=[d['op'],d['cl'],p['tagline'],
      'Here is my '+p['claimType']+' argument claim: '+p['claim'],
      'Here is my evidence: '+p['evLead']+' '+p['evidence'],
      'Here is my warrant: '+p['warrant']+' '+p['wmode']]
    for q in d['plain']: parts+= [q['tagline'],q['text']]
    for r in d['rebs']: parts.append(r['text'])
    if d['support']: parts.append(d['support']['text'])
    n=len(W(' '.join(parts))); tot+=n
    print(' ',d['seat'],n,'OK' if n<=230 else 'OVER')
print('合计',tot)

# ---------------- 生成 HTML ----------------
base=open('/home/xiachen/Desktop/BP辩论稿沙盘.html',encoding='utf-8').read()
CSS=re.search(r'<style>(.*?)</style>',base,re.S).group(1)
JS=re.search(r'<script>(.*?)</script>',base,re.S).group(1)
CSS += '''
  .name{font-size:14px; font-weight:700}
  .avoid{font-size:11px; color:#7a2712; border:1px dashed #c98b6a;
         border-radius:10px; padding:1px 7px; margin-left:4px}
  .side{font-size:11px; border:1px solid var(--ink); border-radius:10px; padding:1px 7px}
  .method{font-size:10px; letter-spacing:.02em; color:var(--muted);
          border:1px solid var(--line); border-radius:10px; padding:1px 7px; margin-left:4px}
  .method::before{content:"Method: "; font-weight:700}
  .opp .method{color:#8a3b12; border-color:#e0b89f}
  .evlead{font-style:normal; font-weight:600; color:#0f3d68}
  .opp .evlead{color:#8a3b12}
  .reb{position:relative; margin-top:12px; border:1px dashed var(--accent); background:#fffaf6}
  .reb.support{position:relative; margin-top:12px; border:1px dashed var(--accent); background:#fffaf6}
  .reb.support::before{content:"声援"; position:absolute; left:9px; top:-9px; font-size:10px;
        font-weight:700; color:#fff; background:var(--accent); border-radius:3px; padding:1px 5px}
  .reb .method{background:#fff}
  .cmpCol .method{font-size:calc(10px * var(--pop))}
  .cmpCol .evlead{color:#0f3d68}
  .cmpCol .lbl{color:#0f3d68}
  .cmpCol.right .lbl,.cmpCol.right .evlead{color:#8a3b12}
  /* 移动端适配 */
  @media (max-width:600px){
    body{padding:12px 10px}
    header.top{gap:6px 10px; padding-bottom:10px; margin-bottom:12px; align-items:center}
    h1{font-size:17px; flex:0 0 auto}
    .motion{flex:1 1 100%; order:3; font-size:13px; line-height:1.45; margin-top:2px}
    #langToggle{order:2; width:44px; height:28px}
    .board{gap:10px}
    .seat{padding:10px; overflow:hidden}
    .seat header{gap:5px}
    .seat h2{font-size:15px}
    .name{font-size:13px}
    .team{font-size:10px; letter-spacing:.02em}
    .tag,.avoid,.method{font-size:9.5px; padding:1px 5px; margin-left:2px; white-space:normal}
    .method::before{content:"M: "}
    .tagline.en,.cwe p,.reb p,.op.en,.cl.en{font-size:12px; line-height:1.55; overflow-wrap:anywhere; word-break:break-word}
    .op,.cl{padding-left:38px; font-size:12px}
    .op::before,.cl::before{left:7px}
    .bl,.en{overflow-wrap:anywhere}
    .cwe p{margin:6px 0}
    .item,.reb{padding:7px}
    .to{display:inline-flex; max-width:100%; white-space:normal; font-size:10px}
    .win{width:94vw; height:82vh}
    .cmpGrid{grid-template-columns:1fr; grid-template-rows:1fr 1fr; gap:6px; padding:6px}
    .cmpCol{padding:6px}
    .cmpCol.left{border-top-width:3px}
    .cmpCol.right{border-top-width:3px}
    .close{font-size:12px}
  }
'''

def DISP(i): return i[:-1]+'-'+i[-1]

out=io.StringIO()
out.write('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n')
out.write('<meta name="viewport" content="width=device-width, initial-scale=1">\n')
out.write('<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 16 16\"%3E%3Ctext y=\"13\" font-size=\"13\"%3E%F0%9F%97%A3%3C/text%3E%3C/svg%3E">\n')
out.write('<title>BP 辩论稿沙盘 · Education isn’t as good as it used to be</title>\n')
out.write('<style>'+CSS+'</style>\n</head>\n<body>\n<div class="wrap">\n\n')
out.write('<header class="top">\n  <h1>BP 辩论稿沙盘</h1>\n')
out.write('  <p class="motion">“Education isn’t as good as it used to be.” (p. 75)</p>\n</header>\n\n')
out.write('<main class="board">\n\n')

for d in DATA:
    cls='seat '+d['side']+(' whip' if d['whip'] else '')
    out.write('  <!-- %d %s / %s -->\n'%(d['order'],d['seat'],d['name']))
    out.write('  <article class="%s" data-seat="%s" data-order="%d">\n'%(cls,d['seat'],d['order']))
    out.write('    <header><span class="no">%d</span><h2>%s</h2><span class="name">%s</span>'%(d['order'],d['seat'],d['name']))
    out.write('<span class="team">%s</span><span class="side">%s</span>'%(d['team'],'支持' if d['side']=='gov' else '反对'))
    if d['whip']: out.write('<span class="nonew">不新增论点</span>')
    out.write('</header>\n')
    out.write('    <p class="role">%s</p>\n'%d['role'])
    out.write('    <p class="op en">%s</p>\n\n'%html.escape(d['op']))

    p=d['point']
    out.write('    <div class="item" id="%s" data-title="%s">\n'%(p['id'],p['title']))
    out.write('      <span class="id">%s</span><span class="tag">Mode: %s</span><span class="method">%s</span><span class="avoid">%s</span>\n'%(DISP(p['id']),p['mode3'],p['tech'],p['avoid']))
    out.write('      <p class="tagline en">%s</p>\n'%html.escape(p['tagline']))
    out.write('      <div class="cwe">\n')
    out.write('        <p><span class="lbl en">Here is my %s argument claim:</span> <span class="en">%s</span></p>\n'%(p['claimType'],html.escape(p['claim'])))
    out.write('        <p><span class="lbl en">Here is my evidence:</span> <span class="evlead en">%s</span> <span class="en">%s</span></p>\n'%(html.escape(p['evLead']),html.escape(p['evidence'])))
    out.write('        <p><span class="lbl en">Here is my warrant:</span> <span class="en">%s</span> <span class="en">%s</span></p>\n'%(html.escape(p['warrant']),html.escape(p['wmode'])))
    out.write('      </div>\n    </div>\n\n')

    for q in d['plain']:
        out.write('    <div class="item" id="%s" data-title="%s">\n'%(q['id'],q['title']))
        out.write('      <span class="id">%s</span><span class="tag">Mode: %s</span><span class="method">%s</span><span class="avoid">%s</span>\n'%(DISP(q['id']),q['mode3'],q['method'],q['avoid']))
        out.write('      <p class="tagline en">%s</p>\n'%html.escape(q['tagline']))
        out.write('      <p class="en">%s</p>\n    </div>\n\n'%html.escape(q['text']))

    for r in d['rebs']:
        out.write('    <div class="item reb">\n')
        out.write('      <a class="to" href="#%s" data-target="%s">%s · %s</a><span class="tag">%s</span><span class="method">%s</span>\n'%(r['target'],r['target'],DISP(r['target']),r['title'],r['tag'],r['method']))
        out.write('      <p class="en">%s</p>\n    </div>\n\n'%html.escape(r['text']))

    if d['support']:
        s=d['support']
        out.write('    <div class="item reb support">\n')
        out.write('      <a class="to" href="#%s" data-target="%s">%s · %s</a><span class="tag">声援 · %s</span><span class="method">%s</span>\n'%(s['target'],s['target'],DISP(s['target']),s['title'],d['seat'],s['method']))
        out.write('      <p class="en">%s</p>\n    </div>\n\n'%html.escape(s['text']))

    out.write('    <p class="cl en">%s</p>\n'%html.escape(d['cl']))
    out.write('  </article>\n\n')

out.write('</main>\n\n</div>\n\n')
out.write('''<div class="overlay" id="compare" hidden>
  <div class="win" role="dialog" aria-modal="true" aria-labelledby="cmpTitle">
    <header>
      <h3 id="cmpTitle">立论 ⇄ 驳论 / 声援</h3>
      <button class="close" type="button" data-close>关闭 ✕</button>
    </header>
    <div class="cmpGrid">
      <div class="cmpCol left" id="cmpLeft"></div>
      <div class="cmpCol right" id="cmpRight"></div>
    </div>
  </div>
</div>

''')
JS2=JS.replace("ttl.textContent=num(t)+' · '+(t.dataset.title||'')+'   ⇄   '+seat(reb)+' 的驳论';",
 "var sup=reb.classList.contains('support');\n    ttl.textContent=num(t)+' · '+(t.dataset.title||'')+'   ⇄   '+seat(reb)+(sup?' 的声援':' 的驳论');")\
 .replace("left.innerHTML='<div class=\"cmpSeat\">'+seat(t)+' · 被驳立论 '+num(t)+'</div>'+t.innerHTML;",
 "left.innerHTML='<div class=\"cmpSeat\">'+seat(t)+(sup?' · 被声援立论 ':' · 被驳立论 ')+num(t)+'</div>'+t.innerHTML;")\
 .replace("right.innerHTML='<div class=\"cmpSeat\">'+seat(reb)+' · 本席驳论</div>'+reb.innerHTML;",
 "right.innerHTML='<div class=\"cmpSeat\">'+seat(reb)+(sup?' · 本席声援</div>':' · 本席驳论</div>')+reb.innerHTML;")
assert 'var sup=' in JS2
out.write('<script>'+JS2+'</script>\n</body>\n</html>\n')
open('/home/xiachen/Desktop/BP辩论稿沙盘_教育辩题.html','w',encoding='utf-8').write(out.getvalue())
print('HTML written, bytes:',len(out.getvalue()))
