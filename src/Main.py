import discord
from discord.ext import commands
import datetime
from discord.app_commands import CommandTree
from discord.interactions import (
    Interaction,
    InteractionResponse
)
import os
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
intents.members = True 

prefix = "$"
bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! 🏓 {round(bot.latency * 1000)}ms")

@bot.command()
async def hola(ctx):
    await ctx.send(f"Hola {ctx.author.name}")

@bot.command()
async def informacion(ctx):
   embed=discord.Embed(title="Sobre Astro",description="Información sobre mi, proporcionada hasta los momentos",color=0x00ff00)
   embed.add_field(name="Sobre mí",value="Soy Astro un bot creado por Dylan Marcano de la compañía Nox Corporations.inc, estoy en desarrollo y quiero llegar a hacer grandes cosas.")
   embed.add_field(name="Creador",value="Dylan Marcano (Dumb.Nox)")
   embed.add_field(name="Compañía que me desarrollo",value="Nox Corporations.inc")
   embed.add_field(name="Fecha de creación",value=f"El {bot.user.created_at.strftime('%d/%m/%Y a las %H:%M:%S')}")
   await ctx.send(embed=embed)

@bot.command()
async def saludar(ctx,member:discord.Member):
   await msg.send(f"<@{ctx.author.id}> saluda con creces a <@{member.id}>, how are you? 🥴")
@bot.command()
async def ayuda(ctx):
    embed = discord.Embed(title="Comandos disponibles", description="Aquí están los comandos disponibles:",color=0x00ff00)
    embed.add_field(name=f"{prefix}ping", value="Muestra 'pong' y el ms.", inline=True)
    embed.add_field(name=f"{prefix}saludar [nombre]", value="Saluda a alguien por su nombre", inline=True)
    embed.add_field(name=f"{prefix}informacion",value="Muestra información sobre mí", inline=True)
    embed.add_field(name=f"{prefix}ayuda",value="Muestra esta lista de comandos",inline=True)
    embed.add_field(name=f"{prefix}avatar",value="Muestra el avatar del usuario que menciones",inline=True)
    embed.add_field(name=f"{prefix}serverinfo",value="Muestra información sobre el servidor",inline=True)
    embed.add_field(name=f"{prefix}userinfo",value="Muestra información sobre el usuario que menciones",inline=True)
    embed.add_field(name=f"{prefix}ayuda_game",value="Muestra los comandos psrs divertirse",inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def ayuda_game(ctx):
    embed= discord.Embed(title="Comando de juegos",description="Comandos Fun",color=0x00ff00)
    embed.add_field(name=f"{prefix}rps",value="Juega al RPS")
    await ctx.send(embed=embed)

@bot.tree.command(name="pong",description="Primer comando de barra")
async def pong(interaction:discord.Interaction):
  await interaction.response.send_message("Es un placer!!!")

@bot.command()
async def avatar(ctx, member:discord.Member = None):
    if member == None:
        member = ctx.author
    embed=discord.Embed(title=f"Avatar de {member.name}",color=0x00ff00)
    embed.set_image(url=member.avatar.url)
    embed.set_footer(text=f"Solicitado por {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command()
async def userinfo(ctx,member:discord.Member = None):
    if member == None:
        member = ctx.author
    embed=discord.Embed(title=f"Información de {member.name}",color=0x00ff00)
    embed.add_field(name="Nombre",value=member.name,inline=False)
    embed.add_field(name="ID",value=member.id,inline=False)
    embed.add_field(name="Fecha de creación",value=member.created_at.strftime("%d/%m/%Y %H:%M:%S"))
    embed.add_field(name="Fecha de ingreso",value=member.joined_at.strftime("%d/%m/%Y %H:%M:%S"))
    embed.add_field(name="Roles",value=", ".join([role.name for role in member.roles]))

    embed.set_thumbnail(url=member.avatar.url)
    embed.set_footer(text=f"Solicitado por {ctx.author.name}")
    await ctx.send(embed=embed)
@bot.command()
async def serverinfo(ctx):
    embed=discord.Embed(title=f"Información del servidor {ctx.guild.name}",color=0x00ff00)
    embed.add_field(name="🖥️Nombre",value=f"`{ctx.guild.name}`",inline=True)
    embed.add_field(name= "🪪ID",value=f"`{ctx.guild.id}`",inline=True)
    embed.add_field(name="🗓️Fecha de creación",value=f"`{ctx.guild.created_at.strftime('Se creo el %d/%m/%Y a las %H:%M:%S')})`",inline=True)
    embed.add_field(name="👑Creador",value=f"`{ctx.guild.owner.name}`",inline=True)
    embed.add_field(name="👥Miembros",value=f"`{ctx.guild.member_count}`",inline=True)
    embed.add_field(name="Canales",value=f"`{len(ctx.guild.channels)}`",inline=True)
    embed.add_field(name="🧾Roles",value=f"`{len(ctx.guild.roles)}`",inline=True)
    embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.set_footer(text=f"Solicitado por {ctx.author.name}")
    await ctx.send(embed=embed)


@bot.command(name="say")
async def say(ctx, *, message):
    await ctx.send(message)
    await ctx.message.delete()


#Comandos de juegos
@bot.command()
async def rps(ctx,*,message):
    opciones = ["tijera","piedra","papel"]
    respuesta = message.lower()
    ordenador = random.choice(opciones)
    embed=discord.Embed(title="RPS Game",color=0x00ff00)
    if respuesta not in opciones:
      embed.add_field(name="Error!",value="Escribe Piedra, Papel o Tijera")
    elif respuesta == ordenador:
      embed.add_field(name=f"He sacado: {ordenador}",value="Es un Empate!!")
    elif respuesta == "tijera" and ordenador == "piedra" or respuesta == "piedra" and ordenador == "papel" or respuesta == "papel" and ordenador == "tijera":
      embed.add_field(name=f"{ordenador}",value="Has Perdido, lo siento")
    else:
      embed.add_field(name=f"He sacado: {ordenador}",value="Has Ganado, impresionante!")
    await ctx.send(embed=embed)
@bot.command()
async def numeromagico(ctx,*,message):
    opcion = random.randint(1,101)
    res = message
    respuesta = int(res)

    if respuesta > 100:
        await ctx.send("El numero debe de estar en el rango de 1 a 100")
    elif respuesta > opcion:
        await ctx.send("El numero que elegiste es muy alto")
    elif respuesta < opcion:
        await ctx.send("El numero que elegiste es muy bajo")
    else:
        await ctx.send("Acertaste, numero correcto")

@bot.command()
async def sincronizar(ctx):
    await bot.tree.sync()
    await ctx.send("Todo listo")
@bot.event
async def on_ready():
   await bot.change_presence(activity=discord.Streaming(name="Desarrollando",url="https://twitch.tv/username"))
   print(f"Conectado como {bot.user.name}")


class Menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Retroceder",style=discord.ButtonStyle.green)
    async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Hola me has clickeado!!")
    @discord.ui.button(label="Avanzar",style=discord.ButtonStyle.blurple)
    async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed=discord.Embed(title="Menu 2",color=discord.Color.random())
        embed.add_field(name="$rps",value="Juega un rato")
        await interaction.response.edit_message(embed=embed)

@bot.command()
async def menu(ctx):
    embed = discord.Embed(title="Menu de Astro",color=discord.Color.random())
    embed.add_field(name="$ayuda",value="Ve los comandos de ayuda de Astro")
    embed.add_field(name="$say",value="Habla como si fueras Astro!!")
    view = Menu()
    await ctx.reply(embed=embed,view=view)





bot.run(TOKEN)
