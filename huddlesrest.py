import os
import cgi

import jinja2
import webapp2

from google.appengine.ext import ndb

class UserTable(ndb.Model):
    userId = ndb.StringProperty(indexed=False)


class MainPage(webapp2.RequestHandler):

    def get(self):
        user = UserTable()
        user.userId = "asdgd"
        user.put()
        self.response.write('<html><body>This is the Huddles rest server</body></html>')

application = webapp2.WSGIApplication([
    ('/', MainPage),

], debug=True)
