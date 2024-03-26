

#!/usr/local/bin/python3
# encoding: utf-8

"""
===============================================================================
 Ontology design facility
===============================================================================

This program is part of the ProcessModelling suite

"""

__project__ = "ProcessModeller  Suite"
__author__ = "PREISIG, Heinz A"
__copyright__ = "Copyright 2015, PREISIG, Heinz A"
__since__ = "16.09.2019"
__license__ = "GPL planned -- until further notice for Bio4Fuel & MarketPlace internal use only"
__version__ = "5.04"
__email__ = "heinz.preisig@chemeng.ntnu.no"
__status__ = "beta"


import sys
import os

ProMo_path = os.path.join("../../","ProMo")



root = os.path.abspath(ProMo_path)      #os.path.join("../../"{{ProMo}}) #ProcessModeller_v7_04"))

ext = [root, os.path.join(root, 'packages'), \
             os.path.join(root, 'tasks'), \
             os.path.join(root, 'packages', 'OntologyBuilder', 'EMMO_Integration')
       ]
# print(os.path.join(root, 'packages', 'OntologyBuilder', 'EMMO_Integration'))

# emmo = "/home/heinz/1_Gits/ProcessModeller/ProcessModeller_v7_04/packages/OntologyBuilder/EMMO_Integration/"

sys.path.extend(ext)
from OntologyBuilder.EMMO_Integration.emmo_attach import ProMoOwlOntology
from Common.ontology_container import OntologyContainer

from owlready2 import *

ontology = OntologyContainer("processes_000") #'flash_03')


variables = ontology.variables

name = "play"
owlfile = name+".owl"

# onto  = O.setup_ontology(name)
o = ProMoOwlOntology()
onto = o.setupOnto()

with onto:
  class ProMoVar(onto.VAR):
    pass

  class has_function(ObjectProperty):
    domain = [ProMoVar]
    range  = [ProMoVar]
    pass

  class function(Thing):
    domain  = [ProMoVar]
    range   = [ProMoVar]
    pass

  class is_function_of(ObjectProperty):
    domain = [ProMoVar]
    range  = [ProMoVar]
    pass

# V_1
label = variables[V_1]["label"]
network = variables[V_1]["network"]
variable_type = variables[V_1]["type"]
label = variables[V_1]["label"]
doc = variables[V_1]["doc"]
onto_ID = "V_V_1"
V_V_1 = onto.ProMoVar( onto_ID )
V_V_1.label = label
V_V_1.network = network
V_V_1.variable_type = variable_type
V_V_1.comment = doc

units = variables[V_1]["units"].asList()
V_V_1.time = [ units[0] ]
V_V_1.length = [ units[1] ]
V_V_1.amount = [ units[2] ]
V_V_1.mass = [ units[3] ]
V_V_1.temperature = [ units[4] ]
V_V_1.current = [ units[5] ]
V_V_1.light = [ units[6] ]

# V_10
label = variables[V_10]["label"]
network = variables[V_10]["network"]
variable_type = variables[V_10]["type"]
label = variables[V_10]["label"]
doc = variables[V_10]["doc"]
onto_ID = "V_V_10"
V_V_10 = onto.ProMoVar( onto_ID )
V_V_10.label = label
V_V_10.network = network
V_V_10.variable_type = variable_type
V_V_10.comment = doc

units = variables[V_10]["units"].asList()
V_V_10.time = [ units[0] ]
V_V_10.length = [ units[1] ]
V_V_10.amount = [ units[2] ]
V_V_10.mass = [ units[3] ]
V_V_10.temperature = [ units[4] ]
V_V_10.current = [ units[5] ]
V_V_10.light = [ units[6] ]

# V_11
label = variables[V_11]["label"]
network = variables[V_11]["network"]
variable_type = variables[V_11]["type"]
label = variables[V_11]["label"]
doc = variables[V_11]["doc"]
onto_ID = "V_V_11"
V_V_11 = onto.ProMoVar( onto_ID )
V_V_11.label = label
V_V_11.network = network
V_V_11.variable_type = variable_type
V_V_11.comment = doc

