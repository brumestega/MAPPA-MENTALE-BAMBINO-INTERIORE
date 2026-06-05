# 🧡 Mappe Mentali — Bambino Interiore & Secondo Chakra (Svadhisthana)

Due mappe mentali visive professionali, **formato A4 orizzontale**, pensate come
supporto per un laboratorio di gruppo. Stile coordinato: palette arancione calda,
sfondo chiaro, icone vettoriali disegnate a mano (niente emoji), testo leggibile
anche a distanza. Pronte per la **stampa ad alta risoluzione**.

## Le due mappe

### 1. Bambino Interiore e Secondo Chakra — *il percorso emotivo*
`mappa-mentale-bambino-interiore.pdf` · `.png` · `.svg`

Nodo centrale + 5 rami radiali:
- 👶 **Bambino Interiore** — Gioia, Gioco, Curiosità, Innocenza, Bisogni, Vulnerabilità
- 🌊 **Secondo Chakra** — Acqua, Emozioni, Piacere, Creatività, Relazioni, Movimento
- 💔 **Ferite** — Rifiuto, Abbandono, Vergogna, Critica, Paura, Controllo
- 🔄 **Nell'adulto** — Chiusura, Dipendenza, Giudizio, Blocchi, Senso di colpa, Difficoltà a ricevere
- ✨ **Guarigione** — Accoglienza, Ascolto, Fiducia, Espressione, Creatività, Gioia

Più le due catene "dal dolore alla gioia" e la frase finale:
*Bambino → Ferita → Emozione → Accoglienza → Gioia*.

### 2. Svadhisthana — *le corrispondenze*
`svadhisthana-corrispondenze.pdf` · `.png` · `.svg`

Companion di approfondimento sul 2° chakra. Nodo centrale + 5 rami:
- 💧 **Corrispondenze** — Elemento Acqua, Basso ventre, Ghiandola gonadi, Plesso lombare, Colore arancione, Mantra VAM
- 🌸 **Temi e Funzioni** — Emozioni, Piacere, Creatività, Relazioni, Sessualità, Movimento
- 💔 **Squilibri** — Senso di colpa, Vergogna del corpo, Colpa nel ricevere, Paura dell'intimità, Dolori pelvici, Creatività bloccata
- 🧬 **Decodifica Hamer** — Mesoderma antico, Cervelletto, Protezione, Attacco all'integrità, Derma e sierose, Mammella ghiandolare
- ✨ **Riequilibrio** — Sentire le emozioni, Lasciar fluire, Concedersi piacere, Acqua e bagni, Danza del bacino, Creatività libera

Con le **domande di auto-osservazione**: *Mi permetto di provare piacere?* ·
*Riesco a esprimere le mie emozioni?*

## Stampa

I file `.pdf` sono **vettoriali in formato A4 (297 × 210 mm)**: si stampano nitidi a
qualsiasi dimensione. I file `.png` sono a **300 DPI (3508 × 2481 px)** per anteprima
o stampa raster. In stampa scegliere "adatta alla pagina / orizzontale".

## Rigenerare i file

Servono Python 3 e `rsvg-convert` (pacchetto `librsvg2-bin`):

```bash
# Mappa 1
python3 genera_mappa.py
rsvg-convert -f pdf mappa-mentale-bambino-interiore.svg -o mappa-mentale-bambino-interiore.pdf
rsvg-convert -f png -d 300 -p 300 mappa-mentale-bambino-interiore.svg -o mappa-mentale-bambino-interiore.png

# Mappa 2
python3 genera_mappa2.py
rsvg-convert -f pdf svadhisthana-corrispondenze.svg -o svadhisthana-corrispondenze.pdf
rsvg-convert -f png -d 300 -p 300 svadhisthana-corrispondenze.svg -o svadhisthana-corrispondenze.png
```

Per modificare contenuti o colori basta editare le liste `BRANCHES` negli script
`genera_mappa.py` / `genera_mappa2.py` e rigenerare.

---
*Nota: la mappa "Decodifica Hamer" riporta corrispondenze simboliche della Nuova
Medicina Germanica a fini di lavoro interiore in un contesto formativo; non
costituisce indicazione medica.*
