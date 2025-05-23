def exibir_menu(): # função para mostrar o menu
    titulo = "MENU"
    opcoes = [" 5 ADM","|", "1 Sobre Nós", "|", "2 Músicas", "|", "3 Playlists", "|","4 Login", "|","0 para sair"]

    # Calcula largura total com base nas opções
    largura_total = 150
    separador = "-" * largura_total

    # Exibe o título centralizado
    print(separador)
    print(titulo.center(largura_total))
    print(separador)

    # Calcula o espaço entre opções
    colunas = len(opcoes)
    espaco_por_coluna = largura_total // colunas

    linha_opcoes = ""
    for opcao in opcoes:
        linha_opcoes += opcao.center(espaco_por_coluna)
    
    print(linha_opcoes)
    print(separador)

def sobre_nos(): # função para exibir rapidamente um sobre nós
    titulo = "Sobre nós"
    largura_total = 120
    separador = "-" * largura_total


    print(separador)
    print(titulo.center(largura_total))
    print(separador)
    print("Somos dois alunos que fizeram um projeto chamado spotifei, que consiste".center(largura_total))
    print("basicamente em recriar algo parecido com o spotify, porém, somente".center(largura_total))
    print("com python.".center(largura_total))

def buscar_musica(): # função para buscar música por nome
    musica_procurar = input("Digite o nome da música que deseja procurar: ")
    with open("musicas.txt", "r") as arquivo_musicas:
        conteudo = arquivo_musicas.readlines()
        

    for linha in conteudo: 
        musica, artista, curtida, descurtida= linha.strip().split(",") 
        if musica_procurar.lower() == musica.lower(): 
            print(f"Nome da música: {musica}, nome do artista: {artista}, quantidade de curtidas: {curtida}, quantidade de descurtidas: {descurtida}")

def curtir_musica(): # função para curtir uma música
    decisao = int(input("Deseja curtir ou descurtir a música? S(1) ou N(2) "))
    if decisao == 1:
        musica_atualizar = input("Digite o nome da música que deseja dar seu feedback: ")
        with open("musicas.txt", "r") as arquivo_musicas:
            conteudo = arquivo_musicas.readlines()

        musica_encontrada = False
        for i, linha in enumerate(conteudo): # pega as músicas do arquivo 
            musica, artista, curtida, descurtida = linha.strip().split(",") # separa as informações por "," e retira os espaços e quebras de linha
            if musica_atualizar.lower() == musica.lower(): # se encontrar a música com o mesmo nome
                musica_encontrada = True
                curtida = int(curtida)
                descurtida = int(descurtida)
                print(f"Música encontrada: {musica} de {artista}. Curtidas: {curtida}, Descurtidas: {descurtida}")
                decisao2 = int(input("Deseja curtir(1) ou descurtir(2) a música? "))
                if decisao2 == 1:
                    curtida += 1
                elif decisao2 == 2:
                    descurtida += 1
                conteudo[i] = f"{musica},{artista},{curtida},{descurtida}\n" # coloca a nova informação dentro do mesmo índice da música selecionada
                break

        if musica_encontrada:
            with open("musicas.txt", "w") as arquivo_musicas: 
                arquivo_musicas.writelines(conteudo) # atualiza as curtidas dentro do .txt
        else:
            print("Música não encontrada.")
    else:
        print("Saindo sem curtir/descurtir.")

def listar_musicas(): # função para listar a músicas
        with open("musicas.txt", "r") as arquivo:
            conteudo = arquivo.readlines()
            print("\n Lista de Músicas ")
            for linha in conteudo: # listagem de músicas incluindo suas curtidas e descurtidas sem organização
                musica, artista, curtidas, descurtidas = linha.strip().split(",")
                print(f"Música: {musica} | Artista: {artista} | Curtidas: {curtidas} | Descurtidas: {descurtidas}")


def musicas(): # função para decidir o que fazer com relação às músicas
    titulo = "Músicas"
    largura_total = 120
    separador = "-" * largura_total

    print("1 buscar música | 2 listar as músicas | 3 adicionar música | 4 curtir ou descurtir música")
    decisao = int(input("Digite o que quer fazer: "))
    if decisao == 1:
        buscar_musica()
    elif decisao == 2:
        listar_musicas()
    elif decisao == 3:
        logar()
    elif decisao == 4:
        curtir_musica()

    print(separador)
    print(titulo.center(largura_total))
    print(separador)
   
