# Meteoritos Brasileiros
Este repositório contém um banco de dados em .csv da coleção de meteoritos oficialmente catalogados no Brasil, juntamente com um código em Python para realizar algumas análises de dados acerca de aspectos como: tipo de descoberta, composição, classe e ano de descoberta dos exemplares. 

A seguir, os dados que podem ser extraídos a partir das funções do código: 

*descoberta()*

Permite gerar um gráfico dos meteoritos catalogados de acordo com o seu tipo de descoberta: se a queda foi testemunhada por alguém (queda observada) ou se o exemplar foi apenas encontrado no campo (achado). A frequência é retornada ao final. 

*tipo()*

Permite gerar um gráfico com a distribuição dos meteoritos catalogados de acordo com a sua composição: rochosa, metálica ou mista. A frequência é retornada ao final. 

*meteoritosRochosos()*

Permite obter o gráfico dos meteoritos do tipo rochoso da coleção brasileira com a sua distribuição por classes. A frequência é retornada ao final. 

*meteoritosMetálicos()*

Permite obter o gráfico dos meteoritos do tipo metálico da coleção brasileira com a sua distribuição por classes. A frequência é retornada ao final. 

*procuraClasse(classe)*

Permite procurar pelos dados completos de todos os meteoritos pertencentes a uma certa classe, passada em formato de string para a função. 

*procuraAno(anoInicial, anoFinal)*

Permite gerar um gráfico com o número de meteoritos descobertos por ano em um dado intervalo de tempo passado em formato int para a função, além de um gráfico com o total de meteoritos por tipo descobertos neste intervalo. Ao final, a frequência dos dados é retornada.

O livro com uma análise completa da coleção de meteoritos brasileiros está disponível em: https://drive.google.com/file/d/16tR0_GGwjBFEdjYfRk4kwqdNeU26jjeK/view
