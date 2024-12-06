PROJETO FINAL DE PADRÕES DE ARQUITETURA DE SOFTWARE 2024/2 - INF/UFG
---
### Seja bem-vindo à página do nosso projeto!

# 1. Apresentação do Projeto:
Nosso projeto consiste em um software de detecção por imagem inteligente. Nossa proposta é construir um sistema capaz de, através do uso de inteligência artificial, detectar microexpressões faciais, e por consequência, identificar emoções e sentimentos.
Esse sistema será usado para analisar imagens de câmeras em locais públicos e privados, a fim de identificar mulheres em situações de perigo.
Uma vez identificada uma situação de perigo/risco, são disparadas mensagens de alerta para canais exclusivos e prioritários com a polícia.

### Equipe: 
  - Augusto Falcão
  - Marcus Mitra
  - Giovanna Lyssa

## 1.1 Escopo:
O Brasil enfrenta um desafio urgente: o combate à violência contra a mulher. A cada 10 minutos, uma mulher sofre violência no país. O feminicídio, crime de ódio que mata mulheres por sua condição de gênero, é uma realidade assustadora.

  * Em 2023, o Brasil registrou o maior número de feminicídios desde a tipificação do crime em 2015, com 1.467 mulheres assassinadas por razões de gênero, um aumento de 0,8% em relação a 2022.
  * A cada 24 horas, pelo menos oito mulheres são vítimas de violência doméstica no Brasil.
  * Em 2023, foram registradas 3.181 mulheres vítimas de violência doméstica nos estados monitorados pela Rede de Observatórios da Segurança, um aumento de 22,04% em relação ao ano anterior.
  * 3 em cada 10 brasileiras já sofreram  algum tipo de violência doméstica.
  * 68% das brasileiras têm uma amiga, familiar ou conhecida que já sofreu violência doméstica. A violência psicológica é a mais recorrente (89%), seguida pela moral (77%), física (76%), patrimonial (34%) e sexual (25%).

Segundo uma pesquisa do DataSenado, apenas 36% das brasileiras acreditam na eficácia da Lei Maria da Penha, mas a tecnologia pode ser uma aliada importante nesse combate.

## 1.2 Solução:
  * Nosso sistema se propõe a utilizar câmeras de vigilância pública e de monitoramento pertencentes às forças policiais.
  * Se utilizando dessas câmeras de vigilância, nosso sistema terá uma IA treinada, que deve identificar mulheres em situação de risco ou de perigo em locais públicos.
  * Além de detectar situações de risco e de perigo, nossa IA deverá ser capaz de perceber microexpressões de medo, a fim de saber se uma mulher está se sentindo em perigo, mesmo não estando em um aparente cenário de risco.
  * Assim que uma situação é classificada como uma situação de risco, as forças policiais são acionadas de imediato através de canais exclusivos, a fim de reduzir o tempo de ação e aumentar a eficácia dos esforços policiais.

# 2. Histórias de Usuário:

Nosso projeto consiste em um software de detecção por imagem com inteligência artificial para identificar microexpressões faciais, com o objetivo de detectar mulheres em situações de perigo e acionar as forças policiais. Abaixo estão as histórias de usuário que descrevem as principais funcionalidades do sistema.

**Usuários:**
- **Policial:** Agente responsável por receber alertas, visualizar imagens e tomar as medidas necessárias para garantir a segurança da vítima.
- **Administradores do Sistema:** Responsáveis por configurar o sistema, gerenciar usuários, monitorar o desempenho e garantir a privacidade dos dados.




### 2.1.1 Detecção de Cenários de Risco
#### US01:
- **Como** policial
- **Quero** que o sistema identifique automaticamente cenários de risco, como agressões físicas (empurrões, socos, chutes), assédio sexual (toques inapropriados, exposição indevida), tentativas de sequestro e perseguição
- **Para que** eu possa ser alertado e agir rapidamente para proteger a vítima.

#### US02:
- **Como** policial
- **Quero** que o sistema analise o contexto da cena, considerando o ambiente (local isolado, presença de armas), a linguagem corporal do agressor (postura ameaçadora, expressões faciais agressivas) e a presença de outras pessoas (possíveis testemunhas ou cúmplices)
- **Para que** a avaliação do risco seja mais precisa e completa.


