from flask import *
app = Flask(__name__)

@app.route('/')
def main():
   return render_template("index.html")

@app.route('/favicon.ico')
def favicon():
   return send_file("static/favicon.ico")

@app.route('/js/')
def js():
   return send_file("static/index.js")

@app.route('/css/')
def css():
   return send_file("static/style.css")

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5050, debug = False)