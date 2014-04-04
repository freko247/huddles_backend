# -*- coding:utf8 -*-
from google.appengine.ext import testbed
from google.appengine.ext import ndb

import baseTest
import db_functions
import models
from fixtures import userFixtures, ratingFixtures

class HuddleTestCase(baseTest.GenericTestCase):

    def testAddUser(self):
        userKey = db_functions.addUser(userFixtures[0])
        self.assertTrue(isinstance(userKey, ndb.Key))

    def testAddUserSkill(self):
        userData = userFixtures[0]
        userData['userSkill'].pop()
        db_functions.addUser(userData)
        userData = {'userEmail': userFixtures[0]['userEmail'],
                    'userSkill': [userFixtures[0]['userSkill'][-1]],
                    }
        updatedUserKey = db_functions.addUserSkill(userData)
        user = updatedUserKey.get()
        self.assertEqual(user.userSkill, userFixtures[0]['userSkill'])

    def testRemoveUserSkill(self):
        db_functions.addUser(userFixtures[0])
        userData = {'userEmail': userFixtures[0]['userEmail'],
                    'userSkill': [userFixtures[0]['userSkill'][-1]],
                    }
        updatedUserKey = db_functions.removeUserSkill(userData)
        user = updatedUserKey.get()
        self.assertEqual(user.userSkill, userFixtures[0]['userSkill'][:-1])

    def testAddUserRating(self):
        # Add rating
        ratingKey = db_functions.addRating(ratingFixtures[0])
        self.assertTrue(isinstance(ratingKey, ndb.Key))
