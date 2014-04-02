# -*- coding:utf8 -*-
import unittest
from datetime import datetime

from google.appengine.ext import testbed
from google.appengine.ext import ndb

import baseTest
import db_functions
import models

groupFixtures = [{'huddleName': 'Mobile Prototyping',
                  'groupName': 'Group 1',
                  'groupUser': ['user@mail.com', 'tester@mail.com'],
                  'groupAdmin': 'user@mail.com',
                  },
                 ]

appointmentFixtures = [{'huddleName': groupFixtures[0]['huddleName'],
                        'groupName': groupFixtures[0]['groupName'],
                        'appointmentName': 'Hangout',
                        'appointmentTime': datetime(2014,4,9,9,0,0),
                        },
                       ]

chatFixtures = [{'huddleName': groupFixtures[0]['huddleName'],
                 'groupName': groupFixtures[0]['groupName'],
                 'timestamp': datetime(2014,4,1,13,0,0),
                 'text':'Hi!',
                 'author': 'user@mail.com',
                 },
                {'huddleName': groupFixtures[0]['huddleName'],
                 'groupName': groupFixtures[0]['groupName'],
                 'timestamp': datetime(2014,4,1,13,0,10),
                 'text':'Hello!',
                 'author': 'tester@mail.com',
                 },
                {'huddleName': groupFixtures[0]['huddleName'],
                 'groupName': groupFixtures[0]['groupName'],
                 'timestamp': datetime(2014,4,1,13,0,15),
                 'text':'Whats up?',
                 'author': 'user@mail.com',
                 },
                {'huddleName': groupFixtures[0]['huddleName'],
                 'groupName': groupFixtures[0]['groupName'],
                 'timestamp': datetime(2014,4,1,13,0,25),
                 'text':'Nothing special',
                 'author': 'tester@mail.com',
                 },
                {'huddleName': groupFixtures[0]['huddleName'],
                 'groupName': groupFixtures[0]['groupName'],
                 'timestamp': datetime(2014,4,1,13,0,30),
                 'text':'Ok, I was just wondering when we can meet next time.',
                 'author': 'user@mail.com',
                 },
                {'huddleName': groupFixtures[0]['huddleName'],
                 'groupName': groupFixtures[0]['groupName'],
                 'timestamp': datetime(2014,4,1,13,0,35),
                 'text':'Maybe Monday evening?',
                 'author': 'tester@mail.com',
                 },
                {'huddleName': groupFixtures[0]['huddleName'],
                 'groupName': groupFixtures[0]['groupName'],
                 'timestamp': datetime(2014,4,1,13,0,40),
                 'text':'Monday is not good for me, what about Thuesday at 9am?',
                 'author': 'user@mail.com',
                 },
                {'huddleName': groupFixtures[0]['huddleName'],
                 'groupName': groupFixtures[0]['groupName'],
                 'timestamp': datetime(2014,4,1,13,0,45),
                 'text':'Thuesday sounds good, see you then',
                 'author': 'tester@mail.com',
                 },
                {'huddleName': groupFixtures[0]['huddleName'],
                 'groupName': groupFixtures[0]['groupName'],
                 'timestamp': datetime(2014,4,1,13,0,50),
                 'text':'Cool, see you.',
                 'author': 'user@mail.com',
                 },
                ]

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
