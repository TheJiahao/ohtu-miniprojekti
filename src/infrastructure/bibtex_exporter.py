from entities.cite import Cite


class BibtexExporter:
    @classmethod
    def dump_list(cls, data: list[str]) -> str:
        """Palauttaa listan BibTeX-kentän arvona ja järjestettynä.

        Args:
            data (list[str]): Arvoksi muutettava lista.

        Returns:
            str: Lista BibTeX-kentän arvona.
        """

        return f"{{{' and '.join(data)}}}"

