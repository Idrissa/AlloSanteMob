# -*- coding: utf-8 -*-

import google.appengine.ext.db


class Category(db.Model):
   
   nom = db.StringProperty()
   created_at = db.DateTimeProperty(auto_now_add=True)


