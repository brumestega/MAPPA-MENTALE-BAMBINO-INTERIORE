#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
7 MEDITAZIONI GUIDATE, una per chakra. Coordinata (colore + elemento) con ogni mappa.
Ogni meditazione e' centrata sui temi del chakra e porta all'ELEVAZIONE DELLA
VIBRAZIONE (luce + mantra bija). NB: non viene usato il termine "guarigione".
Output: meditazione-1..7-*.pdf (A4 verticale) + 7-meditazioni-dei-chakra.pdf + .md
"""
import subprocess, math, colorsys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, PageBreak, Image, Table, TableStyle,
                                KeepTogether, NextPageTemplate, HRFlowable)

def shade(Hdeg, S, L):
    r,g,b = colorsys.hls_to_rgb((Hdeg%360)/360.0, L, S)
    return "#%02X%02X%02X" % (round(r*255),round(g*255),round(b*255))

def pausa(t="(pausa)"):
    return '<font color="%s"><i>%s</i></font>'

# ---------- icone elemento ----------
def light_inner(col):
    s=f'<circle cx="50" cy="50" r="17" fill="{col}"/><g stroke="{col}" stroke-width="6" stroke-linecap="round">'
    for k in range(8):
        a=math.radians(k*45); s+=f'<line x1="{50+math.cos(a)*24:.1f}" y1="{50+math.sin(a)*24:.1f}" x2="{50+math.cos(a)*34:.1f}" y2="{50+math.sin(a)*34:.1f}"/>'
    return s+'</g>'
def cons_inner(col):
    s=f'<circle cx="50" cy="50" r="8" fill="{col}"/><circle cx="50" cy="50" r="20" fill="none" stroke="{col}" stroke-width="3.5" opacity="0.85"/><g stroke="{col}" stroke-width="3.2" stroke-linecap="round">'
    for k in range(16):
        a=math.radians(k*22.5); s+=f'<line x1="{50+math.cos(a)*24:.1f}" y1="{50+math.sin(a)*24:.1f}" x2="{50+math.cos(a)*33:.1f}" y2="{50+math.sin(a)*33:.1f}"/>'
    return s+'</g>'
def elem_inner(name, col):
    if name=="earth":  return f'<path d="M10 78 L38 30 L54 54 L64 40 L90 78 Z" fill="{col}"/><path d="M38 30 L48 46 L33 46 Z" fill="#fff"/>'
    if name=="water":  return f'<path d="M50 14 C50 32 76 50 76 66 A26 26 0 0 1 24 66 C24 50 50 32 50 14 Z" fill="{col}"/><ellipse cx="40" cy="64" rx="6" ry="9" fill="#fff" opacity="0.5"/>'
    if name=="fire":   return f'<path d="M52 10 C66 32 80 42 74 64 A24 24 0 0 1 26 62 C25 50 34 46 39 38 C42 50 51 47 49 36 C48 27 49 19 52 10 Z" fill="{col}"/><path d="M50 50 C58 58 60 64 56 72 A8 8 0 0 1 42 70 C42 62 47 60 50 50 Z" fill="#fff" opacity="0.6"/>'
    if name=="air":    return f'<g fill="none" stroke="{col}" stroke-width="6.5" stroke-linecap="round"><path d="M16 36 H56 a11 11 0 1 0 -11 -11"/><path d="M16 54 H70 a10 10 0 1 1 -10 10"/><path d="M16 72 H48 a9 9 0 1 0 -9 9"/></g>'
    if name=="ether":  return f'<g fill="none" stroke="{col}" stroke-width="5"><circle cx="50" cy="50" r="30"/><circle cx="50" cy="50" r="17"/></g><circle cx="50" cy="50" r="7" fill="{col}"/><g fill="{col}"><circle cx="50" cy="12" r="3"/><circle cx="84" cy="64" r="3"/><circle cx="18" cy="66" r="3"/></g>'
    if name=="light":  return light_inner(col)
    if name=="consciousness": return cons_inner(col)
    return ""
def make_badge(name, deep, path):
    svg=(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">'
         f'<circle cx="50" cy="50" r="49" fill="#ffffff"/>'
         f'<g transform="translate(12,12) scale(0.76)">{elem_inner(name,deep)}</g></svg>')
    open("/tmp/_mb.svg","w").write(svg)
    subprocess.run(["rsvg-convert","-w","300","-h","300","/tmp/_mb.svg","-o",path],check=True)

# ---------- dati 7 chakra ----------
CH = [
 dict(key="muladhara",num=1,sans="MULADHARA",name="Radice",sub="Sicurezza e radicamento",
   Hb=2,Sb=0.68,elem="earth",elabel="TERRA",clabel="ROSSO",affirm="IO ESISTO",bija="LAM",
   loc="alla base della colonna, dove il corpo incontra la terra",cw="rossa",
   ci="come brace viva e calda",close="Sono al sicuro. Appartengo.",
   rel="Forse senti paura, o il bisogno di tenere tutto sotto controllo. Lascia che questi pesi scendano lungo le gambe e si sciolgano nella terra, che tutto accoglie. Le radici ti sostengono: non sei in pericolo, appartieni alla vita."),
 dict(key="svadhisthana",num=2,sans="SVADHISTHANA",name="Sacrale",sub="Emozioni, piacere, creativit&#224;",
   Hb=26,Sb=0.85,elem="water",elabel="ACQUA",clabel="ARANCIONE",affirm="IO SENTO",bija="VAM",
   loc="nel basso ventre, poco sotto l&#8217;ombelico",cw="arancione",
   ci="come un tramonto che si specchia sull&#8217;acqua",close="Mi permetto di sentire e di fluire.",
   rel="Forse trattieni emozioni, o senti colpa nel concederti piacere. Lascia che la luce arancione, come acqua tiepida, sciolga ogni rigidit&#224; nei fianchi e nel ventre. Le emozioni possono muoversi e fluire, libere, senza giudizio."),
 dict(key="manipura",num=3,sans="MANIPURA",name="Plesso Solare",sub="Forza personale e autostima",
   Hb=45,Sb=0.92,elem="fire",elabel="FUOCO",clabel="GIALLO",affirm="IO POSSO",bija="RAM",
   loc="sopra l&#8217;ombelico, nel plesso solare",cw="gialla",
   ci="come un piccolo sole dorato",close="Io posso. Io scelgo.",
   rel="Forse ti critichi, temi il giudizio, ti fai piccolo o piccola. Lascia che il piccolo sole nel ventre sciolga ogni dubbio. Senti crescere il calore della tua forza: hai valore, e puoi scegliere per te."),
 dict(key="anahata",num=4,sans="ANAHATA",name="Cuore",sub="Amore e apertura",
   Hb=142,Sb=0.50,elem="air",elabel="ARIA",clabel="VERDE",affirm="IO AMO",bija="YAM",
   loc="al centro del petto",cw="verde",
   ci="come una foglia al sole del mattino",close="Amo, mi apro, lascio andare.",
   rel="Forse il petto &#232; chiuso dopo una delusione o una perdita. Ad ogni respiro l&#8217;aria apre lo spazio del cuore e allenta la corazza. Puoi lasciar andare ci&#242; che pesa e tornare ad aprirti, con dolcezza."),
 dict(key="vishuddha",num=5,sans="VISHUDDHA",name="Gola",sub="Verit&#224; ed espressione",
   Hb=200,Sb=0.78,elem="ether",elabel="ETERE",clabel="AZZURRO",affirm="IO COMUNICO",bija="HAM",
   loc="nella gola",cw="azzurra",
   ci="limpida come un cielo terso",close="Esprimo la mia verit&#224;.",
   rel="Forse trattieni parole, o fatichi a dire la tua verit&#224;. Senti la luce azzurra sciogliere il nodo alla gola: c&#8217;&#232; spazio per la tua voce, e ci&#242; che senti pu&#242; essere finalmente espresso."),
 dict(key="ajna",num=6,sans="AJNA",name="Terzo Occhio",sub="Intuizione e visione",
   Hb=235,Sb=0.55,elem="light",elabel="LUCE",clabel="INDACO",affirm="IO VEDO",bija="OM",
   loc="tra le sopracciglia",cw="indaco",
   ci="profonda come un cielo notturno",close="Vedo chiaro. Comprendo.",
   rel="Forse la mente &#232; affollata di pensieri e dubiti di ci&#242; che percepisci. Lascia che la luce indaco dissolva la nebbia. Dietro i pensieri c&#8217;&#232; una calma sapienza: la tua intuizione, limpida."),
 dict(key="sahasrara",num=7,sans="SAHASRARA",name="Corona",sub="Connessione e unit&#224;",
   Hb=283,Sb=0.48,elem="consciousness",elabel="COSCIENZA",clabel="VIOLA",affirm="IO COMPRENDO",bija="OM",
   loc="alla sommit&#224; del capo",cw="viola e bianca",
   ci="pura, come luce che scende dall&#8217;alto",close="Sono parte del tutto.",
   rel="Forse ti senti solo o sola, scollegato, senza direzione. Lascia andare il bisogno di capire ogni cosa. La luce che scende dall&#8217;alto dissolve il senso di separazione: nulla di te &#232; davvero diviso dal tutto."),
]

P = lambda t: '<font color="#9A6234"><i>%s</i></font>' % t
def sections(c, pcol):
    pp = lambda t: '<font color="%s"><i>%s</i></font>' % (pcol, t)
    return [
     ("Radicamento e respiro", [
       "Trova una posizione comoda e lascia che il corpo si appoggi, sostenuto. Chiudi dolcemente gli occhi. " + pp("…"),
       "Porta l&#8217;attenzione al respiro: inspira&#8230; ed espira&#8230; Ad ogni espirazione lascia andare un po&#8217; di tensione, e senti il contatto con ci&#242; che ti sostiene. Sei qui, ora. " + pp("(pausa)"),
     ]),
     ("Accendere il centro", [
       f"Porta dolcemente l&#8217;attenzione {c['loc']}. Immagina in quel punto una luce <b>{c['cw']}</b>, calda e viva, {c['ci']}. " + pp("(pausa)"),
       "Ad ogni respiro questa luce diventa pi&#249; limpida e presente, e comincia a pulsare di una vibrazione delicata. " + pp("…"),
     ]),
     ("Riconoscere e lasciar andare", [
       c["rel"] + " " + pp("(pausa lunga)"),
     ]),
     (f"Il suono che eleva &#8212; mantra {c['bija']}", [
       f"Ora accompagna quel centro con il suono. Inspira, e nell&#8217;espirazione lascia vibrare dolcemente il mantra: <b>{c['bija']}</b>&#8230; {c['bija']}&#8230; Senti la vibrazione diffondersi e la luce {c['cw']} farsi pi&#249; brillante ad ogni suono. " + pp("(pausa)"),
       "Ripetilo ancora, anche solo mentalmente. Ad ogni ripetizione la frequenza si alza, leggera, e tutto in te si riallinea in armonia. " + pp("(pausa)"),
     ]),
     ("Espansione", [
       "La luce ora &#232; piena e vibrante. Si espande oltre il corpo, in onde lievi, <b>elevando la tua vibrazione</b> verso una nota pi&#249; alta e luminosa. " + pp("(pausa)"),
       f"Ripeti dentro di te, con dolcezza: <i>&#171;&#160;{c['close']}&#160;&#187;</i> Senti quanto &#232; vero. " + pp("(pausa)"),
     ]),
     ("Integrazione e ritorno", [
       "Lascia che questa vibrazione si stabilizzi dentro di te, come una nota che continua a risuonare. " + pp("(pausa)"),
       "Pian piano riporta l&#8217;attenzione al respiro, al corpo, ai suoni intorno a te. Muovi le dita delle mani e dei piedi, e quando sei pronto o pronta riapri gli occhi, portando con te questa frequenza pi&#249; chiara e viva.",
     ]),
    ]

# ---------- build PDF per chakra ----------
def build_one(c, path):
    Hb,Sb=c["Hb"],c["Sb"]
    deep=shade(Hb,Sb,0.40); mid=shade(Hb,Sb,0.52); acc=shade(Hb,Sb,0.62)
    ink=HexColor(shade(Hb,0.42,0.23)); muted=HexColor(shade(Hb,0.5,0.42))
    cream=HexColor(shade(Hb,0.40,0.975)); tint=HexColor(shade(Hb,0.5,0.94))
    DEEP=HexColor(deep); MID=HexColor(mid); ACC=HexColor(acc); GOLD=HexColor(shade(Hb,Sb,0.46))
    badge=f"/tmp/medc_{c['key']}.png"; make_badge(c["elem"],deep,badge)

    st = dict(
      kick=ParagraphStyle("k",fontName="Helvetica-Bold",fontSize=10,leading=13,textColor=GOLD,alignment=TA_CENTER),
      title=ParagraphStyle("t",fontName="Helvetica-Bold",fontSize=26,leading=30,textColor=DEEP,alignment=TA_CENTER),
      sub=ParagraphStyle("s",fontName="Helvetica",fontSize=13.5,leading=18,textColor=MID,alignment=TA_CENTER),
      tag=ParagraphStyle("g",fontName="Helvetica-Bold",fontSize=10,leading=14,textColor=GOLD,alignment=TA_CENTER,spaceBefore=6),
      h2=ParagraphStyle("h",fontName="Helvetica-Bold",fontSize=14.5,leading=18,textColor=DEEP,spaceBefore=15,spaceAfter=6),
      body=ParagraphStyle("b",fontName="Helvetica",fontSize=12.5,leading=19.5,textColor=ink,alignment=TA_JUSTIFY,spaceAfter=7),
    )
    def bg(canvas,doc,num=True):
        canvas.saveState(); canvas.setFillColor(cream); canvas.rect(0,0,A4[0],A4[1],fill=1,stroke=0)
        dotcol=HexColor(shade(Hb,0.55,0.72))
        for (cx,cy) in [(1.2*cm,A4[1]-1.2*cm),(A4[0]-1.2*cm,A4[1]-1.2*cm),(1.2*cm,1.2*cm),(A4[0]-1.2*cm,1.2*cm)]:
            for (dx,dy,r,op) in [(0,0,5,0.45),(11,5,3,0.35),(5,12,2.4,0.3),(16,-2,2.2,0.25)]:
                canvas.setFillColor(dotcol); canvas.setFillAlpha(op); canvas.circle(cx+dx,cy+dy,r,fill=1,stroke=0)
        canvas.setFillAlpha(1)
        if num:
            canvas.setFillColor(muted); canvas.setFont("Helvetica",8.5)
            canvas.drawCentredString(A4[0]/2,1.0*cm, "Meditazione %d  ·  %s" % (c["num"], c["name"]))
        canvas.restoreState()
    doc=BaseDocTemplate(path,pagesize=A4,leftMargin=2.3*cm,rightMargin=2.3*cm,topMargin=1.8*cm,bottomMargin=1.6*cm,title="Meditazione "+c["name"])
    fr=Frame(doc.leftMargin,doc.bottomMargin,doc.width,doc.height,id="f")
    doc.addPageTemplates([PageTemplate(id="first",frames=[fr],onPage=lambda cv,d: bg(cv,d,False)),
                          PageTemplate(id="later",frames=[fr],onPage=lambda cv,d: bg(cv,d,True))])
    el=[NextPageTemplate("later"), Spacer(1,0.3*cm),
        Image(badge,width=1.7*cm,height=1.7*cm,hAlign="CENTER"), Spacer(1,0.22*cm),
        Paragraph("MEDITAZIONE GUIDATA",st["kick"]),
        Paragraph(c["sans"],st["title"]),
        Paragraph(f'{c["num"]}&#176; Chakra &#183; {c["name"]} &#8212; {c["sub"]}',st["sub"]),
        Paragraph(f'{c["elabel"]} &#183; {c["clabel"]} &#183; &#171;{c["affirm"]}&#187; &#183; mantra {c["bija"]}',st["tag"]),
        Spacer(1,0.18*cm), HRFlowable(width="38%",thickness=2,color=ACC,spaceBefore=2,spaceAfter=10),
       ]
    for i,(h,paras) in enumerate(sections(c, shade(Hb,0.5,0.42)),1):
        block=[Paragraph(f'{i}.&#160;&#160;{h}',st["h2"])]+[Paragraph(p,st["body"]) for p in paras]
        el.append(KeepTogether(block))
    el.append(Spacer(1,0.25*cm))
    el.append(HRFlowable(width="30%",thickness=1.5,color=ACC,spaceBefore=4,spaceAfter=8))
    el.append(Paragraph(f'<i>&#171;&#160;{c["close"]}&#160;&#187;</i>',
              ParagraphStyle("end",fontName="Times-Italic",fontSize=13.5,textColor=DEEP,alignment=TA_CENTER)))
    doc.build(el)

# ---------- markdown combinato ----------
def clean(s):
    import re, html
    s=s.replace("<br/>","\n").replace("<b>","**").replace("</b>","**").replace("<i>","*").replace("</i>","*")
    s=re.sub(r"<font[^>]*>","",s).replace("</font>","")
    return html.unescape(s)

paths=[]
for c in CH:
    p=f'meditazione-{c["num"]}-{c["key"]}.pdf'; build_one(c,p); paths.append(p); print("scritto",p)
subprocess.run(["pdfunite"]+paths+["7-meditazioni-dei-chakra.pdf"],check=True)
print("scritto 7-meditazioni-dei-chakra.pdf")

# md combinato
L=["# 7 Meditazioni dei Chakra","",
   "*Una meditazione per ogni chakra: centrata sui suoi temi, conduce all’elevazione della vibrazione tramite luce e mantra bija.*",""]
for c in CH:
    L.append(f'## {c["num"]}. Meditazione {c["sans"]} — {c["name"]}')
    L.append(f'*{c["elabel"]} · {c["clabel"]} · «{clean(c["affirm"])}» · mantra {c["bija"]} — {clean(c["sub"])}*\n')
    for i,(h,paras) in enumerate(sections(c, shade(c["Hb"],0.5,0.42)),1):
        L.append(f'### {i}. {clean(h)}\n')
        for p in paras: L.append(clean(p)+"\n")
    L.append(f'**« {clean(c["close"])} »**\n')
open("meditazioni-dei-chakra.md","w",encoding="utf-8").write("\n".join(L))
print("scritto meditazioni-dei-chakra.md")
