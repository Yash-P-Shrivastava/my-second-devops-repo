from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Demo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                text-align: center;
                padding-top: 100px;
            }
            .card {
                background: white;
                width: 600px;
                margin: auto;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            }
            h1 {
                color: #2e86de;
            }
            h2 {
                color: #28a745;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Hello from AWS CodeDeploy!</h1>
            <h2>Application Started Successfully ✅</h2>
            <p>CI/CD Pipeline: GitHub → CodeBuild → CodeDeploy → EC2</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