units = variables[V_11]["units"].asList()
V_V_11.time = [ units[0] ]
V_V_11.length = [ units[1] ]
V_V_11.amount = [ units[2] ]
V_V_11.mass = [ units[3] ]
V_V_11.temperature = [ units[4] ]
V_V_11.current = [ units[5] ]
V_V_11.light = [ units[6] ]

# V_2
label = variables[V_2]["label"]
network = variables[V_2]["network"]
variable_type = variables[V_2]["type"]
label = variables[V_2]["label"]
doc = variables[V_2]["doc"]
onto_ID = "V_V_2"
V_V_2 = onto.ProMoVar( onto_ID )
V_V_2.label = label
V_V_2.network = network
V_V_2.variable_type = variable_type
V_V_2.comment = doc

units = variables[V_2]["units"].asList()
V_V_2.time = [ units[0] ]
V_V_2.length = [ units[1] ]
V_V_2.amount = [ units[2] ]
V_V_2.mass = [ units[3] ]
V_V_2.temperature = [ units[4] ]
V_V_2.current = [ units[5] ]
V_V_2.light = [ units[6] ]

# V_3
label = variables[V_3]["label"]
network = variables[V_3]["network"]
variable_type = variables[V_3]["type"]
label = variables[V_3]["label"]
doc = variables[V_3]["doc"]
onto_ID = "V_V_3"
V_V_3 = onto.ProMoVar( onto_ID )
V_V_3.label = label
V_V_3.network = network
V_V_3.variable_type = variable_type
V_V_3.comment = doc

units = variables[V_3]["units"].asList()
V_V_3.time = [ units[0] ]
V_V_3.length = [ units[1] ]
V_V_3.amount = [ units[2] ]
V_V_3.mass = [ units[3] ]
V_V_3.temperature = [ units[4] ]
V_V_3.current = [ units[5] ]
V_V_3.light = [ units[6] ]

# V_4
label = variables[V_4]["label"]
network = variables[V_4]["network"]
variable_type = variables[V_4]["type"]
label = variables[V_4]["label"]
doc = variables[V_4]["doc"]
onto_ID = "V_V_4"
V_V_4 = onto.ProMoVar( onto_ID )
V_V_4.label = label
V_V_4.network = network
V_V_4.variable_type = variable_type
V_V_4.comment = doc

units = variables[V_4]["units"].asList()
V_V_4.time = [ units[0] ]
V_V_4.length = [ units[1] ]
V_V_4.amount = [ units[2] ]
V_V_4.mass = [ units[3] ]
V_V_4.temperature = [ units[4] ]
V_V_4.current = [ units[5] ]
V_V_4.light = [ units[6] ]

# V_5
label = variables[V_5]["label"]
network = variables[V_5]["network"]
variable_type = variables[V_5]["type"]
label = variables[V_5]["label"]
doc = variables[V_5]["doc"]
onto_ID = "V_V_5"
V_V_5 = onto.ProMoVar( onto_ID )
V_V_5.label = label
V_V_5.network = network
V_V_5.variable_type = variable_type
V_V_5.comment = doc

units = variables[V_5]["units"].asList()
V_V_5.time = [ units[0] ]
V_V_5.length = [ units[1] ]
V_V_5.amount = [ units[2] ]
V_V_5.mass = [ units[3] ]
V_V_5.temperature = [ units[4] ]
V_V_5.current = [ units[5] ]
V_V_5.light = [ units[6] ]

# V_6
label = variables[V_6]["label"]
network = variables[V_6]["network"]
variable_type = variables[V_6]["type"]
label = variables[V_6]["label"]
doc = variables[V_6]["doc"]
onto_ID = "V_V_6"
V_V_6 = onto.ProMoVar( onto_ID )
V_V_6.label = label
V_V_6.network = network
V_V_6.variable_type = variable_type
V_V_6.comment = doc

