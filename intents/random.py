import random

def try_random(message):
    if (message.content.find("los") != -1 or
            message.content.find("gener") != -1 or
            (message.content.find("rzu") != -1 and message.content.find("kostk") != -1)):
        ints = sorted([int(s) for s in message.content.split() if s.isdigit()])
        min = 1
        max = 6
        if len(ints) == 2:
            min = ints[0]
            max = ints[1]


        generated_number = random.randint(min, max)

        return f"Wylosowałem dla ciebie liczbę! Jest nią {generated_number}"

    return ""


