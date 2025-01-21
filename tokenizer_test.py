import re

with open("/home/kingston/repos/LLM/the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
#print("Total number of character:", len(raw_text))
#print(raw_text[:99])
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
#print(len(preprocessed))
#print(preprocessed[:30])
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print(vocab_size)