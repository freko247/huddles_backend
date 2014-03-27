# -*- coding:utf8 -*-
import unittest

from google.appengine.api import memcache
from google.appengine.ext import testbed
from google.appengine.ext import ndb

import db_functions


def testAddUser():
    userData = {
        'userName': 'John Doe',
        'userEmail': 'john@mail.com',
        # userSkill: ['Python', 'Mobile', 'Java'],
        # userTag: ['DTU', 'Digital Media Engineering', 'Android'],
    }
    return db_functions.addUser(userData)


class DemoTestCase(unittest.TestCase):
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

    def testInsertEntity(self):
        userKey = testAddUser()
        self.assertTrue(isinstance(userKey, ndb.Key))
