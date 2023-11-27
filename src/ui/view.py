from abc import ABC, abstractmethod

from services.logic import Logic
from infrastructure.console_io import ConsoleIO
from entities.cite import Cite


class View(ABC):
    """Luokka, joka vastaa yksittäisestä näkymästä."""

    def __init__(
        self, description: str, help_message: str, logic: Logic, io: ConsoleIO
    ) -> None:
        self.description: str = description
        self._logic: Logic = logic
        self._help_message: str = help_message
        self._io: ConsoleIO = io

    @abstractmethod
    def start(self) -> None:
        """Käynnistää näkymän."""
        self._show_help()

    def _show_help(self) -> None:
        self._io.write(self._help_message)

    def show_cites(self, cites: list[Cite]) -> None:
        """Tulostaa viitteet.

        Args:
            cites (list[Cite]): Tulostettavat viitteet.
        """
