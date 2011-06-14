# -*- coding: utf-8 -*-

from google.appengine.ext import db


class User(db.Model):
  userid=db.UserProperty()
  timestamp=db.DateTimeProperty(auto_now_add=True)
  first_name=db.StringProperty()
  last_name=db.StringProperty()
  avatar=db.BlobProperty()
