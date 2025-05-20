from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ws-chat')
def ws_chat():
    return render_template("websocket_client.html")

if __name__ == "__main__":
    app.run(port=5000)
