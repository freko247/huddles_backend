# -*- coding: utf-8 -*-
import datetime
import logging
from google.appengine.ext import blobstore, ndb

import models

logging.getLogger().setLevel(logging.DEBUG)


def addUser(userData):
    user = models.User(key=ndb.Key('User', userData['userEmail']))
    user.populate(userEmail=userData['userEmail'],
                  userName=userData['userName'],
                  userPassword=userData['userPassword'],
                  )
    if userData.get('userAvatar'):
        from google.appengine.api import files
        decoded = userData.get('userAvatar').decode('base64')
        # Create the file
        file_name = files.blobstore.create(
            mime_type='image/png',
            _blobinfo_uploaded_filename=userData['userEmail'])
        # Open the file and write to it
        with files.open(file_name, 'a') as f:
            f.write(decoded)
        # Finalize the file. Do this before attempting to read it.
        files.finalize(file_name)
        key = files.blobstore.get_blob_key(file_name)
        user.userAvatarKey = key
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
        huddleTag = [tag for tag in huddleData.get('huddleTag') if len(
            tag.rstrip()) > 0]
        huddle.huddleTag = huddleTag
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
    qr1 = models.Huddle.query(
        models.Huddle.huddleName == huddleData['huddleName'])
    logging.debug('type: %s, name: %s' %
                  (type(huddleData['huddleName']), huddleData['huddleName']))
    for huddle in qr1:
        if huddle.huddleName == huddleData['huddleName']:
            return huddle.huddleTag


def joinHuddle(huddleData):
    qr1 = models.Huddle.query(
        models.Huddle.huddleName == huddleData['huddleName'])
    logging.debug('type: %s, name: %s' %
                  (type(huddleData['huddleName']), huddleData['huddleName']))
    for huddle in qr1:
        logging.debug(
            "Adding user: %s, to huddle: %s" % (
                huddleData['huddleUser'], huddle.huddleName))
        if not isinstance(huddleData['huddleUser'], list):
            huddleData['huddleUser'] = [huddleData['huddleUser']]
        for user in huddleData['huddleUser']:
            if user not in huddle.huddleUser:
                huddle.huddleUser += huddleData['huddleUser']
        huddle.put()
        return huddle.huddleUser


def getHuddleUsers(huddleData):
    qr1 = models.Huddle.query(
        models.Huddle.huddleName == huddleData['huddleName'])
    for huddle in qr1:
        logging.debug("Huddle users are: %s" % huddle.huddleUser)
        return huddle.huddleUser


def authenticateUser(userData):
    qr1 = models.User.query(ndb.AND(
        models.User.userEmail == userData['userEmail'],
        models.User.userPassword == userData['userPassword'],
        ))
    for user in qr1:
        logging.debug("Authenticated user: %s" % user.userEmail)
        return user.userEmail


def getUserAvatar(userData):
    qr1 = models.User.query(models.User.userEmail == userData['userEmail'])
    for user in qr1:
        logging.debug("Getting avatar for user: %s" % user.userEmail)
        blob_reader = blobstore.BlobReader(user.userAvatarKey)
        value = blob_reader.read().encode('base64')
        return value
