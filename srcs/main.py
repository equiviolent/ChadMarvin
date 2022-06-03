import os
import discord
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} has connected to Discord!\n'
        f'{guild.name}(id: {guild.id})'
    )


    members = '\n - '.join([member.name for member in guild.members])
    
    print(f'Chad Members:\n - {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
            f'Hi {member.name}, welcome to the ChadConributors server!'
            )

#This function makes the bot seem depressed if you say windows
def randomPain():
    painWords = ['why','bruh', 'pain', 'no', 'really ?','torment','misery','I am aching', 'Y u n0 u53 4rch??1','https://www.digitalcitizen.life/how-uninstall-windows-8-windows-7-or-any-other-version-windows/','Please dont post this it isnt funny. Never in all my years on this earth have I cringed at a message so much. I swear on God that seeing this word brings me a pain which I cant describe so please for the sake of my body and mind dont ever post this again or I may legitimately die from cringe']
    return ''.join(random.sample(painWords,1))
<<<<<<< HEAD

@client.event
async def on_message(message):
=======
@client.event
async def on_message(self, message):
    if (message.author.bot):
        return
>>>>>>> 44b35fdb0dec78276b0f0618799213bb81b4d1d6
    if 'windows' in  message.content.lower():
        await message.channel.send(randomPain(), reference=message)

client.run(TOKEN)
