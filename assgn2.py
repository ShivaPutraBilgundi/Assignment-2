import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def read_data(file_path):
    """

    Parameters
    ----------
    file_path : dataset for the the code

    Returns
    -------
    data_all : returns years as columns
    data_by_country : returns countries as columns

    """
    
    
    data_all = pd.read_csv(file_path, skiprows=3)
    data_no_code = data_all.drop(columns=["Country Code", "Indicator Name", "Indicator Code"], axis=1)
    data_by_country = data_no_code.set_index('Country Name')
    data_by_country = data_by_country.transpose()

    return data_all, data_by_country

file_path = "API_19_DS2_en_csv_v2_4902199.csv"
years_data, countries_data = read_data(file_path)


years_data = years_data.fillna(0)

def plot_heatmap():
    """

    Yields
    ------
    None.

    """
    
    
    grouped_data = years_data.groupby("Country Name")
    grouped_bd = grouped_data.get_group("Canada")
    grouped_bd = grouped_bd.set_index("Indicator Name")

    grouped_bd = grouped_bd.loc[:, '2000':'2021']
    grouped_bd = grouped_bd.transpose()

    grouped_bd_selected = grouped_bd[["Forest area (% of land area)",
                                       "Cereal yield (kg per hectare)",
                                       "Nitrous oxide emissions (thousand metric tons of CO2 equivalent)",
                                       "Urban population growth (annual %)",
                                       "Agriculture, forestry, and fishing, value added (% of GDP)",
                                       "Total greenhouse gas emissions (kt of CO2 equivalent)"]]
    
    correlation_matrix = grouped_bd_selected.corr()

    correlation_matrix.index = ["Forest area", "cereal", "Nitrous oxide emissions","Urban population", "agriculture", "total greenhouse"]

    correlation_matrix.columns = ["Forest area", "cereal", "Nitrous oxide emissions","Urban population", "agriculture", "total greenhouse"]

    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Canada Indicators correlation", fontsize=20)


plot_heatmap()

    
def plot_correlation_line(data, indicator):
    """

    Parameters
    ----------
    data : dataset for the code
    indicator : indicator for the graph

    Returns
    -------
    None.

    """
    
    
    data_clean = data.drop(["Country Code","Indicator Code"],axis=1)
    data_clean.set_index("Indicator Name", inplace=True)
    data_clean = data_clean.loc[indicator]
    data_clean = data_clean.reset_index(level="Indicator Name")
    data_clean.groupby(["Country Name"]).sum()
    data_clean = data_clean.loc[data_clean["Country Name"].isin(["India", "Afghanistan", "Bangladesh", "Canada", "United Kingdom", "Brazil", "Germany", "Australia", "Croatia","China"]), :]
    
    data_clean.plot(x="Country Name", y=['1965', '1970', '1975', '1980', '1985', '1990','1995','2000','2005', "2018"], figsize=(15,5))
    plt.title(indicator, fontsize=20)
    plt.show()

plot_correlation_line(years_data, "Forest area (% of land area)")
plot_correlation_line(years_data, "Total greenhouse gas emissions (kt of CO2 equivalent)")
plot_correlation_line(years_data, "Cereal yield (kg per hectare)")
plot_correlation_line(years_data, "Agriculture, forestry, and fishing, value added (% of GDP)")

def plot_correlation_bar(data, indicator):
    """


    Parameters
    ----------
    data : dataset for the code
    indicator : indicator for the graph.

    Returns
    -------
    None.

    """
    
    data_clean = data.drop(["Country Code","Indicator Code"],axis=1)
    data_clean.set_index("Indicator Name", inplace=True)
    data_clean = data_clean.loc[indicator]
    data_clean = data_clean.reset_index(level="Indicator Name")
    data_clean.groupby(["Country Name"]).sum()
    data_clean = data_clean.loc[data_clean["Country Name"].isin(["Afghanistan", "Bangladesh", "Canada", "Germany","Croatia"]), :]
    data_clean.plot(x="Country Name", y=['1965', '1970', '1975', '1980', '1985', '1990','1995','2000','2005'], figsize=(15,5), kind="bar")
    plt.title(indicator, fontsize=20)
    plt.show()

plot_correlation_bar(years_data, "Nitrous oxide emissions (thousand metric tons of CO2 equivalent)")

