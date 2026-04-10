<br>


## 📊 Statistics for Data Science with Python — IBM  
> ### *Ambiente de estudo, prática e documentação*

<br>


Este repositório reúne todo o material produzido durante o curso **Statistics for Data Science with Python**, oferecido pela IBM.  
O objetivo é construir uma base sólida em estatística aplicada, com foco em técnicas essenciais para análise de dados e Machine Learning.

Aqui você encontrará:
- 🧪 **Notebooks práticos** com exercícios e experimentos  
- 📚 **Companion Book** (opcional) com explicações teóricas  
- 📂 **Estrutura organizada** para estudo e reuso  
- 🧠 **Processo de aprendizado documentado**  
- 📊 **Visualizações e análises estatísticas**  

<br><br>
## 🎯 1. Objetivo do Repositório

Este projeto documenta:
- o estudo completo do curso IBM Statistics for Data Science  
- os notebooks com práticas e exemplos  
- o raciocínio estatístico aplicado em Python  
- a organização de um ambiente profissional de Data Science  
- a evolução contínua do aprendizado  

O foco é dominar **estatística aplicada**, não apenas executar código.

<br><br>
## 📚 2. Conteúdo do Curso

O curso aborda tópicos fundamentais, incluindo:
- Tipos de dados e distribuições  
- Medidas de tendência central e dispersão  
- Probabilidade  
- Distribuições estatísticas  
- Amostragem e estimação  
- Testes de hipótese  
- Correlação e regressão  
- Estatística aplicada com Python  

Companion Book em:
- `docs/statistics_book.md`

<br><br>
## 🧪 3. Notebooks do Curso

Os notebooks seguem a progressão natural do conteúdo:

`notebooks/`
1. 01_intro_statistics.ipynb  
2. 02_data_types_and_distributions.ipynb  
3. 03_central_tendency_and_variability.ipynb  
4. 04_probability.ipynb  
5. 05_statistical_distributions.ipynb  
6. 06_sampling_and_estimation.ipynb  
7. 07_hypothesis_testing.ipynb  
9. 08_correlation_and_regression.ipynb  
9. 09_statistics_with_python.ipynb  
10. notebooks_model.md  

Cada notebook contém:
- exemplos práticos  
- visualizações  
- exercícios resolvidos  
- anotações complementares  

<br><br>
## 🏗️ 4. Estrutura do Projeto

```text
statistics           # statistics-for-data-science/
│
├── README.md
├── requirements.txt
├── config.py
├── .gitignore.py
│
├── data/
│   ├── raw/          # dados originais
│   └── processed/    # dados transformados
│
├── docs/
│   └── statistics_book.md
│
├── notebooks/
│   ├── 01_intro_statistics.ipynb
│   ├── 02_data_types_and_distributions.ipynb
│   ├── 03_central_tendency_and_variability.ipynb
│   ├── 04_probability.ipynb
│   ├── 05_statistical_distributions.ipynb
│   ├── 06_sampling_and_estimation.ipynb
│   ├── 07_hypothesis_testing.ipynb
│   ├── 08_correlation_and_regression.ipynb
│   ├── 09_statistics_with_python.ipynb
│   └── notebooks_model.md
│
├── scripts/
│   ├── utils.py
│   └── write_version.py
│
├── outputs/
│   ├── figures/
│   └── reports/
│
└── models/
```

<br><br>
## 🧠 5. Processo de Estudo

O fluxo recomendado:
1. Utilizar o `statistics_book.md` para acompanhamento do curso
2. Ler o conteúdo teórico do capítulo  
3. Executar o notebook correspondente  
4. Reproduzir e expandir os exemplos  
5. Criar visualizações adicionais  
6. Registrar aprendizados no Companion Book  
7. Versionar o progresso com commits claros  

Esse processo garante:
- profundidade conceitual  
- prática consistente  
- documentação contínua  
- evolução profissional  

<br><br>
## 🧩 6. Tecnologias Utilizadas

- Python  
- Pandas  
- NumPy  
- SciPy  
- Statsmodels  
- Matplotlib / Seaborn  
- Jupyter Notebook  


<br><br>
## 🧪 7. Como Reproduzir o Ambiente

~~~Python
pip install -r requirements.txt  
jupyter notebook  
~~~


<br><br>
## 🚀 8. Próximos Passos

