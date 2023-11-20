class App:
        """Alustaa olion

        Args:
            io (object): konsoli io
            logic (object): sovelluslogiikka
        """

        self.logic = logic

    def run(self):
        """Käynnistää sovelluksen
        """

        while True:
            choice = self.choose_action()
            if choice == 2:
                added_cite = self.add_cite()
                print(f"\n{added_cite}")
            else:
                print("Toimintoa ei olemassa tai ei toteutettu vielä.")
                break

    def choose_action(self):
        """Käyttäjä voi valita toiminnon

        Returns:
            int: Valittua toimintoa vastaava numero
        """
        print("\nValitse toiminto:\n")
        print("0: lopeta")
        print("1: näytä viitteet")
        print("2: lisää uusi viite\n")

        return int(input())

    def add_cite(self):
        """Lisää viite

        Returns:
            str: Kertoo käyttäjälle onnistuiko lisäys
        """
        fields = {}

        print("\nValitse viitetyyppi:\n")
        print("1: kirja (book)")
        print("2: artikkeli (article)\n")
        cite_type = int(input())

        print("\nSyötä viitteen nimi: \n")
        cite_name = str(input())

        # Seuraavaksi tulisi tyypistä riippuen eri kenttien kyselyitä

        print("\nSyötä kirjailijat (authors), erota pilkulla: \n")
        fields["author"] = (input()).split(", ")

        print("\nSyötä otsikko (title): \n")
        fields["title"] = str(input())

        print("\nSyötä vuosi (year): \n")
        fields["year"] = int(input())

        return self.logic.create_cite(cite_type, cite_name, fields)
