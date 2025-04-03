# AI Image Generation Web App

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/flask-2.0%2B-lightgrey)
![Stable Diffusion](https://img.shields.io/badge/stable%20diffusion-v1.4-orange)
![Colab](https://img.shields.io/badge/Google%20Colab-supported-brightgreen)

A web application that generates AI image from text prompts using Stable Diffusion v1-4, with both local and Google Colab deployment options.

## 🌟 Key Features

- 🎨 Generate images from text prompts using AI
- 🖥️ Two deployment options: Local machine or Google Colab
- 🚀 GPU acceleration support (works best on NVIDIA GPUs)
- 📱 Clean, mobile-friendly interface
- 💾 Save generated images with one click

## 🚀 Getting Started

### Prerequisites
- For local deployment:
  - Python 3.8+
  - NVIDIA GPU (recommended) with CUDA 11.x
- For Google Colab:
  - Just a web browser!

## 🛠️ Installation & Setup

### Option 1: Google Colab (Recommended for low-spec machines)
1. Open the Colab Notebook
2. Run cells
3. Wait for some timr to complete 
4. Click the LocalTunnel link that appears to access the web interface

### Option 2: Local Installation
```bash
git clone https://github.com/your-username/ai-image-generator.git
cd ai art generator
```
pip install if required

## 🏃 Running the Application

### Google Colab Method
Simply run all cells in the notebook - the web interface URL will be displayed automatically.

### Local Method
```bash
python app.py
```
Then open http://localhost:5000 in your browser

## 🗂️ Project Structure
```
ai-image-generator/
├── app.py                 # Main Flask application
├── ai_image_generator.ipynb  # Colab notebook
├── static/                # Static files
│   ├── art-generator.png        # Browser tab icon
│   └── generated/         # Stores generated images
└── templates/             # HTML templates
    └── index.html         # Web interface
```

## 💡 Tips for Best Performance

**In Colab**: Use GPU runtime (Runtime → Change runtime type → GPU)

**CUDA Errors**:
```python
# In app.py, change to:
pipe.to("cpu")
```
