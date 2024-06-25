from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = 'meta-llama/Meta-Llama-3-8B'  # replace with the path to your model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
system_prompt = ""
# Ensure the model is in evaluation mode
#uhhh what does that mean
model.eval()

def query(prompt, max_length=300):
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