units = variables[V_6]["units"].asList()
V_V_6.time = [ units[0] ]
V_V_6.length = [ units[1] ]
V_V_6.amount = [ units[2] ]
V_V_6.mass = [ units[3] ]
V_V_6.temperature = [ units[4] ]
V_V_6.current = [ units[5] ]
V_V_6.light = [ units[6] ]

# V_7
label = variables[V_7]["label"]
network = variables[V_7]["network"]
variable_type = variables[V_7]["type"]
label = variables[V_7]["label"]
doc = variables[V_7]["doc"]
onto_ID = "V_V_7"
V_V_7 = onto.ProMoVar( onto_ID )
V_V_7.label = label
V_V_7.network = network
V_V_7.variable_type = variable_type
V_V_7.comment = doc

units = variables[V_7]["units"].asList()
V_V_7.time = [ units[0] ]
V_V_7.length = [ units[1] ]
V_V_7.amount = [ units[2] ]
V_V_7.mass = [ units[3] ]
V_V_7.temperature = [ units[4] ]
V_V_7.current = [ units[5] ]
V_V_7.light = [ units[6] ]

# V_8
label = variables[V_8]["label"]
network = variables[V_8]["network"]
variable_type = variables[V_8]["type"]
label = variables[V_8]["label"]
doc = variables[V_8]["doc"]
onto_ID = "V_V_8"
V_V_8 = onto.ProMoVar( onto_ID )
V_V_8.label = label
V_V_8.network = network
V_V_8.variable_type = variable_type
V_V_8.comment = doc

units = variables[V_8]["units"].asList()
V_V_8.time = [ units[0] ]
V_V_8.length = [ units[1] ]
V_V_8.amount = [ units[2] ]
V_V_8.mass = [ units[3] ]
V_V_8.temperature = [ units[4] ]
V_V_8.current = [ units[5] ]
V_V_8.light = [ units[6] ]

# V_9
label = variables[V_9]["label"]
network = variables[V_9]["network"]
variable_type = variables[V_9]["type"]
label = variables[V_9]["label"]
doc = variables[V_9]["doc"]
onto_ID = "V_V_9"
V_V_9 = onto.ProMoVar( onto_ID )
V_V_9.label = label
V_V_9.network = network
V_V_9.variable_type = variable_type
V_V_9.comment = doc

units = variables[V_9]["units"].asList()
V_V_9.time = [ units[0] ]
V_V_9.length = [ units[1] ]
V_V_9.amount = [ units[2] ]
V_V_9.mass = [ units[3] ]
V_V_9.temperature = [ units[4] ]
V_V_9.current = [ units[5] ]
V_V_9.light = [ units[6] ]

# V_101
label = variables[V_101]["label"]
network = variables[V_101]["network"]
variable_type = variables[V_101]["type"]
label = variables[V_101]["label"]
doc = variables[V_101]["doc"]
onto_ID = "V_V_101"
V_V_101 = onto.ProMoVar( onto_ID )
V_V_101.label = label
V_V_101.network = network
V_V_101.variable_type = variable_type
V_V_101.comment = doc

units = variables[V_101]["units"].asList()
V_V_101.time = [ units[0] ]
V_V_101.length = [ units[1] ]
V_V_101.amount = [ units[2] ]
V_V_101.mass = [ units[3] ]
V_V_101.temperature = [ units[4] ]
V_V_101.current = [ units[5] ]
V_V_101.light = [ units[6] ]

# V_102
label = variables[V_102]["label"]
network = variables[V_102]["network"]
variable_type = variables[V_102]["type"]
label = variables[V_102]["label"]
doc = variables[V_102]["doc"]
onto_ID = "V_V_102"
V_V_102 = onto.ProMoVar( onto_ID )
V_V_102.label = label
V_V_102.network = network
V_V_102.variable_type = variable_type
V_V_102.comment = doc

units = variables[V_102]["units"].asList()
V_V_102.time = [ units[0] ]
V_V_102.length = [ units[1] ]
V_V_102.amount = [ units[2] ]
V_V_102.mass = [ units[3] ]
V_V_102.temperature = [ units[4] ]
V_V_102.current = [ units[5] ]
V_V_102.light = [ units[6] ]

