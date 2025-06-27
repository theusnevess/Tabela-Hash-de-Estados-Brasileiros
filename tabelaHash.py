class ElementoDaListaSimples: # classe que irá criar os nós
    def __init__(self, sigla, nomeEstado): # no método construtor são passados a sigla e o nome do estado por extenso
        self.sigla = sigla 
        self.nomeEstado = nomeEstado
        self.proximo = None # todos os nós criados apontam para None 

    def __repr__(self):  # método que torna os atríbutos das instâncias em string, para que possam ser printados 
        return  f"{self.sigla}({self.nomeEstado})"

class tabelaHash: 
    def __init__(self): 
        self.tabela = [None] * 10 # ao instânciar a tabelaHash será criado uma lista com 10 posições, e todas elas terão valor None 
        self.estados = [  # lista com todos os estados brasileiros
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins")]


    def funcaoHash(self, siglaEstado): # o método funcaoHash recebe a sigla do estado 
        if siglaEstado == "DF": # caso o estado seja o Distrito Federal, que tem prioridade, será inserido na posição 7 da tabela 
            return 7
        else:
            letra1 = siglaEstado[0] # a sigla do estado inserido é dividida em 2 letras e cada letra terá um valor ASCII
            letra2 = siglaEstado[1]
            posicao = (ord(letra1) + ord(letra2)) % 10 # os valores ASCII de cada letra são somados, e logo depois é dividido pelo módulo de 10
            return posicao # o valor retornado será a posição que o estado será inserido na tabela hash 
        
    def inserir(self, posicao, nodo):
        nodo.proximo = self.tabela[posicao] # o novo nó vai apontar para o que já estiver na posição da tabela
        self.tabela[posicao] = nodo # agora, o novo nó passa a ser o primeiro da lista na posição informada, se tornando o head do seu respectivo índice 
        
    def carregar_estados(self):
        for sigla, nome in self.estados: # o loop percorre todos os elementos da lista de estados, tanto a sigla quanto o nome por extenso 
            nodo = ElementoDaListaSimples(sigla, nome)  # cada índice percorrido da lista é instânciado como um nó
            posicao = self.funcaoHash(sigla) # em seguida cada nó passa pela funcaoHash, que com base nos valores ASCII fará o calculo para determinar a posição do estado na tabela hash
            self.inserir(posicao, nodo) # por fim, o nó é inserido na tabela hash
    
    def inserir_estado_ficticio(self, sigla, nomeEstado):
        nodo = ElementoDaListaSimples(sigla, nomeEstado) # a sigla e o nome do estado fictício serão inseridos nos parâmetros do método, e o nó é instanciado
        posicao = self.funcaoHash(sigla) # o nó passa também pela funcaoHash, para determinar o seu índice na tabela hash 
        self.inserir(posicao, nodo) # é inserido finalmente 

    def imprimir_tabela(self):
        for i in range(len(self.tabela)): # percorre toda a tabela hash e imprime cada índice disponível nela 
            print(f"{i}: ", end="")
            atual = self.tabela[i] # o índice que estiver sendo iterado será o head 
            if atual is None: # caso a tabela esteja vazia será impresso None 
                print("None")
            else:
                nodos = [] # é criado uma lista vazia 
                while atual is not None: # enquanto houver índices na tabela o loop será iterado 
                    nodos.append(f"{atual.sigla}") # cada índice da tebela, que corresponderá a head durante a iteração, será adicionado na lista nodos 
                    atual = atual.proximo # após um índice ser inserido na tabela o head passa a ser o índice subsequente 
                print(" -> ".join(nodos) + " -> None") # as siglas de cada estado são impressas na tabela 


tabela = tabelaHash() # tabela hash instanciada 
print("Antes da inserção:")
tabela.imprimir_tabela() # acionado o método de imprimir a tabela, no entanto ela estará vazia 
print("\nApós a inserção:")
tabela.carregar_estados() # os estados são instanciados como nós e são adicionados a tabela 
tabela.imprimir_tabela() # ao imprimir, agora todos os estados + o DF estarão na tabela 
print()
print("Tabela hash após inserir os 27 estados oficiais e o estado fictício:")
tabela.inserir_estado_ficticio("MN", "Matheus Neves") # o estado fictício é instanciado e adicionado na tabela 
tabela.imprimir_tabela()

 


