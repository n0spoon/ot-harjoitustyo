class CalculationRepository:
    """Luokka, joka säilöö laskutoimitukset.
    """

    def __init__(self):
        """Luokan konstruktori, joka luo uuden taulukon.

        Args:
            _calculations: Taulukko
        """

        self._calculations = []

    def add_calculation(self, content):
        """Lisää laskutoimituksen taulukkoon.

        Args:
            content (int or float): Laskutoimitus.
        """

        self._calculations.append(content)

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
