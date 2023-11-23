# Arkkitehtuuri

Sovellus noudattaa [Repository](https://ohjelmistotekniikka-hy.github.io/python/toteutus#repository-suunnittelumalli) mallia.
Sovelluksen koodit on jaettu/luokitettu neljään kerrokseen:

- Käyttöliittymä
- Logiikka
- Repository: Vastaa tietyn luokan olioiden tietojen lisäämisestä/muokkauksesta.
  Esim. `Viite`-luokalle `ViiteRepository`.
- Infrastruktuuri: Abstrahoi alimman tason operaatiot, esim. tietokantaoperaatiot tai tiedoston luku.

## Hahmotelma mallista

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
Logic --> ExportService
Logic --> CiteValidator
Logic --> FilterService

ExportService --> BibtexExporter
ExportService ..> Cite

FilterService --> CiteRepository
FilterService ..> Cite

CiteRepository --> Database

class Logic{
    +create_cite(type: str, name: str, fields: dict)
    +get_all_cites()
    +export(path: str, format: str, cites: list[Cite])
    +remove_cite(id: str)
}

class Cite {
    +id: str
    +type: str
    +fields: dict
    +__str__()
}

class CiteRepository {
    +add_cite(cite: Cite)
    +get_all_cites()
    +remove_cite(id: str)
}

class Database {
    +add_cite(cite: Cite)
    +get_all_cites()
}

class BibtexExporter {
    +export(path: str, cites: list[Cite])
}

class ExportService {
    +export(path: str, format: str, cites: list[Cite])
}

class CiteValidator {
    +get_fields(type: str)
}

class FilterService {
    +filter_by_name(name: str, )
    +filter_by_author(author: str)
    +filter_by_tag(tag: str)
}
```

## SQL-skeema

```SQL
CREATE TABLE IF NOT EXISTS cites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    entry_type TEXT,
    fields TEXT
);
```
