### 2. Straless (sem estado)

O servidor **não guarda informações de requisições anteriores**.
Cada requisição PRECISA conter **todas as informações necessárias**.

### 3. Cache

As respostas **PODEM** ser armazenadas para reutilização.

Ex: 
- Você pergunta ao vizinho sobre o transito.
- Ele confere, responde
- Se eu perguntar novamente depois, ele pode reutilizar a resposta

### 4. Interface Uniforme (Coração REST)

- Devem seguir um contrato padronizado.
- Métodos HTTP têm um significado claro
- Respostas são padronizadas (ex: 404(not found), 200(ok), 500 (erro interno de servidor))

Get -> Buscar
Post -> Criar
Put -> Atualizar
Delete -> Apagar

/buscaPedido seria errado pois fica redundante, pois o get já nos informa que será uma busca

/pedidos ok, pois o verbo ja está embutido no método HTTP. 

### 5. Sistemas em Camadas

O cliente **não sabe o que acontece entre ele e o servidor**

Pode haver:
- Load balancer
- Firewall
- Cache

O que importa é que a resposta chegue.

.....

### 6. Código sob Demanda

O servidor PODE enviar código.
Ex: html, css, js.
