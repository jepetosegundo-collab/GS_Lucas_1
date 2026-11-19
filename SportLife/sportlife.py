#https://youtu.be/iLyFVkHXsEs?is=Wdvwsb5SayT1OGZ-
#[João Pedro Moraes Basques] — RM [571710] [Anderson Luiz Sanches] — RM [571834] [Guilherme Correia] — RM [568836]
# ============================================================
# SPORTLIFE
# Sistema de Monitoramento Ambiental de Centros Esportivos
# ============================================================

# CRITERIOS DE REFERENCIA:
#
# TEMPERATURA:
# Foi adotado 30 graus Celsius como criterio didatico de alerta.
# A temperatura do ar isolada nao determina a seguranca para
# a pratica esportiva. A avaliacao do calor tambem pode
# considerar umidade, vento e radiacao solar, como no indice WBGT.
#
# Referencia:
# Ministerio do Meio Ambiente do Japao - orientacoes para esportes.
#
# PM2.5:
# Foi adotado o valor de 50 microgramas por metro cubico para
# media de 24 horas, conforme o padrao intermediario PI-2 da
# Resolucao CONAMA 506/2024.
#
# Referencia:
# CONAMA - Resolucao 506/2024.
#
# RUIDO:
# Foi adotado o valor de 65 dB para o periodo diurno, considerando
# hipoteticamente uma area mista com predominancia de atividades
# culturais, lazer e turismo, conforme a Tabela 3 da ABNT NBR 10151.
#
# OBSERVACAO:
# Os dados sao simulados e informados pelo usuario.
# A media aritmetica do ruido e uma estatistica descritiva,
# nao substituindo uma avaliacao acustica oficial.

TEMP_MAX = 30
PM25_MAX = 50
RUIDO_MAX = 65


# ------------------------------------------------------------
# FUNCAO PARA CALCULAR MEDIA, MAIOR E MENOR VALOR
# ------------------------------------------------------------

def calcular_estatisticas(valores):

    soma = 0
    maior = valores[0]
    menor = valores[0]

    for valor in valores:
        soma = soma + valor

        if valor > maior:
            maior = valor

        if valor < menor:
            menor = valor

    media = soma / len(valores)

    return media, maior, menor


# ------------------------------------------------------------
# FUNCAO PARA RECEBER E VALIDAR VALORES NUMERICOS
# ------------------------------------------------------------

def ler_numero(mensagem, minimo):

    while True:
        try:
            valor = float(input(mensagem))

            if valor < minimo:
                print("Valor invalido. Digite um valor maior ou igual a", minimo)

            else:
                return valor

        except ValueError:
            print("Entrada invalida. Digite um numero.")


# ------------------------------------------------------------
# FUNCAO PARA RECEBER A QUANTIDADE DE LEITURAS
# ------------------------------------------------------------

def ler_quantidade():

    while True:
        try:
            quantidade = int(input("\nQuantas leituras deseja realizar? "))

            if quantidade > 0:
                return quantidade

            else:
                print("A quantidade deve ser maior que zero.")

        except ValueError:
            print("Digite uma quantidade inteira valida.")


# ------------------------------------------------------------
# FUNCAO PARA ANALISAR UMA LEITURA AMBIENTAL
# ------------------------------------------------------------

def analisar_ambiente(temperatura, pm25, ruido):

    alertas = []

    if temperatura > TEMP_MAX:
        alertas.append("Temperatura acima de 30 graus Celsius.")

    if pm25 > PM25_MAX:
        alertas.append("PM2.5 acima de 50 microgramas por metro cubico.")

    if ruido > RUIDO_MAX:
        alertas.append("Ruido acima de 65 dB no periodo diurno.")

    if len(alertas) == 0:
        print("Leitura dentro dos limites de referencia estabelecidos.")

    else:
        print("ALERTA AMBIENTAL:")

        for alerta in alertas:
            print("- " + alerta)

    return alertas


# ------------------------------------------------------------
# FUNCAO PARA GERAR O RELATORIO TXT
# ------------------------------------------------------------

