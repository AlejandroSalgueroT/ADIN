from flask import Flask, render_template, send_from_directory
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

@app.route('/<path:filename>')
def serve_templates(filename):
    # Serve other HTML files from templates folder
    return send_from_directory('templates', filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
