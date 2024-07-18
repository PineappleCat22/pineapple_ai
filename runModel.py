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

    prompt = f"{prompt}\nYou respond:"
    messages.append({'role': 'user', 'content': prompt},)
    response = ollama.chat(model=modelName, messages=messages)['message']['content']
    messages.append({'role': 'assistant', 'content': response},)
    return response

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