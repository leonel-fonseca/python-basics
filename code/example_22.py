"""
Read from a pickle file and save to a json file.
"""

import pickle
import json

with open('outputs/series.pkl', 'rb') as f:
    records = pickle.load(f)

with open('outputs/series.json', 'w') as f:
    json.dump(records, f, indent=4)
