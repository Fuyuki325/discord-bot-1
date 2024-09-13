import os
from dotenv import load_dotenv
from typing import Final
from discord import Intents, Client, Message
from afkResponses import send_afk_message
import asyncio
from characterai import aiocai

# Load environment variables
load_dotenv()

CHAR_ID = os.getenv('CHAR_ID')
CHARACTER_AI_TOKEN = os.getenv('CHARACTER_AI_TOKEN')
DISCORD_TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
GENERAL_CHANNEL_ID = os.getenv('GENERAL')
SPECIFIC_CHAT_ID = os.getenv('SPECIFIC_CHAT_ID')

# Initialize Character AI client
async def start_character_ai():
    client = aiocai.Client(CHARACTER_AI_TOKEN)
    me = await client.get_me()
    chat = await client.connect()
    return client, chat, CHAR_ID, me

# Set up the Discord bot
intents: Intents = Intents.default()
intents.message_content = True
discord_client: Client = Client(intents=intents)

# Global variables for Character AI
chat = None
chat_id = None

# Function to handle messages
async def send_message(message: Message, user_message: str) -> None:
    if message.author == discord_client.user:
        return

    # Use Character AI API to get a response
    try:
        if chat and SPECIFIC_CHAT_ID:
            response = await chat.send_message(CHAR_ID, SPECIFIC_CHAT_ID, user_message)
            await message.channel.send(response.text)
        else:
            await message.channel.send("Character AI client is not initialized properly.")
    except Exception as e:
        print(f"An error occurred: {e}")
        await message.channel.send("Sorry, something went wrong.")

@discord_client.event
async def on_ready() -> None:
    global chat, chat_id
    print(f'{discord_client.user} is now running!')
    general_channel = discord_client.get_channel(int(GENERAL_CHANNEL_ID))
    if not chat:
        _, chat, CHAR_ID, me = await start_character_ai()
        # Initialize chat with existing chat ID
        # If SPECIFIC_CHAT_ID is not valid or needs a new one, handle it accordingly
    # while True:
    #     await asyncio.sleep(180)  # 180 seconds = 3 minutes
    #     await send_afk_message(general_channel)

@discord_client.event
async def on_message(message: Message) -> None:
    if message.author == discord_client.user:
        return

    user_message = message.content
    print(f'[{message.channel}] {message.author}: "{user_message}"')
    await send_message(message, user_message)

# Main entry point
async def main():
    global chat
    # Initialize Character AI client
    chat_client, chat, CHAR_ID, me = await start_character_ai()
    
    # Start Discord bot
    await discord_client.start(DISCORD_TOKEN)

if __name__ == '__main__':
    # Run the main coroutine with asyncio
    asyncio.run(main())
