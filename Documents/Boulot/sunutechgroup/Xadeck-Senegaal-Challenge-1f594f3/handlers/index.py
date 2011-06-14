# -*- coding: utf-8 -*-

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from handlers.application import ApplicationHandler


class IndexHandler(ApplicationHandler):
  def get(self):
    values = {}
    values.update(self.CommonValues())
    self.response.out.write(template.render("templates/index.html", values))
