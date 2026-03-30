# Aula 4

## Redes
- Meios físicos + protocolos
- Rede é o subsistema de comunicação de um SD
- Influencia: Tempo de resposta, confiabilidade, escalabilidade
- Hardware: Mídia, roteadores, switches
- Software: Pilha de protocolo, drivers, rotinas de tratamento

## Hetorogeneidade e integração
- O subsistema deve integrar outros SOs (ethernet, ...)

## Desempenho
- O desempenho da rede afeta diretamente como os serviços do SD chegam até o cliente
- Principais parâmetros para determinar o desempenho de uma rede (latência, taxa de transferência)
- Latência: tempo de trânsito do pacote
- Taxa de transferência: Velocidade que dados são transmitidos
- Tempo = latência + (banda/taxa)

## Confiabilidade
- Falhas podem ocorrer por: perda de pacote, estouro de buffer, erro de software
- O sistema não precisa fornecer um serviço tootalmente livre de erros: muitas vezes quem detecta o erro é o usuário. confiabilidade da transm. física é sempre alta

## Segurança
- Firewalls: barreira entre a intranet e a internet
- Controle de acesso
- Criptografia

## Mobilidade
- Dispositivos móveis mudam de localização física continuamente
- Mesmo que a conexão wifi permita que essa reconexão aconteça, o endereço IP não acompanha a mobilidade
- É possível acessar a internet mesmo assim por conta das adaptações realizadas nos próprios protocolos da internet

## Quality of service
- Frequente em redes com transmissão multimídia (serviços de streaming): precisam de latência limitada e banda larga garantida
- Exemplo: MobiliIP: Usa Agente doméstico (AD) para tunelar pacotes até um Agente estrangeiro (AE) onde o host está

## Multicasting
- Comunicação de um pra muitos (mais eficiente que múltiplos envios)
- No contexto de SD, localização de serviços e coordenação de dados replicados

## Confiabilidade e taxonomia de falhas
- Falhas por omissão no subsistema
  - Omissão de envio (falha entre o processo e o buffer de saída)
  - Omissão de canal (mensagem perdida no meio físico: ruído)
  - Omissão de recepção (chega ao buffer de destino mas ele descarta a mensagem)
- Mascaramento de falhas
  - Conversão de falhas arbitrárias em falhas de omissão via checksum
  - Uso de retransmissão para ocultar a omissão (converte perda em latência)
  - Idempotência (operações que podem ser repetidas sem problemas caso a resposta seja perdida)

## Escalabilidade do subsistema
- O subsistema deve evitar gargalos centrais (algoritmos descentralizados)
- Estruturas hieráquicas (DNS) permitem acesso em tempo O(logn)
- Uso de Cache e Replicação para distribuir carga de recursos muito acessados

## Organização de camadas e encapsulamento
- Modularização
  - Facilita o projeto, mas impõe custo de desempenho
  - Sobrecarga de chamadas de sistema e cópias de dados entre camadas
  - A vazão entre processos é sempre menor que a largura de banda bruta da rede
- Encapsulamento e portas
  - Dados de aplicação são envolto por cabeçalhos pra identificar o protocolo
  - Portas UDP/TCP pro SO  entregar a mensagem ao processo correto
- Unidade máxima de transferência (MTU)

## Comutação de pacotes
- Pacotes compartilham enlaces físicos de forma assíncrona
- Store-and-follow
  - Cada roteador deve receber o pacote inteiro e armazena-lo em buffer antes de reencaminhar
  - Permite alocação de buffers no nós e impede que mensagens longas monopolizem o canal por tempo indeterminado

## Roteamento e controle de congestionamento
- Responsabilildade de direcionar pacotes através de roteadores intermediários (hops)
  - Adaptabilidade: Reavaliação da tabela de tempos em tempos
  - Convergência:  tempo para que o sistema de roteamento entre em acordo após uma lteração na topologia
- Algoritmo de roteamento
  - Vetor de distância (cada nó tem uma tabela com destino saída e custo)
