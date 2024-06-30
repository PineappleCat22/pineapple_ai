import discord
import runModel as model
import tokenizer

tkn = tokenizer.Tokenizer() #hey i dont know why this is necessary
with open('botToken') as f:
    TOKEN = f.readline()
testmode = 1
#test mode 0: normal usage
#test mode 1: ai disabled, bot returns the model input, tokens, and token length.

intents = discord.Intents.default()
intents.message_content = True #only good intentions

#idk how to read documentation!!!! try to do the addition thing lmao.

class MyClient(discord.Client):
    try:
        async def on_ready(self):
            print(f'{self.user} initialized successfully')
            print("test mode:", testmode)
            model.debug()
    except Exception as e:
        print("Something went horribly wrong while initializing.")
        print(e)

    async def on_message(self, message):
        if message.author == self.user:
            return  # Ignore messages from the bot itself

        if self.user.mentioned_in(message):
            if testmode == 1:
                try:
                    messageStr = message.content.replace("<@437414611369721856>", f"{message.author.name} says:")
                    messageEncoded = tkn.encode(s=messageStr, eos=False, bos=False)
                    await message.channel.send(messageStr)
                    await message.channel.send(f"tokens: {messageEncoded}")
                    await message.channel.send(f"token length: {len(messageEncoded)}")
                except Exception as e:
                    await message.channel.send("Something went horribly wrong while parsing a message from a user.")
                    await message.channel.send(e)
            elif testmode == 0:
                try:
                    messageStr = message.content.replace("<@437414611369721856>", f"{message.author.name} says:")
                    await message.channel.send(model.query(messageStr)) #parse this into the ai and print its response.
                except Exception as e:
                    await message.channel.send("Something went horribly wrong while trying to send something to the AI.")
                    await message.channel.send(e)
            else:
                await message.channel.send("testmode error. what the fuck is going on. im gonna kill myself.")
                await message.channel.send(testmode)
                quit() #this throws a lot of errors. but it accomplishes what it needs to.

#i dont know why all the awaits are here, but it fucking explodes if they arent there.

client = MyClient(intents=intents) #how the fuck does this work
client.status = discord.Status.idle #cool flavor stuff
client.activity = discord.CustomActivity("coding an ai duplicate of myself")
client.run(TOKEN)
