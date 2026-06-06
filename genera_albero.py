#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pagina A4 orizzontale: CHAKRA . ALBERO DELLA VITA . TAROCCHI (il ponte ermetico).
Albero della Vita "arcobaleno" (7 chakra sulle Sephirot) + 22 sentieri = 22 Arcani
(struttura 3+7+12). Output SVG -> PDF + PNG.
"""
import math, colorsys
W,H=1485,1050
def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def shade(Hd,S,L):
    r,g,b=colorsys.hls_to_rgb((Hd%360)/360.0,L,S); return "#%02X%02X%02X"%(round(r*255),round(g*255),round(b*255))
IND="#3E3566"; INK="#33291F"; MUT="#7C6A52"
TEAL="#1E9E8F"; GOLD="#D99A07"; VIO="#7E5BBE"   # elementi / pianeti / zodiaco

# colori chakra (Hb,Sb)
CHC={'corona':(283,.48),'terzo':(235,.55),'gola':(200,.78),'cuore':(142,.50),
     'plesso':(45,.92),'sacrale':(26,.85),'radice':(2,.68)}
def cc(k,L=.45): Hb,Sb=CHC[k]; return shade(Hb,Sb,L)

# sephirot: key -> (nome, x, y, chakra)
SEPH={
 'keter':("Keter",357,205,'corona'),
 'chokmah':("Chokmah",455,302,'terzo'),'binah':("Binah",259,302,'terzo'),
 'daat':("Da'at",357,372,'gola'),
 'chesed':("Chesed",455,452,'gola'),'gevurah':("Gevurah",259,452,'gola'),
 'tiferet':("Tiferet",357,548,'cuore'),
 'netzach':("Netzach",455,650,'plesso'),'hod':("Hod",259,650,'plesso'),
 'yesod':("Yesod",357,748,'sacrale'),
 'malkhut':("Malkhut",357,858,'radice'),
}
PATHS=[('keter','chokmah','d'),('keter','binah','d'),('keter','tiferet','v'),
 ('chokmah','binah','h'),('chokmah','tiferet','d'),('chokmah','chesed','v'),
 ('binah','tiferet','d'),('binah','gevurah','v'),
 ('chesed','gevurah','h'),('chesed','tiferet','d'),('chesed','netzach','v'),
 ('gevurah','tiferet','d'),('gevurah','hod','v'),
 ('tiferet','netzach','d'),('tiferet','yesod','v'),('tiferet','hod','d'),
 ('netzach','hod','h'),('netzach','yesod','d'),('netzach','malkhut','d'),
 ('hod','yesod','d'),('hod','malkhut','d'),('yesod','malkhut','v')]
PCOL={'h':TEAL,'v':GOLD,'d':VIO}

# livelli chakra (etichette a sinistra): (y, num, nome, chakra)
LEVELS=[(205,7,"Corona",'corona'),(302,6,"Terzo Occhio",'terzo'),(452,5,"Gola",'gola'),
 (548,4,"Cuore",'cuore'),(650,3,"Plesso Solare",'plesso'),(748,2,"Sacrale",'sacrale'),
 (858,1,"Radice",'radice')]

S=[f'<svg xmlns="http://www.w3.org/2000/svg" width="297mm" height="210mm" viewBox="0 0 {W} {H}" font-family="DejaVu Sans, Liberation Sans, sans-serif">']
S.append('<defs>')
S.append(f'<linearGradient id="bgg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#FFFDFA"/><stop offset="100%" stop-color="#F1ECF4"/></linearGradient>')
S.append(f'<linearGradient id="ban" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="{IND}"/><stop offset="100%" stop-color="#6A4A8A"/></linearGradient>')
S.append('<filter id="sh" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#4A3A2A" flood-opacity="0.18"/></filter>')
S.append('<filter id="tsh" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="1.5" stdDeviation="2" flood-color="#1A0E2A" flood-opacity="0.5"/></filter>')
S.append('</defs>')
S.append(f'<rect width="{W}" height="{H}" fill="url(#bgg)"/>')
# banner
S.append(f'<g filter="url(#sh)"><rect x="40" y="28" width="{W-80}" height="96" rx="24" fill="url(#ban)"/></g>')
S.append(f'<text x="{W/2}" y="74" text-anchor="middle" font-size="38" font-weight="bold" fill="#fff" letter-spacing="2" filter="url(#tsh)">CHAKRA &#183; ALBERO DELLA VITA &#183; TAROCCHI</text>')
S.append(f'<text x="{W/2}" y="105" text-anchor="middle" font-size="16.5" fill="#EADBF6" letter-spacing="1" filter="url(#tsh)">Il ponte ermetico: i 7 chakra sulle Sephirot &#183; i 22 sentieri come Arcani Maggiori</text>')

# ====== CARD ALBERO (sinistra) ======
S.append(f'<g filter="url(#sh)"><rect x="40" y="140" width="555" height="835" rx="22" fill="#ffffff" stroke="#E6DDEE" stroke-width="1.5"/></g>')
S.append(f'<text x="357" y="172" text-anchor="middle" font-size="16" font-weight="bold" fill="{IND}" letter-spacing="1">L&#8217;ALBERO DELLA VITA</text>')
# sentieri
for a,b,g in PATHS:
    x1,y1=SEPH[a][1],SEPH[a][2]; x2,y2=SEPH[b][1],SEPH[b][2]
    S.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{PCOL[g]}" stroke-width="4" stroke-linecap="round" opacity="0.85"/>')
# etichette chakra a sinistra
for y,num,nome,k in LEVELS:
    S.append(f'<circle cx="62" cy="{y}" r="7" fill="{cc(k,.5)}"/>')
    S.append(f'<text x="76" y="{y+5}" font-size="13.5" font-weight="bold" fill="{cc(k,.34)}">{num}&#183; {esc(nome)}</text>')
# Da'at (nascosta, tratteggiata)
dx,dy=SEPH['daat'][1],SEPH['daat'][2]
S.append(f'<circle cx="{dx}" cy="{dy}" r="26" fill="#ffffff" stroke="{cc("gola",.55)}" stroke-width="2" stroke-dasharray="4 4"/>')
S.append(f'<text x="{dx}" y="{dy+4}" text-anchor="middle" font-size="11.5" font-style="italic" fill="{cc("gola",.4)}">Da&#8217;at</text>')
# sephirot
for key,(nome,x,y,k) in SEPH.items():
    if key=='daat': continue
    S.append(f'<circle cx="{x}" cy="{y}" r="34" fill="{cc(k,.46)}" stroke="#ffffff" stroke-width="3"/>')
    S.append(f'<text x="{x}" y="{y+5}" text-anchor="middle" font-size="13" font-weight="bold" fill="#ffffff">{esc(nome)}</text>')
# legenda sentieri
ly=935
S.append(f'<text x="62" y="{ly-12}" font-size="12.5" font-weight="bold" fill="{IND}">I 22 sentieri:</text>')
for i,(col,lab) in enumerate([(TEAL,"3 elementi"),(GOLD,"7 pianeti"),(VIO,"12 zodiaco")]):
    bx=62+i*168
    S.append(f'<line x1="{bx}" y1="{ly+10}" x2="{bx+26}" y2="{ly+10}" stroke="{col}" stroke-width="5" stroke-linecap="round"/>')
    S.append(f'<text x="{bx+34}" y="{ly+15}" font-size="13" fill="{INK}">{lab}</text>')

# ====== DESTRA ======
RX=618; RW=825
# Box A: chakra <-> sephirot
S.append(f'<g filter="url(#sh)"><rect x="{RX}" y="140" width="{RW}" height="250" rx="16" fill="#ffffff" stroke="#E6DDEE" stroke-width="1.5"/></g>')
S.append(f'<rect x="{RX}" y="140" width="{RW}" height="38" rx="16" fill="{IND}"/><rect x="{RX}" y="160" width="{RW}" height="18" fill="{IND}"/>')
S.append(f'<text x="{RX+RW/2}" y="166" text-anchor="middle" font-size="14.5" font-weight="bold" fill="#fff" letter-spacing="0.5">LE 7 CORRISPONDENZE  CHAKRA &#8596; SEPHIROT</text>')
rowsA=[("7","Corona",'corona',"Keter","Corona &#183; Unit&#224; divina"),
 ("6","Terzo Occhio",'terzo',"Chokmah &amp; Binah","Saggezza &#183; Comprensione"),
 ("5","Gola",'gola',"Da&#8217;at / Chesed-Gevurah","Conoscenza &#183; Espressione"),
 ("4","Cuore",'cuore',"Tiferet","Bellezza &#183; Armonia"),
 ("3","Plesso Solare",'plesso',"Netzach &amp; Hod","Slancio &#183; Intelletto"),
 ("2","Sacrale",'sacrale',"Yesod","Fondamento"),
 ("1","Radice",'radice',"Malkhut","Regno &#183; Mondo fisico")]
ry=196
for num,ch,k,sef,sig in rowsA:
    S.append(f'<circle cx="{RX+24}" cy="{ry-4}" r="9" fill="{cc(k,.5)}"/><text x="{RX+20}" y="{ry+1}" text-anchor="middle" font-size="11" font-weight="bold" fill="#fff">{num}</text>')
    S.append(f'<text x="{RX+44}" y="{ry}" font-size="14" font-weight="bold" fill="{cc(k,.34)}">{esc(ch)}</text>')
    S.append(f'<text x="{RX+225}" y="{ry}" font-size="14" font-weight="bold" fill="{INK}">{sef}</text>')
    S.append(f'<text x="{RX+470}" y="{ry}" font-size="13.5" fill="{MUT}">{sig}</text>')
    ry+=27

# Box B: 22 sentieri = 22 Arcani
BY=405; BH=470
S.append(f'<g filter="url(#sh)"><rect x="{RX}" y="{BY}" width="{RW}" height="{BH}" rx="16" fill="#ffffff" stroke="#E6DDEE" stroke-width="1.5"/></g>')
S.append(f'<rect x="{RX}" y="{BY}" width="{RW}" height="38" rx="16" fill="{IND}"/><rect x="{RX}" y="{BY+20}" width="{RW}" height="18" fill="{IND}"/>')
S.append(f'<text x="{RX+RW/2}" y="{BY+26}" text-anchor="middle" font-size="14.5" font-weight="bold" fill="#fff" letter-spacing="0.5">I 22 SENTIERI  =  I 22 ARCANI MAGGIORI</text>')
S.append(f'<text x="{RX+22}" y="{BY+62}" font-size="12.7" fill="{INK}">Ogni sentiero = 1 lettera ebraica = 1 Arcano. Struttura (Sefer Yetzirah): <tspan font-weight="bold">3 + 7 + 12 = 22</tspan>.</text>')
def sub(y,col,txt): S.append(f'<text x="{RX+22}" y="{y}" font-size="13" font-weight="bold" fill="{col}">{txt}</text>')
def line(x,y,txt): S.append(f'<text x="{x}" y="{y}" font-size="12.6" fill="{INK}">{txt}</text>')
y=BY+88
sub(y,TEAL,"3 MADRI &#183; elementi"); y+=21
for t in ["Aleph &#8212; Il Matto &#8212; Aria","Mem &#8212; L&#8217;Appeso &#8212; Acqua","Shin &#8212; Il Giudizio &#8212; Fuoco"]:
    line(RX+34,y,t); y+=18
y+=8; sub(y,GOLD,"7 DOPPIE &#183; pianeti  (&#8776; i 7 chakra)"); y+=21
for t in ["Beth &#8212; Il Mago &#8212; Mercurio","Gimel &#8212; La Papessa &#8212; Luna",
          "Daleth &#8212; L&#8217;Imperatrice &#8212; Venere","Kaph &#8212; La Ruota &#8212; Giove",
          "Peh &#8212; La Torre &#8212; Marte","Resh &#8212; Il Sole &#8212; Sole","Tav &#8212; Il Mondo &#8212; Saturno"]:
    line(RX+34,y,t); y+=18
y+=8; sub(y,VIO,"12 SEMPLICI &#183; zodiaco"); y+=21
col2=[("He &#8212; L&#8217;Imperatore &#8212; Ariete","Lamed &#8212; La Giustizia &#8212; Bilancia"),
 ("Vav &#8212; Il Papa &#8212; Toro","Nun &#8212; La Morte &#8212; Scorpione"),
 ("Zayin &#8212; Gli Amanti &#8212; Gemelli","Samekh &#8212; Temperanza &#8212; Sagittario"),
 ("Cheth &#8212; Il Carro &#8212; Cancro","Ayin &#8212; Il Diavolo &#8212; Capricorno"),
 ("Teth &#8212; La Forza &#8212; Leone","Tzaddi &#8212; La Stella &#8212; Acquario"),
 ("Yod &#8212; L&#8217;Eremita &#8212; Vergine","Qoph &#8212; La Luna &#8212; Pesci")]
for a,b in col2:
    line(RX+34,y,a); line(RX+34+405,y,b); y+=18

# Box C: nota onesta
CY=892
S.append(f'<g filter="url(#sh)"><rect x="{RX}" y="{CY}" width="{RW}" height="83" rx="14" fill="#FBF6EE" stroke="#E8C9A6" stroke-width="1.5"/></g>')
S.append(f'<text x="{RX+20}" y="{CY+26}" font-size="12.8" font-weight="bold" fill="#9A5A2A">Nota onesta</text>')
for i,t in enumerate(["Le Sephirot non &#8220;sono&#8221; i chakra: l&#8217;accostamento &#8212; e i 22 Arcani sui sentieri &#8212; &#232; una sintesi ermetica",
 "moderna (&#201;liphas L&#233;vi, 1800; Golden Dawn, 1888). Bel ponte simbolico, non un&#8217;unica dottrina antica."]):
    S.append(f'<text x="{RX+20}" y="{CY+48+i*19}" font-size="12.6" fill="{INK}">{t}</text>')

S.append('</svg>')
open("chakra-albero-tarocchi.svg","w",encoding="utf-8").write("\n".join(S))
print("scritto chakra-albero-tarocchi.svg")
