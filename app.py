from Data_Source import get_data
from flask import Flask, render_template

# Webframework.py is the source for flask webapp. includes flask templates and url endpoints to access data

app = Flask(__name__)
app.debug = True





posts = [
{
    'author': 'jake',
    'title': 'test',
    'date_posted': 'today'
},

{
    'author': 'john',
    'title': 'tess',
    'date_posted': 'yesterday'
}

]


@app.route('/')
@app.route('/raw')
def fec_data():
    return get_data()
@app.route('/biden')
def biden():

    return
@app.route('/test')
def test():
    data = get_data()
    return render_template('tables.html', data = data)
if __name__ == '__main__':
    app.run()



