from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class Szogek8(TestCase):
    def test_feladat(self):
        aktualis = feladatok.szog(0)
        elvart = "nullszög"
        self.assertEqual(elvart, aktualis, elvart+" szöget rosszul határozta meg!")

