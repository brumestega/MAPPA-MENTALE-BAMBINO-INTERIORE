#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pagina A4 orizzontale "CHAKRA & NUMEROLOGIA" - sintesi visiva del report.
Coordinata con le 7 mappe (stessi colori/elementi). Output SVG -> PDF + PNG.
"""
import math, colorsys
W,H = 1485,1050
def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def shade(Hd,S,L):
    r,g,b=colorsys.hls_to_rgb((Hd%360)/360.0,L,S); return "#%02X%02X%02X"%(round(r*255),round(g*255),round(b*255))

IND="#3E3566"; INK="#3A2E2A"; CREAM1="#FFFDFA"; CREAM2="#F4ECE2"

CH=[
 dict(num=1,Hb=2,Sb=0.68,elem="earth",sans="MULADHARA",name="Radice",pet="4",bija="LAM",
   sig="Identit&#224;, inizio, esserci",aff="Io esisto"),
 dict(num=2,Hb=26,Sb=0.85,elem="water",sans="SVADHISTHANA",name="Sacrale",pet="6",bija="VAM",
   sig="Emozione, relazione, dualit&#224;",aff="Io sento"),
 dict(num=3,Hb=45,Sb=0.92,elem="fire",sans="MANIPURA",name="Plesso Solare",pet="10",bija="RAM",
   sig="Creativit&#224;, volont&#224;, gioia",aff="Io posso"),
 dict(num=4,Hb=142,Sb=0.50,elem="air",sans="ANAHATA",name="Cuore",pet="12",bija="YAM",
   sig="Equilibrio, dare e ricevere",aff="Io amo"),
 dict(num=5,Hb=200,Sb=0.78,elem="ether",sans="VISHUDDHA",name="Gola",pet="16",bija="HAM",
   sig="Comunicazione, libert&#224;",aff="Io comunico"),
 dict(num=6,Hb=235,Sb=0.55,elem="light",sans="AJNA",name="Terzo Occhio",pet="2",bija="OM",
   sig="Visione, intuizione, armonia",aff="Io vedo"),
 dict(num=7,Hb=283,Sb=0.48,elem="consciousness",sans="SAHASRARA",name="Corona",pet="1000",bija="OM",
   sig="Spiritualit&#224;, unit&#224;, ricerca",aff="Io comprendo"),
]

def elem_inner(name,col):
    if name=="earth":  return f'<path d="M10 78 L38 30 L54 54 L64 40 L90 78 Z" fill="{col}"/><path d="M38 30 L48 46 L33 46 Z" fill="#fff"/>'
    if name=="water":  return f'<path d="M50 14 C50 32 76 50 76 66 A26 26 0 0 1 24 66 C24 50 50 32 50 14 Z" fill="{col}"/><ellipse cx="40" cy="64" rx="6" ry="9" fill="#fff" opacity="0.5"/>'
    if name=="fire":   return f'<path d="M52 10 C66 32 80 42 74 64 A24 24 0 0 1 26 62 C25 50 34 46 39 38 C42 50 51 47 49 36 C48 27 49 19 52 10 Z" fill="{col}"/><path d="M50 50 C58 58 60 64 56 72 A8 8 0 0 1 42 70 C42 62 47 60 50 50 Z" fill="#fff" opacity="0.6"/>'
    if name=="air":    return f'<g fill="none" stroke="{col}" stroke-width="6.5" stroke-linecap="round"><path d="M16 36 H56 a11 11 0 1 0 -11 -11"/><path d="M16 54 H70 a10 10 0 1 1 -10 10"/><path d="M16 72 H48 a9 9 0 1 0 -9 9"/></g>'
    if name=="ether":  return f'<g fill="none" stroke="{col}" stroke-width="5"><circle cx="50" cy="50" r="30"/><circle cx="50" cy="50" r="17"/></g><circle cx="50" cy="50" r="7" fill="{col}"/>'
    if name=="light":
        s=f'<circle cx="50" cy="50" r="17" fill="{col}"/><g stroke="{col}" stroke-width="6" stroke-linecap="round">'
        for k in range(8): a=math.radians(k*45); s+=f'<line x1="{50+math.cos(a)*24:.1f}" y1="{50+math.sin(a)*24:.1f}" x2="{50+math.cos(a)*33:.1f}" y2="{50+math.sin(a)*33:.1f}"/>'
        return s+'</g>'
    if name=="consciousness":
        s=f'<circle cx="50" cy="50" r="8" fill="{col}"/><circle cx="50" cy="50" r="20" fill="none" stroke="{col}" stroke-width="3.5" opacity="0.85"/><g stroke="{col}" stroke-width="3.2" stroke-linecap="round">'
        for k in range(16): a=math.radians(k*22.5); s+=f'<line x1="{50+math.cos(a)*24:.1f}" y1="{50+math.sin(a)*24:.1f}" x2="{50+math.cos(a)*32:.1f}" y2="{50+math.sin(a)*32:.1f}"/>'
        return s+'</g>'
    return ""

S=[f'<svg xmlns="http://www.w3.org/2000/svg" width="297mm" height="210mm" viewBox="0 0 {W} {H}" font-family="DejaVu Sans, Liberation Sans, sans-serif">']
S.append('<defs>')
S.append(f'<linearGradient id="bgg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="{CREAM1}"/><stop offset="100%" stop-color="{CREAM2}"/></linearGradient>')
stops="".join(f'<stop offset="{i/6*100:.0f}%" stop-color="{shade(c["Hb"],c["Sb"],0.46)}"/>' for i,c in enumerate(CH))
S.append(f'<linearGradient id="rain" x1="0" y1="0" x2="1" y2="0">{stops}</linearGradient>')
S.append('<filter id="sh" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#5A3A22" flood-opacity="0.20"/></filter>')
S.append('<filter id="tsh" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="1.5" stdDeviation="2" flood-color="#2A1500" flood-opacity="0.45"/></filter>')
S.append('</defs>')
S.append(f'<rect width="{W}" height="{H}" fill="url(#bgg)"/>')

# --- banner titolo (arcobaleno) ---
S.append(f'<g filter="url(#sh)"><rect x="55" y="30" width="1375" height="104" rx="26" fill="url(#rain)"/></g>')
S.append(f'<text x="{W/2}" y="86" text-anchor="middle" font-size="44" font-weight="bold" fill="#ffffff" letter-spacing="2" filter="url(#tsh)">CHAKRA &amp; NUMEROLOGIA</text>')
S.append(f'<text x="{W/2}" y="118" text-anchor="middle" font-size="18" fill="#FFF6EC" letter-spacing="2" filter="url(#tsh)">Il linguaggio dei numeri nei sette centri</text>')

# --- intestazione tabella ---
hy=158; hh=46
S.append(f'<rect x="55" y="{hy}" width="1375" height="{hh}" rx="14" fill="{IND}"/>')
hdr=[("N&#176;",95,"middle"),("CHAKRA",205,"start"),("PETALI",537,"middle"),
     ("MANTRA",645,"middle"),("NUMERO &#183; SIGNIFICATO",720,"start"),("AFFERMAZIONE",1150,"start")]
for t,x,anch in hdr:
    S.append(f'<text x="{x}" y="{hy+30}" text-anchor="{anch}" font-size="16" font-weight="bold" fill="#ffffff" letter-spacing="1">{t}</text>')

# --- righe ---
top0=210; rh=77
for i,c in enumerate(CH):
    Hb,Sb=c["Hb"],c["Sb"]
    deep=shade(Hb,Sb,0.42); mid=shade(Hb,Sb,0.50); tint=shade(Hb,Sb,0.955); bord=shade(Hb,Sb,0.66)
    top=top0+i*rh; cy=top+38
    S.append(f'<rect x="60" y="{top+4}" width="1370" height="69" rx="16" fill="{tint}" stroke="{bord}" stroke-opacity="0.55" stroke-width="1.5"/>')
    # numero
    S.append(f'<circle cx="95" cy="{cy}" r="24" fill="{deep}"/><text x="95" y="{cy+10}" text-anchor="middle" font-size="29" font-weight="bold" fill="#ffffff">{c["num"]}</text>')
    # badge elemento + nomi
    S.append(f'<circle cx="170" cy="{cy}" r="22" fill="#ffffff" stroke="{bord}" stroke-opacity="0.5"/>')
    S.append(f'<g transform="translate({170-16},{cy-16}) scale(0.32)">{elem_inner(c["elem"],deep)}</g>')
    S.append(f'<text x="205" y="{cy-3}" font-size="21" font-weight="bold" fill="{deep}" letter-spacing="0.3">{c["sans"]}</text>')
    S.append(f'<text x="206" y="{cy+18}" font-size="14.5" fill="{INK}">{c["num"]}&#176; Chakra &#183; {esc(c["name"])}</text>')
    # petali
    S.append(f'<text x="537" y="{cy+8}" text-anchor="middle" font-size="23" font-weight="bold" fill="{mid}">{c["pet"]}</text>')
    # mantra
    S.append(f'<text x="645" y="{cy+8}" text-anchor="middle" font-size="22" font-weight="bold" fill="{deep}">{c["bija"]}</text>')
    # significato
    S.append(f'<text x="720" y="{cy+8}" font-size="18.5" fill="{INK}">{c["sig"]}</text>')
    # affermazione
    S.append(f'<text x="1150" y="{cy+8}" font-size="20" font-style="italic" fill="{deep}" font-family="DejaVu Serif, serif">&#171;&#160;{esc(c["aff"])}&#160;&#187;</text>')

# --- riquadri sintesi ---
boxes=[
 ("I NUMERI COME SUONO  (tradizione)", [
   ("I petali dei 6 chakra inferiori:",0),
   ("4 + 6 + 10 + 12 + 16 + 2 = 50",1),
   ("le 50 lettere dell&#8217;alfabeto sanscrito",0),
   ("(ogni petalo = un suono / una nadi).",0),
   ("La Corona le ripete &#215;20 &#8594; 1000 petali.",0),
   ("&#200; il legame numero&#8211;suono pi&#249; antico.",0),
 ]),
 ("IL TUO NUMERO DEL PERCORSO DI VITA", [
   ("Somma le cifre della data di nascita",0),
   ("e riducile a una cifra. Esempio:",0),
   ("14&#183;03&#183;1990 &#8594; 1+4+0+3+1+9+9+0 = 27 &#8594; 9",1),
   ("Il numero 1&#8211;7 indica il tuo chakra.",0),
   ("8 &#8594; ottava superiore; 9 &#8594; Corona.",0),
   ("Maestri 11&#183;22&#183;33 non si riducono",0),
   ("(11 Terzo Occhio &#183; 22 Radice+Corona &#183; 33 Cuore).",0),
 ]),
 ("NOTA ONESTA  (fonti)", [
   ("La corrispondenza numero&#8211;chakra (1&#8211;7) e il",0),
   ("&#171;numero del percorso&#187; sono una sintesi",0),
   ("moderna, non antica &#8212; come i colori",0),
   ("arcobaleno (1977). Tradizione vera:",0),
   ("petali, lettere, bija mantra.",0),
   ("Le &#171;frequenze in Hz&#187; sono recenti: il vero",0),
   ("effetto viene da respiro, suono e mantra.",0),
 ]),
]
bx0=55; bw=441; gap=(1375-3*bw)/2; by=772; bh=242
for j,(title,lines) in enumerate(boxes):
    bx=bx0+j*(bw+gap)
    S.append(f'<g filter="url(#sh)"><rect x="{bx:.0f}" y="{by}" width="{bw}" height="{bh}" rx="18" fill="#FFFFFF" stroke="#E7D8C5" stroke-width="1.5"/></g>')
    S.append(f'<rect x="{bx:.0f}" y="{by}" width="{bw}" height="40" rx="18" fill="{IND}"/>')
    S.append(f'<rect x="{bx:.0f}" y="{by+22}" width="{bw}" height="18" fill="{IND}"/>')  # squadra angoli bassi header
    S.append(f'<text x="{bx+bw/2:.0f}" y="{by+26}" text-anchor="middle" font-size="14.5" font-weight="bold" fill="#ffffff" letter-spacing="0.6">{title}</text>')
    ly=by+68
    for txt,emph in lines:
        if emph:
            S.append(f'<text x="{bx+bw/2:.0f}" y="{ly+2}" text-anchor="middle" font-size="18" font-weight="bold" fill="{IND}" font-family="DejaVu Serif, serif">{txt}</text>')
            ly+=27
        else:
            S.append(f'<text x="{bx+20:.0f}" y="{ly}" font-size="14.5" fill="{INK}">{txt}</text>')
            ly+=23

S.append(f'<text x="{W/2}" y="1032" text-anchor="middle" font-size="12.5" fill="#9A6234">Sintesi simbolica per il laboratorio &#183; corrispondenza posizionale 1&#8211;7 &#183; per le fonti vedi il report</text>')
S.append('</svg>')
open("chakra-numerologia.svg","w",encoding="utf-8").write("\n".join(S))
print("scritto chakra-numerologia.svg")
