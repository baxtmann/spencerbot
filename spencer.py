import discord

import asyncio
import random

from dotenv import load_dotenv
import os

# --------------------- SETUP --------------------- #

intents = discord.Intents.default()
client = discord.Bot(intents=intents)
load_dotenv()

# you can replace None with a list of server-IDs, to make the commands instantly available there
# example: guild_ids = [123456789, 987654321]
guild_ids = None

spencer_messages = ["Well too bad! Stairs, stairs, stairs!",
                    "You're grounded for... till college!",
                    "Haha, look! His arm came off!",
                    "Why? Is Santa Clause here to tell me I'm ugly and have no freinds?",
                    "Don't say pie for breakfast, say PIE FOR BREAKFAST!",
                    "I once met a freaky rabi in vegas.",
                    "Look, in my life, I've learned a few things about girls. Like, when you break up with them, they do not like it when you ask out their sisters. That will get you a fork in your arm.",
                    "I told you to breathe through the tube! Oh wait... I forgot the tube.",
                    "She has magic feet!",
                    "Those Thalia-manians taught you good.",
                    "Toasty!",
                    "Don't worry, Toasty. Soon you'll be back and butter than ever!",
                    "So? It's a pie shop, not a church.",
                    "I made it into a squirrel",
                    "It's not just that. Last week on a bus, a hobo spilled chili on me, then continuted to eat it... without a spoon!",
                    "Behold the sign! Are you beholding it?",
                    "Well, I'm cooking/I'm cooking things/Cooking things for people to eat/I'm cooking/I'm cooking things/Things that people will chew.",
                    "If you're looking for a fun creative guy, well, you just took a right turn down lucky street. Why don't you go ahead and put it in park? Send me an email. Write it, click it, send it..."]


# --------------------- SLASH COMMANDS --------------------- #

@client.slash_command(guild_ids=guild_ids, name='spencer', description='spencer')
async def spencer(ctx):
    rand_int = random.randint(0, 6)

    await ctx.respond(f'https://edge.baxtmann.me/spencer/{rand_int}.gif')


@client.slash_command(guild_ids=guild_ids, name='heyspencer', description='hey spencer')
async def heyspencer(ctx):
    rand = random.randint(0, len(spencer_messages) - 1)

    await ctx.respond(spencer_messages[rand])


@client.slash_command(guild_ids=guild_ids, name='spencerchat', description='spencer chat')
async def spencerchat(ctx):
    await ctx.respond("Spencer is ready to unleash notification hell!")

    # spam a random spencer message
    for x in range(50):
        rand_spam = random.randint(0, len(spencer_messages) - 1)
        msg = spencer_messages[rand_spam]

        await ctx.channel.send(msg)

        # wait a few seconds
        await asyncio.sleep(5)


# --------------------- EVENTS --------------------- #

@client.event
async def on_message(message: discord.Message):
    if not message.guild or message.author == client.user:
        return

    if str(message.content).lower() == "who is your daddy":
        await message.channel.send("It's Brandon Axtmann! https://baxtmann.me")
        return

    # spencer replies to gibby quotes
    content = str(message.content).lower()
    reply = None

    if content == "my mom thinks i'm awesome!":
        reply = "Thats what she said!"
    elif content == "ahhhh! don't! i'm just a gibby!":
        reply = "Well I'm just a Spencer!"
    elif content == "i'm the statue of gibberty!":
        reply = "And I'm the statue of Attractive men!"
    elif content == "i couldn't find the tube!":
        reply = "I told you to breathe through the tube! Oh wait... I forgot the tube."
    elif content == "what am i? a mushroom?":
        reply = "No I'm a frog!"
    elif content == "what are you? a cop?":
        reply = "Officer Spencer here at your servi... oh look! A squirrel!"
    elif content == "this pudding rocks!":
        reply = "Why is your pudding rocks?!"
    elif content == "wow... umm. i'm in love with this sauce. what is it?":
        reply = "Its a sauce a hobo gave me!"
    elif content == "i invented cheesecake!":
        reply = "But have you had pie?"
    elif content == "oh really? i have that too!":
        reply = "I made it into a squirrel!"

    if reply is not None:
        await message.channel.send(reply)


@client.event
async def on_ready():
    print('Logged in as:')
    print(" Username:", client.user.name)
    print(" ID:", client.user.id)
    print("To invite the bot in your server use this link:\n https://discord.com/api/oauth2/authorize?client_id" + str(
        client.user.id) + "&permissions=2147518464&scope=bot%20applications.commands")


# --------------------- RUN --------------------- #

if __name__ == "__main__":
    client.run(os.getenv('SPENCER_TOKEN'))
