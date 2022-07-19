#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 16:08:45 2020

@author: gustavo
"""
from math import fabs

def error_abs(exacto, aproximacion):
    return fabs(exacto - aproximacion)


def error_relativo(exacto, aproximacion):
    return (fabs(exacto - aproximacion)/exacto)*100