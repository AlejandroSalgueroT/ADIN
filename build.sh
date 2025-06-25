#!/bin/bash
set -o errexit

# Force installation in the current environment
pip install --upgrade pip
pip install Flask==3.0.0 Werkzeug==3.0.1 gunicorn==22.0.0 --force-reinstall
