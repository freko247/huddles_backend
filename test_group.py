# -*- coding:utf8 -*-
import unittest
from datetime import datetime

from google.appengine.ext import testbed
from google.appengine.ext import ndb

import baseTest
import db_functions
import models
from fixtures import appointmentFixtures, chatFixtures, groupFixtures

class HuddleTestCase(baseTest.GenericTestCase):
    def testCreateGroup(self):
        groupKey = db_functions.createGroup(groupFixtures[0])
        self.assertTrue(isinstance(groupKey, ndb.Key))

    def testCreateAppointment(self):
        appointmentKey = db_functions.createGroupAppointment(appointmentFixtures[0])
        self.assertTrue(isinstance(appointmentKey, ndb.Key))

    def testPostChatMessage(self):
        messageKey = db_functions.postChatMessage(chatFixtures[0])
        self.assertTrue(isinstance(messageKey, ndb.Key))
