import numpy as np

def cosine_similarity(u,l):
    return float(np.dot(u,l)/(np.linalg.norm(u)*np.linalg.norm(l)))
