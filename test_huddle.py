# -*- coding:utf8 -*-
import unittest
from datetime import datetime

from google.appengine.ext import testbed
from google.appengine.ext import ndb

import db_functions
import models


huddleFixtures = [{'huddleDateAndTime': datetime.now(),
                   'huddleLocation': ndb.GeoPt('55.785061,12.519927'),
                   'huddleAdmin': 'user@mail.com',
                   'huddleName': 'Mobile Prototyping',
                   'huddleTags': ['DTU', '02728', 'Digital Media Engineering'],
                   'huddleUser': ['user@mail.com', 'tester@mail.com'],
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

    def testCreateHuddle(self):
        huddleKey = db_functions.createHuddle(huddleFixtures[0])
        self.assertTrue(isinstance(huddleKey, ndb.Key))
