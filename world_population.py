from read_csv import read

def world_population(data):
    
    data = data
    
    population_1970 = []
    population_1980 = []
    population_1990 = []
    population_2000 = []
    population_2010 = []
    population_2015 = []
    population_2020 = []
    population_2022 = []

    for population in data:
        population_1970.append(int(population['1970 Population']))
        population_1980.append(int(population['1980 Population']))
        population_1990.append(int(population['1990 Population']))
        population_2000.append(int(population['2000 Population']))
        population_2010.append(int(population['2010 Population']))
        population_2015.append(int(population['2015 Population']))
        population_2020.append(int(population['2020 Population']))
        population_2022.append(int(population['2022 Population']))

    labels = ['1970', '1980', '1990', '2000', '2010', '2015', '2020', '2022']
    values = [
            sum(population_1970), 
            sum(population_1980), 
            sum(population_1990), 
            sum(population_2000), 
            sum(population_2010),
            sum(population_2015),
            sum(population_2020),
            sum(population_2022)
            ]
    
    return labels, values


if __name__ == '__main__':
    world_population('world_population.csv')