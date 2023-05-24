from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template("index.html")

@app.route('/home')
def home():
    
    return "Goodbye World"

if __name__ == "__main__":
    app.run(debug=True, port=5050)