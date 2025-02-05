from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    # repalce hardcoding
    return render_template('home.html')

@app.route('/wishlist')
def load_wishlist():
    # repalce hardcoding
    return render_template('wishlist.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug = True)