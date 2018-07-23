from behave import given, when, then
from selenium import webdriver
from pages.star_page import star
import time


@given(u'Estar logado no site do vivo star')
def step_impl(context):
    context.i = '0'
    context.driver.get("http://10.129.181.122:7010/Star/web/Login")
    context.star = star(context.driver)
    context.star.logar('LUIZ', 'STAR01!')
    time.sleep(2)

@when(u'Buscar o ID 1229300')
def step_impl(context):
    context.star.buscarID('1229287')
    
@then(u'verificar se NAO está instalado')
def step_impl(context):
   context.i = context.star.valida_status(context.i)
    
