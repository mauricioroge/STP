#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 15:19:57 2018

@author: maco
"""

#!/usr/bin/env python
from lib2to3.fixer_util import String

"""
Usage examples for untangle
"""
import xml.etree.ElementTree as ET

tree =  ET.parse('AustraliaBGHS98.xml')
root = tree.getroot()

for child in root.findall('Instances'):
    instance = child.

