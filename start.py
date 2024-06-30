import discord

with open('botToken') as f:
    TOKEN = f.readline() #to keep my token out of malicious hands.

intents = discord.Intents.default()
intents.message_content = True #only good intentions

#idk how to read documentation!!!! try to do the addition thing lmao.

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} ready to fuck around and find out yeehaw')

    async def on_message(self, message):
        if message.author == self.user:
            return  # Ignore messages from the bot itself

        if self.user.mentioned_in(message):
            await message.channel.send(message.content.replace("<@437414611369721856>", message.author.mention))
            print(message.content) # learning how to handle input. change this to support user input.


client = MyClient(intents=intents) #how the fuck does this work
client.status = discord.Status.idle #cool flavor stuff
client.activity = discord.CustomActivity("coding an ai duplicate of myself")
client.run(TOKEN)
