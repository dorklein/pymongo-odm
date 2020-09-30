# -*- coding: utf-8 -*-
"""
Created on 9/30/20

@author dor
"""


class Map(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
