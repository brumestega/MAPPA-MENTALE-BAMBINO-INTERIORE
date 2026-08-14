#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SCHEDA DEL CONSULTANTE - foglio A4 verticale da CONSEGNARE alla persona
a fine sessione/consultazione. Coordinato col kit (stessi colori, elementi
e stile delle 7 mappe dei chakra e della mappa del Bambino Interiore).

E' un foglio COMPILABILE A MANO dall'operatore davanti al consultante:
 - Nome / Data
 - Il mio chakra guida  (i 7 chakra da cerchiare)
 - Il filo del Bambino Interiore  (Bambino -> Ferita -> Emozione -> Accoglienza -> Gioia)
 - La mia frase / affermazione
 - La mia pratica della settimana  (3 pratiche + 1 libera, una casella per giorno)
 - Note e intenzione
 - Firma "con cura" dell'operatore

Output: scheda-consultante.svg  ->  .pdf + .png (via cairosvg o rsvg-convert, se presenti).
"""
import math, colorsys, os, subprocess, sys

W, H = 1050, 1485          # A4 verticale (210 x 297 mm) a 5 px/mm
ML, MR = 55, 55            # margini
CW = W - ML - MR           # larghezza contenuto (940)
RX = W - MR                # bordo destro contenuto (995)

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def shade(Hd, S, L):
    r, g, b = colorsys.hls_to_rgb((Hd % 360) / 360.0, L, S)
    return "#%02X%02X%02X" % (round(r * 255), round(g * 255), round(b * 255))

IND  = "#3E3566"   # indaco (intestazioni)
INK  = "#3A2E2A"   # testo
CREAM1, CREAM2 = "#FFFDFA", "#F4ECE2"
MUT  = "#9A6234"   # marrone tenue (note a pie' di pagina)
TAN  = "#C9B79F"   # linee da scrivere / caselle

# --- i 7 chakra (coordinati con genera_numerologia.py / genera_chakra.py) ---
CH = [
 dict(num=1, Hb=2,   Sb=0.68, elem="earth",         sans="MULADHARA",   name="Radice",        bija="LAM", aff="Io esisto"),
 dict(num=2, Hb=26,  Sb=0.85, elem="water",         sans="SVADHISTHANA",name="Sacrale",       bija="VAM", aff="Io sento"),
 dict(num=3, Hb=45,  Sb=0.92, elem="fire",          sans="MANIPURA",    name="Plesso Solare", bija="RAM", aff="Io posso"),
 dict(num=4, Hb=142, Sb=0.50, elem="air",           sans="ANAHATA",     name="Cuore",         bija="YAM", aff="Io amo"),
 dict(num=5, Hb=200, Sb=0.78, elem="ether",         sans="VISHUDDHA",   name="Gola",          bija="HAM", aff="Io comunico"),
 dict(num=6, Hb=235, Sb=0.55, elem="light",         sans="AJNA",        name="Terzo Occhio",  bija="OM",  aff="Io vedo"),
 dict(num=7, Hb=283, Sb=0.48, elem="consciousness", sans="SAHASRARA",   name="Corona",        bija="OM",  aff="Io comprendo"),
]

def elem_inner(name, col):
    """Icona-elemento (viewBox ~100x100), disegnata a mano - stesse forme del kit."""
    if name == "earth":  return f'<path d="M10 78 L38 30 L54 54 L64 40 L90 78 Z" fill="{col}"/><path d="M38 30 L48 46 L33 46 Z" fill="#fff"/>'
    if name == "water":  return f'<path d="M50 14 C50 32 76 50 76 66 A26 26 0 0 1 24 66 C24 50 50 32 50 14 Z" fill="{col}"/><ellipse cx="40" cy="64" rx="6" ry="9" fill="#fff" opacity="0.5"/>'
    if name == "fire":   return f'<path d="M52 10 C66 32 80 42 74 64 A24 24 0 0 1 26 62 C25 50 34 46 39 38 C42 50 51 47 49 36 C48 27 49 19 52 10 Z" fill="{col}"/><path d="M50 50 C58 58 60 64 56 72 A8 8 0 0 1 42 70 C42 62 47 60 50 50 Z" fill="#fff" opacity="0.6"/>'
    if name == "air":    return f'<g fill="none" stroke="{col}" stroke-width="6.5" stroke-linecap="round"><path d="M16 36 H56 a11 11 0 1 0 -11 -11"/><path d="M16 54 H70 a10 10 0 1 1 -10 10"/><path d="M16 72 H48 a9 9 0 1 0 -9 9"/></g>'
    if name == "ether":  return f'<g fill="none" stroke="{col}" stroke-width="5"><circle cx="50" cy="50" r="30"/><circle cx="50" cy="50" r="17"/></g><circle cx="50" cy="50" r="7" fill="{col}"/>'
    if name == "light":
        s = f'<circle cx="50" cy="50" r="17" fill="{col}"/><g stroke="{col}" stroke-width="6" stroke-linecap="round">'
        for k in range(8):
            a = math.radians(k * 45)
            s += f'<line x1="{50+math.cos(a)*24:.1f}" y1="{50+math.sin(a)*24:.1f}" x2="{50+math.cos(a)*33:.1f}" y2="{50+math.sin(a)*33:.1f}"/>'
        return s + '</g>'
    if name == "consciousness":
        s = f'<circle cx="50" cy="50" r="8" fill="{col}"/><circle cx="50" cy="50" r="20" fill="none" stroke="{col}" stroke-width="3.5" opacity="0.85"/><g stroke="{col}" stroke-width="3.2" stroke-linecap="round">'
        for k in range(16):
            a = math.radians(k * 22.5)
            s += f'<line x1="{50+math.cos(a)*24:.1f}" y1="{50+math.sin(a)*24:.1f}" x2="{50+math.cos(a)*32:.1f}" y2="{50+math.sin(a)*32:.1f}"/>'
        return s + '</g>'
    return ""

S = [f'<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" '
     f'viewBox="0 0 {W} {H}" font-family="DejaVu Sans, Liberation Sans, sans-serif">']

# ---------- defs ----------
S.append('<defs>')
S.append(f'<linearGradient id="bgg" x1="0" y1="0" x2="0" y2="1">'
         f'<stop offset="0%" stop-color="{CREAM1}"/><stop offset="100%" stop-color="{CREAM2}"/></linearGradient>')
stops = "".join(f'<stop offset="{i/6*100:.0f}%" stop-color="{shade(c["Hb"],c["Sb"],0.46)}"/>' for i, c in enumerate(CH))
S.append(f'<linearGradient id="rain" x1="0" y1="0" x2="1" y2="0">{stops}</linearGradient>')
# gradiente "dal dolore alla gioia" (bruno tenue -> arancio -> oro)
S.append(f'<linearGradient id="joy" x1="0" y1="0" x2="1" y2="0">'
         f'<stop offset="0%" stop-color="{shade(280,0.25,0.55)}"/>'
         f'<stop offset="50%" stop-color="{shade(26,0.85,0.55)}"/>'
         f'<stop offset="100%" stop-color="{shade(45,0.92,0.52)}"/></linearGradient>')
S.append('<filter id="sh" x="-20%" y="-20%" width="140%" height="160%">'
         '<feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#5A3A22" flood-opacity="0.20"/></filter>')
S.append('<filter id="tsh" x="-30%" y="-30%" width="160%" height="160%">'
         '<feDropShadow dx="0" dy="1.5" stdDeviation="2" flood-color="#2A1500" flood-opacity="0.45"/></filter>')
# loto tenue in filigrana dietro il titolo
S.append('</defs>')
S.append(f'<rect width="{W}" height="{H}" fill="url(#bgg)"/>')

# ---------- helpers di layout ----------
def card(x, y, w, h, rx=18, fill="#FFFFFF", stroke="#E7D8C5", sw=1.5, shadow=True):
    g0 = '<g filter="url(#sh)">' if shadow else '<g>'
    S.append(f'{g0}<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="{rx}" '
             f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/></g>')

def header(x, y, w, title, h=38):
    """Barretta indaco con titolo di sezione (allineato a sinistra)."""
    S.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h}" rx="12" fill="{IND}"/>')
    S.append(f'<text x="{x+18:.0f}" y="{y+h/2+5.5:.0f}" font-size="16" font-weight="bold" '
             f'fill="#ffffff" letter-spacing="1.4">{title}</text>')

def wline(x, y, w, dash=True):
    d = ' stroke-dasharray="1.5 6"' if dash else ''
    S.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x+w:.0f}" y2="{y:.0f}" '
             f'stroke="{TAN}" stroke-width="1.6" stroke-linecap="round"{d}/>')

def label(x, y, t, size=15, col=IND, bold=True, anchor="start", italic=False, serif=False):
    fw = ' font-weight="bold"' if bold else ''
    fi = ' font-style="italic"' if italic else ''
    ff = ' font-family="DejaVu Serif, serif"' if serif else ''
    S.append(f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="{anchor}" font-size="{size}"{fw}{fi}{ff} fill="{col}">{t}</text>')

# ============================================================ BANNER
by = 40; bh = 116
S.append(f'<g filter="url(#sh)"><rect x="{ML}" y="{by}" width="{CW}" height="{bh}" rx="26" fill="url(#rain)"/></g>')
S.append(f'<text x="{W/2}" y="{by+52}" text-anchor="middle" font-size="35" font-weight="bold" '
         f'fill="#ffffff" letter-spacing="2" filter="url(#tsh)">LA TUA MAPPA PERSONALE</text>')
S.append(f'<text x="{W/2}" y="{by+84}" text-anchor="middle" font-size="16.5" '
         f'fill="#FFF6EC" letter-spacing="1.5" filter="url(#tsh)">Un piccolo dono da portare con te, dopo il nostro incontro</text>')

# ============================================================ NOME / DATA
ny = by + bh + 20; nh = 60
card(ML, ny, CW, nh, rx=16)
label(ML+22, ny+38, "Nome", size=16)
wline(ML+92, ny+40, 430)
label(ML+560, ny+38, "Data", size=16)
wline(ML+625, ny+40, RX-(ML+625)-18)

# ============================================================ IL MIO CHAKRA GUIDA
cy0 = ny + nh + 22
header(ML, cy0, CW, "IL MIO CHAKRA GUIDA")
label(RX-8, cy0+27, "cerchia quello che &#232; emerso oggi", size=12.5, col="#EED9C4",
      bold=False, anchor="end", italic=True)
strip_y = cy0 + 38
strip_h = 150
card(ML, strip_y, CW, strip_h, rx=16, fill="#FFFDF9")
n = len(CH)
slot = CW / n
for i, c in enumerate(CH):
    cx = ML + slot*i + slot/2
    cyb = strip_y + 52
    deep = shade(c["Hb"], c["Sb"], 0.44)
    tint = shade(c["Hb"], c["Sb"], 0.95)
    bord = shade(c["Hb"], c["Sb"], 0.66)
    # anello tratteggiato "da cerchiare"
    S.append(f'<circle cx="{cx:.1f}" cy="{cyb}" r="41" fill="none" stroke="{bord}" '
             f'stroke-width="1.6" stroke-dasharray="2 5" opacity="0.8"/>')
    # pastiglia colorata
    S.append(f'<circle cx="{cx:.1f}" cy="{cyb}" r="32" fill="{tint}" stroke="{deep}" stroke-width="2"/>')
    S.append(f'<g transform="translate({cx-19:.1f},{cyb-19}) scale(0.38)">{elem_inner(c["elem"], deep)}</g>')
    # numero in alto a destra della pastiglia
    S.append(f'<circle cx="{cx+27:.1f}" cy="{cyb-25}" r="13" fill="{deep}"/>')
    S.append(f'<text x="{cx+27:.1f}" y="{cyb-20}" text-anchor="middle" font-size="15" '
             f'font-weight="bold" fill="#fff">{c["num"]}</text>')
    # nome + bija + affermazione
    label(cx, strip_y+108, c["name"], size=13.5, col=deep, anchor="middle")
    label(cx, strip_y+127, f'{c["bija"]} &#183; &#171;{esc(c["aff"])}&#187;', size=11.5,
          col=INK, bold=False, anchor="middle", italic=True)

# ============================================================ IL FILO DEL BAMBINO INTERIORE
fy0 = strip_y + strip_h + 22
header(ML, fy0, CW, "IL FILO DEL BAMBINO INTERIORE")
fchips = ["Bambino", "Ferita", "Emozione", "Accoglienza", "Gioia"]
fy = fy0 + 38; fh = 74
card(ML, fy, CW, fh, rx=16, fill="#FFFDF9")
m = len(fchips)
inner = CW - 36
cw = 150;
gap = (inner - cw*m) / (m-1)
for i, t in enumerate(fchips):
    x = ML+18 + i*(cw+gap)
    yc = fy + fh/2
    frac = i/(m-1)
    col = shade(280 - frac*0, 0.25, 0.55) if i == 0 else shade(26 + frac*19, 0.85, 0.52 - frac*0)
    S.append(f'<rect x="{x:.1f}" y="{yc-20:.0f}" width="{cw}" height="40" rx="20" '
             f'fill="{col}"/>')
    label(x+cw/2, yc+6, t, size=16, col="#ffffff", anchor="middle")
    if i < m-1:
        ax = x + cw + gap/2
        S.append(f'<path d="M{ax-11:.1f} {yc} H{ax+9:.1f} M{ax+2:.1f} {yc-6} L{ax+9:.1f} {yc} '
                 f'L{ax+2:.1f} {yc+6}" fill="none" stroke="{MUT}" stroke-width="2.4" '
                 f'stroke-linecap="round" stroke-linejoin="round"/>')

# ============================================================ LA MIA FRASE
ay0 = fy + fh + 22
header(ML, ay0, CW, "LA MIA FRASE")
ah = 86
ay = ay0 + 38
card(ML, ay, CW, ah, rx=16)
label(ML+22, ay+30, "La mia affermazione (quella del mio chakra, o parole mie):",
      size=13.5, col=MUT, bold=False, italic=True)
S.append(f'<text x="{ML+30}" y="{ay+64}" font-size="30" fill="{TAN}" '
         f'font-family="DejaVu Serif, serif">&#171;</text>')
wline(ML+58, ay+66, CW-118)
S.append(f'<text x="{RX-30}" y="{ay+64}" font-size="30" fill="{TAN}" '
         f'font-family="DejaVu Serif, serif" text-anchor="end">&#187;</text>')

# ============================================================ LA MIA PRATICA DELLA SETTIMANA
py0 = ay + ah + 22
header(ML, py0, CW, "LA MIA PRATICA DELLA SETTIMANA")
label(RX-8, py0+27, "una casella per ogni giorno", size=12.5, col="#EED9C4",
      bold=False, anchor="end", italic=True)
pr_y = py0 + 38
practices = [
    ("Respiro dell&#8217;acqua &#8212; 5 minuti", "inspiro lento, espiro pi&#249; lungo"),
    ("Il mio mantra &#8212; 7 volte", "il bija del mio chakra guida"),
    ("Un gesto gentile verso di me", "come lo farei al mio Bambino"),
    ("", ""),   # riga libera
]
row_h = 52
ph = 24 + len(practices)*row_h + 12
card(ML, pr_y, CW, ph, rx=16, fill="#FFFDF9")
days = ["L", "M", "M", "G", "V", "S", "D"]
box = 26; bgap = 12
grid_w = len(days)*box + (len(days)-1)*bgap
grid_x = RX - 20 - grid_w
# intestazione giorni
for k, d in enumerate(days):
    bx = grid_x + k*(box+bgap)
    label(bx+box/2, pr_y+20, d, size=12, col=MUT, anchor="middle")
for r, (t, sub) in enumerate(practices):
    ry = pr_y + 30 + r*row_h
    yc = ry + row_h/2 - 4
    if t:
        label(ML+24, yc-2, t, size=15.5, col=INK, bold=True)
        label(ML+24, yc+16, sub, size=12.5, col=MUT, bold=False, italic=True)
    else:
        label(ML+24, yc-2, "Altro:", size=15.5, col=INK, bold=True)
        wline(ML+90, yc+2, grid_x-20-(ML+90))
    for k in range(len(days)):
        bx = grid_x + k*(box+bgap)
        S.append(f'<rect x="{bx:.0f}" y="{yc-box+6:.0f}" width="{box}" height="{box}" rx="7" '
                 f'fill="#ffffff" stroke="{TAN}" stroke-width="1.5"/>')
    if r < len(practices)-1:
        S.append(f'<line x1="{ML+24}" y1="{ry+row_h-6:.0f}" x2="{RX-24}" y2="{ry+row_h-6:.0f}" '
                 f'stroke="#EEE3D3" stroke-width="1"/>')

# ============================================================ NOTE E INTENZIONE
ty0 = pr_y + ph + 22
header(ML, ty0, CW, "NOTE E INTENZIONE")
ty = ty0 + 38
th = 150
card(ML, ty, CW, th, rx=16)
for k in range(4):
    wline(ML+26, ty+40+k*30, CW-52)

# ============================================================ FIRMA "CON CURA"
sy0 = ty + th + 20
sh = 64
card(ML, sy0, CW, sh, rx=16, fill="#FBF4EA", stroke="#E7D8C5")
label(ML+24, sy0+40, "Con cura,", size=17, col=IND, italic=True, serif=True)
wline(ML+150, sy0+42, 300)
label(ML+150, sy0+58, "operatore / facilitatore", size=11, col=MUT, bold=False, italic=True)
label(RX-235, sy0+40, "Data", size=15)
wline(RX-180, sy0+42, 160)

# ============================================================ FOOTER (disclaimer del kit)
S.append(f'<text x="{W/2}" y="{H-24}" text-anchor="middle" font-size="11.5" fill="{MUT}">'
         f'Strumento simbolico di lavoro interiore in contesto formativo &#183; '
         f'non costituisce indicazione medica o diagnosi</text>')

S.append('</svg>')

svg = "scheda-consultante.svg"
open(svg, "w", encoding="utf-8").write("\n".join(S))
print("scritto", svg)

# ---------- export PDF + PNG (cairosvg se presente, altrimenti rsvg-convert) ----------
def export():
    pdf, png = "scheda-consultante.pdf", "scheda-consultante.png"
    try:
        import cairosvg
        cairosvg.svg2pdf(url=svg, write_to=pdf)
        cairosvg.svg2png(url=svg, write_to=png, dpi=300)
        print("scritto", pdf, "e", png, "(cairosvg)")
        return
    except Exception as e:
        print("cairosvg non disponibile:", e, file=sys.stderr)
    if subprocess.call(["which", "rsvg-convert"], stdout=subprocess.DEVNULL) == 0:
        subprocess.check_call(["rsvg-convert", "-f", "pdf", svg, "-o", pdf])
        subprocess.check_call(["rsvg-convert", "-f", "png", "-d", "300", "-p", "300", svg, "-o", png])
        print("scritto", pdf, "e", png, "(rsvg-convert)")
    else:
        print("Nessun convertitore: rigenerato solo l'SVG.", file=sys.stderr)

export()