# V_103
label = variables[V_103]["label"]
network = variables[V_103]["network"]
variable_type = variables[V_103]["type"]
label = variables[V_103]["label"]
doc = variables[V_103]["doc"]
onto_ID = "V_V_103"
V_V_103 = onto.ProMoVar( onto_ID )
V_V_103.label = label
V_V_103.network = network
V_V_103.variable_type = variable_type
V_V_103.comment = doc

units = variables[V_103]["units"].asList()
V_V_103.time = [ units[0] ]
V_V_103.length = [ units[1] ]
V_V_103.amount = [ units[2] ]
V_V_103.mass = [ units[3] ]
V_V_103.temperature = [ units[4] ]
V_V_103.current = [ units[5] ]
V_V_103.light = [ units[6] ]

# V_104
label = variables[V_104]["label"]
network = variables[V_104]["network"]
variable_type = variables[V_104]["type"]
label = variables[V_104]["label"]
doc = variables[V_104]["doc"]
onto_ID = "V_V_104"
V_V_104 = onto.ProMoVar( onto_ID )
V_V_104.label = label
V_V_104.network = network
V_V_104.variable_type = variable_type
V_V_104.comment = doc

units = variables[V_104]["units"].asList()
V_V_104.time = [ units[0] ]
V_V_104.length = [ units[1] ]
V_V_104.amount = [ units[2] ]
V_V_104.mass = [ units[3] ]
V_V_104.temperature = [ units[4] ]
V_V_104.current = [ units[5] ]
V_V_104.light = [ units[6] ]

# V_105
label = variables[V_105]["label"]
network = variables[V_105]["network"]
variable_type = variables[V_105]["type"]
label = variables[V_105]["label"]
doc = variables[V_105]["doc"]
onto_ID = "V_V_105"
V_V_105 = onto.ProMoVar( onto_ID )
V_V_105.label = label
V_V_105.network = network
V_V_105.variable_type = variable_type
V_V_105.comment = doc

units = variables[V_105]["units"].asList()
V_V_105.time = [ units[0] ]
V_V_105.length = [ units[1] ]
V_V_105.amount = [ units[2] ]
V_V_105.mass = [ units[3] ]
V_V_105.temperature = [ units[4] ]
V_V_105.current = [ units[5] ]
V_V_105.light = [ units[6] ]

# V_106
label = variables[V_106]["label"]
network = variables[V_106]["network"]
variable_type = variables[V_106]["type"]
label = variables[V_106]["label"]
doc = variables[V_106]["doc"]
onto_ID = "V_V_106"
V_V_106 = onto.ProMoVar( onto_ID )
V_V_106.label = label
V_V_106.network = network
V_V_106.variable_type = variable_type
V_V_106.comment = doc

units = variables[V_106]["units"].asList()
V_V_106.time = [ units[0] ]
V_V_106.length = [ units[1] ]
V_V_106.amount = [ units[2] ]
V_V_106.mass = [ units[3] ]
V_V_106.temperature = [ units[4] ]
V_V_106.current = [ units[5] ]
V_V_106.light = [ units[6] ]

# V_107
label = variables[V_107]["label"]
network = variables[V_107]["network"]
variable_type = variables[V_107]["type"]
label = variables[V_107]["label"]
doc = variables[V_107]["doc"]
onto_ID = "V_V_107"
V_V_107 = onto.ProMoVar( onto_ID )
V_V_107.label = label
V_V_107.network = network
V_V_107.variable_type = variable_type
V_V_107.comment = doc

units = variables[V_107]["units"].asList()
V_V_107.time = [ units[0] ]
V_V_107.length = [ units[1] ]
V_V_107.amount = [ units[2] ]
V_V_107.mass = [ units[3] ]
V_V_107.temperature = [ units[4] ]
V_V_107.current = [ units[5] ]
V_V_107.light = [ units[6] ]

