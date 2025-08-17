import pandas as pd
import plotly.express as px


class Emissions:

    def __init__(self, csv):
        self.csv = csv

    def read_csv(self):
        return pd.read_csv(self.csv)

    def all_data(self):
        return pd.set_option('display.max_rows', 30000)


    
    
class Visualization:

    def __init__(self, dataframe):
        self.dataframe = dataframe


    def data_reset(self):
        reset = self.dataframe.reset_index()
        melted = reset.melt(id_vars='Year', var_name='Continents', value_name='Annual CO₂ Emissions')
        
        return melted
        

    def line(self):
        melted = self.data_reset()

        return px.line(melted, x='Year', y='Annual CO₂ Emissions',
                       color='Continents', title='CO₂ Emissions Trends for each Continent')
        

    def scatter(self):
        melted = self.data_reset()

        return px.scatter(melted, x='Year', y='Annual CO₂ Emissions',
                          color='Continents', title='CO₂ Emissions Trends for each Continent')

    def bar(self):
        melted = self.data_reset()

        return px.bar(melted, x='Year', y='Annual CO₂ Emissions',
                      color='Continents', title='CO₂ Emissions Trends for each Continent')

    def histogram(self):
        melted = self.data_reset()
        
        return px.histogram(melted, x='Year', y='Annual CO₂ Emissions',
                            title='CO₂ Emissions Trends for each Continent',
                            color='Continents', histfunc='avg')










    
    
