import asyncio

from highrise import *
from highrise import BaseBot, Position, __main__
from highrise.models import *
from highrise.models import (
    Position,
    SessionMetadata,
)

from webserver import keep_alive

name_ad = ["haitham783"]
class BotDefinition:
    def __init__(self, bot, room_id, api_token):
      self.bot = bot
      self.room_id = room_id
      self.api_token = api_token
      


class MyBot(BaseBot):

    def __init__(self, bot, room_id, api_token):
      self.bot = bot
      self.room_id = room_id
      self.api_token = api_token
      
    
    



    async def on_start(self, session_metadata: SessionMetadata) -> None:
      print("hi im alive?")
      try:
        await self.highrise.walk_to( Position(x=15.5, y=0.5, z=22.0, facing='FrontRight'))
      except Exception as e:
        print(f"An exception occurred: {e}")



    





    

      # If no matching function is found
      

    
    

    async def run(self):
      while True:  
         try:
           definitions = [BotDefinition(self, self.room_id, self.api_token)]
           await __main__.main(definitions)
         except Exception as e:
           print(f"An exception occourred: {e}")

keep_alive()
if __name__ == "__main__":
    room_id = "65580096bd12e53ae7c3a64d"
    token = "e90a475c8ffd5d3df0ffb6f3cbbe50f8307e092768a3bcdd6e60d81a167373ff"
    bot = Highrise() 
    bot_instance = MyBot(bot, room_id, token)
    asyncio.run(bot_instance.run())
