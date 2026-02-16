import numpy as np
from config.settings import CATEGORIES

def encode_interests(user_input):
    vector = [user_input.get(cat,0) for cat in CATEGORIES]
    vector = np.array(vector,dtype=float)
    if np.max(vector)>0:
        vector = vector/np.max(vector)
    return vector
