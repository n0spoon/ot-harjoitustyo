class CalculationRepository:
    """Luokka, joka säilöö laskutoimitukset."""

    def __init__(self):
        """Luokan konstruktori, joka luo uuden taulukon.

        Args:
            _calculations: Taulukko
        """

        self._calculations = []

    def add_calculation(self, result):
        """Lisää laskutoimituksen tuloksen muistiin.

        Args:
            result (int, float or str): Laskutoimituksen tulos.
        """

        self._calculations.append(result)

    def print_calculations(self):
        """Tulostaa listan laskutoimituksista.

        Returns:
            Lista laskutoimituksista.
        """

        return print(self._calculations)

    def count_calculations(self):
        """Palauttaa taulukon koon.

        Returns:
            int: Taulukon koko.
        """

        return len(self._calculations)

    def get_last(self):
        """Palauttaa taulukon viimeisen alkion.

        Returns:
            int, float or str: Taulukon viimeinen alkio.
        """

        try:
            return self._calculations[-1]
        except IndexError:
            return "Memory is empty\n"

    def clear_last(self):
        """Poistaa viimeisimmän laskutoimituksen, jos muisti ei ole tyhjä."""

        if self.count_calculations() > 0:
            self._calculations.pop()

    def clear_all(self):
        """Poistaa kaikki laskutoimitukset muistista, jos muisti ei ole tyhjä."""

        if self.count_calculations() > 0:
            self._calculations.clear()
