import discord
import os
from discord.ext import commands
import json
from discord import Intents
#importing random stuff lol
import asyncio
import random

bot = commands.Bot(command_prefix=commands.when_mentioned_or("sex!")) #ass sexy bot prefix

#for checking if bot online yet, printing out to the terminal (bored)
@bot.event
async def on_ready():
    print('im on')
    
#info command
@bot.command(name="info")
async def infobot(ctx):
  embed = discord.Embed(title="infos on me bitch", colour=0x6fa3f7)
  embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/827509069366427668.png")
  embed.add_field(name="Made by Neptix the fucking idiot", value="fucking idiot", inline=False)
  embed.add_field(name="Coded on Dcoder", value="thanks", inline=True)
  embed.add_field(name="im not gonna be running all day", value="not hosted on any web server or smth lol", inline=True)
  embed.set_footer(text="version 1.6.5", icon_url="https://media.discordapp.net/attachments/863373815589371954/864452961882210324/Avatar.png")
  await ctx.send(embed=embed)
#^using embeds lol
  
#small ping command
@bot.command(name="ping")
async def ping(ctx: commands.Context):
  await ctx.send(f"bitch i have {round(bot.latency * 1000)}ms") #bot latency is stuff
  
#bot avatar
@bot.command(name="botav")
async def botav(ctx):
  embed = discord.Embed(title="my sexy avatar", colour=0x6fa3f7)
  embed.set_image(url="https://media.discordapp.net/attachments/863373815589371954/864452961882210324/Avatar.png")
  await ctx.send(embed=embed)
  
#presence (owner only)
@bot.command(name="setstatus")
@discord.ext.commands.is_owner()
async def setstatus(ctx: commands.Context, *, text: str):
  await bot.change_presence(activity=discord.Game(name=text))
  await ctx.send(f'yeah done set status to "{text}" check my status')

    
#help command
@bot.command(name="commands")
async def commands(ctx: commands.Context):
  embed = discord.Embed(title="__Commands for me bitch__", description="command syntax is sex! btw fucker (or you can ping me lololol)", colour=0x6fa3f7)
  embed.add_field(name="sex!info", value="infos on me bitch")
  embed.add_field(name="sex!changelog", value="the changelog fucker")
  embed.add_field(name="sex!normalcommands", value="normal commands fucker")
  embed.add_field(name="sex!modcommands", value="mod commands fucker")
  embed.set_author(name="secks bot lol", icon_url="https://media.discordapp.net/attachments/863373815589371954/864452961882210324/Avatar.png")
  await ctx.send(embed=embed)
  
#moderation help command
@bot.command(name="modcommands")
async def modcommands(ctx):
  embed = discord.Embed(title="__Mod commands fucker__", description="you and i must have mod perms to use these commands fucker", colour=0x6fa3f7)
  embed.add_field(name="kick (sex!kick @user)", value="kick a bitch out of this guild")
  embed.add_field(name="ban (sex!ban @user)", value="ban a bitch out of this guild")
  embed.add_field(name="mute (only available in platform gdps please wait)", value="make a bitch shut the fuck up")
  embed.add_field(name="unmute (only available in platform gdps please wait)", value="fine you lucky this time bitch")
  await ctx.send(embed=embed)
  
#normal commands help
@bot.command(name="normalcommands")
async def normalcommands(ctx):
  embed = discord.Embed(title="__Normal commands fucker__", description="funny", colour=0x6fa3f7) 
  embed.add_field(name="ping (sex!ping)", value="my ping bitch")
  embed.add_field(name="botav (sex!botav)", value="my sexy avatar (its opheebop but humanoid bitch)")
  embed.add_field(name="setstatus", value="set my status to whatever the fuck you want (owner usage only)")
  embed.add_field(name="speak (sex!speak msg)", value="make me say anything bitch")
  embed.add_field(name="quote (sex!copy quote)", value="make a funny quote (amogus)")
  embed.add_field(name="avatar (sex!avatar @user)", value="get a person avatar (pedophile simulator)")
  embed.add_field(name="serverav (sex!serverav)", value="get the funny server picture")
  await ctx.send(embed=embed)
  
#changelog command
@bot.command(name="changelog")
async def changelog(ctx):
  embed = discord.Embed(title="__Changelogs for secks bot lol__", description="we do a little trolling", colour=0x6fa3f7)
  embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/827509069366427668.png")
  embed.add_field(name="version 1.6.5 (7/25/2021)", value="added serverav command")
  embed.add_field(name="version 1.6 (7/23/2021)", value="added avatar command for pedophiles")
  embed.add_field(name="version 1.5.99 (7/22/2021)", value="added unmute command (only available for platform gdps other servers please wait)")
  embed.add_field(name="version 1.5.8 (7/22/2021)", value="added quote command, added changelog command, revamped copy command to speak command, revamped snd added more to help commands and info commands")
  embed.set_footer(text="your welcome", icon_url="https://media.discordapp.net/attachments/863373815589371954/864452961882210324/Avatar.png")
  await ctx.send(embed=embed)
  
