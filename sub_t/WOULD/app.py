from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# SIMPLE CONDITIONAL
@app.route('/simple', methods=['GET', 'POST'])
def simple():
    score = None
    total = 11  # 3 verdadero/falso + 5 blanks + 3 multiple choice
    if request.method == 'POST':
        correct_answers = {
            'q1': 'Falso',
            'q2': 'Verdadero',
            'q3': 'Falso',
            'blank1': 'would',
            'blank2': 'would',
            'blank3': 'would',
            'blank4': 'would',
            'blank5': 'would',
            'mc1': 'would travel',
            'mc2': 'would help',
            'mc3': 'would visit'
        }
        user_answers = request.form.to_dict()
        score = 0
        for key, correct in correct_answers.items():
            if user_answers.get(key, '').strip().lower() == correct.lower():
                score += 1
    return render_template('simple.html', score=score, total=total)

# CONTINUOUS CONDITIONAL
@app.route('/continuous', methods=['GET', 'POST'])
def continuous():
    score = None
    total = 9
    if request.method == 'POST':
        correct_answers = {
            'q1': 'Falso',
            'q2': 'Verdadero',
            'blank1': 'would be',
            'blank2': 'would be',
            'blank3': 'would be',
            'mc1': 'would be studying',
            'mc2': 'would be working',
            'mc3': 'would be traveling'
        }
        user_answers = request.form.to_dict()
        score = 0
        for key, correct in correct_answers.items():
            if user_answers.get(key, '').strip().lower() == correct.lower():
                score += 1
    return render_template('continuous.html', score=score, total=total)

# PERFECT CONDITIONAL
@app.route('/perfect', methods=['GET', 'POST'])
def perfect():
    score = None
    total = 9
    if request.method == 'POST':
        correct_answers = {
            'q1': 'Falso',
            'q2': 'Verdadero',
            'blank1': 'would have',
            'blank2': 'would have',
            'blank3': 'would have',
            'mc1': 'would have eaten',
            'mc2': 'would have studied',
            'mc3': 'would have traveled'
        }
        user_answers = request.form.to_dict()
        score = 0
        for key, correct in correct_answers.items():
            if user_answers.get(key, '').strip().lower() == correct.lower():
                score += 1
    return render_template('perfect.html', score=score, total=total)

# PERFECT CONTINUOUS CONDITIONAL
@app.route('/perfect_continuous', methods=['GET', 'POST'])
def perfect_continuous():
    score = None
    total = 9
    if request.method == 'POST':
        correct_answers = {
            'q1': 'Falso',
            'q2': 'Verdadero',
            'blank1': 'would have been',
            'blank2': 'would have been',
            'blank3': 'would have been',
            'mc1': 'would have been studying',
            'mc2': 'would have been working',
            'mc3': 'would have been traveling'
        }
        user_answers = request.form.to_dict()
        score = 0
        for key, correct in correct_answers.items():
            if user_answers.get(key, '').strip().lower() == correct.lower():
                score += 1
    return render_template('perfect_continuous.html', score=score, total=total)

# PRONUNCIACIONES (para el bot de pronunciación)
@app.route('/pronunciaciones')
def pronunciaciones():
    ejemplos = [
        {"es": "Yo viajaría a Japón.", "en": "I would travel to Japan."},
        {"es": "Ella te ayudaría.", "en": "She would help you."},
        {"es": "Nosotros compraríamos una casa.", "en": "We would buy a house."},
        {"es": "Ellos nos visitarían.", "en": "They would visit us."},
        {"es": "Él llamaría a su amigo.", "en": "He would call his friend."},
        {"es": "Yo estaría estudiando.", "en": "I would be studying."},
        {"es": "Ella estaría trabajando.", "en": "She would be working."},
        {"es": "Nosotros habríamos terminado.", "en": "We would have finished."},
        {"es": "Ellos habrían estado durmiendo.", "en": "They would have been sleeping."},
        {"es": "Él habría estado viajando.", "en": "He would have been traveling."},
    ]
    return render_template('pronunciaciones.html', ejemplos=ejemplos)

if __name__ == '__main__':
    app.run(debug=True)