# V_108
label = variables[V_108]["label"]
network = variables[V_108]["network"]
variable_type = variables[V_108]["type"]
label = variables[V_108]["label"]
doc = variables[V_108]["doc"]
onto_ID = "V_V_108"
V_V_108 = onto.ProMoVar( onto_ID )
V_V_108.label = label
V_V_108.network = network
V_V_108.variable_type = variable_type
V_V_108.comment = doc

units = variables[V_108]["units"].asList()
V_V_108.time = [ units[0] ]
V_V_108.length = [ units[1] ]
V_V_108.amount = [ units[2] ]
V_V_108.mass = [ units[3] ]
V_V_108.temperature = [ units[4] ]
V_V_108.current = [ units[5] ]
V_V_108.light = [ units[6] ]

# V_109
label = variables[V_109]["label"]
network = variables[V_109]["network"]
variable_type = variables[V_109]["type"]
label = variables[V_109]["label"]
doc = variables[V_109]["doc"]
onto_ID = "V_V_109"
V_V_109 = onto.ProMoVar( onto_ID )
V_V_109.label = label
V_V_109.network = network
V_V_109.variable_type = variable_type
V_V_109.comment = doc

units = variables[V_109]["units"].asList()
V_V_109.time = [ units[0] ]
V_V_109.length = [ units[1] ]
V_V_109.amount = [ units[2] ]
V_V_109.mass = [ units[3] ]
V_V_109.temperature = [ units[4] ]
V_V_109.current = [ units[5] ]
V_V_109.light = [ units[6] ]

# V_110
label = variables[V_110]["label"]
network = variables[V_110]["network"]
variable_type = variables[V_110]["type"]
label = variables[V_110]["label"]
doc = variables[V_110]["doc"]
onto_ID = "V_V_110"
V_V_110 = onto.ProMoVar( onto_ID )
V_V_110.label = label
V_V_110.network = network
V_V_110.variable_type = variable_type
V_V_110.comment = doc

units = variables[V_110]["units"].asList()
V_V_110.time = [ units[0] ]
V_V_110.length = [ units[1] ]
V_V_110.amount = [ units[2] ]
V_V_110.mass = [ units[3] ]
V_V_110.temperature = [ units[4] ]
V_V_110.current = [ units[5] ]
V_V_110.light = [ units[6] ]

# V_111
label = variables[V_111]["label"]
network = variables[V_111]["network"]
variable_type = variables[V_111]["type"]
label = variables[V_111]["label"]
doc = variables[V_111]["doc"]
onto_ID = "V_V_111"
V_V_111 = onto.ProMoVar( onto_ID )
V_V_111.label = label
V_V_111.network = network
V_V_111.variable_type = variable_type
V_V_111.comment = doc

units = variables[V_111]["units"].asList()
V_V_111.time = [ units[0] ]
V_V_111.length = [ units[1] ]
V_V_111.amount = [ units[2] ]
V_V_111.mass = [ units[3] ]
V_V_111.temperature = [ units[4] ]
V_V_111.current = [ units[5] ]
V_V_111.light = [ units[6] ]

# V_112
label = variables[V_112]["label"]
network = variables[V_112]["network"]
variable_type = variables[V_112]["type"]
label = variables[V_112]["label"]
doc = variables[V_112]["doc"]
onto_ID = "V_V_112"
V_V_112 = onto.ProMoVar( onto_ID )
V_V_112.label = label
V_V_112.network = network
V_V_112.variable_type = variable_type
V_V_112.comment = doc

units = variables[V_112]["units"].asList()
V_V_112.time = [ units[0] ]
V_V_112.length = [ units[1] ]
V_V_112.amount = [ units[2] ]
V_V_112.mass = [ units[3] ]
V_V_112.temperature = [ units[4] ]
V_V_112.current = [ units[5] ]
V_V_112.light = [ units[6] ]

# V_113
label = variables[V_113]["label"]
network = variables[V_113]["network"]
variable_type = variables[V_113]["type"]
label = variables[V_113]["label"]
doc = variables[V_113]["doc"]
onto_ID = "V_V_113"
V_V_113 = onto.ProMoVar( onto_ID )
V_V_113.label = label
V_V_113.network = network
V_V_113.variable_type = variable_type
V_V_113.comment = doc