#ban command
@bot.command(name="ban")
@discord.ext.commands.has_permissions(ban_members=True)
async def bantest(ctx, *, member: discord.User):
  embed = discord.Embed(title="died", description=f"{member} got yeeted out of this server ekcs dee")
  await member.ban()
  await ctx.send(embed=embed)
  
#kick command
@bot.command(name="kick")
@discord.ext.commands.has_permissions(kick_members=True)
async def kick(ctx, *, member: discord.User):
  embed = discord.Embed(title="kicke", description=f"{member} has been kicke out of da server")
  await member.kick()
  await ctx.send(embed=embed)
  
#mute command
@bot.command(name="mute")
@discord.ext.commands.has_permissions(kick_members=True)
async def mute(ctx, *, user: discord.User):
  role = discord.utils.get(ctx.guild.roles, id=804318738144428073)
  embed = discord.Embed(title="muted", description=f"{user} got muted (fat fuvking nuts)", colour=0xff0004)
  await user.add_roles(role)
  await ctx.send(embed=embed)
  
#unmute command
@bot.command(name="unmute")
@discord.ext.commands.has_permissions(kick_members=True)
async def unmute(ctx, *, user: discord.User):
  role = discord.utils.get(ctx.guild.roles, id=804318738144428073)
  embed = discord.Embed(title="unmuted", description=f"{user} got unmuted (lucky)", colour=0x00ff2f)
  await user.remove_roles(role)
  await ctx.send(embed=embed)
  
#check if online
@bot.command(name="online")
async def onlinecheck(ctx):
  await ctx.send("yes im online stfu")
  
#enslave command
@bot.command(name="sex")
async def sexplease(ctx, *, member: discord.User):
  await ctx.send(f"uwu please cum on me {member.mention} :yum: :hot_face:")

#copy command
@bot.command(name="speak")
async def copy(ctx, *, msg):
  await ctx.send(f"{msg}")
  
#quote command
@bot.command(name="quote")
async def quote(ctx, *, quote):
  await ctx.send(f'"{quote}"\n- {ctx.author.mention}')
  
#epic embed fail
@bot.command(name="embfail")
@discord.ext.commands.is_owner()
async def epicembedfail(ctx):
  await ctx.send("https://tenor.com/view/among-us-epic-embed-fail-amogus-sus-gif-20553663")

#epic embed success
@bot.command(name="embsuccess")
@discord.ext.commands.is_owner()
async def epicembedsuccess(ctx):
  await ctx.send("https://tenor.com/view/epic-embed-success-epic-embed-fail-gif-21239189")  

#avatar command
@bot.command(name="avatar")
async def avatar(ctx, *, member: discord.Member = None):
  if not member:
    member = ctx.message.author
  memav = member.avatar_url 
  embed = discord.Embed(title=f"avatar of {member}", colour=0x6fa3f7)
  embed.set_image(url=memav) 
  await ctx.send(embed=embed) 
  
#the legendary shut up command
@bot.command(name="shutup")
@discord.ext.commands.is_owner()
async def shutup(ctx, *, member: discord.User):
  await ctx.send(f"shut the fuck up {member.mention}")
  
#remove roles
@bot.command(name="removerole", description='Adds/removes a role from/to a user.')
@discord.ext.commands.has_guild_permissions(manage_roles=True)
async def removerole(ctx, user: discord.Member, *, role: discord.Role):
    if role.position > user.top_role.position:
      await ctx.send("bro you dont have perm smh")
      return
    
    if role in user.roles:
      await user.remove_roles(role)
      await ctx.send(f"yeeted {role} from {user.mention}")
    
#give role command
@bot.command(name="giverole", description='Adds/removes a role from/to a user.')
@discord.ext.commands.has_permissions(manage_roles=True)
async def giverole(ctx, user: discord.Member, *, role: discord.Role):
    if role.position > user.top_role.position:
      await ctx.send("you dont have perm smh")
      return
      
    if role in user.roles:
      await user.add_roles(role)
      await ctx.send(f"big chungus came and gave {user.mention} da powa of {role}")
      
#your mother
@bot.command(name="sexcum")
async def sexcum(ctx):
  await ctx.send(f"uwu please cum on my daddy {ctx.message.author} >_< :yum: :hot_face:")
  
#server avatar
@bot.command(name="serverav")
async def serverav(ctx):
  serverav = ctx.guild.icon_url
  embed = discord.Embed(title=f"sexy {ctx.guild.name} server avatar", colour=0x6fa3f7)
  embed.set_image(url=serverav)
  await ctx.send(embed=embed)



bot.run(insert_token)
