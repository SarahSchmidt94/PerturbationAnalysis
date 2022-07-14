# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 15:20:12 2022

@author: schmidt
"""

import brightway2 as bw
#ILCD 2011: Recommendations for Life Cycle Impact Assessment in the European context

#Global Warming - climate change
GW =[m for m in bw.methods if 'ILCD 2.0 2018 midpoint no LT' in str(m) and  'climate change total' in str(m)][0]

#Ozone depletion - human health
OD =[m for m in bw.methods if 'ILCD 2.0 2018 midpoint no LT' in str(m) and 'ozone layer depletion' in str(m)][0]

#Human toxicity, carcinogenic - human health
HTc =[m for m in bw.methods if 'ILCD 2.0 2018 midpoint no LT' in str(m) and 'carcinogenic effects' in str(m)][0]

#Human toxicity, non-carcinogenic - human health
HTnc =[m for m in bw.methods if 'ILCD 2.0 2018 midpoint no LT' in str(m) and 'non-carcinogenic effects' in str(m)][0]

#Respiratory effects / Particulate Matter - human health
PM = [m for m in bw.methods if 'ILCD 2.0 2018 midpoint no LT' in str(m) and 'respiratory effects, inorganics' in str(m)][0]

#Ionising radiation - human health
IR = [m for m in bw.methods if 'ILCD 2.0 2018 midpoint no LT' in str(m) and 'ionising radiation' in str(m)][0]

#Ionising radiation - ecosystems (no method recommended by ILCD)

#Photochemical ozone formation - human health
POF = [m for m in bw.methods if 'ILCD 2.0 2018 midpoint no LT' in str(m) and 'photochemical ozone creation' in str(m)][0]

#Acidification - ecosystem quality
AC = [m for m in bw.methods if 'ILCD 2.0 2018 midpoint no LT' in str(m) and 'freshwater and terrestrial acidification' in str(m)][0]

#Terrestrial eutrophication - ecosystem quality
TE = [m for m in bw.methods if 'ILCD 2.0 2018 midpoint no LT' in str(m) and 'terrestrial eutrophication' in str(m)][0]

#Freshwater eutrophication - ecosystem quality
FE = [m for m in bw.methods if 'ILCD 2.0 2018 midpoint no LT' in str(m) and 'freshwater eutrophication' in str(m)][0]

#Marine eutrophication - ecosystem quality
ME = [m for m in bw.methods if 'ILCD 2.0 2018 midpoint no LT' in str(m) and 'marine eutrophication' in str(m)][0]

#Ecotoxicity (freshwater) - ecosystem quality
ET = [m for m in bw.methods if 'ILCD 2.0 2018 midpoint no LT' in str(m) and 'freshwater ecotoxicity' in str(m)][0]

# Ecotoxicity (terrestrialand marine) (no method recommended by ILCD)

#Land use - resources
LU = [m for m in bw.methods if 'ILCD 2.0 2018 midpoint no LT' in str(m) and 'land use' in str(m) and 'resources' in str(m)][0]

#Resource depletion, water - resources
RDw = [m for m in bw.methods if 'ILCD 2.0 2018 midpoint no LT' in str(m) and 'dissipated water' in str(m) and 'resources' in str(m)][0]

#Resource depletion, minerals and metals - resources
RDm = [m for m in bw.methods if 'ILCD 2.0 2018 midpoint no LT' in str(m) and 'resources' in str(m) and 'minerals and metals' in str(m)][0]

#Resource depletion, fossils - resources
RDf = [m for m in bw.methods if 'ILCD 2.0 2018 midpoint no LT' in str(m) and 'resources' in str(m) and 'fossils' in str(m)][0]

LCIA_methods = [GW, OD, HTc, HTnc, PM, IR, POF, AC, TE, FE, ME, ET, LU, RDw, RDm, RDf]

IC_names = ['GW', 'OD', 'HTc', 'HTnc', 'PM', 'IR', 'POF', 'AC', 'TE', 'FE', 'ME', 'ET', 'LU', 'RDw', 'RDm', 'RDf']