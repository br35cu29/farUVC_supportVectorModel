# Predicting log reductions of infectious aerosols indoors with a support vector model

## Overview

A support vector model (SVM) is provided for predicting the effectiveness of a far-UVC system indoors. Simple system and room specifications are required as model inputs. The model was trained on the results of computational fluid dynamics (CFD) simulations. Refer to Cummings et al. (in press) for a detailed accounting of the scope, capabilities, and limitations of this model.

## Model details
#### The SVM accepts five input parameters, sequentially:
 - The UV power density (mW of optical power per m^2^).
 - The susceptibility of the target pathogen to 222-nm UV light (m^2^ W^-1^ s^-1^). 
 - The room air exchange rate (h^-1^).
 - The coverage area of each lamp (m^2^ per lamp).
 - The beam angle of each lamp (°).

#### Assumptions
 - All lamps are ceiling-mounted and regularly-spaced, pointing downward. 
 - Only one type of lamp is used in a room.
 - 3 m (10 ft) ceiling heights.
#### Outputs
The model estimates the room-averaged log reductions.
#### Validation
Model estimations were in good agreement with the CFD results, having a residual standard error (RSE) of 0.13. 
## Contents
The "model_and_example" folder contains two files:

 - svm.pkl which contains the trained model.
 - example.py which demonstrates how to load and execute the model using Python.

In the example, users specify the number of lamps, the optical power output emitted from each lamp, the lamp beam angle, the room floor area, the room air exchange rate, and the viral susceptibility. The code calculates the UV power density and the coverage area from the provided inputs. The SVM outputs the best-estimate log reduction value.

Users also specify a confidence level. Using the RSE = 0.13 associated with the model, the script calculates the log reduction threshold above which the actual value is expected at the stated confidence level.
## Citation
If you use this model, please cite:
>Cummings BE, Haas CN, Lo LJ, Sales CM, Waring MS. 2025. Inactivating airborne pathogens indoors with 222-nm far-UVC systems: Insights from a CFD-based analysis and a predictive performance model. In press.
