import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from datetime import datetime
import random
from piadas import piadas_p

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"Oliveira online como {bot.user}")

@bot.command()
async def dev(ctx):
    await ctx.send("feito por SLRDev, discord: **oliveira__.**")

@bot.command()
async def oliveira(ctx):
    await ctx.send("fala")

@bot.command()
async def ping(ctx):
    ping = round(bot.latency * 1000)
    await ctx.send(f"pong **{ping}ms**")

@bot.command()
async def data(ctx):
    data = datetime.now().strftime("%d/%m/%Y")
    await ctx.send(f"hoje é dia {data}")

@bot.command()
async def hora(ctx):
    hora = datetime.now().strftime("%H:%M:%S")
    await ctx.send(f"agora são {hora}")

@bot.command()
async def moeda(ctx):
    cara_coroa = ["cara", "coroa"]
    await ctx.send(random.choice(cara_coroa))

@bot.command()
async def d6(ctx):
    dado_d6 = random.randint(1, 6)
    await ctx.send(f"o dado caiu no {dado_d6}")

@bot.command()
async def d20(ctx):
    dado_d20 = random.randint(1, 20)
    await ctx.send(f"o dado caiu no {dado_d20}")

@bot.command()
async def d100(ctx):
    dado_d100 = random.randint(1, 100)
    await ctx.send(f"o dado caiu no {dado_d100}")

@bot.command()
async def piada(ctx):
    await ctx.send("carrascosa")

@bot.command()
async def piadas(ctx):
    piada = random.choice(piadas_p)
    await ctx.send(piada)

@bot.command()
async def help(ctx):
    ordem = [
        "**dev**",
        "**oliveira**",
        "**ping**",
        "**data**",
        "**hora**",
        "**moeda**",
        "**d6**",
        "**d20**",
        "**d100**",
        "**piadas**",
    ]

    lista = "\n".join(f"- {c}" for c in ordem)

    embed = discord.Embed(
        title="Lista de Comandos",
        description=lista,
        color=discord.Color.blue()
    )

    await ctx.send(embed=embed)

bot.run(TOKEN)