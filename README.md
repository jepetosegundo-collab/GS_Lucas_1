# SportLife — Sistema de Monitoramento Ambiental

Disciplina:Computational Thinking for Engineering  
Curso: Engenharia de Computação — FIAP  
Turma: 1ECA

## Integrantes

- [João Pedro Moraes Basques] — RM [571710]
- [Anderson Luiz Sanches] — RM [571834]
- [Guilherme Correia] — RM [568836]

## Sobre o projeto

O SportLife é um sistema desenvolvido em Python para simular o monitoramento ambiental de um centro esportivo comunitário, composto por quadras, áreas destinadas à prática de atividades físicas e espaços de convivência.

O objetivo do projeto é receber e armazenar informações ambientais, analisar os valores registrados, identificar possíveis condições de atenção e gerar relatórios com os resultados da simulação.

## Parâmetros monitorados

- Temperatura do ar:(°C) — critério didático de alerta acima de 30 °C.
- Material particulado PM2.5: µg/m³ — referência de 50 µg/m³ para média de 24 horas.
- Ruído ambiental:(dB) — referência de 65 dB para o período diurno, considerando o cenário hipotético adotado.

As fontes, justificativas e limitações dos critérios estão apresentadas na pesquisa de referências ambientais e nos comentários do código.

## Funcionamento

O programa solicita a quantidade de leituras e recebe os valores de temperatura, PM2.5 e ruído informados pelo usuário.

Cada leitura é analisada individualmente e comparada com os critérios de referência. Quando algum parâmetro ultrapassa o valor estabelecido, o sistema apresenta um alerta.

Ao final da sequência, são calculadas as estatísticas dos parâmetros, a quantidade de ocorrências, o número de leituras críticas únicas e o percentual de leituras críticas. O sistema também apresenta uma classificação geral e gera um relatório em formato TXT.

Após a geração do relatório, o usuário pode iniciar uma nova sequência de monitoramento.

## Como executar

1. Abra o terminal na pasta do projeto.
2. Execute o comando:

py sportlife.py

O programa será iniciado no terminal e solicitará os dados necessários para a simulação.

## Arquivos do projeto

- `sportlife.py` — código-fonte do sistema.
- `README.md` — apresentação e instruções do projeto.
- `SportLife.pdf` — pesquisa dos parâmetros, fontes e justificativas.
- `relatorio_sportlife_1.txt` — exemplo de relatório gerado pelo programa.

## Observação

O SportLife utiliza valores informados pelo usuário para fins de simulação acadêmica. O sistema não realiza medições ambientais reais e não substitui avaliações técnicas.

A temperatura do ar isolada não determina a segurança para a prática de atividades físicas. Da mesma forma, a média aritmética do ruído é uma estatística descritiva simplificada e não corresponde a uma avaliação acústica oficial.
