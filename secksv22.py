import discord
import os
from discord.ext import commands
import json
from discord import Intents
import aiohttp
import dotenv
from dotenv import load_dotenv, find_dotenv
import io
import sys
import traceback
import re
import datetime
#importing random stuff lol
import asyncio
import random
import time

#=================BOT INSTANCES AND STUFF=====================
load_dotenv()
load_dotenv(find_dotenv())
itsumi = os.getenv('itsumi')
activity = discord.Activity(name="neptix (aka doing neptix <3)", type = discord.ActivityType.playing)
bot = commands.Bot(command_prefix=commands.when_mentioned_or("sex!"), case_insensitive=True, activity=activity, intents = discord.Intents.all())
bot.remove_command("help")

#=================EVENTS=====================

#for checking if bot online yet, printing out to the terminal (bored)
@bot.event
async def on_ready():
    print('im on')
    
   
#snipe event
snipe_message_author = {}
snipe_message_content = {}

@bot.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await asyncio.sleep(60)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]
     
#piethon
@bot.listen()
async def on_message(message):
    for mentions in message.mentions:
      if message.author == bot.user:
        return
      if mentions.id == 754172554746265701:
            await message.channel.send("shut up")
            
     
#================SNIPE COMMAND LOL==================

#snipe command
@bot.command()
async def snipe(ctx):
    channel = ctx.channel
    try: #This piece of code is run if the bot finds anything in the dictionary
        em = discord.Embed(title=f"something sniped from poopoo head {snipe_message_author[channel.id]}:", description=f'"{snipe_message_content[channel.id]}"', colour=0x6fa3f7)
        #{snipe_message_author[channel.id]}
        await ctx.send(embed = em)
    except: #This piece of code is run if the bot doesn't find anything in the dictionary
        await ctx.send(f"theres currently nothing in {ctx.channel.mention} poopoo head")

#If the bot sends the embed, but it's empty, it simply means that the deleted message was either a media file or another embed.

#===============INFOS COMMANDS==========================      
        
#info command
@bot.command(name="info")
async def infobot(ctx):
  botavatar = bot.user.avatar_url
  embed = discord.Embed(title="infos on me bitch", colour=0x6fa3f7)
  embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/827509069366427668.png")
  embed.add_field(name="Made by Neptix the fucking idiot", value="fucking idiot", inline=False)
  embed.add_field(name="Coded on Dcoder and discord.py", value="thanks", inline=True)
  embed.add_field(name="im not gonna be running all day", value="not hosted on any web server or smth lol", inline=True)
  embed.set_footer(text="version 2.2, discord.py", icon_url=botavatar)
  await ctx.send(embed=embed)
#^using embeds lol
  
#THE HELP COMMAND (uses help function and also more space saving)
@bot.command(aliases=["helps", "commands"])
async def help(ctx):
  embed = discord.Embed(title="HELP SECTIONS (mhm hot)", description="command prefix is ```sex!``` btw fucker or you can ping me lolololol", colour=0x6fa3f7)
  embed.add_field(name="INFO COMMANDS", value="```info```, ```changelog```, ```help (this command)```", inline=True)
  embed.add_field(name="NORMAL COMMANDS", value="```ping```, ```quote```, ```copy```, ```point (direction)```, ```percent```, ```poll```, ```snipe```, ```ship```", inline=True)
  embed.add_field(name="GET STUFF COMMANDs", value="```serverav```, ```botav```, ```av```")
  embed.add_field(name="IMAGE COMMANDS", value="```dog```, ```cat```, ```pat```, ```hug```, ```wink```, ```horny```, ```triggered```, ```hex```, ```simpcard```")
  embed.add_field(name="SEARCH COMMANDS", value="```lyrics```")
  embed.add_field(name="MODERATION COMMANDS", value="```ban```, ```unban```, ```kick```, ```giverole```, ```removerole```, ```mute```, ```unmute```, ```purge (delete, clear)```", inline=True)
  embed.add_field(name="VC RELATED COMMANDS", value="```join (joinvc)```, ```disconnect (leavevc)```")
  embed.add_field(name="OWNER-ONLY COMMANDS", value="```setstatus```, ```setwatching```, ```sex```, ```shutup```, ```senddm```, ```shutdown```", inline=True)
  embed.set_footer(text="properly belongs to secks bot and a littlebit of big chungus", icon_url="https://cdn.discordapp.com/avatars/844199379678265365/93c36e20efd4ff67eb89bf0309b045dc.webp")
  await ctx.send(embed=embed)
  
