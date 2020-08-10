#!/usr/bin/env python3
import discord
import os
import asyncio
import config
from discord.ext import commands
import time
import datetime
import random


# Use ! to invoke custom bot commands (none implemented at this time)
bot = commands.Bot(command_prefix="!", pm_help=True, case_insensitive=True)
# removing default help command imported by discord python library
bot.remove_command("help")


@bot.event
async def on_message(message: discord.Message):
        # if not message.author.bot:
            if message.guild:
                if str(message.content).lower() == "spencer":
                    rand1 = random.randrange(0, 7)#setting range and generating random number
                    randstr = str(rand1)#converting int to string to we can add to url of gif
                    await message.channel.send("https://edge.baxtmann.me/spencer/"+(randstr)+".gif")#generates gif to display

            if str(message.content).lower() == "hey spencer":#when hey spencer is typed we will randomly generate a number and select a chat line to send to discord
                rand = random.randrange(0, 19)#generating random number
                if rand == 4:
                        await message.channel.send("Well too bad! Stairs, stairs, stairs!")
                if rand == 1:
                        await message.channel.send("You're grounded for... till college!")
                if rand == 2:
                        await message.channel.send("Haha, look! His arm came off!")
                if rand == 3:
                        await message.channel.send("Why? Is Santa Clause here to tell me I'm ugly and have no freinds?")
                if rand == 5:
                        await message.channel.send("Don't say pie for breakfast, say PIE FOR BREAKFAST!")
                if rand == 6:
                        await message.channel.send("I once met a freaky rabi in vegas.")
                if rand == 7:
                        await message.channel.send("Look, in my life, I've learned a few things about girls. Like, when you break up with them, they do not like it when you ask out their sisters. That will get you a fork in your arm.")
                if rand == 8:
                        await message.channel.send("I told you to breathe through the tube! Oh wait... I forgot the tube.")
                if rand == 9:
                        await message.channel.send("She has magic feet!")
                if rand == 10:
                        await message.channel.send("Those Thalia-manians taught you good.")
                if rand == 11:
                        await message.channel.send("Toasty!")
                if rand == 12:
                        await message.channel.send("Don't worry, Toasty. Soon you'll be back and butter than ever!")
                if rand == 13:
                        await message.channel.send("So? It's a pie shop, not a church.")
                if rand == 14:
                        await message.channel.send("I made it into a squirrel")
                if rand == 15:
                        await message.channel.send("It's not just that. Last week on a bus, a hobo spilled chili on me, then continuted to eat it... without a spoon!")
                if rand == 16:
                        await message.channel.send("Behold the sign! Are you beholding it?")
                if rand == 17:
                        await message.channel.send("Well, I'm cooking/I'm cooking things/Cooking things for people to eat/I'm cooking/I'm cooking things/Things that people will chew.")
                if rand == 18:
                        await message.channel.send("If you're looking for a fun creative guy, well, you just took a right turn down lucky street. Why don't you go ahead and put it in park? Send me an email. Write it, click it, send it...")
            if str(message.content).lower() == "who is your daddy":
                await message.channel.send("It's Brandon Axtmann! https://baxtmann.me")
            if str(message.content).lower() == "spencer chat":
                await message.channel.send("Spencer is ready to unleash notification hell!")
                for x in range(50):#this will loop spenver chats spam responces 50 times
                        randSpam = random.randrange(0, 19)#generating random number to randomly choose spencer chat line
                        if randSpam == 4:
                                await message.channel.send("Well too bad! Stairs, stairs, stairs!")
                        if randSpam == 1:
                                await message.channel.send("You're grounded for... till college!")
                        if randSpam == 2:
                                await message.channel.send("Haha, look! His arm came off!")
                        if randSpam == 3:
                                await message.channel.send("Why? Is Santa Clause here to tell me I'm ugly and have no freinds?")
                        if randSpam == 5:
                                await message.channel.send("Don't say pie for breakfast, say PIE FOR BREAKFAST!")
                        if randSpam == 6:
                                await message.channel.send("I once met a freaky rabi in vegas.")
                        if randSpam == 7:
                                await message.channel.send("Look, in my life, I've learned a few things about girls. Like, when you break up with them, they do not like it when you ask out their sisters. That will get you a fork in your arm.")
                        if randSpam == 8:
                                await message.channel.send("I told you to breathe through the tube! Oh wait... I forgot the tube.")
                        if randSpam == 9:
                                await message.channel.send("She has magic feet!")
                        if randSpam == 10:
                                await message.channel.send("Those Thalia-manians taught you good.")
                        if randSpam == 11:
                                await message.channel.send("Toasty!")
                        if randSpam == 12:
                                await message.channel.send("Don't worry, Toasty. Soon you'll be back and butter than ever!")
                        if randSpam == 13:
                                await message.channel.send("So? It's a pie shop, not a church.")
                        if randSpam == 14:
                                await message.channel.send("I made it into a squirrel")
                        if randSpam == 15:
                                await message.channel.send("It's not just that. Last week on a bus, a hobo spilled chili on me, then continuted to eat it... without a spoon!")
                        if randSpam == 16:
                                await message.channel.send("Behold the sign! Are you beholding it?")
                        if randSpam == 17:
                                await message.channel.send("Well, I'm cooking/I'm cooking things/Cooking things for people to eat/I'm cooking/I'm cooking things/Things that people will chew.")
                        if randSpam == 18:
                                await message.channel.send("If you're looking for a fun creative guy, well, you just took a right turn down lucky street. Why don't you go ahead and put it in park? Send me an email. Write it, click it, send it...")
                        time.sleep(10)#tell loop to sleep for 10s so it doesnt go to fast/so discord cant give us shit for being a spam bot
            #reactions for when hey gibby is triggered - when gibby says one of his quotes, spencer will respond based on what gibby says
            if str(message.content).lower() == "my mom thinks i'm awesome!":
                await message.channel.send("Thats what she said!")
            if str(message.content).lower() == "ahhhh! don't! i'm just a gibby!":
                await message.channel.send("Well I'm just a Spencer!")
            if str(message.content).lower() == "i'm the statue of gibberty!":
                await message.channel.send("And I'm the statue of Attractive men!")
            if str(message.content).lower() == "i couldn't find the tube!":
                await message.channel.send("I told you to breathe through the tube! Oh wait... I forgot the tube.")
            if str(message.content).lower() == "what am i? a mushroom?":
                await message.channel.send("No I'm a frog!")
            if str(message.content).lower() == "what are you? a cop?":
                await message.channel.send("Officer Spencer here at your servi... oh look! A squirrel!")
            if str(message.content).lower() == "this pudding rocks!":
                await message.channel.send("Why is your pudding rocks?!")
            if str(message.content).lower() == "wow... umm. i'm in love with this sauce. what is it?":
                await message.channel.send("Its a sauce a hobo gave me!")
            if str(message.content).lower() == "i invented cheesecake!":
                await message.channel.send("But have you had pie?")
            if str(message.content).lower() == "oh really? i have that too!": 
                await message.channel.send("I made it into a squirrel!")

@bot.event
async def on_ready():
    print('\nLogged in as:')#debug info stated when bot starts in cli
    print(" Username",bot.user.name)
    print(" User ID",bot.user.id)
    print("To invite the bot in your server use this link:\n https://discordapp.com/oauth2/authorize?&client_id="+str(bot.user.id)+"&scope=bot&permissions=0")

def run_client(token):
    global bot
    
    print("Starting at time",str(datetime.datetime.now()))
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(bot.start(token))
    except Exception as e:
        print("Error", e)
        loop.run_until_complete(bot.logout())
        
if __name__ == "__main__":
            
    run_client(config.discordtoken)
