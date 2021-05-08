import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = "~" , self_bot=True)
#prefix = ~

client.remove_command('help')

@client.event
async def on_connect():
    print("Logged in as")
    print(client.user.name)
    print("------------")

client.run(os.getenv('SELF_TOKEN') , bot=False)

