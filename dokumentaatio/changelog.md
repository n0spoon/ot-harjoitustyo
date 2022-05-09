# Changelog

## Viikko 3
- Alustava sovellusmalli luotu, src/index.py src/services/calcservice.py src/ui/iface.py
- Testaaminen aloitettu.  Kaksi testiä luotu tiedostoon calcservice_test.py jotka varmistavat, ettei alussa laskutoimituksia ole tapahtunut ja pluslaskun toimivan oikein

## Viikko 4
- Pylint otettu käyttöön projektille ja lähdekoodi siistitty(formatoitu)
- Lisätty toiminnallisuus jako- ja kertolaskuille, ja testit näille toiminnallisuuksille
- Luotu poetry run invoke format ja poetry run invoke lint -poetrytehtävät
- Lisätty toiminnallisuus, jolla voi tarkastaa suoritettujen laskutoimitusten määrän
- Siirretty laskutoimitusten tallennus luokkaan calculation_repository.py kansiossa repositories
- Parannettu ja selkeytetty käyttöliittymän io.py ja palvelun calculation_service.py toimintaa

## Viikko 5
- Ensimmäinen release
- Lisätty toiminnallisuus positiivisten lukujen neliöjuurien laskemiseen
- Lisätty toiminnallisuus CalculationService luokkaan, joka estää ohjelman kaatumisen virhetilanteessa esim. laskutoimitukseen syötettäessä jokin ei-numero, kuten "abc.123", ja käsittelee tilanteen
- Vähennetty koodin toistoa luomalla metodi clean_result(result), joka tarkistaa onko luku desimaaliluku jonka desimaaliosan pituus on 1 ja arvo 0 esim 1.0, 2.0 ja muokkaa luvut muotoon 1, 2 ilman desimaaliosaa
- Lisätty toiminnallisuus potenssilaskuihin ja testit toiminnallisuudelle

## Viikko 6
- Toinen release
- Lisätty docstring dokumentaatio luokille calculation_service.py, calculation_repository.py ja io.py
- Lisätty toiminnallisuus käänteislukujen laskemiseen, viimeisen tuloksen käyttämiseen laskuissa, viimeisimmän tuloksen poistamiseen muistista, kaikkien tuloksien poistamiseen muistista ja testit uusille toiminnallisuuksille

## Viikko 7
- Lisätty sqlite3 tietojen pysyväistallennukseen ja toiminnallisuus sekä tiedon lisäämiseen että poistamiseen tietokannasta
- Paranneltu docstring dokumentaatiota
- Eriytetty laskimen tietokanta ja testitietokanta, jotta testien suorittaminen sovelluksen käynnissä ollessa ei pyyhi muistia