#changelog command
@bot.command(name="changelog")
async def changelog(ctx):
  embed = discord.Embed(title="CHANGELOGS", description="we do a little trolling", colour=0x6fa3f7)
  embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/827509069366427668.png")
  embed.add_field(name="version 2.2", value="added simpcard and hex command")
  embed.add_field(name="version 2.1", value="added search commands, added triggered and horny cmmands, more bug fix")
  embed.add_field(name="version 2.0 official release", value="fixed stuff, added more features for mod commands and stuff, bug fixs")
  embed.add_field(name="VERSION 2.0 pre-release (huge update)", value="REVAMPED ALOT OF STUFF (cool), ADDED IMAGES COMMANDS (check in help command), BECAME LESS RACIST (no balls), ORGANIZED CODE FILE (might open source this lol)")
  embed.set_footer(text="funy changelogs", icon_url="https://images-ext-2.discordapp.net/external/seppmsU7GonsQfo_VrnmMPKGC9KT_SKsAkjtLSU8D-8/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/844199379678265365/93c36e20efd4ff67eb89bf0309b045dc.webp")
  await ctx.send(embed=embed)  
  
#====================NORMAL COMMANDS=======================  
  
#small ping command
@bot.command(name="ping")
async def ping(ctx):
  await ctx.reply(f"bitch i have {round(bot.latency * 1000)}ms") #bot latency is stuff
  
#bot avatar
@bot.command(name="botav", aliases=["botavatar"])
async def botav(ctx):
  botavatar = bot.user.avatar_url
  embed = discord.Embed(title="im sexy", colour=0x6fa3f7)
  embed.set_image(url=botavatar)
  await ctx.send(embed=embed)
  
#presence (owner only)
@bot.command(name="setstatus")
@discord.ext.commands.is_owner()
async def setstatus(ctx: commands.Context, *, text: str):
  await bot.change_presence(activity=discord.Game(name=text))
  await ctx.send(f'yeah done set status to "{text}" check my status')
  
#presence (watching) (owner only)
@bot.command(name="setwatching")
@discord.ext.commands.is_owner()
async def setwatching(ctx: commands.Context, *, text: str):
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=text))
  await ctx.send(f'yeah done set status to "{text}" check my status')
  
#ban command
@bot.command()
@discord.ext.commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason = None):
  embed = discord.Embed(title="fucking died", description=f'{member} just got vanished by big chungus with the reason: "{reason}"', colour=0x00ff00)
  if member == ctx.message.author:
    no = discord.Embed(title="no", description="you dont ban yourself shithead", colour=0xff0000)
    return await ctx.send(embed=no)
  elif member == ctx.bot.user:
    nolol = discord.Embed(title="no you motherfucker", description="you cant ban me shithead", colour=0xff0000)
    return await ctx.send(embed=nolol)
  elif reason is None:
    return await ctx.send("provide a reason smh")
  elif member == ctx.message.author:
    no = discord.Embed(title="no", description="you dont ban yourself shithead", colour=0xff0000)
    return await ctx.send(embed=no)
  try:
    await member.ban(reason=reason)
  except Exception as e:
    return await ctx.send(e)
  await ctx.send(embed=embed)
  await member.send(f'yo got banned by big chungus (aka {ctx.message.author}) from {ctx.guild} because "{reason}" (aka you suck cock)!!!!!!!!!!!!!;;;')
  
