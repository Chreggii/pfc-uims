#! /bin/bash

cd /Users/sarah/Documents/UZH/Masterarbeit/project/Configuration-System/backend

chmod u+x run.command

export FLASK_APP=configuration
export FLASK_ENV=development
flask init-db
