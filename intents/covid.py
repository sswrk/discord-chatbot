import covid19cases as covid
import json


def try_covid(message):
    if (message.content.find("koronawirus") != -1 or
            message.content.find("coronavirus") != -1 or
            (message.content.find("koron") != -1 and message.content.find("wirus") != -1) or
            message.content.find("pandem") != -1 or
            message.content.find("epidem") != -1):
        cases = json.loads(covid.get_country_cases("Poland").__str__().replace('\'', '\"'))['NewCases']
        return f"Smuci mnie ten koronawirus, nowe przypadki w Polsce:\n{cases}"

    return ""
