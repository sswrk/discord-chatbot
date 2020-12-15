import random

random.seed()

answers = ["W porządku",
           "Wszystko dobrze",
           "OK",
           "U mnie wszystko gra :)"]

def try_whats_up(message):
    if message.content.find("co") != -1 or message.content.find("jak") != -1:
        if message.content.find("tam") != -1 or message.content.find("się masz") != -1:
            return answers[random.randrange(0, len(answers))]
    return ""