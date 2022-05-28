class Question():
    def __init__(self, title: str, text: str, image: str, position: int):
        self.title = title
        self.text = text
        self.image = image
        self.position = position
        self.answers = []

    def serialize(self):
        return {
            'title': self.title,
            'text': self.text,
            'image': self.image,
            'position': self.position,
            'answers': [answer.serialize() for answer in self.answers]
        }

    @staticmethod
    def unserialize(json):
        question = Question(
            json['title'], json['text'], json['image'], json['position'])
        answers = []
        for answer in json["possibleAnswers"]:
            answers.append(Answer.unserialize(answer))
        question.answers = answers
        return question


class Answer():
    def __init__(self, text: str, is_correct: bool):
        self.text = text
        self.is_correct = is_correct

    def serialize(self):
        return {
            'text': self.text,
            'isCorrect': self.is_correct
        }

    @staticmethod
    def unserialize(json):
        answer = Answer(json['text'], json['isCorrect'])
        return answer


class Participation():
    def __init__(self, player_name: str):
        self.player_name = player_name

    def serialize(self):
        return {
            'playerName': self.player_name
        }

    @staticmethod
    def unserialize(json):
        participation = Participation(json['playerName'])
        return participation