def gerar_relatorio(dados, temperaturas, particulas, ruidos,
                    alertas_temp, alertas_pm25, alertas_ruido,
                    leituras_criticas, percentual, classificacao):

    numero = 1
    nome_arquivo = "relatorio_sportlife_" + str(numero) + ".txt"

    # Verifica se ja existe um relatorio com esse nome.
    # Caso exista, procura o proximo numero disponivel.

    while True:
        try:
            teste = open(nome_arquivo, "r", encoding="utf-8")
            teste.close()

            numero = numero + 1
            nome_arquivo = "relatorio_sportlife_" + str(numero) + ".txt"

        except FileNotFoundError:
            break

    media_temp, maior_temp, menor_temp = calcular_estatisticas(temperaturas)
    media_pm, maior_pm, menor_pm = calcular_estatisticas(particulas)
    media_ruido, maior_ruido, menor_ruido = calcular_estatisticas(ruidos)

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:

        arquivo.write("============================================\n")
        arquivo.write("             RELATORIO SPORTLIFE\n")
        arquivo.write("============================================\n\n")

        arquivo.write("Ambiente monitorado: Centro esportivo comunitario\n")
        arquivo.write("Quantidade de leituras: " + str(len(dados)) + "\n\n")

        arquivo.write("CRITERIOS DE REFERENCIA\n")
        arquivo.write("Temperatura: ate 30 graus Celsius\n")
        arquivo.write("PM2.5: ate 50 microgramas por metro cubico (media de 24 horas)\n")
        arquivo.write("Ruido: ate 65 dB (periodo diurno)\n\n")

        arquivo.write("ESTATISTICAS AMBIENTAIS\n\n")

        arquivo.write("TEMPERATURA DO AR\n")
        arquivo.write("Media: " + format(media_temp, ".2f") + " graus Celsius\n")
        arquivo.write("Maior valor: " + str(maior_temp) + " graus Celsius\n")
        arquivo.write("Menor valor: " + str(menor_temp) + " graus Celsius\n")
        arquivo.write("Ocorrencias acima do criterio: " + str(alertas_temp) + "\n\n")

        arquivo.write("MATERIAL PARTICULADO PM2.5\n")
        arquivo.write("Media: " + format(media_pm, ".2f") + " microgramas por metro cubico\n")
        arquivo.write("Maior valor: " + str(maior_pm) + " microgramas por metro cubico\n")
        arquivo.write("Menor valor: " + str(menor_pm) + " microgramas por metro cubico\n")
        arquivo.write("Ocorrencias acima do criterio: " + str(alertas_pm25) + "\n\n")

        arquivo.write("RUIDO AMBIENTAL\n")
        arquivo.write("Media aritmetica descritiva: " + format(media_ruido, ".2f") + " dB\n")
        arquivo.write("Maior valor: " + str(maior_ruido) + " dB\n")
        arquivo.write("Menor valor: " + str(menor_ruido) + " dB\n")
        arquivo.write("Ocorrencias acima do criterio: " + str(alertas_ruido) + "\n\n")

        arquivo.write("RESUMO DAS OCORRENCIAS\n")
        arquivo.write("Leituras criticas unicas: " + str(leituras_criticas) + "\n")
        arquivo.write("Percentual de leituras criticas: " + format(percentual, ".2f") + "%\n\n")

        arquivo.write("CLASSIFICACAO GERAL\n")
        arquivo.write(classificacao + "\n\n")

        arquivo.write("DETALHAMENTO DAS LEITURAS\n")

        indice = 0

        while indice < len(dados):

            arquivo.write("\nLeitura " + str(indice + 1) + "\n")
            arquivo.write("Temperatura: " + str(dados[indice]["temperatura"]) + " graus Celsius\n")
            arquivo.write("PM2.5: " + str(dados[indice]["pm25"]) + " microgramas por metro cubico\n")
            arquivo.write("Ruido: " + str(dados[indice]["ruido"]) + " dB\n")

            if len(dados[indice]["alertas"]) == 0:
                arquivo.write("Situacao: Dentro dos limites de referencia.\n")

            else:
                arquivo.write("Situacao: Foram identificados alertas.\n")

                for alerta in dados[indice]["alertas"]:
                    arquivo.write("- " + alerta + "\n")

            indice = indice + 1

        arquivo.write("\nOBSERVACOES\n")
        arquivo.write("Os dados utilizados sao simulados e informados pelo usuario.\n")
        arquivo.write("O sistema nao realiza medicoes ambientais reais.\n")
        arquivo.write("A media aritmetica do ruido e uma estatistica descritiva simplificada.\n")
        arquivo.write("Ela nao corresponde a uma avaliacao acustica oficial.\n")
        arquivo.write("A temperatura do ar isolada nao determina a seguranca para exercicios.\n")

        arquivo.write("\n============================================\n")
        arquivo.write("          FIM DO RELATORIO SPORTLIFE\n")
        arquivo.write("============================================\n")

    print("\nRelatorio gerado com sucesso: " + nome_arquivo)


# ------------------------------------------------------------
# FUNCAO PRINCIPAL DO MONITORAMENTO
# ------------------------------------------------------------

