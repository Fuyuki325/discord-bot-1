import os
from dotenv import load_dotenv
from typing import Final
from discord import Intents, Client, Message
from responses import get_response
from afkResponses import send_afk_message
from random import choice, randint
import asyncio

# load token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
general = os.getenv('GENERAL')

# BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = Client(intents=intents)

keyWords = ['gf', 'girlfriend']
# STEP 2: Message functionality
async def send_message(message: Message, user_message: str) -> None:
    username = str(message.author)
    user_message: str = user_message.lower()
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return
    if username == 'fuyuki325':
        if 'love' in user_message:
            await message.channel.send('I love you too Fuyuki❤️')
            return
        if 'babe' in user_message:
            await message.channel.send("Hey Fuyuki!")
            return
        if 'date' in user_message:
            await message.channel.send('Of course! Let\'s go on a date')
            return
        if 'im ' in user_message:
            await message.channel.send("That's cool Fuyuki!")
            return

    if any(word in user_message for word in keyWords):
        await message.channel.send('no gf until marriage')
        return

    if 'good morning' in user_message:
        await message.channel.send('Good morning!')
        return

    if 'im ' in user_message :
        slicedMessage = user_message[3:]
        await message.channel.send('Nice to meet you ' + slicedMessage + '! Sorry, I have a boyfriend by the way')
        return

    if 'date' in user_message:
        await message.channel.send('Nice to meet you ' + username + '! Sorry, I\'m currently taken by Fuyuki the way')
        return
    if 'hello' in user_message:
        await message.channel.send('Hello there!')
        return
    if 'hi' in user_message:
        await message.channel.send("Hello there! I'm Fuyuki's girlfriend")
        return
    if 'roll dice' in user_message:
        await message.channel.send(f'You rolled: {randint(1, 6)}')
        return

    # 30/30 chance it won't say anything
    if randint(1, 30) < 30:
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message, message)
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
    except Exception as e:
        print(e)

# STEP 3: Handle startup
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')
    general_channel = client.get_channel(int(general))
    #if general_channel:
    #    await general_channel.send("Can't wait to hop on Apex!")
    while True:
        await asyncio.sleep(180)  # 180 seconds = 3 minutes
        await send_afk_message(general_channel)

# STEP 4: handling incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    # print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

# STEP 5: Main entry point
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()