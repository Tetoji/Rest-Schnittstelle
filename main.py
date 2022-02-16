# open cmd and: "cd C:\Users\tjschulz\Desktop\Schule\Aufgaben\Netzwerktechnik\Lehrjahr 2\2022\RestAPI"
#         then: "py main.py"

from flask import Flask, render_template      

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("main.html")
    
if __name__ == "__main__":
    app.run(debug=True)