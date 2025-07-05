from fastapi import FastAPI, Request
from pydantic import BaseModel
from diffusers import StableDiffusionPipeline, StableVideoDiffusionPipeline
import torch, os, tempfile
import shutil
from fastapi.responses import FileResponse

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

device = "cuda" if torch.cuda.is_available() else "cpu"
sd_pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5").to(device)
svd_pipe = StableVideoDiffusionPipeline.from_pretrained("stabilityai/stable-video-diffusion-img2vid-xt").to(device)

@app.post("/generate")
def generate_video(request: PromptRequest):
    prompt = request.prompt
    image = sd_pipe(prompt).images[0]
    frames = svd_pipe(image, decode_chunk_size=8, motion_bucket_id=127, noise_aug_strength=0.1).frames[0]
    
    tmpdir = tempfile.mkdtemp()
    output_path = os.path.join(tmpdir, "video.mp4")

    import imageio
    imageio.mimsave(output_path, frames, fps=6)

    return FileResponse(output_path, media_type="video/mp4", filename="generated_video.mp4")
