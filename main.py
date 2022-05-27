import os
import discord
from dotenv import load_dotenv

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

#@client.event
#async def on_message(message):
#    if 'loser' in message.content.lower():
#        await message.channel.send('Yes I agree Tanguy is loser! 🎈')

client.run(TOKEN)
