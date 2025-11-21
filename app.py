from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    message = ''
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        user_message = request.form.get('message')
        # Demo: Always display success, no backend storage
        message = f"Thanks, {name}! Your message was received."
    return render_template('contact.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
