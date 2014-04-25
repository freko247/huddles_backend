# -*- coding:utf8 -*-
import baseTest
import copy
import db_functions
from fixtures import huddleFixtures


class HuddleTestCase(baseTest.GenericTestCase):

    def testCreateHuddle(self):
        huddleName = db_functions.createHuddle(huddleFixtures[0])
        self.assertEqual(huddleFixtures[0]['huddleName'], huddleName)

    def testGetHuddleInfo(self):
        huddleName = db_functions.createHuddle(huddleFixtures[0])
        huddleInfo = db_functions.getHuddleInfo({'huddleName': huddleName})
        self.assertEqual(huddleFixtures[0]['huddleTag'], huddleInfo)

    def testJoinHuddle(self):
        huddleData = copy.deepcopy(huddleFixtures[0])
        huddleData['huddleUser'].pop()
        huddleName = db_functions.createHuddle(huddleData)
        huddleUser = db_functions.joinHuddle(
            {'huddleName': huddleName,
             'huddleUser': [huddleFixtures[0]['huddleUser'][-1], ]})
        self.assertEqual(huddleFixtures[0]['huddleUser'], huddleUser)

    def testGetHuddleUsers(self):
        huddleName = db_functions.createHuddle(huddleFixtures[0])
        huddleUsers = db_functions.getHuddleUsers({'huddleName': huddleName})
        self.assertEqual(huddleFixtures[0]['huddleUser'], huddleUsers)
