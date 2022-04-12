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
