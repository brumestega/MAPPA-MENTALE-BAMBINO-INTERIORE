# 🌈 Mappe Mentali — Chakra & Bambino Interiore

Raccolta di mappe mentali visive professionali, **formato A4 orizzontale**, pensate
come supporto per laboratori di gruppo. Stile coordinato: sfondo chiaro, loto
sfumato dietro al nodo centrale, **icone vettoriali disegnate a mano** (niente
emoji), testo leggibile a distanza. Pronte per la **stampa ad alta risoluzione**.

## A. Mappa del Bambino Interiore
`mappa-mentale-bambino-interiore.pdf` · `.png` · `.svg`

Il percorso emotivo: nodo centrale *Bambino Interiore e Secondo Chakra* + 5 rami
(Bambino Interiore · Secondo Chakra · Ferite · Nell'adulto · Guarigione), le catene
"dal dolore alla gioia" e la frase *Bambino → Ferita → Emozione → Accoglienza → Gioia*.

## B. I 7 Chakra — Le Corrispondenze
`i-7-chakra-corrispondenze.pdf` (**un unico file, 7 pagine**) + i singoli file
`chakra-1-muladhara` … `chakra-7-sahasrara` (`.pdf` / `.png` / `.svg`).

Una mappa per ciascun chakra, **color-codata sul colore del chakra** (rosso → viola)
e con la **icona-elemento** dedicata (terra, acqua, fuoco, aria, etere, luce,
coscienza). Ogni mappa ha la stessa struttura a 5 rami:

| Ramo | Contenuto |
|------|-----------|
| **Corrispondenze** | Elemento · Posizione · Ghiandola · Plesso · Colore · Mantra |
| **Temi e Funzioni** | i temi positivi del chakra |
| **Squilibri** | sintomi emotivi e fisici dello squilibrio |
| **Decodifica Hamer** | foglietto embrionale · area cerebrale · conflitto · organi |
| **Riequilibrio** | pratiche per riarmonizzare |

più il banner con le **domande di auto-osservazione** e l'**affermazione** del chakra.

I 7 chakra: 1 Muladhara (Radice/rosso) · 2 Svadhisthana (Sacrale/arancione) ·
3 Manipura (Plesso solare/giallo) · 4 Anahata (Cuore/verde) · 5 Vishuddha (Gola/azzurro) ·
6 Ajna (Terzo occhio/indaco) · 7 Sahasrara (Corona/viola).

## C. Meditazione guidata del Bambino Interiore
`meditazione-bambino-interiore.pdf` (copione impaginato, A4 verticale) · `.md` (testo)

Un copione pronto da **leggere ad alta voce** in un laboratorio di gruppo: 9 fasi
(preparazione · respiro dell'acqua · luogo sicuro · incontro · ascolto · accoglienza ·
gioco e gioia · integrazione · ritorno), con le **pause** indicate, le **affermazioni**
finali e le **note per il facilitatore** (durata ~20–25 min). Collegata al 2° chakra
(acqua, emozioni, luce arancione).

## D. 7 Meditazioni dei Chakra
`7-meditazioni-dei-chakra.pdf` (**un unico file, 14 pagine**) + i singoli
`meditazione-1-muladhara` … `meditazione-7-sahasrara` (`.pdf`) e
`meditazioni-dei-chakra.md` (testo).

Una meditazione guidata **per ogni chakra**, coordinata nel colore e nell'elemento
con la rispettiva mappa. Ognuna è centrata sui temi del chakra e conduce
all'**elevazione della vibrazione** (luce + mantra *bija*: LAM · VAM · RAM · YAM ·
HAM · OM). Struttura in 6 fasi: Radicamento · Accendere il centro · Riconoscere e
lasciar andare · Il suono che eleva · Espansione · Integrazione e ritorno.

## E. Chakra & Numerologia
`chakra-numerologia.pdf` · `.png` · `.svg`

Pagina A4 di sintesi (coordinata col kit): tabella arcobaleno dei 7 chakra con
**numero · petali · mantra bija · significato numerologico · affermazione**, più tre
riquadri — *I numeri come suono* (i 50 petali = le 50 lettere sanscrite), *Il tuo
Numero del Percorso di Vita* (calcolo + esempio) e una *Nota onesta* sulle fonti
(cosa è tradizione e cosa è sintesi moderna). Vedi `genera_numerologia.py`.

