from behave import given, when, then
from selenium import webdriver
from pages.star_page import star
import time


@given(u'acessar o site do Vivo Star e realizar o Login')
def step_impl(context):
    context.driver.get("http://10.129.181.122:7010/Star/web/Login")
    context.star = star(context.driver)
    context.star.logar('LUIZ', 'STAR01!') 

@when(u'Busco pelo ID 1229287')
def step_impl(context):
    context.star.buscarID('1229287')


@then(u'Verificar que o status está como instalado')
def step_impl(context):    
    context.i =  context.star.valida_status(context.i)
      
      

    