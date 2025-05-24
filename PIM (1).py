import json
import os
import matplotlib.pyplot as plt
import sys

arquivo_json = 'usuarios.json'

#Funcão para carregar dados
def carregar_dados():
    if os.path.exists(arquivo_json):
        with open(arquivo_json, "r", encoding="utf-8") as f:
            return json.load(f)
    return []
    

#Funcação para salvar dados
def salvar_dados(usuarios):
    with open(arquivo_json, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)


#funcão para cadastro de usuarios
def cadastrar_usuarios():

    arquivo_json = 'usuarios.json'

    # Tenta carregar os usuários já cadastrados
    if os.path.exists(arquivo_json):
        try:
            with open(arquivo_json, 'r', encoding='utf-8') as f:
                usuarios = json.load(f)
                # Se o arquivo for um dicionário, converte para lista
                if isinstance(usuarios, dict):
                    usuarios = [usuarios]
        except (json.JSONDecodeError, FileNotFoundError):
            usuarios = []
    else:
        usuarios = []   

    # Coleta os dados do novo usuário
    novo_usuario = {
        "nome": input("Digite o nome: "),
        "idade": int(input("Digite a idade: ")),
        "email": input("Digite o e-mail: "),
        "acessos": 0
    }

    # Adiciona o novo usuário à lista
    usuarios.append(novo_usuario)

    # Salva a lista atualizada no arquivo JSON
    with open(arquivo_json, 'w', encoding='utf-8') as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)

    print("Cadastro salvo com sucesso!")
    continuar_ou_sair()

#Função para mostrar os usuarios cadastrados
def listagem_de_usuarios(usuarios):
    os.system("cls")
    if not usuarios:
        print("Não existem usuários cadastrados")
    
    else:
        with open(arquivo_json, 'r', encoding='utf-8') as lista:
            usuarios = json.load(lista)

        for i, u in enumerate(usuarios, 1):
            print(f"{i}. {u['nome']} - {u['idade']} anos - {u['email']}")
    
    
    

#Registrar Acesso de Usuarios
def registrar_acesso(usuarios):
    os.system("cls")
    listagem_de_usuarios(usuarios)
    if not usuarios:
        return
    try:
        i = int(input("Digite o número do usuário para registrar acesso e iniciar aula: ")) - 1
        usuarios[i]["acessos"] += 1
        salvar_dados(usuarios)
        print(f"Acesso registrado para {usuarios[i]['nome']}.\n")
        modulo_educativo()
    except:
        print("Opção inválida.")
        
#Módulo para as aulas
def modulo_educativo():
    os.system("cls")
    print(f"\nSeja Bem-Vindo! Vamos aprender algo novo.")
    while True:
        print("\n--- Módulo Educativo ---")
        print("1. Programação Básica")
        print("2. Segurança Digital")
        print("3. Cidadania Digital")
        print("4. Voltar")
        opcao = input("Escolha o tema: ")

        if opcao == "1":
            os.system("cls")
            aula_programacao()
        elif opcao == "2":
            os.system("cls")
            aula_seguranca()
        elif opcao == "3":
            os.system("cls")
            aula_cidadania()
        elif opcao == "4":
            os.system("cls")
            break
        else:
            print("Opção inválida.")

#=======================================
# AULAS E QUESTÕES
#=======================================


def aula_programacao():
    print("\n--- Aula: Programação Básica em Python ---")
    print("1. Variável é um espaço da memória onde você armazena um valor (ex: nome = 'Ana')")
    print("2. if é usado para decisões (ex: if idade >= 18: print('maior de idade'))")
    print("3. while é usado para repetições (ex: while True: faça algo)")
    input("Pressione ENTER para fazer o quiz.\n")

    acertos = 0
    r1 = input("1) Qual comando usamos para decisão? (a) while (b) if (c) print: ").lower()
    if r1 == "b": acertos += 1
    r2 = input("2) Uma variável armazena? (a) repetição (b) função (c) valor: ").lower()
    if r2 == "c": acertos += 1

    os.system("cls")

    print(f"Você acertou {acertos}/2.\n")



def aula_seguranca():
    print("\n--- Aula: Segurança Digital ---")
    print("1. Senhas fortes têm letras, números e símbolos.")
    print("2. Phishing são golpes por e-mail que tentam roubar seus dados.")
    print("3. Backup é salvar seus dados em outro lugar, para não perder.")
    input("Pressione ENTER para fazer o quiz.\n")

    acertos = 0
    r1 = input("1) Qual é uma boa prática? (a) usar '1234' (b) senhas fortes (c) compartilhar senha: ").lower()
    if r1 == "b": acertos += 1
    r2 = input("2) O que é phishing? (a) Atualização (b) Vírus (c) Golpe por e-mail: ").lower()
    if r2 == "c": acertos += 1

    print(f"Você acertou {acertos}/2.\n")

