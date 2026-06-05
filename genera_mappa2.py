#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MAPPA 2 - "SVADHISTHANA: le corrispondenze del Secondo Chakra".
Companion della Mappa 1 (stesso stile). A4 orizzontale, pronta per stampa.
Contenuti: corrispondenze energetiche, temi/funzioni, squilibri, decodificazione
Hamer (mesoderma antico / cervelletto), pratiche di riequilibrio, domande.
"""
import math

W, H = 1485, 1050

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def wapprox(text, fs, factor=0.58):
    return len(text) * fs * factor

# ---------------- PALETTE (coordinata con Mappa 1)
BG1, BG2, BG3 = "#FFFBF5", "#FFF3E4", "#FBE6CF"
INK = "#5A3216"
NODE_D, NODE_L = "#E85D04", "#FB8B36"

# rami: (chiave, nome, icona, fill_scuro, accento, items)
BRANCHES = [
    ("corr", "CORRISPONDENZE", "droplet", "#EF7011", "#FB9D4D",
     ["Elemento Acqua", "Basso ventre", "Ghiandola gonadi", "Plesso lombare", "Colore arancione", "Mantra VAM"]),
    ("temi", "TEMI E FUNZIONI", "flower", "#E0900C", "#FCC53B",
     ["Emozioni", "Piacere", "Creatività", "Relazioni", "Sessualità", "Movimento"]),
    ("squilibri", "SQUILIBRI", "broken", "#B23A12", "#E5683A",
     ["Senso di colpa", "Vergogna del corpo", "Colpa nel ricevere", "Paura dell'intimità", "Dolori pelvici", "Creatività bloccata"]),
    ("hamer", "DECODIFICA HAMER", "dna", "#7C3A18", "#B26C36",
     ["Mesoderma antico", "Cervelletto", "Protezione", "Attacco all'integrità", "Derma e sierose", "Mammella ghiandolare"]),
    ("riequilibrio", "RIEQUILIBRIO", "sparkle", "#E89A0F", "#FFCB47",
     ["Sentire le emozioni", "Lasciar fluire", "Concedersi piacere", "Acqua e bagni", "Danza del bacino", "Creatività libera"]),
]

PW, PH = 332, 264
POS = {
    "corr":         (78,   35),
    "temi":         (1075, 35),
    "squilibri":    (78,   470),
    "hamer":        (576,  470),
    "riequilibrio": (1075, 470),
}
NODE_CX, NODE_CY, NODE_RX, NODE_RY = 742, 255, 205, 158

S = []
S.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="297mm" height="210mm" '
         f'viewBox="0 0 {W} {H}" font-family="DejaVu Sans, Liberation Sans, sans-serif">')
S.append('<defs>')
S.append(f'''
 <radialGradient id="bg" cx="50%" cy="40%" r="75%">
   <stop offset="0%" stop-color="{BG1}"/><stop offset="60%" stop-color="{BG2}"/><stop offset="100%" stop-color="{BG3}"/>
 </radialGradient>
 <radialGradient id="nodeg" cx="50%" cy="38%" r="72%">
   <stop offset="0%" stop-color="#FFA94D"/><stop offset="55%" stop-color="{NODE_L}"/><stop offset="100%" stop-color="{NODE_D}"/>
 </radialGradient>
 <radialGradient id="glow" cx="50%" cy="50%" r="50%">
   <stop offset="0%" stop-color="#FBC893" stop-opacity="0.75"/>
   <stop offset="70%" stop-color="#FBC893" stop-opacity="0.18"/>
   <stop offset="100%" stop-color="#FBC893" stop-opacity="0"/>
 </radialGradient>
 <filter id="soft" x="-25%" y="-25%" width="150%" height="160%">
   <feDropShadow dx="0" dy="5" stdDeviation="7" flood-color="#8A3B12" flood-opacity="0.20"/>
 </filter>
 <filter id="softsm" x="-40%" y="-40%" width="180%" height="180%">
   <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#8A3B12" flood-opacity="0.22"/>
 </filter>''')
for key, name, icon, deep, acc, items in BRANCHES:
    S.append(f'<linearGradient id="g-{key}" x1="0" y1="0" x2="0" y2="1">'
             f'<stop offset="0%" stop-color="{acc}"/><stop offset="100%" stop-color="{deep}"/></linearGradient>')

# ----- ICONE riutilizzate
S.append('''
 <symbol id="ic-broken" viewBox="0 0 100 100">
   <path d="M50 84 C16 60 7 40 22 26 C34 15 47 19 50 31 C53 19 66 15 78 26 C93 40 84 60 50 84 Z" fill="currentColor"/>
   <path d="M50 24 L43 42 L57 55 L46 70 L51 83" stroke="#fff" stroke-width="5" fill="none" stroke-linejoin="round" stroke-linecap="round"/>
 </symbol>
 <symbol id="ic-waves" viewBox="0 0 100 100">
   <g fill="none" stroke="currentColor" stroke-width="6.5" stroke-linecap="round">
     <path d="M16 36 q9 -12 18 0 q9 12 18 0 q9 -12 18 0"/>
     <path d="M16 54 q9 -12 18 0 q9 12 18 0 q9 -12 18 0"/>
     <path d="M16 72 q9 -12 18 0 q9 12 18 0 q9 -12 18 0"/>
   </g>
 </symbol>
 <symbol id="ic-sparkle" viewBox="0 0 100 100">
   <path d="M46 18 C49 40 52 45 76 48 C52 51 49 56 46 78 C43 56 40 51 16 48 C40 45 43 40 46 18 Z" fill="currentColor"/>
   <path d="M78 20 C79 28 80 30 88 31 C80 32 79 34 78 42 C77 34 76 32 68 31 C76 30 77 28 78 20 Z" fill="currentColor"/>
   <path d="M26 66 C27 72 28 73 34 74 C28 75 27 76 26 82 C25 76 24 75 18 74 C24 73 25 72 26 66 Z" fill="currentColor"/>
 </symbol>''')

# ----- NUOVE ICONE
# goccia
S.append('''
 <symbol id="ic-droplet" viewBox="0 0 100 100">
   <path d="M50 14 C50 32 76 50 76 66 A26 26 0 0 1 24 66 C24 50 50 32 50 14 Z" fill="currentColor"/>
   <ellipse cx="40" cy="64" rx="6" ry="9" fill="#fff" opacity="0.45"/>
 </symbol>''')
# fiore/loto a 6 petali (generato)
petals = []
for k in range(6):
    th = math.radians(k*60 - 90)
    cx = 50 + math.cos(th)*19
    cy = 50 + math.sin(th)*19
    rot = math.degrees(th) + 90
    petals.append(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="9.5" ry="17" '
                  f'transform="rotate({rot:.1f} {cx:.1f} {cy:.1f})" fill="currentColor"/>')
S.append('<symbol id="ic-flower" viewBox="0 0 100 100">' + "".join(petals) +
         '<circle cx="50" cy="50" r="11" fill="#fff"/><circle cx="50" cy="50" r="6" fill="currentColor"/></symbol>')
# dna
S.append('''
 <symbol id="ic-dna" viewBox="0 0 100 100">
   <g fill="none" stroke="currentColor" stroke-linecap="round">
     <path d="M34 18 C66 30 66 46 50 50 C34 54 34 70 66 82" stroke-width="5.5"/>
     <path d="M66 18 C34 30 34 46 50 50 C66 54 66 70 34 82" stroke-width="5.5"/>
     <path d="M41 23 L59 23" stroke-width="4"/><path d="M36 33 L64 33" stroke-width="4"/>
     <path d="M36 67 L64 67" stroke-width="4"/><path d="M41 77 L59 77" stroke-width="4"/>
   </g>
 </symbol>''')
# occhio (auto-osservazione)
S.append('''
 <symbol id="ic-eye" viewBox="0 0 100 100">
   <path d="M12 50 Q50 20 88 50 Q50 80 12 50 Z" fill="none" stroke="currentColor" stroke-width="6" stroke-linejoin="round"/>
   <circle cx="50" cy="50" r="14" fill="currentColor"/><circle cx="45" cy="46" r="4" fill="#fff"/>
 </symbol>''')
S.append('</defs>')

# ---------------- SFONDO
S.append(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')
def dots(cx, cy):
    out=[]
    for (dx,dy,r,op) in [(0,0,7,0.5),(26,10,4,0.4),(14,30,3,0.35),(40,-6,3,0.3),(-4,22,4,0.3)]:
        out.append(f'<circle cx="{cx+dx}" cy="{cy+dy}" r="{r}" fill="#F6B775" opacity="{op}"/>')
    return "".join(out)
S.append(dots(40,40)); S.append(dots(W-70,44)); S.append(dots(44,H-70)); S.append(dots(W-70,H-72))

# loto + glow dietro al nodo
S.append(f'<circle cx="{NODE_CX}" cy="{NODE_CY}" r="305" fill="url(#glow)"/>')
lot=[]
for k in range(6):
    a=math.radians(30+k*60); px=NODE_CX+math.cos(a)*155; py=NODE_CY+math.sin(a)*155
    deg=90+(30+k*60)
    lot.append(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="60" ry="155" transform="rotate({deg:.1f} {px:.1f} {py:.1f})" fill="#F8C28A" opacity="0.30"/>')
S.append('<g>'+"".join(lot)+'</g>')

# ---------------- CONNETTORI
HEADC = {
    "corr":         (POS["corr"][0]+PW/2,         POS["corr"][1]+40),
    "temi":         (POS["temi"][0]+PW/2,         POS["temi"][1]+40),
    "squilibri":    (POS["squilibri"][0]+PW/2,    POS["squilibri"][1]+40),
    "hamer":        (POS["hamer"][0]+PW/2,        POS["hamer"][1]+10),
    "riequilibrio": (POS["riequilibrio"][0]+PW/2, POS["riequilibrio"][1]+40),
}
for key, name, icon, deep, acc, items in BRANCHES:
    hx, hy = HEADC[key]
    cxm = (NODE_CX+hx)/2; cym = NODE_CY+(hy-NODE_CY)*0.15
    S.append(f'<path d="M{NODE_CX} {NODE_CY} Q{cxm:.0f} {cym:.0f} {hx:.0f} {hy:.0f}" '
             f'fill="none" stroke="{acc}" stroke-width="15" stroke-linecap="round" opacity="0.45"/>')

# ---------------- PANNELLI
def panel(key, name, icon, deep, acc, items):
    px, py = POS[key]
    out=[f'<g filter="url(#soft)"><rect x="{px}" y="{py}" width="{PW}" height="{PH}" rx="26" '
         f'fill="#ffffff" stroke="{acc}" stroke-opacity="0.35" stroke-width="1.5"/></g>']
    hx, hy, hw, hh = px+12, py+12, PW-24, 60
    out.append(f'<rect x="{hx}" y="{hy}" width="{hw}" height="{hh}" rx="20" fill="url(#g-{key})"/>')
    bcx, bcy, br = hx+35, hy+hh/2, 21
    out.append(f'<circle cx="{bcx}" cy="{bcy}" r="{br}" fill="#ffffff"/>')
    out.append(f'<use href="#ic-{icon}" x="{bcx-16}" y="{bcy-16}" width="32" height="32" color="{deep}"/>')
    name_fs = 20 if len(name) <= 15 else 19
    out.append(f'<text x="{bcx+br+11}" y="{hy+hh/2+7}" font-size="{name_fs}" font-weight="bold" '
               f'fill="#ffffff" letter-spacing="0.3">{esc(name)}</text>')
    y0 = py + 106
    for i, it in enumerate(items):
        yy = y0 + i*27
        out.append(f'<circle cx="{px+34}" cy="{yy-6}" r="5" fill="{acc}"/>')
        out.append(f'<text x="{px+50}" y="{yy}" font-size="22" fill="{INK}" font-weight="500">{esc(it)}</text>')
    return "".join(out)
for b in BRANCHES:
    S.append(panel(*b))

# ---------------- NODO CENTRALE
S.append(f'<g filter="url(#soft)"><ellipse cx="{NODE_CX}" cy="{NODE_CY}" rx="{NODE_RX}" ry="{NODE_RY}" '
         f'fill="url(#nodeg)" stroke="#ffffff" stroke-width="6"/></g>')
S.append(f'<ellipse cx="{NODE_CX}" cy="{NODE_CY}" rx="{NODE_RX-13}" ry="{NODE_RY-13}" '
         f'fill="none" stroke="#ffffff" stroke-opacity="0.45" stroke-width="2"/>')
S.append(f'<use href="#ic-waves" x="{NODE_CX-30}" y="{NODE_CY-128}" width="60" height="60" color="#ffffff"/>')
S.append(f'<text x="{NODE_CX}" y="{NODE_CY-16}" text-anchor="middle" font-size="42" font-weight="bold" '
         f'fill="#ffffff" letter-spacing="0.5">SVADHISTHANA</text>')
S.append(f'<text x="{NODE_CX}" y="{NODE_CY+24}" text-anchor="middle" font-size="23" font-weight="bold" '
         f'fill="#ffffff" letter-spacing="0.5">2&#176; CHAKRA &#183; SACRALE</text>')
S.append(f'<text x="{NODE_CX}" y="{NODE_CY+62}" text-anchor="middle" font-size="18" '
         f'fill="#FFE6C8" letter-spacing="3" font-weight="500">ACQUA &#183; ARANCIONE &#183; &#8220;IO SENTO&#8221;</text>')

# ---------------- BANNER DOMANDE DI AUTO-OSSERVAZIONE
by, bh = 772, 246
bx, bw = 150, W-300
S.append(f'<g filter="url(#soft)"><rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="30" '
         f'fill="#FFFFFF" stroke="#F2B985" stroke-width="2"/></g>')
S.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="30" fill="none" stroke="#FBD9AE" stroke-width="6" opacity="0.5"/>')
# etichetta
S.append(f'<text x="{W/2}" y="{by+44}" text-anchor="middle" font-size="19" fill="#9A5A2A" '
         f'font-weight="bold" letter-spacing="3">DOMANDE DI AUTO-OSSERVAZIONE</text>')
# due card domanda con icona occhio
QS = ["Mi permetto di provare piacere?", "Riesco a esprimere le mie emozioni?"]
fs_q = 21
eye_d = 50
gap_card = 50
def card_w(t):
    return wapprox(t, fs_q, 0.50) + 46
total = sum(eye_d+10+card_w(t) for t in QS) + gap_card
x = (W - total)/2
cyq = by + 138
ch = 58
for i, t in enumerate(QS):
    ex = x + eye_d/2
    S.append(f'<g filter="url(#softsm)"><circle cx="{ex:.0f}" cy="{cyq}" r="{eye_d/2}" fill="#E89A0F"/></g>')
    S.append(f'<use href="#ic-eye" x="{ex-16:.0f}" y="{cyq-16}" width="32" height="32" color="#ffffff"/>')
    x += eye_d + 10
    cw = card_w(t)
    S.append(f'<rect x="{x:.0f}" y="{cyq-ch/2}" width="{cw:.0f}" height="{ch}" rx="{ch/2}" '
             f'fill="#FFF6E9" stroke="#F2C98C" stroke-width="2"/>')
    S.append(f'<text x="{x+cw/2:.0f}" y="{cyq+8}" text-anchor="middle" font-size="{fs_q}" '
             f'fill="{INK}" font-family="DejaVu Serif, serif" font-style="italic">{esc(t)}</text>')
    x += cw + gap_card
# riga finale mantra
S.append(f'<text x="{W/2}" y="{by+212}" text-anchor="middle" font-size="22" fill="#C2531F" '
         f'font-family="DejaVu Serif, serif" font-style="italic">Quando l\'acqua scorre, l\'emozione si libera e il piacere ritorna.</text>')

S.append('</svg>')
open("svadhisthana-corrispondenze.svg","w",encoding="utf-8").write("\n".join(S))
print("SVG scritto: svadhisthana-corrispondenze.svg")
