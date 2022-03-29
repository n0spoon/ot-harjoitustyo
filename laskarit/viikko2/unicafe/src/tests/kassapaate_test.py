from operator import truediv
import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(640)

    def test_correct_status(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateisosto_toimii(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)

        if self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10):
            self.assertEqual(self.kassapaate.kassassa_rahaa, 100010)
            self.assertEqual(self.kassapaate.edulliset, 1)

        if self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(410), 10):
            self.assertEqual(self.kassapaate.kassassa_rahaa, 100010)
            self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_toimii(self):
        if self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.kortti)):
            self.assertEqual(self.kortti.saldo, 400)
            self.assertEqual(self.kassapaate.edulliset, 1)
            
        if self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.kortti)):
            self.assertEqual(self.kortti.saldo, 0)
            self.assertEqual(self.kassapaate.maukkaat, 1)

        if self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.kortti)):
            self.assertEqual(self.kortti.saldo, 0)
            self.assertEqual(self.kassapaate.maukkaat, 0)

        if self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.kortti)):
            self.assertEqual(self.kortti.saldo, 0)
            self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kortin_lataus_toimii(self):
        if self.kassapaate.lataa_rahaa_kortille(self.kortti, 360):
            self.assertEqual(self.kortti.saldo, 1000)
            self.assertEqual(self.kassapaate.kassassa_rahaa, 100360)
        self.assertFalse(self.kassapaate.lataa_rahaa_kortille(self.kortti, -13))