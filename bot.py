
import discord
import requests
import json

# Function to fetch a meme URL from the Meme API
def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

# Custom client class extending discord.Client
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # Prevent the bot from responding to its own messages
        if message.author == self.user:
            return
        # Respond with a meme when the user types $meme
        if message.content.startswith('$meme'):
            meme_url = get_meme()
            await message.channel.send(meme_url)

# Set the message content intents
intents = discord.Intents.default()
intents.message_content = True

# Create and run the client with your bot token
client = MyClient(intents=intents)
client.run('MTI4Nzk3NDY0MzAwMDY3NjM5NQ.Ga2wef.C_HYnnn1fM_mW-tXo1rhFtdMCG-2sWAtYEFHzw')
