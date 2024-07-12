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

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
intents.members = True 


bot = commands.Bot(command_prefix="&", intents=intents)


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
   await ctx.send(f"<@{ctx.author.id}> saluda con creces a <@{member.id}>, how are you? 🥴")
@bot.command()
async def ayuda(ctx):
    embed = discord.Embed(title="Comandos disponibles", description="Aquí están los comandos disponibles:")
    embed.add_field(name="&ping", value="Muestra 'pong' y el ms.", inline=False)
    embed.add_field(name="&saludar [nombre]", value="Saluda a alguien por su nombre", inline=False)
    embed.add_field(name="&informacion",value="Muestra información sobre mí", inline=False)
    embed.add_field(name="&ayuda",value="Muestra esta lista de comandos",inline=False)
    embed.add_field(name="&avatar",value="Muestra el avatar del usuario que menciones",inline=False)
    embed.add_field(name="&serverinfo",value="Muestra información sobre el servidor",inline=False)
    embed.add_field(name="&userinfo",value="Muestra información sobre el usuario que menciones",inline=False)
    
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
    embed.add_field(name="Nombre",value=ctx.guild.name,inline=False)
    embed.add_field(name="ID",value=ctx.guild.id,inline=False)
    embed.add_field(name="Fecha de creación",value=ctx.guild.created_at.strftime("Se creo el %d/%m/%Y a las %H:%M:%S"))
    embed.add_field(name="Creador",value=ctx.guild.owner.name)
    embed.add_field(name="Miembros",value=ctx.guild.member_count)
    embed.add_field(name="Canales",value=len(ctx.guild.channels))
    embed.add_field(name="Roles",value=len(ctx.guild.roles))
    embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.set_footer(text=f"Solicitado por {ctx.author.name}")
    await ctx.send(embed=embed)
    

@bot.command(name="say")
async def say(ctx, *, message):
    await ctx.send(message)



@bot.command()
async def sincronizar(ctx):
    await bot.tree.sync()
    await ctx.send("Listo!")
@bot.event
async def on_ready():
   await bot.change_presence(activity=discord.Activity(
       type=discord.ActivityType.watching, name="&ayuda"))
   print(f"Conectado como {bot.user}")


bot.run(TOKEN)
