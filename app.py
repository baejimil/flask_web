from flask import Flask , render_template
from data import Articles
app = Flask(__name__)
app.debug=True

@app.route('/')
def index():
    print('seccess')
    # return 'TEST'
    return render_template('home.html', hello='garykim')

@app.route('/about')
def about():
    # print('seccess')
    # return 'TEST'
    return render_template('about.html', hello='garykim')

@app.route('/articles')
def Articles():
    print('seccess')
    # return 'TEST'
    articles = Articles()
    print(len(articles))
    return render_template('articles.html', articles=articles)

if __name__ == '__main__' :
    # app.run(host='0.0.0.0', port='8080')
    app.run()
    
