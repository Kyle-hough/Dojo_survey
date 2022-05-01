from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        results = connectToMySQL("dojo_survey_db").query_db(query, data)
        if results:
            return cls(results[0])

    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        print(data)
        return connectToMySQL("dojo_survey_db").query_db(query, data)

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            flash("Name must have at least 3 characters.")
            is_valid = False
        if len(dojo['language']) < 1:
            flash("Language must be selected.")
            is_valid = False
        if len(dojo['location']) < 1:
            flash("Location must be selected.")
            is_valid = False
        if len(dojo['comment']) < 3:
            flash("Comments must be at least 3 characters.")
            is_valid = False
        return is_valid

