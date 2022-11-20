from read_csv import read
from population_by_country import country_population
from charts import generate_bar_chart
from world_population import world_population
from charts import generate_pie_chart
from pie_wolrd_population import pie_percentage


def run():
    data = read('./world_population.csv')
        
    choose = input('What would you like to know, the population grown in one country(C)\
or the world population growth(W) or know the percentage(P)?(choose C or W or P): ')
    choose = choose.upper()
    if choose == 'C':
        countries = input('Choose a country: ')
        countries = countries.capitalize()
        for country in data:
            if country['Country/Territory'] == countries:
                labels , values = country_population(country)
                generate_bar_chart(countries, labels, values)
    elif choose == 'W':
        labels, values = world_population(data)
        generate_bar_chart('Wolrd Population Growth', labels, values)
    elif choose == 'P':
        values, labels = pie_percentage(data)
        generate_pie_chart(values, labels)

        


if __name__ == '__main__':
    run()