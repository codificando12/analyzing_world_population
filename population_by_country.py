from read_csv import read


def country_population(country_dict):

    country_population ={
        '2022': int(country_dict['2022 Population']),
        '2020': int(country_dict['2020 Population']),
        '2015': int(country_dict['2015 Population']),
        '2010': int(country_dict['2010 Population']),
        '2000': int(country_dict['2000 Population']),
        '1990': int(country_dict['1990 Population']),
        '1980': int(country_dict['1980 Population']),
        '1970': int(country_dict['1970 Population'])
        }
    
    labels = country_population.keys()
    values = country_population.values()

    return labels, values

if __name__ == '__main__': 
   country_population('./world_population.csv')