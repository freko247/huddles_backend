# -*- coding:utf8 -*-
import unittest

from google.appengine.api import memcache
from google.appengine.ext import testbed
from google.appengine.ext import ndb

import db_functions
import models

userFixtures = [{'userEmail': 'user@mail.com',
                'userName': 'John Doe',
                'userSkill': ['Python', 'Communication', 'Leadership'],
                'userTag': ['DTU', 'Digital Media Engineering', 'Android'],
                 },
                {'userEmail': 'rating.user@mail.com',
                 'userName': 'Jane Doe',
                 },
                ]
ratingFixtures = [{'userEmail': userFixtures[0]['userEmail'],
                   'ratingUserEmail': userFixtures[1]['userEmail'],
                   'ratingValue': 5,
                   },
                  ]

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
        userKey = db_functions.addUser(userFixtures[0])
        self.assertTrue(isinstance(userKey, ndb.Key))

    def testAddUserRating(self):
        # Add rating
        ratingKey = db_functions.addRating(ratingFixtures[0])
        self.assertTrue(isinstance(ratingKey, ndb.Key))
