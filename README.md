# **Sprint Predictor AI**

Systém pre komplexnú analýzu atletickej pripravenosti a predikciu športového výkonu na základe biometrických dát.  
**Autor:** Tomáš Žigo

## **Motivácia**

Beh je fyziologicky jedna z najextrémnejších atletických disciplín. Motiváciou tohto projektu je vytvoriť analytický nástroj šitý na mieru pre šprintérov, ktorý eliminuje dohady v tréningovom procese tým, že prepojí dáta o regenerácii s konkrétnymi výkonmi na dráhe.

## **Cieľ projektu**

Cieľom je vytvoriť softvérový analytický nástroj vo forme webovej aplikácie, ktorý dokáže automatizovane spracovať dáta z fitness trackerov (napr. WHOOP) a spojiť ich s manuálne zadaným tréningovým denníkom. Výsledkom je predikčný model založený na strojovom učení (Machine Learning) integrovaný v databázovom systéme.

## **Hlavné funkcionality (Jadro projektu)**

* **Track & Field databáza:** Štruktúrovaný zber špecifických tréningových parametrov, ako sú kategórie tréningov, presné časy jednotlivých úsekov a dĺžka oddychu v minútach.  
* **AI predikčný model:** Využitie algoritmov strojového učenia, ktoré na základe historických dát a aktuálnej úrovne regenerácie dokážu predpovedať očakávaný pretekový čas.  
* **Webová aplikácia:** Rozhranie pre zápis tréningov, analýzu pomocou AI a možnosť prihlásenia používateľov pre porovnávanie aktuálnych výkonov s minulosťou.

## **Doplňujúce funkcionality**

| Funkcia | Popis   |
| :---- | :---- |
| **Analýza konzistencie (Drop-off)** | Automatické vyhodnotenie spomalenia medzi prvým a posledným úsekom (napr. 3x300m) a hľadanie korelácie s ranným HRV. |
| **Vizualizácia trendov** | Generovanie grafov pre dlhodobé sledovanie progresu a únavy. |
| **Systém odporúčaní** | Upozornenia na zvýšené riziko pretrénovania na základe biometrických odchýlok. |

## **Technologický stack**

* **Programovací jazyk:** Python  
* **Webový framework:** Flask + Flask-SQLAlchemy  
* **Databáza:** SQLite  
* **Strava integrácia:** stravalib  
* **AI chat:** Groq API (DeepSeek R1 / LLaMA 3.3)  
* **Mapy:** Leaflet.js (heatmapa behov)  
* **Frontend:** HTML, CSS, JavaScript

## **Prínos projektu**

Projekt umožňuje autorovi zlepšiť sa v programovaní a zároveň priamo aplikovať technologické poznatky na zvýšenie vlastnej športovej výkonnosti.

## **Inštalácia a spustenie**

1. Klonovanie repozitára z GitHubu.  
2. Inštalácia závislostí cez pip install \-r requirements.txt.  
3. Skopíruj `.env.example` ako `.env` a doplň svoje API kľúče.  
4. Spustenie aplikácie pomocou python app.py.

*Tento dokument slúži ako oficiálne README pre projekt Sprint Predictor AI.*