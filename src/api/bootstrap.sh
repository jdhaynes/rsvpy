# Environment variables.
export FLASK_CONFIG=dev
export FLASK_APP=run.py
export VENV_DIR=../../venv

# Start instance of Flask dev server inside virtual environment.
source $VENV_DIR/bin/activate
flask run