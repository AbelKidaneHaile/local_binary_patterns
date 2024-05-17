import numpy as np


# Chi-square distance
def chi_square_distance(hist_P, hist_Q):
    # Ensure histograms are not zero
    hist_P[hist_P == 0] = 1e-10
    hist_Q[hist_Q == 0] = 1e-10
    
    # Calculate the Chi-square distance
    distance = np.sum((hist_P - hist_Q)**2 / (hist_P + hist_Q))
    
    return distance

def chi2_distance(A, B):
 
    # compute the chi-squared distance using above formula
    chi = 0.5 * np.sum([((a - b) ** 2) / (a + b) 
                      for (a, b) in zip(A, B)])

    return chi