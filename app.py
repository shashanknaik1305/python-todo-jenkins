from flask import Flask, request, render_template_string

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return render_template_string("""
        <h2>My To-Do List</h2>
        <form action="/add" method="post">
            <input name="task">
            <input type="submit" value="Add">
        </form>
        <ul>
            {% for t in tasks %}
                <li>{{ t }}</li>
            {% endfor %}
        </ul>
    """, tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return home()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
