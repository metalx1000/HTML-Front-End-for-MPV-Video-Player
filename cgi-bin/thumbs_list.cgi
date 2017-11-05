#!/bin/sh
echo "Content-type: text/plain\n"
ls ../thumbs/*.png|while read file
do
  basename "$file"
done
