import torch
from diffusers import StableDiffusionPipeline


model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32, timeout=100)
pipe = pipe.to("cpu")
#pipe.enable_model_cpu_offload()

prompt = "A futuristic class full of students learning AI coding in the surreal style of Salvador Dali"
image = pipe(prompt).images[0]
# run with: ~/repos/LLM/llms/bin/python -u "/home/kingston/repos/LLM/Udemy/local_image_gen.py"
# It'll  take a while to download the needed pipeline model