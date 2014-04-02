# -*- coding: utf-8 -*-
from google.appengine.ext import ndb

import models


def addUser(userData):
        user = models.User(key=ndb.Key('User', userData['userEmail']))
        user.populate(userEmail=userData['userEmail'],
                      userName=userData['userName'],
                      )
        if userData.get('userSkill'):
            user.userSkill = userData.get('userSkill')
        if userData.get('userTag'):
            user.userTag = userData.get('userTag')
        return user.put()


def addUserSkill(userData):
    user = ndb.Key('User', userData['userEmail']).get()
    for skill in userData['userSkill']:
        if skill not in user.userSkill:
            user.userSkill += userData['userSkill']
    return user.put()


def removeUserSkill(userData):
    user = ndb.Key('User', userData['userEmail']).get()
    for skill in userData['userSkill']:
        if skill in user.userSkill:
            user.userSkill.remove(skill)
    return user.put()


def addRating(ratingData):
        return models.Rating(key=ndb.Key(models.User,
                                         ratingData['userEmail'],
                                         models.Rating,
                                         ratingData['ratingUserEmail'],
                                         ),
                             ratingUser=ratingData['ratingUserEmail'],
                             ratingValue=ratingData['ratingValue']).put()


def addHuddle(huddleData):
    pass


def addGroup():
    pass


def addGroupAppointment():
    pass
