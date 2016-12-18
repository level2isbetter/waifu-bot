import discord
import asyncio

client = discord.Client()

#Getting set up
@client.async_event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    yield from client.change_presence(game=discord.Game(name='boi'))

#Process commands
@client.event
async def on_message(message):
    await client.process_commands(message)
    
#Error messages
@client.event
async def on_command_error(error, context):
    await client.send_message(context.message.channel, 'you fucking idiot messed up on ' + repr(error))

#Reloading shit
@client.command(description='Reloads extensions. Usage: /reload [extension_list]')

@client.event
async def on_message(message):
    if message.content.startswith('/hi'):
        tmp = await client.send_message(message.channel, 'hi!!!! xD')

@client.event
async def on_message(message):
    if message.content.startswith('boi'):
        tmp = await client.send_message(message.channel, 'ayyy boi what skin you want boi?')

@client.event
async def on_reaction_add(reaction, user):
    await client.send_message(reaction.message.channel, "The reaction added was: " + str(reaction.emoji))
    await client.delete_message(reaction.message)

client.run('MjU2NjI5NTQwOTYzNjE0NzIw.CywisA.cttD_e4F3mZP2uYxJWZ1ZSSfTHI')
