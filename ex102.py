pessoas = []

for i in range(10):
    print(f"Pessoa {i + 1}")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    pessoa = {"nome": nome, "idade": idade}
    pessoas.append(pessoa)

menores = []
maiores = []

for pessoa in pessoas:
    if pessoa["idade"] < 18:
        menores.append(pessoa)
    else:
        maiores.append(pessoa)

print("PESSOAS COM MENOS DE 18 ANOS ")
for pessoa in menores:
    print(f"Nome: {pessoa['nome']} - Idade: {pessoa['idade']} anos")

print("PESSOAS COM 18 ANOS OU MAIS")
for pessoa in maiores:
    print(f"Nome: {pessoa['nome']} - Idade: {pessoa['idade']} anos")
