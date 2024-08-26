from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Словарь для хранения сообщений, где ключ - имя пользователя, значение - список сообщений
messages = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_message', methods=['POST'])
def send_message():
    username = request.form.get('username')
    message = request.form.get('message')

    if username not in messages:
        messages[username] = []

    messages[username].append(message)

    return jsonify(messages)


@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify(messages)


if __name__ == '__main__':
    app.run(debug=True)
