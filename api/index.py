from flask import Flask, jsonify
import gdown

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'


@app.route('/run-colab')
def run_colab():
    gdown.download('https://drive.google.com/file/d/1NkBYI8SYXTvvdj6Cxjg-gGdVE-hDugjn#scrollTo=gXaoZs2lh1hi', 'colab.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')