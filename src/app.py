class App:
    def __init__(self, logic):
        self.logic = logic

    def run(self):
        while True:
            choice = self.choose_action()
            if choice == 2:
                added_cite = self.add_cite()
                print(f"\n{added_cite}")
            else:
                print("Toimintoa ei olemassa tai ei toteutettu vielä.")
                break

    def choose_action(self):
        print("\nValitse toiminto:\n")
        print("0: lopeta")
        print("1: näytä viitteet")
        print("2: lisää uusi viite\n")

        return int(input())

    def add_cite(self):
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
