import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def all_years(): #Probably a better way to do this
    return ["2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"] #All the years that content has been added to neflix

def all_months():
    return ["January","February","March","April","May","June","July","August","September","October","November","December"]

def valid_dates(dataframe):
    """
    Returns the dataframe where entries with "Uknown date_added" are removed
    """
    dataframe = dataframe[dataframe.date_added != "Unknown date_added"]
    return dataframe

def create_year_column(dataframe):
    dataframe["year"] = dataframe["date_added"].apply(lambda x: x.split(", ")[-1])  #Lambda: Iterates though every entry. Splits by comma and extracts the last value (which is year)
    return dataframe

def create_month_column(dataframe):
    dataframe["month"] = dataframe["date_added"].apply(lambda x: x.lstrip().split(" ")[0]) #Remove leading whitespace using lstrip(), then using split by whitespace and extracting the first value
    return dataframe

def sort_by_year(dataframe):
    df = dataframe.groupby("year")
    return df

def monthly_yearly_table(dataframe):
    df = dataframe.groupby("year")
    df = df['month'].value_counts() #count values in month
    df = df.unstack() 
    df = df.fillna(0) #fill nans with 0
    return df


def heatmap(dataframe,title,xlab,ylab):
    """
    dataframe be a readily counted dataframee
    """
    plt.figure(figsize=(15,15))
    plt.pcolor(dataframe, cmap="Greens", edgecolors = "white",linewidths=2)
    plt.xticks(np.arange(0.5, len(dataframe.columns), 1), dataframe.columns)
    plt.yticks(np.arange(0.5, len(dataframe.index), 1), dataframe.index)
    plt.colorbar(orientation="horizontal")
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)

def find_missing_months(dataframe):
    months = all_months()
    missing_months = []
    for m in months:
        if m not in dataframe.columns:
            missing_months.append(m)
    return missing_months

def add_missing_months(dataframe):
    missing = find_missing_months(dataframe)
    for m in missing:
        dataframe[m] = np.zeros(len(dataframe.index))
    return dataframe

def find_missing_years(dataframe):
    years = all_years()
    missing_yrs = []
    for y in years:
        if y not in dataframe.index:
            missing_yrs.append(y)
    return missing_yrs

def add_missing_yrs(dataframe):
    missing = find_missing_years(dataframe)
    for y in missing:
        dataframe.loc[y] = np.zeros(len(dataframe.columns))
    return dataframe


def create_table(dataframe):
    df = monthly_yearly_table(dataframe)
    df = add_missing_months(df)
    df = add_missing_yrs(df)
    df = df[all_months()]
    df = df.sort_values(by = "year")
    return df