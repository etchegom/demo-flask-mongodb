#!/bin/bash

set -e

case $1 in
    run)
        python app.py
        ;;
    populate)
        python populate.py
        ;;
    *)
        echo "Running server command: $@"
        exec "$@"
esac
