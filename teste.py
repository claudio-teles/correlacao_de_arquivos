from correlacao_de_arquivos import(
	listar_todos_arquivos,
	obter_nome_arquivo,
	remover_hifen_inicio_token,
	remover_nomes_desnecessarios,
	substituir_hifem_por_espaco,
	criar_nos,
	criar_lista_locais_sem_init__,
	criar_arestas,
	converter_nos_em_strings,
	converter_arestas_em_strings
)

local_da_pasta_raiz = 'C:\\Users\\Claudio\\Documents\\Temp'
#local_da_pasta_raiz = 'C:\\Users\\Claudio\\Anaconda3\\Lib'

lista_nomes = []
for local in listar_todos_arquivos(local_da_pasta_raiz):
	lista_nomes.append(obter_nome_arquivo(local))

lista_tokens_sem_hifem_inicio = []
for nome in lista_nomes:
	lista_tokens_sem_hifem_inicio.append(remover_hifen_inicio_token(nome))

lista_de_nomes_adequados = []
for nome in remover_nomes_desnecessarios(lista_tokens_sem_hifem_inicio):
	lista_de_nomes_adequados.append(nome)

nomes_dos_nos_arquivos = []
nomes_dos_nos_arquivos = substituir_hifem_por_espaco(lista_de_nomes_adequados)

locais_sem_init__ = []
locais_sem_init__ = criar_lista_locais_sem_init__(listar_todos_arquivos(local_da_pasta_raiz))

nos ={}
nos = criar_nos(nomes_dos_nos_arquivos)

arestas = {}
arestas = criar_arestas(nos, locais_sem_init__)

string_dos_nos = ''
string_dos_nos = converter_nos_em_strings(nos)

string_das_arestas = ''
string_das_arestas = converter_arestas_em_strings(arestas)


def salvar_csv(_string, path):
	# Transformar a string em bytes
	bytes_dos_para_gravar = _string.encode()
	#bytes_dos_para_gravar = string_das_arestas.encode()

	# Escrever os bytes no arquivo CSV
	with open(path, "wb") as arquivo:
	    arquivo.write(bytes_dos_para_gravar)

	print('Gravação do arquivo .csv finalizada com sucesso!')


salvar_csv(string_dos_nos, "C:\\Users\\Claudio\\Documents\\Microsoft Office\\Exel\\correlacao_de_arquivos_python\\nos_arquivos_base_python.csv")
salvar_csv(string_das_arestas, "C:\\Users\\Claudio\\Documents\\Microsoft Office\\Exel\\correlacao_de_arquivos_python\\arestas_arquivos_base_python.csv")

