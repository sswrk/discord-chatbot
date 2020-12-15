import random

random.seed()

answers = ["Świetny kawałek",
           "Kocham muzykę!",
           "Super piosenka",
           "Polecam ten utwór :)"]

youtube_links = ["https://youtu.be/aGSKrC7dGcY",
                 "https://www.youtube.com/watch?v=Vg1jyL3cr60",
                 "https://youtu.be/UmFFTkjs-O0",
                 "https://youtu.be/9EKi2E9dVY8",
                 "https://youtu.be/8UK3c60wN2Q",
                 "https://youtu.be/T1NW57lk5fY",
                 "https://youtu.be/y-JqH1M4Ya8",
                 "https://youtu.be/u5CVsCnxyXg"]


def try_music(message):
    if (message.content.find("słucha") != -1 or message.content.find("puść") != -1 or message.content.find(
            "włącz") != -1
            or message.content.find("wyślij") != -1 or message.content.find("zapodaj") != -1):

        if (message.content.find("muzy") != -1 or message.content.find("piosenk") != -1 or message.content.find(
                "coś") != -1 or message.content.find("czegoś") != -1 or message.content.find("kawał") != -1
                or message.content.find("cokolwiek") != -1):
            reply = f"{answers[random.randrange(0, len(answers))]}\n" \
                    f"{youtube_links[random.randrange(0, len(youtube_links))]}"
            return reply

    return ""
