from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def news_webhook():
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.json)
        return Response(status=200)

@app.route("/")
def hello():
  return 'Hello World!'

app.run(host='0.0.0.0', port=8000)


if __name__ == '__main__':
    app.run()
