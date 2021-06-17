from flask import Flask

app = Flask(__name__)


@app.route('/')
def display_Score():
    f = open("Scores.txt", "r")
    score = int(f.readline())
    f.close()
    try:
        return 'Your score is : ' + str(score)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


def call_to_flask():
    app.run(port=80)
