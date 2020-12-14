import random

random.seed()

answers = ["Korea Północna i Kuba to jedyne miejsca, w których nie można kupić Coca-Coli.",
           "8 Polaków otrzymało Nagrodę Nobla. Są to: Maria Skłodowska-Curie, Henryk Sienkiewicz, Władysław Reymont, Czesław Miłosz, Lech Wałęsa, Józef Rotblat, Wisława Szymborska oraz Olga Tokarczuk.",
           "Francja jest najczęściej odwiedzanym krajem na świecie.",
           "Zaskakujące jest, że Australia jest najbardziej otyłym krajem na świecie od 2012 r., a odsetek otyłości wynosi 26 procent.",
           "W kasynach hazardowych w Las Vegas nie ma zegarów.",
           "Honolulu to jedyne miejsce w Stanach Zjednoczonych, które posiada pałac królewski.",
           "Hiszpania jest uważana za najbardziej górzysty kraj w Europie, a ma ponad 8000 km plaż.",
           "Stany Zjednoczone nie posiadają języka urzędowego.",
           "Jedna trzecia wszystkich portów lotniczych na świecie znajduje się w Stanach Zjednoczonych.",
           "Mexico City tonie w tempie 10 cm rocznie, 10 razy szybciej niż Wenecja.",
           "Arabia Saudyjska jest jedynym krajem na świecie, w którym nie ma rzek.",
           "Mówi się, że Wielki Mur można zobaczyć z kosmosu, ale w rzeczywistości tak nie jest.",
           "Karaluch może żyć kilka tygodni bez głowy. W końcu umrze z głodu.",
           "Środkowy palec Galileusza jest przechowywany w Muzeum Nauki we Florencji.",
           "IPhone, książki o Harrym Potterze i Kostka Rubika to 3 najlepiej sprzedające się produkty w historii ludzkości.",
           "Obraz Mona Lisy przez kilka lat wisiał w sypialni Napoleona Bonaparte.",
           "Oprócz zmysłów, które wszyscy znamy, takich jak węch i dotyk, człowiek ma także inne zmysły: propriocepcja (świadomość pozycji części ciała)."]


def check_for_fun_fact(message):
    if (message.content.find("podasz") != -1 or message.content.find("zapodaj") != -1 or message.content.find(
            "podaj") != -1 or
            message.content.find("zapodaj") != -1 or message.content.find("chcę") != -1):
        if message.content.find("ciekaw") != -1:
            return answers[random.randrange(0, len(answers))]
    return ""
