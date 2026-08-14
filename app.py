from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello from AWS CodeDeploy!</h1>
    <h2>Application started successfully</h2>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)