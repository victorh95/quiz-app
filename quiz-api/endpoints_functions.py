import jwt_utils

from db_class import Database
from models import Question, Answer


def verify_token(request):
    if request.headers.get('Authorization') is None:
        return False
    token_payload_sub = jwt_utils.decode_token(
        request.headers.get('Authorization').replace("Bearer ", ""))
    if(token_payload_sub == "quiz-app-admin"):
        return True
    else:
        return False


def add_question(new_question):
    db = Database()
    db.connection()
    question = Question.unserialize(new_question)
    db.exec_query(
        "update Question set position=position+1 where position>=" + str(question.position))
    db.save_question(question)
    db.disconnection()


def delete_question(position):
    db = Database()
    db.connection()
    db.exec_query("delete from Question where position=" + position)
    db.exec_query(
        "update Question set position=position-1 where position>=" + position)
    db.disconnection()


def get_question(position):
    db = Database()
    db.connection()
    question = db.select_query(
        "select * from Question where position=" + position)[0]
    answers = db.select_query(
        "select * from Answer where idQuestion=" + str(question['id']))
    question["possibleAnswers"] = answers
    for possibleAnswer in question["possibleAnswers"]:
        possibleAnswer["isCorrect"] = bool(possibleAnswer["isCorrect"])
    db.disconnection()
    return question


def update_question(position, modified_question):
    db = Database()
    db.connection()
    question = Question.unserialize(modified_question)
    # modify the position of other questions if the position of the question is updated
    if int(position) != question.position:
        if int(position) > question.position:
            db.exec_query(
                "update Question set position=position+1 where position<" + position)
        else:
            db.exec_query(
                "update Question set position=position-1 where position>" + position)
    # update question
    id_question = str(db.select_query(
        "select id from Question where position=" + position)[0]['id'])
    question_params = (question.title, question.text,
                       question.image, str(question.position))
    db.exec_query("update Question set title=?, text=?, image=?, position=? where id=" +
                  id_question, question_params)
    # update answers (delete then insert -> more simple )
    db.exec_query("delete from Answer where idQuestion=" + id_question)
    for answer in question.answers:
        answer_params = (answer.text, answer.is_correct, id_question)
        db.exec_query(
            "insert into Answer (text, isCorrect, idQuestion) values (?, ?, ?)", answer_params)
    db.disconnection()


def verify_position(position):
    db = Database()
    db.connection()
    result = db.select_query(
        "select * from Question where position=" + position)
    db.disconnection()

    if(len(result) <= 0):
        return False
    return True


def add_participations(playload):
    db = Database()
    db.connection()
    player_name = playload["playerName"]
    answers = playload["answers"]
    questions = db.select_query("select * from Question order by position")
    if len(answers) != len(questions):
        raise IndexError
    # find postion of good answers
    position_good_answers = []
    for question in questions:
        question_answers = db.select_query(
            "select * from Answer where idQuestion=" + str(question["id"]))
        for i, answer in enumerate(question_answers):
            if(answer["isCorrect"] == 1):
                position_good_answers.append(i+1)
                break
    # count good answers
    score = 0
    for i in range(len(answers)):
        if answers[i] == position_good_answers[i]:
            score = score + 1
    # save participation
    participation_params = (player_name, score)
    db.exec_query(
        "insert into Participation (playerName, score) values (?, ?)", participation_params)
    db.disconnection()
    return player_name, score


def delete_participations():
    db = Database()
    db.connection()
    db.exec_query("delete from Participation")
    db.disconnection()


def get_quiz_infos():
    db = Database()
    db.connection()
    size = db.select_query("select count(*) as size from Question")[0]["size"]
    scores = db.select_query("select * from Participation order by score desc")
    db.disconnection()
    return size, scores
