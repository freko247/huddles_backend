# -*- coding:utf8 -*-
import baseTest
import geo

from fixtures import geoFixtures


class GeoTestCase(baseTest.GenericTestCase):

    def testBoundingBox(self):
        dlat, dlon = geo.bounding_box(geoFixtures[0]['startLat'],
                                      geoFixtures[0]['distance'])
        self.assertEqual(round(dlat, 4), round(geoFixtures[0]['dlat'], 4))