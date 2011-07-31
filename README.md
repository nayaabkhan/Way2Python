Way2Python: Way2SMS API in Python
=================================

Way2Python is a small command line utility written in python
that can be used to send SMS's to multiple recipients without
having to go through the process of logging into Way2SMS.com.

This utility works only with Way2SMS accounts and hence
works for Indian phone numbers only.

Usage
-----

You'll require to have atleast Python 2.5 installed on your machine
and you'll also need to get the httplib2 library from
[httplib2 on Google code](http://code.google.com/p/httplib2) to get starting.

First of all open the way2python.py and edit the following lines with your login details:  
`USERNAME = 'your login phone number'`  
`PASSWORD = 'your password'`

Use the program by writing down the following on your command line:  
`python way2python.py --numbers=9825012345:9998123456 --message="Hello, I am now using way2python!"`

The `:` is used to separate multiple numbers.

Bugs
----

This is the first version and still might require a little brushing.
Hope you try out the utility and report any issues here on github.
Issues could be added using the Issues button at the top on the
[Way2Python's Github page](https://github.com/nayaab/Way2Python).
*Cheers!!!*
