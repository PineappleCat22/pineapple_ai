import discord
import runModel as model
import tokenizer
from datetime import datetime
import traceback
import asyncio
from concurrent.futures import ThreadPoolExecutor
import time

tkn = tokenizer.Tokenizer()
with open('/home/pineapple/pineapple_ai/botToken') as f:
    TOKEN = f.readline()
testmode = 2
#test mode 0: normal usage
#test mode 1: ai disabled, bot returns the model input, tokens, and token length.
#test mode 2: prints ai response time after message.
executor = ThreadPoolExecutor()
intents = discord.Intents.default()
intents.message_content = True
modelName = "pineapple-ai-v1.4"

class MyClient(discord.Client):
    try:
        async def on_ready(self):
            #technically you shouldnt do any of this here
            async def set_status():
                i = 1
                while True: #so fucking cringe...
                    def query_ai_for_status(): # DEFS INSIDE DEFS INSIDE DEFS INSIDE DEFS INSIDE DEFS INSIDE DEFS INSIDE DEFS INSIDE DEFS INSIDE DEFS INSIDE DEFS INSIDE ...
                        #return model.query("Describe what you are doing in ten words or less.", modelName)
                        return "balls"
                    loop = asyncio.get_event_loop()
                    status_message = await loop.run_in_executor(executor, query_ai_for_status)
                    await self.change_presence(status=discord.Status.idle, activity=discord.CustomActivity(status_message))
                    await asyncio.sleep(60)
                    print(f"status changed {i} times")
                    i += 1
            asyncio.run(set_status()) #this is fucking goofy.
            print(f'{self.user} initialized successfully')
            print("test mode:", testmode)

    except Exception as e:
        print("Something went horribly wrong while initializing.")
        print(e)

    async def on_message(self, message):

        async def sendMsg(*msgs):
            for msg in msgs:
                msg = str(msg)
                if len(msg) > 2000:
                    await message.channel.send(f"aw fuck something went wrong while sending a message.\n<@189034549789851648> HEY SHITHEAD SOMETHING IS FUCKED.\nmessage send error: message longer than 2000 chars\ntime: {datetime.now()}")
                    print("======================================== THIS IS WHERE THE MESSAGE SEND ERROR OCCURRED =========================")
                    print(f"message: {msg}\n length: {len(msg)}\n time: {datetime.now()}")
                    return
                else: message.channel.send(msg)

        async def replyMsg(*msgs):
            for msg in msgs:
                msg = str(msg)
                if len(msg) > 2000:
                    await message.reply(f"aw fuck something went wrong while sending a message.\n<@189034549789851648> HEY SHITHEAD SOMETHING IS FUCKED.\nmessage send error: message longer than 2000 chars\ntime: {datetime.now()}")
                    print("======================================== THIS IS WHERE THE MESSAGE SEND ERROR OCCURRED =========================")
                    print(f"message: {msg}\n length: {len(msg)}\n time: {datetime.now()}")
                    return
                else: await message.reply(msg)

        if message.author == self.user:
            return  # Ignore messages from the bot itself

        if self.user.mentioned_in(message):
            if testmode == 2:
                try:
                    messageStr = f"{message.author.name} says: " + message.content.replace("<@437414611369721856>", "").strip()
                    start = time.time()
                    async with message.channel.typing():
                        loop = asyncio.get_event_loop()
                        AIMsg = await loop.run_in_executor(executor, model.query, messageStr, modelName)
                        await replyMsg(AIMsg)
                    end = time.time()
                    await replyMsg(f"Elapsed time: {time.strftime('%H:%M:%S', time.gmtime(end - start))}")
                except Exception as e:
                    await replyMsg(
                        "aw fuck. ai query error.",
                        ''.join(traceback.format_exception(e)))

            elif testmode == 1:
                try:
                    messageStr = f"{message.author.name} says: " + message.content.replace("<@437414611369721856>", "").strip()
                    messageEncoded = tkn.encode(s=messageStr, eos=False, bos=False)
                    await replyMsg(
                        messageStr,
                        f"tokens: {messageEncoded}",
                        f"token length: {len(messageEncoded)}")
                except Exception as e:
                    await replyMsg(
                        "aw fuck. message parse error.",
                        e)

            elif testmode == 0:
                try:
                    messageStr = f"{message.author.name} says: " + message.content.replace("<@437414611369721856>", "").strip()
                    async with message.channel.typing():
                        loop = asyncio.get_event_loop()
                        AIMsg = await loop.run_in_executor(executor, model.query, messageStr, modelName)
                        await replyMsg(AIMsg)
                except Exception as e:
                    await replyMsg(
                        "aw fuck. ai query error.",
                        ''.join(traceback.format_exception(e)))

            else:
                await sendMsg(
                    "testmode error. what the fuck is going on. im gonna kill myself.",
                    testmode)
                quit() #this throws a lot of errors. but it accomplishes what it needs to.

client = MyClient(intents=intents)
client.status = discord.Status.idle
client.activity = discord.CustomActivity("BOOTING UP...")
client.run(TOKEN)

#TODO: add more shit to the system prompt?
#TODO: tell it to omit unnecessary details.
#TODO: tell it the distinction between asexual and aromantic?
#TODO: ai gets repetetive sometimes?