Feature: Busca superior
 
Scenario: Realizar a busca de um ID
Given acessar o site do Vivo Star e realizar o Login
When Busco pelo ID 1229287
Then Verificar que o status está como instalado