#kick command
@bot.command()
@discord.ext.commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member = None, *, reason = None):
  if member == ctx.message.author:
    deez = discord.Embed(title="no", description="you dont kick youself shithead", colour=0xff0000)
    return await ctx.send(embed=deez)
  elif member == ctx.bot.user:
    noshithead = discord.Embed(title="no you motherfucker", description="you cant kick me shithead", colour=0xff0000)
    return await ctx.send(embed=noshithead)
  elif member is None:
    return await ctx.send("get someone to kick smh")
  elif member.top_role >= ctx.author.top_role:
    error_embed = discord.Embed(title='too bad', description="you cant kick because youre sucker than the person youre trying to kick!!!!!!", colour=0xff0000)
    return await ctx.send(embed=error_embed)
  elif reason is None:
    return await ctx.send("provide a reason smh")
  try:
    embed = discord.Embed(title="kicke", description=f'{member} just got kicke by big chungus with the reason: "{reason}"', colour=0x00ff00)
    await member.kick(reason=reason)
    await ctx.send(embed=embed)
    await member.send(f'yo got kicke by big chungus (aka {ctx.message.author}) from {ctx.guild.name} because "{reason}" (aka you suck)!!!!!!!!!;;')
  except Exception as e:
    await ctx.send(e)
    
#mute command
@bot.command(name="mute")
@discord.ext.commands.has_permissions(kick_members=True)
async def mute(ctx, *, user: discord.Member):
  if user == ctx.message.author:
    no = discord.Embed(title="no", description="you dont mute yourself shithead", colour=0xff0000)
    return await ctx.send(embed=no)
  elif user == ctx.bot.user:
    shithead = discord.Embed(title="no", description="you cant mute me you fuckhead!!!!!", colour=0xff0000)
    return await ctx.send(embed=shithead)
  role = discord.utils.get(ctx.guild.roles, name="Muted")
  embed = discord.Embed(title="muted", description=f"{user} got muted (fat fuvking nuts)", colour=0xff0004)
  await user.add_roles(role)
  await ctx.send(embed=embed)
  
#unmute command
@bot.command(name="unmute")
@discord.ext.commands.has_permissions(kick_members=True)
async def unmute(ctx, *, user: discord.Member):
  Muted = discord.utils.get(ctx.guild.roles, name="Muted")
  if Muted not in user.roles:
    no = discord.Embed(title="no", description="your not muted smh why are you even trying to unmute yourself when youre not muted", colour=0xff0000)
    return await ctx.send(embed=no)
  role = discord.utils.get(ctx.guild.roles, name="Muted")
  embed = discord.Embed(title="unmuted", description=f"{user} got unmuted (lucky)", colour=0x00ff2f)
  await user.remove_roles(role)
  await ctx.send(embed=embed)    
  
#enslave command
@bot.command(name="sex")
async def sexplease(ctx, *, member: discord.User):
  await ctx.send(f"uwu please cum on me {member.mention} :yum: :hot_face:")

#copy command
@bot.command(name="copy")
async def copy(ctx, *, msg):
 content = ctx.message.content 
 await ctx.message.delete()
 await ctx.send(msg)
  
#quote command
@bot.command(name="quote")
async def quote(ctx, *, quote):
  await ctx.send(f'"{quote}"\n- {ctx.author.mention}') 

#avatar command
@bot.command(name="avatar", aliases=["av"])
async def avatar(ctx, *, member: discord.Member = None):
  if not member:
    member = ctx.message.author
  elif member == ctx.bot.user:
    return await ctx.send("bro you can use sex!botav yk smh")
  memav = member.avatar_url 
  embed = discord.Embed(title=f"avatar of {member}", colour=0x6fa3f7)
  embed.set_image(url=memav) 
  await ctx.send(embed=embed) 
  
