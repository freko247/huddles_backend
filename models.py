# -*- coding: utf-8 -*-

from google.appengine.ext import ndb


# Property (field) types
# IntegerProperty     64-bit signed integer
# FloatProperty       Double-precision floating-point number
# BooleanProperty     Boolean
# StringProperty      Unicode string; up to 500 characters, indexed
# TextProperty        Unicode string; unlimited length, not indexed
# BlobProperty        Uninterpreted byte string: if you set indexed=True, up to 500 characters, indexed; if indexed is False (the default), unlimited length, not indexed. Optional keyword argument: compressed.
# DateTimeProperty    Date and time (see Date and Time Properties)
# DateProperty    Date (see Date and Time Properties)
# TimeProperty    Time (see Date and Time Properties)
# GeoPtProperty   Geographical location. This is a ndb.GeoPt object. The object has attributes lat and lon, both floats. You can construct one with two floats like ndb.GeoPt(52.37, 4.88) or with a string ndb.GeoPt("52.37, 4.88"). (This is actually the same class as db.GeoPt)
# KeyProperty     Datastore key Optional keyword argument: kind=kind, to require that keys assigned to this property always have the indicated kind. May be a string or a Model subclass.
# BlobKeyProperty     Blobstore key Corresponds to BlobReferenceProperty in the old db API, but the property value is a BlobKey instead of a BlobInfo; you can construct a BlobInfo from it using BlobInfo(blobkey)
# UserProperty        User object.
# StructuredProperty  Includes one kind of model inside another, by value (see Structured Properties)
# LocalStructuredProperty     Like StructuredProperty, but on-disk representation is an opaque blob and is not indexed (see Structured Properties). Optional keyword argument: compressed.
# JsonProperty    Value is a Python object (such as a list or a dict or a string) that is serializable using Python's json module; the Datastore stores the JSON serialization as a blob. Unindexed by default. Optional keyword argument: compressed.
# PickleProperty  Value is a Python object (such as a list or a dict or a string) that is serializable using Python's pickle protocol; the Datastore stores the pickle serialization as a blob. Unindexed by default. Optional keyword argument: compressed.
# GenericProperty     Generic value Used mostly by the Expando class, but also usable explicitly. Its type may be any of int, long, float, bool, str, unicode, datetime, Key, BlobKey, GeoPt, User, None.
# ComputedProperty    Value computed from other properties by a user-defined function. (See Computed Properties.)

# Property options
# indexed     bool        Usually True        Include property in Datastore's indexes; if False, values cannot be queried but writes are faster. Not all property types support indexing; setting indexed to True fails for these. Unindexed properties cost fewer write ops than indexed properties.
# repeated        bool        False       Property value is a Python list containing values of the underlying type (see Repeated Properties).
# required        bool        False       Property must have a value specified. Cannot be combined with repeated=True but can be combined with default=True.
# default     Property's underlying type  None    Default value of property if none explicitly specified. Cannot be combined with repeated=True but can be combined with required=True.
# choices     List of values of underlying type   None        Optional list of allowable values.
# validator       Function    None        Optional function to validate and possibly coerce the value. Will be called with arguments (prop, value) and should either return the (possibly coerced) value or raise an exception. Calling the function again on a coerced value should not modify the value further. (For example, returning value.strip() or value.lower() is fine, but not value + '$'.) May also return None, which means "no change". See also Writing Property Subclasses
# verbose_name    string  None    Optional HTML label to use in web form frameworks like jinja2.


#USER ---------------------------------------------------
class User(ndb.Model):
    userName = ndb.StringProperty(indexed=False)
    userEmail = ndb.StringProperty(indexed=False)
    userTag = ndb.StringProperty(indexed=False, repeated=True)
    userFriend = ndb.StringProperty(indexed=False, repeated=True)

class Rating(ndb.Model):
    ratingUser = ndb.StringProperty(indexed=False)
    ratingValue = ndb.IntegerProperty(indexed=False)


#HUDDLE ---------------------------------------------------
class Huddle(ndb.Model):
    huddleDateAndTime = ndb.DateTimeProperty(indexed=False)
    huddleLocation = ndb.GeoPtProperty(indexed=False)
    huddleAdmin = ndb.StringProperty(indexed=False)
    huddleTags = ndb.StringProperty(indexed=False, repeated=True)
    huddleUser = ndb.StringProperty(indexed=False, repeated=True)


#GROUP ---------------------------------------------------
class Group(ndb.Model):
    groupHuddleId = ndb.StringProperty(indexed=False)
    groupUser =     userGroup = ndb.StringProperty(indexed=False, repeated=True)
    groupAdmin = ndb.StringProperty(indexed=False)

class GroupAppointment(ndb.Model):
    appointmentName = ndb.StringProperty(indexed=False)
    appointmentTime = ndb.DateTimeProperty(indexed=False)


class GroupChat(ndb.Model):
    timestamp = ndb.TimeProperty(indexed=False)
    text = ndb.TextProperty(indexed=False)
