import csv


def read(path):
    with open(path, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            itarable = zip(header, row)
            country_dic = {key: value for key, value in itarable}
            data.append(country_dic)

        return data
    
if __name__ == '__main__':
    print(read('./world_population.csv'))
    