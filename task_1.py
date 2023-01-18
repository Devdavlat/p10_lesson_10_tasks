"""
a) release_year da 2020 va 2021 yildagi kinolar ma'lumotlari bilan birga alohida csv faylga yozing
b) listed_in ustunidan Comedies bo'lgan filmlarni alohida csv faylga yozing.
c) type Movie va country United States bo'lgan filmalarni alohida csv faylga yozing.
"""

import csv
from get_exseptions import write_exceptins


class Netflix:
    def __init__(self, file_csv):
        self.file = file_csv

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

    def __get_data_by_year(self):
        file = self.get_file()
        data = ['2020', '2021']
        result = []
        for i in file:
            if i.get('release_year') in data:
                result.append(i)

        return result

    def get_release_year_20_21(self):
        result_data = self.__get_data_by_year()
        header = [i for i in self.get_file()[0]]

        self.__custom_csv_file('netflix_by_year_20_21.csv', header, result_data)

    def __get_data_by_type(self):

        file = self.get_file()
        type_ = 'Comedies'
        result = []
        for i in file:
            temp_listed_in = (i.get('listed_in')).split()
            if type_ in temp_listed_in:
                result.append(i)

        return result

    def get_listed_in(self):
        header = [i for i in self.get_file()[0]]
        rows = self.__get_data_by_type()
        csv_file_name = 'netflix_by_listed_in.csv'
        self.__custom_csv_file(csv_file_name, header, rows)

    def __get_data_by_country_type(self):

        file = self.get_file()
        total_cases = 'TotalCases'

        result = []
        for i in file:
            temp_number = (i.get('country')).split(',')
            temp_type = i.get('type')

            if country in temp_country_name and temp_type == type_:
                result.append(i)
        return result

    def get_data_by_country_and_type(self):
        header = [i for i in self.get_file()[0]]
        rows = self.__get_data_by_country_type()

        csv_file_name = 'netflix_by_country_type.csv'
        # print(rows)
        self.__custom_csv_file(csv_file_name, header, rows)


netflix_obj = Netflix('netflix_titles.csv')
# print(netflix_obj.get_release_year_20_21())
print(netflix_obj.get_data_by_country_and_type())

# def get_order_date():
#     info = get_full_info()
#     result = []
#     data = "04/10/19"
#     for i in info:
#         if i.get("Order Date") > data:
#             result.append(i)
#     return result
#
#
# def write_order_date():
#     order_date = [i for i in get_order_date()]
#     columns = [i for i in order_date[0]]
#     try:
#         with open("order_date.csv", "w", newline="") as files:
#             writer = csv.DictWriter(files, fieldnames=columns)
#             writer.writeheader()
#             writer.writerows(order_date)
#     except FileNotFoundError as e:
#         write_exceptions(e)
#     return files
