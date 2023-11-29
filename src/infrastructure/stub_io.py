class StubIO:
    """Testauksessa käytettävä luokka, joka vastaa syötteistä ja tulostuksista."""

    def __init__(self, inputs):
        """Luokan konstruktori, joka alustaa syöte ja tulostus listat.

        Args:
            inputs (list): Syötteet
        """
        self.inputs = inputs
        self.outputs = ["poistuu"]

    def read(self):
        """Palauttaa ja poistaa syötelistasta ensimmäisen syötteen.

        Returns:
            str: Sovellukselle annettava syöte
        """
        if len(self.inputs) == 0:
            return ""
        return self.inputs.pop(0)

    def write(self, text):
        """Lisää tulostuslistaan merkkijonon.

        Args:
            text (str): Tulostukseen lisättävä merkkijono
        """
        self.outputs.append(str(text))

    def add_input(self, text):
        """Lisää syötelistan loppuun uuden syötten.

        Args:
            text (str): Lisättävä merkkijono
        """
        self.inputs.append(text)
