import discord
from discord import app_commands
from discord.ext import commands
import os
import Droller

secret_code = os.getenv('DB_TOKEN')
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


class db(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=1100490695309017168))
        self.synced = True
        print('Bot is Online')


bot = db()
tree = app_commands.CommandTree(bot)


@tree.command(name='dice_box', description='tells user what types of dice they can roll', guild=discord.Object(id=1100490695309017168))
async def self(interaction: discord.Interaction):
    await interaction.response.send_message('dice')

bot.run(secret_code)