import discord
from discord.ext import commands
import cat_facts
import useless_facts
import roast
import definitions
import random
import compliment_api
import quotes
import praw


reddit = praw.Reddit(client_id = '***************',
                     client_secret = '*********************',
                     username = '***************',
                     password = '***************',
                     user_agent = 'python')

f = open("rules.txt", "r")
rules = f.readlines()
 
client = commands.Bot(command_prefix="!", case_insensitive = True)
 
@client.event
async def on_ready():
    print("Welcome Mojo MFs")
    
@client.command(aliases = ['hi','hey','sup'], brief = 'Say hi to the bot', help = 'Just say hello mf')
async def hello(ctx):
    await ctx.send("Sup Hoe")
    
@client.command(aliases = ['math'], brief = 'Can solve your math problems', help = 'Use + to add, - to minuse, * to multiply and / to divide')
async def solve(ctx, *args):
    problem = ' '.join(args)
    try:
        await ctx.send(eval(problem))
    except:
        await ctx.send("Here's math for you: 1-D-10-T")
        
@client.command(aliases = ['rules'], brief = 'Rules of the group')
async def rule(ctx, *, number):
    await ctx.send(rules[int(number) - 1])
    
@client.command(aliases = ['catfact', 'catfacts'], brief = 'For random cat facts')
async def meow(ctx):
    await ctx.send(cat_facts.cat_fact())
    
@client.command(aliases = ['uselessfacts'], brief = 'For facts that will change your life')
async def useless(ctx):
    await ctx.send(useless_facts.useless_fact())
    
@client.command(aliases = ['advice'], brief = 'Get quotes')
async def quote(ctx):
    await ctx.send(quotes.quote_content())
    
    
@client.command()
async def AmongUs(ctx):
    subreddit = reddit.subreddit("AmongUs")
    all_subs = []
    
    top = subreddit.top(limit = 500)
    
    for submission in top:
        all_subs.append(submission)
        
    random_submission = random.choice(all_subs)
    
    name = random_submission.title
    url = random_submission.url
    
    em = discord.Embed(title = name)
    em.set_image(url = url)
    
    await ctx.send(embed = em)
    
    
    
@client.command()
async def meme(ctx):
    subreddit = reddit.subreddit("memes")
    all_subs = []
    
    top = subreddit.top(limit = 500)
    
    for submission in top:
        all_subs.append(submission)
        
    random_submission = random.choice(all_subs)
    
    name = random_submission.title
    url = random_submission.url
    
    em = discord.Embed(title = name)
    em.set_image(url = url)
    
    await ctx.send(embed = em)
    
@client.command(aliases = ['roast'], brief = 'Use if you want your dignitiy to be lost')
async def roastme(ctx, arg1, *args):
    name = arg1
    await ctx.send(f"{name.capitalize()}, {roast.roast_me().lower()}")
    
@client.command(brief = 'Use to cheer someone up')
async def compliment(ctx, arg1, *args):
    name = arg1
    await ctx.send(f"{name.capitalize()}, {compliment_api.compliment_me().lower()}")

@client.command(aliases = ['die','apologize','shutdown','reset','kill'], brief = 'To kill the bot')
async def crash(ctx):
    apologies = ["I'm Sorry",
                 "I was just kidding",
                 "Sike",
                 "You can't do shit",
                 "Please don't harm me :pleading_face:",
                 "Stfu",
                 "I love you :heart:"]
    await ctx.send(apologies[(random.randrange(0,7))])
    
@client.command(aliases = ['meaning'], brief = 'To display meaning of English words')
async def define(ctx, *args):
    words = list(args)
    for word in words:
        try:
            for i in range(0, len(definitions.defined(word))):
                await ctx.send(f"{word.capitalize()}: {definitions.defined(word.lower())[i]['definition']}")
        except:
            await ctx.send(f"Definition for {word} not found")
            

@client.command(aliases = ['clear', 'c', 'd'], brief = 'Delete messages, admin only')
@commands.has_permissions(manage_messages = True)
async def delete(ctx, amount = 2):
    await ctx.channel.purge(limit = amount + 1)
    

client.run("***************************************************")
