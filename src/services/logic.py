from cite import Cite
from citerepository import CiteRepository

class Logic:
    """Sovelluslogiikasta vastaava luokka.
    """
    def __init__(self):
        self.repository = CiteRepository()

    def create_cite(self, type: str, name: str, fields: dict):
        """Lisää uuden viitteen.

        Args:
            type (str): Viitteen tyyppi
            name (str): Viitteen nimi
            fields (dict): Vitteen kentät

        Returns:
            str: "Cite added" tai "Error"
        """
        cite = Cite(name, type, fields)
        try:
            self.repository.add_cite(cite)
            return "Cite added"
        except Exception:
            return "Error"
            