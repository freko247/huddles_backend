# -*- coding: utf-8 -*-
import json
import logging
import urllib
import webapp2

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
                     'createHuddle': db_functions.createHuddle,
                     'getSuggestedHuddles': db_functions.getSuggestedHuddles,
                     'getHuddleInfo': db_functions.getHuddleInfo,
                     }
        data = {}
        for argument in self.request.arguments():
            tmp = self.request.get_all(argument)
            if isinstance(tmp, list):
                tmp = [urllib.unquote_plus(value) for value in tmp]
            else:
                urllib.unquote_plus(tmp)
            logging.debug('Argument: %s, Value: %s' % (argument, tmp))
            if len(tmp) <= 1:
                tmp = tmp[0]
            data[argument] = tmp
        result = functions.get(data['db_function'])(data)
        self.response.out.write(json.dumps(result))


class MainPage(webapp2.RequestHandler):

    def get(self):
        # TODO: Rename test page and also delete entities after creation
        self.response.write(
            '<html><body>This is the Huddles rest server</body></html>')

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/api', Rest),
], debug=True)
