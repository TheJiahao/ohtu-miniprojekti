from entities.cite import Cite


class BibtexExporter:
    """Luokka, joka vastaa viitteiden muuntamisesta BibTeX-muotoon."""

    @classmethod
    def dump_cite(cls, cite: Cite) -> str:
        """Palauttaa viitteen BibTeX-muodossa kentät järjestettynä.

        Args:
            cite (Cite): Muunnettava viite.

        Returns:
            str: Viite BibTeX-muodossa.
        """

        lines = [f"@{cite.type}{{{cite.id}"]

        fields = [f"author = {cls.dump_list(cite.authors)}"]
        fields.extend(
            [
                f"{name} = {cls.dump_string(content)}"
                for name, content in cite.fields.items()
            ]
        )

        lines.extend(sorted(fields))
        lines.append("}")

        return ",\n".join(lines)

    @classmethod
    def dump_list(cls, data: list[str]) -> str:
        """Palauttaa listan BibTeX-kentän arvona ja järjestettynä.

        Args:
            data (list[str]): Arvoksi muutettava lista.

        Returns:
            str: Lista BibTeX-kentän arvona.
        """

        return f"{{{' and '.join(data)}}}"

    @classmethod
    def dump_string(cls, data: str) -> str:
        """Palauttaa merkkijonon BibTeX-kentän arvona.

        Args:
            data (list[str]): Arvoksi muutettava merkkijono.

        Returns:
            str: Merkkijono BibTeX-kentän arvona.
        """

        return f"{{{data}}}"
