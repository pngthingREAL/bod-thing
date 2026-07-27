import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random


# Cargar variables
load_dotenv()

TOKEN = os.getenv("TOKEN")


# Configuración
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# Inicio del bot
@bot.event
async def on_ready():
    print("======================")
    print(" BOT ENCENDIDO")
    print(f" Usuario: {bot.user}")
    print("======================")


# Manejo de errores de comandos
@bot.event
async def on_command_error(ctx, error):

    if isinstance(error, commands.CommandNotFound):
        return

    print("Error:", error)

    await ctx.send(
        "⚠️ Ocurrió un error ejecutando el comando."
    )


# Comando hola
@bot.command()
async def hola(ctx):

    await ctx.send(
        f"👋 Hola {ctx.author.mention}"
    )


# Comando dado
@bot.command()
async def dado(ctx):

    numero = random.randint(1, 6)

    await ctx.send(
        f"🎲 Resultado: **{numero}**"
    )


# Comando ping
@bot.command()
async def ping(ctx):

    latencia = round(bot.latency * 1000)

    await ctx.send(
        f"🏓 Pong! {latencia}ms"
    )


# Comando ayuda
@bot.command()
async def ayuda(ctx):

    texto = """
🤖 **Comandos disponibles**

!hola
Saludo del bot

!dado
Tira un dado

!ping
Muestra la latencia

!ayuda
Lista de comandos
"""

    await ctx.send(texto)


# Respuestas normales
@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    texto = message.content.lower()

    if texto == "hola bot":
        await message.channel.send(
            "¡Hola! Estoy funcionando correctamente"
        )

    await bot.process_commands(message)


# Comprobar token
if TOKEN is None:
    print("❌ ERROR: Falta el TOKEN en el archivo .env")
    print("por eso, me apagare, HAHAHAH)

else:
    bot.run(TOKEN)
