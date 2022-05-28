import sqlite3

from models import Question, Answer


class Database:
    def __init__(self):
        self.cur = None
        self.db_connection = None

    def connection(self):
        db_connection = sqlite3.connect("../db.db")
        db_connection.isolation_level = None
        cur = db_connection.cursor()
        self.cur = cur
        self.db_connection = db_connection
    
    def disconnection(self):
        self.db_connection.close()

    def select_query(self, query):
        res = self.cur.execute(query)
        json_res = []
        for entry in res.fetchall():
            json_res.append(self.serialize_entry(entry))
        return json_res

    def serialize_entry(self, entry):
        serialized_entry = {}
        for i, description in enumerate(self.cur.description):
            serialized_entry[description[0]] = entry[i]
        return serialized_entry

    def exec_query(self, query, params=None):
        self.cur.execute("begin")
        if params:
            self.cur.execute(query, params)
        else:
            self.cur.execute(query)
        self.cur.execute("commit")

    def save_question(self, question: Question):
        # save question
        question_params = (question.title, question.text, question.image, str(question.position))
        self.exec_query("insert into Question (title, text, image, position) values (?, ?, ?, ?)", question_params)
        # save answers
        id_question = self.cur.lastrowid
        for answer in question.answers:
            answer_params = (answer.text, answer.is_correct, id_question)
            self.exec_query("insert into Answer (text, isCorrect, idQuestion) values (?, ?, ?)", answer_params)
