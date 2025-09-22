this repo is a clone of
https://github.com/miguelgrinberg/flasky

this is also the docker version, use these commands to create image and run container
docker build -t flask-app .  
docker run -p 5000:5000 -e FLASK_APP=hello.py flask-app

Flasky
======

This repository contains the source code examples for the second edition of my O'Reilly book [Flask Web Development](http://www.flaskbook.com).

The commits and tags in this repository were carefully created to match the sequence in which concepts are presented in the book. Please read the section titled "How to Work with the Example Code" in the book's preface for instructions.

For Readers of the First Edition of the Book
--------------------------------------------

The code examples for the first edition of the book were moved to a different repository: [https://github.com/miguelgrinberg/flasky-first-edition](https://github.com/miguelgrinberg/flasky-first-edition).
