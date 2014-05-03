# -*- coding:utf8 -*-
import copy

import baseTest
import db_functions
from fixtures import userFixtures, ratingFixtures


class HuddleTestCase(baseTest.GenericTestCase):

    def testAddUser(self):
        userEmail = db_functions.addUser(userFixtures[0])
        self.assertEqual(userFixtures[0]['userEmail'], userEmail)

    def testAddUserSkill(self):
        userData = copy.deepcopy(userFixtures[0])
        userData['userSkill'].pop()
        db_functions.addUser(userData)
        userData = {'userEmail': userFixtures[0]['userEmail'],
                    'userSkill': [userFixtures[0]['userSkill'][-1]],
                    }
        userSkill = db_functions.addUserSkill(userData)
        self.assertEqual(userSkill, userFixtures[0]['userSkill'])

    def testRemoveUserSkill(self):
        db_functions.addUser(userFixtures[0])
        userData = {'userEmail': userFixtures[0]['userEmail'],
                    'userSkill': [userFixtures[0]['userSkill'][-1]],
                    }
        userSkill = db_functions.removeUserSkill(userData)
        self.assertEqual(userSkill, userFixtures[0]['userSkill'][:-1])

    def testAddUserRating(self):
        # Add rating
        ratingUserEmail = db_functions.addRating(ratingFixtures[0])
        self.assertEqual(ratingFixtures[0]['ratingUserEmail'], ratingUserEmail)

    def testAuthenticateUser(self):
        userEmail = db_functions.addUser(userFixtures[0])
        authenticatedUserEmail = db_functions.authenticateUser(
            {'userEmail': userEmail,
             'userPassword': userFixtures[0]['userPassword']})
        self.assertEqual(userFixtures[0]['userEmail'], authenticatedUserEmail)

    def testGetUserInfo(self):
        userEmail = db_functions.addUser(userFixtures[0])
        userAvatar = db_functions.getUserInfo({'userEmail': userEmail, })
        self.assertEqual(userFixtures[0]['userAvatar'], userAvatar[2])