- Controle de congestionamento
  - Ocorre quando a carga se aproxima da capacidade máxima
  - Filas crescem até o estouro do buffer, resultando no descarte de pactotes
  - Retransmissões excessivas consomem ainda mais recursos, levando ao colapso do desempenho

## Tipos de redes
- Redes de área local (LAN)
  - Alta largura de banda e baixa latência
  - Dispositivos em uma área geográfica restrita
- Ethernet
  - CSMA/CD (detecção de portadora e detecção de colisão)
  - Inicialmente por barramento de disputa mas evoluiu para comutação
- Ethernet comutada (switches)
  - Switches eliminam a disputa pelo meio ao criar segmentos dedicados para cada host
  - Cada porta do switch oferece banda exclusiva
- Redes sem fio (WLAN, WIFI)
  - Padrão IEEE
  - Regula frequências, modulações e velocidade de dados
- Redes de loga distância (WAN) e inter-redes
  - Interconectam nós em grandes distâncias
  - A internet é o maior exemplo de WAN

## Mascaramento de colisão
- Por que não usar CD (Collision Detection) no WiFi?
  - O sinal transmitido pelo rádio local abafa a percepção de colisão externa
- Solução CSMA/CA (prevenção de colisão) e mecanismo de reserva via mensagens RTS/CTS
  - CSMA/CA "ouve" o canal e, se livre, utiliza um tempo de espera aleatório (backoff) e mensagens RTS/CTS (request to send/clear to send) para garantir que apenas um dispositivo transmita

## Firewalls e segurança de borda
- Filtragem de mensagens no gateway de uma intranet
  - Baseado na origem

## Tunelamento
- Transmissão de pacotes dentro de pacotes (VPNs, MoIP, transição de protocolos)

## Protocolo IP
- Semântica de entrega não confiável ou de "melhor esforço"
- Checksum apenas no cabeçalho para acelerar o roteamento
- IPv6
  - Endereços de 128 bits para suprir o esgotamento do IPv4
  - Anycast: Nova modalidade que entrega o pacote a pelo menos um dos membros de um grupo
  - Suporte nativo para segurança (IPSec) e QoS
  - Processamento em cada nó é reduzido para aumentar a vazão do SD em larga escala
  - Sem checksum de rede: Confia-se na integridade das camadas de enlace e transporte
  - Sem fragmentação em roteadores: O MTU do caminho é determinado antes do envio
  - Campo de 20 bits no cabeçalho que identifica pacotes de um fluxo específico
  - Permite que roteadores apliquem reservas de recursos e tratamento diferenciado de forma eficiente, sem analisar cabeçalhos de transporte (TCP/UDP)

## Protocolos de Rede
- Protocolo UDP (mensagens simples, ex: consultas rápidas, onde dados atrasados não são tão significantes)
- Protocolo TCP (confiável, controle de fluxo e congestionamento, sequenciamento de dados, ...)

## Gerenciamento de fluxos
- Exige largura de banda alta e garantida
- Elementos que chegam após o seu tempo de reprodução são inúteis e descartáveis
- Uso de buffers no destino para suavizar a jitter da rede (variação estática do atraso na entrega de mensagens)

## Redes tolerantes a rompimento
- Caminhos contínuos podem não existir em ambientes voláteis

## Virtualização em nível de rede
- Capacidade de criar múltiplas redes virtuais isoladas sobre a mesma infraestrutura física
- Permite experimentação e isolamento de serviços críticos de tráfego comum

## O papel da rede no SD
- A rede não é transparente
  - Suas limitações de tempo e confiabilidade devem moldar a lógica da aplicação
- O projetista de SD deve equilibrar a abstração do middleware com o entendimento profundo do subsistema de comunicação subjacente

## Resumo
- Redes como subsistema de comunicação
  - Requisitos de rede
  - Tipos de rede
  - Organização de camadas
  - Encapsualmetno
  - Comutação de pacotes
  - roteamento
  - controle de congestionamento
  - mascaramento de colisão
  - ...


