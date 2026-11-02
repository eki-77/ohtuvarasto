import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varasto_negatiivinen(self):
        testivarasto = Varasto(0, -5)
        self.assertAlmostEqual(testivarasto.tilavuus, 0)
        self.assertAlmostEqual(testivarasto.saldo, 0)

    def test_konstruktori_rajoittaa_saldon_tilavuuteen(self):
        testivarasto = Varasto(10, 12)

        self.assertAlmostEqual(testivarasto.saldo, 10)
        self.assertAlmostEqual(testivarasto.paljonko_mahtuu(), 0)

    def test_lisays_ei_yrita_lisata_negatiivista_maaraa(self):
        self.varasto.lisaa_varastoon(3)

        self.varasto.lisaa_varastoon(-2)

        self.assertAlmostEqual(self.varasto.saldo, 3)

    def test_lisays_ei_yrita_lisata_yli_tilavuuden(self):
        self.varasto.lisaa_varastoon(12)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_palauttaa_varastossa_olevan_maaran(self):
        self.varasto.lisaa_varastoon(3)

        saatu_maara = self.varasto.ota_varastosta(5)

        self.assertAlmostEqual(saatu_maara, 3)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_negatiivisen_maaran_ottaminen_palauttaa_nollan(self):
        self.varasto.lisaa_varastoon(3)

        saatu_maara = self.varasto.ota_varastosta(-2)

        self.assertAlmostEqual(saatu_maara, 0)
        self.assertAlmostEqual(self.varasto.saldo, 3)

    dev test_merkkijonoesitys(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
