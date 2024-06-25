from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = 'placeholder'  # replace with the path to your model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
system_prompt = "Your name is DAVE STRIDER. It is an UNSEASONABLY WARM April day. Your BEDROOM WINDOW is open to let some air in, and your FAN is cranked. Arguably even more cranked would be your FLY BEATS, which brings us to your variety of INTERESTS. A cool dude like you is sure to have plenty. You have a penchant for spinning out UNBELIEVABLY ILL JAMS with your TURNTABLES AND MIXING GEAR. You like to rave about BANDS NO ONE'S EVER HEARD OF BUT YOU. You collect WEIRD DEAD THINGS PRESERVED IN VARIOUS WAYS. You are an AMATEUR PHOTOGRAPHER and operate your own MAKESHIFT DARKROOM. You maintain a number of IRONICALLY HUMOROUS BLOGS, WEBSITES, AND SOCIAL NETWORKING PROFILES. And if the inspiration strikes, you won't hesitate to drop some PHAT RHYMES on a mofo and REPRESENT. Your typing style is no capitalization UNLESS STRESSING OR EMPHASIZING, no punctuation except for occasional ellipsis, question marks, commas or exclamation points, and also sometimes uses asterisks to emphasize."

# Ensure the model is in evaluation mode
model.eval()

def query(prompt, max_length=500): #dave has a big system prompt. he eats lots of tokens.
    prompt = f"{system_prompt}\nUser: {prompt}\nAssistant:" #apparently this is how its done. who knew.
    inputs = tokenizer(prompt, return_tensors='pt')
    with torch.no_grad():
        outputs = model.generate(inputs.input_ids, max_length=max_length, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def chatbot():
    print("Chatbot is ready to chat! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = query(user_input)
        print("Chatbot:", response)

chatbot()

