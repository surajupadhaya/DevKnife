#!/bin/sh
nginx -g "daemon off;" &
python3 backend.py