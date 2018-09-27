from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author':'jk rowling',
        'title':'Blog Post 1',
        'content':'first post content',
        'date_posted':'April 21 2018'
    },
    {
        'author':'john doe',
        'title':'Blog Post 2',
        'content':'second post content',
        'date_posted':'April 21 2018'
    }
]

@app.route('/')
def index():
    return render_template('index.html',posts = posts)



@app.route('/about')
def about():
    return render_template('about.html',title='about')




if __name__ == '__main__':
    app.run(debug=True)
