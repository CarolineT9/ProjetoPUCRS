
#Importando CSV=======================================================================================================================================================================================================================
import csv

def ler_arquivo_csv(nome_arquivo):
    dados = []
    with open(nome_arquivo, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv, delimiter=';')
        for linha in leitor_csv:
            if linha[0] != 'data':  # Ignorar o cabeçalho do arquivo
                # Tratamento dos dados
                data = linha[0]
                precipitacao = float(linha[1])
                maxima = float(linha[2])
                minima = float(linha[3])
                horas_insol = float(linha[4])
                temp_media = float(linha[5])
                um_relativa = float(linha[6])
                vel_vento = float(linha[7])
                
                # Verificação de dados incorretos ou inconsistentes
                if precipitacao < 0:  # Ignorar dados negativos de precipitação
                    continue
                
                # Armazenar os dados em uma estrutura adequada
                dados.append({
                    'data': data,
                    'precipitacao': precipitacao,
                    'maxima': maxima,
                    'minima': minima,
                    'horas_insol': horas_insol,
                    'temp_media': temp_media,
                    'um_relativa': um_relativa,
                    'vel_vento': vel_vento
                })
    return dados
#Visualização de intervalo de dados ===================================================================================================================================================================================================
def visualizar_dados(dados, data_inicial, data_final, tipo_dados):
    tipos_permitidos = ['todos', 'precipitacao', 'temperatura', 'umidade_vento']
    
    # Validação dos dados de entrada
    if tipo_dados not in tipos_permitidos:
        print("Tipo de dados inválido.")
        return
    
    # Filtrar os dados de acordo com o período informado
    dados_filtrados = []
    for dado in dados:
        if data_inicial <= dado['data'] <= data_final:
            dados_filtrados.append(dado)
    
    # Verificar o tipo de dados solicitado
    if tipo_dados == 'todos':
        for dado in dados_filtrados:
            print(dado)
    elif tipo_dados == 'precipitacao':
        for dado in dados_filtrados:
            print(f"Data: {dado['data']}, Precipitação: {dado['precipitacao']}")
    elif tipo_dados == 'temperatura':
        for dado in dados_filtrados:
            print(f"Data: {dado['data']}, Máxima: {dado['maxima']}, Mínima: {dado['minima']}")
    elif tipo_dados == 'umidade_vento':
        for dado in dados_filtrados:
            print(f"Data: {dado['data']}, Umidade: {dado['um_relativa']}, Velocidade do Vento: {dado['vel_vento']}")
#Mês mais chuvoso:=======================================================================================================================================================================================
def mes_mais_chuvoso(dados):
    meses_precipitacao = {}
    
    for dado in dados:
        data_split = dado['data'].split('/')
        mes_ano = f"{data_split[1]}/{data_split[2]}"
        precipitacao = dado['precipitacao']
        
        if mes_ano in meses_precipitacao:
            meses_precipitacao[mes_ano] += precipitacao
        else:
            meses_precipitacao[mes_ano] = precipitacao
    
    mes_mais_chuvoso = max(meses_precipitacao, key=meses_precipitacao.get)
    precipitacao_maxima = meses_precipitacao[mes_mais_chuvoso]
    
    return mes_mais_chuvoso, precipitacao_maxima

#Média da temperatura mínima==================================================================================================================================================================================================
def calcular_medias_temperatura_minima(dados, mes):
    medias_mes = []
    todas_temperaturas_min = []
    
    for dado in dados:
        data_split = dado['data'].split('/')
        mes_dado = int(data_split[1])
        ano = int(data_split[2])
        
        if mes_dado == mes:
            todas_temperaturas_min.append(dado['minima'])
            if ano >= 2006 and ano <= 2016:
                medias_mes.append(dado['minima'])
    
    media_geral = sum(todas_temperaturas_min) / len(todas_temperaturas_min)
    media_mes = sum(medias_mes) / len(medias_mes)
    
    return media_mes, media_geral

#Gráficos:=======================================================================================================================================================================================================================
import matplotlib.pyplot as plt

def gerar_grafico_barras_medias_mes(dados, mes):
    anos = []
    medias_mes = []
    
    for dado in dados:
        data_split = dado['data'].split('/')
        mes_dado = int(data_split[1])
        ano = int(data_split[2])
        
        if mes_dado == mes and ano >= 2006 and ano <= 2016:
            anos.append(ano)
            medias_mes.append(dado['minima'])
    
    plt.bar(anos, medias_mes)
    plt.xlabel('Ano')
    plt.ylabel('Temperatura Mínima')
    plt.title(f'Médias de Temperatura Mínima do Mês {mes} nos Últimos 11 Anos')
    plt.show()

# Programa Principal================================================================================================================================================================================
# Leitura dos dados
nome_arquivo = 'OK_Anexo_Arquivo_Dados_Projeto.csv'
dados = ler_arquivo_csv(nome_arquivo)

#Vizualização de dados por um período eleito pelo usuário:=======================================================================================================================================
data_inicial = input("Informe a data inicial (DD/MM/AAAA): ")
data_final = input("Informe a data final (DD/MM/AAAA): ")
tipo_dados = input("Informe o tipo de dados (todos/precipitacao/temperatura/umidade_vento): ")

visualizar_dados(dados, data_inicial, data_final, tipo_dados)

#Mês mais chuvoso===============================================================================================================================================================================
mes_mais_chuv, precip_max = mes_mais_chuvoso(dados)
print(f"O mês mais chuvoso foi: {mes_mais_chuv} com precipitação de {precip_max}mm.")

#Média da temperatura mínima de um determinado mês==================================================================================================================================================
mes = int(input("Informe o número do mês (1-12): "))
media_mes, media_geral = calcular_medias_temperatura_minima(dados, mes)
print(f"Média da temperatura mínima do mês {mes} nos últimos 11 anos: {media_mes:.2f}")
print(f"Média geral da temperatura mínima para todo o período: {media_geral:.2f}")

#Gráfico de barras=======================================================================================================================================================================
mes_grafico = int(input("Informe o número do mês (1-12): "))
gerar_grafico_barras_medias_mes(dados, mes_grafico)