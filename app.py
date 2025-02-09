from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    # repalce hardcoding
    return render_template('home.html')

list = [
    {
        'id': 1,
        'wish': 'New Job Position',
        'desc': 'I would like a remote position.',
        'salary': '30$ an hour',
    },
    {
        'id': 2,
        'wish': 'New Car',
        'desc': "I've been wantin a Tesla for a long time. I really like the new model facelift alot.",
    },
    {
        'id': 3,
        'wish': 'New Place',
        'desc': 'I really value my space and i have never been able to have a space i could say is "mine". Id like a nice office with a window.'
    },
    {
        'id': 4,
        'wish': 'New Computer',
        'desc': 'Im a gamer at heart and the games nowadays are pushing my systems limits',
}
]

@app.route('/wishlist')
def load_wishlist():
    # repalce hardcoding
    return render_template('wishlist.html', wishlist = list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)