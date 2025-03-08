from huggingface_hub import login
from transformers import AutoTokenizer

hf_token = userdata.get('HF_TOKEN')
login(hf_token, add_to_git_credential=True)

'''In order to use the fantastic Llama 3.1, Meta does require you to sign their terms of service.

Visit their model instructions page in Hugging Face: https://huggingface.co/meta-llama/Meta-Llama-3.1-8B

At the top of the page are instructions on how to agree to their terms. If possible, you should use the same email as your huggingface account.

In my experience approval comes in a couple of minutes. Once you've been approved for any 3.1 model, it applies to the whole family of models.

If the next cell gives you an error, then please check:

Are you logged in to HuggingFace? Try running login() to check your key works
Did you set up your API key with full read and write permissions?
If you visit the Llama3.1 page with the link above, does it show that you have access to the model near the top?
I've also set up this troubleshooting colab to try to diagnose any HuggingFace connectivity issues:
https://colab.research.google.com/drive/1deJO03YZTXUwcq2vzxWbiBhrRuI29Vo8?usp=sharing'''

tokenizer = AutoTokenizer.from_pretrained('meta-llama/Meta-Llama-3.1-8B-Instruct', trust_remote_code=True)

messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Tell a light-hearted joke for a room of Data Scientists"}
  ]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
print(prompt)