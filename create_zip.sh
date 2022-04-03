#!/bin/bash

PYTHON_VERSION=3.10
VENV_DIR=venv

echo 'Zipping repository...'
git archive -o lambda.zip HEAD
echo 'Adding site-pachages to zip...'
pushd "$VENV_DIR/lib/python$PYTHON_VERSION/site-packages"
ls
zip -x *.dist-info/** -x __pycache__/** -g ../../../../lambda.zip -r .
popd
