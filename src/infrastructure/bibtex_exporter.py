from pathlib import PosixPath

from entities.cite import Cite


class BibtexExporter:
    """Luokka, joka vastaa viitteiden muuntamisesta BibTeX-muotoon."""

    def export(self, path: PosixPath, cites: list[Cite]) -> str:
        """
        Kirjoittaa viitteet BiBTeX-muodossa tiedostoon.

        Args:
            path (str): Polku kirjoitettavaan tiedostoon.
            cites (list[Cite]): Kirjoitettavat viitteet.

        Returns:
            str: Polku, johon viitteet tallennettiin.
        """

        data = self.__dump(cites)

        with open(path.with_suffix(".bib"), mode="w", encoding="utf-8") as file:
            file.write(data)

        return path

    def __dump(self, cites: list[Cite]) -> str:
        """Palauttaa viitteet BibTeX-muodossa, aakkosjärjestyksessä id:n perusteella.

        Args:
            cites (list[Cite]): Muunnettavat viitteet.

        Returns:
            str: Viitteet BibTeX-muodossa.
        """

        cites = sorted(cites)

        return ",\n".join([self.__dump_cite(cite) for cite in cites])

    def __dump_cite(self, cite: Cite) -> str:
        """Palauttaa viitteen BibTeX-muodossa kentät järjestettynä.

        Args:
            cite (Cite): Muunnettava viite.

        Returns:
            str: Viite BibTeX-muodossa.
        """

        lines = [f"@{cite.type}{{{cite.id}"]

        fields = [f"author = { self.__dump_list(cite.authors)}"]
        fields.extend(
            [
                f"{name} = { self.__dump_string(content)}"
                for name, content in cite.fields.items()
            ]
        )

        lines.extend(sorted(fields))
        lines.append("}")

        return ",\n".join(lines)

    def __dump_list(self, data: list[str]) -> str:
        """Palauttaa listan BibTeX-kentän arvona ja järjestettynä.

        Args:
            data (list[str]): Arvoksi muutettava lista.

        Returns:
            str: Lista BibTeX-kentän arvona.
        """

        return f"{{{' and '.join(data)}}}"

    def __dump_string(self, data: str) -> str:
        """Palauttaa merkkijonon BibTeX-kentän arvona.

        Args:
            data (list[str]): Arvoksi muutettava merkkijono.

        Returns:
            str: Merkkijono BibTeX-kentän arvona.
        """

        return f"{{{data}}}"
