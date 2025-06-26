
import discord
from discord.ext import commands, tasks
import random
import os

TOKEN = os.getenv("TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))
ROLE_ID = int(os.getenv("ROLE_ID"))

intents = discord.Intents.default()
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    change_color.start()

@tasks.loop(seconds=5)  # Change every 5 seconds
async def change_color():
    guild = bot.get_guild(GUILD_ID)
    if not guild:
        print("Guild not found.")
        return
    role = guild.get_role(ROLE_ID)
    if not role:
        print("Role not found.")
        return

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    await role.edit(color=discord.Color.from_rgb(r, g, b))
    print(f"Changed role color to RGB({r}, {g}, {b})")

bot.run(TOKEN)
