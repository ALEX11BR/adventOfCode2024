#!/usr/bin/env sh
cd "$(dirname $(readlink -f "$0") )"

if [ -z "$1" ]; then
    echo !!! Supply day number !!!
    exit 1
fi

cp -r d1 d"$1"
