import discord  
import time
from datetime import date

token = "OTcyMjMzMDY4Mzg1NTU0NTU1.YnWEmg.jQC1ZcGHDwOBLjbTBy7k10RFzaA"

client = discord.Client()

@client.event
async def on_ready():
    print("{0.user} je na drate".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    if message.author.id == 643440819713343488:
        channel = client.get_channel(966422290801786990)
        await channel.send("drz hubu")


    elif message.content.startswith("!dny") or message.content.startswith("/dny"):
        await cas()
        
    elif message.content.startswith("!mogus"):
        channel = client.get_channel(966422290801786990)
        await channel.send(file=discord.File('C:\gay.png'))
    
    elif message.content.startswith("!petrkokot"):
        channel = client.get_channel(966422290801786990)
        await channel.send(file=discord.File('C:\selfie.png'))

    elif message.content.startswith("!kostka"):
        channel = client.get_channel(966422290801786990)
        import random
        n = random.randint(1,6)
        await channel.send(n)




def datum():
    while True:
        today = date.today()
        if str(today) == "2022-07-01":
            channel = client.get_channel(966422290801786990)
            channel.send('leto zmrde')
        print("Today's date:", today)

async def cas():
    today = date.today()
    d0 = today
    d1 = date(2022, 7, 1)
    delta = d1 - d0
    print(delta.days)
    channel = client.get_channel(966422290801786990)
    await channel.send(str(delta.days) + " dni zbyva do prazdin zmrde ")
client.run(token)
