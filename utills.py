import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(path):
    return pd.read_csv(path)

def plot_class_distribution(df, target_col="Cover_Type"):
    sns.countplot(x=target_col, data=df)
    plt.title("Forest Cover Type Distribution")
    plt.xlabel("Cover Type")
    plt.ylabel("Count")
    plt.show()