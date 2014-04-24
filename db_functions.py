# -*- coding: utf-8 -*-
import datetime
from google.appengine.ext import ndb

import models


def addUser(userData):
    user = models.User(key=ndb.Key('User', userData['userEmail']))
    user.populate(userEmail=userData['userEmail'],
                  userName=userData['userName'],
                  userPassword=userData['userPassword'],
                  )
    if userData.get('userSkill'):
        user.userSkill = userData.get('userSkill')
    if userData.get('userTag'):
        user.userTag = userData.get('userTag')
    user.put()
    return user.userEmail


def addUserSkill(userData):
    user = ndb.Key('User', userData['userEmail']).get()
    for skill in userData['userSkill']:
        if skill not in user.userSkill:
            user.userSkill += userData['userSkill']
    user.put()
    return user.userSkill


def removeUserSkill(userData):
    user = ndb.Key('User', userData['userEmail']).get()
    for skill in userData['userSkill']:
        if skill in user.userSkill:
            user.userSkill.remove(skill)
    user.put()
    return user.userSkill


def addRating(ratingData):
    rating = models.Rating(key=ndb.Key(models.User,
                                       ratingData['userEmail'],
                                       models.Rating,
                                       ratingData['ratingUserEmail'],
                                       ),
                           ratingUser=ratingData['ratingUserEmail'],
                           ratingValue=ratingData['ratingValue'])
    rating.put()
    return rating.ratingUser


def createHuddle(huddleData):
    huddle = models.Huddle(key=ndb.Key('Huddle', huddleData['huddleName']))
    huddleDateAndTime = datetime.datetime.utcfromtimestamp(
        int(huddleData['huddleDateAndTime'][:-3]))
    huddleLocation = ndb.GeoPt(','.join(huddleData['huddleLocation']))
    huddle.populate(huddleDateAndTime=huddleDateAndTime,
                    huddleLocation=huddleLocation,
                    huddleName=huddleData['huddleName'],
                    huddleAdmin=huddleData['huddleAdmin'],
                    )
    if huddleData.get('huddleTag'):
        huddle.huddleTag = huddleData.get('huddleTag')
    if huddleData.get('huddleUser'):
        huddle.huddleUser = huddleData.get('huddleUser')
    huddle.put()
    return huddle.huddleName


def createGroup(groupData):
    group = models.Group(key=ndb.Key('Huddle',
                                     groupData['huddleName'],
                                     'Group',
                                     groupData['groupName']
                                     )
                         )
    group.populate(groupName=groupData['groupName'],
                   groupAdmin=groupData['groupAdmin'],
                   )
    if groupData.get('groupUser'):
        group.groupData = groupData.get('groupUser')
    if groupData.get('groupUser'):
        group.groupData = groupData.get('groupUser')
    group.put()
    return group.groupAdmin


def createGroupAppointment(appointmentData):
    # TODO: Check that appointment is in the future.
    appointment = models.GroupAppointment(key=ndb.Key('Huddle',
                                                      appointmentData[
                                                      'huddleName'],
                                                      'Group',
                                                      appointmentData[
                                                      'groupName'],
                                                      'GroupAppointment',
                                                      appointmentData[
                                                      'appointmentName']
                                                      )
                                          )
    appointment.populate(appointmentName=appointmentData['appointmentName'],
                         appointmentTime=appointmentData['appointmentTime'],
                         )
    appointment.put()
    return appointment.appointmentName


def postChatMessage(messageData):
    message = models.GroupChat(key=ndb.Key('Huddle',
                                           messageData['huddleName'],
                                           'Group',
                                           messageData['groupName'],
                                           'GroupChat',
                                           messageData['timestamp'].isoformat()
                                           )
                               )
    message.populate(timestamp=messageData['timestamp'],
                     author=messageData['author'],
                     text=messageData['text'],
                     )
    message.put()
    return message.author


def getSuggestedHuddles(userData):
    qr1 = models.Huddle.query()
    huddles = []
    for huddle in qr1:
        huddles.append(huddle.huddleName)
    return huddles


def getHuddleInfo(huddleData):
    print 'searching for: ', huddleData['huddleName']
    qr1 = models.Huddle.query()
    for huddle in qr1:
        print huddle.huddleName, huddle.huddleTag
        if huddle.huddleName == huddleData['huddleName']:
            print 'its a match'
    return "success"
