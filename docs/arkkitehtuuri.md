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

View <|-- UI
View <|-- SearchCiteView
View <|-- AddCiteView
View --> Logic

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

class View {
    +description: str
    #help_message: str
    #logic: Logic
    +start()
    #show_help()
    #show_cites(cites: list[Cite])
}

class UI {
    -views: ordered_dict[str, View]
}

class Logic{
    +create_cite(id: str, type: str, authors: list[str], fields: dict)
    +filter_cites(filters: set[str])
    +get_all_cites()
    +export(path: str, format: str, cites: list[Cite])
    +remove_cite(id: str)
}

class Cite {
    +id: str
    +type: str
    +authors: list[str]
    +fields: dict
    +__str__()
}

class CiteRepository {
    +add_cite(cite: Cite)
    +get_all_cites()
    +remove_cite(id: str)
}

class Database {
    +connection: sqlite3.Connection
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

### Käyttöliittymä

- Yhteiden yliluokka: käyttöliittymillä on paljon yhteistä
- Viitteiden listaus: tätä tarvitaan ainakin viitteiden poistossa, haussa, listauksessa.
  Näin ollen se on hyvä toteuttaa vain kerran.

## SQL-skeema

```SQL
CREATE TABLE Cites (
    id TEXT PRIMARY KEY,
    type TEXT
)

CREATE TABLE Fields (
    cite_id TEXT REFERENCES Cites,
    name TEXT,
    content TEXT
)

CREATE TABLE Authors (
    cite_id TEXT REFERENCES Cites,
    name TEXT
)
```