def adicionar_musica(): # função para adicionar música
    nome = input("Digite o nome da música: ")
    artista = input("Digite o artista da música: ")
    arquivo_musicas = open("musicas.txt", "a")
    arquivo_musicas.write(f"{nome},{artista},{0},{0}\n") 
    arquivo_musicas.close()
    print("música cadastrada com sucesso!") 


def criar_playlist(): # função para criar playlists
    with open("musicas.txt", "r") as arquivo:
        musicas = arquivo.readlines()

    nome_playlist = input("Digite o nome da nova playlist: ") # pede o nome da playlist
    print("\n Músicas Disponíveis ")
    musicas_escolhidas = [] # abre a lista para adicionar as músicas para posteriormente adicioná-las a playlist
    for i, linha in enumerate(musicas): # exibe em forma de lista com valor de índice + 1 para facilitar a escolha
        musica, artista, _, _ = linha.strip().split(",")
        print(f"{i + 1}. {musica} - {artista}")
        musicas_escolhidas.append(f"{musica} - {artista}")

    escolhas = input("Digite os números das músicas separadas por vírgula (ex: 1,3,4): ") # escolha de múltiplas músicas
    indices = escolhas.split(",")

    playlist = []
    for idx in indices: # para cada escolha - 1, da um append na música para dentro da lista playlist
            num = int(idx.strip()) - 1
            playlist.append(musicas_escolhidas[num])

    # aqui é usado a variável linha_playlist para organizar as informações dentro dela, separa o nome da playlist das músicas com ":" e as músicas por "|"
    linha_playlist = nome_playlist + ":" + "|".join(playlist) + "\n" # o join aqui serve para unir elementos de listas, podendo ser listas diferentes

    with open("playlists.txt", "a") as arquivo_playlists:
        arquivo_playlists.write(linha_playlist)

    print(f"Playlist '{nome_playlist}' criada com sucesso!")

