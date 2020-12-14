def send_google_link(message):
    query = message.content.replace(" ", "+")
    link = f"https://www.google.com/search?q={query}"

    reply = "Niestety nie wiem jak ci odpowiedzieć :(\n" \
            "Może chcesz to wygooglować?\n" \
            f"{link}"

    return reply