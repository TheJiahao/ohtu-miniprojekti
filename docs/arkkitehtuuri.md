# Arkkitehtuuri

Sovellus noudattaa [Repository](https://ohjelmistotekniikka-hy.github.io/python/toteutus#repository-suunnittelumalli) mallia.
Sovelluksen koodit on jaettu/luokitettu neljään kerrokseen:

- Käyttöliittymä
- Logiikka
- Repository: Vastaa tietyn luokan olioiden tietojen lisäämisestä/muokkauksesta.
  Esim. `Viite`-luokalle `ViiteRepository`.
- Infrastruktuuri: Abstrahoi alimman tason operaatiot, esim. tietokantaoperaatiot tai tiedoston luku.

Hahmotelma mallista

```mermaid
classDiagram
UI --> Logiikka
Logiikka --> Repository
Repository --> Tietokanta
```

## Luokkakaavio

```mermaid
classDiagram
Ui --> Logic
Logic --> Cite
Logic --> CiteRepository
CiteRepository --> Database

class Logic{
    +create_cite(type: str, name: str, fields: dict)
    +get_all_cites()
}

class Cite {
    +name: str
    +entry_type: str
    +fields: dict
    +__str__()
}

class CiteRepository {
    +add_cite(cite: Cite)
    +get_all_cites()
}

class Database {
    +add_cite(cite: Cite)
    +get_all_cites()
}
```
