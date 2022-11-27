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
import streamlit.components.v1 as components

st.title("Treatments Systems and Drug Analysis on Diabetes and Readmission Rate")

st.header("Data Ingestion and Cleaning")
"The raw input was a UCI dataset with 101,766 patient encounters and 50 features. The original dataframe is shown here."

data = pd.read_csv('dataset_diabetes/diabetic_data.csv')
st.dataframe(data)

"We created a graph showing the pairwise drug combinations the patients have taken. The red edges have an edge weight >1000, meaning that at least 1000 patients took this pair of drugs."
components.iframe(src='http://127.0.0.1:8050/', width=1000, height=600)
