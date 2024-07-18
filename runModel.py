import ollama

messages = []

def query(prompt, modelName='llama3'):
    #look ma, i can write documentation!
    """
    initialize and query a specified ai model. probably put this in a repl. also handles default system prompts on its own based on modelname, but specifying one overrides it.\n
    available models:\n
    llama3 - meta's standard llama 3 model\n
    Pineapple-AI-Vwhatever - fine tuned model to mimic behaviors based on the dev's discord messages.\n
    DAVE-Vwhatever - fine tuned model to mimic behaviors based on dialog from a Homestuck character. (NOT IMPLEMENTED)
    :param prompt: prompt
    :param modelName: (optional) ai model name, defaults to Meta-Llama-3-8B.
    :return: ai response as a string
    """
    """['Traceback (most recent call last):\n', '  File "/home/pineapple/pineapple_ai/start.py", line 35, in sendMsg\n    if len(msg) > 2000:\n       ^^^^^^^^\n', "TypeError: object of type 'coroutine' has no len()\n"]
/home/pineapple/pineapple_ai/start.py:70: RuntimeWarning: coroutine 'query' was never awaited
  await sendMsg(model.query(messageStr, modelName="pineapple-ai-v1.2")) #okay. this works, but i dont know why. i wont touch it
RuntimeWarning: Enable tracemalloc to get the object allocation traceback"""
    # I DUNNO WHATS CAUSING THIS
    # I DONT HAVE ENOUGH THINKING ABILITYT TO FIX IT.

    #prompt stage

    prompt = f"{prompt}\nYou respond:"
    print(f"AI PROMPT SENT: {prompt}")
    print("NOW WE APPEND THAT TO THE messages STACK")
    messages.append({'role': 'user', 'content': prompt},)
    print("OK QUERYING THE AI NOW")
    response = ollama.chat(model=modelName, messages=messages)['message']['content']
    print(f"AI RESPONDED WITH {response}")
    print("ADDING RESPONSE TO MESSAGE STACK")
    messages.append({'role': 'assistant', 'content': response},)
    return response

def debug():
    print("runModel exists hooray")

if __name__ == "__main__":
    print("TEST INSTANCE INITIALIZED. 'exit' TO QUIT. RUNNING MODEL IS META-LLAMA-3-8B")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        RSP = query(user_input)
        print("bot:", RSP) #haha sex
        print(messages)