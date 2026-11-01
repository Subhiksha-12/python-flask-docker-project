from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <div style='text-align: center; font-family: sans-serif; padding-top: 50px;'>
        <h1 style='color: #2563eb;'>Python Flask Application in Docker! 🐍</h1>
        <p>Your Python web app is running smoothly inside a Docker container.</p>
    </div>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)