def executar_monitoramento():

    # Listas para armazenar os valores de cada parametro.
    temperaturas = []
    particulas = []
    ruidos = []

    # Lista de dicionarios para guardar cada leitura completa.
    dados = []

    # Contadores de ocorrencias por parametro.
    alertas_temp = 0
    alertas_pm25 = 0
    alertas_ruido = 0

    # Conta cada leitura critica apenas uma vez.
    leituras_criticas = 0

    print("\n============================================")
    print("              SISTEMA SPORTLIFE")
    print("       MONITORAMENTO AMBIENTAL")
    print("============================================")

    print("\nAmbiente: Centro esportivo comunitario")
    print("Informe os valores simulados de cada leitura.")

    quantidade = ler_quantidade()

    indice = 0

    while indice < quantidade:

        print("\n--------------------------------------------")
        print("LEITURA " + str(indice + 1))
        print("--------------------------------------------")

        temperatura = ler_numero(
            "Temperatura do ar (graus Celsius): ", -100
        )

        pm25 = ler_numero(
            "PM2.5 - media de 24 horas (microgramas/m3): ", 0
        )

        ruido = ler_numero(
            "Ruido - LAeq,T no periodo diurno (dB): ", 0
        )

        # Armazenamento dos valores nas listas.
        temperaturas.append(temperatura)
        particulas.append(pm25)
        ruidos.append(ruido)

        # Analise dos tres parametros.
        alertas = analisar_ambiente(temperatura, pm25, ruido)

        # Contagem independente de cada parametro.
        if temperatura > TEMP_MAX:
            alertas_temp = alertas_temp + 1

        if pm25 > PM25_MAX:
            alertas_pm25 = alertas_pm25 + 1

        if ruido > RUIDO_MAX:
            alertas_ruido = alertas_ruido + 1

        # A leitura e contada uma unica vez, mesmo que
        # apresente alertas em mais de um parametro.
        if len(alertas) > 0:
            leituras_criticas = leituras_criticas + 1

        # Armazenamento dos dados associados em um dicionario.
        registro = {
            "temperatura": temperatura,
            "pm25": pm25,
            "ruido": ruido,
            "alertas": alertas
        }

        dados.append(registro)

        indice = indice + 1

    # --------------------------------------------------------
    # CALCULO DAS ESTATISTICAS
    # --------------------------------------------------------

    media_temp, maior_temp, menor_temp = calcular_estatisticas(temperaturas)
    media_pm, maior_pm, menor_pm = calcular_estatisticas(particulas)
    media_ruido, maior_ruido, menor_ruido = calcular_estatisticas(ruidos)

    percentual = (leituras_criticas / quantidade) * 100

    print("\n============================================")
    print("          RESULTADO DO MONITORAMENTO")
    print("============================================")

    print("\nTEMPERATURA DO AR")
    print("Media: " + format(media_temp, ".2f") + " graus Celsius")
    print("Maior valor: " + str(maior_temp))
    print("Menor valor: " + str(menor_temp))
    print("Ocorrencias acima do criterio: " + str(alertas_temp))

    print("\nPM2.5")
    print("Media: " + format(media_pm, ".2f") + " microgramas/m3")
    print("Maior valor: " + str(maior_pm))
    print("Menor valor: " + str(menor_pm))
    print("Ocorrencias acima do criterio: " + str(alertas_pm25))

    print("\nRUIDO AMBIENTAL")
    print("Media aritmetica descritiva: " + format(media_ruido, ".2f") + " dB")
    print("Maior valor: " + str(maior_ruido))
    print("Menor valor: " + str(menor_ruido))
    print("Ocorrencias acima do criterio: " + str(alertas_ruido))

    print("\nRESUMO DAS OCORRENCIAS")
    print("Leituras criticas unicas: " + str(leituras_criticas))
    print("Percentual de leituras criticas: " + format(percentual, ".2f") + "%")

    # --------------------------------------------------------
    # CLASSIFICACAO GERAL
    # --------------------------------------------------------

    if percentual > 30:

        classificacao = "Estado geral: condições ambientais de atenção, com frequência de ocorrências acima do critério estabelecido"

    else:

        classificacao = "Estado geral: frequência de ocorrências dentro do critério estabelecido para a simulação"

    print("\nCLASSIFICACAO GERAL")
    print(classificacao)

    # --------------------------------------------------------
    # GERACAO DO RELATORIO
    # --------------------------------------------------------

    gerar_relatorio(
        dados,
        temperaturas,
        particulas,
        ruidos,
        alertas_temp,
        alertas_pm25,
        alertas_ruido,
        leituras_criticas,
        percentual,
        classificacao
    )


# ------------------------------------------------------------
# CONTROLE DE NOVAS SEQUENCIAS
# ------------------------------------------------------------

def iniciar_programa():

    while True:

        executar_monitoramento()

        print("\nDeseja iniciar uma nova sequencia de monitoramento?")
        resposta = input("Digite S para sim ou N para nao: ")

        if resposta == "S" or resposta == "s":

            print("\nIniciando uma nova sequencia...")

        elif resposta == "N" or resposta == "n":

            print("\nSistema SportLife encerrado.")
            break

        else:

            print("\nResposta invalida. O sistema sera encerrado.")
            break


# ------------------------------------------------------------
# INICIO DO PROGRAMA
# ------------------------------------------------------------

iniciar_programa()
