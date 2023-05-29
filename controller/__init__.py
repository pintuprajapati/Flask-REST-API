import os
import glob

# In this __all__ = [] list, we are appending controller files, so that we can import them using "from controller import *" 
__all__ = [os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]

# i.e. # __all__ = ['user_controller', 'product_controller']