# Aula 5

## Comunicação interprocessos (IPC)
- Conjunto de primitivas que permite a processos trocar dados e sincronizar ações
  - SDs = Conjunto de processos executando tarefas coloborativas via mensagens

## Sockets
- Abstração de "ponto de destino" (endpoint) para comunicação
  - Origem: UNIX, mas hoje presente em quase todos SOs
- Identificação
  - Endereço IP (computador)
  - Número da porta (Processo específico)
- Cada computador possui 2**16 portas disponíveis
- Primitivas de sockets em C
  - Implementação manual (baixo nível)
  - Responsabilidade:
    - Criar o socket
    - Associar a um nome/endereço (bind)
    - Controlar o fluxo de dados manualmente
- APIs em linguagens como Java escondem parte deste controle

```md
Primitva socket():
- sd = socket(format, type, protocol)
- Format: AF_INET (internet ipv4)
- Type:
    - SOCK_STREAM
    - SOCK_DGRAM
```

```md
Primitva bind():
- sd = bind(sd, address, length)
    - Associa o socket local a uma porta específica no host
    - Essencial para servidores, que precisam ouvir em portas conhecidas (ex: 80 para HTTP)

> Clientes geralmente usam portas dinâmicas
```

```md
Primitva listen():
- listen(sd, qlength)
    - Apenas para sockets orientados a conexão (TCP)
    - qlength: Define o tamanho da fila de espera para conexões pendentes
    - O socket passa do modo "ativo" para o mode "escuta" (passivo)
```

```md
Primitva accept() (Servidor):
- nsd = accept(sd, address, addrlen)
    - Bloqueia o servidor até que um cliente solicite conexão
    - Retorno crucial: Um novo descritor de socket (nsd) para a comunicação dedicada com aquele cliente
    - O socket original (sd) continua ouvindo novos clientes
```

```md
Primitva connect() (Cliente):
- connect(sd, server_address, length)
- O cliente solicita uma conexão ativa com o servidor
    - No TCP: inicia o handshake de 3 vias
    - No UDP: Apenas define o endereço padrão para envios futuros (sem conexão real)
```

```md
Primitva send() e recv():
- send(sd, msg, length, flags)
- recv(sd, buffer, length, flags)
- Responsáveis pela transferência eferiva de bytes
    - No TCP: os dados são vistos como um fluxo contínuo (stream) sem limites de mensagens
```

```md
Encerramento da comunicação:
- close(sd): destrói o socket e libera a porta
- shutdown(sd, mode): fecha a conexão em apenas um sentido (leitura ou escrita)
> Tentativas de ler um socket fechado resultam em EOFException (Java) ou retorno 0 (C)
```
## Sockets Datagrama (UDP):
- Sem garantia de entrega ou ordenação
- Sem fase de estabelecimento de conexão (mais rápido)
- Uso de sendto() e recvfrom() para especificar o destino em cada pacote
- Ideal para: Streaming, jogos online e consultas rápidas (DNS)

## Sockets de Fluxo (TCP):
- Orientado a conexão e confiável
- Garante entrega na ordem correta e sem duplicatas
- Controle de fluxo
  - Ajusta a velocidade entre emissor e receptor
- Sobrecarga
  - Mensagens extras de controle e maior latência

## Passagem de mensagens
- Abstração acima dos sockets
- Oculta a complexidade de portas e endereços do programador
- Operações centrais: send e receive
- Pode ser suportada por bibliotecas especializadas (ex: MPI)

## Sincronismo na comunicação
- Síncrona
  - Emissor bloqueia até que o receptor realize o receive
- Assíncrona
  - Emissor prossegue imediatamente após a mensagem para o buffer local
- Recepção bloqueante
  - Mais comum; simplifica a sincronização da thread

## Problema da heterogeneidade
- Dados no programa
  - Estruturas complexas (objetos, arrays, listas)
- Dados na rede
  - Seuqência pura de bytes
- Diferenças de arquitetura
  - Representação de inteiros e ponto flutuante
  - codificação de caracteres (ASCII vs Unicode)

## Ordem de bytes (Endianness)
- Big-endian
  - Byte mais significativo primeiro (ex: redes IP)
- Little-endian
  - Byte menos significativo primeiro (ex: intel x86)
> Atenção: os bits dentro de um byte não mudam de ordem, apenas os bytes dentro de uma palavra

## Marshalling
- Processo de organizar itens de dados em um formato plano de bytes pronto pra transmissão
  - Unmarshalling: Processo inverso de reconstrução dos dados no destino
  - Representação externa de dados (Padrão comum acordado entre as partes)
- Estratégias:
  - CORBA CDR (Common data representation):
    - Representação binária eficiente
    - Tipos definidos via IDL (interface definition language)
    - Não inclui informações de tipo na mensagem (assume que o receptor conhece a estrutura)
  - Serialização Java:
    - Achatamento (flattening) de objetos para forma serial
    - Inclui informações completas sobre os tipos e classes
    - Usa reflexão para descobrir a estrutura do objeto em tempo de execução
    - Variáveis *transient* não são serializadas (ex: arquivos locais)
  - XML e JSON:
    - XML: (entensible markup language)
      - Formato textual e autodescritivo
      - Muito flexível, mas com alta sobrecarga de tamanho
    - JSON / Google protocol buffers: (javascript object notation)
      - Alternativas modernas mais leves para serialização de dados estruturados

## MPI
- Message passing interface: padrão para programação paralela leve e eficiente
  - Foco: computação de alto desempenho (HPC) e clusters
  - Portabilidade e desempenho máximo
  - Disponível para C, C++, Fortran, Java e Python
  - SPMD (single program multiple data):
    - Múltiplas instâncias do mesmo programa executam em paralelo
    - Cada instância processa um conjunto de dados diferente
    - O paralelismo no MPI é tipicamente restrito a este modelo
- Escopo do MPI
  - As funções devem estar entre:
    - MPI_Init(&argc, &argv)
      - Inicia o ambiente
    - MPI_Finalize()
      - Encerra o escopo
    - MPI_COMM_WORLD
      - Variável global que identifica todos os processos do grupo
- Controle: rank e size
  - MPI_Comm_size(comm, &size)
    - retorna o número total de processos disparados
  - MPI_Comm_rank(comm, &size)
    - Retorna a id do processo atual
      - Usamos o rank para decidir qual parte do trabalho cada processo fará
- Comunicação ponto a ponto
  - MPI_Send(msg, length, type, dest, tag, comm)
  - MPI_Recv(msg, length, type, src, tag, comm, status)
    - Tipos MPI: MPI_INT, MPI_FLOAT, MPI_DOUBLE, ...
      - Gerenciam a heterogeneidade internamente
- Broadcast
  - MPI_Bcast(msg, count, type, root, comm)
    - O processo *root* envia a mesma mensagem para todos os outros processos do grupo
      - Muito mais eficiente que múltiplos envios individuais
      - Deve ser chamado por todos os membros simultaneamente
- Coletivas: Scatter e Gather
- MPI_Scatter(...)
  - Divide uma array em partes e envia um pedaço diferente para cada processo
- MPI_Gather(...)
  - Recolhe pedaços de todos os processos e os une em uma única array no mestre
- Operações de redução
  - MPI_Reduce(operand, result, count, type, op, root, comm)
    - Combina dados de todos os processos usando uma operação aritmética/lógica (operadores comuns são: MPI_SUM, MPI_MAX, MPI_PROD)