#the legendary shut up command
@bot.command(name="shutup")
@discord.ext.commands.is_owner()
async def shutup(ctx, *, member: discord.User):
  content = ctx.message.content
  await ctx.message.delete()
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
    
    try:
      if role not in user.roles:
       await user.add_roles(role)
       await ctx.send(f"big chungus came and gave {user.mention} da powa of {role}")
    except Exception as e:
      print(e)
      
#server avatar
@bot.command(name="serverav")
async def serverav(ctx):
  serverav = ctx.guild.icon_url
  embed = discord.Embed(title=f"sexy {ctx.guild.name} server avatar", colour=0x6fa3f7)
  embed.set_image(url=serverav)
  await ctx.send(embed=embed)
  
#shut down bot
@bot.command(name="shutdown")
@discord.ext.commands.is_owner()
async def shutdownbot(ctx):
  embed = discord.Embed(title="anything for you babe neptix", description="shitting myself down...", colour=0xee0000)
  shutdown = discord.Embed(title="ok shutted down", description="uwu >_< (i have no balls)", colour=0xee0000)
  await ctx.send(embed=embed)
  await ctx.send(embed=shutdown)
  await bot.close()

#join vc
@bot.command(aliases=["joinvc", "join_voicechannel"])
async def join(ctx):
  try:
    vchannel = ctx.author.voice.channel
    await vchannel.connect()
    await ctx.send(f"joined vc {ctx.author.voice.channel}, having sex rn")
  except Exception as e:
    await ctx.send(f"```{e}```")
    
#disconnect 
@bot.command(aliases=["leave", "leavevc", "disconnectvc"], pass_context=True)
async def disconnect(ctx):
  try:
    vchannel = ctx.voice_client
    if vchannel:
      await ctx.send(f"done having sex in {ctx.author.voice.channel}")
      await vchannel.disconnect()
  except Exception as e:
    
    await ctx.send(f"```{e}```")
  
#send dms
@bot.command(name="senddm")
@discord.ext.commands.is_owner()
async def senddm(ctx, member: discord.User, *, msgdm):
    user = await member.create_dm()
    content = ctx.message.content
    await ctx.message.delete()
    await user.send(msgdm)
    await ctx.send(f"epicly trolled {member.mention}")
    
#random direction pointing shit
@bot.command(aliases=["randompoint", "direction"])
async def point(ctx):
  direction = ["Up", "Down", "Right", "Left", "12H", "13H", "9H", "8H", "24H", "6H"]
  await ctx.send("{}".format(random.choice(direction)))
  
#percent command thingy
@bot.command()
async def percent(ctx, *, thingy):
  await ctx.send(f"{ctx.message.author.mention}, you're {(random.randint(1, 100))}% ''{thingy}''")
    
#purge command
@bot.command(aliases=["delete", "clear"])
@discord.ext.commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
  await ctx.channel.purge(limit=amount)
  await ctx.send(f"deleted {amount} messages thingy in {ctx.channel.mention}")
  
#poll command
@bot.command()
async def poll(ctx, *, msg):
  await ctx.message.delete()
  embed = discord.Embed(title=f"poll by {ctx.message.author}:", description=f"{msg}", colour=0x6fa3f7)
  msg = await ctx.send(embed=embed)
  await msg.add_reaction("👍")
  await msg.add_reaction("👎")
  
#ship command
@bot.command()
async def ship(ctx, memberone: discord.User, membertwo: discord.User):
  embed = discord.Embed(title=f"{memberone.name} + {membertwo.name}", description=f"{memberone} and {membertwo} are canonically {(random.randint(1, 101))}% in love with eachother", colour=0xff66ff)
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/831532590862565387/873241777635733534/sketch-1628267442855.png")
  await ctx.send(embed=embed)
  
#no embed avatar
@bot.command()
async def noembav(ctx, member: discord.Member=None):
  if not member:
    member = ctx.author
    
  await ctx.reply(member.avatar_url)

