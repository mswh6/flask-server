from flask import Flask

app = Flask(__name__)

# Trasa główna "/"
@app.route('/')
def home():
    return "Serwer Flask działa poprawnie! :)"

# Obsługa favicon.ico (uniknięcie błędu 404)
@app.route('/favicon.ico')
def favicon():
    return "", 204  # Zwraca pustą odpowiedź z kodem 204 (No Content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
