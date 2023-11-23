# Käytänteet

## Työskentelytavat

- **Daily scrum**: Discord-kanavalle "Daily scrum". Lyhyesti oman työskentelypäivän jälkeen vastaukset seuraaviin kysymyksiin:
  - Mitä sain aikaan päivän aikana?
  - Mitä aion saada aikaan seuraavaan daily scrumiin mennessä?
  - Mitä esteitä etenemiselläni on?

## Ohjelmointi

### Yleistä

- Käytä tyyppivihjeitä
- Laita docstring-kommentit julkisille metodeille, käytä esim. [autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
- Jos toteutat jotain, niin toteuta myös testit


### Git

- Commit message: Käskymuodossa, kuten "Add jotain", "Fix jotain", "Implement jotain"
- Tee user storyyn liittyvät muutokset omaan user story-haaraan, esim. `us1`, `us2`, jne.
  - Kun user story on valmis definition of donen tasolla, niin merkkaa valmiiksi
  - Pushaa vain testit läpäisevää koodia
