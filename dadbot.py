from maubot import Plugin, MessageEvent
from maubot.handlers import command
from typing import List, Tuple
from random import choice

class DadBot(Plugin):
    @command.passive(r"\bi['’]?m\s+(\w+)", case_insensitive=True) ## return word after im 
    async def handler(self, evt: MessageEvent, match: tuple) -> None:
        await evt.mark_read()
        self.log.debug(f"dadbot matched {match}")
        ## check for word
        if match[1] != None: ## check group 1
            result = f"Hi {match[1]} I'm Dadbot"
        else:
            result = f"Hi ERROR I'm Dabdort"
        await evt.reply(result, allow_html=True)
    
    @command.new("validation")
    async def validation_handler(self, evt: MessageEvent) -> None:
        dad_praise = [
            f"I'm proud of you Son.",
            f"I love you Son.",
            f"The day you were born was the happiest day of my life.",
            f"You make me so proud.",
            f"*hug*",
            f"Good job, sport!",
            f"It's ok to make mistakes, I still love you Son.",
            f"I'm always here for you Son.",
        ]
        praise = f"{choice(dad_praise)}"
        await evt.reply(praise, allow_html=True)

    @command.new("joke")
    async def joke_handler(self, evt: MessageEvent) -> None:
        dad_jokes = [
            f"My wife is really mad at the fact that I have no sense of direction. So I packed up my stuff and right.",
            f"How do you make holy water? You boil the hell out of it.",
            f"I bought some shoes from a drug dealer. I don't know what he laced them with, but I was tripping all day!",
            f"Did you know the first French fries weren't actually cooked in France? They were cooked in Greece.",
            f"I'm reading a book about anti-gravity. It's impossible to put down!",
            f"What do you call someone with no body and no nose? Nobody knows.",
            f"A slice of apple pie is $2.50 in Jamaica and $3.00 in the Bahamas. These are the pie rates of the Caribbean.",
            f"Justice is a dish best served cold, if it were served warm it would be justwater.",
            f"Why can't you hear a pterodactyl go to the bathroom? Because the pee is silent.",
            f"What did the drummer call his twin daughters? Anna one, Anna two!",
            f"What’s Forrest Gump’s password? 1forrest1",
            f"Want to hear a joke about construction? I'm still working on it.",
            f"Does anyone need an ark? I Noah guy!",
            f"I wanted to go on a diet, but I feel like I have way too much on my plate right now.",
            f"To whoever stole my copy of Microsoft Office, I will find you. You have my Word!",
            f"Which bear is the most condescending? A pan-duh!",
            f"What kind of noise does a witch’s vehicle make? Brrrroooom, brrroooom.",
            f"What’s brown and sticky? A stick.",
            f"Two guys walked into a bar. The third guy ducked.",
            f"How do you get a country girl’s attention? A tractor.",
            f"Why are elevator jokes so classic and good? They work on many levels.",
            f"What do you call a pudgy psychic? A four-chin teller.",
            f"What did the police officer say to his belly-button? You’re under a vest.",
            f"What do you call it when a group of apes start a company? Monkey business.",
            f"My wife asked me to stop singing “Wonderwall” to her. I said maybe –",
            f"What did Tennessee? The same thing as Arkansas.",
        ]
        joke = f"{choice(dad_jokes)}"
        await evt.reply(joke, allow_html=True)