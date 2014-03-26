# -*- coding: utf-8 -*-

import os
import cgi

import jinja2
import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        user = User()
        user.userId = "John Doe"
        k = user.put()
        userTag = UserTags(parent=k)
        userTag.tag = "Python"
        userTag.put()
        self.response.write('<html><body>This is the Huddles rest server</body></html>')


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
