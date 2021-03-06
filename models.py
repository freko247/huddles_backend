# -*- coding: utf-8 -*-
from google.appengine.ext import ndb


# USER ---------------------------------------------------
class User(ndb.Model):
    userName = ndb.StringProperty(indexed=False, required=True)
    userEmail = ndb.StringProperty(indexed=True, required=True)
    userPassword = ndb.StringProperty(indexed=True, required=True)
    userSkill = ndb.StringProperty(indexed=False, repeated=True)
    userFriend = ndb.StringProperty(indexed=False, repeated=True)
    userAvatarKey = ndb.BlobKeyProperty(indexed=False)


class Rating(ndb.Model):
    ratingUser = ndb.StringProperty(indexed=False)
    ratingValue = ndb.IntegerProperty(indexed=False)


# HUDDLE ---------------------------------------------------
class Huddle(ndb.Model):
    huddleDateAndTime = ndb.DateTimeProperty(indexed=True, required=True)
    huddleLocation = ndb.GeoPtProperty(indexed=False, required=True)
    huddleAdmin = ndb.StringProperty(indexed=False, required=True)
    huddleName = ndb.StringProperty(indexed=True, required=True)
    huddleTag = ndb.StringProperty(indexed=True, repeated=True)
    huddleUser = ndb.StringProperty(indexed=False, repeated=True)
    huddleGeoDocId = ndb.StringProperty(indexed=True)


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