def listar_playlist(): # função para listar a playlist e suas músicas
    with open("playlists.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            print("\n Playlists ")
            for linha in linhas:
                nome, musicas = linha.strip().split(":")
                lista_musicas = musicas.split("|")
                print(f"\n Playlist: {nome}")
                for m in lista_musicas:
                    print(f" {m}")

def editar_nome_playlist(): # função para editar o nome da playlist
    with open("playlists.txt", "r") as f:
        linhas = f.readlines()

    print("Playlists disponíveis:")
    for i, linha in enumerate(linhas):
        nome, _ = linha.strip().split(":")
        print(f"{i + 1}. {nome}") # para mostrar o valor como índice + 1

    escolha = int(input("Digite o número da playlist que deseja renomear: ")) - 1 # -1 para estar dentro do índice.
    if 0 <= escolha < len(linhas): # essa linha garante que o número escolhido esteja dentro dos limites da lista.
        novo_nome = input("Digite o novo nome da playlist: ")
        _, musicas = linhas[escolha].strip().split(":")
        linhas[escolha] = f"{novo_nome}:{musicas}\n" # atualiza a playlist com a nova escolha de nome
        with open("playlists.txt", "w") as playlists:
            playlists.writelines(linhas) # atualiza o .txt com o novo nome da playlist
        print("Nome da playlist atualizado com sucesso!")
    else:
        print("Escolha inválida.")

def excluir_playlist(): # início da função para excluir uma playlist
    with open("playlists.txt", "r") as f:
        linhas = f.readlines()

    print("Playlists disponíveis:")
    for i, linha in enumerate(linhas):
        nome, _ = linha.strip().split(":")
        print(f"{i + 1}. {nome}") # mostra a playlist com um valor que é o índice + 1

    escolha = int(input("Digite o número da playlist que deseja excluir: ")) - 1 # transforma o valor escoliho em índice novamente
    if 0 <= escolha < len(linhas): # verifica se a escolha está entre o primeiro índice e o último
        del linhas[escolha] # deleta a playlist
        with open("playlists.txt", "w") as playlists:
            playlists.writelines(linhas) # atualiza o .txt
        print("Playlist excluída com sucesso!")
    else:
        print("Escolha inválida.")

def adicionar_musica_playlist(): # início da função para adicionar músicas na playlist
    with open("playlists.txt", "r") as f:
        playlists = f.readlines()
    with open("musicas.txt", "r") as f:
        musicas = f.readlines()

    print("Playlists disponíveis:")
    for i, linha in enumerate(playlists): # lista as playlists disponíveis
        nome, _ = linha.strip().split(":")
        print(f"{i + 1}. {nome}")

    escolha = int(input("Digite o número da playlist para adicionar músicas: ")) - 1
    if 0 <= escolha < len(playlists): # utiliza a escolha por índice, mas mostra visualmente como 1,2,3 etc..
        nome, musicas_existentes = playlists[escolha].strip().split(":") # aqui pega o nome da playlist e as músicas dentro dela
        print("\n Músicas Disponíveis ")
        musicas_escolhidas = [] #abre uma lista para adicionar posteriormente na playlist
        for i, linha in enumerate(musicas): # faz a listagem das músicas disponíveis para serem adicionadas nas playlists
            musica, artista, *_ = linha.strip().split(",")
            print(f"{i + 1}. {musica} - {artista}")
            musicas_escolhidas.append(f"{musica} - {artista}")

        escolhas = input("Digite os números das músicas para adicionar (ex: 1,2,5): ")
        indices = escolhas.split(",") # separa as escolhas do usuário por "," para ser manipulado posteriormente

        for idx in indices:
                musica = musicas_escolhidas[int(idx.strip()) - 1] # volta a escolha para o índice da música
                if musica not in musicas_existentes: # caso a música escolhida não esteja dentro da playlist
                    musicas_existentes += f"|{musica}" # adiciona a música na playlist

        playlists[escolha] = f"{nome}:{musicas_existentes}\n" # atualiza a playlist com as escolhas de músicas para serem adicionadas para serem adicionadas ao .txt
        with open("playlists.txt", "w") as playlist:
            playlist.writelines(playlists) # atualiza o .txt com as novas músicas dentro da playlist
        print("Músicas adicionadas com sucesso!")
    else:
        print("Escolha inválida.")

def remover_musica_playlist(): # função para remover música de uma playlist por índice

    with open("playlists.txt", "r") as f:
        playlists = f.readlines()

    print("Playlists disponíveis:") #listagem das playlist existentes
    for i, linha in enumerate(playlists):
        nome, _ = linha.strip().split(":")
        print(f"{i + 1}. {nome}") # é adicionado 1 no índice para facilitar visualmente a escolha

    escolha = int(input("Digite o número da playlist para remover músicas: ")) - 1 # é retirado 1 da escolha para condizer com o índice
    if 0 <= escolha < len(playlists): # se a escolha for maior ou igual a zero e menor que a quantidade máx de playlist, prossegue com o código
        nome, musicas = playlists[escolha].strip().split(":")  # pega a linha da playlist escolhida removendo espaços de linhas e quebras de linhas e dizendo que o espaço que determina o que é o conteúdo da playlist é informado por ":"
        lista_musicas = musicas.split("|") # separa as músicas da playlist pelo |

        print("\n Músicas da Playlist ")
        for i, m in enumerate(lista_musicas):
            print(f"{i + 1}. {m}")

        escolhas = input("Digite os números das músicas para remover (ex: 1,3): ") # escolha múltipla para remoção
        indices = [int(i.strip()) - 1 for i in escolhas.split(",") if i.strip().isdigit()] # pega os ìndices das escolhas acima, verificando se o que foi digitado é realmente número e retirando os espaços entre as informações
        novas_musicas = [m for i, m in enumerate(lista_musicas) if i not in indices] # atualiza as músicas que ficaram na playlist

        playlists[escolha] = f"{nome}:{'|'.join(novas_musicas)}\n" # Essa linha atualiza a playlist escolhida, com as novas informações, para depois salvar de volta no arquivo.
        with open("playlists.txt", "w") as f:
            f.writelines(playlists) # atualiza no .txt as músicas que estão na playlist
        print("Músicas removidas com sucesso!")
    else:
        print("Escolha inválida.")

def adm(): # função para abrir a aba de adm
    logar()

def playlist(): # função para decidir o que fazer com relaçao à playlist
    titulo = "faça sua playlist ou liste as músicas que tem dentro de uma."
    largura_total = 120
    separador = "-" * largura_total

    print(separador)
    print(titulo.center(largura_total))
    print(separador)
    decisao = int(input('"1" para começar a criar sua playlist, "2" para listar as músicas de uma playlist, "3" para alterar nome da playlist, "4" para excluir uma playlist, "5" para adicionar ou remover músicas de uma playlist: '))
    if decisao == 1:
        criar_playlist()
    elif decisao == 2:
        listar_playlist()
    elif decisao == 3:
        editar_nome_playlist()
    elif decisao == 4:
        excluir_playlist()
    elif decisao == 5:
        decisao2 = int(input("Deseja adicionar música em uma playlist (1)? ou remover música de uma playlist (2)?"))
        if decisao2 == 1:
            adicionar_musica_playlist()
        elif decisao2 == 2:
            remover_musica_playlist()

def logar(): # função para logar utilizando apenas informações de usuários retiradas de usuarios.txt, exceto o adm
    nome_procurar = input("Digite o nome cadastrado: ")
    senha_procurar = input("Digite a sua senha: ")
    with open("usuarios.txt", "r") as arquivo_usuarios:
        conteudo = arquivo_usuarios.readlines()
        
    for linha in conteudo: 
        nome, senha, email = linha.strip().split(",")
        if nome_procurar.lower() == nome.lower() and senha_procurar == senha.lower(): 
            print(f"Usuário {nome} logado! email do usuário: {email}")
            break 
        if nome_procurar.lower() == "adm".lower() and senha_procurar == "adm".lower(): # quando o adm loga, as opções abaixo podem ser escolhidas, caso contrário, a pessoa passa pelo login normalmente
            print(f"ADM logado!")
            decisao = int(input("O que deseja fazer como adm? 1 add música | 2 consultar usuarios | 3 top 5 músicas curtidas/descurtidas | 4 total de músicas | 5 total de usuarios: "))
            if decisao == 1:
                adicionar_musica()
            elif decisao == 2:
                consulta_usuario()
            elif decisao == 3:
                top_5()
            elif decisao == 4:
                total_musicas()
            elif decisao == 5:
                total_usuarios() 
        else: 
            print("Usuário não cadastrado") 

def consulta_usuario(): # função para decidir que tipo de consulta o adm vai querer fazer
    print("O que deseja fazer? 1 para buscar usuário por nome, 2 para listar usuários")
    decisao = int(input("Digite para onde quer ir: "))
    if decisao == 1:
        buscar_usuario()
    elif decisao == 2:
        listar_usuarios()

def buscar_usuario(): # função para buscar o usuário por nome
    usuario_procurar = input("Digite o nome do usuário que deseja procurar: ")
    with open("usuarios.txt", "r") as arquivo_usuarios:
        conteudo = arquivo_usuarios.readlines()
        

    for linha in conteudo: 
        nome, senha, email = linha.strip().split(",") 
        if usuario_procurar.lower() == nome.lower(): 
            print(f"Nome do usuário: {nome}, senha do usuário: {senha}, email do usuário: {email}")


def listar_usuarios(): # função para listar todos os usuários
    with open("usuarios.txt", "r") as arquivo:
        conteudo = arquivo.readlines()
        print("\n Lista de Usuários ")
        for linha in conteudo:
            nome, senha, email = linha.strip().split(",")
            print(f"Nome: {nome} | Senha: {senha} | Email: {email}")

def top_5(): # função para escolher qual top deseja ver
    decisao = int(input("Digite 1 para top 5 músicas mais curtidas e 2 para top 5 músicas mais descurtidas: "))
    if decisao == 1:
        top_musicas_curtidas()
    elif decisao == 2:
        top_musicas_descurtidas()

def ordenar_por_curtidas(musica): # função para complementar a função top_musicas_curtidas, retornando as curtidas em número para ser exibido de forma ordenada pelo sorted
    return musica["curtidas"]

def top_musicas_curtidas(): #função para exibir o top 5 músicas 5 curtidas
        with open("musicas.txt", "r") as arquivo:
            musicas = [] # ele cria uma lista para adicionar os elementos
            for linha in arquivo:
                nome, artista, curtidas, descurtidas = linha.strip().split(",")
                musicas.append({    # adiciona um dicionário dentro da lista musicas
                    "nome": nome,
                    "artista": artista,
                    "curtidas": int(curtidas),
                    "descurtidas": int(descurtidas)
                })
                            # e aqui ele ordena as informações recebidas pelo dicionário, pegando o dicionário, passando pela key e ordenando pelo reverse, que seria o reverso de crescente e o ":5", que pega os maiores 5 valores apenas.
        top5 = sorted(musicas, key=ordenar_por_curtidas, reverse=True)[:5] # a key aqui é utilizada para usar escolher um atributo para comparação, que nesse caso, são as curtidas, que vem direto da função ordenar_por_curtidas.
                                                                           # o reverse, serve para fazer a organização(sorted) ao contrário, ou seja, decrescente.

        print("\n Top 5 músicas mais curtidas:")
        for i, j in enumerate(top5, 1):
            print(f"{i}. {j['nome']} - {j['artista']} ({j['curtidas']} curtidas)")

def ordenar_por_descurtidas(musica): # função para complementar a função top_musicas_descurtidas, retornando as descurtidas em número para ser exibido de forma ordenada pelo sorted
    return musica["descurtidas"]

def top_musicas_descurtidas():
        with open("musicas.txt", "r") as arquivo:
            musicas = []
            for linha in arquivo:
                nome, artista, curtidas, descurtidas = linha.strip().split(",")
                musicas.append({
                    "nome": nome,
                    "artista": artista,
                    "curtidas": int(curtidas),
                    "descurtidas": int(descurtidas)
                })

        top5 = sorted(musicas, key=ordenar_por_descurtidas, reverse=True)[:5] # a key aqui é utilizada para usar escolher um atributo para comparação, que nesse caso, são as descurtidas, que vem direto da função ordenar_por_descurtidas.
                                                                              # o reverse, serve para fazer a organização(sorted) ao contrário, ou seja, decrescente.


        print("\n Top 5 músicas mais descurtidas:")
        for i, m in enumerate(top5, 1):
            print(f"{i}. {m['nome']} - {m['artista']} ({m['descurtidas']} descurtidas)")




def total_musicas(): # função para mostrar o total de músicas
        with open("musicas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            quantidade = len(linhas)
            print(f"\n Total de músicas cadastradas: {quantidade}")

def total_usuarios(): #função para mostrar o total de usuários
        with open("usuarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            quantidade = len(linhas)
            print(f"\n Total de usuários cadastrados: {quantidade}")


def cadastrar():                # função para cadastrar um usuário
    nome = input("Digite o nome: ")
    senha = input("Digite a senha: ")
    email = input("Digite o e-mail: ")
    arquivo_contatos = open("usuarios.txt", "a")
    arquivo_contatos.write(f"{nome},{senha},{email}\n") 
    arquivo_contatos.close()
    print("usuário cadastrado com sucesso!") 

def login():    # função para cadastrar ou logar
    titulo = "Faça aqui seu login, para criar playlists ou no caso de ser administrador, para adicionar músicas"
    largura_total = 120
    separador = "-" * largura_total

    print(separador)
    print(titulo.center(largura_total))
    print(separador)
    decisao = input("Digite logar para começar o login ou cadastrar para se cadastrar: ").upper()
    if decisao == "LOGAR":
        logar()
    elif decisao == "CADASTRAR":
        cadastrar()
    

def sair():
    print("fechando o programa...") # função para sair do programa
    exit()




while True: # Loop infinito para demonstrar o menu e pedir pro usuário para prosseguir, caso não queira, é só sair do programa.
        exibir_menu()
        escolha = int(input("Digite para qual menu deseja prosseguir: "))
        if escolha == 1: 
            sobre_nos() 
        elif escolha == 2: 
            musicas()
        elif escolha == 3: 
            playlist() 
        elif escolha == 4:
            login() 
        elif escolha == 0:
            sair() 
        elif escolha == 5:
            adm()
        else:
            print("Opção inválida. Tente novamente.")