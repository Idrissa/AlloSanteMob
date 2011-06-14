# -*- coding: utf-8 -*-

# See http://code.google.com/appengine/docs/python/tools/libraries.html#Django
from google.appengine.dist import use_library
# use_library('django', '1.2')


from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from handlers.index import IndexHandler
from handlers.user import UserHandler
from handlers.question import QuestionHandler
from handlers.ranking import RankingHandler
from handlers.profile import ProfileHandler

handlers = [
  ("/", IndexHandler),
  ("/user", UserHandler),
  ("/questions", QuestionHandler),
  ("/ranking", RankingHandler),
  ("/profile", ProfileHandler),
]


application = webapp.WSGIApplication(handlers, debug = True)


def main():
  run_wsgi_app(application)


if __name__ == "__main__":
  main()

