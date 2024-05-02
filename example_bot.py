import os
import discord
from markov import discord_bot


# base_path = "/path/to/src"
# file_name = ["green-eggs.txt"]

# file_path = os.path.join(base_path, file_name)

if __name__ == '__main__':

    discord_bot("green-eggs.txt")

    # text = open_and_read_file(["green-eggs.txt"])
    # chains = make_chains(text)
    # make_text(chains)

    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents = intents)

    client.run(os.environ['DISCORD_TOKEN'])

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    if message.content.startswith("$hello"):
        await message.channel.send("hi!")

