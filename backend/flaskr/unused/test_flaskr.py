import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category

class QuestionTestCase(unittest.TestCase):
    #This class represents the trivia test case

    def setUp(self):
        #Define test Vars and initialize
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "bookself_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {
            'question' : 'What color is the sky',
            'answer' : 'Mostly Blue',
            'category' : 'Trick Question',
            'difficulty' : "4"
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        #Executed after reach test
        pass


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()