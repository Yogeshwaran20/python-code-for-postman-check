from flask import Flask 

app=Flask(__name__)

@app.route('/')
def hello():
    return "BASIC PYTHON CODE FOR TESTING IN FLASK"
if __name__ == "__main__":
    app.run()