@bot.command()
@discord.ext.commands.guild_only()
async def serverinfo(ctx):
  servername = str(ctx.guild.name)
  icon = str(ctx.guild.icon_url)
  desc = str(ctx.guild.description)
  owner = str(ctx.guild.owner)
  region = str(ctx.guild.region)
  members = str(ctx.guild.member_count)
  textch = len(ctx.guild.text_channels)
  voicech = len(ctx.guild.voice_channels)
  categories = len(ctx.guild.categories)
  verifylevel = str(ctx.guild.verification_level).upper()
  
  format = "%a, %d %b %Y | %H:%M:%S %ZGMT"
  
  embed = discord.Embed(title=f"infos for {servername}", description=f'"{desc}"', colour=0x6fa3f7)
  embed.set_thumbnail(url=icon)
  embed.add_field(name="**Server daddy**", value=owner)
  embed.add_field(name="**Le region**", value=region)
  embed.add_field(name="**Server count**", value=f"{members} memers")
  embed.add_field(name="**Le channels**", value=f":hash: {textch} :microphone2: {voicech} :asterisk: {categories}")
  embed.add_field(name="**Server existed since:**", value=f"{ctx.guild.created_at.strftime(format)}")
  embed.add_field(name="**Le verification**", value=verifylevel)
  embed.add_field(name="**Le features**", value=f"{', '.join(f'{x}' for x in ctx.guild.features)}")
  embed.add_field(name="**Le splash screen**", value=f"ctx.guild.splash")
  await ctx.send(embed=embed)
  
  
#==================AIOHTTP STUFF=========================
  
#doggy
@bot.command(aliases=["doggy", "dogs", "dogpics", "randomdogs"])
async def dog(ctx):
  async with aiohttp.ClientSession() as session:
    request = await session.get('https://some-random-api.ml/img/dog') # Make a request
    dogjson = await request.json() # Convert it to a JSON dictionary
    embed = discord.Embed(title="yooooo dogs", colour=0x6fa3f7) # Create embed
    embed.set_image(url=dogjson['link']) # Set the embed image to the value of the 'link' key
    await ctx.send(embed=embed) # Send the embed
    
#cat
@bot.command(aliases=["cats"])
async def cat(ctx):
  async with aiohttp.ClientSession() as session:
    request = await session.get('https://some-random-api.ml/animal/cat') # Make a request
    catjson = await request.json() # Convert it to a JSON dictionary
    embed = discord.Embed(title="yooooo cats", colour=0x6fa3f7) # Create embed
    embed.set_image(url=catjson['image']) # Set the embed image to the value of the 'link' key
    await ctx.send(embed=embed) # Send the embed
    
#pat anime shits
@bot.command(aliases=["animepat"])
async def pat(ctx):
  async with aiohttp.ClientSession() as session:
    request = await session.get('https://some-random-api.ml/animu/pat')
    patjson = await request.json()
    embed = discord.Embed(title="heres your pat weirdo (aka pedophile)", colour=0x6fa3f7)
    embed.set_image(url=patjson['link'])
    await ctx.send(embed=embed)

#hug anime shits
@bot.command(aliases=["animehug"])
async def hug(ctx):
  async with aiohttp.ClientSession() as session:
    request = await session.get('https://some-random-api.ml/animu/hug')
    hugjson = await request.json()
    embed = discord.Embed(title="heres some hugs weirdo (aka pedophile)", colour=0x6fa3f7)
    embed.set_image(url=hugjson['link'])
    await ctx.send(embed=embed)

