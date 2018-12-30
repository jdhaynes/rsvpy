#########################################################################
# bootstrap.sh                                                          #
# --------------------------------------------------------------------- #
# Establishes and launches development environment to run the app       #
# on the Flask dev server.                                              #
#########################################################################

export FLASK_CONFIG=dev
export FLASK_APP=main.py
export VENV_DIR=../../venv
 
# Run Flask dev server inside virtual env.
if [ -d "$VENV_DIR" ]; 
    then
        source $VENV_DIR/bin/activate
        flask run --host=0.0.0.0
    else
        echo "A virtual environment could not be found at $VENV_DIR."
fi