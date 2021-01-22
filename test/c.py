#-*- coding:utf8 -*-
import sys
from test import *
from .a import A
from .b import B

addons = [
    A(),
    B(),
]

if __name__ == "__main__":
    print(sys.path)