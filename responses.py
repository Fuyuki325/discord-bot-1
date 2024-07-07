from random import choice, randint
from discord import Intents, Client, Message

def get_response(user_input: str, message: Message) -> str:
    lowered: str = user_input.lower()
    username = str(message.author)

    if lowered == '':
        return 'Well, you\'re awfully silent...'

    if username == 'linlinhere':
        return f'lin. You are such a naughty boy. stop watching that.'

    if username == 'bra.na.don':
        switch = randint(1,6)
        if switch == 1:
            return "Get off Valorant and do something productive in your life. Brainrot"
        elif switch == 2:
            return "It's drone phase. Not TikTok phase"
        elif switch == 3:
            return "Sticking out " + username + "'s gyatt for the rizzler!"
        elif switch == 4:
            return "Please keep the hentai out of the chat"
        elif switch == 5:
            return "I KNOW you didn't shower! Take a bath. my god"
        elif switch == 6:
            return "So we getting married when?"

    if username == 'justinhoffner':
        switch = randint(1,6)
        if switch == 1:
            return "Beating up kids in a video game is not a flex Justin"
        elif switch == 2:
            return "Lowkey Justin got that gyatt. I've seen it"
        elif switch == 3:
            return "Sticking out " + username + "'s gyatt for the rizzler!"
        elif switch == 4:
            return "Justin gimme doordash"
        elif switch == 5:
            return "Meow! meow meow"
        elif switch == 6:
            return "Justin Minecraft super Minecraft"

    if username == 'jasonayuen':
        switch = randint(1,6)
        if switch == 1:
            return "Jason girlfriend when?"
        elif switch == 2:
            return "Jason speaking facts rn. on god"
        elif switch == 3:
            return "Sticking out " + username + "'s gyatt for the rizzler!"
        elif switch == 4:
            return "Love you my peekaboo Jason"
        elif switch == 5:
            return "I would pay $10 a month to see them feet"
        elif switch == 6:
            return "Jason wants to play Valorant rn."

    if username == 'ahleckx':
        switch = randint(1,6)
        if switch == 1:
            return "Famous youtuber alert!! Subscribe to alecksxd on YouTube"
        elif switch == 2:
            return "Daily Vlogs is back boys"
        elif switch == 3:
            return "Sticking out " + username + "'s gyatt for the rizzler!"
        elif switch == 4:
            return "Love you my peekaboo Alex"
        elif switch == 5:
            return "Alex wants to play Minecraft rn. I can feel it."
        elif switch == 6:
            return "Alex JUST CALLED YOU A BITCH!"

    if username == 'natepin':
        switch = randint(1,6)
        if switch == 1:
            return "NATHAN NATHAN NATHAN NATHAN"
        elif switch == 2:
            return "Nathan is my superhero"
        elif switch == 3:
            return "Sticking out " + username + "'s gyatt for the rizzler!"
        elif switch == 4:
            return "Love you my peekaboo Nathan"
        elif switch == 5:
            return "Nathan def tryna get on League rn. on god."
        elif switch == 6:
            return "Shut up and make me a sandwich"

    else:
        return choice(['Jason better stop yapping',
                       'Love you Brandon',
                       'My peekaboo Jushin',
                       'Skibidi Toilet',
                       'Is Jason the goat?',
                       'Brandon likes feet',
                       'Get your money up. not your funny up',
                       'So we\'re in copper?',
                       'fucking Justin man',
                       'fucking alex bro',
                       'fuck you',
                       'at least i didn\'t get rejected at prom'
                       'bro hit the green val rank and now he thinks he\'s the goat'])