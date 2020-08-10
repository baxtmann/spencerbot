# Spencerbot

Spencerbot is a Discord bot written in python that will return various spencer-related responces!
This bot is completly open source, feel free to do whatever you want with it! My only request is that if you do anything cool with it, I want to hear about it! Shoot me a tweet @BrandonAxtmann or email me at baxtmann@jumpstartlabs.co

## Commands for SpencerBot
See the below commands that are available in the current version of Spencerbot. If you have any suggestions for other commands, create a suggestion on Github!
*Note* The command prefix for the bot is "!", but this bot currently does not use the command prefix. The bot checks every message sent to see if it matched any of the criteria it is seaching for.
### spencer
When spencer is stated, the bot will post a randomly chosen gif out of a list of 7 spencer related gifs. Gifs are hosted on https://edge.baxtmann.me (gifs to be uploaded to github soon)
### hey spencer
when hey spencer is triggered, the bot will post a quote spencer has said in chat. There is 18 options spencer can post. 
### who is your daddy
when who is your daddy is triggered, the bot will state who the bots creator is
### spencer talk
when spencer talk is triggered, spencer will use the same quotes from hey spencer but will post a total of 50 quotes (aka spam mode). Both gibbybot and spencerbot have spam mode, and whenever one of 10 quotes are stated, gibbybot will react with a specific message for each of the random messages sent.

## Getting Started
### Linux (Ubuntu)
1. Install Python3 & PIP3
2. Install dependencies - 'pip install -r reqirements.txt'
3. Give permissions to start.py - 'sudo chmod 777 start.py'
4. Install dos2unix to convert start.py to run on unix - 'sudo apt-get install dos2unix'
5. Convert file for dos2unix - 'sudo dos2unix start.py'
4. Open config.ini to add bot token 'sudo nano config.ini' - input discord bot token into file
5. Run discord bot - './start.py' once running, do not exit out of bot as that will stop it. You can run bot in a screen session to allow it to run in the background

To run in a screen session: 
1. Install screen - 'sudo apt-get install screen'
2. Start screen - 'screen -S Gibbybot'
3. Start bot in screen session - './start.py'
4. Exit screen - 'ctrl + a + d'

### Windows Guide TBA

If you have any issues running spencerbot, or have any questions, feel free to open an issue and I will try to help you out!

# And don't forget to check out [gibbybot](https://github.com/baxtmann/Gibbybot)! 
