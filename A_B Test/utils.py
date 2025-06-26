import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_count_of_categorical_varaibles(df,variable):
    """plot the count of categorical varaiables in histogram and pie chart

    Args:
        df (_type_): dataframe
        variable (_type_): column

    Returns:
        _type_: _description_
    """
    
    plt.figure(figsize = (6,10))

    #Countplot
    plt.subplot(1, 2, 1)
    sns.countplot(x=variable, order= df['variable'].value_counts().index, data=df)
    plt.title(f"Count of {variable}")
    plt.xticks(rotation=90)

    #Pie chart
    plt.subplot(1, 2, 2)
    counts = df[variable].value_counts()
    plt.pie(counts, labels = counts.index, autopct='%0.2f%%')
    plt.title('Pie-chart of ' + variable)
    
    #adjust tight layout
    plt.tight_layout()
    
    return plt.show()