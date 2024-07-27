from flask import Flask, request, Response, jsonify

app = Flask(__name__)


@app.route('/webhook', methods=['POST', 'GET'])
def news_webhook():
    print("Data received from Finnhub Webhook is: ", request.json)
    if request.method == 'POST':
        print("post")
        return Response('post',status=200)
    else:
        print("get")
        return Response('get',status=200)

@app.route("/")
def hello():
    return 'News ingestion Webhook'


# app.run(host='0.0.0.0', port=8000)


if __name__ == '__main__':
    app.run()
