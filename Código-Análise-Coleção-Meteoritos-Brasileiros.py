#Análise de dados da colecao de meteoritos brasileiros catalogados
#Desenvolvido por Higor Martinez Oliveira

import matplotlib.pyplot as plt
import pandas as pd


dadosMeteoritos = pd.read_csv("Brazilian-Meteorites-Database.csv")


def descoberta():
    "Retorna a frequencia dos meteoritos catalogados por tipo de descoberta: se a queda foi testemunhada por alguém (queda observada) ou se o exemplar foi apenas encontrado no campo (achado)"

    frequencia = dadosMeteoritos["Descoberta"].value_counts()
    plt.axis("equal")
    frequencia.plot.pie(autopct = "%1.1f%%")
    plt.show()
    
    return frequencia


def tipo():
    "Retorna a frequencia dos meteoritos catalogados de acordo com a sua composicao: rochosa, metálica, mista"
    
    frequencia = dadosMeteoritos["Tipo"].value_counts()
    plt.axis("equal")
    frequencia.plot.pie(autopct = "%1.1f%%")
    plt.show()

    return frequencia


def meteoritosRochosos():
    "Retorna a frequencia dos meteoritos rochosos por classe"

    meteoritosRochosos = dadosMeteoritos[(dadosMeteoritos["Tipo"] == "Rochoso")]
    dadosClasse = meteoritosRochosos.value_counts()
    frequenciaClasse = meteoritosRochosos["Classe"].value_counts()
    frequenciaClasse.plot.pie(autopct = "%1.1f%%")

    plt.show()

    return frequenciaClasse


def meteoritosMetalicos():
    "Retorna a frequencia dos meteoritos metálicos por classe"

    meteoritosMetalicos = dadosMeteoritos[(dadosMeteoritos["Tipo"] == "Metálico")]
    dadosClasse = meteoritosMetalicos.value_counts()
    frequenciaClasse = meteoritosMetalicos["Classe"].value_counts()
    frequenciaClasse.plot.pie(autopct = "%1.1f%%")

    plt.show()

    return frequenciaClasse


def procuraClasse(classe):
    "Retorna os dados dos meteoritos de uma certa classe (entrada deve ser uma string)"
    
    resultadoBuscaClasse = dadosMeteoritos[(dadosMeteoritos["Classe"] == classe)]
    dadosBusca = resultadoBuscaClasse.value_counts()

    return dadosBusca


def procuraAno(anoInicial, anoFinal):
    "Retorna os dados dos meteoritos descobertos num intervalo de anos"

    resultadoBuscaAno = dadosMeteoritos[(dadosMeteoritos["Ano"] >= anoInicial) & (dadosMeteoritos["Ano"] <= anoFinal)]
    dadosBusca = resultadoBuscaAno.value_counts()
    frequenciaBuscaAno = resultadoBuscaAno["Ano"].value_counts()
    frequenciaBuscaAnoTipo = resultadoBuscaAno["Tipo"].value_counts()
    frequenciaBuscaAno.plot.bar(color = "orange", rot = 0)
    plt.show()
    frequenciaBuscaAnoTipo.plot.bar(color = "orange", rot = 0)
    plt.show()

    print ("A frequencia por ano no intervalo dado é:")
    print(frequenciaBuscaAno)
    print("*********************************************")
    print ("A frequencia por tipo para o intervalo dado é:")
    print(frequenciaBuscaAnoTipo)
    print("*********************************************")
    
    return dadosBusca
    