units = variables[V_113]["units"].asList()
V_V_113.time = [ units[0] ]
V_V_113.length = [ units[1] ]
V_V_113.amount = [ units[2] ]
V_V_113.mass = [ units[3] ]
V_V_113.temperature = [ units[4] ]
V_V_113.current = [ units[5] ]
V_V_113.light = [ units[6] ]

# V_114
label = variables[V_114]["label"]
network = variables[V_114]["network"]
variable_type = variables[V_114]["type"]
label = variables[V_114]["label"]
doc = variables[V_114]["doc"]
onto_ID = "V_V_114"
V_V_114 = onto.ProMoVar( onto_ID )
V_V_114.label = label
V_V_114.network = network
V_V_114.variable_type = variable_type
V_V_114.comment = doc

units = variables[V_114]["units"].asList()
V_V_114.time = [ units[0] ]
V_V_114.length = [ units[1] ]
V_V_114.amount = [ units[2] ]
V_V_114.mass = [ units[3] ]
V_V_114.temperature = [ units[4] ]
V_V_114.current = [ units[5] ]
V_V_114.light = [ units[6] ]

# V_115
label = variables[V_115]["label"]
network = variables[V_115]["network"]
variable_type = variables[V_115]["type"]
label = variables[V_115]["label"]
doc = variables[V_115]["doc"]
onto_ID = "V_V_115"
V_V_115 = onto.ProMoVar( onto_ID )
V_V_115.label = label
V_V_115.network = network
V_V_115.variable_type = variable_type
V_V_115.comment = doc

units = variables[V_115]["units"].asList()
V_V_115.time = [ units[0] ]
V_V_115.length = [ units[1] ]
V_V_115.amount = [ units[2] ]
V_V_115.mass = [ units[3] ]
V_V_115.temperature = [ units[4] ]
V_V_115.current = [ units[5] ]
V_V_115.light = [ units[6] ]

# V_116
label = variables[V_116]["label"]
network = variables[V_116]["network"]
variable_type = variables[V_116]["type"]
label = variables[V_116]["label"]
doc = variables[V_116]["doc"]
onto_ID = "V_V_116"
V_V_116 = onto.ProMoVar( onto_ID )
V_V_116.label = label
V_V_116.network = network
V_V_116.variable_type = variable_type
V_V_116.comment = doc

units = variables[V_116]["units"].asList()
V_V_116.time = [ units[0] ]
V_V_116.length = [ units[1] ]
V_V_116.amount = [ units[2] ]
V_V_116.mass = [ units[3] ]
V_V_116.temperature = [ units[4] ]
V_V_116.current = [ units[5] ]
V_V_116.light = [ units[6] ]

# V_117
label = variables[V_117]["label"]
network = variables[V_117]["network"]
variable_type = variables[V_117]["type"]
label = variables[V_117]["label"]
doc = variables[V_117]["doc"]
onto_ID = "V_V_117"
V_V_117 = onto.ProMoVar( onto_ID )
V_V_117.label = label
V_V_117.network = network
V_V_117.variable_type = variable_type
V_V_117.comment = doc

units = variables[V_117]["units"].asList()
V_V_117.time = [ units[0] ]
V_V_117.length = [ units[1] ]
V_V_117.amount = [ units[2] ]
V_V_117.mass = [ units[3] ]
V_V_117.temperature = [ units[4] ]
V_V_117.current = [ units[5] ]
V_V_117.light = [ units[6] ]

# V_118
label = variables[V_118]["label"]
network = variables[V_118]["network"]
variable_type = variables[V_118]["type"]
label = variables[V_118]["label"]
doc = variables[V_118]["doc"]
onto_ID = "V_V_118"
V_V_118 = onto.ProMoVar( onto_ID )
V_V_118.label = label
V_V_118.network = network
V_V_118.variable_type = variable_type
V_V_118.comment = doc

