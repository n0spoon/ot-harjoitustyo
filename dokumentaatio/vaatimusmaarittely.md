# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on tekstipohjaista käyttöliittymää (TUI) käyttävä laskin, jolla on mahdollista suorittaa laskutoimenpiteitä reaaliluvuilla, tallentaa, hakea ja poistaa tuloksia muistista.

## Perusversion toiminnallisuus
- Tekstikäyttöliittymällä toimiva laskin kokonais- ja liukuluvuille
- Positiivisten ja negatiivisten reaalilukujen käsittelyyn
- Laskutoiminnot
  - Summa
  - Erotus
  - Jako
  - Kerto
  - Neliöjuuri
  - Potenssilasku
  - Käänteisluku
  - Lattia- ja kattofunktiot
    - Funktiot osaavat käsitellä 'inf' syötteen
  - Sovellus tunnistaa NaN (Not-a-Number) syötteen ja sivuuttaa sen
  - Pii ja Neperin luvun likiarvot

- Muistitoiminnot
  - Tuloksen voi lisätä muistiin
  - Tuloksen voi hakea muistista
  - Tuloksen voi poistaa muistista
  - Viimeisintä tulosta voi käyttää laskutoimituksissa
  - Viimeisimmän tuloksen voi poistaa muistista
  - Kaikki muistissa olevat tulokset voidaan tulostaa
  - sqlite3 integraatio
  - Sovellus tunnistaa NaN tuloksen ja sivuuttaa sen tallennuksen muistiin

## Jatkokehitykseen
Sovelluksen perusmallia voi jatkokehittää ainakin seuraavasti:
- Graafinen laskin
- Lisää laskutoimintoja
  - Kaksikantaiset logaritmit
  - Kuutiojuuret
  - Kertoma
  - Itseisarvo
- TUI sijaan GUI
- Profiilit
  - Useampi kuin yksi profiili muistitoimintoja varten
    - Profiilit useammalle käyttäjälle
    - Mahdollisuus luoda/poistaa profiili

