import discord
import asyncio

client = discord.Client()

@client.async_event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    yield from client.change_presence(game=discord.Game(name='boi'))

@client.event
async def on_message(message):
    if message.content.startswith('/hi'):
        await client.send_message(message.channel, 'hi!!!! xD')

@client.event
async def on_message(message):
    if message.content.startswith('boi'):
        await client.send_message(message.channel, 'ayyy boi what skin you want boi?')

@client.event
async def on_reaction_add(reaction, user):
    await client.send_message(reaction.message.channel, "The reaction added was: " + str(reaction.emoji))
    await client.delete_message(reaction.message)

client.run('MjU2NjI5NTQwOTYzNjE0NzIw.CywisA.cttD_e4F3mZP2uYxJWZ1ZSSfTHI')
