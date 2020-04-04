text = input('Input your text:')


def acro(text):
    new_text = text[0]
    for i in range(len(text)):
        if text[i - 1] == ' ':
            new_text += text[i]
    return new_text.upper()


print(acro(text))
