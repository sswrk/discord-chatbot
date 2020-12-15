import random

random.seed()

answers = ["Jestem wesołym botem!",
           "Jestem botem Discordowym, miło mi :)",
           "Jestem twoim przyjacielem!",
           "Botem stworzonym na zajęcia z Podstaw Sztucznej Inteligencji"]


def try_who_are_you(message):
    if (message.content.find("przedstaw się") != -1 or
            message.content.find("kim jesteś") != -1 or
            message.content.find("kto ty") != -1 or
            message.content.find("przedstaw sie") != -1 or
            message.content.find("kim jestes") != -1 or
            (message.content.find("z kim") != -1 and (
                    message.content.find("rozmawiam") != -1 or message.content.find("mam przyjemność") != -1))
    ):
        return answers[random.randrange(0, len(answers))]
    return ""
