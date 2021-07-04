#!/bin/sh

DIR=./
LOGDIR=./logs
source $DIR/venv/bin/activate
python $DIR/script.py > $LOGDIR/script.log 2>&1
