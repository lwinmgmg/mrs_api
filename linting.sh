#!/bin/bash

echo "Started Black Formatter"
poetry run black mrs_api
echo "Done Black Formatter"

echo "Started Flake8 Linter"
poetry run flake8 mrs_api
echo "Done Flake8 Formatter"

echo "Started Pylint Linter"
poetry run pylint mrs_api
echo "Done Pylint Linter"
