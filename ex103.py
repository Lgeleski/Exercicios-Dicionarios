def busca_dados_arquivos():
    dados = {}

    arquivo = open("moedas.csv", mode="r", encoding="utf8")
    try:
        for linha in arquivo:
            partes = linha.split(",")
            if len(partes) == 4:
                codigo = partes[0]
                nome_moeda = partes[2]
                cotacao = float(partes[3])
                dados[codigo] = (nome_moeda, cotacao)
    finally:
        arquivo.close()

    return dados


print("Programa para conversão de moedas")
print()

dados = busca_dados_arquivos()

valor_reais = float(input("Informe o valor em R$: "))
codigo = input("Informe o código da moeda de destino: ").upper()

print()
if codigo in dados:
    nome_moeda = dados[codigo][0]
    cotacao = dados[codigo][1]
    valor_convertido = valor_reais / cotacao

    print(f"Moeda: {nome_moeda}")
    print(f"Valor convertido: {valor_convertido:.2f}")
else:
    print("Moeda não encontrada")