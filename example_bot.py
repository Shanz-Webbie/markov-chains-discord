import os
import discord
from markov import discord_bot



# base_path = "/path/to/src"
# file_name = ["green-eggs.txt"]

# file_path = os.path.join(base_path, file_name)

if __name__ == '__main__':


    # text = open_and_read_file(["green-eggs.txt"])
    # chains = make_chains(text)
    # make_text(chains)

    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents = intents)

    @client.event
    async def on_ready():
        print(f"We have logged in as {client.user}")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 
        elif message.content.startswith("$hello"):
            await message.channel.send("hi!")
        elif message.content.startswith("$eggs"):
            await message.channel.send("green? and ham?")
        else:
            await message.channel.send(discord_bot("green-eggs.txt"))


    client.run(os.environ['DISCORD_TOKEN'])

