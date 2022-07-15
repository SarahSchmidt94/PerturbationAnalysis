# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 15:20:12 2022

@author: schmidt
"""

import brightway2 as bw

#ILCD 2011: Recommendations for Life Cycle Impact Assessment in the European context

#Global Warming - climate change
GW =[m for m in bw.methods if 'EF v2.0 2018 no LT' in str(m) and  'climate change no LT' in str(m) and 'global warming potential (GWP100) no LT' in str(m)][0]

#Ozone depletion - human health
OD =[m for m in bw.methods if 'EF v2.0 2018 no LT' in str(m) and 'ozone depletion no LT' in str(m) and 'ozone depletion potential (ODP)  no LT' in str(m)][0]

#Human toxicity, carcinogenic - human health
HTc =[m for m in bw.methods if 'EF v2.0 2018 no LT' in str(m) and 'human toxicity: carcinogenic no LT' in str(m) and 'comparative toxic unit for human (CTUh)  no LT' in str(m)][0]

#Human toxicity, non-carcinogenic - human health
HTnc =[m for m in bw.methods if 'EF v2.0 2018 no LT' in str(m) and 'human toxicity: non-carcinogenic no LT' in str(m) and 'comparative toxic unit for human (CTUh)  no LT' in str(m)][0]

#Respiratory effects / Particulate Matter - human health
PM = [m for m in bw.methods if 'EF v2.0 2018 no LT' in str(m) and 'particulate matter formation no LT' in str(m) and 'impact on human health no LT' in str(m)][0]

#Ionising radiation - human health
IR = [m for m in bw.methods if 'EF v2.0 2018 no LT' in str(m) and 'ionising radiation: human health no LT' in str(m) and 'human exposure efficiency relative to u235 no LT' in str(m)][0]

#Ionising radiation - ecosystems (no method recommended by ILCD)

#Photochemical ozone formation - human health
POF = [m for m in bw.methods if 'EF v2.0 2018 no LT' in str(m) and 'photochemical ozone formation: human health no LT' in str(m) and 'tropospheric ozone concentration increase no LT' in str(m)][0]

#Acidification - ecosystem quality
AC = [m for m in bw.methods if 'EF v2.0 2018 no LT' in str(m) and 'acidification no LT' in str(m) and 'accumulated exceedance (ae) no LT' in str(m)][0]

#Terrestrial eutrophication - ecosystem quality
TE = [m for m in bw.methods if 'EF v2.0 2018 no LT' in str(m) and 'eutrophication: terrestrial no LT' in str(m) and 'accumulated exceedance (AE)  no LT' in str(m)][0]

#Freshwater eutrophication - ecosystem quality
FE = [m for m in bw.methods if 'EF v2.0 2018 no LT' in str(m) and 'eutrophication: freshwater no LT' in str(m) and 'fraction of nutrients reaching freshwater end compartment (P) no LT' in str(m)][0]

#Marine eutrophication - ecosystem quality
ME = [m for m in bw.methods if 'EF v2.0 2018 no LT' in str(m) and 'eutrophication: marine no LT' in str(m) and 'fraction of nutrients reaching marine end compartment (N) no LT' in str(m)][0]

#Ecotoxicity (freshwater) - ecosystem quality
ET = [m for m in bw.methods if 'EF v2.0 2018 no LT' in str(m) and 'ecotoxicity: freshwater no LT' in str(m) and 'comparative toxic unit for ecosystems (CTUe)  no LT' in str(m)][0]

# Ecotoxicity (terrestrialand marine) (no method recommended by ILCD)

#Land use - resources
LU = [m for m in bw.methods if 'EF v2.0 2018 no LT' in str(m) and 'land use no LT' in str(m) and 'soil quality index no LT' in str(m)][0]

#Resource depletion, water - resources
RDw = [m for m in bw.methods if 'EF v2.0 2018 no LT' in str(m) and 'water use no LT' in str(m) and 'user deprivation potential (deprivation-weighted water consumption) no LT' in str(m)][0]

#Resource depletion, minerals and metals - resources
RDm = [m for m in bw.methods if 'EF v2.0 2018 no LT' in str(m) and 'material resources: metals/minerals no LT' in str(m) and 'abiotic depletion potential (ADP): elements (ultimate reserves) no LT' in str(m)][0]

#Resource depletion, fossils - resources
RDf = [m for m in bw.methods if 'EF v2.0 2018 no LT' in str(m) and 'energy resources: non-renewable no LT' in str(m) and 'abiotic depletion potential (ADP): fossil fuels no LT' in str(m)][0]

LCIA_methods = [GW, OD, HTc, HTnc, PM, IR, POF, AC, TE, FE, ME, ET, LU, RDw, RDm, RDf]

LCIA_method_names = ['GW', 'OD', 'HTc', 'HTnc', 'PM', 'IR', 'POF', 'AC', 'TE', 'FE', 'ME', 'ET', 'LU', 'RDw', 'RDm', 'RDf']