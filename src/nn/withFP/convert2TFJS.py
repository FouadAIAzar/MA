import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflowjs as tfjs
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

model = load_model("model.h5")
tfjs.converters.save_keras_model(model,'models')


