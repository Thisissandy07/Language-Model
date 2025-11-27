import torch
import transformers
import sentencepiece
import sacremoses
import os
from huggingface_hub import InferenceClient
import hf_xet





from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-de-en")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-de-en")

inp = str(input("Please enter the german setence to be translated:   "))
input_ids = tokenizer(inp, return_tensors="pt").input_ids
outputs = model.generate(input_ids=input_ids, num_beams=4, num_return_sequences=1)
print("Generated:", tokenizer.batch_decode(outputs, skip_special_tokens=True))




