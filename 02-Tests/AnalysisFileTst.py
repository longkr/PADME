#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for "AnalysisFiles" class
=====================================

  Assumes python path includes PADME code.

  Script starts by testing built in methods.

"""

import os
import AnalysisFile as AnaF


##! Start:
print("========  AnalysisFile: tests start  ========")

##! Check built-in methods:
AnalysisFileTest = 1
print()
print("AnalysisFileTest:", AnalysisFileTest, " check built-in methods.")
#.. __init__
print("    __init__:")
try:
    AnaF00 = AnaF.AnalysisFile()
except:
    print('      ----> Correctly trapped no arguments.')
try:
    AnaF01 = AnaF.AnalysisFile("Rubbish", "File1.txt")
except:
    print('      ----> Correctly trapped no path exception.')
PADMEPATH = os.getenv('PADMEPATH')
filepath  = os.path.join(PADMEPATH, '11-AnalysisFiles')
try:
    AnaF02 = AnaF.AnalysisFile(filepath, "Rubbish")
except:
    print('      ----> Correctly trapped bad file exception.')
try:
    AnaF1 = AnaF.AnalysisFile(filepath, "File1.txt")
except:
    print('      ----> Failed to create instance.')
    raise Exception
#.. __repr__
print("    __repr__:")
#print("      ---->", repr(AnaF1))
print("    <---- __repr__ done.")
#.. __str__
print("    __str__:")
print(str(AnaF1))
print("    <---- __str__ done.")


##! Complete:
print()
print("========  AnalysisFile: tests complete  ========")
