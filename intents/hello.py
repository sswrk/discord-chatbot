import random

random.seed()

answers = ["Cześć, cześć :)",
           "Witam!",
           "Dzień dobrek",
           "Hejka!"]


def try_hello(message):
    if (message.content.find("siema") != -1 or
            message.content.find("siemka") != -1 or
            message.content.find("cześć") != -1 or
            message.content.find("witam") != -1 or
            message.content.find("dzień dobry") != -1 or
            message.content.find("hej") != -1 or
            message.content.find("hejka") != -1 or
            message.content.find("dzień dobry") != -1 or
            message.content.find("dobry wieczór") != -1 or
            message.content.find("hejo") != -1 or
            message.content.find("siemaneczko") != -1 or
            message.content.find("serwus") != -1
    ):
        return answers[random.randrange(0, len(answers))]
    return ""
