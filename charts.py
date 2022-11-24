import matplotlib.pyplot as plt

def generate_bar_chart(country, labels, values):
    
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.title(country)
    plt.savefig(f'./img/{country}.png')
    plt.close()

def generate_pie_chart(labels, values):

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()

if __name__ == '__main__':
    countries = [
        {
        'country': 'argentina',
        'population': 400
        },
         {
        'country': 'bolibia',
        'population': 1000
        }
        ]
    # generata_bar_chart(labels, values)
    generate_pie_chart(countries['country'], countries['population']) 
    