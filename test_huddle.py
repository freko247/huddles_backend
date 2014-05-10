# -*- coding:utf8 -*-
import baseTest
from datetime import datetime
import copy

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
        self.assertEqual(str(huddlesTimestamp), huddle[3])

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

    def testGetHuddlesInRangeAndTagged(self):
        db_functions.createHuddle(huddleFixtures[0])
        db_functions.createHuddle(huddleFixtures[1])
        suggestions = db_functions.getSuggestedHuddles(settingsFixtures)
        self.assertEqual([huddleFixtures[0]['huddleName']], [suggestions[0][0][0]])
        self.assertEqual(0, suggestions[1])
        self.assertEqual(1, suggestions[2])

    def testGetHuddlesInRange(self):
        db_functions.createHuddle(huddleFixtures[0])
        db_functions.createHuddle(huddleFixtures[1])
        suggestions = db_functions.getSuggestedHuddles(
            {'filterDistance': settingsFixtures['filterDistance'],
             'userLocation': settingsFixtures['userLocation'],
             })
        self.assertEqual([huddleFixtures[0]['huddleName']], [suggestions[0][0][0]])
        self.assertEqual(0, suggestions[1])
        self.assertEqual(0, suggestions[2])
