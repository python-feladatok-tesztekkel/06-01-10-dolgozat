from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok



class TestEBetukSzama5(TestCase):
    def test_feladat05(self):
        aktualis = feladatok.ebetuk_szama("abcdfgh12fdsd")
        elvart = 0
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg az e vagy é betűk számát")
