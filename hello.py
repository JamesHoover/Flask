from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def helloName(name=None):
    return render_template('hello.html', name=name)

@app.route('/alert/')
@app.route('/alert/<name>')
def show_alert(name=None):
    return render_template('js_alert_test.html', name=name)

@app.route('/button')
def button():
    return render_template('button.html')

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/projects')
def projects():
    return 'The projects page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/button/2')
def button2():
    return render_template('button2.html')

@app.route('/button/3')
def button3():
    return render_template('button3.html')

@app.route('/button/4')
def button4():
    return render_template('button4.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.debug = True
    app.run()
