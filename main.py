import discord
from discord.ext import commands
import os
import random
# import requests 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Dan inilah cara Kamu mengganti nama file dari variabel!

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')
@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('img'))
    with open(f'img/{img_name}', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

organik = ["daun", "sisa makanan", "kayu", "ranting", "buah"]
anorganik = ["plastik", "kaca", "limbah masyarakat", "botol", "besi"]

@bot.command()
async def pilih(ctx, *sampah):
    temp = " ".join(sampah)
    # msg = await bot.wait_for("message")

    if temp in organik:
        await ctx.send("Masukkan ke sampah organik")
    elif temp in anorganik:
        await ctx.send("Masukkan ke sampah anorganik")


bot.run("TOKEN")