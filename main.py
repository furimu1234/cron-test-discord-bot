from discord.ext import commands
import discord

import os

TOKEN = os.environ.get("TOKEN", "")

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!!!", intents=discord.Intents.all())

    
    async def on_ready(self):
        if not self.user:
            return

        print(f"{self.user.display_name}起動完了")
    

if __name__== "__main__":
    bot = Bot()
    bot.run(TOKEN)