### 2.1.2 Detecção de Microexpressões
#### US03:
- **Como** policial
- **Quero** que o sistema reconheça microexpressões faciais de medo, ansiedade e pânico em mulheres, mesmo que elas estejam tentando disfarçar ou em situações onde não haja um risco aparente
- **Para que** eu possa identificar potenciais vítimas e oferecer assistência.

#### US04:
- **Como** policial
- **Quero** que o sistema diferencie microexpressões genuínas de expressões que podem ser causadas por outros fatores, como surpresa, raiva ou tristeza
- **Para que** os alertas sejam precisos e evitem falsos positivos.


### 2.1.3 Interface do Sistema e Alertas
#### US05:
- **Como** policial
- **Quero** que o sistema me envie alertas em tempo real, incluindo a localização exata da ocorrência, imagens da câmera e gravação do áudio (se disponível)
- **Para que** eu possa avaliar a situação e despachar a equipe mais próxima.

#### US06:
- **Como** policial
- **Quero** que uma interface intuitiva e fácil de usar, com mapa interativo mostrando a localização das câmeras e dos eventos, ferramentas de zoom e reprodução de imagens, e histórico de ocorrências
- **Para que** eu possa monitorar a situação e gerenciar as respostas de forma eficiente, aprendendo os locais de maior incidência e tomar medidas preventivas.


### 2.1.4 Privacidade e Segurança
#### US07:
- **Como** administrador do sistema
- **Quero** que o sistema garanta a privacidade das pessoas, anonimizando os dados e armazenando as imagens de forma segura
- **Para que** haja proteção contra o uso indevido das informações.

#### US08:
- **Como** administrador do sistema
- **Quero** controlar o acesso ao sistema e às imagens, através de autenticação de usuários e permissões de acesso
- **Para que** apenas pessoas autorizadas possam visualizar as informações.

## 2.2 Critérios de Aceitação
Cada história de usuário deve ser validada pelos seguintes critérios:
1. A funcionalidade deve atender ao propósito descrito na história de usuário.
2. O sistema deve passar por testes de precisão e minimizar alarmes falsos.
3. As notificações de alerta devem ser enviadas em tempo real para os canais designados.
4. A IA deve ser constantemente treinada e monitorada para melhorar a precisão da detecção.

## 2.3 Observações:
- É crucial que o sistema seja treinado com um conjunto de dados diversificado e representativo da população brasileira, para evitar vieses e garantir a precisão da detecção.
- A equipe deve trabalhar em conjunto com especialistas em violência contra a mulher, psicólogos e profissionais de segurança pública para garantir que o sistema atenda às necessidades reais e seja eficaz na prevenção e combate à violência.
- É importante que o sistema seja integrado com outras ferramentas e tecnologias de segurança pública, como bancos de dados criminais e sistemas de comunicação, para potencializar sua eficácia.

# 3. Arquitetura do Sistema:

## 3.1 Contexto Operacional:

O sistema funcionará integrado a uma infraestrutura de vigilância já existente, utilizando câmeras instaladas em locais públicos e privados. As câmeras capturam imagens e enviam esses dados para o processamento no módulo de IA do sistema, que é capaz de analisar microexpressões faciais para identificar sinais de medo ou estresse que possam indicar uma situação de risco. A arquitetura também contempla canais de comunicação priorizados com as forças policiais, permitindo o envio de alertas em tempo real.

## 3.2 Componentes Principais da Arquitetura:
### 3.2.1 Módulo de Captura de Imagens:

Responsável por coletar imagens em tempo real a partir das câmeras conectadas ao sistema.
Inclui mecanismos de pré-processamento para ajustar a qualidade das imagens e garantir o melhor desempenho da análise facial.

### 3.2.2 Processador de IA para Detecção de Microexpressões:
Este é o núcleo de análise do sistema, onde algoritmos de aprendizado de máquina e redes neurais processam as imagens capturadas.
O módulo é treinado para identificar microexpressões faciais associadas a emoções de medo, estresse e outras emoções relevantes que podem indicar perigo.
O Processador de IA realiza uma análise em tempo real, classificando a situação como “segura” ou “de risco”.

