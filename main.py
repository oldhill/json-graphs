"""Recommends SoundCloud artists based on who an input artist follows
"""

import os

import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True
)


class MainHandler(webapp2.RequestHandler):
  """ Index
  TODO: move this out of main file...
  """
  def get(self):
    template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    self.response.write(template.render())


app = webapp2.WSGIApplication([
  ('/', MainHandler),
], debug=True)