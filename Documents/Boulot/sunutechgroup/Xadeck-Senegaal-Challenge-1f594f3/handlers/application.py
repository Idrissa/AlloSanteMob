# -*- coding: utf-8 -*-

from google.appengine.ext import webapp
from google.appengine.dist import use_library
from google.appengine.api import users


class ApplicationHandler(webapp.RequestHandler):
    """Base class for all handlers.

    Add there methods/helpers that can be used by all handlers,
    such as greetings, logout messages, etc."""
    def CommonValues(self):
        values = {}
        values["tabs"] = [
            dict(text="Acceuil", url="/",rel=""),
            dict(text="Classements", url="/ranking",rel=""),
            dict(text="Questions", url="/questions",rel=""),
        ]
        if not users.get_current_user():
            values["tabs"].append(dict(text="Login",
                                       url=users.create_login_url("/"),rel="#overlay"))
        else:
            values["tabs"].append(dict(text="Mon profil",
                                       url="/profile"))
            values["tabs"].append(dict(text="Déconnecter",
                                       url=users.create_logout_url("/")))
        return values

