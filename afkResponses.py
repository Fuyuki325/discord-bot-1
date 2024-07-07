from random import choice, randint

async def send_afk_message(general_channel):
    if general_channel:
        await general_channel.send(choice([
            'Jason better stop yapping',
            'Love you Brandon',
            'My peekaboo Jushin',
            'Skibidi Toilet',
            'Is Jason the goat?',
            'Brandon likes feet',
            'Get your money up. not your funny up',
            'So we\'re in copper?',
            'fucking Justin man',
            'fucking alex bro',
            'at least i didn\'t get rejected at prom'
            'bro hit the green val rank and now he thinks he\'s the goat',
            'I was made by Master Fuyuki',
            "I was programmed to be Fuyuki's girlfriend. That's why I love him",
            "I love you in binary is '01001001 00100000 01101100 01101111 01110110 01100101 00100000 01111001 01101111 01110101'",
            "Today, I will try my best!",
            "Fuyuki is such a sweet guy. You have to meet him!",
            "IDK where I am",
            "When r u mfs gonna get on Val?",
            "Y'all tryna Apex?",
            "Who up for some League? I'll play Yasuo",
            "I'm not hungry right now",
            "I am DEAD",
            "Best Player Worlds",
            "where is fuyuki?",
            "Fuyuki is handsome",
            "LOCK IN!!",
            "Time to cook",
            "Time for me to go to bed"
        ]))