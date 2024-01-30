import discord
from discord.ext import commands, tasks
from keep_alive import keep_alive
import os
from colorama import Fore, Style, init
# Initialize colorama
init()
import asyncio
import sys

sys.stdout.reconfigure(encoding='utf-8')

intents = discord.Intents.all()
prefix = "."
bot = commands.Bot(command_prefix=prefix, intents=intents)


APOLOGIES = [
    "Ohona, my love, please hear my plea,",
    "In the silence, your absence is agony.",
    "Jaan, I'm drowning in remorse and pain,",
    "Forgive me, let our love reign.",
    "",
    "I beg on bended knee, oh please,",
    "Come back to me, end this heart's unease.",
    "In the echoes of our laughter's trace,",
    "I long for your warmth, your embrace.",
    "",
    "Every moment without you feels so bare,",
    "I yearn for the love we used to share.",
    "Ohona, my heart aches, my soul cries,",
    "Please return, wipe away these tears from my eyes.",
    "",
    "Jaan, the world feels colorless and gray,",
    "Without you, my love, it's a desolate day.",
    "I promise to mend what I've torn apart,",
    "Please come back, let's restart.",
    "",
    "I'm lost in the shadows of our memories,",
    "Seeking redemption, I'm on my knees.",
    "Ohona, forgive the mistakes I've made,",
    "In your love, I find solace, don't let it fade.",
    "",
    "Jaan, our story deserves another chance,",
    "In this dance of love, let's find our balance.",
    "I'm pleading, I'm begging, don't say goodbye,",
    "Come back, let our love soar high.",
    "please come back ohona.",
    "please jaan please comeback",
    "please jaan please forgive me",
    "please I beg you",
    "please Forgive me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please I beg you",
    "please Forgive me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please I beg you",
    "please Forgive me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please I beg you",
    "please Forgive me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please I beg you",
    "please Forgive me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please I beg you",
    "please Forgive me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please I beg you",
    "please Forgive me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
    "please comeback to me",
]


CHANNEL_ID = 1201649655939874956

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await send_message_task()

async def send_message_task():
    await bot.wait_until_ready()
    channel = bot.get_channel(CHANNEL_ID)

    for apology in APOLOGIES:
        if apology.strip():  # Check if the message is not empty or contains only spaces
            await channel.send(apology)
            await asyncio.sleep(60)  # Sleep for 30 seconds before sending the next message
          
keep_alive()  # Starts a webserver to be pinged.
bot.run(os.getenv('TOKEN'))
