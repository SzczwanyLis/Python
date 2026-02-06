import unittest

class BankAccount:
    def __init__(self, saldo_startowe=0):
        self.saldo = saldo_startowe

    def wplac(self, kwota):
        if kwota <= 0:
            raise ValueError("Kwota musi byc dodatnia")
        self.saldo += kwota

    def wyplac(self, kwota):
        if kwota <= 0:
            raise ValueError("Kwota musi byc dodatnia")
        if kwota > self.saldo:
            raise ValueError("Brak srodkow na koncie")
        self.saldo -= kwota

    def stan_konta(self):
        return self.saldo

class TestBanku(unittest.TestCase):
    def setUp(self):
        self.konto = BankAccount(420)

    def test_wplaty(self):
        self.konto.wplac(80)
        self.assertEqual(self.konto.stan_konta(), 500)

    def test_wyplaty(self):
        self.konto.wyplac(420)
        self.assertEqual(self.konto.stan_konta(), 0)

    def test_wyplaty_za_duzo(self):
        with self.assertRaises(ValueError):
            self.konto.wyplac(421)

    def test_bledne_kwoty(self):
        with self.assertRaises(ValueError):
            self.konto.wplac(-50)
        with self.assertRaises(ValueError):
            self.konto.wyplac(0)

if __name__ == '__main__':
    unittest.main()