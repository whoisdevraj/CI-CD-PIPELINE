from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_text = request.form['new-task']
        if task_text:
            task_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tasks.append({'text': task_text, 'time': task_time})
    return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    if 0 <= task_id < len(tasks):
        task_text = request.form['updated-task']
        if task_text:
            task_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tasks[task_id] = {'text': task_text, 'time': task_time}
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
