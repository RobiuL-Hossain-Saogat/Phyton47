def emojiConverter(minput):
    words=minput.split(' ')
    emojis={
        ":)":"😊",
        ":(":"😒",
        "a":"Apple",
        ":":"😑"
    }

    output=""
    for word in words:
        output+=emojis.get(word)
    return output

msgEmoji=input(">")
print(emojiConverter(msgEmoji))