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