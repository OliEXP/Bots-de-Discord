import discord
import random

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Evita que el bot responda a sus propios mensajes

    if message.content.startswith("!password"):
        password = gen_pass(10)  # Genera una contraseña de 10 caracteres
        await message.channel.send(f"Tu contraseña aleatoria es: {password}")

# Inicia el bot (reemplaza "TU_TOKEN_AQUI" con tu token real)
client.run("")
