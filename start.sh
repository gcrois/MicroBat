#! /bin/bash

TMUX_INSTANCE="mb_flask"
export FLASK_APP="app/__init__.py"

if [ "$1" == "local" ]; then
	echo "Starting locally..."
	tmux new-session -d -s $TMUX_INSTANCE 'export FLASK_APP=app/__init__.py; flask run'
elif [ "$1" == "external" ]; then
	echo "Starting externally..."
	tmux new-session -d -s $TMUX_INSTANCE 'export FLASK_APP=app/__init__.py; flask run --host=0.0.0.0'
else
	echo "Usage: " $0 "[local/external]"
	echo "WARNING: External is generally unsafe! Use at your own risk!"
	exit 1
fi
echo "Started! To view live server console, do 'tmux a -t " $TMUX_INSTANCE "'"
