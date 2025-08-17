import os
import pandas as pd
import plotly.express as px
from emission_class import Emissions
from emission_class import Visualization



def file_setup():

    file = 'co-emissions-per-capita.csv'
    df = Emissions(file)
    df_emissions = df.read_csv()
    


    return df_emissions


def cleaning_data():

    df_emissions = file_setup()

    # renaming columns
    df_emissions.rename(columns={'Entity': 'Continent',
                                 'Annual CO₂ emissions (per capita)': 'Annual CO₂ Emissions'},
                        inplace=True)

    # pivoting data file
    df_emissions = df_emissions.pivot(index='Year', columns='Continent', values='Annual CO₂ Emissions')

    # drop null values
    df_emissions.dropna(inplace=True)

    df_emissions = df_emissions[['Africa', 'Asia', 'Australia',
                                 'North America','South America',
                                 'Europe']] 

    return df_emissions


def choices():

    return '\n1) Scatter plot\n2) Line plot\n3) Bar graph\n4) Histogram\n5) Quit'


def visuals():
    
    df_emissions = cleaning_data()

    df = Visualization(df_emissions)

    print('View the annual CO₂ emissions for each continent during the last 29 years with various visualization methods') 
    while True:

        print(choices())
        visual_choice = input('\nSelect a visual representation: ')

        if visual_choice ==  '1':
            fig = df.scatter()
            fig
            fig.show()
        elif visual_choice == '2':
            fig = df.line()
            fig
            fig.show()
        elif visual_choice == '3':
            fig = df.bar()
            fig
            fig.show()
        elif visual_choice =='4':
            fig = df.histogram()
            fig
            fig.show()
        elif visual_choice =='5':
            break
        else:
            print('\nInvalid Option')
            

def converting_files():
    # converting csv directory to an excel directory
    csv_dir = r'C:\Users\William\OneDrive\Desktop\pd_projects\greenhouse-analysis'
    excel_dir = r'C:\Users\William\OneDrive\Desktop\pd_projects\greenhouse-analysis'

    os.makedirs(excel_dir, exist_ok=True)

    for filename in os.listdir(csv_dir):
        if filename.lower().endswith('.csv'):
            csv_path = os.path.join(csv_dir, filename)
            excel_path = os.path.join(excel_dir, filename[:-4]+'.xlsx')

            df = pd.read_csv(csv_path)
            file = 'co-emissions-per-capita.xlsx'

            df.rename(columns={'Entity': 'Continent',
                                 'Annual CO₂ emissions (per capita)': 'Annual CO₂ Emissions'},
                      inplace=True)

            # pivoting data file
            excel_data = df.pivot(index='Year', columns='Continent', values='Annual CO₂ Emissions')

            # drop null values
            excel_data.dropna(inplace=True)

            excel_data = excel_data[['Africa', 'Asia', 'Australia',
                                     'North America','South America',
                                     'Europe']]


            
            excel_data.dropna(inplace=True)

 
            
            excel_data.to_excel(file, index=True)


    
    

def main():

    visuals()

    
    user_excel = input('\nPress any button to access the data through an excel spread sheet: ')

    if user_excel:

        print('\nAnnual CO₂ emission data for each continent has been imported to your file explorer')
        converting_files()


if __name__ == "__main__":

    main()

    

    
    
         

     

    



    

    
    
          
    
        
        
                             
    
    
    

    
    
    


