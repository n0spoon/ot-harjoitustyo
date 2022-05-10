from db_connection import get_db_connection


class CalculationRepository:
    """Laskutoimitusten säilönnästä vastaava luokka."""

    def __init__(self):
        """Luokan konstruktori, luo uuden tietokanta-olion.

        Args:
            _db: Tietokantayhteyden Connection-olio.
        """

        self._db = get_db_connection()

    def add_calculation(self, result):
        """Lisää laskutoimituksen tuloksen tietokannan muistiin.

        Args:
            result (str): Laskutoimituksen tulos.
        """

        if not isinstance(result, str):
            result = str(result)

        cursor = self._db.cursor()

        cursor.execute(
            "INSERT INTO Calculations (result) values (?)", [result])
        self._db.commit()

    def print_calculations(self):
        """Hakee ja palauttaa listan, jossa on laskutoimitusten tulokset.

        Returns:
            Lista laskutoimituksista.
        """

        cursor = self._db.cursor()

        cursor.execute("SELECT * FROM Calculations")

        calculations = cursor.fetchall()
        calculations_to_return = []
        for calculation in calculations:
            calculations_to_return.append(
                dict(zip(calculation.keys(), calculation))["result"])
        return calculations_to_return

    def count_calculations(self):
        """Palauttaa laskutoimitusten lukumäärän.

        Returns:
            int: Laskettujen laskutoimitusten lukumäärä.
        """

        cursor = self._db.cursor()

        cursor.execute("SELECT * FROM Calculations")

        calculations = cursor.fetchall()
        return len(calculations)

    def memory_is_empty(self):
        """Palauttaa totuusarvon, joka kuvaa muistin tilaa.

        Returns:
            True: Muisti on tyhjä
            False: Muisti ei ole tyhjä
        """

        return self.count_calculations() < 1

    def get_last(self):
        """Palauttaa viimeisen laskutoimituksen tuloksen.

        Returns:
            str: Viimeisimmän laskutoimituksen tulos tietokannassa.
            str: Virheviesti, jos tietokanta on tyhjä.
        """

        if not self.memory_is_empty():
            cursor = self._db.cursor()

            cursor.execute(
                "SELECT * FROM Calculations ORDER BY rowid DESC LIMIT 1")
            result = cursor.fetchone()

            unpacked_result = dict(zip(result.keys(), result))
            return unpacked_result["result"]
        return "Memory is empty\n"

    def clear_last(self):
        """Poistaa viimeisimmän laskutoimituksen tietokannan muistista."""

        cursor = self._db.cursor()

        cursor.execute(
            "DELETE FROM Calculations WHERE id = (SELECT MAX(id) FROM Calculations)")

        self._db.commit()

    def clear_all(self):
        """Poistaa kaikki laskutoimitukset tietokannan muistista."""

        cursor = self._db.cursor()

        cursor.execute("DELETE FROM Calculations")

        self._db.commit()
