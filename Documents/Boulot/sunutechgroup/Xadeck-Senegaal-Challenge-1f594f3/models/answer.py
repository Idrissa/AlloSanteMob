# -*- coding: utf-8 -*-

from google.appengine.ext import db
from models import User,Question
 

class Answer(db.Model):
  
  user=  db.Reference(User)
  question= db.Reference(Question)
  score=db.StringProperty()
