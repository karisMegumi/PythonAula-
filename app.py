from flask import Flask

app = Flask(__name__)
@app.route('/')
def curso():
    return 'Pagina inicial'
@app.route('/produtos')
def produto():
    return '<h1>Minha pagina de produtos</h1>'


'''cd\
    cd users
    cd karis.mshimizu
    cd documents
    cd cebolinha
    set FLASK_APP = app
    env\scripts\activate
    flask run
    
    FLASK_DEBUG = development
    flask run'''