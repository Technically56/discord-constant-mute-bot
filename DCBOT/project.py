# bot.py
import discord.ext.commands
import os
import time
import discord
import asyncio
TOKEN = "bottoken"

intents1 = discord.Intents.all()



client = discord.Client(intents = intents1)
guild = "servername"
mutemod = int(input("Please Select A Mute Mode: \n"))
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    global uid
    
    await client.change_presence(status=discord.Status.offline)
    if mutemod == 3:
        global channel
        global message
        global counter
        message = str(input("Please enter the message you want repeated: \n"))
        channel = client.get_channel(int(input("Please Enter Channel Id(accessible via right clicking a channel with developer mode enabled): \n")))
        counter = int(input("Please enter how many repetitions you want: \n"))        
        for i in range(counter):
            await channel.send(message)
    elif mutemod != 3:
        uid = int(input("Please enter the user id(accessible via right clicking a channel with developer mode enabled): \n"))
@client.event
async def on_voice_state_update(member, before, after):
    if mutemod != 3:
        guild = member.guild
        user_id = guild.get_member(uid)
        if member == user_id and mutemod == 1:
            await member.edit(mute=True)
            print(member,"muted.")
            asyncio.sleep(1)
        elif member == user_id and mutemod ==0:
            await member.move_to(None)
            print(member,"disconnected")
        elif member == user_id and mutemod == 2:
            loop = asyncio.get_event_loop()
            async def mute():
                await member.edit(deafen=True)
                await member.edit(mute=True)
                await asyncio.sleep(1)
            async def kick():        
                await member.move_to(None)
                await asyncio.sleep(1)
            async def main():
                f1 = loop.create_task(mute())
                f2 = loop.create_task(kick())
                await asyncio.wait([f1,f2])
            loop.run_until_complete(main())
            loop.close()
            print(member,"server muted, deafened and disconnected")       
       
             
client.run(TOKEN)

