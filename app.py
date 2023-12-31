"""Flask server processing user requests"""
# Importing required libs
from flask import Flask, render_template, request
from model import preprocess_img, predict_result
# Instantiating flask app
app = Flask(__name__)
# Home route
@app.route("/")
def main():
    """Renders home page"""
    return render_template("index.html")
# Prediction route
@app.route('/prediction', methods=['POST'])
def predict_image_file():
    """predict_image_file predicts images submitted by the user"""
    try:
        if request.method == 'POST':
            img = preprocess_img(request.files['file'].stream)
            pred = predict_result(img)
            return render_template("result.html", predictions=str(pred))
        return None
    except:
        error = "File cannot be processed."
        return render_template("result.html", err=error)
    return None
# Driver code
if __name__ == "__main__":
    app.run(port=9000, debug=True)