### 3.2.3 Sistema de Alerta para Forças Policiais:
Responsável por gerar notificações em tempo real ao detectar uma situação de risco.
Envia mensagens para canais exclusivos de contato com as forças policiais, permitindo o rápido acionamento.
Possui mecanismos de confirmação para reduzir falsos positivos, minimizando possíveis alarmes falsos.

### 3.2.4 Armazenamento Seguro de Dados:
Garante a integridade e confidencialidade dos dados capturados, armazenando registros de situações classificadas como "de risco" para posterior análise e auditoria.
Este módulo está em conformidade com as regulamentações de proteção de dados, como a LGPD, para assegurar a privacidade das pessoas capturadas pelas câmeras.

## 3.3 Fluxo de Operação:
### 3.3.1 Captura e Pré-processamento de Imagens: 
As câmeras registram o ambiente e transmitem as imagens para o módulo de captura de imagens, que as prepara para análise.

### 3.3.2 Análise e Classificação:
O Processador de IA recebe as imagens pré-processadas, identifica microexpressões faciais e classifica a situação como segura ou de risco.

### 3.3.3 Geração de Alertas: 
Se a situação for classificada como de risco, o sistema dispara alertas imediatos para as forças policiais por meio do sistema de alerta, utilizando canais de comunicação priorizados.

### 3.3.4 Armazenamento de Dados:
As imagens e resultados das análises são armazenados em um repositório seguro, onde podem ser acessados apenas por autoridades autorizadas para fins de investigação.

## 3.4 Benefícios da Arquitetura
### 3.4.1 Detecção Precisa e em Tempo Real: 
A análise de microexpressões faciais é processada em baixa latência, garantindo que qualquer risco seja identificado e notificado de forma rápida.

### 3.4.2 Segurança e Conformidade: 
A arquitetura foi projetada para atender às regulamentações de segurança e privacidade, com armazenamento seguro e tratamento responsável dos dados capturados.

### 3.4.3 Escalabilidade e Flexibilidade: 
A arquitetura modular permite que o sistema possa ser expandido com novos algoritmos de detecção e ajuste dos canais de comunicação, adequando-se às necessidades futuras.

# 4. Arquitetura do Software(conforme a seção 6 da norma 42010-2022 - IEEE/ISO/IEC):

## 4.1 Stakeholders e Requisitos da Arquitetura
- **Forças Policiais:** Precisam receber alertas com precisão e em tempo real para reduzir o tempo de resposta a incidentes.
- **Equipe de Desenvolvimento:** Requer uma estrutura modular e flexível para melhorar a capacidade de manutenção e atualização dos algoritmos de IA e das interfaces com o sistema de alertas.
- **Organizações de Proteção à Privacidade:** Demandam garantias de que os dados de vigilância respeitem as regulamentações de privacidade e segurança, como a LGPD.

## 4.2 Viewpoints Selecionados
A partir da norma IEEE/ISO/IEC 42010-2022, selecionamos viewpoints que proporcionam uma visão completa da arquitetura do software, considerando sua estrutura, comunicação, e segurança:
- **Viewpoint Funcional (Descrevendo o Comportamento do Sistema):**
Focado em detalhar os principais módulos funcionais que integram o sistema.

![Viewpoint Funcional](/media/ViewpointFuncional.png)

- **Viewpoint de Comunicação (Interação entre Componentes):**
Esclarece a comunicação entre os módulos do software, especialmente entre a detecção de IA e o sistema de alertas.

![Viewpoint de Comunicação](/media/ViewpointComunicacao.png)

- **Viewpoint de Segurança (Proteção de Dados e Privacidade):**
Define práticas de segurança para proteger as informações sensíveis geradas e capturadas pelo sistema.

![Viewpoint de Segurança](/media/ViewpointSeguranca.png)

## 4.3 Modelos de Componentes e Estrutura Modular do Software

