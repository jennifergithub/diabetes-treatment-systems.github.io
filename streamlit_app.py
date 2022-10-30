"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import interpret
from interpret.perf import ROC
from interpret.data import Marginal
from interpret.data import ClassHistogram
from interpret import show
from interpret.glassbox import ExplainableBoostingClassifier
from sklearn.model_selection import train_test_split
import sklearn
from collections import Counter
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import missingno as msno
import seaborn as sns
import pandas as pd

data = pd.read_csv('dataset_diabetes/diabetic_data.csv')

st.dataframe(data)
