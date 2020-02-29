#!/bin/python

"""
Solution to the unpaid content problem on the internet using the lightning network.
"""

from flask import Flask, escape, request
from app.reward import fill_bucket
from app.server import server

__author__ = "Daan Middendorp"
__copyright__ = "Copyright 2020, Technische Universität Berlin"
__license__ = "MIT"
__version__ = "0.0.1"

app = Flask(__name__)
app.config['ENV'] = 'development'
app.register_blueprint(server)

# Make sure that the bucket filler is running
fill_bucket()

# send_money('027d2456f6d4aaf27873b68b7717c8137aaa8043d687a2113b916a5016e9a880e9', 10)

if __name__ == '__main__':
    app.run()