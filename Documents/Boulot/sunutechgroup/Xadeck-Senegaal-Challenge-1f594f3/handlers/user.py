# -*- coding: utf-8 -*-

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from handlers.application import ApplicationHandler
from models.user import User
import logging

class UserHandler(ApplicationHandler):
  def get(self):
    values = {}
    values.update(self.CommonValues())
    # Search for a user, and if none, create one
    userid = users.get_current_user()
    user = User.get_by_key_name(userid.nickname())
    if not user:
        user = User(key_name=userid.nickname())
        user.userid = userid
        user.put()
        logging.info("Created user %s", userid.nickname())
    values.update(user=user)
    self.response.out.write(template.render("templates/user.html", values))

  def post(self):
    userid = users.get_current_user()
    user = User.get_by_key_name(userid.nickname())
    if user:
      user.first_name = self.request.get("first_name")
      user.last_name = self.request.get("last_name")
      user.put()
      logging.info("Updated user %s", userid.nickname())
    # TODO(xdecoret) add notice when redirecting
    self.redirect("/user")

