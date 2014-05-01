# -*- coding:utf8 -*-
import baseTest
from datetime import datetime
import copy
import logging

import db_functions
from fixtures import huddleFixtures, settingsFixtures


class HuddleTestCase(baseTest.GenericTestCase):

    def testCreateHuddle(self):
        huddleName = db_functions.createHuddle(huddleFixtures[0])
        self.assertEqual(huddleFixtures[0]['huddleName'], huddleName)

    def testGetHuddleInfo(self):
        huddleName = db_functions.createHuddle(huddleFixtures[0])
        huddle = db_functions.getHuddleInfo({'huddleName': huddleName})
        huddlesTimestamp = datetime.utcfromtimestamp(
            int(huddleFixtures[0]['huddleDateAndTime'][:-3]))
        self.assertEqual(huddleFixtures[0]['huddleName'], huddle[0])
        self.assertEqual(huddleFixtures[0]['huddleTag'], huddle[1])
        self.assertEqual(huddleFixtures[0]['huddleLocation'], huddle[2])
        self.assertEqual(huddlesTimestamp, huddle[3])

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

    def testGetHuddlesInRange(self):
        db_functions.createHuddle(huddleFixtures[0])
        huddles = db_functions.getSuggestedHuddles(settingsFixtures)
        logging.debug([str(huddleFixtures[0]['huddleName']),
                       huddleFixtures[0]['huddleTag'],
                       huddleFixtures[0]['huddleLocation'],
                       huddleFixtures[0]['huddleDateAndTime']])
        huddlesTimestamp = datetime.utcfromtimestamp(
            int(huddleFixtures[0]['huddleDateAndTime'][:-3]))
        self.assertEqual(huddleFixtures[0]['huddleName'], huddles[0][0])
        self.assertEqual(huddleFixtures[0]['huddleTag'], huddles[0][1])
        self.assertEqual(huddleFixtures[0]['huddleLocation'], huddles[0][2])
        self.assertEqual(huddlesTimestamp, huddles[0][3])
