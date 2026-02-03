#!/bin/bash

RUN_FILE="$(ls -t *.py | head -n 1)"

echo "[selected file] $RUN_FILE"

python "$RUN_FILE" < input.txt