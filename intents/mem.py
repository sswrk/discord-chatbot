import json
import urllib

import requests
import random

random.seed()

meme_paths = ["resources/memes/1.png",
              "resources/memes/2.png",
              "resources/memes/3.png",
              "resources/memes/4.png",
              "resources/memes/5.png"]


def check_for_meme(message):
    if message.content.find("mem") != -1:
        return meme_paths[random.randrange(0, len(meme_paths))]
    return ""
