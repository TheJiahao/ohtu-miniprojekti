from entities.cite import Cite
from infrastructure.bibtex_exporter import BibtexExporter


class ExportService:
    """
    Luokka, joka vastaa viitteiden tiedostoon viemisestä.
    """

    def __init__(self, exporters: dict | None = None) -> None:
        """
        Luokan konstruktori.

        Args:
            exporters (dict | None, optional): Viitteiden viemisestä vastaavat oliot.
            Oletukseltaan None.
        """

        self.__exporters: dict = exporters or {"bibtex": BibtexExporter()}

    def export(self, path: str, format: str, cites: list[Cite]) -> str:
        """
        Kirjoittaa viitteet annettuun tiedostoon.

        Args:
            path (str): Polku kirjoitettavaan tiedostoon.
            format (str): Tiedostomuoto. Tuetut muodot: bibtex
            cites (list[Cite]): Kirjoitettavat viitteet.

        Returns:
            str: Polku, johon viitteet tallennettiin.

        Raises:
            ValueError: Tiedostomuoto ei ole tuettu.
        """

        try:
            path = self.__exporters[format].export(path, cites)

            return path

        except KeyError as exception:
            raise ValueError(
                f"{format}-tiedostoon vieminen ei ole tuettu."
            ) from exception
