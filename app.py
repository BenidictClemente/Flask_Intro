from flask import Flask, render_template, request
from linkedlist import Linkedlist
from infix_to_postfix import infix_to_postfix


app = Flask(__name__)

linked_list = Linkedlist()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/infix', methods=['GET', 'POST'])
def infix_page():
    result = ""
    expression = ""
    if request.method == 'POST':
        expression = request.form.get('expression')
        if expression:
            result = infix_to_postfix(expression)
    return render_template('infix.html', result=result, expression=expression)


@app.route('/linkedlist', methods=['GET', 'POST'])
def linkedlist_page():
    if request.method == 'POST':
        action = request.form.get('action')
        value = request.form.get('value')
        if action == 'insert' and value:
            linked_list.insert(value)
        elif action == 'delete' and value:
            linked_list.delete(value)
    return render_template('linkedlist.html', items=linked_list.get_items())

@app.route('/circle')
def circle_page():
    return render_template('circle.html')

@app.route('/triangle')
def triangle_page():
    return render_template('triangle.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)



