from flask import Flask, render_template, request, jsonify
from diffusers import StableDiffusionPipeline
import torch
import os

# Initialize Flask app
app = Flask(__name__)

# Load Stable Diffusion model
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipe.to("cuda")

# Ensure the static folder exists
os.makedirs("static", exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form.get("text")
        if prompt:
            try:
                # Generate the image
                image = pipe(prompt).images[0]
                image_path = os.path.join("static", "generated_image.png")
                image.save(image_path)
                return render_template("index.html", image_path=image_path, prompt=prompt)
            except Exception as e:
                return f"An error occurred: {str(e)}"
    return render_template("index.html")

if __name__ == "__main__":
    app.run()