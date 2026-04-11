<br>

## 📊 Statistics for Data Science with Python — IBM  
> #### *Ambiente de estudo, prática e documentação pessoal*

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![IBM](https://img.shields.io/badge/IBM-Statistics%20for%20Data%20Science-blue)
![License](https://img.shields.io/badge/License-Projeto%20Autoral-green)

Este repositório documenta minha jornada no curso **Statistics for Data Science with Python**, oferecido pela IBM.  
O objetivo é consolidar o aprendizado em estatística aplicada, organizar o raciocínio estatístico e construir um ambiente profissional de estudo e experimentação.

<br><br>
## 🔒 1. Política de Conteúdo (IBM & Autoral)

Para respeitar direitos autorais e manter o repositório profissional:

#### ✔ Conteúdo incluído no repositório  
Somente materiais **autorais**, criados por mim:

- `notebooks/7_finalExamReview.ipynb`  
- `notebooks/8_appliedStatisticsForDataScience.ipynb`  
- `docs/statistics_book.md` (Companion Book)  
- scripts, utilitários e dados sintéticos  
- anotações e análises próprias  

#### ❌ Conteúdo excluído do repositório  
Os notebooks **1 a 6** são materiais originais da IBM.  
Por isso:
- não são versionados  
- estão listados no `.gitignore`  
- são usados apenas localmente para estudo  

Essa abordagem garante conformidade com direitos autorais e transparência.

<br><br>
## 📂 2. Estrutura do Projeto

~~~text
statistics/
│
├── README.md
├── requirements.txt
├── config.py
│
├── data/
│   ├── raw/                        # dados originais (não versionados)
│   └── processed/                  # dados transformados
│
├── docs/
│   └── statistics_book.md          # Companion Book (autoral)
│
├── notebooks/
│   ├── 1_reviewIntroduction.ipynb                  # (Ignorado - IBM)
│   ├── 2_descriptiveStatistics.ipynb               # (Ignorado - IBM)
│   ├── 3_visualizingData.ipynb                     # (Ignorado - IBM)
│   ├── 4_introductionToProbabilityDistribution.ipynb   # (Ignorado - IBM)
│   ├── 5_hypothesisTesting.ipynb                   # (Ignorado - IBM)
│   ├── 6_regressionAnalysis.ipynb                  # (Ignorado - IBM)
│   ├── 7_finalExamReview.ipynb                     # ✔ Autoral
│   ├── 8_appliedStatisticsForDataScience.ipynb     # ✔ Autoral
│   └── laboratory/
│
├── outputs/
│   ├── figures/
│   └── reports/
│
├── scripts/
│   ├── utils.py
│   └── write_version.py
│
└── models/
~~~

<br><br>
## 📚 3. Companion Book

O Companion Book está em:

~~~text
docs/statistics_book.md
~~~

Ele contém:

- explicações teóricas  
- fluxogramas  
- árvores conceituais  
- exemplos sintéticos  
- capítulos organizados conforme o curso  
- preparação para o exame final  

> O conteúdo é **100% autoral**.


<br><br>
## 🧪 4. Notebooks Autorais

#### ✔ `7_finalExamReview.ipynb`  
Revisão completa para o exame final, com:

- síntese dos conceitos  
- exemplos aplicados  
- exercícios de revisão  
- preparação para o projeto final  
<br>
#### ✔ `8_appliedStatisticsForDataScience.ipynb`  
Integração prática de estatística com:

- EDA  
- testes de hipótese  
- regressão  
- visualização  
- raciocínio estatístico aplicado  

> Ambos são **autorais** e podem ser publicados.


<br><br>
## 🧠 5. Processo de Estudo

Fluxo recomendado:

1. Ler o capítulo correspondente no Companion Book  
2. Executar o notebook autoral  
3. Criar visualizações adicionais  
4. Registrar aprendizados  
5. Versionar o progresso com commits claros  

Esse processo garante:

- profundidade conceitual  
- prática consistente  
- documentação contínua  
- evolução profissional  


<br><br>
## 🧩 6. Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3.10-blue)
![NumPy](https://img.shields.io/badge/NumPy-Array%20Computing-orange)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![SciPy](https://img.shields.io/badge/SciPy-Statistics%20%26%20Math-lightgrey)
![Statsmodels](https://img.shields.io/badge/Statsmodels-Statistical%20Modeling-yellow)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-blueviolet)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-teal)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)

Ferramentas utilizadas ao longo do projeto:

- **Python** para análise e experimentação  
- **NumPy** para operações numéricas  
- **Pandas** para manipulação de dados  
- **SciPy** para estatística aplicada  
- **Statsmodels** para regressão e testes estatísticos  
- **Matplotlib** e **Seaborn** para visualização  
- **Jupyter Notebook** como ambiente interativo  


<br><br>
## 🧪 7. Como Reproduzir o Ambiente

~~~bash
pip install -r requirements.txt
jupyter notebook
~~~


<br><br>
## 🤝 8. Autor

Moacir  
Estudo contínuo em Estatística, Machine Learning e Ciência de Dados.  
Este repositório documenta minha jornada técnica e serve como portfólio profissional.


<br><br>
## 🗺️ 09. Roadmap do Curso

Este roadmap organiza o progresso do curso **Statistics for Data Science with Python — IBM** em etapas claras, permitindo acompanhar a evolução do aprendizado de forma estruturada e consistente.

<br>

### 📌 **Fase 1 — Preparação do Ambiente**
- [x] Criar estrutura inicial do projeto  
- [x] Configurar `requirements.txt`  
- [x] Criar `config.py`  
- [x] Configurar CI/CD (ativado apenas por tags)  
- [x] Criar template base para notebooks  
- [x] Definir política de conteúdo (IBM vs Autoral)  

<br>

### 📌 **Fase 2 — Capítulo 1 + Notebook 1 (Ignorado)**
**Tema:** Review Introduction (Introdução à Estatística)   
**Objetivo:** Construir a base conceitual do curso.

- [x] Estudar notebook 1 (local, não versionado)  
- [x] Criar capítulo 1 no Companion Book  
- [x] Registrar conceitos fundamentais  
- [ ] Criar exemplos sintéticos adicionais  

<br>

### 📌 **Fase 3 — Capítulo 2 + Notebook 2 (IGNORADO)**
**Tema: Descriptive Statistics (Estatística Descritiva)**

- [x] Estudar notebook 2  
- [x] Criar capítulo 2 no Companion Book  
- [ ] Criar gráficos adicionais (histogramas, boxplots, KDE)  
- [ ] Criar exemplos sintéticos próprios  

<br>

### 📌 **Fase 4 — Capítulo 3 + Notebook 3 (IGNORADO)**
**Tema: Visualizing Data (Visualização de Dados)**

- [x] Estudar notebook 3  
- [x] Criar capítulo 3 no Companion Book  
- [ ] Criar visualizações comparativas  
- [ ] Criar exercícios extras  

<br>

### 📌 **Fase 5 — Capítulo 4 + Notebook 4 (IGNORADO)**
**Tema: Probability Distribution (Distribuições e Probabilidade)**

- [x] Estudar notebook 4  
- [x] Criar capítulo 4 no Companion Book  
- [ ] Criar simulações com NumPy  
- [ ] Criar exemplos sintéticos de distribuições  

<br>

### 📌 **Fase 6 — Capítulo 5 + Notebook 5 (IGNORADO)**
**Tema: Hypothesis Testing (Testes de Hipótese)**

- [x] Estudar notebook 5  
- [x] Criar capítulo 5 no Companion Book  
- [ ] Criar fluxograma de decisão  
- [ ] Criar exercícios extras  

<br>

### 📌 **Fase 7 — Capítulo 6 + Notebook 6 (IGNORADO)**
**Tema: Regression Analysis (Regressão Linear)**

- [x] Estudar notebook 6  
- [x] Criar capítulo 6 no Companion Book  
- [ ] Criar exemplos sintéticos de regressão  
- [ ] Criar visualizações com linha de tendência  

<br>

### 📌 **Fase 8 — Capítulo 7 + Notebook 7 (AUTORAL)**
**Tema: Review Final Exam (Revisão para o Exame Final)**

- [x] Criar notebook 7 (`7_finalExamReview.ipynb`)  
- [x] Criar capítulo 7 no Companion Book  
- [x] Criar exemplos sintéticos para revisão  
- [ ] Criar simulado extra (opcional)  

<br>

### 📌 **Fase 9 — Capítulo 8 + Notebook 8 (AUTORAL)**
**Tema: Applied Statistics (Estatística Aplicada para Data Science)**

- [x] Criar notebook 8 (`8_appliedStatisticsForDataScience.ipynb`)  
- [x] Criar capítulo 8 no Companion Book  
- [x] Integrar EDA + testes + regressão  
- [ ] Criar estudo de caso adicional (opcional)  

<br>

### 📌 **Fase 10 — Projeto Final (Boston Housing)**
**Tema:** Aplicação completa da estatística**

- [ ] Executar o notebook oficial do projeto (local)  
- [ ] Criar relatório em `outputs/reports/`  
- [ ] Registrar conclusões no Companion Book  
- [ ] Preparar versão para submissão (AI-Graded ou Peer-Graded)  

---

### 📌 **Fase 11 — Consolidação e Portfólio**
- [ ] Revisar todos os notebooks autorais  
- [ ] Revisar o Companion Book completo  
- [ ] Criar README final com badges e links  
- [ ] Criar release versionada (ex.: `v1.0.0`)  
- [ ] Publicar no GitHub como projeto de portfólio  

---

### 📌 **Fase 12 — Extensões Futuras (Opcional)**
- [ ] Criar dashboards com Plotly  
- [ ] Criar scripts automatizados de análise  
- [ ] Integrar com datasets externos  
- [ ] Criar mini-projetos estatísticos  
- [ ] Criar versão em inglês do Companion Book  


<br><br>