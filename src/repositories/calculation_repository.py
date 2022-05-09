from db_connection import get_db_connection


class CalculationRepository:
    """Laskutoimitusten säilönnästä vastaava luokka"""

    def __init__(self):
        """Luokan konstruktori.

        Args:
            _db: Tietokantayhteyden Connection-olio
        """

        self._db = get_db_connection()

    def add_calculation(self, result):
        """Lisää laskutoimituksen tuloksen muistiin.

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
        """Hakee ja palauttaa listan, jossa on laskutoimituksien tulokset.

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

    def get_last(self):
        """Palauttaa viimeisen tuloksen.

        Returns:
            str: Viimeisimmän laskutoimituksen tulos tietokannassa.
        """

        if self.count_calculations() > 0:
            cursor = self._db.cursor()

            cursor.execute(
                "SELECT * FROM Calculations ORDER BY rowid DESC LIMIT 1")
            result = cursor.fetchone()

            unpacked_result = dict(zip(result.keys(), result))
            return unpacked_result["result"]
        return "Memory is empty.\n"

    def clear_last(self):
        """Poistaa viimeisimmän laskutoimituksen, jos muisti ei ole tyhjä."""

        last = self.get_last()
        cursor = self._db.cursor()

        cursor.execute(
            "DELETE FROM Calculations WHERE id = (SELECT MAX(id) FROM Calculations)")

        self._db.commit()
        return f"Cleared last result from memory: {last}.\n"

    def clear_all(self):
        """Poistaa kaikki laskutoimitukset muistista, jos muisti ei ole tyhjä."""

        cursor = self._db.cursor()

        cursor.execute("DELETE FROM Calculations")

        self._db.commit()
