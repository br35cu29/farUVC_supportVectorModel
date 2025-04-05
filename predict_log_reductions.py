import joblib
import numpy as np
from scipy.stats import norm


# -----------
# User inputs
# -----------

A_floor = 20 # m2
N_lamps = 4 # lamp
P_lamp = 250 # mW lamp-1; emitted optical power from each lamp
k = 0.5 # m2 W-1 s-1; virus UV susceptibility constant
aer = 1 # h-1; air changes per hour 
beam_angle  = 100 # ° (Force between 60 and 150)
confidence = 0.75 # Fraction; must be between 0.0 and 1.0


# ----------------------------
# SVM - Predict log reductions
# ----------------------------

# Model parameters
rse_LR = 0.13 # residual standard error of the SVM

# Calcs
uvpd = N_lamps*P_lamp/A_floor # mW m-2
coverage = A_floor/N_lamps # m2 lamp-1

# By convention, the model accepts the log (base 10) of the following five 
#   parameters in this order: [uvpd, k, aer, coverage, beam_angle]
x = np.log10([uvpd, k, aer, coverage, beam_angle])

# SVR.predict expects a 2D array, so the data must be reshaped
x = x.reshape(1, -1)

# Load and execute the trained model
model = joblib.load("svr_model_20250401.pkl")
lr0 = model.predict(x)[0]

# Compute the lower bound at the specified confidence
quantile = norm.ppf(confidence) 
lr1 = lr0 - rse_LR*quantile
if lr1 < 0:
    lr1 = 0 # Ensure log reduction is non-negative

# Print results 
print(f'Best-estimate Log reductions = {lr0:.3f}')
print(f'{confidence*100:.0f}% confident Log reductions > {lr1:.3f}')