- Criar os primeiros notebooks  
- Iniciar o Companion Book  
- Adicionar visualizações estatísticas  
- Consolidar exemplos para portfólio  


<br><br>
## 🤝 9. Autor

Moacir  
Estudo contínuo em Estatística, Machine Learning e Ciência de Dados.  
Este repositório documenta sua jornada técnica e serve como portfólio profissional.

<br><br>
## 🗺️ 10. Roadmap do Curso

Este roadmap organiza o progresso do curso **Statistics for Data Science with Python — IBM** em etapas claras, permitindo acompanhar a evolução do aprendizado de forma estruturada e consistente.


### 📌 **Fase 1 — Preparação do Ambiente**
- [x] Criar estrutura inicial do projeto  
- [x] Configurar `requirements.txt`  
- [x] Criar `config.py`  
- [x] Configurar CI  
- [x] Configurar CD (ativado apenas por tags)  
- [ ] Criar template base para notebooks  
- [ ] Criar índice inicial no `statistics_book.md`  

<br>


### 📌 **Fase 2 — Fundamentos de Estatística**
**Objetivo:** Construir a base teórica e prática essencial.

- [ ] Notebook 01 — Introdução à Estatística  
- [ ] Registrar conceitos no Companion Book  
- [ ] Criar exemplos próprios além dos do curso  

<br>


### 📌 **Fase 3 — Tipos de Dados e Distribuições**
- [ ] Notebook 02 — Tipos de Dados e Distribuições  
- [ ] Criar gráficos adicionais (histogramas, KDE, boxplots)  
- [ ] Documentar no Companion Book  
- [ ] Criar exemplos com datasets reais (opcional)  

<br>

### 📌 **Fase 4 — Medidas de Tendência Central e Dispersão**
- [ ] Notebook 03 — Média, Mediana, Moda, Variância, Desvio  
- [ ] Criar visualizações comparativas  
- [ ] Criar seção no Companion Book com fórmulas e interpretações  
- [ ] Criar exercícios extras  

<br>

### 📌 **Fase 5 — Probabilidade**
- [ ] Notebook 04 — Probabilidade  
- [ ] Criar exemplos com eventos independentes e dependentes  
- [ ] Documentar propriedades no Companion Book  
- [ ] Criar simulações com NumPy  

<br>

### 📌 **Fase 6 — Distribuições Estatísticas**
- [ ] Notebook 05 — Distribuições (Normal, Binomial, Poisson, etc.)  
- [ ] Criar gráficos comparativos  
- [ ] Criar simulações com `scipy.stats`  
- [ ] Documentar cada distribuição no Companion Book  

<br>

### 📌 **Fase 7 — Amostragem e Estimação**
- [ ] Notebook 06 — Amostragem e Estimadores  
- [ ] Criar exemplos com diferentes tamanhos de amostra  
- [ ] Documentar conceitos de viés e variância  
- [ ] Criar exercícios extras  

<br>

### 📌 **Fase 8 — Testes de Hipótese**
- [ ] Notebook 07 — Testes de Hipótese  
- [ ] Criar exemplos com t-test, z-test, chi-square  
- [ ] Criar fluxograma de decisão no Companion Book  
- [ ] Criar exercícios extras  

<br>

### 📌 **Fase 9 — Correlação e Regressão**
- [ ] Notebook 08 — Correlação e Regressão  
- [ ] Criar gráficos de dispersão com linhas de tendência  
- [ ] Documentar coeficientes e interpretações  
- [ ] Criar exemplos com datasets reais  

<br>

### 📌 **Fase 10 — Estatística Aplicada com Python**
- [ ] Notebook 09 — Estatística Aplicada  
- [ ] Criar estudo de caso próprio  
- [ ] Criar relatório em `outputs/reports/`  
- [ ] Documentar conclusões no Companion Book  

<br>

### 📌 **Fase 11 — Consolidação e Portfólio**
- [ ] Revisar todos os notebooks  
- [ ] Revisar o Companion Book  
- [ ] Criar README final com badges e links  
- [ ] Criar release versionada (ex.: `v1.0.0`)  
- [ ] Publicar no GitHub como projeto de portfólio  

<br>

### 📌 **Fase 12 — Extensões Futuras (Opcional)**
- [ ] Criar dashboards com Plotly  
- [ ] Criar scripts automatizados de análise  
- [ ] Integrar com datasets externos  
- [ ] Criar mini-projetos estatísticos  

<br><br>