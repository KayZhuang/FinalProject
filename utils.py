import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

#df_mom = df_income.loc[df_income['交易对方'] == '妈👩']
#df_dad = df_income.loc[df_income['交易对方'] == '爸👨']
#df_momo = df_out.loc[df_out['交易对方'] == '妈👩']
#df_dado = df_out.loc[df_out['交易对方'] == '爸👨']


def bar_chart_example(x_ser,y_ser,title,x,y):
    plt.figure() # to create a new current figure
    plt.bar(x_ser, y_ser)
    plt.xticks(rotation = 25, ha="right")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    plt.grid()

