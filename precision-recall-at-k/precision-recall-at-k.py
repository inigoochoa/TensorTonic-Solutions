import numpy as np

def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    # Write code here
    counts = 0
    n_relevant = len(relevant)
    k_rec = recommended[:k]
    for i in range(k):
        if k_rec[i] in relevant:
            counts += 1
        
    precision = counts / k
    recall = counts / n_relevant
    return [precision, recall]