## F. Chakra · Albero della Vita · Tarocchi
`chakra-albero-tarocchi.pdf` · `.png` · `.svg`

Pagina A4 sul "ponte" ermetico tra chakra e tradizione occidentale: l'**Albero della
Vita "arcobaleno"** (i 7 chakra mappati sulle 10 Sephirot) e i **22 sentieri = i 22
Arcani Maggiori**, color-codati secondo la struttura del *Sefer Yetzirah* (3 lettere
madri/elementi · 7 doppie/pianeti · 12 semplici/zodiaco). Include la tabella
chakra↔Sephirot, l'elenco completo dei 22 Arcani (lettera ebraica · carta ·
pianeta/segno) e una nota sull'origine moderna del sincretismo. Vedi `genera_albero.py`.

## G. Scheda del Consultante — *da consegnare*
`scheda-consultante.pdf` · `.png` · `.svg` (A4 **verticale**)

Il foglio da **regalare alla persona a fine sessione**: un promemoria da compilare
a mano davanti al consultante, così diventa un piccolo dono personalizzato da portare
a casa. Coordinato col kit (crema, banner arcobaleno, icone-elemento). Contiene:
*Nome · Data*; **Il mio chakra guida** (i 7 chakra da cerchiare, con bija e affermazione);
**Il filo del Bambino Interiore** (Bambino → Ferita → Emozione → Accoglienza → Gioia);
**La mia frase** (affermazione); **La mia pratica della settimana** (respiro dell'acqua ·
mantra · gesto gentile + una riga libera, una casella per ogni giorno);
**Note e intenzione**; e la firma *«Con cura»* dell'operatore. Vedi `genera_scheda_consultante.py`.

## Stampa
I `.pdf` (mappe) sono **vettoriali in A4 (297 × 210 mm)**: nitidi a qualsiasi dimensione.
I `.png` sono a **300 DPI (3508 × 2481 px)**. In stampa: "Adatta alla pagina",
orientamento **orizzontale**. La *Scheda del Consultante* e le meditazioni sono invece
in A4 **verticale** (210 × 297 mm).

## Rigenerare i file
Serve Python 3 e, per l'export PDF/PNG, `rsvg-convert` (pacchetto `librsvg2-bin`)
**oppure** `cairosvg` (`pip install cairosvg`); per il PDF unico `pdfunite`
(pacchetto `poppler-utils`); per le meditazioni `reportlab` (`pip install reportlab`).

```bash
python3 genera_mappa.py        # Mappa del Bambino Interiore
python3 genera_chakra.py       # le 7 mappe dei chakra (chakra-1..7-*.svg)
python3 genera_meditazione.py  # meditazione del Bambino Interiore (PDF + Markdown)  [serve reportlab]
python3 genera_meditazioni_chakra.py  # le 7 meditazioni dei chakra (PDF + PDF unico + Markdown)
python3 genera_scheda_consultante.py  # Scheda del Consultante (esporta da sé PDF+PNG)

# esempio export di una mappa
rsvg-convert -f pdf chakra-4-anahata.svg -o chakra-4-anahata.pdf
rsvg-convert -f png -d 300 -p 300 chakra-4-anahata.svg -o chakra-4-anahata.png

# PDF unico dei 7 chakra
pdfunite chakra-1-*.pdf chakra-2-*.pdf chakra-3-*.pdf chakra-4-*.pdf \
         chakra-5-*.pdf chakra-6-*.pdf chakra-7-*.pdf i-7-chakra-corrispondenze.pdf
```

Per modificare testi/colori basta editare la lista `CHAKRAS` in `genera_chakra.py`
(o `BRANCHES` in `genera_mappa.py`) e rigenerare.

---
*Nota: i contenuti (corrispondenze energetiche e "Decodifica Hamer" della Nuova
Medicina Germanica) sono proposti come strumenti simbolici di lavoro interiore in
un contesto formativo e non costituiscono indicazione medica o diagnosi.*
