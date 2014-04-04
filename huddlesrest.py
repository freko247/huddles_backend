# -*- coding: utf-8 -*-

import os
import cgi

import jinja2
import webapp2


# class Rest(webapp2.RequestHandler):

#     '''
#     classdocs
#     '''

#     def post(self):
# pop off the script name ('/api')
#         self.request.path_info_pop()
# Load the JSON values that were sent to the server
#         dictionary = json.loads(self.request.body)
# Clever way to initialize the Data object without specifying each
# field
#         newObject = globals()[self.request.path_info[1:]](**dictionary)
# Returns the ID that was created
#         self.response.write(str(newObject.put().id()))

#     def get(self):
# pop off the script name ('/api')
#         self.request.path_info_pop()
# forget about the leading '/' and seperate the Data type and the ID
#         split = self.request.path_info[1:].split(':')
# If no ID, then we will return all objects of this type
#         if len(split) == 1:
#             everyItem = []
# Finds the class that was specified from our list of global objects
# and create a Query for all of these objects. Then iterate through
# and collect the IDs
#             for item in globals()[split[0]].all(keys_only=True):
#             everyItem.append(item.id())
# Write JSON back to the client
#             self.response.write(json.dumps(everyItem))
#         else:
# Convert the ID to an int, create a key and retrieve the object
#             retrievedEntity = db.get(db.Key.from_path(split[0], int(split[1])))
# Return the values in the entity dictionary
#             self.response.write(json.dumps(retrievedEntity._entity))

#     def delete(self):
# pop off the script name
#         self.request.path_info_pop()
# forget about the leading '/'
#         split = self.request.path_info[1:].split(':')
#         db.delete(db.Key.from_path(split[0], int(split[1])))


class MainPage(webapp2.RequestHandler):

    def get(self):
        # TODO: Rename test page and also delete entitie after creation
        import db_functions
        import fixtures
        userKey = db_functions.addUser(fixtures.userFixtures[0])
        userRating = db_functions.addRating(fixtures.ratingFixtures[0])
        groupKey = db_functions.createGroup(fixtures.groupFixtures[0])
        appointmentKey = db_functions.createGroupAppointment(
            fixtures.appointmentFixtures[0])
        huddleKey = db_functions.createHuddle(fixtures.huddleFixtures[0])
        self.response.write(
            '<html><body>This is the Huddles rest server</body></html>')


application = webapp2.WSGIApplication([
    ('/', MainPage),
    # ('/api.*', Rest),
], debug=True)
