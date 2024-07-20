from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments, TextDataset, DataCollatorForLanguageModeling
import torch

# Load the pre-trained model and tokenizer
model_name = '/home/pineapple/pineapple_ai/Meta-Llama-3-8B'
data = "/home/pineapple/pineapple_ai/dave/data/sample.txt"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Ensure mixed precision if using
torch.cuda.set_per_process_memory_fraction(0.90)  # Use only 90% of available GPU memory
torch.backends.cudnn.benchmark = True
model.half()  # Use FP16 precision

# Load the text data
def load_dataset(file_path, tokenizer, block_size=128):
    dataset = TextDataset(
        tokenizer=tokenizer,
        file_path=file_path,
        block_size=block_size,
    )
    return dataset

train_dataset = load_dataset(data, tokenizer)

# Data collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False,  # We are not using masked language modeling
)

# Training arguments
training_args = TrainingArguments(
    output_dir="/home/pineapple/pineapple_ai/dave/",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=2,  # Adjust based on available GPU memory
    save_steps=10_000,
    save_total_limit=2,
    fp16=True,  # Enable mixed precision
    gradient_accumulation_steps=4,  # Accumulate gradients to simulate larger batch size
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
)

# Fine-tune the model
trainer.train()

# Save the model and tokenizer
model.save_pretrained("/home/pineapple/pineapple_ai/dave/")
tokenizer.save_pretrained("/home/pineapple/pineapple_ai/dave/")
