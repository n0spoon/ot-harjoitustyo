from math import pi, e, ceil, floor
from pandas import isna
from repositories.calculation_repository import CalculationRepository


class CalculationService:
    """Luokka, joka muuntaa syötteen luvuksi ja laskee käyttäjän määrittämän laskutoimituksen."""

    def __init__(self):
        """Luokan konstruktori.  Luo uuden CalculationRepository-olion.

        Args:
            _calcdata: CalculationRepository instanssi, johon talletetaan laskutoimitusten tulokset.
        """

        self._calcdata = CalculationRepository()

    def constant_pi(self):
        """Pii vakio math kirjastosta.

        Returns:
            float: Piin likiarvo.
        """

        return pi

    def constant_e(self):
        """Neperin luku math kirjastosta.

        Returns:
            float: Neperin luvun likiarvo.
        """

        return e

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
                try:
                    if var_s.lower() == "nan" or var_s.lower() == "-nan":
                        return print(f"Error: {var_s} is not a number.")
                except AttributeError:
                    pass
                return float(var_s)
            except ValueError:
                return print(f"Error: {var_s} is not a number.")

    def sum_service(self, var_a, var_b):
        """Laskee kahden luvun summan.

        Args:
            var_a (str): Käyttäjän syöttämä luku.
            var_b (str): Käyttäjän syöttämä luku.

        Returns:
            None: Jos vähintään toinen muuttujista var_a tai var_b ei ole luku.
            str: Laskutoimitus ja summalaskun tulos.
        """

        if isna(var_a) or isna(var_b):
            return ""
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
            var_a (str): Käyttäjän syöttämä luku.
            var_b (str): Käyttäjän syöttämä luku.

        Returns:
            None: Jos vähintään toinen muuttujista var_a tai var_b ei ole luku.
            str: Laskutoimitus ja erotuslaskun tulos.
        """

        if isna(var_a) or isna(var_b):
            return ""
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
            var_a (str): Käyttäjän syöttämä luku.
            var_b (str): Käyttäjän syöttämä luku.

        Returns:
            None: Jos vähintään toinen muuttujista var_a tai var_b ei ole luku.
            str: Laskutoimitus ja kertolaskun tulos.
        """

        if isna(var_a) or isna(var_b):
            return ""
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
            var_a (str): Käyttäjän syöttämä luku.
            var_b (str): Käyttäjän syöttämä luku.

        Returns:
            None: Jos vähintään toinen muuttujista var_a tai var_b ei ole luku.
            str: Virheviesti, jos jakajan arvo on nolla.
            str: Laskutoimitus ja jakolaskun tulos.
        """

        if isna(var_a) or isna(var_b):
            return ""
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
            var_a (str): Käyttäjän syöttämä luku.

        Returns:
            None: Jos muuttuja var_a ei ole luku.
            str: Virheviesti, jos luku ei ole positiivinen.
            str: Laskutoimitus ja luvun neliöjuuren tulos.
        """

        if isna(var_a):
            return ""
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
            var_a (str): Käyttäjän syöttämä luku, kantaluku.
            var_b (str): Käyttäjän syöttämä luku, eksponentti.

        Returns:
            None: Jos vähintään toinen muuttujista var_a tai var_b ei ole luku.
            str: Virheviesti, jos kantaluku on nolla ja eksponentti negatiivinen.
            str: Laskutoimitus ja eksponenttilaskun tulos.
        """

        if isna(var_a) or isna(var_b):
            return ""
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
            var_a (str): Käyttäjän syöttämä luku.

        Returns:
            None: Jos muuttuja var_a ei ole luku.
            str: Virheviesti, jos muuttujan var_a arvo on nolla.
            str: Laskutoimitus ja luvun käänteisluku.
        """

        if isna(var_a):
            return ""
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

    def ceil_service(self, var_a):
        """Laskee luvun kattofunktion tuloksen.

        Args:
            var_a (str): Käyttäjän syöttämä luku.

        Returns:
            None: Jos muuttuja var_a ei ole luku.
            str: Laskutoimitus ja tulos.
        """

        if isna(var_a):
            return ""
        try:
            var_x = self.string_to_number(var_a)
            result = ceil(var_x)
            self.add_result(result)
            return f"The ceiling value of {var_a} = {result}\n"
        except TypeError:
            return ""

    def floor_service(self, var_a):
        """Laskee luvun lattiafunktion tuloksen.

        Args:
            var_a (str): Käyttäjän syöttämä luku.

        Returns:
            None: Jos muuttuja var_a ei ole luku.
            str: Laskutoimitus ja tulos.
        """

        if isna(var_a):
            return ""
        try:
            var_x = self.string_to_number(var_a)
            result = floor(var_x)
            self.add_result(result)
            return f"The floor value of {var_a} = {result}\n"
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
        """Palauttaa merkkijonon, jossa on laskettujen laskutoimitusten tulokset.

        Returns:
            Virheviesti, jos muisti on tyhjä.
            str: Muistissa olevien laskutoimitusten tulokset.
        """

        if not self.memory_is_empty():
            calculations = self._calcdata.print_calculations()
            to_return = ""
            for calculation in calculations:
                to_return += calculation + ", "
            return f"Calculations in memory: {to_return[:-2]}\n"
        return "Error: Memory is empty.\n"

    def add_result(self, result):
        """Tallentaa tuloksen tietokantaan, jos tulos ei ole NaN.

        Args:
            result (int, float or str): Laskutoimituksen tulos.
        """
        if not isna(result):
            self._calcdata.add_calculation(result)

    def get_last_result(self):
        """Hakee viimeisimmän laskutoimituksen tuloksen.

        Returns:
            str: Viimeisimmän laskutoimituksen tulos.
        """

        return self._calcdata.get_last()

    def clear_last_calculation(self):
        """Poistaa viimeisimmän laskutoimituksen tuloksen muistista, jos muisti ei ole tyhjä.

        Returns:
            str: Ilmoittaa poistetun tuloksen, jos muisti ei ole tyhjä.
            str: Ilmoittaa virheviestin, jos muisti on tyhjä.
        """

        if not self.memory_is_empty():
            last = self._calcdata.get_last()
            self._calcdata.clear_last()
            return f"Cleared last result from memory: {last}\n"
        return "Error: Memory is empty.\n"

    def clear_all_calculations(self):
        """Poistaa kaikkien laskutoimitusten tulokset muistista, jos muisti ei ole tyhjä.

        Returns:
            str: Ilmoittaa muistin tyhjentyneen, jos muisti ei ole tyhjä.
            str: Ilmoittaa virheviestin, jos muisti on tyhjä.
        """

        if not self.memory_is_empty():
            self._calcdata.clear_all()
            return "Cleared everything from memory.\n"
        return "Error: Memory is empty.\n"

    def memory_is_empty(self):
        """Palauttaa totuusarvon, joka kuvaa muistin tilaa.

        Returns:
            True: Muisti on tyhjä
            False: Muisti ei ole tyhjä
        """

        return self._calcdata.memory_is_empty()
