from repositories.calculation_repository import CalculationRepository


class CalculationService:
    """Luokka, joka muuntaa syötteen luvuksi ja laskee käyttäjän määrittämän laskutoimituksen."""

    def __init__(self):
        """Luokan konstruktori.  Luo uuden CalculationRepository-olion.

        Args:
            _calcdata: CalculationRepository instanssi, johon talletetaan laskutoimitusten tulokset.
        """

        self._calcdata = CalculationRepository()

    def string_to_number(self, var_s):
        """Muuntaa merkkijonon luvuksi mikäli se on joko liuku- tai kokonaisluku.

        Args:
            var_s (str): Merkkijono, joka yritetään muuttaa luvuksi.

        Returns:
            str: Virheviesti, jos merkkijono ei ole kokonaisluku tai liukuluku.
            int: Jos käyttäjän syöte on kokonaisluku.
            float: Jos käyttäjän syöte on liukuluku.
        """

        try:
            return int(str(var_s), 0)
        except ValueError:
            try:
                return float(var_s)
            except ValueError:
                return print(f"Error: {var_s} is not a number")

    def sum_service(self, var_a, var_b):
        """Laskee kahden luvun summan.

        Args:
            var_a (int or float): Käyttäjän syöttämä kokonais- tai liukuluku.
            var_b (int or float): Käyttäjän syöttämä kokonais- tai liukuluku.

        Returns:
            None: Jos vähintään toinen muuttujista var_a tai var_b ei ole luku.
            str: Laskutoimitus ja summalaskun tulos.
        """

        try:
            var_x = self.string_to_number(var_a)
            var_y = self.string_to_number(var_b)
            result = (var_x+var_y)
            result = self.clean_result(result)
            self.add_result(result)
            return f"{var_x} + {var_y} = {result}\n"
        except TypeError:
            return ""

    def sub_service(self, var_a, var_b):
        """Laskee kahden luvun erotuksen.

        Args:
            var_a (int or float): Käyttäjän syöttämä kokonais- tai liukuluku.
            var_b (int or float): Käyttäjän syöttämä kokonais- tai liukuluku.

        Returns:
            None: Jos vähintään toinen muuttujista var_a tai var_b ei ole luku.
            str: Laskutoimitus ja erotuslaskun tulos.
        """

        try:
            var_x = self.string_to_number(var_a)
            var_y = self.string_to_number(var_b)
            result = (var_x-var_y)
            result = self.clean_result(result)
            self.add_result(result)
            return f"{var_x} - {var_y} = {result}\n"
        except TypeError:
            return ""

    def mul_service(self, var_a, var_b):
        """Laskee kahden luvun kertolaskun.

        Args:
            var_a (int or float): Käyttäjän syöttämä kokonais- tai liukuluku.
            var_b (int or float): Käyttäjän syöttämä kokonais- tai liukuluku.

        Returns:
            None: Jos vähintään toinen muuttujista var_a tai var_b ei ole luku.
            str: Laskutoimitus ja kertolaskun tulos.
        """

        try:
            var_x = self.string_to_number(var_a)
            var_y = self.string_to_number(var_b)
            result = (var_x*var_y)
            result = self.clean_result(result)
            self.add_result(result)
            return f"{var_x} * {var_y} = {result}\n"
        except TypeError:
            return ""

    def div_service(self, var_a, var_b):
        """Laskee jakolaskun, jossa var_a on jaettava ja var_b on jakaja.

        Args:
            var_a (int or float): Käyttäjän syöttämä kokonais- tai liukuluku.
            var_b (int or float): Käyttäjän syöttämä kokonais- tai liukuluku.

        Returns:
            None: Jos vähintään toinen muuttujista var_a tai var_b ei ole luku.
            str: Virheviesti, jos jakajan arvo on nolla.
            str: Laskutoimitus ja jakolaskun tulos.
        """

        try:
            var_x = self.string_to_number(var_a)
            var_y = self.string_to_number(var_b)
            if var_y == 0:
                return "Error: Division by Zero isn't allowed\n"
            result = (var_x/var_y)
            result = self.clean_result(result)
            self.add_result(result)
            return f"{var_x} / {var_y} = {result}\n"
        except TypeError:
            return ""

    def sqrt_service(self, var_a):
        """Laskee positiivisen reaaliluvun neliöjuuren.

        Args:
            var_a (int or float): Käyttäjän syöttämä kokonais- tai liukuluku.

        Returns:
            None: Jos muuttuja var_a ei ole luku.
            str: Virheviesti, jos luku ei ole positiivinen.
            str: Laskutoimitus ja luvun neliöjuuren tulos.
        """

        try:
            var_x = self.string_to_number(var_a)
            if var_x < 0:
                return f"Error: Input {var_x} is not a positive number\n"
            result = var_x**(1/2)
            result = f"±{self.clean_result(result)}"
            self.add_result(result)
            return f"√{var_x} = {result}\n"
        except TypeError:
            return ""

    def exp_service(self, var_a, var_b):
        """Laskee exponenttilaskun, jossa var_a on kantaluku ja var_b eksponentti.

        Args:
            var_a (int or float): Käyttäjän syöttämä kokonais- tai liukuluku, kantaluku.
            var_b (int or float): Käyttäjän syöttämä kokonais- tai liukuluku, eksponentti.

        Returns:
            None: Jos vähintään toinen muuttujista var_a tai var_b ei ole luku.
            str: Virheviesti, jos kantaluku on nolla ja eksponentti negatiivinen.
            str: Laskutoimitus ja eksponenttilaskun tulos.
        """

        try:
            var_x = self.string_to_number(var_a)
            var_y = self.string_to_number(var_b)
            var_x = self.clean_result(var_x)
            if (var_x == 0) and (var_y < 0):
                return "Error: Division by Zero isn't allowed\n"
            result = var_x**var_y
            result = self.clean_result(result)
            if var_y == 0.5:
                result = f"±{self.clean_result(result)}"
            self.add_result(result)
            return f"{var_x}^{var_y} = {result}\n"
        except TypeError:
            return ""

    def inv_service(self, var_a):
        """Laskee luvun var_a käänteisluvun.

        Args:
            var_a (int or float): Käyttäjän syöttämä kokonais- tai liukuluku.

        Returns:
            None: Jos muuttuja var_a ei ole luku.
            str: Virheviesti, jos muuttujan var_a arvo on nolla.
            str: Laskutoimitus ja luvun käänteisluku.
        """

        try:
            var_x = self.string_to_number(var_a)
            if var_x == 0:
                return "Error: Division by Zero isn't allowed\n"
            result = 1/var_x
            result = self.clean_result(result)
            self.add_result(result)
            return f"1 / {var_x} = {result}\n"
        except TypeError:
            return ""

    def clean_result(self, result):
        """Siistii annetun luvun kokonaisluvuksi mikäli mahdollista.

        Args:
            result (int or float): Siistittävä luku.

        Returns:
            int: Jos luku on kokonaisluku tai liukuluku, jonka desimaaliosa on nolla.
            float: Jos luku on liukuluku, jonka desimaaliosa ei ole nolla.
        """

        pieces = str(result).split(".")
        if len(pieces[-1]) == 1:
            last = int(pieces[-1])
            if last == 0:
                result = int(result)
        return result

    def count(self):
        """Palauttaa laskutoimitusten määrän.

        Returns:
            int: Laskutoimitusten määrä.
        """

        return self._calcdata.count_calculations()

    def return_calculations(self):
        """Palauttaa listan lasketuista laskutoimituksista.

        Returns:
            Lista laskutoimituksista.
        """

        return self._calcdata.print_calculations()

    def add_result(self, result):
        """Tallentaa tuloksen tietokantaan.

        Args:
            result (int, float or str): Laskutoimituksen tulos.
        """

        self._calcdata.add_calculation(result)

    def get_last_result(self):
        """Hakee viimeisimmän laskutoimituksen tuloksen.

        Returns:
            str: Viimeisimmän laskutoimituksen tulos.
        """

        return self._calcdata.get_last()

    def clear_last_calculation(self):
        """Poistaa viimeisimmän laskutoimituksen tuloksen muistista.

        Returns:
            str: Ilmoittaa poistetun tuloksen, jos muisti ei ole tyhjä.
            str: Ilmoittaa virheviestin, jos muisti on tyhjä.
        """

        if self._calcdata.count_calculations() > 0:
            last = self._calcdata.get_last()
            self._calcdata.clear_last()
            return f"Cleared last result from memory: {last}\n"
        return "Error: Memory is empty.\n"

    def clear_all_calculations(self):
        """Poistaa kaikkien laskutoimitusten tulokset muistista.

        Returns:
            str: Ilmoittaa muistin tyhjentyneen, jos muisti ei ole tyhjä.
            str: Ilmoittaa virheviestin, jos muisti on tyhjä.
        """

        if self._calcdata.count_calculations() > 0:
            self._calcdata.clear_all()
            return "Cleared everything from memory.\n"
        return "Error: Memory is empty.\n"
