import openpyxl


class DataRpaChallenge:
    def __init__(self):
        self.spreadsheet = openpyxl.load_workbook('documents/challenge.xlsx')
        self.tab = self.spreadsheet.active