from selenium import webdriver
import time

def before_all(context):
    context.i = '0'

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome('C:\\Users\\fmoreiraf\\Desktop\\testePython\\Star\\bin\chromedriver.exe')
    

def after_scenario(context, scenario):
    context.driver.quit()
 