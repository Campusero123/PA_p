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
