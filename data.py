from flask import Flask, render_template
from app1 import app1
from app2 import app2
from app3 import app3
from app4 import app4



app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')

app.register_blueprint(app1, url_prefix='/app1')
app.register_blueprint(app2, url_prefix='/app2')
app.register_blueprint(app3, url_prefix='/app3')
app.register_blueprint(app4, url_prefix='/app4')


# Route to the HTML page
@app.route('/')
def index():
    return render_template('index.html',title='Home')

@app.route('/about')
def about():
    return render_template('about.html',title='About')

# @app.route('/home')
# def home():
#     return render_template('index.html',title='Home2')
if __name__ == '__main__':
    app.run(debug=True)
