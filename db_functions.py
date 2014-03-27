# -*- coding: utf8 -*-
from google.appengine.ext import ndb

import models

def addUser(userData):
    user = models.User(key=ndb.Key("User", userData.get('userName')))
    user.populate(
        userName = userData.get('userName'),
        userEmail = userData.get('userEmail'),
        )
    if userData.get('userTag'):
        user.userTag = userData.get('userTag')
    if userData.get('userFriend'):
        user.userFriend = userData.get('userFriend')
    return user.put()
