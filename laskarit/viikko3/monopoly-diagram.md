## Sovelluslogiikka

```mermaid
 classDiagram
     Monopoli "1" -- "2" Noppa
     Monopoli "1" -- "2..8" Pelaaja
     Monopoli "1" -- "1" Pelilauta
     Pelilauta "1" -- "40" Ruutu
     Ruutu "1" -- "1" Ruutu
     Pelaaja "1" -- "1" Pelinappula
     Pelinappula "1" -- "2..8" Ruutu
```
