import random

random.seed()

answers = ["Proszę bardzo",
           "Proszę :)",
           "Nie ma sprawy",
           "Luzik",
           "Spoko :)"]


def try_thanks(message):
    if (message.content.find("dzięki") != -1 or
            message.content.find("thank") != -1 or
            message.content.find("thx") != -1 or
            message.content.find("dziękuję") != -1 or
            message.content.find("dziena") != -1
    ):
        return answers[random.randrange(0, len(answers))]
    return ""
