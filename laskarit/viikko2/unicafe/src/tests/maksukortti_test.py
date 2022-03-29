from operator import truediv
import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(self.maksukortti.saldo, 20)

    def test_rahan_ottaminen_toimii_kun_rahaa_on_tarpeeksi(self):
        self.assertTrue(self.maksukortti.ota_rahaa(self.maksukortti.saldo), True)
        self.assertEqual(self.maksukortti.saldo, 0)
    
    def test_saldo_ei_muutu_jos_katetta_ei_ole(self):
        self.assertFalse(self.maksukortti.ota_rahaa(self.maksukortti.saldo+1), False)
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_toString_toimii(self):
        self.assertEqual(str(self.maksukortti), f'saldo: {round(self.maksukortti.saldo / 100, 2)}')