#lycris yes  
@bot.command(aliases=['lyrc'])
async def lyrics(ctx, *, search = None):
    if not search:
        await ctx.send("put something dumbass")
        
    song = search.replace(' ', '%20')
    
    async with aiohttp.ClientSession() as lyricsSession: # define session
        async with lyricsSession.get(f'https://some-random-api.ml/lyrics?title={song}') as jsondata:
            if not (300 > jsondata.status >= 200):
                await ctx.send(f'{jsondata.status} api website is being shitty rn, can you be patient kthx and maybe try again')
            else:
                lyricsData = await jsondata.json() # load json data
        songLyrics = lyricsData['lyrics'] # the lyrics
        songArtist = lyricsData['author'] # the authors name
        songTitle = lyricsData['title'] # the songs title
        
        try:
            for chunk in [songLyrics[i:i+2000] for i in range(0, len(songLyrics), 2000)]: # if the lyrics extend the discord character limit (2000): split the embed
                embed = discord.Embed(title=f'heres your {songTitle} lycris that made by cool people {songArtist}', description=chunk, colour=0x6fa3f7)
                
                await lyricsSession.close() # closing the session
                
                await ctx.reply(embed=embed)
                
        except discord.HTTPException:
            embed = discord.Embed(title=f'heres your {songTitle} lyrcis that made by cool people {songArtist}', description=chunk, colour=0x6fa3f7)
            
            await lyricsSession.close() # closing the session
            
            await ctx.reply(embed=embed)  
            
#wink shit
@bot.command()
async def wink(ctx):
  async with aiohttp.ClientSession() as session:
    request = await session.get("https://some-random-api.ml/animu/wink")
    winkjson = await request.json()
    embed = discord.Embed(title="wink wink penis piss", colour=0x6fa3f7)
    embed.set_image(url=winkjson['link'])
    await ctx.send(embed=embed)

#code steal simulator
@bot.command()
async def triggered(ctx, member: discord.Member=None):
    if not member: # if no member is mentioned
        member = ctx.author # the user who ran the command will be the member
        
    async with aiohttp.ClientSession() as trigSession:
        async with trigSession.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg: # get users avatar as png with 1024 size
            imageData = io.BytesIO(await trigImg.read()) # read the image/bytes
            
            await trigSession.close() # closing the session and;
            
            await ctx.reply(file=discord.File(imageData, 'triggered.gif')) # sending the file
            
            
#yo horny
@bot.command()
async def horny(ctx, member: discord.Member = None):
    '''Horny license just for u'''
    member = member or ctx.author
    await ctx.trigger_typing()
    async with aiohttp.ClientSession() as session:
        async with session.get(
        f'https://some-random-api.ml/canvas/horny?avatar={member.avatar_url_as(format="png")}') as af:
         if 300 > af.status >= 200:
            fp = io.BytesIO(await af.read())
            file = discord.File(fp, "horny.png")
            em = discord.Embed(title="get pissed", color=0x6fa3f7)
            em.set_image(url="attachment://horny.png")
            await ctx.send(embed=em, file=file)
         else:
            await ctx.send('aiohttp got pissed, not working')
        await session.close()
   
#hex viewer
@bot.command()
async def hex(ctx, hex = None):
  if hex is None:
    return await ctx.send("put a hex code smh")
    
  async with aiohttp.ClientSession() as oph:
    async with oph.get(f'https://some-random-api.ml/canvas/colorviewer?hex={hex}') as balls:
      apishit = io.BytesIO(await balls.read())
      
      await oph.close()
      
      await ctx.send(file=discord.File(apishit, 'hex.png'))

#code steal simulator
@bot.command()
async def simpcard(ctx, member: discord.Member=None):
    if not member:
        member = ctx.author
        
    async with aiohttp.ClientSession() as simping:
        async with simping.get(f'https://some-random-api.ml/canvas/simpcard?avatar={member.avatar_url_as(format="png")}') as pissy:
            pissyapi = io.BytesIO(await pissy.read())
            
            await simping.close()
            
            await ctx.reply(file=discord.File(pissyapi, 'smhsimping.png')) # sending the file
            

#==================BOT RUN AND MORE IMPORTANT STUFF=========================

bot.run(itsumi)
