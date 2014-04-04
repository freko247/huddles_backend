# -*- coding:utf8 -*-
import unittest
from datetime import datetime

from google.appengine.ext import testbed
from google.appengine.ext import ndb

import baseTest
import db_functions
import models
from fixtures import huddleFixtures

class HuddleTestCase(baseTest.GenericTestCase):
    def testCreateHuddle(self):
        huddleKey = db_functions.createHuddle(huddleFixtures[0])
        self.assertTrue(isinstance(huddleKey, ndb.Key))
