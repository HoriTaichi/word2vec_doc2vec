#!/bin/sh

DIR=./
LOGDIR=./logs
source $DIR/venv/bin/activate
python $DIR/word2vec.py > $LOGDIR/word2vec.log 2>&1