def aula_cidadania():
    print("\n--- Aula: Cidadania Digital ---")
    print("1. É importante respeitar os outros também no mundo virtual.")
    print("2. Ética digital inclui não espalhar fake news e não praticar bullying online.")
    input("Pressione ENTER para fazer o quiz.\n")

    acertos = 0
    r1 = input("1) O que é cidadania digital? (a) comprar online (b) votar (c) agir com respeito online: ").lower()
    if r1 == "c": acertos += 1
    r2 = input("2) É ético espalhar fake news? (a) sim (b) não: ").lower()
    if r2 == "b": acertos += 1

    print(f"Você acertou {acertos}/2.\n")

#======================================


# Relatório
def relatorio(usuarios):
    os.system("cls")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    idades = [int(u["idade"]) for u in usuarios]
    acessos = [u["acessos"] for u in usuarios]

    media_idade = sum(idades) / len(idades)
    media_acessos = sum(acessos) / len(acessos)

    print(f"\n--- Relatório ---")
    print(f"Total de usuários: {len(usuarios)}")
    print(f"Média de idade: {media_idade:.2f}")
    print(f"Média de acessos: {media_acessos:.2f}")

    if media_idade < 18:
        faixa = "Adolescente"
    elif media_idade <= 25:
        faixa = "Jovem-adulto"
    elif media_idade <= 40:
        faixa = "Adulto"
    else:
        faixa = "Maduro/Idoso"

    print(f"Faixa etária predominante: {faixa}")
    
    continuar_ou_sair()


# GERAR GRÁFICOS
def gerar_graficos(usuarios):
    if not usuarios:
        print("Não exitem usuarios cadastrados")
    else:
        # Gráfico de quem mais acessou com a idade
        ordenados = sorted(usuarios, key=lambda u: u["acessos"], reverse=True)

        nomes_idades = [f"{u['nome']} ({u['idade']})" for u in ordenados]
        acessos = [u["acessos"] for u in ordenados]

        plt.figure(figsize=(10,6), facecolor='white')
        plt.bar(nomes_idades, acessos, color='dimgray')

        plt.title("Usuários que mais acessaram e suas Idades", color='black')
        plt.xlabel("Usuário (Idade)", color='black')
        plt.ylabel("Acessos", color='black')
        plt.xticks(rotation=45, color='black')
        plt.yticks(color='black')

        plt.tight_layout()
        plt.savefig("grafico_mais_acessaram_idade.png")
        plt.show()

        print("Gráfico para análise de acessos salvo como: 'grafico_mais_acessaram_idade.png'.")

        # Gráfico de Pizza: Distribuição por Faixa Etária
        menor_20 = sum(1 for u in usuarios if u["idade"] < 20)
        maior_igual_20 = len(usuarios) - menor_20

        labels = ['Menores de 20', '20 ou mais']
        sizes = [menor_20, maior_igual_20]

        colors = ['lightblue', 'lightcoral']

        plt.figure(figsize=(8,8), facecolor='white')
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)

        plt.title("Distribuição por Faixa Etária", color='black')
        plt.tight_layout()
        plt.savefig("grafico_faixa_etaria.png")
        plt.show()

        print("Gráfico de faixa etária salvo como: 'grafico_faixa_etaria.png'.")

#Função para o usuario voltar para o menu principal ou sair da aplicação
def continuar_ou_sair():
    continuar = input("Deseja voltar ao inicio? Digite 'S'. Ou digite 'N' para sair.")


    if continuar == "s":
        os.system("cls")
        menu()


    elif continuar == "n":
        print("Saindo...")
        sys.exit()
        

    else:
        print("Digite um valor válido.")
        continuar_ou_sair()


#Menu principal do sistema
def menu():
    usuarios = carregar_dados()

    while True:
        print("\n--------MENU---------")
        print("1. Crie um novo Cadastro\n2. Lista de usuários\n3. Registrar acesso e fazer aula\n4. Análise escrita\n5. Análise gráfica\n6. Sair")

        opcao = input("Escolha uma das opções: ")

        if opcao == "1":
            os.system("cls")
            cadastrar_usuarios()
    
        elif opcao == "2":
            os.system("cls")
            listagem_de_usuarios(usuarios)
        
        elif opcao == "3":
            os.system("cls")
            registrar_acesso(usuarios)

        elif opcao == "4":
            os.system("cls")
            relatorio(usuarios)

        elif opcao == "5":
            os.system("cls")
            gerar_graficos(usuarios)

        elif opcao == "6":
            print("SAINDO...")
            sys.exit()

        else:
            print("Opção invalida.")

#chamada do menu principal (inicio do programa)
menu()
