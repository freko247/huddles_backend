# -*- coding: utf-8 -*-
import webapp2
import json

import db_functions


class Rest(webapp2.RequestHandler):

    def get(self):
        self.response.write('<html><body>'
                            'This is the Huddles rest server API page'
                            '</body></html>')

    def post(self):
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Content-Type'] = 'application/json'
        functions = {'addUser': db_functions.addUser,
                     'createHuddle': db_functions.createHuddle}
        userData = {}
        for argument in self.request.arguments():
            tmp = self.request.get_all(argument)
            if len(tmp) <= 1:
                tmp = tmp[0]
            userData[argument] = tmp
        functions.get(userData['db_function'])(userData)
        self.response.out.write(json.dumps('success'))


class MainPage(webapp2.RequestHandler):

    def get(self):
        # TODO: Rename test page and also delete entities after creation
        self.response.write(
            '<html><body>This is the Huddles rest server</body></html>')


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/api', Rest),
], debug=True)
