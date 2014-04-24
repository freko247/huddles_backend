# -*- coding:utf8 -*-
import baseTest
import db_functions
from fixtures import huddleFixtures


class HuddleTestCase(baseTest.GenericTestCase):
    def testCreateHuddle(self):
        huddleName = db_functions.createHuddle(huddleFixtures[0])
        self.assertEqual(huddleFixtures[0]['huddleName'], huddleName)
