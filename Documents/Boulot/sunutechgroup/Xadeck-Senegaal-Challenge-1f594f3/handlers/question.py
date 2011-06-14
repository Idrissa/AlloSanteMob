from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from handlers.application import ApplicationHandler


class QuestionHandler(ApplicationHandler):

    def get(self):
        values = {}
        values.update(self.CommonValues())
        self.response.out.write(template.render("templates/questions.html", values))


    def post(self):
        self.redirect("/questions")

