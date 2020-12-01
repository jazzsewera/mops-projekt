#!/bin/bash

# To render a pdf with Vim: '!./render.sh %' will render current file

FILENAME=$(echo -n $1 | perl -ne 'print "$&" if /[a-zA-Z0-9 _-]+?(?=\.)/g')

pandoc -f markdown_mmd+smart -V lang=pl-PL -o ${FILENAME}.pdf $1
