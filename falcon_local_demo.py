from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch


# model = "tiiuae/falcon-7b-instruct"
# tokenizer = AutoTokenizer.from_pretrained(model)

model_id="tiiuae/falcon-7b-instruct"
tokenizer=AutoTokenizer.from_pretrained(model_id)
model=AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)

pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
    max_length=200,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id
)

sequences = pipeline(
   "Create a list of 3 important things to reduce global warming"
)


for seq in sequences:
    print(f"Result: {seq['generated_text']}")