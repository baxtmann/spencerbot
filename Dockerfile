FROM python:latest

RUN echo "YOU MUST ENTER BOT TOKEN BEFORE RUNNING DOCKER!!"

ADD . / spencerbot/

RUN cd spencerbot/

RUN apt-get update

RUN apt-get install -y software-properties-common git

RUN pip3 install python-dotenv

RUN pip3 install -U git+https://github.com/Pycord-Development/pycord

RUN echo "SpencerBot TOKEN = ""$SPENCER_TOKEN" >> .env

CMD [ "python", "./spencerbot/spencer.py" ]