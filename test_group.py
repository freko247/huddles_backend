# -*- coding:utf8 -*-
import baseTest
import db_functions
from fixtures import appointmentFixtures, chatFixtures, groupFixtures


class HuddleTestCase(baseTest.GenericTestCase):
    def testCreateGroup(self):
        groupAdmin = db_functions.createGroup(groupFixtures[0])
        self.assertEqual(groupFixtures[0]['groupAdmin'], groupAdmin)

    def testCreateAppointment(self):
        appointmentName = db_functions.createGroupAppointment(
            appointmentFixtures[0])
        self.assertEqual(
            appointmentFixtures[0]['appointmentName'], appointmentName)

    def testPostChatMessage(self):
        author = db_functions.postChatMessage(chatFixtures[0])
        self.assertEqual(chatFixtures[0]['author'], author)
