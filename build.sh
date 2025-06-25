#!/bin/bash
set -o errexit

# Install packages using pip directly
python -m pip install --upgrade pip
python -m pip install Flask==3.0.0 Werkzeug==3.0.1 gunicorn==22.0.0
