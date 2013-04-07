"""Securely serves 1PasswordAnywhere files from App Engine.

Edit the application ID and both environment variables in app.yaml.
"""

import os
import zipfile

import webapp2

from google.appengine.api import users


class MainPage(webapp2.RequestHandler):
  """Defines a GET handler to verify user identity and serve archive files."""

  def get(self):
    user = users.get_current_user()
    if user.email() != os.environ['USER_EMAIL']:
      self.error(403)
      return
    else:
      f = zipfile.ZipFile(os.environ['AGILE_KEYCHAIN_ARCHIVE'])
      if self.request.path == '/':
        self.response.write(f.read('1Password.html'))
      else:
        self.response.write(f.read(self.request.path[1:]))
      f.close()

app = webapp2.WSGIApplication([('.*', MainPage)])
