import argparse
import math
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
from typing import Optional, Tuple, Dict, List
import time
import json
from pathlib import Path


data = np.load('burgers1D_training_data_Nu0.01.npz')
uu = data['u']  # u(x,t)
