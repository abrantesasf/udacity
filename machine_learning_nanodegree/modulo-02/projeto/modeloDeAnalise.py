#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 18:06:09 2018

@author: abrantesasf
"""

#%% Ambiente da análise
def ambienteDaAnalise():
    """
    Abrantes Araújo Silva Filho
    abrantesasf@gmail.com
    
    Imprime informações a respeito do ambiente de análise utilizado,
    incluindo detalhes do hardware, software, versões do Python e
    packages utilizados.
    
    Pré-requisitos: utiliza os packages subprocess, sys, pip, platform,
                    psutil e math
    
    Limitações: essa função foi pensada para sistemas operacionais
                Linux, não testada em Windows ou Mac. Na verdae nem me
                preocupei em preparar a função para funcionar corretamente
                em Windows ou Mac, portanto provavelmente ela NÃO FUNCIONARÁ
                nesses sistemas operacionais!
    
    Inputs: nenhum
    
    Outputs: print de informações
    
    Retorno: nenhum
    """
    import os
    import subprocess
    import sys
    import pip
    import platform
    import psutil
    import math
    
    data = subprocess.check_output(['date', '+%Y-%m-%d, %H:%M (UTC %:z), %A']).replace('\n', '')
    
    nomeComputador = platform.node()
    arquiteturaComputador = platform.machine()
    processador = platform.processor()
    MHz = psutil.cpu_freq()[2] / 1000.0
    coresFisicos = psutil.cpu_count(logical = False)
    coresLogicos = psutil.cpu_count()
    memoriaFisica = math.ceil(psutil.virtual_memory()[0] / 1024 / 1024 / 1024.0)
    
    plataforma = platform.system()
    plataforma2 = sys.platform
    osName = os.name
    versaoSO = platform.version()
    release = platform.release()
    
    versaoPython = platform.python_version()
    implementacaoPython = platform.python_implementation()
    buildPython = platform.python_build()[0] + ', ' + platform.python_build()[1]
    interpreterPython = sys.version.replace('\n', '')
    
    pacotes = sorted(["%s==%s" % (i.key, i.version) \
                      for i in pip.get_installed_distributions()])
    
    print('|-----------------------------------------------------------|')
    print('|                         HARDWARE                          |')
    print('|-----------------------------------------------------------|')
    print('Host:           ' + nomeComputador)
    print('Arquitetura:    ' + arquiteturaComputador)
    print('Processador:    ' + processador + ' de ' + str(MHz) + ' MHz (' \
          + str(coresFisicos) + ' cores físicos e ' + str(coresLogicos) + \
          ' cores lógicos)')
    print('Memória física: ' + str(memoriaFisica) + ' GB')
    print('|-----------------------------------------------------------|')
    print('|                         SOFTWARE                          |')
    print('|-----------------------------------------------------------|')
    print('Plataforma:     ' + plataforma + ' (' + plataforma2 + ', ' + osName \
                                               + ')')
    print('Versão:         ' + versaoSO)
    print('Release:        ' + release)
    print('|-----------------------------------------------------------|')
    print('|                         PYTHON                            |')
    print('|-----------------------------------------------------------|')
    print('Python:         ' + versaoPython)
    print('Implementação:  ' + implementacaoPython)
    print('Build:          ' + buildPython)
    print('Interpreter:    ' + interpreterPython)
    print('|-----------------------------------------------------------|')
    print('|                         PACKAGES                          |')
    print('|-----------------------------------------------------------|')
    for pacote in pacotes:
        print(pacote)
    print('|-----------------------------------------------------------|')
    print('|                         DATA                              |')
    print('|-----------------------------------------------------------|')
    print('A data atual do sistema é: ' + data)

ambienteDaAnalise()


#%% Imports básicos
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import stemgraphic


#%% Definição de diretório de trabalho


#%% Leitura dos dados
# Input dos dados e tamanho do dataset


#%% Conhecendo as variáveis
# Codebook de cada variável


#%% Ajustes básicos das variáveis
# Acertos rápidos e diretos, como por exemplo transformar datas em formato
# string para formato de data, etc.

# Novo codebook das variáveis, se necessário


#%% Variáveis missing
# Existem dados missing? O que fazer com eles?


#%% EDA: univariada

# Stem-and-Leaf, histograma, boxplot, 5-num, letter value,
# etc. para cada variável, onde for pertinente
# Notar, especialmente:
#    - A forma e o comportamente da distribuição como um todo
#    - A simetria ou assimetria da distribuição
#    - Ocorrência de padrões nos dados
#    - Separação aparente entre grupos
#    - Ocorrência de valores inesperadamente populares ou impopulares
#    - O intervalo no qual os dados se espalham
#    - Concentrações ou gaps nos dados
#    - Valores distantes e/ou outliers