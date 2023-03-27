# Pen Plotter Demo for 2023-03-30

Please set up this project BEFORE the lunch and learn on Thursday the 30th. You will need Python 3.11, but otherwise it 
should work right out-of-the-box thanks to Poetry. Once you've got your python environment set up, run `main.py`, and
if a window pops up with a blue grid of squares and red text that reads "Elk Plot Works!" you'll know that you're good
to go.

## Note for PyCharm Users
The `elkplot` library makes frequent use of nested `tqdm` progress bars, and the pycharm terminal doesn't handle those
well. To make them play nice again go to your run configuration and check the "emulate terminal in output console"
checkbox.
