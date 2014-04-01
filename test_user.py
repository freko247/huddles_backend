# -*- coding:utf8 -*-
import unittest

from google.appengine.api import memcache
from google.appengine.ext import testbed
from google.appengine.ext import ndb

import models

class GenericTestCase(unittest.TestCase):
    def setUp(self):
        # First, create an instance of the Testbed class.
        self.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        self.testbed.activate()
        # Next, declare which service stubs you want to use.
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def testAddUser(self):
        userEmail = 'user@mail.com'
        userName = 'John Doe'
        userSkill = ['Python', 'Communication', 'Leadership']
        userTag = ['DTU', 'Digital Media Engineering', 'Android']
        user = models.User(key=ndb.Key('User', userEmail))
        user.populate(userEmail=userEmail,
                      userName=userName,
                      userSkill=userSkill,
                      userTag=userTag,
                      )
        userKey = user.put()
        self.assertTrue(isinstance(userKey, ndb.Key))

    def testAddUserRating(self):
        # Add user
        userEmail = 'test.user@mail.com'
        userName = 'John Doe'
        user = models.User(key=ndb.Key('User', userEmail),
                           userEmail=userEmail,
                           userName=userName)
        user.put()
        ratingUserEmail = 'rating.user@mail.com'
        ratingUserName = 'Jane Doe'
        ratingUser = models.User(key=ndb.Key(models.User,
                                             ratingUserEmail),
                                 userEmail=ratingUserEmail,
                                 userName=ratingUserName)
        ratingUser.put()
        # Add rating
        rating = models.Rating(key=ndb.Key(models.User,
                                           user.userEmail,
                                           models.Rating,
                                           ratingUser.userEmail),
                               ratingUser=ratingUser.userEmail,
                               ratingValue=5).put()
        self.assertTrue(isinstance(rating, ndb.Key))
