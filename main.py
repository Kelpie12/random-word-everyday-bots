# getting the necessary imports for requesting data

import requests as req


# getting the new word from random word api
def get_new_word():
    res = req.get('https://random-word-api.herokuapp.com/word')

    word = res.json()[0]

    return word


# will return a list of meanings
def get_word_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    res = req.get(url)
    out = []
    if res:
        if len(res.json()[0]['meanings']) > 0:
            for i in res.json()[0]['meanings']:
                obj = {
                    i['partOfSpeech']: i['definitions'][0]['definition']
                }
                out.append(obj)

    if out:
        return out
    else:
        return False


if __name__ == "__main__":
    new_word = get_new_word()
    data = get_word_definition(new_word)

    while not data:
        new_word = get_new_word()
        data = get_word_definition(new_word)

    print(new_word)
    print(data)
