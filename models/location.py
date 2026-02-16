import json
import numpy as np
from config.settings import CATEGORIES

def load_locations(path):
    with open(path) as f:
        data = json.load(f)
    processed=[]
    for loc in data:
        vec=[loc["features"].get(cat,0) for cat in CATEGORIES]
        vec=np.array(vec,dtype=float)
        if np.max(vec)>0:
            vec=vec/np.max(vec)
        loc["feature_vector"]=vec
        processed.append(loc)
    return processed
