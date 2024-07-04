import discord
import runModel as model
import tokenizer
import datetime as time
import traceback

tkn = tokenizer.Tokenizer() #hey i dont know why this is necessary
with open('/home/pineapple/pineapple_ai/botToken') as f:
    TOKEN = f.readline()
testmode = 0
#test mode 0: normal usage
#test mode 1: ai disabled, bot returns the model input, tokens, and token length.
#test mode 2: test the typing feature. thats it.

intents = discord.Intents.default()
intents.message_content = True #only good intentions

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
        async def sendMsg(*msgs):
            for msg in msgs:
                try:
                    if len(msg) > 2000:
                        await message.channel.send(f"aw fuck something went wrong while sending a message.\n<@189034549789851648> HEY SHITHEAD SOMETHING IS FUCKED.\nmessage send error: message longer than 2000 chars\ntime: {time.datetime.now()}")
                        print("======================================== THIS IS WHERE THE MESSAGE SEND ERROR OCCURRED =========================")
                        print(f"message: {msg}\n length: {len(msg)}\n time: {time.datetime.now()}")
                    else:
                        await message.channel.send(msg)
                except Exception as e2:
                    print(f"SOMETHING EVEN WORSE HAPPENED WHILE SENDING A MESSAGE.\n{traceback.format_exception(e2)}")


        if message.author == self.user:
            return  # Ignore messages from the bot itself

        if self.user.mentioned_in(message):
            if testmode == 1:
                try:
                    messageStr = message.content.replace("<@437414611369721856>", f"{message.author.name} says:")
                    messageEncoded = tkn.encode(s=messageStr, eos=False, bos=False)
                    await sendMsg(
                        messageStr,
                        f"tokens: {messageEncoded}",
                        f"token length: {len(messageEncoded)}")
                except Exception as e:
                    await sendMsg(
                        "aw fuck. message parse error.",
                        e)
            elif testmode == 0:
                try:
                    messageStr = message.content.replace("<@437414611369721856>", f"{message.author.name} says:")
                    async with message.channel.typing():
                        await sendMsg(model.query(messageStr, modelName="pineapple-ai-v1.1")) #todo: improve this later
                except Exception as e:
                    await sendMsg(
                        "aw fuck. ai query error.",
                        traceback.format_exception(e))
            else:
                await sendMsg(
                    "testmode error. what the fuck is going on. im gonna kill myself.",
                    testmode)
                quit() #this throws a lot of errors. but it accomplishes what it needs to.

#i dont know why all the awaits are here, but it fucking explodes if they arent there.
#this code is so bad it would probably be a severe liability if it didnt run a silly little bot.

client = MyClient(intents=intents) #how the fuck does this work
client.status = discord.Status.idle #cool flavor stuff
client.activity = discord.CustomActivity("coding an ai duplicate of myself")
client.run(TOKEN)
