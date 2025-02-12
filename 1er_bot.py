import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Hola'):
        await message.channel.send("Hola. ¿Todo bien?")
    elif message.content.startswith("Adiós"):
        await message.channel.send("Chao")
    else:
        await message.channel.send(message.content)

client.run()
