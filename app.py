from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/circle', methods=['GET', 'POST'])
def circle():
    area = None
    if request.method == 'POST':
        try:
            radius = float(request.form['radius'])
            area = 3.1416 * (radius ** 2)
        except:
            area = "Invalid input"
    return render_template('circle.html', area=area)

@app.route('/triangle', methods=['GET', 'POST'])
def triangle():
    area = None
    if request.method == 'POST':
        try:
            base = float(request.form['base'])
            height = float(request.form['height'])
            area = 0.5 * base * height
        except:
            area = "Invalid input"
    return render_template('triangle.html', area=area)

if __name__ == '__main__':
    app.run(debug=True)

