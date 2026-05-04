# RESUMO GERAL  | STATISTCS FOR DATA SCIENCE WITH PYTHON 📊 

<a id="indice"></a>
## RESUMO ULTRACURTO (10 segundos)  

2. [**Descriptive Statistics**](#modulo2)
    - Estatística descritiva = resumir, organizar e interpretar dados
    - Tipos de dados: categóricos, numéricos, ordinais, razão
    - População vs amostra → parâmetros vs estatísticas
    - Média, mediana, moda → tendência central
    - Variância, desvio padrão → dispersão
    - Z‑score → padronização
    - Histogramas, barras, boxplots → visualização básica
    - Teaching ratings → laboratório prático

<br>

3. [**Data Visualization**](#modulo3)
    - Visualização = transformar dados em padrões visuais
    - Tipos de gráficos dependem da pergunta
    - Variáveis categóricas → barras
    - Variáveis numéricas → histogramas, densidade, boxplot
    - Relações → scatterplot
    - Storytelling → gráficos que comunicam uma mensagem
    - Boas práticas → clareza, cores, escalas, percepção visual

<br>

4. [**Probability Distributions**](#modulo4)
    - Probabilidade = chance  
    - PMF/PDF/CDF = formas de descrever distribuições  
    - Normal = distribuição contínua mais importante  
    - Z‑score = distância da média em σ  
    - t‑Student = comparação de médias com incerteza  
    - Hipóteses = H₀ vs Hₐ  
    - α e valor‑p = decisão estatística  
    - Tabela Z = probabilidades da Normal  
    - Teaching ratings = aplicação prática  

<br><br>

<a id="modulo2"></a>
[↑ Índice](#indice)
<details>
<summary> 📘 <b> MÓDULO 2 (Descriptive Statistics) </b></summary> <br>

0. Setup — Bibliotecas e Dados
    - numpy, pandas, matplotlib
    - teaching ratings dataset
    - Variáveis: idade, gênero, beleza, avaliação, tenure, etc.

1. Introdução à Estatística
    - Estatística = coletar, organizar, analisar e comunicar dados.
    - Duas áreas:
        - Estatística descritiva → descreve o que os dados mostram
        - Estatística inferencial → generaliza para a população
    - Aplicações: clima, economia, saúde, educação, esportes, pesquisas.

2. Tipos de Dados

    - 2.1 Estrutura dos dados
        - Cross-sectional → várias unidades em um único momento (teaching ratings)
        - Time series → uma variável ao longo do tempo
        - Panel data → combinação de ambos

    - 2.2 Tipos de variáveis
        - Categóricas:
            - Nominais (gender, minority, native)
            - Ordinais (níveis de satisfação)
        - Numéricas:
            - Discretas (students)
            - Contínuas (age)
            - Intervalo (temperatura)
            - Razão (renda, distância)
        - Identificadores (prof)

3. População, Amostra e Parâmetros
    - População → conjunto total
    - Amostra → subconjunto observado
    - Parâmetros (μ, σ²) → população
    - Estatísticas (x̄, s²) → amostra
    - teaching ratings = amostra de cursos reais

4. Medidas de Tendência Central

    - 4.1 Média
        - Centro de gravidade dos dados
        - Sensível a outliers

    - 4.2 Mediana
        - Divide os dados ao meio
        - Robusta a outliers

    - 4.3 Moda
        - Valor mais frequente
        - Útil para variáveis categóricas

5. Medidas de Dispersão

    - 5.1 Amplitude
        - Máximo − mínimo

    - 5.2 Variância e desvio padrão
        - Variância = dispersão quadrática
        - Desvio padrão = dispersão na mesma unidade da variável
        - Média + desvio padrão → leitura completa da distribuição

    - 5.3 Padronização (Z‑score)
        - z = (x − média) / desvio padrão
        - Média → 0
        - Desvio padrão → 1
        - Interpretação:
            - z = 0 → na média
            - z = 1 → 1σ acima
            - |z| > 2 → valores incomuns
        - beauty já vem padronizada no dataset

6. Visualização de Dados (básico)
    - Histograma → distribuição numérica
    - Gráfico de barras → categorias
    - Boxplot → mediana, quartis, outliers
    - Interpretação visual é parte essencial da estatística descritiva

7. Aplicações com Teaching Ratings
    - Identificação do tipo de dado (cross-sectional)
    - Estatísticas descritivas de students
    - Histograma de beauty
    - Comparação de beauty por gênero
    - Proporção de tenure por gênero
    - Gráficos interpretativos com média, mediana, desvio padrão

8. Exercícios Guiados
    - Média, mediana, mínimo e máximo
    - Comparações por gênero
    - Histogramas
    - Barplots
    - Medianas condicionais

9. Diagramas Conceituais
    - Tipos de dados
    - Tendência central
    - Dispersão
    - Relações entre conceitos

10. Apêndice Matemático Avançado
    - Propriedades da média
    - Variância como energia
    - Estimadores não-viesados
    - Justificativa do n−1 na variância amostral


</details>
<br><br>

<a id="modulo3"></a>
[↑ Índice](#indice)
<details>
<summary> 📘 <b> MÓDULO 3 (Visualização de Dados) </b></summary>
<br>

0. Setup — Bibliotecas e Dados
    - seaborn, matplotlib, numpy, pandas  
    - teaching ratings dataset  
    - Usado para demonstrar visualizações categóricas, numéricas e multivariadas  

1. Introdução: por que visualizar dados?
    - Visualização transforma números em padrões, histórias e decisões  
    - É o primeiro passo da análise exploratória (EDA)  
    - Ajuda a identificar:
        - padrões  
        - outliers  
        - assimetrias  
        - relações  
        - grupos  
    - Combina estatística + design + percepção + comunicação  

    - 1.1 História da visualização
        - Playfair → gráficos modernos  
        - Nightingale → coxcomb chart  
        - Tukey → EDA e boxplot  
        - Tufte → princípios de design  
        - Few → dashboards  
        - Abela → Chart Chooser  

    - 1.2 Por que visualizar antes de analisar?
        - Visualização = “olhar para o problema”  
        - Revela padrões que números não mostram sozinhos  

    - 1.3 Percepção visual
        - Processos pré-atentivos: cor, forma, tamanho, posição  
        - Leis da Gestalt: proximidade, similaridade, continuidade  

    - 1.4 Visualização como comunicação
        - Um gráfico é uma mensagem  
        - Deve destacar o que importa e remover o que distrai  

    - 1.5 Triângulo da Visualização (Abela)
        - Perguntas fundamentais:
            - Comparação  
            - Composição  
            - Distribuição  
            - Relação  
        - Base para escolher o gráfico certo  

    - 1.6 O que aprenderemos
        - Escolha de gráficos  
        - Storytelling  
        - Boas práticas  
        - Visualizações multivariadas  
        - Uso de cores, escalas e formas  

2. Fundamentos da Visualização

    - 2.1 Tipos de variáveis → tipos de gráficos
        - Categóricas → barras, countplot, stacked bar  
        - Numéricas → histograma, KDE, boxplot, violinplot  
        - Numérica × Numérica → scatterplot, regplot  
        - Numérica × Categórica → boxplot, violinplot  
        - Categórica × Categórica → heatmap, stacked bar  

    - 2.2 Método de Apresentação Extrema (Abela)
        - Pergunta → gráfico  
        - Comparação, Composição, Distribuição, Relação  

    - 2.3 Boas práticas de design
        - Maximize data‑ink ratio  
        - Evite 3D  
        - Use cores com propósito  
        - Prefira posição a área  
        - Títulos informativos  
        - Consistência visual  

    - 2.4 Erros comuns
        - Pizza para muitos grupos  
        - 3D desnecessário  
        - Cores aleatórias  
        - Escalas quebradas  
        - Barras para variáveis contínuas  

    - 2.5 Exemplo: countplot
        - Frequência de categorias (gender)

    - 2.6 Exemplo: distribuição numérica
        - Histograma + KDE  
        - Interpretação de beauty como variável padronizada (z‑score)

3. Ferramentas em Python

    - 3.1 matplotlib
        - Base da visualização  
        - Controle total, porém verboso  

    - 3.2 seaborn
        - Camada estatística de alto nível  
        - Ideal para Data Science  
        - Entende DataFrames e tipos de variáveis  

    - 3.3 Estilos e temas
        - whitegrid, darkgrid, ticks, white  

    - 3.4 Paletas de cores
        - Qualitativas, sequenciais, divergentes  

    - 3.5 Boas práticas de código
        - figsize, títulos, rótulos, paletas consistentes  

4. Gráficos para Variáveis Categóricas

    - 4.1 Countplot
        - Frequências absolutas  
        - Ex.: cursos por gênero  

    - 4.2 Barplot
        - Comparação de médias  
        - Ex.: avaliação média por divisão  

    - 4.3 Stacked Bar
        - Composição dentro de categorias  
        - Ex.: tenure por gênero  

    - 4.4 Catplot
        - Visualização categórica multivariada  
        - hue, col, row  

    - 4.5 Facetamento
        - Comparações entre divisões  
        - Ex.: gênero × tenure × divisão  

5. Gráficos para Variáveis Numéricas
    - Histograma  
    - KDE (densidade)  
    - Boxplot  
    - Violinplot  
    - ECDF (avançado)  

6. Relações entre Variáveis
    - Scatterplot  
    - Regplot  
    - Jointplot  
    - Pairplot  

7. Storytelling com Dados
    - Gráficos devem responder perguntas  
    - Destacar o que importa  
    - Guiar o olhar  
    - Remover ruído visual  
    - Construir narrativa  

8. Aplicações com Teaching Ratings
    - Comparações categóricas (gender, tenure, division)  
    - Distribuições numéricas (beauty, eval, age)  
    - Relações entre variáveis (age × eval)  
    - Visualizações multivariadas com catplot  

9. Exercícios Guiados
    - Countplot  
    - Histograma  
    - Boxplot  
    - Comparações por gênero  
    - Facetamento  

10. Diagramas Conceituais
    - Tipos de variáveis  
    - Tipos de gráficos  
    - Princípios de design  
    - Fluxo de escolha de gráfico  

11. Apêndice Matemático Avançado
    - Percepção visual formal  
    - Weber-Fechner  
    - Shannon (entropia)  
    - Gestalt  
    - Justificativas perceptuais para escolha de gráficos  

12. Encerramento
    - Visualização = ponte entre dados e decisão  
    - Combina estatística, design e comunicação  
    - Base para análises mais profundas nos módulos seguintes  

</details>
<br><br>

<a id="modulo4"></a>
[↑ Índice](#indice)
<details>
<summary> 📘 <b> MÓDULO 4 (Introdução a distribuições de probabilidade) </b></summary> <br>

0. Setup — Bibliotecas e Dados  
    - Importação de numpy, pandas, matplotlib, scipy.stats  
    - Carregamento do dataset teaching ratings  
    - Dataset usado para probabilidades, z‑score, normal e t‑Student  

1. Probabilidade e Números Aleatórios  
    - Probabilidade ∈ [0,1]  
    - Espaço amostral (S) e eventos (A ⊆ S)  
    - Probabilidade clássica: P(A) = favoráveis / possíveis  
    - Exemplo: soma de dois dados → distribuição discreta  

2. Variáveis Aleatórias  
    - Discretas → valores isolados (contagens)  
    - Contínuas → valores em intervalos (medidas)  
    - Cada tipo usa uma função diferente (PMF vs PDF)  

3. PMF, PDF e CDF  
    - PMF → probabilidade exata de cada valor (discretas)  
    - PDF → densidade; probabilidade = área sob a curva (contínuas)  
    - CDF → probabilidade acumulada P(X ≤ x)  

4. Distribuição Normal  
    - Forma de sino, simétrica  
    - Parâmetros: média (μ) e desvio padrão (σ)  
    - Probabilidade = área sob a curva  
    - Regra 68-95-99.7  
    - Padronização: Z = (X − μ) / σ  

5. Distribuição t de Student  
    - Usada quando σ é desconhecido e n é pequeno  
    - Caudas mais pesadas que a Normal  
    - Graus de liberdade: ν = n − 1  
    - Converge para a Normal quando ν cresce  
    - Aplicação: comparação de médias (teaching ratings)
        - 8-9 Normal 2 e t‑Student 2  
            - Aplicações adicionais  
            - Visualizações complementares  
            - Conexões com o dataset teaching ratings  


6. Hipóteses Estatísticas  
    - H₀: hipótese nula (nenhuma diferença)  
    - Hₐ: hipótese alternativa (diferença existe)  
    - Testes: bilateral (≠), unilateral (< ou >)  
    - Visualização das regiões de rejeição  

7. Alfa (α) e Valor‑p  
    - α = probabilidade de erro tipo I  
    - Define região crítica  
    - Valor‑p = evidência contra H₀  
    - Quanto menor o valor‑p, maior a evidência  

10. Aplicações com Teaching Ratings  
    - Comparação de médias por gênero  
    - Intervalos de confiança com distribuição t  
    - Interpretação visual: sobreposição dos ICs  

11. Tabela Z — Normal Padrão  
    - 31 linhas (0.0 a 3.0)  
    - 10 colunas (0.00 a 0.09)  
    - 310 valores  
    - Usada para probabilidades da Normal Padrão  

12. Exercícios Guiados  
    - Probabilidades  
    - Interpretação de gráficos  
    - Uso de z‑score e t‑score  

13. Apêndice Matemático Avançado  
    - Demonstrações  
    - Derivações  
    - Fundamentos teóricos  

</details>