import os

def listar_todos_arquivos(pasta_raiz):
	print('listar_todos_arquivos')
	contador = 0
	quantidade_arquivos = 0
	locais_dos_arquivos = []
	for diretorio_atual, subdiretorios, arquivos in os.walk(pasta_raiz):
		for arquivo in arquivos:
			if arquivo.endswith('.py'):
				local_do_arquivo = os.path.join(diretorio_atual, arquivo)
				if 'site-packages' not in local_do_arquivo:
					locais_dos_arquivos.append(local_do_arquivo)
					contador += 1
	quantidade_arquivos = len(locais_dos_arquivos)
	print(local_do_arquivo)
	return locais_dos_arquivos

def obter_nome_arquivo(local):
	nome_arquivo = ''
	nome_arquivo_com_extensao = os.path.basename(local)
	nome_arquivo_sem_extensao, extensao = os.path.splitext(nome_arquivo_com_extensao)
	nome_arquivo = nome_arquivo_sem_extensao
	print('obter_nome_arquivo - local = '+local)
	return nome_arquivo

def remover_hifen_inicio_token(token):
	if token.startswith('_'):
		print('remover_hifen_inicio_token = '+token[1:])
		return token[1:]
	else:
		print('remover_hifen_inicio_token = '+token)
		return token

def remover_nomes_desnecessarios(nomes):
	print('remover_nomes_desnecessarios')
	return [nomes_adequados for nomes_adequados in nomes if nomes_adequados != '_init__']

def substituir_hifem_por_espaco(lista_nomes_hifen_interno):
	print('substituir_hifem_por_espaco')
	return [nome.replace('_', ' ') for nome in lista_nomes_hifen_interno]

def criar_nos(lista_nomes_arquivos):
	print('criar_nos')
	nos = {}
	for i in range(len(lista_nomes_arquivos)):
		nos[i+1] = lista_nomes_arquivos[i]
	return nos

def criar_lista_locais_sem_init__(locais_dos_arquivos):
	print('criar_lista_locais_sem_init__')
	lista_locais_sem_init__ = []
	for local in locais_dos_arquivos:
		if '_init__' not in local:
			lista_locais_sem_init__.append(local)
	return lista_locais_sem_init__

def criar_arestas(nos, locais_dos_arquivos):
	print('criar_arestas')
	arestas = {}
	for source, no in nos.items():
		for target, local in enumerate(locais_dos_arquivos, start=1):
			if tem_string_no_arquivo(no, local):
				arestas[source] = target
	return arestas

def tem_string_no_arquivo(palavra, path_arquivo):
    with open(path_arquivo, 'r', encoding='iso-8859-1') as arquivo:
        conteudo = arquivo.read()
        if palavra in conteudo:
            return True
        else:
            return False
    print('tem_string_no_arquivo')

def converter_nos_em_strings(nos):
	print('tem_string_no_arquivo')
	string_dos_nos = 'Id;Label\r\n'
	for i, no in nos.items():
		string_dos_nos += (str(i)+';'+no+"\r\n")
	return string_dos_nos

def converter_arestas_em_strings(arestas):
	print('converter_arestas_em_strings')
	string_das_arestas = 'Source;'+'Target'+';'+'Type'+'\r\n'
	for i, aresta in arestas.items():
		string_das_arestas += (str(i)+';'+str(aresta)+';'+'Directed'+'\r\n')
	return string_das_arestas

#print('Arquivo salvo com sucesso!') , quoting=csv.QUOTE_NONE
