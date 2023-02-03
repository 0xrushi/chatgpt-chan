from flask import Flask, request, send_file
from torch import autocast
from diffusers import StableDiffusionPipeline
import io

app = Flask(__name__)
pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",
        use_auth_token=True
).to("cuda")

@app.route("/")
def generate_image():
    prompt = request.args.get("prompt", "a photo of an astronaut riding a horse on mars")
    with autocast("cuda"):
        image = pipe(prompt)["images"][0]
    img_data = io.BytesIO()
    image.save(img_data, "PNG")
    img_data.seek(0)
    return send_file(img_data, mimetype='image/png')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8088)