### 4.3.1 Módulo de Captura de Imagens
- **Descrição:** Interface de entrada que coleta as imagens de vídeo em tempo real a partir das câmeras conectadas ao sistema.
- **Responsabilidades:**
	- Realizar o pré-processamento das imagens, incluindo a padronização da qualidade para análise.
	- Filtrar imagens irrelevantes para reduzir a carga de processamento da IA.
- **Comunicação:** Transmite as imagens para o Processador de IA para análise.
- **Concerns:** Qualidade das imagens e segurança na transferência de dados.

### 4.3.2 Módulo Processador de IA (Detecção de Microexpressões Faciais)
- **Descrição:** Módulo central de análise responsável por interpretar microexpressões faciais e identificar emoções de risco.
- **Responsabilidades:**
	- Processar as imagens recebidas e detectar microexpressões faciais que indiquem emoções como medo ou estresse.
	- Classificar a situação como “segura” ou “de risco” com base nos resultados da análise.
- **Comunicação:** Envia o resultado da análise para o Sistema de Alerta quando uma situação de risco é identificada.
- **Concerns:** Precisão e confiabilidade dos algoritmos de IA, controle de falsos positivos.

### 4.3.3 Sistema de Alerta
- **Descrição:** Gera e envia notificações para as forças policiais ao identificar uma situação de risco.
- **Responsabilidades:**
	- Estabelecer conexão com canais de comunicação exclusivos para alertar as forças policiais.
	- Confirmar a entrega dos alertas e permitir acompanhamento das notificações.
- **Comunicação:** Recebe a classificação de risco do Processador de IA e envia mensagens aos sistemas policiais.
- **Concerns:** Baixa latência na geração e envio dos alertas, garantia de confidencialidade no canal de comunicação.

### 4.3.4 Armazenamento Seguro de Dados
- **Descrição:** Repositório seguro para armazenar os dados capturados e os resultados das análises de situações classificadas como “de risco”.
- **Responsabilidades:**
	- Guardar os registros de forma segura e em conformidade com a LGPD.
	- Proteger o acesso aos dados, limitando-o a autoridades autorizadas para investigação e auditoria.
- **Comunicação:** Recebe dados diretamente do Processador de IA e do Sistema de Alerta.
- **Concerns:** Conformidade com a LGPD e segurança dos dados armazenados.

## 4.4 Fluxo de Dados e Comunicação Entre Componentes
- **Captura e Transmissão de Imagens:** As câmeras conectadas ao Módulo de Captura enviam as imagens processadas ao Processador de IA.
- **Análise e Detecção de Risco:** O Processador de IA classifica a situação e notifica o Sistema de Alerta caso um risco seja detectado.
- **Envio de Alertas:** O Sistema de Alerta comunica-se diretamente com as forças policiais por meio de canais de comunicação seguros e exclusivos.
- **Armazenamento Seguro:** Dados sensíveis das situações de risco são armazenados de forma segura, e acessíveis apenas para autoridades autorizadas.

## 4.5 Restrições e Condições de Operação
- **Restrições de Tempo Real:** O sistema precisa responder rapidamente à análise e envio de alertas, minimizando atrasos.
- **Segurança e Conformidade com Regulamentações:** Todos os módulos devem assegurar a proteção dos dados e conformidade com as leis de privacidade, como a LGPD.
- **Escalabilidade:** A arquitetura deve ser preparada para expansão, permitindo a adição de novos algoritmos de análise e suporte a mais câmeras.

## 4.6 Benefícios Arquiteturais e Riscos
**Benefícios:**
- **Modularidade:** Facilita atualizações e manutenção dos módulos de IA e alertas.
- **Segurança:** Conformidade com a LGPD e proteção dos dados capturados.
- **Tempo Real:** O sistema permite uma resposta rápida a incidentes, ajudando a prevenir crimes em potencial.

**Riscos:**
- **Falsos Positivos/Negativos:** Algoritmos de IA podem classificar erroneamente situações de risco, exigindo ajustes contínuos nos modelos de detecção.
- **Privacidade:** Garantir que as imagens e dados sensíveis estejam protegidos e apenas acessíveis para fins legais.
