from requests.models import Response
import discord, aiocron, time, aiohttp, os, random, re, datetime
import requests, json
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Member
from urllib import parse, request
from datetime import datetime
from googletrans import Translator
from discord import Color

from discord import FFmpegPCMAudio
from dotenv import load_dotenv

#load_dotenv()

CHANNEL_ID="channel_id"

bot = discord.Client()
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', help_command=None, owner_id = 538435819975868417, intents=intents)
bot.launch_time = datetime.utcnow()

#join
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you | !help")) 
    print(f"{bot.user}"[:-5] + " - is on")

#upcoming commands
#!nday !gif !radio

helpcmd = "CMD: !yt !gather !poke !agent !rulete !ping !translate"
ruletes = "Go shoot yourself - !bang"
agents = ["Astra :woman_astronaut:", "Breach :bread:", "Brimstone", "Cypther", "Jett", "Killjoy", "Omen", "Pheonix :fire:", "Raze", "Sage", "Skye", "Sova", "Viper", "Yoru"]
greetings = ['hello', "hi", "labas", "sveiki", "sveikas", "hey", "y0", "y0y0", "sup", "yo",]
bangs = ["you are still alive", "great luck keep going", "amazing you might clutch few rounds today", "go to play lottery", "viking lotto is waiting for you", "i would play bet game right now", "da nu na..."]
translates = 'Example: !tl ja kaip sekasi?`\nOutput: 元気ですか`'
#help
@bot.command()
async def help(context):
    await context.send(helpcmd)
    return

#rulete explain
@bot.command()
async def rulete(context):
    await context.send(ruletes)
    return

#translate explain
@bot.command()
async def translate(context):
    await context.send(translates)
    return

#rulete game
@bot.command()
async def bang(ctx):
    bullet_pos = 3
    if bullet_pos == (random.randint(1,6)):
        await ctx.send("you are dead 💩") 
    else:
        await ctx.send(random.choice(bangs) +"\n`bang once more?`")

#gather
@bot.command()
async def gather(ctx, *, args=None):
    if args is not None:
        members = ctx.guild.members
        for member in members:
            try:
                await member.send(args)
            except discord.errors.Forbidden:
                print(f"not sent: {member.name}")
            except discord.errors.HTTPException:
                print(f"not sent: {member.name}")
    else:
        await ctx.send("insert text :poop:\ntype: !gather text")

#agent
@bot.command()
async def agent(context):
    await context.send("Go win with " +random.choice(agents))

#poke
@bot.command()
async def poke(ctx, user: discord.Member=None):
    if user is None:
        await ctx.send("insert user :poop:\ntype: !poke user (or @user)")
    await user.send(":wave:")

#ping
@bot.command()
async def ping(ctx):
    await ctx.send(f'Poooonnng! {bot.latency * 1000}ms')

#translate
@bot.command()
async def tl(ctx, lang, *, thing):
    translator = Translator()
    translation = translator.translate(thing, dest=lang)
    await ctx.send(translation.text)

#yt
@bot.command()
async def yt(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_content= html_content.read().decode()
    search_results = re.findall(r'\/watch\?v=\w+', search_content)
    #print(search_results)
    await ctx.send('https://www.youtube.com' + search_results[0])

#uptime
@bot.command()
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - bot.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.send(f"{days}d, {hours}h, {minutes}m, {seconds}s")

bot.run("token")
