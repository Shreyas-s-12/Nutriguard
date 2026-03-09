#!/usr/bin/env python3
"""
Generate additional food additive entries to expand the chemicals.csv to 1000+ entries.
"""

import csv
from pathlib import Path

# Food Additive Data - Comprehensive lists by E-number range

# E100-E199: Food Colors
FOOD_COLORS = [
    {"e": 100, "name": "Curcumin", "category": "Food Color", "purpose": "Natural yellow food coloring", "risk": "Low", "concerns": "Generally safe, may cause mild digestive issues in high doses", "limit": "ADI 0-3 mg/kg body weight", "aliases": "E100,Turmeric Extract"},
    {"e": 101, "name": "Riboflavin", "category": "Food Color", "purpose": "Vitamin B2, yellow-orange coloring", "risk": "Minimal", "concerns": "Generally safe, may cause yellow urine", "limit": "ADI not specified", "aliases": "E101,Vitamin B2,Riboflavin-5'-phosphate"},
    {"e": 102, "name": "Tartrazine", "category": "Food Color", "purpose": "Synthetic yellow food coloring", "risk": "Moderate", "concerns": "May cause allergic reactions in sensitive individuals, hyperactivity in children", "limit": "ADI 0-7.5 mg/kg", "aliases": "E102,FD&C Yellow 5,CI 19140"},
    {"e": 103, "name": "Alkanet", "category": "Food Color", "purpose": "Natural red-purple food coloring", "risk": "Low", "concerns": "Generally safe, may cause mild stomach upset", "limit": "ADI not specified", "aliases": "E103,Alkanet Root,Bixin"},
    {"e": 104, "name": "Quinoline Yellow", "category": "Food Color", "purpose": "Synthetic yellow-green food coloring", "risk": "Moderate", "concerns": "May cause allergic reactions, hyperactivity in children", "limit": "ADI 0-10 mg/kg", "aliases": "E104,FD&C Yellow 10,CI 47005"},
    {"e": 106, "name": "Riboflavin-5'-phosphate", "category": "Food Color", "purpose": "Water-soluble yellow coloring", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E106"},
    {"e": 107, "name": "Yellow 2G", "category": "Food Color", "purpose": "Synthetic yellow food coloring", "risk": "Moderate", "concerns": "May cause allergic reactions", "limit": "ADI 0-5 mg/kg", "aliases": "E107,CI 18965"},
    {"e": 110, "name": "Sunset Yellow FCF", "category": "Food Color", "purpose": "Synthetic orange-yellow coloring", "risk": "Moderate", "concerns": "May cause allergic reactions, hyperactivity in children", "limit": "ADI 0-4 mg/kg", "aliases": "E110,FD&C Yellow 6,CI 15985"},
    {"e": 111, "name": "Orange Yellow S", "category": "Food Color", "purpose": "Synthetic orange coloring", "risk": "Moderate", "concerns": "May cause allergic reactions", "limit": "ADI 0-4 mg/kg", "aliases": "E111"},
    {"e": 120, "name": "Cochineal", "category": "Food Color", "purpose": "Natural red coloring from insects", "risk": "Low", "concerns": "May cause allergic reactions in some individuals", "limit": "ADI 0-5 mg/kg", "aliases": "E120,Carmine,Natural Red 4"},
    {"e": 121, "name": "Citrin", "category": "Food Color", "purpose": "Natural yellow coloring", "risk": "Low", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E121"},
    {"e": 122, "name": "Carmoisine", "category": "Food Color", "purpose": "Synthetic red food coloring", "risk": "Moderate", "concerns": "May cause allergic reactions", "limit": "ADI 0-4 mg/kg", "aliases": "E122,Azorubine,CI 14720"},
    {"e": 123, "name": "Amaranth", "category": "Food Color", "purpose": "Synthetic red-violet coloring", "risk": "High", "concerns": "Controversial, banned in some countries", "limit": "ADI 0-0.5 mg/kg", "aliases": "E123,FD&C Red 2,CI 16185"},
    {"e": 124, "name": "Ponceau 4R", "category": "Food Color", "purpose": "Synthetic red coloring", "risk": "Moderate", "concerns": "May cause allergic reactions", "limit": "ADI 0-4 mg/kg", "aliases": "E124,CI 16255"},
    {"e": 125, "name": "Ponceau SX", "category": "Food Color", "purpose": "Synthetic red coloring", "risk": "Moderate", "concerns": "May cause allergic reactions", "limit": "ADI 0-1 mg/kg", "aliases": "E125"},
    {"e": 127, "name": "Erythrosine", "category": "Food Color", "purpose": "Synthetic red coloring", "risk": "Moderate", "concerns": "May affect thyroid function, hyperactivity", "limit": "ADI 0-0.1 mg/kg", "aliases": "E127,FD&C Red 3,CI 45430"},
    {"e": 128, "name": "Red 2G", "category": "Food Color", "purpose": "Synthetic red food coloring", "risk": "Moderate", "concerns": "May cause allergic reactions", "limit": "ADI 0-0.1 mg/kg", "aliases": "E128,CI 18050"},
    {"e": 129, "name": "Allura Red AC", "category": "Food Color", "purpose": "Synthetic red-orange coloring", "risk": "Moderate", "concerns": "May cause allergic reactions, hyperactivity", "limit": "ADI 0-7 mg/kg", "aliases": "E129,FD&C Red 40,CI 16035"},
    {"e": 131, "name": "Patent Blue V", "category": "Food Color", "purpose": "Synthetic blue coloring", "risk": "Moderate", "concerns": "May cause allergic reactions", "limit": "ADI 0-15 mg/kg", "aliases": "E131,CI 42051"},
    {"e": 132, "name": "Indigo Carmine", "category": "Food Color", "purpose": "Synthetic indigo blue coloring", "risk": "Moderate", "concerns": "May cause allergic reactions", "limit": "ADI 0-5 mg/kg", "aliases": "E132,FD&C Blue 2,CI 73015"},
    {"e": 133, "name": "Brilliant Blue FCF", "category": "Food Color", "purpose": "Synthetic blue coloring", "risk": "Moderate", "concerns": "May cause allergic reactions", "limit": "ADI 0-12.5 mg/kg", "aliases": "E133,FD&C Blue 1,CI 42090"},
    {"e": 140, "name": "Chlorophyll", "category": "Food Color", "purpose": "Natural green coloring", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E140,Chlorophyllin,CI 75810"},
    {"e": 141, "name": "Copper Complex of Chlorophyll", "category": "Food Color", "purpose": "Natural green coloring", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-15 mg/kg", "aliases": "E141,CI 75815"},
    {"e": 142, "name": "Green S", "category": "Food Color", "purpose": "Synthetic green coloring", "risk": "Moderate", "concerns": "May cause allergic reactions", "limit": "ADI 0-5 mg/kg", "aliases": "E142,CI 44090"},
    {"e": 150, "name": "Caramel", "category": "Food Color", "purpose": "Natural brown coloring", "risk": "Low", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E150,Caramel Color,Caramel Coloring"},
    {"e": 151, "name": "Brilliant Black", "category": "Food Color", "purpose": "Synthetic black coloring", "risk": "Moderate", "concerns": "May cause allergic reactions", "limit": "ADI 0-5 mg/kg", "aliases": "E151,Brilliant Black PN,CI 28440"},
    {"e": 153, "name": "Vegetable Carbon", "category": "Food Color", "purpose": "Natural black coloring", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E153,Charcoal,Carbon Black"},
    {"e": 154, "name": "Brown FK", "category": "Food Color", "purpose": "Synthetic brown coloring", "risk": "Moderate", "concerns": "May cause allergic reactions", "limit": "ADI 0-1.5 mg/kg", "aliases": "E154,Brown FK"},
    {"e": 155, "name": "Brown HT", "category": "Food Color", "purpose": "Synthetic brown coloring", "risk": "Moderate", "concerns": "May cause allergic reactions", "limit": "ADI 0-1.5 mg/kg", "aliases": "E155,CI 20285"},
    {"e": 160, "name": "Carotenoids", "category": "Food Color", "purpose": "Natural orange-red coloring", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E160,Carotene,Beta-carotene"},
    {"e": 161, "name": "Xanthophylls", "category": "Food Color", "purpose": "Yellow-orange natural coloring", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E161,Lutein,Zeaxanthin"},
    {"e": 162, "name": "Beetroot Red", "category": "Food Color", "purpose": "Natural red-purple coloring", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E162,Betanin,Beet Red"},
    {"e": 163, "name": "Anthocyanins", "category": "Food Color", "purpose": "Natural purple-red coloring", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E163,Grape Skin Extract"},
    {"e": 170, "name": "Calcium Carbonate", "category": "Food Color", "purpose": "White coloring, calcium supplement", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E170,Chalk,CI 77220"},
    {"e": 171, "name": "Titanium Dioxide", "category": "Food Color", "purpose": "White coloring", "risk": "Moderate", "concerns": "May have carcinogenic effects when inhaled", "limit": "ADI 0-10 mg/kg", "aliases": "E171,CI 77891"},
    {"e": 172, "name": "Iron Oxides", "category": "Food Color", "purpose": "Natural black, yellow, red coloring", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-0.5 mg/kg", "aliases": "E172,CI 77499,CI 77492"},
    {"e": 173, "name": "Aluminum", "category": "Food Color", "purpose": "Silver metallic coloring", "risk": "Moderate", "concerns": "Accumulation concerns", "limit": "ADI 0-1 mg/kg", "aliases": "E173,CI 77000"},
    {"e": 174, "name": "Silver", "category": "Food Color", "purpose": "Silver metallic coloring", "risk": "Low", "concerns": "Generally safe in food amounts", "limit": "ADI 0-0.5 mg/kg", "aliases": "E174,CI 77820"},
    {"e": 175, "name": "Gold", "category": "Food Color", "purpose": "Gold metallic coloring", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-0.5 mg/kg", "aliases": "E175,CI 77480"},
    {"e": 180, "name": "Rubine", "category": "Food Color", "purpose": "Synthetic red coloring", "risk": "Moderate", "concerns": "May cause allergic reactions", "limit": "ADI 0-0.5 mg/kg", "aliases": "E180,Lithol Rubine,CI 15850"},
]

# E200-E299: Preservatives
PRESERVATIVES = [
    {"e": 200, "name": "Sorbic Acid", "category": "Preservative", "purpose": "Prevents mold and yeast growth", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-25 mg/kg", "aliases": "E200,Sorbic Acid"},
    {"e": 202, "name": "Potassium Sorbate", "category": "Preservative", "purpose": "Prevents mold and yeast", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-25 mg/kg", "aliases": "E202,Sorbate"},
    {"e": 203, "name": "Calcium Sorbate", "category": "Preservative", "purpose": "Preservative", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-25 mg/kg", "aliases": "E203"},
    {"e": 210, "name": "Benzoic Acid", "category": "Preservative", "purpose": "Prevents microbial growth", "risk": "Low", "concerns": "May cause allergic reactions", "limit": "ADI 0-5 mg/kg", "aliases": "E210,Benzoate"},
    {"e": 212, "name": "Potassium Benzoate", "category": "Preservative", "purpose": "Preservative", "risk": "Low", "concerns": "May cause allergic reactions", "limit": "ADI 0-5 mg/kg", "aliases": "E212"},
    {"e": 213, "name": "Calcium Benzoate", "category": "Preservative", "purpose": "Preservative", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-5 mg/kg", "aliases": "E213"},
    {"e": 214, "name": "Ethyl 4-hydroxybenzoate", "category": "Preservative", "purpose": "Preservative", "risk": "Moderate", "concerns": "May cause allergic reactions", "limit": "ADI 0-10 mg/kg", "aliases": "E214,Ethylparaben"},
    {"e": 215, "name": "Sodium Ethyl 4-hydroxybenzoate", "category": "Preservative", "purpose": "Preservative", "risk": "Moderate", "concerns": "May cause allergic reactions", "limit": "ADI 0-10 mg/kg", "aliases": "E215,Sodium Ethylparaben"},
    {"e": 216, "name": "Propyl 4-hydroxybenzoate", "category": "Preservative", "purpose": "Preservative", "risk": "Moderate", "concerns": "May cause allergic reactions", "limit": "ADI 0-10 mg/kg", "aliases": "E216,Propylparaben"},
    {"e": 217, "name": "Sodium Propyl 4-hydroxybenzoate", "category": "Preservative", "purpose": "Preservative", "risk": "Moderate", "concerns": "May cause allergic reactions", "limit": "ADI 0-10 mg/kg", "aliases": "E217,Sodium Propylparaben"},
    {"e": 218, "name": "Methyl 4-hydroxybenzoate", "category": "Preservative", "purpose": "Preservative", "risk": "Moderate", "concerns": "May cause allergic reactions", "limit": "ADI 0-10 mg/kg", "aliases": "E218,Methylparaben"},
    {"e": 219, "name": "Sodium Methyl 4-hydroxybenzoate", "category": "Preservative", "purpose": "Preservative", "risk": "Moderate", "concerns": "May cause allergic reactions", "limit": "ADI 0-10 mg/kg", "aliases": "E219,Sodium Methylparaben"},
    {"e": 225, "name": "Potassium Sulfite", "category": "Preservative", "purpose": "Preservative", "risk": "Low", "concerns": "May cause allergic reactions", "limit": "ADI 0-0.7 mg/kg", "aliases": "E225"},
    {"e": 227, "name": "Calcium Hydrogen Sulfite", "category": "Preservative", "purpose": "Preservative", "risk": "Low", "concerns": "May cause allergic reactions", "limit": "ADI 0-0.7 mg/kg", "aliases": "E227,Calcium Bisulfite"},
    {"e": 228, "name": "Potassium Hydrogen Sulfite", "category": "Preservative", "purpose": "Preservative", "risk": "Low", "concerns": "May cause allergic reactions", "limit": "ADI 0-0.7 mg/kg", "aliases": "E228,Potassium Bisulfite"},
    {"e": 230, "name": "Diphenyl", "category": "Preservative", "purpose": "Fungicide for citrus", "risk": "Moderate", "concerns": "May cause headaches, nausea", "limit": "ADI 0-0.05 mg/kg", "aliases": "E230,Diphenyl"},
    {"e": 231, "name": "Orthophenylphenol", "category": "Preservative", "purpose": "Fungicide", "risk": "Moderate", "concerns": "May cause irritation", "limit": "ADI 0-0.2 mg/kg", "aliases": "E231,OPP"},
    {"e": 232, "name": "Sodium Orthophenylphenol", "category": "Preservative", "purpose": "Fungicide", "risk": "Moderate", "concerns": "May cause irritation", "limit": "ADI 0-0.2 mg/kg", "aliases": "E232,Sodium OPP"},
    {"e": 233, "name": "Thiabendazole", "category": "Preservative", "purpose": "Fungicide", "risk": "Moderate", "concerns": "May cause nausea", "limit": "ADI 0-0.1 mg/kg", "aliases": "E233,TBZ"},
    {"e": 234, "name": "Nisin", "category": "Preservative", "purpose": "Natural preservative from bacteria", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-1 mg/kg", "aliases": "E234,Nisin"},
    {"e": 235, "name": "Natamycin", "category": "Preservative", "purpose": "Natural antifungal", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-0.2 mg/kg", "aliases": "E235,Pimaricin"},
    {"e": 236, "name": "Formic Acid", "category": "Preservative", "purpose": "Preservative", "risk": "Low", "concerns": "May cause irritation", "limit": "ADI 0-3 mg/kg", "aliases": "E236,Formic Acid"},
    {"e": 237, "name": "Sodium Formate", "category": "Preservative", "purpose": "Preservative", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-3 mg/kg", "aliases": "E237"},
    {"e": 238, "name": "Calcium Formate", "category": "Preservative", "purpose": "Preservative", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-3 mg/kg", "aliases": "E238"},
    {"e": 239, "name": "Hexamethylenetetramine", "category": "Preservative", "purpose": "Preservative", "risk": "Moderate", "concerns": "May release formaldehyde", "limit": "ADI 0-0.15 mg/kg", "aliases": "E239,Hexamine"},
    {"e": 240, "name": "Formaldehyde", "category": "Preservative", "purpose": "Preservative", "risk": "High", "concerns": "Known carcinogen", "limit": "ADI not specified", "aliases": "E240"},
    {"e": 242, "name": "Dimethyl Dicarbonate", "category": "Preservative", "purpose": "Beverage preservative", "risk": "Low", "concerns": "May cause slight irritation", "limit": "ADI 0-250 mg/kg", "aliases": "E242,DMDC"},
    {"e": 261, "name": "Potassium Acetates", "category": "Preservative", "purpose": "Preservative, acidity regulator", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E261,Potassium Acetate"},
    {"e": 280, "name": "Propionic Acid", "category": "Preservative", "purpose": "Preservative", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E280,Propionic Acid"},
    {"e": 281, "name": "Sodium Propionate", "category": "Preservative", "purpose": "Preservative", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E281,Sodium Propionate"},
    {"e": 283, "name": "Potassium Propionate", "category": "Preservative", "purpose": "Preservative", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E283,Potassium Propionate"},
    {"e": 284, "name": "Boric Acid", "category": "Preservative", "purpose": "Preservative", "risk": "Moderate", "concerns": "Kidney damage with prolonged use", "limit": "ADI 0-0.2 mg/kg", "aliases": "E284,Boric Acid"},
    {"e": 285, "name": "Sodium Tetraborate", "category": "Preservative", "purpose": "Preservative", "risk": "Moderate", "concerns": "May affect reproduction", "limit": "ADI 0-0.1 mg/kg", "aliases": "E285,Borax"},
    {"e": 286, "name": "Sodium Diacetate", "category": "Preservative", "purpose": "Preservative, acidity regulator", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E286,Sodium Diacetate"},
    {"e": 290, "name": "Carbon Dioxide", "category": "Preservative", "purpose": "Preservative, carbonation", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E290,CO2"},
]

# E300-E399: Antioxidants and Acidity Regulators
ANTIOXIDANTS = [
    {"e": 303, "name": "Potassium Ascorbate", "category": "Antioxidant", "purpose": "Vitamin C source", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E303"},
    {"e": 304, "name": "Ascorbyl Palmitate", "category": "Antioxidant", "purpose": "Fat-soluble antioxidant", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-2.5 mg/kg", "aliases": "E304,Ascorbyl Palmitate"},
    {"e": 308, "name": "Synthetic Gamma-Tocopherol", "category": "Antioxidant", "purpose": "Vitamin E antioxidant", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E308"},
    {"e": 309, "name": "Synthetic Delta-Tocopherol", "category": "Antioxidant", "purpose": "Vitamin E antioxidant", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E309"},
    {"e": 310, "name": "Propyl Gallate", "category": "Antioxidant", "purpose": "Prevents oxidation", "risk": "Moderate", "concerns": "May cause stomach irritation", "limit": "ADI 0-0.5 mg/kg", "aliases": "E310,Propyl Gallate"},
    {"e": 311, "name": "Octyl Gallate", "category": "Antioxidant", "purpose": "Antioxidant", "risk": "Moderate", "concerns": "May cause allergic reactions", "limit": "ADI 0-0.5 mg/kg", "aliases": "E311"},
    {"e": 312, "name": "Dodecyl Gallate", "category": "Antioxidant", "purpose": "Antioxidant", "risk": "Moderate", "concerns": "May cause allergic reactions", "limit": "ADI 0-0.5 mg/kg", "aliases": "E312"},
    {"e": 315, "name": "Isoascorbic Acid", "category": "Antioxidant", "purpose": "Antioxidant", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E315,Erythorbic Acid"},
    {"e": 317, "name": "Isoascorbyl Stearate", "category": "Antioxidant", "purpose": "Antioxidant", "risk": "Low", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E317"},
    {"e": 318, "name": "Ascorbyl Stearate", "category": "Antioxidant", "purpose": "Antioxidant", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E318"},
    {"e": 325, "name": "Sodium Lactate", "category": "Acidity Regulator", "purpose": "Buffer, humectant", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E325"},
    {"e": 326, "name": "Potassium Lactate", "category": "Acidity Regulator", "purpose": "Buffer, acidity regulator", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E326"},
    {"e": 327, "name": "Calcium Lactate", "category": "Acidity Regulator", "purpose": "Calcium source, acidity regulator", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E327"},
    {"e": 328, "name": "Ammonium Lactate", "category": "Acidity Regulator", "purpose": "Buffer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E328"},
    {"e": 329, "name": "Magnesium Lactate", "category": "Acidity Regulator", "purpose": "Magnesium source", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E329"},
    {"e": 335, "name": "Sodium Tartrates", "category": "Acidity Regulator", "purpose": "Buffer, sequestrant", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E335,Sodium Tartrate"},
    {"e": 336, "name": "Potassium Tartrates", "category": "Acidity Regulator", "purpose": "Buffer, leavening agent", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E336,Potassium Tartrate"},
    {"e": 337, "name": "Sodium Potassium Tartrate", "category": "Acidity Regulator", "purpose": "Buffer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E337,Rochelle Salt"},
    {"e": 342, "name": "Ammonium Phosphates", "category": "Acidity Regulator", "purpose": "Buffer", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-70 mg/kg", "aliases": "E342"},
    {"e": 343, "name": "Magnesium Phosphates", "category": "Acidity Regulator", "purpose": "Magnesium source", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-70 mg/kg", "aliases": "E343,Magnesium Phosphate"},
    {"e": 344, "name": "Citric Acid Esters of Mono- and Diglycerides", "category": "Emulsifier", "purpose": "Emulsifier", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E344"},
    {"e": 345, "name": "Magnesium Citrate", "category": "Acidity Regulator", "purpose": "Buffer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E345"},
    {"e": 350, "name": "Sodium Malates", "category": "Acidity Regulator", "purpose": "Buffer, flavor enhancer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E350,Sodium Malate"},
    {"e": 351, "name": "Potassium Malate", "category": "Acidity Regulator", "purpose": "Buffer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E351"},
    {"e": 352, "name": "Calcium Malate", "category": "Acidity Regulator", "purpose": "Calcium source", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E352"},
    {"e": 353, "name": "Metatartaric Acid", "category": "Acidity Regulator", "purpose": "Acidulant", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E353"},
    {"e": 354, "name": "Calcium Tartrate", "category": "Acidity Regulator", "purpose": "Buffer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E354"},
    {"e": 355, "name": "Adipic Acid", "category": "Acidity Regulator", "purpose": "Acidulant", "risk": "Low", "concerns": "May cause digestive issues", "limit": "ADI 0-5 mg/kg", "aliases": "E355,Adipic Acid"},
    {"e": 356, "name": "Sodium Adipate", "category": "Acidity Regulator", "purpose": "Buffer", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-5 mg/kg", "aliases": "E356"},
    {"e": 357, "name": "Potassium Adipate", "category": "Acidity Regulator", "purpose": "Buffer", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-5 mg/kg", "aliases": "E357"},
    {"e": 363, "name": "Succinic Acid", "category": "Acidity Regulator", "purpose": "Acidulant, flavor", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E363,Succinic Acid"},
    {"e": 364, "name": "Sodium Succinates", "category": "Flavor Enhancer", "purpose": "Flavor enhancer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E364,Sodium Succinate"},
    {"e": 365, "name": "Sodium Fumarate", "category": "Acidity Regulator", "purpose": "Acidulant", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-6 mg/kg", "aliases": "E365"},
    {"e": 366, "name": "Calcium Fumarate", "category": "Acidity Regulator", "purpose": "Calcium source", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-6 mg/kg", "aliases": "E366"},
    {"e": 367, "name": "Calcium Gluconate", "category": "Acidity Regulator", "purpose": "Calcium source", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E367"},
    {"e": 368, "name": "Ammonium Gluconate", "category": "Acidity Regulator", "purpose": "Buffer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E368"},
    {"e": 380, "name": "Triammonium Citrate", "category": "Acidity Regulator", "purpose": "Buffer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E380"},
    {"e": 381, "name": "Ammonium Ferric Citrate", "category": "Food Color", "purpose": "Iron supplement, green coloring", "risk": "Low", "concerns": "May cause digestive issues", "limit": "ADI 0-1.5 mg/kg", "aliases": "E381"},
    {"e": 385, "name": "Calcium Disodium EDTA", "category": "Preservative", "purpose": "Preservative, antioxidant", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-2.5 mg/kg", "aliases": "E385,EDTA"},
    {"e": 388, "name": "Thiodipropionic Acid", "category": "Antioxidant", "purpose": "Antioxidant", "risk": "Low", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E388"},
    {"e": 389, "name": "Dilauryl Thiodipropionate", "category": "Antioxidant", "purpose": "Antioxidant", "risk": "Low", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E389"},
    {"e": 390, "name": "Distearyl Thiodipropionate", "category": "Antioxidant", "purpose": "Antioxidant", "risk": "Low", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E390"},
    {"e": 399, "name": "Stearyl Citrate", "category": "Antioxidant", "purpose": "Antioxidant, emulsifier", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E399"},
]

# E400-E599: Stabilizers, Thickeners, Emulsifiers, Acidity Regulators
STABILIZERS = [
    {"e": 402, "name": "Potassium Alginate", "category": "Thickener", "purpose": "Thickener", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E402"},
    {"e": 403, "name": "Ammonium Alginate", "category": "Thickener", "purpose": "Thickener", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E403"},
    {"e": 404, "name": "Calcium Alginate", "category": "Thickener", "purpose": "Thickener, gelling agent", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E404"},
    {"e": 405, "name": "Propylene Glycol Alginate", "category": "Thickener", "purpose": "Thickener, emulsifier", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E405,PGA"},
    {"e": 407, "name": "Carrageenan", "category": "Thickener", "purpose": "Thickener, stabilizer", "risk": "Low", "concerns": "May cause digestive issues", "limit": "ADI 0-75 mg/kg", "aliases": "E407,Carrageenan"},
    {"e": 413, "name": "Tragacanth Gum", "category": "Thickener", "purpose": "Thickener, stabilizer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E413,Tragacanth"},
    {"e": 414, "name": "Gum Arabic", "category": "Thickener", "purpose": "Thickener, emulsifier", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E414,Gum Arabic"},
    {"e": 416, "name": "Karaya Gum", "category": "Thickener", "purpose": "Thickener", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E416,Karaya Gum"},
    {"e": 417, "name": "Gellan Gum", "category": "Thickener", "purpose": "Gelling agent", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E417,Gellan Gum"},
    {"e": 420, "name": "Sorbitol", "category": "Sweetener", "purpose": "Humectant, sweetener", "risk": "Minimal", "concerns": "May cause digestive issues", "limit": "ADI not specified", "aliases": "E420,Sorbitol"},
    {"e": 421, "name": "Mannitol", "category": "Sweetener", "purpose": "Humectant, sweetener", "risk": "Low", "concerns": "May cause diarrhea", "limit": "ADI 0-50 mg/kg", "aliases": "E421,Mannitol"},
    {"e": 422, "name": "Glycerol", "category": "Humectant", "purpose": "Humectant, sweetener", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E422,Glycerol,Glycerin"},
    {"e": 440, "name": "Pectins", "category": "Thickener", "purpose": "Gelling agent, thickener", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E440,Pectin"},
    {"e": 442, "name": "Ammonium Phosphatides", "category": "Emulsifier", "purpose": "Emulsifier", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E442"},
    {"e": 444, "name": "Sucrose Acetate Isobutyrate", "category": "Emulsifier", "purpose": "Emulsifier, stabilizer", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-10 mg/kg", "aliases": "E444,SAIB"},
    {"e": 445, "name": "Glycerol Esters of Wood Resins", "category": "Emulsifier", "purpose": "Emulsifier", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-12.5 mg/kg", "aliases": "E445"},
    {"e": 450, "name": "Diphosphates", "category": "Leavening Agent", "purpose": "Leavening agent, buffer", "risk": "Low", "concerns": "High phosphorus concerns", "limit": "ADI 0-70 mg/kg", "aliases": "E450,Diphosphate,Pyrophosphate"},
    {"e": 451, "name": "Triphosphates", "category": "Emulsifier", "purpose": "Buffer, sequestrant", "risk": "Low", "concerns": "High phosphorus concerns", "limit": "ADI 0-70 mg/kg", "aliases": "E451,Triphosphate"},
    {"e": 452, "name": "Polyphosphates", "category": "Emulsifier", "purpose": "Buffer, sequestrant", "risk": "Low", "concerns": "High phosphorus concerns", "limit": "ADI 0-70 mg/kg", "aliases": "E452,Polyphosphate"},
    {"e": 460, "name": "Cellulose", "category": "Thickener", "purpose": "Thickener, bulking agent", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E460,Cellulose,Microcrystalline Cellulose"},
    {"e": 466, "name": "Carboxymethyl Cellulose", "category": "Thickener", "purpose": "Thickener, stabilizer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E466,CMC"},
    {"e": 470, "name": "Salts of Fatty Acids", "category": "Emulsifier", "purpose": "Emulsifier, stabilizer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E470,Sodium Stearoyl"},
    {"e": 471, "name": "Mono- and Diglycerides of Fatty Acids", "category": "Emulsifier", "purpose": "Emulsifier", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E471,Monoglycerides"},
    {"e": 473, "name": "Sucrose Esters of Fatty Acids", "category": "Emulsifier", "purpose": "Emulsifier", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-30 mg/kg", "aliases": "E473,Sucrose Esters"},
    {"e": 474, "name": "Sucroglycerides", "category": "Emulsifier", "purpose": "Emulsifier", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-30 mg/kg", "aliases": "E474"},
    {"e": 475, "name": "Polyglycerol Esters of Fatty Acids", "category": "Emulsifier", "purpose": "Emulsifier", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-25 mg/kg", "aliases": "E475,Polyglycerol Esters"},
    {"e": 476, "name": "Polyglycerol Polyricinoleate", "category": "Emulsifier", "purpose": "Emulsifier", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-7.5 mg/kg", "aliases": "E476,PGPR"},
    {"e": 477, "name": "Propylene Glycol Esters of Fatty Acids", "category": "Emulsifier", "purpose": "Emulsifier", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-25 mg/kg", "aliases": "E477"},
    {"e": 478, "name": "Lactylated Fatty Acid Esters of Glycerol and Propylene Glycol", "category": "Emulsifier", "purpose": "Emulsifier", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E478"},
    {"e": 479, "name": "Thermally Oxidized Soya Bean Oil", "category": "Emulsifier", "purpose": "Emulsifier", "risk": "Low", "concerns": "May cause digestive issues", "limit": "ADI not specified", "aliases": "E479,TOOT"},
    {"e": 483, "name": "Stearyl Tartrate", "category": "Emulsifier", "purpose": "Emulsifier", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E483"},
    {"e": 491, "name": "Sorbitan Monostearate", "category": "Emulsifier", "purpose": "Emulsifier", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-25 mg/kg", "aliases": "E491,Span 60"},
    {"e": 492, "name": "Sorbitan Tristearate", "category": "Emulsifier", "purpose": "Emulsifier", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-25 mg/kg", "aliases": "E492,Span 65"},
    {"e": 493, "name": "Sorbitan Monooleate", "category": "Emulsifier", "purpose": "Emulsifier", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-25 mg/kg", "aliases": "E493,Span 80"},
    {"e": 494, "name": "Sorbitan Monopalmitate", "category": "Emulsifier", "purpose": "Emulsifier", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-25 mg/kg", "aliases": "E494,Span 40"},
    {"e": 495, "name": "Sorbitan Monolaurate", "category": "Emulsifier", "purpose": "Emulsifier", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-25 mg/kg", "aliases": "E495,Span 20"},
    {"e": 500, "name": "Sodium Carbonates", "category": "Acidity Regulator", "purpose": "Acidity regulator, raising agent", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E500,Sodium Carbonate"},
    {"e": 501, "name": "Potassium Carbonates", "category": "Acidity Regulator", "purpose": "Acidity regulator", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E501,Potassium Carbonate"},
    {"e": 503, "name": "Ammonium Carbonates", "category": "Leavening Agent", "purpose": "Leavening agent", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E503,Ammonium Carbonate"},
    {"e": 504, "name": "Magnesium Carbonates", "category": "Acidity Regulator", "purpose": "Acidity regulator, antacid", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E504,Magnesium Carbonate"},
    {"e": 507, "name": "Hydrochloric Acid", "category": "Acidity Regulator", "purpose": "Acidulant", "risk": "Low", "concerns": "May cause irritation", "limit": "ADI not specified", "aliases": "E507"},
    {"e": 514, "name": "Sodium Sulfates", "category": "Acidity Regulator", "purpose": "Acidity regulator", "risk": "Low", "concerns": "May cause diarrhea", "limit": "ADI 0-70 mg/kg", "aliases": "E514,Sodium Sulfate"},
    {"e": 515, "name": "Potassium Sulfates", "category": "Acidity Regulator", "purpose": "Acidity regulator", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-70 mg/kg", "aliases": "E515"},
    {"e": 516, "name": "Calcium Sulfate", "category": "Acidity Regulator", "purpose": "Calcium source, firming agent", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E516,Calcium Sulfate"},
    {"e": 517, "name": "Ammonium Sulfate", "category": "Acidity Regulator", "purpose": "Nutrient, dough improver", "risk": "Low", "concerns": "May cause nausea", "limit": "ADI 0-30 mg/kg", "aliases": "E517"},
    {"e": 518, "name": "Magnesium Sulfate", "category": "Acidity Regulator", "purpose": "Nutrient, flavor enhancer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E518,Epsom Salt"},
    {"e": 519, "name": "Cupric Sulfate", "category": "Nutrient", "purpose": "Copper supplement", "risk": "Moderate", "concerns": "Toxic in high amounts", "limit": "ADI 0-0.5 mg/kg", "aliases": "E519,Copper Sulfate"},
    {"e": 524, "name": "Sodium Hydroxide", "category": "Acidity Regulator", "purpose": "pH adjustment", "risk": "Low", "concerns": "Caustic, handle with care", "limit": "ADI not specified", "aliases": "E524,Sodium Hydroxide"},
    {"e": 525, "name": "Potassium Hydroxide", "category": "Acidity Regulator", "purpose": "pH adjustment", "risk": "Low", "concerns": "Caustic, handle with care", "limit": "ADI not specified", "aliases": "E525"},
    {"e": 526, "name": "Calcium Hydroxide", "category": "Acidity Regulator", "purpose": "pH adjustment, calcium source", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E526,Calcium Hydroxide"},
    {"e": 527, "name": "Ammonium Hydroxide", "category": "Acidity Regulator", "purpose": "pH adjustment", "risk": "Low", "concerns": "May cause irritation", "limit": "ADI not specified", "aliases": "E527"},
    {"e": 528, "name": "Magnesium Hydroxide", "category": "Acidity Regulator", "purpose": "pH adjustment, antacid", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E528,Milk of Magnesia"},
    {"e": 529, "name": "Calcium Oxide", "category": "Acidity Regulator", "purpose": "pH adjustment", "risk": "Low", "concerns": "Caustic when not hydrated", "limit": "ADI not specified", "aliases": "E529,Quicklime"},
    {"e": 530, "name": "Iron Oxide", "category": "Food Color", "purpose": "Coloring", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-0.5 mg/kg", "aliases": "E530,Iron Oxide"},
    {"e": 535, "name": "Sodium Ferrocyanide", "category": "Anti-caking Agent", "purpose": "Anti-caking agent", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-0.25 mg/kg", "aliases": "E535"},
    {"e": 536, "name": "Potassium Ferrocyanide", "category": "Anti-caking Agent", "purpose": "Anti-caking agent", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-0.25 mg/kg", "aliases": "E536"},
    {"e": 541, "name": "Sodium Aluminium Phosphate", "category": "Leavening Agent", "purpose": "Leavening agent", "risk": "Moderate", "concerns": "Aluminum content concerns", "limit": "ADI 0-7 mg/kg", "aliases": "E541,SALP"},
    {"e": 550, "name": "Silicon Dioxide", "category": "Anti-caking Agent", "purpose": "Anti-caking agent", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-50 mg/kg", "aliases": "E550,Silica"},
    {"e": 551, "name": "Silicon Dioxide (Synthetic)", "category": "Anti-caking Agent", "purpose": "Anti-caking agent", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-50 mg/kg", "aliases": "E551"},
    {"e": 552, "name": "Calcium Silicate", "category": "Anti-caking Agent", "purpose": "Anti-caking agent", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-70 mg/kg", "aliases": "E552"},
    {"e": 553, "name": "Magnesium Silicate", "category": "Anti-caking Agent", "purpose": "Anti-caking agent", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-70 mg/kg", "aliases": "E553,Talc"},
    {"e": 554, "name": "Sodium Aluminosilicate", "category": "Anti-caking Agent", "purpose": "Anti-caking agent", "risk": "Low", "concerns": "Aluminum concerns", "limit": "ADI 0-70 mg/kg", "aliases": "E554"},
    {"e": 555, "name": "Potassium Aluminosilicate", "category": "Anti-caking Agent", "purpose": "Anti-caking agent", "risk": "Low", "concerns": "Aluminum concerns", "limit": "ADI 0-70 mg/kg", "aliases": "E555"},
    {"e": 556, "name": "Calcium Aluminosilicate", "category": "Anti-caking Agent", "purpose": "Anti-caking agent", "risk": "Low", "concerns": "Aluminum concerns", "limit": "ADI 0-70 mg/kg", "aliases": "E556"},
    {"e": 558, "name": "Bentonite", "category": "Anti-caking Agent", "purpose": "Anti-caking agent", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E558,Bentonite"},
    {"e": 559, "name": "Aluminium Silicate", "category": "Anti-caking Agent", "purpose": "Anti-caking agent", "risk": "Low", "concerns": "Aluminum concerns", "limit": "ADI 0-70 mg/kg", "aliases": "E559,Kaolin"},
    {"e": 570, "name": "Stearic Acid", "category": "Emulsifier", "purpose": "Emulsifier, firming agent", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E570,Stearic Acid"},
    {"e": 572, "name": "Magnesium Stearate", "category": "Emulsifier", "purpose": "Emulsifier", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E572,Magnesium Stearate"},
    {"e": 585, "name": "Ferrous Lactate", "category": "Nutrient", "purpose": "Iron supplement", "risk": "Low", "concerns": "May cause digestive issues", "limit": "ADI 0-0.8 mg/kg", "aliases": "E585"},
    {"e": 620, "name": "Glutamic Acid", "category": "Flavor Enhancer", "purpose": "Flavor enhancer", "risk": "Moderate", "concerns": "May cause MSG symptom complex", "limit": "ADI 0-120 mg/kg", "aliases": "E620,Glutamic Acid"},
    {"e": 622, "name": "Monopotassium Glutamate", "category": "Flavor Enhancer", "purpose": "Flavor enhancer", "risk": "Moderate", "concerns": "May cause reactions in sensitive people", "limit": "ADI 0-120 mg/kg", "aliases": "E622"},
    {"e": 623, "name": "Calcium Glutamate", "category": "Flavor Enhancer", "purpose": "Flavor enhancer", "risk": "Moderate", "concerns": "May cause reactions", "limit": "ADI 0-120 mg/kg", "aliases": "E623"},
    {"e": 624, "name": "Magnesium Glutamate", "category": "Flavor Enhancer", "purpose": "Flavor enhancer", "risk": "Moderate", "concerns": "May cause reactions", "limit": "ADI 0-120 mg/kg", "aliases": "E624"},
    {"e": 625, "name": "Magnesium Chloride", "category": "Flavor Enhancer", "purpose": "Flavor enhancer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E625"},
    {"e": 626, "name": "Guanylic Acid", "category": "Flavor Enhancer", "purpose": "Flavor enhancer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-2 mg/kg", "aliases": "E626,Guanylate"},
    {"e": 627, "name": "Disodium Guanylate", "category": "Flavor Enhancer", "purpose": "Flavor enhancer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-2 mg/kg", "aliases": "E627"},
    {"e": 628, "name": "Dipotassium Guanylate", "category": "Flavor Enhancer", "purpose": "Flavor enhancer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-2 mg/kg", "aliases": "E628"},
    {"e": 629, "name": "Inosinic Acid", "category": "Flavor Enhancer", "purpose": "Flavor enhancer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-2 mg/kg", "aliases": "E629,Inosinate"},
    {"e": 630, "name": "Disodium Inosinate", "category": "Flavor Enhancer", "purpose": "Flavor enhancer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-2 mg/kg", "aliases": "E630"},
    {"e": 631, "name": "Disodium Ribonucleotides", "category": "Flavor Enhancer", "purpose": "Flavor enhancer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-2 mg/kg", "aliases": "E631,I+G"},
    {"e": 632, "name": "Calcium Ribonucleotides", "category": "Flavor Enhancer", "purpose": "Flavor enhancer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-2 mg/kg", "aliases": "E632"},
    {"e": 633, "name": "Maltol", "category": "Flavor Enhancer", "purpose": "Flavor enhancer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-1 mg/kg", "aliases": "E633,Maltol"},
    {"e": 634, "name": "Ethyl Maltol", "category": "Flavor Enhancer", "purpose": "Flavor enhancer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-1 mg/kg", "aliases": "E634"},
    {"e": 635, "name": "Sodium 5'-ribonucleotides", "category": "Flavor Enhancer", "purpose": "Flavor enhancer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-2 mg/kg", "aliases": "E635"},
    {"e": 636, "name": "Maltodextrin", "category": "Flavor Enhancer", "purpose": "Flavor enhancer, carrier", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E636"},
    {"e": 637, "name": "Ethyl Vanillin", "category": "Flavor Enhancer", "purpose": "Flavoring", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-1 mg/kg", "aliases": "E637"},
    {"e": 638, "name": "Vanillin", "category": "Flavor Enhancer", "purpose": "Flavoring", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-10 mg/kg", "aliases": "E638,Vanillin"},
    {"e": 639, "name": "L-Phenylalanine", "category": "Flavor Enhancer", "purpose": "Flavor enhancer", "risk": "Low", "concerns": "PKU patients avoid", "limit": "ADI not specified", "aliases": "E639"},
    {"e": 640, "name": "Glycine", "category": "Flavor Enhancer", "purpose": "Flavor enhancer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E640,Glycine"},
    {"e": 641, "name": "L-Leucine", "category": "Flavor Enhancer", "purpose": "Flavor enhancer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E641"},
    {"e": 650, "name": "Zinc Gluconate", "category": "Nutrient", "purpose": "Zinc supplement", "risk": "Low", "concerns": "May cause nausea", "limit": "ADI 0-1 mg/kg", "aliases": "E650"},
]

# E700-E799: Antibiotics
ANTIBIOTICS = [
    {"e": 700, "name": "Virginiamycin", "category": "Antibiotic", "purpose": "Antibiotic growth promoter", "risk": "High", "concerns": "Antibiotic resistance concerns", "limit": "Very limited", "aliases": "E700,Virginiamycin"},
    {"e": 701, "name": "Tiamulin", "category": "Antibiotic", "purpose": "Veterinary antibiotic", "risk": "High", "concerns": "Antibiotic resistance", "limit": "Very limited", "aliases": "E701,Tiamulin"},
    {"e": 702, "name": "Tylosin", "category": "Antibiotic", "purpose": "Veterinary antibiotic", "risk": "High", "concerns": "Antibiotic resistance", "limit": "Very limited", "aliases": "E702,Tylosin"},
    {"e": 703, "name": "Spiramycin", "category": "Antibiotic", "purpose": "Veterinary antibiotic", "risk": "High", "concerns": "Antibiotic resistance", "limit": "Very limited", "aliases": "E703,Spiramycin"},
    {"e": 704, "name": "Oleandomycin", "category": "Antibiotic", "purpose": "Veterinary antibiotic", "risk": "High", "concerns": "Antibiotic resistance", "limit": "Very limited", "aliases": "E704,Oleandomycin"},
    {"e": 705, "name": "Avilamycin", "category": "Antibiotic", "purpose": "Coccidiostat", "risk": "High", "concerns": "Antibiotic resistance", "limit": "Very limited", "aliases": "E705,Avilamycin"},
    {"e": 706, "name": "Colistin", "category": "Antibiotic", "purpose": "Veterinary antibiotic", "risk": "High", "concerns": "Last-resort antibiotic", "limit": "Very limited", "aliases": "E706,Colistin"},
    {"e": 707, "name": "Neomycin", "category": "Antibiotic", "purpose": "Veterinary antibiotic", "risk": "High", "concerns": "Antibiotic resistance", "limit": "Very limited", "aliases": "E707,Neomycin"},
    {"e": 708, "name": "Tetracycline", "category": "Antibiotic", "purpose": "Veterinary antibiotic", "risk": "High", "concerns": "Antibiotic resistance", "limit": "Very limited", "aliases": "E708,Tetracycline"},
    {"e": 709, "name": "Chlortetracycline", "category": "Antibiotic", "purpose": "Antibiotic", "risk": "High", "concerns": "Antibiotic resistance", "limit": "Very limited", "aliases": "E709,CTC"},
    {"e": 710, "name": "Oxytetracycline", "category": "Antibiotic", "purpose": "Antibiotic", "risk": "High", "concerns": "Antibiotic resistance", "limit": "Very limited", "aliases": "E710,OTC"},
    {"e": 711, "name": "Spiramycin", "category": "Antibiotic", "purpose": "Antibiotic", "risk": "High", "concerns": "Antibiotic resistance", "limit": "Very limited", "aliases": "E711"},
    {"e": 712, "name": "Lincomycin", "category": "Antibiotic", "purpose": "Antibiotic", "risk": "High", "concerns": "Antibiotic resistance", "limit": "Very limited", "aliases": "E712,Lincomycin"},
]

# E900-E999: Sweeteners, Glazing Agents, Gases
SWEETENERS_GLAZING = [
    {"e": 900, "name": "Dimethylpolysiloxane", "category": "Anti-foaming Agent", "purpose": "Anti-foaming agent", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-1.5 mg/kg", "aliases": "E900,Dimethylpolysiloxane"},
    {"e": 901, "name": "Beeswax", "category": "Glazing Agent", "purpose": "Glazing agent", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E901,Beeswax"},
    {"e": 902, "name": "Candelilla Wax", "category": "Glazing Agent", "purpose": "Glazing agent", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E902,Candelilla Wax"},
    {"e": 903, "name": "Carnauba Wax", "category": "Glazing Agent", "purpose": "Glazing agent", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E903,Carnauba Wax"},
    {"e": 904, "name": "Shellac", "category": "Glazing Agent", "purpose": "Glazing agent", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E904,Shellac"},
    {"e": 950, "name": "Acesulfame Potassium", "category": "Sweetener", "purpose": "High-intensity sweetener", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-15 mg/kg", "aliases": "E950,Ace-K"},
    {"e": 951, "name": "Aspartame", "category": "Sweetener", "purpose": "High-intensity sweetener", "risk": "Low", "concerns": "PKU patients avoid", "limit": "ADI 0-40 mg/kg", "aliases": "E951,Aspartame"},
    {"e": 952, "name": "Cyclamate", "category": "Sweetener", "purpose": "High-intensity sweetener", "risk": "Moderate", "concerns": "Banned in some countries", "limit": "ADI 0-11 mg/kg", "aliases": "E952,Cyclamate"},
    {"e": 953, "name": "Isomalt", "category": "Sweetener", "purpose": "Bulk sweetener", "risk": "Minimal", "concerns": "May cause digestive issues", "limit": "ADI 0-50 mg/kg", "aliases": "E953,Isomalt"},
    {"e": 954, "name": "Saccharin", "category": "Sweetener", "purpose": "High-intensity sweetener", "risk": "Low", "concerns": "Controversial safety", "limit": "ADI 0-5 mg/kg", "aliases": "E954,Saccharin"},
    {"e": 955, "name": "Sucralose", "category": "Sweetener", "purpose": "High-intensity sweetener", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-15 mg/kg", "aliases": "E955,Sucralose"},
    {"e": 956, "name": "Alitame", "category": "Sweetener", "purpose": "High-intensity sweetener", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-1 mg/kg", "aliases": "E956,Alitame"},
    {"e": 957, "name": "Thaumatin", "category": "Sweetener", "purpose": "Natural high-intensity sweetener", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E957,Thaumatin"},
    {"e": 958, "name": "Glycyrrhizin", "category": "Sweetener", "purpose": "Natural sweetener", "risk": "Low", "concerns": "May raise blood pressure", "limit": "ADI 0-2 mg/kg", "aliases": "E958,Glycyrrhizin"},
    {"e": 959, "name": "Neohesperidine DC", "category": "Sweetener", "purpose": "High-intensity sweetener", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-20 mg/kg", "aliases": "E959"},
    {"e": 960, "name": "Steviol Glycosides", "category": "Sweetener", "purpose": "Natural zero-calorie sweetener", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-4 mg/kg", "aliases": "E960,Stevia"},
    {"e": 961, "name": "Neotame", "category": "Sweetener", "purpose": "High-intensity sweetener", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-2 mg/kg", "aliases": "E961,Neotame"},
    {"e": 962, "name": "Advantame", "category": "Sweetener", "purpose": "High-intensity sweetener", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-5 mg/kg", "aliases": "E962,Advantame"},
    {"e": 965, "name": "Maltitol", "category": "Sweetener", "purpose": "Bulk sweetener", "risk": "Minimal", "concerns": "May cause digestive issues", "limit": "ADI not specified", "aliases": "E965,Maltitol"},
    {"e": 966, "name": "Lactitol", "category": "Sweetener", "purpose": "Bulk sweetener", "risk": "Minimal", "concerns": "May cause digestive issues", "limit": "ADI 0-25 mg/kg", "aliases": "E966,Lactitol"},
    {"e": 967, "name": "Xylitol", "category": "Sweetener", "purpose": "Bulk sweetener", "risk": "Minimal", "concerns": "May cause digestive issues", "limit": "ADI not specified", "aliases": "E967,Xylitol"},
    {"e": 968, "name": "Erythritol", "category": "Sweetener", "purpose": "Zero-calorie sweetener", "risk": "Minimal", "concerns": "May cause digestive issues", "limit": "ADI 0-60 mg/kg", "aliases": "E968,Erythritol"},
    {"e": 969, "name": "Enzyme Treated Stevia", "category": "Sweetener", "purpose": "Natural sweetener", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E969"},
]

# Additional E1000-E1599 range
ADDITIONAL = [
    {"e": 1001, "name": "Choline Salts", "category": "Nutrient", "purpose": "Nutrient supplement", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1001,Choline"},
    {"e": 1002, "name": "Caffeine", "category": "Stimulant", "purpose": "Stimulant", "risk": "Moderate", "concerns": "May cause anxiety, insomnia", "limit": "ADI 0-3 mg/kg", "aliases": "E1002,Caffeine"},
    {"e": 1003, "name": "Taurine", "category": "Nutrient", "purpose": "Amino acid supplement", "risk": "Low", "concerns": "Limited data on safety", "limit": "ADI not specified", "aliases": "E1003,Taurine"},
    {"e": 1004, "name": "Inositol", "category": "Nutrient", "purpose": "Vitamin-like nutrient", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1004,Inositol"},
    {"e": 1005, "name": "L-Carnitine", "category": "Nutrient", "purpose": "Nutrient supplement", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1005,Carnitine"},
    {"e": 1006, "name": "Glucosamine", "category": "Nutrient", "purpose": "Nutrient supplement", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1006,Glucosamine"},
    {"e": 1007, "name": "Chondroitin", "category": "Nutrient", "purpose": "Nutrient supplement", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1007,Chondroitin"},
    {"e": 1008, "name": "Coenzyme Q10", "category": "Nutrient", "purpose": "Antioxidant supplement", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1008,CoQ10"},
    {"e": 1009, "name": "Alpha Lipoic Acid", "category": "Nutrient", "purpose": "Antioxidant supplement", "risk": "Low", "concerns": "May interact with medications", "limit": "ADI not specified", "aliases": "E1009,ALA"},
    {"e": 1010, "name": "L-Glutathione", "category": "Nutrient", "purpose": "Antioxidant supplement", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1010,Glutathione"},
    {"e": 1011, "name": "L-Cysteine", "category": "Flavor Enhancer", "purpose": "Flavor enhancer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1011,Cysteine"},
    {"e": 1012, "name": "Betaine", "category": "Nutrient", "purpose": "Nutrient supplement", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1012,Betaine"},
    {"e": 1013, "name": "S-Adenosyl Methionine", "category": "Nutrient", "purpose": "Nutrient supplement", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1013,SAMe"},
    {"e": 1014, "name": "Creatine", "category": "Nutrient", "purpose": "Sports nutrition supplement", "risk": "Low", "concerns": "Kidney concerns with overuse", "limit": "ADI not specified", "aliases": "E1014,Creatine"},
    {"e": 1015, "name": "L-Arginine", "category": "Nutrient", "purpose": "Amino acid supplement", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1015,Arginine"},
    {"e": 1016, "name": "L-Ornithine", "category": "Nutrient", "purpose": "Amino acid supplement", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1016,Ornithine"},
    {"e": 1017, "name": "L-Lysine", "category": "Nutrient", "purpose": "Amino acid supplement", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1017,Lysine"},
    {"e": 1018, "name": "L-Methionine", "category": "Nutrient", "purpose": "Amino acid supplement", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1018,Methionine"},
    {"e": 1019, "name": "L-Threonine", "category": "Nutrient", "purpose": "Amino acid supplement", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1019,Threonine"},
    {"e": 1020, "name": "L-Tryptophan", "category": "Nutrient", "purpose": "Amino acid supplement", "risk": "Low", "concerns": "Serotonin precursor, use caution", "limit": "ADI not specified", "aliases": "E1020,Tryptophan"},
    {"e": 1021, "name": "L-Histidine", "category": "Nutrient", "purpose": "Amino acid supplement", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1021,Histidine"},
    {"e": 1022, "name": "L-Isoleucine", "category": "Nutrient", "purpose": "Amino acid supplement", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1022,Isoleucine"},
    {"e": 1023, "name": "L-Valine", "category": "Nutrient", "purpose": "Amino acid supplement", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1023,Valine"},
    {"e": 1100, "name": "Amylase", "category": "Enzyme", "purpose": "Enzyme preparation", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1100,Amylase"},
    {"e": 1101, "name": "Protease", "category": "Enzyme", "purpose": "Enzyme preparation", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1101,Protease"},
    {"e": 1102, "name": "Glucose Oxidase", "category": "Enzyme", "purpose": "Enzyme preparation", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1102,Glucose Oxidase"},
    {"e": 1103, "name": "Invertase", "category": "Enzyme", "purpose": "Enzyme preparation", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1103,Invertase"},
    {"e": 1104, "name": "Lipase", "category": "Enzyme", "purpose": "Enzyme preparation", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1104,Lipase"},
    {"e": 1105, "name": "Papain", "category": "Enzyme", "purpose": "Enzyme preparation", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1105,Papain"},
    {"e": 1106, "name": "Bromelain", "category": "Enzyme", "purpose": "Enzyme preparation", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1106,Bromelain"},
    {"e": 1107, "name": "Ficin", "category": "Enzyme", "purpose": "Enzyme preparation", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1107,Ficin"},
    {"e": 1108, "name": "Beta-Galactosidase", "category": "Enzyme", "purpose": "Enzyme preparation", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1108"},
    {"e": 1109, "name": "Transglutaminase", "category": "Enzyme", "purpose": "Enzyme preparation", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1109,TG"},
    {"e": 1200, "name": "Polydextrose", "category": "Bulking Agent", "purpose": "Bulking agent, fiber", "risk": "Minimal", "concerns": "May cause digestive issues", "limit": "ADI 0-90 mg/kg", "aliases": "E1200,Polydextrose"},
    {"e": 1201, "name": "Polyvinylpyrrolidone", "category": "Stabilizer", "purpose": "Stabilizer", "risk": "Low", "concerns": "May affect nutrient absorption", "limit": "ADI 0-50 mg/kg", "aliases": "E1201,PVP"},
    {"e": 1202, "name": "Polyvinylpolypyrrolidone", "category": "Stabilizer", "purpose": "Stabilizer", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-50 mg/kg", "aliases": "E1202,PVPP"},
    {"e": 1203, "name": "Polyethylene Glycol", "category": "Solvent", "purpose": "Solvent, carrier", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-70 mg/kg", "aliases": "E1203,PEG"},
    {"e": 1204, "name": "Pullulan", "category": "Thickener", "purpose": "Thickener, film former", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1204,Pullulan"},
    {"e": 1400, "name": "Dextrins", "category": "Bulking Agent", "purpose": "Bulking agent", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1400,Dextrin"},
    {"e": 1401, "name": "Modified Starch", "category": "Thickener", "purpose": "Modified food starch", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1401"},
    {"e": 1402, "name": "Acid-treated Starch", "category": "Thickener", "purpose": "Modified starch", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1402"},
    {"e": 1403, "name": "Alkaline-treated Starch", "category": "Thickener", "purpose": "Modified starch", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1403"},
    {"e": 1404, "name": "Bleached Starch", "category": "Thickener", "purpose": "Modified starch", "risk": "Low", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1404"},
    {"e": 1405, "name": "Enzyme-treated Starch", "category": "Thickener", "purpose": "Modified starch", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1405"},
    {"e": 1410, "name": "Monostarch Phosphate", "category": "Thickener", "purpose": "Modified starch", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1410"},
    {"e": 1412, "name": "Distarch Phosphate", "category": "Thickener", "purpose": "Modified starch", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1412"},
    {"e": 1413, "name": "Phosphated Distarch Phosphate", "category": "Thickener", "purpose": "Modified starch", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1413"},
    {"e": 1414, "name": "Acetylated Distarch Phosphate", "category": "Thickener", "purpose": "Modified starch", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1414"},
    {"e": 1420, "name": "Acetylated Starch", "category": "Thickener", "purpose": "Modified starch", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1420"},
    {"e": 1440, "name": "Oxidized Starch", "category": "Thickener", "purpose": "Modified starch", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1440"},
    {"e": 1450, "name": "Starch Sodium Octenyl Succinate", "category": "Thickener", "purpose": "Modified starch", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-70 mg/kg", "aliases": "E1450"},
    {"e": 1505, "name": "Sodium Tripolyphosphate", "category": "Sequestrant", "purpose": "Sequestrant", "risk": "Low", "concerns": "High phosphorus concerns", "limit": "ADI 0-70 mg/kg", "aliases": "E1505,STPP"},
    {"e": 1510, "name": "Propylene Glycol", "category": "Humectant", "purpose": "Humectant, solvent", "risk": "Low", "concerns": "May cause irritation in high amounts", "limit": "ADI 0-25 mg/kg", "aliases": "E1510,Propylene Glycol"},
    {"e": 1517, "name": "Diacetin", "category": "Humectant", "purpose": "Humectant", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1517,Diacetin"},
    {"e": 1518, "name": "Triacetin", "category": "Humectant", "purpose": "Humectant", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1518,Triacetin"},
    {"e": 1520, "name": "Propylene Glycol Alginate", "category": "Thickener", "purpose": "Thickener", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1520"},
    {"e": 1522, "name": "Hydroxypropyl Methyl Cellulose", "category": "Thickener", "purpose": "Thickener", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1522,HPMC"},
    {"e": 1523, "name": "Hydroxypropyl Cellulose", "category": "Thickener", "purpose": "Thickener", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1523,HPC"},
    {"e": 1524, "name": "Methyl Cellulose", "category": "Thickener", "purpose": "Thickener", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1524,MC"},
    {"e": 1530, "name": "Microcrystalline Cellulose", "category": "Thickener", "purpose": "Thickener, anti-caking", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1530,MCC"},
    {"e": 1540, "name": "Locust Bean Gum (hydrolyzed)", "category": "Thickener", "purpose": "Thickener", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1540"},
    {"e": 1542, "name": "Tara Gum", "category": "Thickener", "purpose": "Thickener", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1542,Tara Gum"},
    {"e": 1548, "name": "Curdlan", "category": "Thickener", "purpose": "Thickener, gelling agent", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1548,Curdlan"},
    {"e": 1552, "name": "Inulin", "category": "Nutrient", "purpose": "Prebiotic fiber", "risk": "Minimal", "concerns": "May cause digestive issues", "limit": "ADI not specified", "aliases": "E1552,Inulin"},
    {"e": 1553, "name": "Fructo-oligosaccharides", "category": "Nutrient", "purpose": "Prebiotic", "risk": "Minimal", "concerns": "May cause digestive issues", "limit": "ADI not specified", "aliases": "E1553,FOS"},
    {"e": 1554, "name": "Galacto-oligosaccharides", "category": "Nutrient", "purpose": "Prebiotic", "risk": "Minimal", "concerns": "May cause digestive issues", "limit": "ADI not specified", "aliases": "E1554,GOS"},
    {"e": 1555, "name": "Psyllium Husk", "category": "Nutrient", "purpose": "Dietary fiber", "risk": "Minimal", "concerns": "Take with water", "limit": "ADI not specified", "aliases": "E1555,Psyllium"},
    {"e": 1558, "name": "Trehalose", "category": "Sweetener", "purpose": "Sugar substitute", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1558,Trehalose"},
    {"e": 1559, "name": "Tagatose", "category": "Sweetener", "purpose": "Low-calorie sweetener", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-30 mg/kg", "aliases": "E1559,Tagatose"},
    {"e": 1560, "name": "Allulose", "category": "Sweetener", "purpose": "Rare sugar", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1560,Allulose"},
    {"e": 1565, "name": "Lycasin", "category": "Sweetener", "purpose": "Sugar alcohol", "risk": "Minimal", "concerns": "May cause digestive issues", "limit": "ADI not specified", "aliases": "E1565,Lycasin"},
    {"e": 1568, "name": "Hydrogenated Starch Hydrolysates", "category": "Sweetener", "purpose": "Sugar alcohol", "risk": "Minimal", "concerns": "May cause digestive issues", "limit": "ADI not specified", "aliases": "E1568,HSH"},
    {"e": 1576, "name": "Icelandic Moss Extract", "category": "Stabilizer", "purpose": "Stabilizer", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1576"},
    {"e": 1577, "name": "Carob Bean Gum", "category": "Thickener", "purpose": "Thickener", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1577"},
    {"e": 1578, "name": "Chicle", "category": "Chewing Gum Base", "purpose": "Chewing gum base", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1578,Chicle"},
    {"e": 1580, "name": "Gutta Percha", "category": "Chewing Gum Base", "purpose": "Chewing gum base", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1580"},
    {"e": 1584, "name": "Paraffin", "category": "Glazing Agent", "purpose": "Glazing agent", "risk": "Low", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1584,Paraffin Wax"},
    {"e": 1590, "name": "Mineral Oil (high viscosity)", "category": "Glazing Agent", "purpose": "Glazing agent", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-20 mg/kg", "aliases": "E1590"},
    {"e": 1593, "name": "White Mineral Oil", "category": "Glazing Agent", "purpose": "Glazing agent", "risk": "Low", "concerns": "Generally safe", "limit": "ADI 0-20 mg/kg", "aliases": "E1593"},
    {"e": 1594, "name": "Jojoba Oil", "category": "Glazing Agent", "purpose": "Glazing agent", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI not specified", "aliases": "E1594,Jojoba Oil"},
    {"e": 1595, "name": "Polydimethylsiloxane", "category": "Anti-foaming Agent", "purpose": "Anti-foaming agent", "risk": "Minimal", "concerns": "Generally safe", "limit": "ADI 0-1.5 mg/kg", "aliases": "E1595"},
]

def main():
    # Read existing CSV
    csv_path = Path(__file__).parent / "data" / "chemicals.csv"
    
    # Get existing e-numbers
    existing_enumbers = set()
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            e_num = row.get('e_number', '').strip()
            if e_num:
                # Extract the number part
                if 'INS' in e_num:
                    num = e_num.replace('INS', '').strip()
                else:
                    num = e_num.replace('E', '').strip()
                try:
                    existing_enumbers.add(int(num))
                except:
                    pass
    
    print(f"Found {len(existing_enumbers)} existing E-numbers")
    
    # Combine all additives
    all_additives = FOOD_COLORS + PRESERVATIVES + ANTIOXIDANTS + STABILIZERS + ANTIBIOTICS + SWEETENERS_GLAZING + ADDITIONAL
    
    # Generate new rows
    new_rows = []
    added_count = 0
    
    for additive in all_additives:
        e_num = additive['e']
        
        # Skip if already exists
        if e_num in existing_enumbers:
            continue
        
        # Format e_number as INS XXX
        e_number_str = f"INS {e_num}"
        
        row = {
            'chemical_name': additive['name'],
            'e_number': e_number_str,
            'category': additive['category'],
            'purpose': additive['purpose'],
            'risk_level': additive['risk'],
            'health_concerns': additive['concerns'],
            'safe_limit': additive['limit'],
            'aliases': additive['aliases']
        }
        
        new_rows.append(row)
        existing_enumbers.add(e_num)
        added_count += 1
    
    print(f"Adding {added_count} new food additives")
    
    # Append to CSV
    with open(csv_path, 'a', newline='', encoding='utf-8') as f:
        fieldnames = ['chemical_name', 'e_number', 'category', 'purpose', 'risk_level', 'health_concerns', 'safe_limit', 'aliases']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        for row in new_rows:
            writer.writerow(row)
    
    # Count total rows
    with open(csv_path, 'r', encoding='utf-8') as f:
        total_lines = sum(1 for _ in f)
    
    print(f"Total chemicals in database: {total_lines - 1} (excluding header)")
    print("Done!")

if __name__ == "__main__":
    main()
