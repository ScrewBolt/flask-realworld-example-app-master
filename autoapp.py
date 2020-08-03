# -*- coding: utf-8 -*-
"""Create an application instance."""
from flask.helpers import get_debug_flag

from conduit.app import create_app
from conduit.settings import DevConfig, ProdConfig
from flask import Flask
CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)

@app.route('/')
def hello_world():
    return 'Hello, World! This is Wei-Chyang Test'
