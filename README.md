# 🗺️ Tabela Hash com Encadeamento para Estados Brasileiros

Este projeto em Python simula uma **tabela hash com endereçamento em cadeia (listas encadeadas)** para armazenar informações sobre os **27 estados brasileiros**. Também permite a adição de um **estado fictício** e a visualização da estrutura da tabela.

---

## 📚 Descrição

A estrutura central do código é baseada em:

- **Hash Table** com **10 posições fixas**
- Utilização de **listas encadeadas** (via objetos com ponteiros `proximo`)
- Função hash que calcula a posição com base no **valor ASCII das letras da sigla**
- Tratamento especial para o **Distrito Federal (DF)**, que é sempre inserido na posição 7
- Impressão visual do conteúdo da tabela hash, mostrando a cadeia de colisões

---

## 🧩 Estrutura do Código

### 📦 Classes

#### `ElementoDaListaSimples`

Define os nós da lista encadeada que armazenam:
- `sigla`: Sigla do estado (ex: "SP")
- `nomeEstado`: Nome completo (ex: "São Paulo")
- `proximo`: Referência para o próximo nó na lista

#### `tabelaHash`

Responsável por:
- Armazenar os dados em uma lista de 10 posições
- Definir a função de hashing
- Inserir novos estados (oficiais ou fictícios)
- Imprimir a tabela formatada

---

## ⚙️ Funcionalidades

- ✅ Criação e impressão de tabela hash vazia
- ✅ Carga automática dos 27 estados brasileiros
- ✅ Inserção de estado fictício
- ✅ Impressão com representação encadeada (ex: `SC -> RN -> MS -> None`)

---

## 🧪 Exemplo de Execução

```bash
Antes da inserção:
0: None
1: None
...
9: None

Após a inserção:
0: SC -> RN -> MS -> GO -> None
1: RO -> MT -> BA -> AL -> None
...
9: PE -> None

Tabela hash após inserir os 27 estados oficiais e o estado fictício:
...
3: TO -> SP -> PI -> MN -> None
