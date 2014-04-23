# -*- coding:utf8 -*-
from google.appengine.ext import ndb

import baseTest
import db_functions
from fixtures import huddleFixtures


class HuddleTestCase(baseTest.GenericTestCase):
    def testCreateHuddle(self):
        huddleKey = db_functions.createHuddle(huddleFixtures[0])
        self.assertTrue(isinstance(huddleKey, ndb.Key))
