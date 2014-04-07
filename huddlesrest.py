# -*- coding: utf-8 -*-

import os
import cgi

import jinja2
import webapp2

import db_functions

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

class Rest(webapp2.RequestHandler):

    def get(self):
        self.response.write(
            '<html><body>This is the Huddles rest server API page</body></html>')

    def post(self):
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        functions = {'addUser': db_functions.addUser}
        userData = {}
        for argument in self.request.arguments():
            userData[argument] = self.request.get(argument, allow_multiple=True),
        entityKey = functions.get(userData.pop('db_function'))(userData)


class MainPage(webapp2.RequestHandler):

    def get(self):
        # TODO: Rename test page and also delete entities after creation
        self.response.write(
            '<html><body>This is the Huddles rest server</body></html>')


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/api', Rest),
], debug=True)
