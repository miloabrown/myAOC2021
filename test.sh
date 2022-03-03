#!/bin/bash

for py_file in $(find Tasks -name *.py)
do
    python $py_file
done