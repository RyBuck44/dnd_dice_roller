import discord
from discord import app_commands
from discord.ext import commands
import os
from Droller import coin_flip, d_roller

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


@tree.command(name='help', description='prompts the beginning of the rolling process', guild=discord.Object(id=1100490695309017168))
async def self(interaction: discord.Interaction):
    await interaction.response.send_message('Please enter all the dice you want me to roll. \n'
                                            'Currently I have D20s, D12s, D10s, D8s, D6s, D4s. \n'
                                            'I can also flip a coin using ** /flip **. \n'
                                            'To start rolling, see the format below and use ** /roll **\n'
                                            'Please use this format: numddie. \n'
                                            'EX: 2d4,4d12,7d8')


@tree.command(name='flip', description='flips a coin', guild=discord.Object(id=1100490695309017168))
async def self(interaction: discord.Interaction):
    outcome = coin_flip()
    await interaction.response.send_message(f"Ahh the old two sided die! \n"
                                            f"Here's what I got: {outcome}")


@tree.command(name='roll', description='rolls selected dice', guild=discord.Object(id=1100490695309017168))
async def self(interaction: discord.Interaction, dice:str):
    available_dice = [
        4,
        6,
        8,
        10,
        12,
        20,
    ]
    all_dice = dice.split(',')
    total_number = []
    for dice in all_dice:
        d = dice.split('d')
        die = int(d[1])
        rolls = int(d[0])
        if die in available_dice:
            total = d_roller(die, rolls)
            total_number.append(total)
        else:
            break
    all_roles = []
    for sublist in total_number:
        for item in sublist:
            all_roles.append(item)
    final_number = sum(all_roles)
    await interaction.response.send_message(f"Dice rolled: {all_dice}\n"
                                            f"Here's all your rolls: {all_roles}\n"
                                            f"Here's the total: {final_number}")


def run_Dice_bot():
    bot.run(secret_code)


run_Dice_bot()