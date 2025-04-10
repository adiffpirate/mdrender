#!/bin/bash

while IFS= read -r line; do                                                                                                                                                
    for (( i=0; i<${#line}; i++ )); do
        echo -n "${line:$i:1}"
        sleep 0.001
    done
    echo
done < test.md | python3 $1
