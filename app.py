from flask import Flask, render_template, send_file

app = Flask(__name__)

# Hlavní stránka (úvodní stránka)
@app.route('/')
def home():
    return render_template('index.html')

# Sekce "O mně"
@app.route('/about')
def about():
    return render_template('about.html')

# Sekce "Zkušenosti"
@app.route('/experience')
def experience():
    return render_template('experience.html')

# Sekce "Kontakt"
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Sekce "Životopis ke stažení"
@app.route('/cv')
def cv():
    return send_file('static/your_cv.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)