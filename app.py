from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import re
from nltk.stem import WordNetLemmatizer

app = Flask(__name__)
CORS(app)

# Load trained files
model = joblib.load("spam_model.pkl")
cv = joblib.load("count_vectorizer.pkl")
le = joblib.load("label_encoder.pkl")

wnl = WordNetLemmatizer()


def preprocess_message(message):
    words = re.sub(r"[^a-zA-Z]", " ", message)
    words = words.lower()
    words = words.split()

    words = [
        wnl.lemmatize(word)
        for word in words
    ]

    return " ".join(words)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    message = data.get("message", "")

    if not message:
        return jsonify({
            "error": "Message is required"
        }), 400

    # Preprocess message
    cleaned_message = preprocess_message(message)

    # Convert text into same BoW features
    message_vector = cv.transform([cleaned_message])

    # Predict
    prediction = model.predict(message_vector)

    # Convert 0/1 back to Ham/Spam
    result = le.inverse_transform(prediction)[0]

    return jsonify({
        "message": message,
        "prediction": result
    })


if __name__ == "__main__":
    app.run(debug=True)