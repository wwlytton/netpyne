"""
framework.py

Contains all the model shared variables and modules.
It is imported as "f" from all other file,  so that any variable or module can be referenced from any module using f.varName

Contributors: salvadordura@gmail.com
"""

from netpyne import sim
from netpyne import analysis
from netpyne.network import Network
from netpyne.cell import Cell, PointNeuron, Pop
