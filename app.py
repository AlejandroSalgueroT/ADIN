from flask import Flask, render_template, send_from_directory, abort
import os

app = Flask(__name__, 
    template_folder='templates',
    static_folder='static'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/img/<path:filename>')
def serve_img(filename):
    return send_from_directory('img', filename)

# Servir archivos de las subcarpetas específicas
@app.route('/sub_t/<path:filepath>')
def serve_sub_t(filepath):
    return send_from_directory('sub_t', filepath)

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

# Servir archivos HTML desde templates
@app.route('/<path:filename>')
def serve_templates(filename):
    try:
        # Primero intentar desde templates
        return send_from_directory('templates', filename)
    except:
        # Si no está en templates, buscar en otras carpetas
        try:
            return send_from_directory('.', filename)
        except:
            abort(404)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
