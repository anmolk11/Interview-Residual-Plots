import numpy as np
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def make_plot(df : pd.DataFrame,target : str):
    X = df.drop([target],axis = 1)
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    residuals = y_test - y_pred

    plt.figure(figsize=(8, 6))
    sns.scatterplot(x = y_pred.flatten(), y = residuals.values.flatten()) 
    plt.axhline(y=0, color = 'r', linestyle = '--', linewidth = 2)  
    plt.title('Residual Plot for Linear Regression')
    plt.xlabel('Predicted Values')
    plt.ylabel('Residuals')

    
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)

    plot_image = base64.b64encode(image_stream.read()).decode('utf-8')
    return plot_image