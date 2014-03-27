# -*- coding: utf8 -*-

import models

def addUser(userData):
    user = models.User(ndb.Key("User"), userData.get('userId'))
    user.populate(
        userName = userData.get('userName'),
        userEmail = userData.get('userEmail'),
        userTag = userData.get('userTag'),
        userFriend = userData.get('userFriend'),
        )
    user.put()
