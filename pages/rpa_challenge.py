import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from documents.data_rpa_challenge import DataRpaChallenge


class RpaChallenge:
    def __init__(self):
        self.planilha = DataRpaChallenge()
        self.url = "https://www.rpachallenge.com"
        self.robo = webdriver.Chrome(executable_path="chromedriver.exe")
        self.phone_number = "[ng-reflect-name='labelPhone']"
        self.role_in_company = "[ng-reflect-name='labelRole']"
        self.address = "[ng-reflect-name='labelAddress']"
        self.first_name = "[ng-reflect-name='labelFirstName']"
        self.company_name = "[ng-reflect-name='labelCompanyName']"
        self.email = "[ng-reflect-name='labelEmail']"
        self.last_name = "[ng-reflect-name='labelLastName']"
        self.btn_submit = ".btn.uiColorButton"

    def fill_out_form(self):
        self.robo.get(self.url)
        for linha in range(2, len(self.planilha.tab['A']) - 2):
            if self.planilha.tab.cell(row=linha, column=1).value != None:
                self.robo.find_element(By.CSS_SELECTOR, self.first_name).send_keys(self.planilha.tab.cell(row=linha, column=1).value)
                self.robo.find_element(By.CSS_SELECTOR, self.last_name).send_keys(self.planilha.tab.cell(row=linha, column=2).value)
                self.robo.find_element(By.CSS_SELECTOR, self.company_name).send_keys(self.planilha.tab.cell(row=linha, column=3).value)
                self.robo.find_element(By.CSS_SELECTOR, self.role_in_company).send_keys(self.planilha.tab.cell(row=linha, column=4).value)
                self.robo.find_element(By.CSS_SELECTOR, self.address).send_keys(self.planilha.tab.cell(row=linha, column=5).value)
                self.robo.find_element(By.CSS_SELECTOR, self.email).send_keys(self.planilha.tab.cell(row=linha, column=6).value)
                self.robo.find_element(By.CSS_SELECTOR, self.phone_number).send_keys(self.planilha.tab.cell(row=linha, column=7).value)
                self.robo.find_element(By.CSS_SELECTOR, self.btn_submit).click()
            else:
                break
        pyautogui.alert('Finalizado!')
