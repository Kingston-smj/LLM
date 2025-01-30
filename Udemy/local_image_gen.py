import torch
from diffusers import StableDiffusionPipeline


model_id = "deepseek-ai/DeepSeek-R1"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cpu")
pipe.enable_model_cpu_offload()


prompt = "A futuristic class full of students learning AI coding in the surreal style of Salvador Dali"
image = pipe(prompt).images[0]