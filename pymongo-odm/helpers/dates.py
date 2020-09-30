# -*- coding: utf-8 -*-
"""
Created on 9/30/20

@author dor
"""
import datetime

from .type_hints import Datetime


def now() -> Datetime:
    return datetime.datetime.utcnow()
