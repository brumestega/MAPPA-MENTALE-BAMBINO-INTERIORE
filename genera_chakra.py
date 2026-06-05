#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera le 7 MAPPE DELLE CORRISPONDENZE, una per ciascun chakra.
Stile coordinato (come la mappa Svadhisthana), ma color-codato sul colore del
singolo chakra. A4 orizzontale, pronte per la stampa.
Fonti: documento sui 7 chakra + tabella corrispondenze/Hamer forniti dall'utente.
"""
import math, colorsys

W, H = 1485, 1050

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def wapprox(text, fs, factor=0.55):
    return len(text) * fs * factor

def hx(r, g, b):
    return "#%02X%02X%02X" % (max(0,min(255,round(r*255))), max(0,min(255,round(g*255))), max(0,min(255,round(b*255))))

def shade(Hdeg, S, L):
    r, g, b = colorsys.hls_to_rgb((Hdeg % 360)/360.0, L, S)
    return hx(r, g, b)

# --------- DATI DEI 7 CHAKRA ----------
CHAKRAS = [
 dict(key="muladhara", num=1, sans="MULADHARA", name="RADICE", Hb=2, Sb=0.68,
   elem="earth", elabel="TERRA", clabel="ROSSO", affirm="IO ESISTO",
   closing="Sono al sicuro. Appartengo.",
   corr=["Elemento Terra","Base colonna","Surrenali","Plesso sacrale","Colore rosso","Mantra LAM"],
   temi=["Sicurezza","Stabilità","Radicamento","Sopravvivenza","Fiducia","Appartenenza"],
   squ=["Paura, ansia","Iper-controllo","Insicurezza","Lombalgia","Gambe pesanti","Colon irritabile"],
   hamer=["Endoderma","Tronco encefalico","Sopravvivenza","Boccone, profugo","Intestino, reni","Paura di morte"],
   rieq=["Radicarsi a terra","Camminare scalzi","Respiro profondo","Routine sicure","Corpo e movimento","«Sono al sicuro»"],
   dom=["Mi sento sicuro nella vita?","Ho fiducia nel futuro?"]),

 dict(key="svadhisthana", num=2, sans="SVADHISTHANA", name="SACRALE", Hb=26, Sb=0.85,
   elem="water", elabel="ACQUA", clabel="ARANCIONE", affirm="IO SENTO",
   closing="Mi permetto di sentire, mi permetto di fluire.",
   corr=["Elemento Acqua","Basso ventre","Gonadi","Plesso lombare","Colore arancione","Mantra VAM"],
   temi=["Emozioni","Piacere","Creatività","Relazioni","Sessualità","Movimento"],
   squ=["Senso di colpa","Vergogna del corpo","Colpa nel ricevere","Paura dell'intimità","Dolori pelvici","Creatività bloccata"],
   hamer=["Mesoderma antico","Cervelletto","Protezione","Attacco all'integrità","Derma e sierose","Mammella ghiandolare"],
   rieq=["Sentire le emozioni","Lasciar fluire","Concedersi piacere","Acqua e bagni","Danza del bacino","Creatività libera"],
   dom=["Mi permetto di provare piacere?","Riesco a esprimere le mie emozioni?"]),

 dict(key="manipura", num=3, sans="MANIPURA", name="PLESSO SOLARE", Hb=45, Sb=0.92,
   elem="fire", elabel="FUOCO", clabel="GIALLO", affirm="IO POSSO",
   closing="Io posso. Io scelgo.",
   corr=["Elemento Fuoco","Sopra l'ombelico","Pancreas","Plesso solare","Colore giallo","Mantra RAM"],
   temi=["Volontà","Autostima","Potere personale","Identità","Azione","Scelta"],
   squ=["Autocritica","Perfezionismo","Cerco approvazione","Gastrite, reflusso","Affaticamento","Non chiedo"],
   hamer=["Mesoderma recente","Midollo cerebrale","Svalutazione di sé","Ossa e muscoli","Tessuto connettivo","Autostima ferita"],
   rieq=["Riconoscere il valore","Porre confini","Gentilezza con sé","Sole e calore","Respiro nel ventre","«Io posso»"],
   dom=["Credo nelle mie capacità?","Quanto potere mi concedo?"]),

 dict(key="anahata", num=4, sans="ANAHATA", name="CUORE", Hb=142, Sb=0.50,
   elem="air", elabel="ARIA", clabel="VERDE", affirm="IO AMO",
   closing="Amo. Mi apro. Perdono.",
   corr=["Elemento Aria","Centro del petto","Timo","Plesso cardiaco","Colore verde","Mantra YAM"],
   temi=["Amore","Empatia","Compassione","Perdono","Apertura","Relazione"],
   squ=["Chiusura emotiva","Paura di amare","Gelosia","Paura dell'abbandono","Petto contratto","Dare troppo"],
   hamer=["Ectoderma","Corteccia cerebrale","Relazione","Separazione","Pelle (epidermide)","Conflitti affettivi"],
   rieq=["Aprire il petto","Dare e ricevere","Perdono","Gratitudine","Natura e verde","«Mi apro»"],
   dom=["Riesco a dare e ricevere amore?","Mi permetto di essere vulnerabile?"]),

 dict(key="vishuddha", num=5, sans="VISHUDDHA", name="GOLA", Hb=200, Sb=0.78,
   elem="ether", elabel="ETERE", clabel="AZZURRO", affirm="IO COMUNICO",
   closing="Esprimo la mia verità.",
   corr=["Elemento Etere","Gola","Tiroide","Plesso cervicale","Colore azzurro","Mantra HAM"],
   temi=["Comunicazione","Verità","Espressione","Ascolto","Creatività","Autenticità"],
   squ=["Difficoltà col no","Paura del giudizio","Mi scuso sempre","Nodo alla gola","Bruxismo","Verità taciuta"],
   hamer=["Ectoderma","Corteccia cerebrale","Laringe e tiroide","Conflitto di spavento","Non poter parlare","Sentirsi impotenti"],
   rieq=["Dire la verità","Cantare, vocalizzare","Esprimere il sentire","Scrivere","Silenzio consapevole","«Esprimo me»"],
   dom=["Esprimo la mia verità?","Mi sento ascoltato dagli altri?"]),

 dict(key="ajna", num=6, sans="AJNA", name="TERZO OCCHIO", Hb=235, Sb=0.55,
   elem="light", elabel="LUCE", clabel="INDACO", affirm="IO VEDO",
   closing="Vedo oltre. Comprendo.",
   corr=["Elemento Luce","Tra le sopracciglia","Ipofisi","Plesso carotideo","Colore indaco","Mantra OM"],
   temi=["Intuizione","Visione interiore","Immaginazione","Chiarezza","Saggezza","Percezione"],
   squ=["Confusione mentale","Overthinking","Indecisione","Sfiducia nell'intuito","Emicranie","Insonnia"],
   hamer=["Ectoderma","Corteccia visiva","Retina e vitreo","Pericolo alle spalle","Paura del futuro","Non voler vedere"],
   rieq=["Fidarsi dell'intuito","Meditazione","Visualizzazione","Ridurre il rumore","Sogni e immagini","«Vedo oltre»"],
   dom=["Ascolto la mia intuizione?","Riesco a vedere oltre le apparenze?"]),

 dict(key="sahasrara", num=7, sans="SAHASRARA", name="CORONA", Hb=283, Sb=0.48,
   elem="consciousness", elabel="COSCIENZA", clabel="VIOLA", affirm="IO COMPRENDO",
   closing="Sono parte del tutto.",
   corr=["Coscienza pura","Sommità del capo","Pineale (epifisi)","Cervello","Viola / bianco","Silenzio · OM"],
   temi=["Spiritualità","Coscienza","Connessione","Unità","Presenza","Trascendenza"],
   squ=["Senso di vuoto","Disconnessione","Cinismo","Mancanza di senso","Burnout","Testa pesante"],
   hamer=["Oltre la materia","Sistema nervoso","Corteccia / pineale","Ricerca di senso","Disconnessione","Integrazione"],
   rieq=["Silenzio, quiete","Meditazione","Connettersi al tutto","Lasciar andare","Gratitudine","«Sono parte del tutto»"],
   dom=["Sento connessione con la vita?","Coltivo silenzio e quiete?"]),
]

# --------- ICONE (simboli) ----------
def icon_defs():
    d = []
    # acqua
    d.append('<symbol id="ic-water" viewBox="0 0 100 100"><path d="M50 14 C50 32 76 50 76 66 A26 26 0 0 1 24 66 C24 50 50 32 50 14 Z" fill="currentColor"/><ellipse cx="40" cy="64" rx="6" ry="9" fill="#fff" opacity="0.45"/></symbol>')
    # terra (montagne)
    d.append('<symbol id="ic-earth" viewBox="0 0 100 100"><path d="M10 78 L38 30 L54 54 L64 40 L90 78 Z" fill="currentColor"/><path d="M38 30 L48 46 L33 46 Z" fill="#fff" opacity="0.5"/></symbol>')
    # fuoco (fiamma)
    d.append('<symbol id="ic-fire" viewBox="0 0 100 100"><path d="M52 10 C66 32 80 42 74 64 A24 24 0 0 1 26 62 C25 50 34 46 39 38 C42 50 51 47 49 36 C48 27 49 19 52 10 Z" fill="currentColor"/><path d="M50 50 C58 58 60 64 56 72 A8 8 0 0 1 42 70 C42 62 47 60 50 50 Z" fill="#fff" opacity="0.55"/></symbol>')
    # aria (vento)
    d.append('<symbol id="ic-air" viewBox="0 0 100 100"><g fill="none" stroke="currentColor" stroke-width="6.5" stroke-linecap="round"><path d="M16 36 H56 a11 11 0 1 0 -11 -11"/><path d="M16 54 H70 a10 10 0 1 1 -10 10"/><path d="M16 72 H48 a9 9 0 1 0 -9 9"/></g></symbol>')
    # etere (spazio: anelli + bindu + scintille)
    rays = '<g fill="none" stroke="currentColor" stroke-width="5"><circle cx="50" cy="50" r="30"/><circle cx="50" cy="50" r="17"/></g><circle cx="50" cy="50" r="7" fill="currentColor"/>'
    rays += '<g fill="currentColor"><circle cx="50" cy="12" r="3"/><circle cx="84" cy="64" r="3"/><circle cx="18" cy="66" r="3"/></g>'
    d.append('<symbol id="ic-ether" viewBox="0 0 100 100">'+rays+'</symbol>')
    # luce (sole)
    sun = '<circle cx="50" cy="50" r="17" fill="currentColor"/><g stroke="currentColor" stroke-width="6" stroke-linecap="round">'
    for k in range(8):
        a = math.radians(k*45); x1=50+math.cos(a)*24; y1=50+math.sin(a)*24; x2=50+math.cos(a)*34; y2=50+math.sin(a)*34
        sun += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>'
    sun += '</g>'
    d.append('<symbol id="ic-light" viewBox="0 0 100 100">'+sun+'</symbol>')
    # coscienza (corona radiante / mille petali)
    cons = '<circle cx="50" cy="50" r="8" fill="currentColor"/><circle cx="50" cy="50" r="20" fill="none" stroke="currentColor" stroke-width="3.5" opacity="0.8"/><g stroke="currentColor" stroke-width="3.2" stroke-linecap="round">'
    for k in range(16):
        a = math.radians(k*22.5); x1=50+math.cos(a)*24; y1=50+math.sin(a)*24; x2=50+math.cos(a)*33; y2=50+math.sin(a)*33
        cons += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>'
    cons += '</g>'
    d.append('<symbol id="ic-consciousness" viewBox="0 0 100 100">'+cons+'</symbol>')
    # fiore/loto 6 petali (Temi)
    pet = ''
    for k in range(6):
        th = math.radians(k*60 - 90); cx=50+math.cos(th)*19; cy=50+math.sin(th)*19; rot=math.degrees(th)+90
        pet += f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="9.5" ry="17" transform="rotate({rot:.1f} {cx:.1f} {cy:.1f})" fill="currentColor"/>'
    d.append('<symbol id="ic-flower" viewBox="0 0 100 100">'+pet+'<circle cx="50" cy="50" r="11" fill="#fff"/><circle cx="50" cy="50" r="6" fill="currentColor"/></symbol>')
    # cuore spezzato (Squilibri)
    d.append('<symbol id="ic-broken" viewBox="0 0 100 100"><path d="M50 84 C16 60 7 40 22 26 C34 15 47 19 50 31 C53 19 66 15 78 26 C93 40 84 60 50 84 Z" fill="currentColor"/><path d="M50 24 L43 42 L57 55 L46 70 L51 83" stroke="#fff" stroke-width="5" fill="none" stroke-linejoin="round" stroke-linecap="round"/></symbol>')
    # dna (Hamer)
    d.append('<symbol id="ic-dna" viewBox="0 0 100 100"><g fill="none" stroke="currentColor" stroke-linecap="round"><path d="M34 18 C66 30 66 46 50 50 C34 54 34 70 66 82" stroke-width="5.5"/><path d="M66 18 C34 30 34 46 50 50 C66 54 66 70 34 82" stroke-width="5.5"/><path d="M41 23 L59 23" stroke-width="4"/><path d="M36 33 L64 33" stroke-width="4"/><path d="M36 67 L64 67" stroke-width="4"/><path d="M41 77 L59 77" stroke-width="4"/></g></symbol>')
    # scintilla (Riequilibrio)
    d.append('<symbol id="ic-sparkle" viewBox="0 0 100 100"><path d="M46 18 C49 40 52 45 76 48 C52 51 49 56 46 78 C43 56 40 51 16 48 C40 45 43 40 46 18 Z" fill="currentColor"/><path d="M78 20 C79 28 80 30 88 31 C80 32 79 34 78 42 C77 34 76 32 68 31 C76 30 77 28 78 20 Z" fill="currentColor"/><path d="M26 66 C27 72 28 73 34 74 C28 75 27 76 26 82 C25 76 24 75 18 74 C24 73 25 72 26 66 Z" fill="currentColor"/></symbol>')
    # occhio (domande)
    d.append('<symbol id="ic-eye" viewBox="0 0 100 100"><path d="M12 50 Q50 20 88 50 Q50 80 12 50 Z" fill="none" stroke="currentColor" stroke-width="6" stroke-linejoin="round"/><circle cx="50" cy="50" r="14" fill="currentColor"/><circle cx="45" cy="46" r="4" fill="#fff"/></symbol>')
    return "\n".join(d)

PW, PH = 332, 264
POS = {0:(78,35),1:(1075,35),2:(78,470),3:(576,470),4:(1075,470)}  # corr,temi,squ,hamer,rieq
NODE_CX, NODE_CY, NODE_RX, NODE_RY = 742, 255, 205, 158
BR_META = [("CORRISPONDENZE","__elem__"),("TEMI E FUNZIONI","flower"),
           ("SQUILIBRI","broken"),("DECODIFICA HAMER","dna"),("RIEQUILIBRIO","sparkle")]

def build(c):
    Hb, Sb = c["Hb"], c["Sb"]
    def C(L, dH=0, S=None): return shade(Hb+dH, Sb if S is None else S, L)
    INK = shade(Hb, 0.42, 0.24)
    items_branches = [c["corr"], c["temi"], c["squ"], c["hamer"], c["rieq"]]
    # colori per ramo (leggera variazione di tinta)
    deep=[]; mid=[]; acc=[]
    for i in range(5):
        dH=(i-2)*7
        deep.append(C(0.40,dH)); mid.append(C(0.52,dH)); acc.append(C(0.62,dH))
    S=[]
    S.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="297mm" height="210mm" viewBox="0 0 {W} {H}" font-family="DejaVu Sans, Liberation Sans, sans-serif">')
    S.append('<defs>')
    S.append(f'''<radialGradient id="bg" cx="50%" cy="40%" r="75%">
      <stop offset="0%" stop-color="{shade(Hb,0.30,0.985)}"/><stop offset="60%" stop-color="{shade(Hb,0.45,0.955)}"/><stop offset="100%" stop-color="{shade(Hb,0.50,0.905)}"/></radialGradient>
     <radialGradient id="nodeg" cx="50%" cy="36%" r="72%">
      <stop offset="0%" stop-color="{shade(Hb,Sb*0.92,0.66)}"/><stop offset="55%" stop-color="{shade(Hb,Sb,0.50)}"/><stop offset="100%" stop-color="{shade(Hb,Sb,0.385)}"/></radialGradient>
     <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{shade(Hb,0.6,0.80)}" stop-opacity="0.75"/>
      <stop offset="70%" stop-color="{shade(Hb,0.6,0.80)}" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="{shade(Hb,0.6,0.80)}" stop-opacity="0"/></radialGradient>
     <filter id="soft" x="-25%" y="-25%" width="150%" height="160%"><feDropShadow dx="0" dy="5" stdDeviation="7" flood-color="{shade(Hb,0.6,0.20)}" flood-opacity="0.22"/></filter>
     <filter id="softsm" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="{shade(Hb,0.6,0.20)}" flood-opacity="0.25"/></filter>
     <filter id="tsh" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="1.5" stdDeviation="2" flood-color="#3A1500" flood-opacity="0.45"/></filter>''')
    for i in range(5):
        S.append(f'<linearGradient id="g{i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="{acc[i]}"/><stop offset="100%" stop-color="{deep[i]}"/></linearGradient>')
    S.append(icon_defs())
    S.append('</defs>')
    S.append(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')
    # puntini angoli
    def dots(cx,cy):
        o=[]
        for dx,dy,r,op in [(0,0,7,0.5),(26,10,4,0.4),(14,30,3,0.35),(40,-6,3,0.3),(-4,22,4,0.3)]:
            o.append(f'<circle cx="{cx+dx}" cy="{cy+dy}" r="{r}" fill="{shade(Hb,0.55,0.70)}" opacity="{op}"/>')
        return "".join(o)
    S.append(dots(40,40)+dots(W-70,44)+dots(44,H-70)+dots(W-70,H-72))
    # glow + loto
    S.append(f'<circle cx="{NODE_CX}" cy="{NODE_CY}" r="305" fill="url(#glow)"/>')
    lot=[]
    for k in range(6):
        a=math.radians(30+k*60); px=NODE_CX+math.cos(a)*155; py=NODE_CY+math.sin(a)*155; deg=90+(30+k*60)
        lot.append(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="60" ry="155" transform="rotate({deg:.1f} {px:.1f} {py:.1f})" fill="{shade(Hb,0.5,0.82)}" opacity="0.32"/>')
    S.append('<g>'+"".join(lot)+'</g>')
    # connettori
    HEAD=[(POS[i][0]+PW/2, POS[i][1]+(10 if i==3 else 40)) for i in range(5)]
    for i in range(5):
        hxp,hyp=HEAD[i]; cxm=(NODE_CX+hxp)/2; cym=NODE_CY+(hyp-NODE_CY)*0.15
        S.append(f'<path d="M{NODE_CX} {NODE_CY} Q{cxm:.0f} {cym:.0f} {hxp:.0f} {hyp:.0f}" fill="none" stroke="{mid[i]}" stroke-width="15" stroke-linecap="round" opacity="0.5"/>')
    # pannelli
    for i in range(5):
        px,py=POS[i]; name,icon=BR_META[i]
        if icon=="__elem__": icon=c["elem"]
        S.append(f'<g filter="url(#soft)"><rect x="{px}" y="{py}" width="{PW}" height="{PH}" rx="26" fill="#ffffff" stroke="{acc[i]}" stroke-opacity="0.4" stroke-width="1.5"/></g>')
        hxx,hyy,hw,hh=px+12,py+12,PW-24,60
        S.append(f'<rect x="{hxx}" y="{hyy}" width="{hw}" height="{hh}" rx="20" fill="url(#g{i})"/>')
        bcx,bcy,br=hxx+35,hyy+hh/2,21
        S.append(f'<circle cx="{bcx}" cy="{bcy}" r="{br}" fill="#ffffff"/>')
        S.append(f'<use href="#ic-{icon}" x="{bcx-16}" y="{bcy-16}" width="32" height="32" color="{deep[i]}"/>')
        nfs=20 if len(name)<=15 else 19
        S.append(f'<text x="{bcx+br+11}" y="{hyy+hh/2+7}" font-size="{nfs}" font-weight="bold" fill="#ffffff" letter-spacing="0.3">{esc(name)}</text>')
        y0=py+106
        for j,it in enumerate(items_branches[i]):
            yy=y0+j*27
            S.append(f'<circle cx="{px+34}" cy="{yy-6}" r="5" fill="{mid[i]}"/>')
            S.append(f'<text x="{px+50}" y="{yy}" font-size="22" fill="{INK}" font-weight="500">{esc(it)}</text>')
    # nodo
    S.append(f'<g filter="url(#soft)"><ellipse cx="{NODE_CX}" cy="{NODE_CY}" rx="{NODE_RX}" ry="{NODE_RY}" fill="url(#nodeg)" stroke="#ffffff" stroke-width="6"/></g>')
    S.append(f'<ellipse cx="{NODE_CX}" cy="{NODE_CY}" rx="{NODE_RX-13}" ry="{NODE_RY-13}" fill="none" stroke="#ffffff" stroke-opacity="0.45" stroke-width="2"/>')
    S.append(f'<use href="#ic-{c["elem"]}" x="{NODE_CX-31}" y="{NODE_CY-130}" width="62" height="62" color="#ffffff"/>')
    tfs = 42 if len(c["sans"])<=12 else 38
    S.append(f'<text x="{NODE_CX}" y="{NODE_CY-14}" text-anchor="middle" font-size="{tfs}" font-weight="bold" fill="#ffffff" letter-spacing="1" filter="url(#tsh)">{esc(c["sans"])}</text>')
    S.append(f'<text x="{NODE_CX}" y="{NODE_CY+24}" text-anchor="middle" font-size="23" font-weight="bold" fill="#ffffff" letter-spacing="0.5" filter="url(#tsh)">{c["num"]}&#176; CHAKRA &#183; {esc(c["name"])}</text>')
    S.append(f'<text x="{NODE_CX}" y="{NODE_CY+62}" text-anchor="middle" font-size="17" fill="#FFF1E0" letter-spacing="2" font-weight="500">{esc(c["elabel"])} &#183; {esc(c["clabel"])} &#183; &#171;{esc(c["affirm"])}&#187;</text>')
    # banner domande
    by,bh=772,246; bx,bw=150,W-300
    S.append(f'<g filter="url(#soft)"><rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="30" fill="#FFFFFF" stroke="{acc[2]}" stroke-opacity="0.6" stroke-width="2"/></g>')
    S.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="30" fill="none" stroke="{shade(Hb,0.5,0.86)}" stroke-width="6" opacity="0.55"/>')
    S.append(f'<text x="{W/2}" y="{by+44}" text-anchor="middle" font-size="19" fill="{shade(Hb,0.55,0.38)}" font-weight="bold" letter-spacing="3">DOMANDE DI AUTO-OSSERVAZIONE</text>')
    QS=c["dom"]; fs_q=21; eye_d=50; gap=50
    def cw(t): return wapprox(t,fs_q,0.50)+46
    total=sum(eye_d+10+cw(t) for t in QS)+gap; x=(W-total)/2; cyq=by+138; ch=58
    for t in QS:
        ex=x+eye_d/2
        S.append(f'<g filter="url(#softsm)"><circle cx="{ex:.0f}" cy="{cyq}" r="{eye_d/2}" fill="{deep[2]}"/></g>')
        S.append(f'<use href="#ic-eye" x="{ex-16:.0f}" y="{cyq-16}" width="32" height="32" color="#ffffff"/>')
        x+=eye_d+10; w=cw(t)
        S.append(f'<rect x="{x:.0f}" y="{cyq-ch/2}" width="{w:.0f}" height="{ch}" rx="{ch/2}" fill="{shade(Hb,0.55,0.965)}" stroke="{acc[2]}" stroke-opacity="0.7" stroke-width="2"/>')
        S.append(f'<text x="{x+w/2:.0f}" y="{cyq+8}" text-anchor="middle" font-size="{fs_q}" fill="{INK}" font-family="DejaVu Serif, serif" font-style="italic">{esc(t)}</text>')
        x+=w+gap
    S.append(f'<text x="{W/2}" y="{by+212}" text-anchor="middle" font-size="23" fill="{shade(Hb,0.7,0.34)}" font-family="DejaVu Serif, serif" font-style="italic">&#171;&#160;{esc(c["closing"])}&#160;&#187;</text>')
    S.append('</svg>')
    return "\n".join(S)

for c in CHAKRAS:
    fn = f'chakra-{c["num"]}-{c["key"]}.svg'
    open(fn,"w",encoding="utf-8").write(build(c))
    print("scritto", fn)
print("FATTO: 7 mappe")
