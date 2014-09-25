import webapp2
import os
from google.appengine.ext.webapp import template

class Redirect(webapp2.RequestHandler):
	def get(self):
		return webapp2.redirect('/')

class Main(webapp2.RequestHandler):
    def get(self):
		template_values = {
            'url':'a',
            'url_linktext': 'b',
        }
		self.response.out.write(template.render('index.html', template_values))

application = webapp2.WSGIApplication([
	('/', Main),
    ('/.*', Redirect)
], debug=True)
