import asyncio
import importlib.util
import os
import random

from highrise import *
from highrise import BaseBot, Position, User, __main__
from highrise.models import *
from highrise.models import (
    Item,
    Position,
    SessionMetadata,
    User,
)
import random
from webserver import keep_alive


MESSAGES = ["its nice of you enter","keep it up","everyone welcome"]


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


  MESSAGES = ["Welcome to the room.its nice of you enter"]
  greetings = [ "Welcome to the room.its nice of you enter"

      # ... (ترحيبات أخرى هنا)
  ]






  message_count = {}

  async def send_periodic_message(self):
    try:
      while True:
        message = random.choice(MESSAGES)
        await self.highrise.chat(message)
        await asyncio.sleep(50)  # 2 minutes
    except Exception as e:
      print(f"An exception occurred: {e}")
  async def on_user_move(self, user: User, pos: Position) -> None:
    print(f"{user.username} moved to {pos}")

  async def on_start(self, session_metadata: SessionMetadata) -> None:
    print("[Start]")
    try:
       await self.highrise.walk_to( Position(x=15.5, y=0.5, z=26.0, facing='FrontRight'))



    except Exception as e:
        print(f"Error in on_start: {e}")

    send_task = asyncio.create_task(self.send_periodic_message())
    await asyncio.gather(send_task)






  async def on_chat(self, user: User, message: str) -> None:


    if message.lower().startswith("/dress") and user.username == "haitham783":
      await self.highrise.set_outfit(outfit=[
        Item(type='clothing',
             amount=1,
             id='body-flesh',
             account_bound=False,
             active_palette=1),
        Item(type='clothing',
             amount=3,
             id='hair_front-n_basic2018straightlowsidepart',
             account_bound=False,
             active_palette=3),
        Item(type='clothing',
           amount=3,
           id='face_hair-n_newbasicfacehairupper07',
           account_bound=False,
           active_palette=3),
        Item(type='clothing',
         amount=3,
         id='face_hair-n_newbasicfacehairlower12',
         account_bound=False,
         active_palette=3),

        Item(type='clothing',
             amount=3,
             id='eyebrow-n_basic2018newbrows16',
             account_bound=False,
             active_palette=3),
        Item(type='clothing',
             amount=1,
             id='mouth-basic2018unimpressed',
             account_bound=False,
             active_palette=1),
        Item(
            type='clothing',
            amount=1,
            id='nose-n_room22019nosestud',
        ),
        Item(type='clothing',
             amount=1,
             id='shirt-f_marchingband',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='pants-n_starteritems2019cuffedjeansblack',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='shoes-n_room12019bootsblack',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=3,
             id='eye-n_basic2018malediamondsleepy',
             account_bound=False,
             active_palette=3),

        Item(type='clothing',
             amount=1,
             id='hair_back-n_malenew06',
             account_bound=False,
             active_palette=1),
    ])





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
