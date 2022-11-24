from read_csv import read

def pie_percentage(data):


    countries = list(map(lambda country: country['Country/Territory'], data))
    percentages = list(map(lambda percent: float(percent['World Population Percentage']), data))

    return countries, percentages


if __name__ == '__main__':
    print(pie_percentage('world_population.csv'))