from bottle import Bottle, request, run, template, static_file
import os
from datetime import datetime

app = Bottle()

@app.route('/')
def index():
    return template('views/notepad.tpl')

@app.route('/save', method='POST')
def save_note():
    note = request.json.get('note')
    if note:
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('static/notes.txt', 'a') as f:
            f.write(f'{current_date}: {note}\n')
        return {'message': 'Note saved successfully.'}
    else:
        return {'message': 'No note provided.'}

@app.route('/static/<filename:path>')
def serve_static(filename):
    return static_file(filename, root='./static/')

if __name__ == '__main__':
    if not os.path.exists('static/notes.txt'):
        with open('static/notes.txt', 'w') as f:
            f.write('')
    run(app, port=8081, debug=True)
