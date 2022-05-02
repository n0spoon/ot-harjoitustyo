from repositories.calculation_repository import CalculationRepository


class CalculationService:
    """Luokka, joka muuntaa syötteen numeroksi ja laskee käyttäjän määrittämän laskutoimituksen.

    Attributes:
        _calcdata: CalculationRepository instanssi, johon talletetaan laskutoimituksien tulokset.
    """

    def __init__(self):
        """Luokan konstruktori.  Luo uuden CalculationRepository-olion.

        Args:
            _calcdata: CalculationRepository instanssi, johon talletetaan laskutoimitusten tulokset.
        """

        self._calcdata = CalculationRepository()

    def string_to_number(self, var_s):
        """Muuntaa merkkijonon numeroksi mikäli se on joko liuku- tai kokonaisluku.

        Args:
            var_s (str): Merkkijono, joka kuvaa numeroa.

        Returns:
            Tulostaa virheviestin, jos merkkijono ei ole kokonaisluku tai liukuluku.
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
            None olio, jos vähintään toinen muuttujista var_a tai var_b ei ole numero.
            Muuten tulostaa summalaskun.
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
            None olio, jos vähintään toinen muuttujista var_a tai var_b ei ole numero.
            Muuten tulostaa erotuslaskun.
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
            None olio, jos vähintään toinen muuttujista var_a tai var_b ei ole numero.
            Muuten tulostaa kertoslaskun.
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
        """Laskee kahden luvun jakolaskun.

        Args:
            var_a (int or float): Käyttäjän syöttämä kokonais- tai liukuluku.
            var_b (int or float): Käyttäjän syöttämä kokonais- tai liukuluku.

        Returns:
            None olio, jos vähintään toinen muuttujista var_a tai var_b ei ole numero.
            Tulostaa virheviestin, jos jakajan arvo on nolla.
            Muuten tulostaa jakolaskun.
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
        """Laskee reaaliluvun neliöjuuren.

        Args:
            var_a (int or float): Käyttäjän syöttämä kokonais- tai liukuluku.

        Returns:
            None olio, jos muuttuja var_a ei ole numero.
            Tulostaa virheviestin, jos luku ei ole positiivinen.
            Muuten tulostaa luvun neliöjuuren.
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
            None olio, jos vähintään toinen muuttujista var_a tai var_b ei ole numero.
            Tulostaa virheviestin, jos kantaluku on nolla ja eksponentti negatiivinen.
            Muuten tulostaa eksponenttilaskun.
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

    def clean_result(self, result):
        """Siistii annetun numeron.

        Args:
            result (int or float): Laskutoimituksen tulos.

        Returns:
            int: Jos numero on liukuluku, jonka desimaaliosa on nolla.
            float: Jos numero on liukuluku, jonka desimaaliosa ei ole nolla.
        """

        pieces = str(result).split(".")
        if len(pieces[-1]) == 1:
            last = int(pieces[-1])
            if last == 0:
                result = int(result)
        return result

    def count(self):
        """Laskee laskutoimitusten määrän.

        Returns:
            int: Laskutoimitusten määrä.
        """
        return self._calcdata.count_calculations()

    def return_calculations(self):
        """Tulostaa lasketut laskutoimitukset.

        Returns:
            Lista laskutoimituksista.
        """

        return self._calcdata.print_calculations()

    def add_result(self, result):
        """Tallentaa laskutoimituksen _calcdata-olioon.

        Args:
            result (int or float): Laskutoimituksen tulos.
        """

        self._calcdata.add_calculation(result)
