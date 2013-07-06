Usage
=====

Just run **example.py**

The Idea
========

A dedicated process only for the displays. The main program sends message to the Display program to display Images, and to perform ant other tasks


+ The program crashes when you try to create more than one display throwing strange X Server errors (on my Arch Linux 64-bit). 
+ The proper way to do multiple displays would be to have just one process for all displays created and to have it show a new window for each display the user requests
