from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hola, HL Inversiones está en la nube con Render!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
