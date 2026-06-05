#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera la MEDITAZIONE GUIDATA DEL BAMBINO INTERIORE.
Output: PDF impaginato (A4 verticale, stile caldo coordinato) + versione Markdown.
Copione pronto da leggere ad alta voce in un laboratorio di gruppo.
"""
import subprocess, os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, PageBreak, Image, Table, TableStyle, KeepTogether,
                                NextPageTemplate)

# ---------- colori ----------
ORANGE_D = HexColor("#C2531F")
ORANGE   = HexColor("#E8771E")
GOLD     = HexColor("#E0900C")
INK      = HexColor("#43291A")
MUTED    = HexColor("#9A6234")
CREAM    = HexColor("#FFF8F0")
TINT     = HexColor("#FCEBD8")
TINT2    = HexColor("#FFF1E0")

PAUSE = '<font color="#C8732A"><i>{}</i></font>'
def pausa(t="(pausa)"): return PAUSE.format(t)

# ---------- icone decorative (PNG da SVG) ----------
def make_png(svg, path, size=240):
    open("/tmp/_m.svg","w").write(svg)
    subprocess.run(["rsvg-convert","-w",str(size),"-h",str(size),"/tmp/_m.svg","-o",path], check=True)

HEART_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
<path d="M50 84 C16 60 7 40 22 26 C34 15 47 19 50 31 C53 19 66 15 78 26 C93 40 84 60 50 84 Z" fill="#E8771E"/></svg>'''
LOTUS_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
%s<circle cx="50" cy="50" r="10" fill="#fff"/><circle cx="50" cy="50" r="5.5" fill="#E8771E"/></svg>'''
import math
_pet=""
for k in range(6):
    th=math.radians(k*60-90); cx=50+math.cos(th)*19; cy=50+math.sin(th)*19; rot=math.degrees(th)+90
    _pet+=f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="9.5" ry="17" transform="rotate({rot:.1f} {cx:.1f} {cy:.1f})" fill="#E8771E"/>'
make_png(HEART_SVG, "/tmp/med_heart.png", 260)
make_png(LOTUS_SVG % _pet, "/tmp/med_lotus.png", 240)

# ---------- contenuto ----------
TITLE = "Meditazione del Bambino Interiore"
SUBTITLE = "Un viaggio di accoglienza e guarigione"
TAG = "2&#176; CHAKRA  &#183;  SVADHISTHANA  &#183;  ACQUA ED EMOZIONI"

INTRO = ("Questa meditazione accompagna chi la ascolta a incontrare il proprio "
 "bambino interiore: la parte pi&#249; autentica, spontanea e sensibile di noi, che "
 "custodisce la gioia e il gioco, ma anche le ferite delle origini. Attraverso il "
 "respiro e l&#8217;elemento <b>acqua</b> del secondo chakra, lasciamo fluire le emozioni "
 "e offriamo a quel bambino ci&#242; di cui ha bisogno: presenza, ascolto e amore.")

# (titolo sezione, [paragrafi])
SECTIONS = [
 ("Preparazione &#8212; tornare a casa nel corpo", [
   "Trova una posizione comoda, seduta o sdraiata. Lascia che il corpo si appoggi, "
   "completamente sostenuto. Quando te la senti, chiudi dolcemente gli occhi. " + pausa("…"),
   "Porta l&#8217;attenzione al respiro. Non cambiarlo: solo osservalo. Inspira&#8230; ed espira&#8230; "
   "Ad ogni espirazione lascia andare un po&#8217; di tensione: le spalle&#8230; la mascella&#8230; il ventre&#8230; "
   + pausa(),
   "Senti il peso del corpo, il contatto con ci&#242; che ti sostiene. Sei qui. Sei al sicuro. "
   "Non c&#8217;&#232; nulla da fare, nessun luogo in cui andare. Solo essere, per qualche istante. " + pausa("(pausa)"),
 ]),
 ("Il respiro dell&#8217;acqua", [
   "Porta ora una mano sul basso ventre, poco sotto l&#8217;ombelico: &#232; la casa del tuo bambino "
   "interiore, il centro delle emozioni, del piacere e della creativit&#224;.",
   "Immagina in quel punto una luce <b>arancione</b>, calda e morbida, come un tramonto che si "
   "specchia sull&#8217;acqua. Ad ogni respiro questa luce si espande, scioglie ci&#242; che era rigido, "
   "rende tutto pi&#249; fluido. " + pausa(),
   "Ripeti dentro di te, senza fretta: <i>&#171;Mi permetto di sentire. Mi permetto di fluire.&#187;</i> " + pausa("(pausa)"),
 ]),
 ("Il luogo sicuro", [
   "Immagina ora di trovarti in un luogo sicuro e bellissimo. Pu&#242; essere un giardino, una "
   "spiaggia al tramonto, una stanza calda: un posto solo tuo, dove nulla pu&#242; farti del male.",
   "Guarda i colori intorno a te&#8230; ascolta i suoni&#8230; senti la temperatura sulla pelle, la "
   "terra o la sabbia sotto di te. " + pausa(),
   "Poco distante senti il suono dell&#8217;acqua: un ruscello, il mare, una fontana. L&#8217;acqua che "
   "scorre, libera, proprio come le emozioni che qui possono finalmente muoversi. " + pausa("(pausa)"),
 ]),
 ("L&#8217;incontro", [
   "In questo luogo, poco pi&#249; in l&#224;, c&#8217;&#232; qualcuno che ti aspetta. &#200; un bambino. Sei tu, da "
   "piccolo o piccola.",
   "Avvicinati con dolcezza, senza fretta. Osservalo. Quanti anni ha?&#8230; Com&#8217;&#232; vestito?&#8230; "
   "Che espressione ha sul viso?&#8230; Forse sorride, forse &#232; timido, forse tiene gli occhi bassi. "
   "Qualunque cosa provi, va bene cos&#236;. " + pausa(),
   "Mettiti alla sua altezza. Guardalo negli occhi e fagli sapere, semplicemente con la tua "
   "presenza, che sei venuto o venuta apposta per lui. " + pausa("(pausa lunga)"),
 ]),
 ("L&#8217;ascolto", [
   "Chiedigli con tenerezza: <i>&#171;Come stai? Di cosa hai bisogno?&#187;</i> E poi ascolta. Non con la "
   "mente, ma con il cuore. " + pausa(),
   "Forse ha bisogno di essere visto&#8230; di sentirsi al sicuro&#8230; di giocare&#8230; di sbagliare "
   "senza essere giudicato&#8230; di sentirsi amato cos&#236; com&#8217;&#232;.",
   "Forse porta delle ferite: il rifiuto, l&#8217;abbandono, la vergogna, la paura. Lascia che te le "
   "mostri, senza correggerlo, senza spiegare. Solo accogliendo ci&#242; che &#232;. " + pausa("(pausa lunga)"),
 ]),
 ("L&#8217;accoglienza e il dono", [
   "Ora dai a quel bambino esattamente ci&#242; che allora gli &#232; mancato. Scegli le parole che "
   "sente vere:",
   "Se ha avuto paura: <i>&#171;Adesso ci sono io. Sei al sicuro.&#187;</i><br/>"
   "Se si &#232; sentito solo: <i>&#171;Non ti lascer&#242; pi&#249;. Sono qui.&#187;</i><br/>"
   "Se si &#232; vergognato: <i>&#171;Vai benissimo cos&#236; come sei. Ti voglio bene.&#187;</i><br/>"
   "Se non si &#232; sentito visto: <i>&#171;Io ti vedo. Sei importante per me.&#187;</i> " + pausa(),
   "Se lo desidera, prendilo in braccio, abbraccialo, oppure semplicemente tienigli la mano. "
   "Senti il suo calore, il suo respiro che si calma insieme al tuo. " + pausa("(pausa lunga)"),
 ]),
 ("Il gioco e la gioia", [
   "E adesso&#8230; lascia che torni a essere bambino. Invitalo a giocare, a ridere, a correre, a "
   "inventare. Accolto e al sicuro, in lui si riaccende la gioia, la curiosit&#224;, la spontaneit&#224;.",
   "Quella luce arancione nel ventre si fa pi&#249; viva. L&#8217;acqua scorre limpida: le emozioni "
   "fluiscono, la creativit&#224; si libera. Senti quanta vita c&#8217;&#232;, quando ci si sente amati. " + pausa("(pausa)"),
 ]),
 ("L&#8217;integrazione", [
   "Guarda ora il tuo bambino interiore, sereno. Digli che d&#8217;ora in poi camminerete insieme, "
   "che non lo lascerai pi&#249; solo.",
   "Immagina che diventi piccolo come una luce calda e luminosa, e accoglilo dentro di te, nel "
   "cuore o nel ventre, dove star&#224; al sicuro. Non &#232; pi&#249; solo: ha te. E tu hai ritrovato lui. " + pausa(),
   "Ripeti dolcemente: <i>&#171;Mi accolgo. Mi ascolto. Mi voglio bene.&#187;</i> " + pausa("(pausa lunga)"),
 ]),
 ("Il ritorno", [
   "Pian piano riporta l&#8217;attenzione al respiro&#8230; al corpo&#8230; al contatto con ci&#242; che ti "
   "sostiene. Senti i suoni intorno a te.",
   "Muovi dolcemente le dita delle mani e dei piedi. Porta con te questa sensazione, come un "
   "profumo invisibile che ti accompagna. " + pausa(),
   "Quando sei pronto o pronta, con calma, riapri gli occhi. Bentornato, bentornata. "
   "Il tuo bambino interiore &#232; con te. " + pausa("(pausa)"),
 ]),
]

AFFERMAZIONI = [
  "Sono al sicuro: appartengo alla vita.",
  "Mi permetto di sentire e di fluire.",
  "Merito amore cos&#236; come sono.",
  "Mi permetto di giocare e di gioire.",
  "Mi accolgo, mi ascolto, mi voglio bene.",
]

NOTE_FACILITATORE = [
  "<b>Durata:</b> circa 20&#8211;25 minuti, con voce lenta e calda.",
  "<b>Pause:</b> &#8220;&#8230;&#8221; = pausa breve (2&#8211;3 respiri); (pausa) = 5&#8211;8 respiri; (pausa lunga) = fino a un minuto.",
  "<b>Ambiente:</b> luce soffusa e musica dolce di sottofondo (suoni d&#8217;acqua).",
  "<b>Cura:</b> tieni dei fazzoletti a disposizione &#8212; spesso emergono emozioni profonde.",
  "<b>Dopo:</b> se in gruppo, chiudi con una condivisione in cerchio o qualche minuto di scrittura.",
]

# ---------- stili ----------
styles = {
 "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=27, leading=31,
                         textColor=ORANGE_D, alignment=TA_CENTER),
 "subtitle": ParagraphStyle("subtitle", fontName="Helvetica", fontSize=14.5, leading=19,
                         textColor=ORANGE, alignment=TA_CENTER),
 "tag": ParagraphStyle("tag", fontName="Helvetica-Bold", fontSize=10, leading=14,
                         textColor=GOLD, alignment=TA_CENTER, spaceBefore=10),
 "intro": ParagraphStyle("intro", fontName="Helvetica", fontSize=12.5, leading=19,
                         textColor=INK, alignment=TA_JUSTIFY),
 "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=15, leading=19,
                         textColor=ORANGE_D, spaceBefore=17, spaceAfter=7),
 "body": ParagraphStyle("body", fontName="Helvetica", fontSize=12.5, leading=19.5,
                         textColor=INK, alignment=TA_JUSTIFY, spaceAfter=8),
 "affirm": ParagraphStyle("affirm", fontName="Times-Italic", fontSize=13.5, leading=22,
                         textColor=ORANGE_D, alignment=TA_LEFT, leftIndent=6),
 "boxh": ParagraphStyle("boxh", fontName="Helvetica-Bold", fontSize=12.5, leading=16,
                         textColor=ORANGE_D, spaceAfter=4),
 "note": ParagraphStyle("note", fontName="Helvetica", fontSize=11, leading=16,
                         textColor=INK),
 "foot": ParagraphStyle("foot", fontName="Helvetica", fontSize=8.5, textColor=MUTED,
                         alignment=TA_CENTER),
}

def callout(flowables, bg, bar):
    t = Table([[flowables]], colWidths=[16.0*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),bg),
        ("LEFTPADDING",(0,0),(-1,-1),16),("RIGHTPADDING",(0,0),(-1,-1),16),
        ("TOPPADDING",(0,0),(-1,-1),12),("BOTTOMPADDING",(0,0),(-1,-1),12),
        ("LINEBEFORE",(0,0),(0,-1),4,bar),
        ("ROUNDEDCORNERS",[8,8,8,8]),
    ]))
    return t

# ---------- documento ----------
def bg_page(canvas, doc, page_label=True):
    canvas.saveState()
    canvas.setFillColor(CREAM)
    canvas.rect(0,0,A4[0],A4[1],fill=1,stroke=0)
    # puntini decorativi negli angoli
    for (cx,cy) in [(1.2*cm,A4[1]-1.2*cm),(A4[0]-1.2*cm,A4[1]-1.2*cm),(1.2*cm,1.2*cm),(A4[0]-1.2*cm,1.2*cm)]:
        for (dx,dy,r,op) in [(0,0,5,0.45),(11,5,3,0.35),(5,12,2.4,0.30),(16,-2,2.2,0.25)]:
            canvas.setFillColor(HexColor("#F6B775")); canvas.setFillAlpha(op)
            canvas.circle(cx+dx,cy+dy,r,fill=1,stroke=0)
    canvas.setFillAlpha(1)
    if page_label:
        canvas.setFillColor(MUTED)
        canvas.setFont("Helvetica",8.5)
        canvas.drawCentredString(A4[0]/2, 1.0*cm, "Meditazione del Bambino Interiore  ·  %d" % doc.page)
    canvas.restoreState()

def on_first(canvas, doc): bg_page(canvas, doc, page_label=False)
def on_later(canvas, doc): bg_page(canvas, doc, page_label=True)

def build_pdf(path):
    doc = BaseDocTemplate(path, pagesize=A4,
                          leftMargin=2.5*cm, rightMargin=2.5*cm,
                          topMargin=2.0*cm, bottomMargin=1.8*cm, title=TITLE)
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
    doc.addPageTemplates([
        PageTemplate(id="first", frames=[frame], onPage=on_first),
        PageTemplate(id="later", frames=[frame], onPage=on_later),
    ])
    el = []
    el.append(NextPageTemplate("later"))   # dalla pagina 2 in poi: con numero di pagina
    # --- copertina ---
    el.append(Spacer(1, 0.6*cm))
    el.append(Image("/tmp/med_heart.png", width=1.7*cm, height=1.7*cm, hAlign="CENTER"))
    el.append(Spacer(1, 0.35*cm))
    el.append(Paragraph(TITLE, styles["title"]))
    el.append(Spacer(1, 0.15*cm))
    el.append(Paragraph(SUBTITLE, styles["subtitle"]))
    el.append(Paragraph(TAG, styles["tag"]))
    el.append(Spacer(1, 0.5*cm))
    el.append(callout([Paragraph(INTRO, styles["intro"])], TINT2, GOLD))
    el.append(Spacer(1, 0.45*cm))
    el.append(callout(
        [Paragraph("Come usare questa meditazione", styles["boxh"])] +
        [Paragraph("&#8226; "+n, styles["note"]) for n in NOTE_FACILITATORE],
        TINT, ORANGE))
    el.append(PageBreak())
    # passa al template con numero pagina
    el.append(Spacer(1, 0.1*cm))
    # --- sezioni ---
    for i,(h,paras) in enumerate(SECTIONS,1):
        block = [Paragraph(f'{i}.&#160;&#160;{h}', styles["h2"])] + [Paragraph(p, styles["body"]) for p in paras]
        el.append(KeepTogether(block))
    # --- affermazioni ---
    el.append(Spacer(1, 0.3*cm))
    aff = [Paragraph("Affermazioni del bambino interiore", styles["boxh"])] + \
          [Paragraph("&#9825;&#160;&#160;"+a, styles["affirm"]) for a in AFFERMAZIONI]
    el.append(callout(aff, TINT2, ORANGE))
    el.append(Spacer(1, 0.5*cm))
    el.append(Image("/tmp/med_lotus.png", width=1.4*cm, height=1.4*cm, hAlign="CENTER"))
    el.append(Spacer(1, 0.15*cm))
    el.append(Paragraph("<i>Bentornato a casa, bambino mio.</i>",
                        ParagraphStyle("end", parent=styles["subtitle"], fontName="Times-Italic", fontSize=13)))

    doc.build(el)

# ---------- markdown ----------
def clean(s):
    import re, html
    s = s.replace("<br/>","\n").replace("<b>","**").replace("</b>","**").replace("<i>","*").replace("</i>","*")
    s = re.sub(r"<font[^>]*>","",s).replace("</font>","")
    return html.unescape(s)

def build_md(path):
    L=[]
    L.append(f"# {clean(TITLE)}")
    L.append(f"### {clean(SUBTITLE)}")
    L.append(f"*{clean(TAG)}*\n")
    L.append("> " + clean(INTRO).replace("\n"," ") + "\n")
    L.append("**Come usare questa meditazione**\n")
    for n in NOTE_FACILITATORE: L.append("- " + clean(n))
    L.append("")
    for i,(h,paras) in enumerate(SECTIONS,1):
        L.append(f"## {i}. {clean(h)}\n")
        for p in paras: L.append(clean(p)+"\n")
    L.append("## Affermazioni del bambino interiore\n")
    for a in AFFERMAZIONI: L.append(f"- *{clean(a)}*")
    L.append("\n*Bentornato a casa, bambino mio.*")
    open(path,"w",encoding="utf-8").write("\n".join(L))

build_pdf("meditazione-bambino-interiore.pdf")
build_md("meditazione-bambino-interiore.md")
print("FATTO: meditazione-bambino-interiore.pdf + .md")
