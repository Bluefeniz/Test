from flask import Flask, jsonify
import gdown
app = Flask(__name__)

@app.route('/run-colab')
def run_colab():
    gdown.download('https://colab.research.google.com/drive/1hNrfyuEQN1EyqOCuZV7eysT1tAM9j5-r#scrollTo=J9teZ-sCmrDE', 'tradingBot.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')
def hello_world():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run()
