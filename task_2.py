"""
a) TotalCases ustunda 100000 va 1000000 orasidagi holatlarni alohida csv faylga yozing.
b) Country/Region dagi davlatlarni kiritiganda ActiveCases qiymatini qaytarish uchun funksiya yarating.
c) Continent dagi mintaqa kiritiganda umumiy TotalCases qaytini qaytarish uchun funksiya yarating.
"""
import csv
from get_exseptions import write_exceptins
from pprint import pprint


class WorksWCovid19:
    def __init__(self, csv_file):
        self.file = csv_file

    def get_file(self):
        with open(self.file, 'r', encoding='utf-8') as file:
            res = csv.DictReader(file)
            return [i for i in res]

    @staticmethod
    def __custom_csv_file(csv_file_name, header, rows):
        try:
            with open(csv_file_name, "w", encoding='utf8', newline="") as files:
                writer = csv.DictWriter(files, fieldnames=header)
                writer.writeheader()
                writer.writerows(rows)
        except Exception as e:
            write_exceptins(Exception, e)

    def __get_sorted_data_by_number(self):
        file = self.get_file()
        numbers_list = [100000, 1000000]
        total_cases = 'TotalCases'

        result = []
        for i in file:
            temp_country_name = int(i.get(total_cases))

            if numbers_list[0] < temp_country_name < numbers_list[1]:
                result.append(i)
        return result

    def get_data_by_country_and_type(self):
        header = [i for i in self.get_file()[0]]
        rows = self.__get_sorted_data_by_number()

        csv_file_name = 'covid_data_by_total_cases.csv'

        self.__custom_csv_file(csv_file_name, header, rows)

    def get_data_by_country_name(self, country_name):
        file = self.get_file()
        result = []
        for i in file:
            data = i.get('Country/Region')
            if data == country_name:
                print(i.get('ActiveCases'))
                result.append(i)

        return pprint(result)

    def get_data_by_country_mintage(self, country_name):
        file = self.get_file()
        result = []
        for i in file:
            data = i.get('Continent')
            if data == country_name:
                res = f"{i}\n TotalCases : {i.get('TotalCases')}"
                result.append(res)

        return pprint(result)


covid_19_obj = WorksWCovid19('worldometer_data.csv')
# print(covid_19_obj.get_data_by_country_and_type())
# print(covid_19_obj.get_data_by_country_name('Brazil'))
print(covid_19_obj.get_data_by_country_mintage('Asia'))
