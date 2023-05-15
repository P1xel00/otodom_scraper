import pandas as pd
import datetime
# necessary to import openpyxl bcs pandas needs it to export to excel
import openpyxl

now = datetime.datetime.now()


class Export:
    def __init__(self, data, type_of_search):
        self.data = data
        self.type_of_search = type_of_search

    def to_excel(self):
        frame = {'Adres': [x for x in self.data[0]],
                 'Metraż': [x for x in self.data[1]],
                 'Cena': [x for x in self.data[2]],
                 'Czynsz': [x for x in self.data[4]],
                 'Link': [x for x in self.data[3]]

                 }

        df = pd.DataFrame(frame)

        df.to_excel(f"./{self.type_of_search}_{now.strftime('%Y-%m-%d_%H-%M')}.xlsx", index=False)