units = variables[V_118]["units"].asList()
V_V_118.time = [ units[0] ]
V_V_118.length = [ units[1] ]
V_V_118.amount = [ units[2] ]
V_V_118.mass = [ units[3] ]
V_V_118.temperature = [ units[4] ]
V_V_118.current = [ units[5] ]
V_V_118.light = [ units[6] ]

# V_119
label = variables[V_119]["label"]
network = variables[V_119]["network"]
variable_type = variables[V_119]["type"]
label = variables[V_119]["label"]
doc = variables[V_119]["doc"]
onto_ID = "V_V_119"
V_V_119 = onto.ProMoVar( onto_ID )
V_V_119.label = label
V_V_119.network = network
V_V_119.variable_type = variable_type
V_V_119.comment = doc

units = variables[V_119]["units"].asList()
V_V_119.time = [ units[0] ]
V_V_119.length = [ units[1] ]
V_V_119.amount = [ units[2] ]
V_V_119.mass = [ units[3] ]
V_V_119.temperature = [ units[4] ]
V_V_119.current = [ units[5] ]
V_V_119.light = [ units[6] ]

# V_120
label = variables[V_120]["label"]
network = variables[V_120]["network"]
variable_type = variables[V_120]["type"]
label = variables[V_120]["label"]
doc = variables[V_120]["doc"]
onto_ID = "V_V_120"
V_V_120 = onto.ProMoVar( onto_ID )
V_V_120.label = label
V_V_120.network = network
V_V_120.variable_type = variable_type
V_V_120.comment = doc

units = variables[V_120]["units"].asList()
V_V_120.time = [ units[0] ]
V_V_120.length = [ units[1] ]
V_V_120.amount = [ units[2] ]
V_V_120.mass = [ units[3] ]
V_V_120.temperature = [ units[4] ]
V_V_120.current = [ units[5] ]
V_V_120.light = [ units[6] ]

# functions assignments

#V_1

V_V_1.has_function = []
#V_10

V_V_10.has_function = []
#V_11

V_V_11.has_function = []
#V_2

V_V_2.has_function = []
#V_3

V_V_3.has_function = []
#V_4

V_V_4.has_function = []
#V_5

V_V_5.has_function = []
#V_6

V_V_6.has_function = []
#V_7

V_V_7.has_function = []
#V_8

V_V_8.has_function = []
#V_9

V_V_9.has_function = []
#V_101

V_V_101.has_function = []
#V_102

V_V_102.has_function = []
incidence_list = []
incidence_list.append( V_101 )
incidence_list.append( V_101 )
F_ID = "F_E_1"
F_E_1 = onto.function( F_ID )
F_E_1.is_function_of = incidence_list
V_V_102.has_function.append( F_E_1 )
#V_103

V_V_103.has_function = []
incidence_list = []
incidence_list.append( V_101 )
incidence_list.append( V_101 )
F_ID = "F_E_2"
F_E_2 = onto.function( F_ID )
F_E_2.is_function_of = incidence_list
V_V_103.has_function.append( F_E_2 )
#V_104

V_V_104.has_function = []
incidence_list = []
incidence_list.append( V_101 )
incidence_list.append( V_101 )
F_ID = "F_E_3"
F_E_3 = onto.function( F_ID )
F_E_3.is_function_of = incidence_list
V_V_104.has_function.append( F_E_3 )
#V_105

V_V_105.has_function = []
#V_106

V_V_106.has_function = []
#V_107

V_V_107.has_function = []
#V_108

V_V_108.has_function = []
incidence_list = []
incidence_list.append( V_9 )
incidence_list.append( V_10 )
incidence_list.append( V_11 )
F_ID = "F_E_4"
F_E_4 = onto.function( F_ID )
F_E_4.is_function_of = incidence_list
V_V_108.has_function.append( F_E_4 )
#V_109

V_V_109.has_function = []
incidence_list = []
incidence_list.append( V_105 )
incidence_list.append( V_108 )
F_ID = "F_E_5"
F_E_5 = onto.function( F_ID )
F_E_5.is_function_of = incidence_list
V_V_109.has_function.append( F_E_5 )
#V_110

