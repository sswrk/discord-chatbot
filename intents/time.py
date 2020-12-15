from datetime import datetime


def try_time(message):
    if message.content.find("która") != -1 or message.content.find("jak") != -1:
        if message.content.find("godzina") != -1:
            return "Jest " + str(datetime.now())[:-6][11:]
    return ""
