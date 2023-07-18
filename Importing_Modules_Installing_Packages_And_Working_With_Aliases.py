'''

Importing modules:

import turtle

import is a keyword and turtle is a module name

from turtle import Turtle

from is a keyword, turtle is a module name, import is a keyword, and Turtle is a thing in module

from turtle import * , from random import * => Avoid writing code like this

Working with aliases:

import turtle as t

import is a keyword, turtle is a module name, as is a keyword, and t is an alias name

Installing modules:

import heroes

Turtle is a module that's packaged with the python standard library. And this is a small library of code that
contains the basics to get you started like a core set

Tkinter is the standard GUI library for Python.
 Python when combined with Tkinter provides a fast and easy way to create GUI applications.
 Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.
 Creating a GUI application using Tkinter is an easy task.
'''

import turtle as t

tommy = t.Turtle()

# Installing packages

import heroes
print(heroes.gen())
