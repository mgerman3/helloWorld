from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!- From Michael German. I am adding my first code change.'

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/favorite-course')
def favorite_course():
    print('Subject: ' + request.args.get('subject'))
    print('Number: ' + request.args.get('course_number'))

    return render_template('favorite-course.html')


@app.route('/contact')
def contact():
    if request.method == 'post':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')


if __name__ == '__main__':
    app.run()
