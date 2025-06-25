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

# Servir archivos CSS y JS específicos de subcarpetas
@app.route('/sub_t/MUST/<path:filename>')
def serve_must_files(filename):
    return send_from_directory('sub_t/MUST', filename)

@app.route('/sub_t/might/<path:filename>')
def serve_might_files(filename):
    return send_from_directory('sub_t/might', filename)

@app.route('/sub_t/Should/<path:filename>')
def serve_should_files(filename):
    return send_from_directory('sub_t/Should', filename)

@app.route('/sub_t/WOULD/<path:filename>')
def serve_would_files(filename):
    return send_from_directory('sub_t/WOULD', filename)

@app.route('/sub_t/Verbos/<path:filename>')
def serve_verbos_files(filename):
    return send_from_directory('sub_t/Verbos', filename)

@app.route('/sub_t/Proyec/<path:filename>')
def serve_proyec_files(filename):
    return send_from_directory('sub_t/Proyec', filename)

@app.route('/sub_t/TenSe May/<path:filename>')
def serve_tense_may_files(filename):
    return send_from_directory('sub_t/TenSe May', filename)

@app.route('/sub_t/Tenses Future/<path:filename>')
def serve_tenses_future_files(filename):
    return send_from_directory('sub_t/Tenses Future', filename)

@app.route('/sub_t/Tenses past/<path:filename>')
def serve_tenses_past_files(filename):
    return send_from_directory('sub_t/Tenses past', filename)

@app.route('/sub_t/Tenses_Present/<path:filename>')
def serve_tenses_present_files(filename):
    return send_from_directory('sub_t/Tenses_Present', filename)

# Servir archivos generales de sub_t
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
