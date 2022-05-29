#!/usr/bin/bash
for FILE in *.json;
do
    curl -X POST -H "Content-Type: application/json" -d @$FILE https://backmagic.herokuapp.com/api/recruitment;
done