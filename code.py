from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = "Artificial intelligence will change the world because"

result = generator(prompt, max_length=60)

print(result[0]['generated_text'])