Feature:  Busca ID para saber se NAO está instalado

Scenario: Buscar ID que não esteja instalado

Given Estar logado no site do vivo star 
When Buscar o ID 1229300
Then verificar se NAO está instalado

