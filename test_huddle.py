# -*- coding:utf8 -*-
import baseTest
import db_functions
from fixtures import huddleFixtures


class HuddleTestCase(baseTest.GenericTestCase):

    def testCreateHuddle(self):
        huddleName = db_functions.createHuddle(huddleFixtures[0])
        self.assertEqual(huddleFixtures[0]['huddleName'], huddleName)

    def testGetHuddle(self):
        huddleName = db_functions.createHuddle(huddleFixtures[0])
        huddleInfo = db_functions.getHuddleInfo({'huddleName': huddleName})
        self.assertEqual(huddleFixtures[0]['huddleTag'], huddleInfo)
