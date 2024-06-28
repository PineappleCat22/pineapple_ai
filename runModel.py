from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def query(prompt, max_length=300, systemPrompt="You are an AI currently speaking to your creator.", modelName='Meta-Llama-3-8B'):
    #look ma, i can write documentation!
    """
    initialize and query a specified ai model. probably put this in a repl. also handles default system prompts on its own based on modelname, but specifying one overrides it.\n
    available models:\n
    Meta-Llama-3-8B - meta's standard llama 3 model\n
    Pineapple-AI-Vwhatever - fine tuned model to mimic behaviors based on the dev's discord messages. (NOT IMPLEMENTED)\n
    DAVE-Vwhatever - fine tuned model to mimic behaviors based on dialog from a Homestuck character. (NOT IMPLEMENTED)
    :param prompt: input prompt.
    :param max_length: num of tokens accepted.
    :param systemPrompt: (optional) system prompt.
    :param modelName: (optional) ai model name, defaults to Meta-Llama-3-8B.
    :return: ai response as a string
    """

    #handle presets
    #Meta preset: "You are an AI currently speaking to your creator."
    #Pineapple preset: "You are a really cool dude currently speaking to your really cool friend." (CHANGEME)
    #Dave preset: "Your name is DAVE STRIDER. It is an UNSEASONABLY WARM April day. Your BEDROOM WINDOW is open to let some air in, and your FAN is cranked. Arguably even more cranked would be your FLY BEATS, which brings us to your variety of INTERESTS. A cool dude like you is sure to have plenty. You have a penchant for spinning out UNBELIEVABLY ILL JAMS with your TURNTABLES AND MIXING GEAR. You like to rave about BANDS NO ONE'S EVER HEARD OF BUT YOU. You collect WEIRD DEAD THINGS PRESERVED IN VARIOUS WAYS. You are an AMATEUR PHOTOGRAPHER and operate your own MAKESHIFT DARKROOM. You maintain a number of IRONICALLY HUMOROUS BLOGS, WEBSITES, AND SOCIAL NETWORKING PROFILES. And if the inspiration strikes, you won't hesitate to drop some PHAT RHYMES on a mofo and REPRESENT. Your typing style is no capitalization UNLESS STRESSING OR EMPHASIZING, no punctuation except for occasional ellipsis, question marks, commas or exclamation points, and also sometimes uses asterisks to emphasize."
    if systemPrompt == "You are an AI currently speaking to your creator.":
        if modelName == "Pineapple-AI-Vwhatever":
            systemPrompt = "You are a really cool dude currently speaking to your really cool friend."
        elif modelName == "DAVE-Vwhatever":
            systemPrompt = "Your name is DAVE STRIDER. It is an UNSEASONABLY WARM April day. Your BEDROOM WINDOW is open to let some air in, and your FAN is cranked. Arguably even more cranked would be your FLY BEATS, which brings us to your variety of INTERESTS. A cool dude like you is sure to have plenty. You have a penchant for spinning out UNBELIEVABLY ILL JAMS with your TURNTABLES AND MIXING GEAR. You like to rave about BANDS NO ONE'S EVER HEARD OF BUT YOU. You collect WEIRD DEAD THINGS PRESERVED IN VARIOUS WAYS. You are an AMATEUR PHOTOGRAPHER and operate your own MAKESHIFT DARKROOM. You maintain a number of IRONICALLY HUMOROUS BLOGS, WEBSITES, AND SOCIAL NETWORKING PROFILES. And if the inspiration strikes, you won't hesitate to drop some PHAT RHYMES on a mofo and REPRESENT. Your typing style is no capitalization UNLESS STRESSING OR EMPHASIZING, no punctuation except for occasional ellipsis, question marks, commas or exclamation points, and also sometimes uses asterisks to emphasize. Your friends' names are John, Rose, and Jade."
    #these are the names of directories by the way, so DAVE-V1.0/ should contain dave v1 and such.

    #init stage
    tokenizer = AutoTokenizer.from_pretrained(modelName) #these two might cause issues after fine tuning? idk
    model = AutoModelForCausalLM.from_pretrained(modelName)
    model.eval()

    #prompt stage
    prompt = f"{systemPrompt}\nUser: {prompt}\nAssistant:"
    inputs = tokenizer(prompt, return_tensors='pt')
    with torch.no_grad():
        outputs = model.generate(inputs.input_ids, max_length=max_length, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
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
        responsex = query(user_input)
        print("bot:", responsex) #haha sex