# Environment variables.
export FLASK_CONFIG=dev
export FLASK_APP=run.py
export VENV_DIR=../../venv

# Start instance of Flask dev server inside virtual environment.
if [ -d "$VENV_DIR" ]; 
    then
        source $VENV_DIR/bin/activate
        flask run
    else
        echo "A virtual environment could not be found at $VENV_DIR"
fi