V_V_110.has_function = []
incidence_list = []
incidence_list.append( V_105 )
incidence_list.append( V_106 )
F_ID = "F_E_6"
F_E_6 = onto.function( F_ID )
F_E_6.is_function_of = incidence_list
V_V_110.has_function.append( F_E_6 )
#V_111

V_V_111.has_function = []
incidence_list = []
incidence_list.append( V_105 )
incidence_list.append( V_107 )
F_ID = "F_E_7"
F_E_7 = onto.function( F_ID )
F_E_7.is_function_of = incidence_list
V_V_111.has_function.append( F_E_7 )
#V_112

V_V_112.has_function = []
incidence_list = []
incidence_list.append( V_105 )
incidence_list.append( V_109 )
incidence_list.append( V_108 )
F_ID = "F_E_8"
F_E_8 = onto.function( F_ID )
F_E_8.is_function_of = incidence_list
V_V_112.has_function.append( F_E_8 )
#V_113

V_V_113.has_function = []
incidence_list = []
incidence_list.append( V_105 )
incidence_list.append( V_110 )
incidence_list.append( V_106 )
F_ID = "F_E_9"
F_E_9 = onto.function( F_ID )
F_E_9.is_function_of = incidence_list
V_V_113.has_function.append( F_E_9 )
#V_114

V_V_114.has_function = []
incidence_list = []
incidence_list.append( V_105 )
incidence_list.append( V_109 )
incidence_list.append( V_108 )
incidence_list.append( V_110 )
incidence_list.append( V_106 )
F_ID = "F_E_10"
F_E_10 = onto.function( F_ID )
F_E_10.is_function_of = incidence_list
V_V_114.has_function.append( F_E_10 )
#V_115

V_V_115.has_function = []
incidence_list = []
incidence_list.append( V_1 )
incidence_list.append( V_9 )
F_ID = "F_E_11"
F_E_11 = onto.function( F_ID )
F_E_11.is_function_of = incidence_list
V_V_115.has_function.append( F_E_11 )
incidence_list = []
incidence_list.append( V_9 )
incidence_list.append( V_1 )
F_ID = "F_E_16"
F_E_16 = onto.function( F_ID )
F_E_16.is_function_of = incidence_list
V_V_115.has_function.append( F_E_16 )
#V_116

V_V_116.has_function = []
incidence_list = []
incidence_list.append( V_1 )
incidence_list.append( V_10 )
F_ID = "F_E_12"
F_E_12 = onto.function( F_ID )
F_E_12.is_function_of = incidence_list
V_V_116.has_function.append( F_E_12 )
incidence_list = []
incidence_list.append( V_10 )
incidence_list.append( V_1 )
F_ID = "F_E_17"
F_E_17 = onto.function( F_ID )
F_E_17.is_function_of = incidence_list
V_V_116.has_function.append( F_E_17 )
#V_117

V_V_117.has_function = []
incidence_list = []
incidence_list.append( V_1 )
incidence_list.append( V_11 )
F_ID = "F_E_13"
F_E_13 = onto.function( F_ID )
F_E_13.is_function_of = incidence_list
V_V_117.has_function.append( F_E_13 )
incidence_list = []
incidence_list.append( V_11 )
incidence_list.append( V_1 )
F_ID = "F_E_18"
F_E_18 = onto.function( F_ID )
F_E_18.is_function_of = incidence_list
V_V_117.has_function.append( F_E_18 )
#V_118

V_V_118.has_function = []
incidence_list = []
incidence_list.append( V_106 )
incidence_list.append( V_101 )
F_ID = "F_E_14"
F_E_14 = onto.function( F_ID )
F_E_14.is_function_of = incidence_list
V_V_118.has_function.append( F_E_14 )
#V_119

V_V_119.has_function = []
#V_120

V_V_120.has_function = []
incidence_list = []
incidence_list.append( V_119 )
incidence_list.append( V_118 )
F_ID = "F_E_15"
F_E_15 = onto.function( F_ID )
F_E_15.is_function_of = incidence_list
V_V_120.has_function.append( F_E_15 )

onto.save("variables.owl")
