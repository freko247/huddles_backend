# -*- coding: utf-8 -*-

from google.appengine.ext import ndb


# USER ---------------------------------------------------
class User(ndb.Model):
    userName = ndb.StringProperty(indexed=False, required=True)
    userEmail = ndb.StringProperty(indexed=False, required=True)
    userSkill = ndb.StringProperty(indexed=False, repeated=True)
    userTag = ndb.StringProperty(indexed=False, repeated=True)
    userFriend = ndb.StringProperty(indexed=False, repeated=True)


class Rating(ndb.Model):
    ratingUser = ndb.StringProperty(indexed=False)
    ratingValue = ndb.IntegerProperty(indexed=False)


# HUDDLE ---------------------------------------------------
class Huddle(ndb.Model):
    huddleDateAndTime = ndb.DateTimeProperty(indexed=False, required=True)
    huddleLocation = ndb.GeoPtProperty(indexed=False, required=True)
    huddleAdmin = ndb.StringProperty(indexed=False, required=True)
    huddleName = ndb.StringProperty(indexed=False, required=True)
    huddleTag = ndb.StringProperty(indexed=False, repeated=True)
    huddleUser = ndb.StringProperty(indexed=False, repeated=True)


# GROUP ---------------------------------------------------
class Group(ndb.Model):
    groupName = ndb.StringProperty(indexed=False, required=True)
    groupUser = ndb.StringProperty(indexed=False, repeated=True)
    groupAdmin = ndb.StringProperty(indexed=False)


class GroupAppointment(ndb.Model):
    appointmentName = ndb.StringProperty(indexed=False, required=True)
    appointmentTime = ndb.DateTimeProperty(indexed=False, required=True)


class GroupChat(ndb.Model):
    timestamp = ndb.DateTimeProperty(indexed=False, required=True)
    text = ndb.TextProperty(indexed=False, required=True)
    author = ndb.TextProperty(indexed=False, required=True)
