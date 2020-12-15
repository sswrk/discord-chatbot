import random

random.seed()

answers = ["Do usłyszenia!",
           "Słyszymy się niedługo",
           "Pa, napisz znowu :)",
           "Miło było z Tobą rozmawiać, do zobaczenia!"]


def try_goodbye(message):
    if (message.content.find("pa") != -1 or
            message.content.find("na razie") != -1 or
            message.content.find("narazie") != -1 or
            message.content.find("nara") != -1 or
            message.content.find("żegnam") != -1 or
            message.content.find("do widzenia") != -1 or
            message.content.find("dobranoc") != -1 or
            message.content.find("do usłyszenia") != -1 or
            message.content.find("do zobaczenia") != -1
    ):
        return answers[random.randrange(0, len(answers))]
    return ""
