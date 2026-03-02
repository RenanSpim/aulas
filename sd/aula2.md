# Aula 2

## Introdução
- Sistema distribuído é um sistema onde os componentes de hardware e software estão localizados em computadores interligados em rede, se comunicando e coordenando suas ações apenas através de mensagens entre si
- Características:
  - Concorrência
  - Coordenação
  - Falta de um relógio global
  - Falhas independentes
  - **Compartilhamento de recursos**
  - Transparência

## Tendências em SD
- Interligação em rede pervasiva/ubíqua (onipresência de tecnologia no mundo, smartwatch, indústria 4.0)
  - Estruturas de conexão invisíveis que integram tecnologia ao cotidiano
- Computação móvel e miniaturização de dispositivos
  - Execução de tarefas enquanto o usuário se desloca
- Sistemas multimídia, tem a capacidade de suportar diversos tipos de mídia de maneira integrada e exuta as mesmas tarefas em todas as mídias
  - Mensagens de texto, áudio, vídeo, fotos ...
  - Armazenar, localizar, transmitir, suporte à apresentação, compartilhar ...
- Serviço público, análogo a serviços como água e energia, que estão sempre disponíveis e possuem fornecedores apropriados, não pertencendo ao usuário final
  - Armazenamento em nuvem (g drive, one drive, dropbox, icloud)
  - Computação em nuvem (aws, azure, g cloud)
  - Serviços de software (SaaS)
    - google workspace, office 365, adobe creative cloud, salesforce, canva, netflix
  - Pagos conforme utilização
- Compartilhamento de recursos
  - É tão comum o compartilhamento de recursos que não paramos pra pensar na estrutura de hardware por trás desse tipo de serviço
    - Pensar em qual serviço de armazenamento está em um arquivo, não em qual disco rígido ou servidor
  - Isso se deve tanto a práticas de engenharia de software quanto à própria característica dos sistemas distribuídos
    - Num sistema distribuído, os recursos são fisicamente encapsulados dentro dos computadores e só podem ser acessados a partir de outros computadores por intermédio de mecanismos de comunicação
  - **Servidor**, é um processo em um computador interligado em rede que aceita pedidos de outros processos em outros computadores para efetuar um serviço
    - Cliente-servidor

## Desafios
- Heterogeneidade, diferenças entre máquinas e programas precisam ser mascaradas por interfaces e protocolos
  - Middlewares e máquinas virtuais
- Sistemas abertos, para garantir a interoperabilidade e consistência entre componentes apenas com base em padrões publicados
- Segurança, para garantir informações sigilosas sejam transmitidas de maneira segura
  - Envolve não só a ocultação do conteúdo como saber a identidade de quem enviou ou quem receberá a informação
  - Denial of service, segurança de código móvel
- Escalabilidade, um sistema é dito escalável se permanece eficiente quando há aumento de usuários ou recursos
  - Controle de custo dos recursos físicos
  - Controle de perda de desempenho
  - Gargalos de desempenho
  - Esgotamento de recursos de software
- Tratamento de falhas, em sistemas distribuídos, falhas são parciais
  - Detecção, mascaramento/ocultamento, tolerância, recuperação, redundância
- Concorrência, diferentes clientes podem tentar acessar um recurso ao mesmo tempo
  - As operações a serem realizadas precisam ser sincronizadas de modo que os dados permaneçam consistentes
- Transparência, o usuário precisa sempre achar que está no mesmo servidor, não deve parecer que está disputando recursos com outros usuários
  - O ANSA reference manual e o RM-ODP da ISO definem oito formas de transparência
    - Acesso, localização, concorrência, replicação, falhas, mobilidade, desempenho, escalabilidade
- Qualidade de serviço, questões como confiabilidade, segurança e desempenho afetam a qualidade do serviço
  - Você começa a ficar irritado e questionar por que paga tão caro na assinatura quando um serviço de *streaming* demora pra carregar ou diminui a resolução
- Modelos fornecem uma descrição abstrata e simplificada de um aspecto relevante do projeto de um SD
  - **Modelos físicos**
  - Modelos de arquitetura (próxima aula)
  - Modelos de fundamentais (próxima aula)

## Modelos físicos
- Representação dos elementos de hardware de um SD de maneira a abstrair os detalhes específicos do computador e das tecnologias de rede empregadas
- **Modelo físico básico**: Componentes de hardware e software localizados em computadores interligados em rede que se comunicam e coordenam apenas por mensagens

## Outros tipos

### Sistemas distribuídos primitivos (1970-1990)
- Surge em resposta ao surgimento de redes locais (ethernet)
- De 10 a 100 nós, conexão limitada
- Serviços suportados: Impressoras locais, servidores de arquivos compartilhados, emails, transferência de arquivos pela internet
- Homogêneos
- Pouca preocupação com o fato de serem abertos
- Qualidade de serviço não era exatamente uma preocupação
- Escalabilidade limitada

### Sistemas distribuídos adaptados para a internet (1990)
- Sistemas de maior escala em resposta  ao crescimento e popularização da internet
  - Mecanismo de busca do google surge em 1996
- Consistem de um modelo físico com um conjunto de nós extensível interconectados por uma rede de redes (internet)
  - Exploravam a infraestrutura da internet para desenvolver SDs globais com um grande número de nós (sistemas que forneciam certos serviços passaram a ser distribuídos para além de suas organiszações)
- Heterogeneidade significativa (diferentes arquiteturas de computadores, SOs, linguagens de programação)
- Maior ênfase em padrões abertos e middlewares (serviços web)
- Qualidade de serviço passou a ser relevante

### Sistemas distribuídos contemporâneos (hoje)
- Sistemas que fogem do padrão dos anteriores (estáticos, separados e autônomos em termos de estrutura física)
- Computação móvel levou a nós que podem mudar de local, exigindo mais recursos
- Surgimento da computação ubíqua levou à mudanças de alguns nós para arquiteturas onde os computadores fazem parte de outros objetos
- Computação em nuvem e *clusters* levaram ao surgimento de conjuntos de nós que juntos fornecem um determinado serviço
  - Ao invés de um único nó autônomo ser responsável por um serviço
- Alta heterogeneidade
- Utilização de estrutura em grid
- Sistemas de grande escala

### Sistemas distrbuídos de sistemas
- Existe a discussão sobre uma quarta geração de modelos (Sistemas distrbuídos de sistemas)
  - Complexidade física dos sistemas distribuídos modernos aumentou consideravelmente
  - Um sistema de sistemas pode ser definido como um sistema complexo composto por uma série de subsistemas os quais são também sistemas que se reúnem para executar uma ou mais tarefas
- Exemplo: Gerenciamento ambiental para previsão de enchentes
  - Redes de sensores para os mais diversos fins acopladas a sistemas capazes de prever a probabilidade de enchentes através de simulações em *clusters*


## Resumo
- O que são SDss
- Características
- Exemplos
- Tendências
- Desafios 
- Modelos