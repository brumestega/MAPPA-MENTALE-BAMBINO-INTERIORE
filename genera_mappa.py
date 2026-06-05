#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera la MAPPA MENTALE "Bambino Interiore e Secondo Chakra (Svadhisthana)".
Output: SVG vettoriale in formato A4 orizzontale, pronto per stampa ad alta risoluzione.
"""

W, H = 1485, 1050  # proporzioni A4 orizzontale (297 x 210 mm)

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def wapprox(text, fs, factor=0.58):
    return len(text) * fs * factor

# ---------------------------------------------------------------- PALETTE
BG1, BG2, BG3 = "#FFFBF5", "#FFF3E4", "#FBE6CF"
INK = "#5A3216"          # testo scuro caldo
NODE_D, NODE_L = "#E85D04", "#FB8B36"

# rami: (chiave, nome, icona, fill_pill_scuro, accento_chiaro, items)
BRANCHES = [
    ("bambino", "BAMBINO INTERIORE", "child", "#E0900C", "#FCC53B",
     ["Gioia", "Gioco", "Curiosità", "Innocenza", "Bisogni", "Vulnerabilità"]),
    ("chakra", "SECONDO CHAKRA", "waves", "#EF7011", "#FB9D4D",
     ["Acqua", "Emozioni", "Piacere", "Creatività", "Relazioni", "Movimento"]),
    ("ferite", "FERITE", "broken", "#B23A12", "#E5683A",
     ["Rifiuto", "Abbandono", "Vergogna", "Critica", "Paura", "Controllo"]),
    ("adulto", "NELL'ADULTO", "cycle", "#7C3A18", "#B26C36",
     ["Chiusura", "Dipendenza", "Giudizio", "Blocchi", "Senso di colpa", "Difficoltà a ricevere"]),
    ("guarigione", "GUARIGIONE", "sparkle", "#E89A0F", "#FFCB47",
     ["Accoglienza", "Ascolto", "Fiducia", "Espressione", "Creatività", "Gioia"]),
]

# posizione pannelli (top-left)
PW, PH = 332, 236
POS = {
    "bambino":    (78,   32),
    "chakra":     (1075, 32),
    "ferite":     (78,   418),
    "adulto":     (576,  418),
    "guarigione": (1075, 418),
}
NODE_CX, NODE_CY, NODE_RX, NODE_RY = 742, 242, 200, 145

S = []  # parti svg

# ============================================================ DEFS
# width/height in mm => pagina A4 orizzontale; viewBox mantiene le coordinate interne
S.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="297mm" height="210mm" '
         f'viewBox="0 0 {W} {H}" font-family="DejaVu Sans, Liberation Sans, sans-serif">')
S.append('<defs>')

S.append(f'''
 <radialGradient id="bg" cx="50%" cy="40%" r="75%">
   <stop offset="0%" stop-color="{BG1}"/>
   <stop offset="60%" stop-color="{BG2}"/>
   <stop offset="100%" stop-color="{BG3}"/>
 </radialGradient>
 <radialGradient id="nodeg" cx="50%" cy="38%" r="72%">
   <stop offset="0%" stop-color="#FFA94D"/>
   <stop offset="55%" stop-color="{NODE_L}"/>
   <stop offset="100%" stop-color="{NODE_D}"/>
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

# gradienti pill per ramo
for key, name, icon, deep, acc, items in BRANCHES:
    S.append(f'''<linearGradient id="g-{key}" x1="0" y1="0" x2="0" y2="1">
   <stop offset="0%" stop-color="{acc}"/><stop offset="100%" stop-color="{deep}"/></linearGradient>''')

# ----- SIMBOLI ICONE
S.append('''
 <symbol id="ic-heart" viewBox="0 0 100 100">
   <path d="M50 84 C16 60 7 40 22 26 C34 15 47 19 50 31 C53 19 66 15 78 26 C93 40 84 60 50 84 Z" fill="currentColor"/>
 </symbol>
 <symbol id="ic-child" viewBox="0 0 100 100">
   <circle cx="50" cy="28" r="6.5" fill="currentColor"/>
   <circle cx="50" cy="55" r="26" fill="currentColor"/>
   <circle cx="41" cy="53" r="3.6" fill="#fff"/><circle cx="59" cy="53" r="3.6" fill="#fff"/>
   <path d="M41 64 Q50 73 59 64" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round"/>
   <circle cx="33" cy="61" r="3.3" fill="#fff" opacity="0.55"/><circle cx="67" cy="61" r="3.3" fill="#fff" opacity="0.55"/>
 </symbol>
 <symbol id="ic-waves" viewBox="0 0 100 100">
   <g fill="none" stroke="currentColor" stroke-width="6.5" stroke-linecap="round">
     <path d="M16 36 q9 -12 18 0 q9 12 18 0 q9 -12 18 0"/>
     <path d="M16 54 q9 -12 18 0 q9 12 18 0 q9 -12 18 0"/>
     <path d="M16 72 q9 -12 18 0 q9 12 18 0 q9 -12 18 0"/>
   </g>
 </symbol>
 <symbol id="ic-broken" viewBox="0 0 100 100">
   <path d="M50 84 C16 60 7 40 22 26 C34 15 47 19 50 31 C53 19 66 15 78 26 C93 40 84 60 50 84 Z" fill="currentColor"/>
   <path d="M50 24 L43 42 L57 55 L46 70 L51 83" stroke="#fff" stroke-width="5" fill="none" stroke-linejoin="round" stroke-linecap="round"/>
 </symbol>
 <symbol id="ic-cycle" viewBox="0 0 100 100">
   <g fill="none" stroke="currentColor" stroke-width="7" stroke-linecap="round">
     <path d="M26 40 A28 28 0 0 1 74 40"/><path d="M74 60 A28 28 0 0 1 26 60"/>
   </g>
   <path d="M74 40 l9 -3 l-3 13 z" fill="currentColor"/>
   <path d="M26 60 l-9 3 l3 -13 z" fill="currentColor"/>
 </symbol>
 <symbol id="ic-sparkle" viewBox="0 0 100 100">
   <path d="M46 18 C49 40 52 45 76 48 C52 51 49 56 46 78 C43 56 40 51 16 48 C40 45 43 40 46 18 Z" fill="currentColor"/>
   <path d="M78 20 C79 28 80 30 88 31 C80 32 79 34 78 42 C77 34 76 32 68 31 C76 30 77 28 78 20 Z" fill="currentColor"/>
   <path d="M26 66 C27 72 28 73 34 74 C28 75 27 76 26 82 C25 76 24 75 18 74 C24 73 25 72 26 66 Z" fill="currentColor"/>
 </symbol>
 <symbol id="ic-hands" viewBox="0 0 100 100">
   <path d="M48 80 C36 76 24 67 21 54 C20 48 24 46 28 50 C28 44 33 43 35 48 C36 43 41 43 42 49 C43 44 48 45 48 51 Z" fill="currentColor"/>
   <path d="M52 80 C64 76 76 67 79 54 C80 48 76 46 72 50 C72 44 67 43 65 48 C64 43 59 43 58 49 C57 44 52 45 52 51 Z" fill="currentColor"/>
   <path d="M50 34 C47 29 40 31 42 37 C43 41 48 44 50 47 C52 44 57 41 58 37 C60 31 53 29 50 34 Z" fill="currentColor" opacity="0.92"/>
 </symbol>''')
S.append('</defs>')

# ============================================================ SFONDO
S.append(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')
# puntini decorativi tenui negli angoli
def dots(cx, cy):
    out = []
    import math
    for (dx, dy, r, op) in [(0,0,7,0.5),(26,10,4,0.4),(14,30,3,0.35),(40,-6,3,0.3),(-4,22,4,0.3)]:
        out.append(f'<circle cx="{cx+dx}" cy="{cy+dy}" r="{r}" fill="#F6B775" opacity="{op}"/>')
    return "".join(out)
S.append(dots(40, 40)); S.append(dots(W-70, 44))
S.append(dots(44, H-70)); S.append(dots(W-70, H-72))

# ============================================================ LOTO + GLOW dietro al nodo
import math
S.append(f'<circle cx="{NODE_CX}" cy="{NODE_CY}" r="290" fill="url(#glow)"/>')
petals = []
for k in range(6):
    a = math.radians(30 + k*60)
    px = NODE_CX + math.cos(a)*150
    py = NODE_CY + math.sin(a)*150
    deg = 90 + (30 + k*60)
    petals.append(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="58" ry="150" '
                  f'transform="rotate({deg:.1f} {px:.1f} {py:.1f})" '
                  f'fill="#F8C28A" opacity="0.30"/>')
S.append('<g>' + "".join(petals) + '</g>')

# ============================================================ CONNETTORI (rami)
HEADC = {  # centro header pannello
    "bambino":    (POS["bambino"][0]+PW/2,    POS["bambino"][1]+40),
    "chakra":     (POS["chakra"][0]+PW/2,     POS["chakra"][1]+40),
    "ferite":     (POS["ferite"][0]+PW/2,     POS["ferite"][1]+40),
    "adulto":     (POS["adulto"][0]+PW/2,     POS["adulto"][1]+10),
    "guarigione": (POS["guarigione"][0]+PW/2, POS["guarigione"][1]+40),
}
for key, name, icon, deep, acc, items in BRANCHES:
    hx, hy = HEADC[key]
    cxm = (NODE_CX + hx)/2
    cym = NODE_CY + (hy-NODE_CY)*0.15
    S.append(f'<path d="M{NODE_CX} {NODE_CY} Q{cxm:.0f} {cym:.0f} {hx:.0f} {hy:.0f}" '
             f'fill="none" stroke="{acc}" stroke-width="15" stroke-linecap="round" opacity="0.45"/>')

# ============================================================ PANNELLI RAMI
def panel(key, name, icon, deep, acc, items):
    px, py = POS[key]
    out = [f'<g filter="url(#soft)">'
           f'<rect x="{px}" y="{py}" width="{PW}" height="{PH}" rx="26" fill="#ffffff" '
           f'stroke="{acc}" stroke-opacity="0.35" stroke-width="1.5"/></g>']
    # header pill
    hx, hy, hw, hh = px+12, py+12, PW-24, 60
    out.append(f'<rect x="{hx}" y="{hy}" width="{hw}" height="{hh}" rx="20" fill="url(#g-{key})"/>')
    # badge icona
    bcx, bcy, br = hx+35, hy+hh/2, 21
    out.append(f'<circle cx="{bcx}" cy="{bcy}" r="{br}" fill="#ffffff"/>')
    out.append(f'<use href="#ic-{icon}" x="{bcx-16}" y="{bcy-16}" width="32" height="32" color="{deep}"/>')
    # nome ramo (dimensione adattata alla lunghezza per restare dentro la pill)
    name_fs = 20 if len(name) <= 15 else 19
    out.append(f'<text x="{bcx+br+11}" y="{hy+hh/2+7}" font-size="{name_fs}" font-weight="bold" '
               f'fill="#ffffff" letter-spacing="0.3">{esc(name)}</text>')
    # items
    y0 = py + 98
    for i, it in enumerate(items):
        yy = y0 + i*25
        out.append(f'<circle cx="{px+34}" cy="{yy-6}" r="5" fill="{acc}"/>')
        out.append(f'<text x="{px+50}" y="{yy}" font-size="21" fill="{INK}" font-weight="500">{esc(it)}</text>')
    return "".join(out)

for b in BRANCHES:
    S.append(panel(*b))

# ============================================================ NODO CENTRALE
S.append(f'<g filter="url(#soft)"><ellipse cx="{NODE_CX}" cy="{NODE_CY}" rx="{NODE_RX}" ry="{NODE_RY}" '
         f'fill="url(#nodeg)" stroke="#ffffff" stroke-width="6"/></g>')
S.append(f'<ellipse cx="{NODE_CX}" cy="{NODE_CY}" rx="{NODE_RX-13}" ry="{NODE_RY-13}" '
         f'fill="none" stroke="#ffffff" stroke-opacity="0.45" stroke-width="2"/>')
S.append(f'<use href="#ic-heart" x="{NODE_CX-29}" y="{NODE_CY-120}" width="58" height="58" color="#ffffff"/>')
S.append(f'<text x="{NODE_CX}" y="{NODE_CY-12}" text-anchor="middle" font-size="38" font-weight="bold" '
         f'fill="#ffffff" letter-spacing="0.5">BAMBINO INTERIORE</text>')
S.append(f'<text x="{NODE_CX}" y="{NODE_CY+32}" text-anchor="middle" font-size="38" font-weight="bold" '
         f'fill="#ffffff" letter-spacing="0.5">E SECONDO CHAKRA</text>')
S.append(f'<text x="{NODE_CX}" y="{NODE_CY+74}" text-anchor="middle" font-size="20" '
         f'fill="#FFE6C8" letter-spacing="6" font-weight="500">S V A D H I S T H A N A</text>')

# ============================================================ STRISCE COLLEGAMENTI
def arrow(x1, y, x2, col, sw=4):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2-9}" y2="{y}" stroke="{col}" stroke-width="{sw}" stroke-linecap="round"/>'
            f'<path d="M{x2} {y} l-12 -7 l0 14 z" fill="{col}"/>')

def chain(cy, icon, icon_deep, items, chip_fill, chip_text, chip_border, arrow_col):
    fs = 22
    chip_h = 52
    pad = 22
    gap_arrow = 40
    # misura
    widths = [wapprox(t, fs, 0.60) + pad*2 for t in items]
    icd = 58  # diametro cerchio icona
    total = icd + 18 + sum(widths) + gap_arrow*len(items)
    x = (W - total)/2
    out = []
    # cerchio icona iniziale
    icx = x + icd/2
    out.append(f'<g filter="url(#softsm)"><circle cx="{icx:.0f}" cy="{cy}" r="{icd/2}" fill="{icon_deep}"/></g>')
    out.append(f'<use href="#ic-{icon}" x="{icx-19:.0f}" y="{cy-19}" width="38" height="38" color="#ffffff"/>')
    x += icd + 18
    for i, t in enumerate(items):
        w = widths[i]
        out.append(f'<rect x="{x:.0f}" y="{cy-chip_h/2}" width="{w:.0f}" height="{chip_h}" rx="{chip_h/2}" '
                   f'fill="{chip_fill}" stroke="{chip_border}" stroke-width="2"/>')
        out.append(f'<text x="{x+w/2:.0f}" y="{cy+8}" text-anchor="middle" font-size="{fs}" '
                   f'font-weight="bold" fill="{chip_text}" letter-spacing="0.5">{esc(t)}</text>')
        x += w
        if i < len(items)-1:
            out.append(arrow(x+8, cy, x+gap_arrow-6, arrow_col, 4))
            x += gap_arrow
    return "".join(out)

# titoletto delle due catene
S.append(f'<text x="{W/2}" y="690" text-anchor="middle" font-size="19" fill="#9A5A2A" '
         f'font-weight="bold" letter-spacing="3">DAL DOLORE ALLA GIOIA</text>')

# catena ferita (toni terracotta)
S.append(chain(730, "broken", "#B23A12",
               ["FERITA", "EMOZIONE BLOCCATA", "DIFESA", "COMPORTAMENTO ADULTO"],
               "#FBE3D6", "#9A3010", "#E8A98E", "#C2531F"))
# catena guarigione (toni oro)
S.append(chain(804, "hands", "#E0900C",
               ["ACCOGLIENZA", "GUARIGIONE", "FLUIDITÀ", "GIOIA"],
               "#FDEFCF", "#9A6206", "#F1C879", "#E0900C"))

# ============================================================ BANNER FRASE FINALE
by, bh = 856, 164
bx, bw = 150, W-300
S.append(f'<g filter="url(#soft)"><rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="30" '
         f'fill="#FFFFFF" stroke="#F2B985" stroke-width="2"/></g>')
S.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="30" fill="none" '
         f'stroke="#FBD9AE" stroke-width="6" opacity="0.5"/>')

flow = [
    ("Bambino", "child", "#E0900C"),
    ("Ferita", "broken", "#B23A12"),
    ("Emozione", "waves", "#EF7011"),
    ("Accoglienza", "hands", "#E0650E"),
    ("Gioia", "sparkle", "#E89A0F"),
]
icd = 70
n = len(flow)
gapA = 124
total = n*icd + (n-1)*gapA
x = (W - total)/2
cyc = by + 60
centers = []
for i, (lab, icon, col) in enumerate(flow):
    cx = x + icd/2
    centers.append((cx, lab, col))
    S.append(f'<g filter="url(#softsm)"><circle cx="{cx:.0f}" cy="{cyc}" r="{icd/2}" fill="{col}" '
             f'stroke="#ffffff" stroke-width="3"/></g>')
    S.append(f'<use href="#ic-{icon}" x="{cx-22:.0f}" y="{cyc-22}" width="44" height="44" color="#ffffff"/>')
    x += icd
    if i < n-1:
        S.append(arrow(x+20, cyc, x+gapA-20, "#D9772B", 5))
        x += gapA

# riga parole (frase tra virgolette), allineata sotto le icone
wy = by + 135
S.append(f'<text x="{centers[0][0]-74:.0f}" y="{wy+6}" font-size="46" fill="#E08A2A" '
         f'font-family="DejaVu Serif, serif" font-weight="bold">&#8220;</text>')
for i, (cx, lab, col) in enumerate(centers):
    S.append(f'<text x="{cx:.0f}" y="{wy}" text-anchor="middle" font-size="23" font-weight="bold" '
             f'fill="{INK}" font-family="DejaVu Serif, serif">{esc(lab)}</text>')
    if i < len(centers)-1:
        midx = (centers[i][0]+centers[i+1][0])/2
        S.append(f'<text x="{midx:.0f}" y="{wy-3}" text-anchor="middle" font-size="21" '
                 f'fill="#D9772B" font-weight="bold">&#8594;</text>')
S.append(f'<text x="{centers[-1][0]+62:.0f}" y="{wy+6}" font-size="46" fill="#E08A2A" '
         f'font-family="DejaVu Serif, serif" font-weight="bold">&#8221;</text>')

S.append('</svg>')

with open("mappa-mentale-bambino-interiore.svg", "w", encoding="utf-8") as f:
    f.write("\n".join(S))
print("SVG scritto:", "mappa-mentale-bambino-interiore.svg")
