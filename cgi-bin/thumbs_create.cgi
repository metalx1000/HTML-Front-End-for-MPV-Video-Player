#!/bin/sh
echo "Content-type: text/plain\n\n"

rm ../thumbs/*

for i in ../videos/*
do
  vid="$(basename "$i")"
  ffmpeg -y -i "$i" -ss 00:00:01 -s 400x300 -vframes 1 ../thumbs/${vid}.png 2> /dev/null
  echo "$vid"
done
