import configparser
import os, sys

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)
	
config = configparser.ConfigParser()

config.read(str(application_path)+'/config.ini')

discordtoken = config['SETTINGS']['discordtoken'].strip()