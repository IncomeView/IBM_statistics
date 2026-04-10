# 📘 Statistics for data science with python

# Capítulo 1 — Introdução ao Curso e Fundamentos da Análise Estatística
<details>

## 1. Introdução
<details>
<br>

O Módulo 1 do curso *IBM Statistics for Data Science with Python* apresenta o propósito geral da disciplina, os instrutores, a estrutura do curso e as ferramentas que serão utilizadas. Embora seja um módulo introdutório, ele estabelece a base conceitual para todo o raciocínio estatístico que será desenvolvido nos módulos seguintes.

A estatística é apresentada como uma ferramenta essencial para transformar dados em conhecimento. O curso enfatiza que estatística não é apenas cálculo — é **interpretação**, **raciocínio** e **tomada de decisão baseada em evidências**.

Este capítulo tem três objetivos principais:

- contextualizar o papel da estatística na ciência de dados;  
- apresentar o fluxo geral do pensamento estatístico;  
- preparar o leitor para os próximos capítulos, que entrarão em estatística descritiva, visualização, probabilidade, testes de hipótese e regressão.

O vídeo de boas‑vindas reforça que o curso é prático, aplicado e orientado ao uso de Python e Jupyter Notebooks — ferramentas centrais para o cientista de dados moderno.

</details>
<br>

## 2. Revisão do fluxo anterior
<details>
<br>

Como este é o primeiro capítulo, não há conteúdo anterior a ser revisado. No entanto, o módulo 1 já introduz elementos fundamentais que moldam todo o curso:

- estatística como linguagem da ciência de dados;  
- Python como ferramenta de análise;  
- Jupyter como ambiente de experimentação;  
- bibliotecas essenciais (Pandas, NumPy, SciPy, Matplotlib, Seaborn, Scikit‑learn, Statsmodels).

Esses elementos formam o alicerce para todos os capítulos seguintes. A partir daqui, cada novo conceito estatístico será acompanhado de exemplos práticos em Python.

</details>
<br>

## 3. Apresentação do problema
<details>
<br>

O problema central que este capítulo responde é:

> **Por que precisamos de estatística para fazer ciência de dados?**

No cotidiano, lidamos com incerteza, variabilidade e dados imperfeitos. A estatística fornece métodos para:

- resumir grandes quantidades de informação;  
- identificar padrões;  
- quantificar incertezas;  
- tomar decisões fundamentadas;  
- construir modelos que generalizam para novos dados.

Exemplos reais:

- **Negócios:** prever demanda, segmentar clientes, medir impacto de campanhas.  
- **Saúde:** avaliar eficácia de tratamentos, analisar riscos.  
- **Transporte:** estimar fluxo de tráfego, otimizar rotas.  
- **Marketing:** medir conversão, testar hipóteses sobre comportamento.  
- **Economia:** analisar tendências, prever indicadores.

Sem estatística, decisões seriam baseadas apenas em intuição — e intuição não escala.

</details>
<br>

## 4. Conceito central
<details>
<br>

### 4.1 Explicação intuitiva

Estatística é o processo de transformar dados em conhecimento.  
Ela responde perguntas como:

- “O que está acontecendo?”  
- “Por que isso está acontecendo?”  
- “O que provavelmente acontecerá depois?”  

### 4.2 Explicação formal

A estatística se divide em duas áreas principais:

- **Estatística descritiva:** resume e organiza dados.  
- **Estatística inferencial:** tira conclusões sobre populações a partir de amostras.

### 4.3 O que a estatística resolve

- Variabilidade natural dos dados  
- Incerteza em medições  
- Comparações entre grupos  
- Relações entre variáveis  
- Previsões e estimativas  

### 4.4 O que a estatística NÃO resolve

- Dados mal coletados  
- Viés de amostragem  
- Erros de interpretação  
- Causalidade sem experimentação  
- Problemas sem contexto  

### 4.5 Fluxograma conceitual — O processo estatístico

~~~text
Início
  ↓
Coletar dados
  ↓
Entender o tipo de dado
  ↓
Aplicar estatística descritiva
  ↓
Visualizar padrões
  ↓
Formular hipóteses
  ↓
Aplicar métodos inferenciais
  ↓
Interpretar resultados
  ↓
Tomar decisão
~~~

### 4.6 Fluxograma — Como pensar estatisticamente

~~~text
Pergunta
  ↓
Dados
  ↓
Análise
  ↓
Evidência
  ↓
Conclusão
~~~

</details>
<br>

## 5. Exemplos conceituais com código
<details>
<br>

Os exemplos abaixo usam dados sintéticos e servem apenas para ilustrar conceitos introdutórios.

### 5.1 Criando um pequeno conjunto de dados

~~~python
import pandas as pd

df = pd.DataFrame({
    "idade": [22, 35, 29, 41, 30],
    "salario": [2500, 4800, 3200, 6100, 4000]
})
df
~~~

### 5.2 Calculando estatísticas simples

~~~python
df.describe()
~~~

Esse comando resume:

- média  
- mediana  
- desvio padrão  
- valores mínimo e máximo  

### 5.3 Visualizando uma relação simples

~~~python
import matplotlib.pyplot as plt

plt.scatter(df["idade"], df["salario"])
plt.xlabel("Idade")
plt.ylabel("Salário")
plt.title("Relação entre idade e salário")
plt.show()
~~~

Esses exemplos ilustram como Python e Jupyter serão usados ao longo do curso para explorar dados e aplicar conceitos estatísticos.

</details>
<br>

## 6. Integração com capítulos anteriores
<details>
<br>

Como este é o primeiro capítulo, ele estabelece a base para todos os demais. A partir daqui:

- o Capítulo 2 aprofundará estatística descritiva;  
- o Capítulo 3 explorará visualização de dados;  
- o Capítulo 4 introduzirá distribuições de probabilidade;  
- o Capítulo 5 abordará testes de hipótese;  
- o Capítulo 6 apresentará regressão e correlação.

Este capítulo prepara o terreno conceitual para entender por que essas técnicas existem e como elas se conectam.

</details>
<br>

## 7. Boas práticas e limitações
<details>
<br>

### ✔ Boas práticas

- Sempre começar com perguntas claras.  
- Entender o tipo de dado antes de aplicar técnicas.  
- Usar visualizações para complementar estatísticas.  
- Interpretar resultados no contexto do problema.  
- Documentar raciocínio e decisões.

### ⚠ Limitações

- Estatística não corrige dados ruins.  
- Resultados podem ser sensíveis a outliers.  
- Inferências dependem de suposições.  
- Correlação não implica causalidade.

### ❗ Armadilhas comuns

- Confiar apenas em médias.  
- Ignorar variabilidade.  
- Interpretar gráficos sem contexto.  
- Aplicar técnicas avançadas sem entender fundamentos.

</details>
<br>

## 8. Glossário técnico
<details>
<br>

- **Estatística descritiva:** técnicas para resumir dados.  
- **Estatística inferencial:** técnicas para generalizar conclusões.  
- **Variável:** característica observada (idade, renda, etc.).  
- **Amostra:** subconjunto de uma população.  
- **População:** conjunto completo de interesse.  
- **Distribuição:** forma como valores se espalham.  
- **Python:** linguagem usada para análise.  
- **Jupyter Notebook:** ambiente interativo para código e texto.

</details>
<br>

## 9. Referência rápida
<details>
<br>

- Estatística transforma dados em conhecimento.  
- O curso usa Python, Jupyter e bibliotecas científicas.  
- O processo estatístico segue um fluxo lógico:  
  coleta → descrição → visualização → inferência → decisão.  
- Este capítulo prepara para estatística descritiva.  

</details>
<br>

## 10. Conclusão do capítulo
<details>
<br>

Este capítulo apresentou a base conceitual do curso: o papel da estatística, o fluxo do raciocínio estatístico e as ferramentas que serão utilizadas. A partir daqui, cada capítulo aprofundará um componente essencial da análise estatística.

O próximo capítulo introduzirá **estatística descritiva**, o primeiro passo concreto para transformar dados em informação.

</details>
</details>
<br>

# Capítulo 2 — Estatística Descritiva
<details>


## 1. Introdução
<details>
<br>

A estatística descritiva é o primeiro bloco fundamental da análise estatística.  
Ela responde à pergunta mais básica e, ao mesmo tempo, mais poderosa:

> **“O que os dados dizem antes de qualquer modelo?”**

No Módulo 2 do curso *IBM Statistics for Data Science with Python*, os instrutores mostram como estatísticas simples — média, mediana, moda, variância, desvio padrão — já revelam padrões profundos sobre fenômenos reais, como:

- clima  
- preços de moradia  
- salários  
- desempenho esportivo  
- criminalidade  
- comportamento de consumo  

Este capítulo transforma esse conteúdo em uma estrutura clara, intuitiva e visual, preparando você para:

- interpretar dados com precisão  
- escolher medidas adequadas  
- evitar erros comuns  
- construir análises sólidas antes de qualquer modelagem  

### 🎯 Motivação

A estatística descritiva é o **primeiro filtro** entre dados brutos e conhecimento.  
Sem ela, qualquer análise posterior — visualização, probabilidade, regressão — fica comprometida.

### 🔗 Conexão com o capítulo anterior

O Capítulo 1 apresentou:

- o papel da estatística  
- o fluxo geral da análise  
- o uso de Python e Jupyter  

Agora, entramos no **primeiro componente técnico** desse fluxo.

### 🎥 Relação com o vídeo correspondente

O vídeo “Bem-vindo ao Statistics!” mostra como estatísticas simples aparecem em:

- previsões do tempo  
- notícias econômicas  
- esportes  
- mídia  
- comportamento social  

Este capítulo organiza esse conteúdo em uma estrutura didática e aplicável.

</details>
<br>

## 2. Revisão do fluxo anterior
<details>
<br>

No capítulo anterior, aprendemos:

- o que é estatística  
- por que ela é essencial  
- como funciona o processo estatístico  
- como Python e Jupyter serão usados  

Agora, avançamos para a primeira etapa concreta do fluxo:

~~~text
Dados brutos
  ↓
Estatística descritiva
  ↓
Visualização
  ↓
Probabilidade
  ↓
Inferência
  ↓
Modelagem
~~~

A estatística descritiva é o **ponto de partida obrigatório**.

### Por que isso importa agora?

Porque antes de:

- criar gráficos  
- estimar distribuições  
- testar hipóteses  
- ajustar regressões  

…você precisa entender:

- como os dados se distribuem  
- qual é o valor típico  
- quanta variabilidade existe  
- quais são os extremos  
- se há simetria ou assimetria  

### Como o conteúdo se encaixa no curso

Este capítulo prepara você para:

- Capítulo 3: Visualização  
- Capítulo 4: Distribuições  
- Capítulo 5: Testes de hipótese  
- Capítulo 6: Regressão e correlação  

Sem estatística descritiva, nada disso funciona.

</details>
<br>

## 3. Apresentação do problema
<details>
<br>

A estatística descritiva responde a três perguntas fundamentais:

### **1. Qual é o valor típico?**  
(média, mediana, moda)

### **2. Quão dispersos estão os dados?**  
(variância, desvio padrão, amplitude)

### **3. Como os dados estão distribuídos?**  
(simetria, caudas, extremos)

Essas perguntas aparecem em situações reais:

### 🏠 **Negócios e economia**
- preço médio de imóveis  
- variação salarial  
- inflação mensal  

### 🏥 **Saúde**
- idade média de pacientes  
- variabilidade de pressão arterial  
- distribuição de tempos de espera  

### 🚗 **Transporte**
- velocidade média  
- variabilidade no tempo de viagem  

### 📈 **Mercado financeiro**
- retorno médio  
- volatilidade (desvio padrão)  

### 🎮 **Esportes**
- pontuação média  
- consistência de desempenho  

### Fluxograma — Quando usar estatística descritiva

~~~text
Início
  ↓
Tenho dados brutos?
  ↓
Sim → Quero entender o comportamento geral?
  ↓
Sim → Aplicar estatística descritiva
  ↓
Interpretar padrões
  ↓
Decidir próximos passos (visualizar, modelar, testar hipóteses)
~~~

### Árvore de decisão — Qual medida usar?

~~~text
                     Tipo de variável?
                     /              \
                Categórica        Numérica
                /       \         /       \
         Nominal     Ordinal   Contínua  Discreta
            |           |          |         |
         Moda       Mediana     Média     Média
                     Moda       Mediana   Mediana
~~~

### O que queremos responder neste capítulo

- Como identificar o tipo de dado  
- Como escolher a medida correta  
- Como interpretar média, mediana e moda  
- Como entender variância e desvio padrão  
- Como usar Python para calcular tudo isso  

</details>
<br>

## 4. Conceito central
<details>
<br>

A estatística descritiva é o conjunto de técnicas que permite **resumir, organizar e interpretar dados** antes de qualquer modelagem.  
Ela responde às perguntas fundamentais:

- Qual é o valor típico?  
- Quão dispersos estão os dados?  
- Como os dados se distribuem?  
- Existem padrões, simetrias ou extremos?  

Nesta seção, vamos construir a intuição e a formalização dessas ideias.

---

### 4.1 Explicação intuitiva

Imagine que você recebe uma planilha com 10.000 linhas.  
Ninguém consegue “ver” 10.000 números.  
Mas você consegue ver:

- uma **média**  
- uma **mediana**  
- uma **moda**  
- um **desvio padrão**  
- um **intervalo**  

Esses valores funcionam como **resumos inteligentes**, que condensam milhares de observações em poucos números significativos.

#### Analogia: “O retrato falado dos dados”

A estatística descritiva funciona como um retrato falado:

- **Média** → o “rosto típico”  
- **Mediana** → o “ponto central”  
- **Moda** → o “traço mais comum”  
- **Desvio padrão** → o “quanto o rosto varia”  
- **Intervalo** → os “limites extremos”  

---

### 4.2 Explicação formal

A estatística descritiva se divide em três grupos:

#### **1. Medidas de tendência central**
- Média  
- Mediana  
- Moda  

#### **2. Medidas de dispersão**
- Variância  
- Desvio padrão  
- Amplitude (range)  

#### **3. Medidas de posição**
- Quartis  
- Percentis  
- IQR (intervalo interquartil)  

---

### 4.3 O que a técnica resolve

- Resumo de grandes volumes de dados  
- Comparação entre grupos  
- Identificação de padrões gerais  
- Detecção de valores extremos  
- Preparação para visualização e modelagem  

---

### 4.4 O que a técnica NÃO resolve

- Não identifica causalidade  
- Não substitui visualização  
- Não detecta relações complexas entre variáveis  
- Não corrige dados ruins  
- Não substitui inferência estatística  

---

### 4.5 Fluxograma conceitual — Como escolher a medida correta

~~~text
Início
  ↓
Qual é o tipo de variável?
  ↓
Categórica? → Moda
  ↓
Numérica?
  ↓
Distribuição simétrica? → Média
  ↓
Distribuição assimétrica? → Mediana
  ↓
Precisa medir variabilidade? → Desvio padrão / Variância
  ↓
Precisa medir extremos? → Amplitude / Quartis / IQR
~~~

---

### 4.6 Árvore conceitual — Estrutura da estatística descritiva

~~~text
Estatística Descritiva
├── Tendência Central
│   ├── Média
│   ├── Mediana
│   └── Moda
├── Dispersão
│   ├── Variância
│   ├── Desvio Padrão
│   └── Amplitude
└── Posição
    ├── Quartis
    ├── Percentis
    └── IQR
~~~

---

### 4.7 Script conceitual — Processo mental do analista

~~~text
1. Identifique o tipo de variável
2. Verifique se há outliers
3. Observe a forma da distribuição
4. Escolha a medida de tendência central adequada
5. Calcule a dispersão para entender variabilidade
6. Use quartis para entender extremos e caudas
7. Combine tudo para interpretar o comportamento dos dados
~~~

---

### 4.8 Fluxograma — Média vs Mediana vs Moda

~~~text
                  Dados numéricos?
                     /        \
                   Sim        Não → Moda
                   |
           Distribuição simétrica?
                /         \
              Sim         Não
              |            |
            Média       Mediana
~~~

---

### 4.9 Fluxograma — Variância vs Desvio Padrão

~~~text
Preciso medir variabilidade?
  ↓
Sim
  ↓
Quero interpretar facilmente?
  ↓
Sim → Desvio padrão
Não → Variância
~~~

---

### 4.10 Conclusão da seção

A estatística descritiva é o alicerce da análise.  
Ela transforma dados brutos em informação estruturada, permitindo que você:

- entenda o comportamento geral  
- identifique padrões  
- detecte anomalias  
- prepare o terreno para análises mais avançadas  

</details>
<br>

## 5. Exemplos conceituais com código
<details>
<br>

Nesta seção, apresentamos exemplos **curtos, sintéticos e conceituais**, seguindo o padrão editorial do livro.

---

### 5.1 Criando um conjunto de dados sintético

~~~python
import pandas as pd

df = pd.DataFrame({
    "idade": [22, 35, 29, 41, 30, 28, 33, 27],
    "salario": [2500, 4800, 3200, 6100, 4000, 3900, 4500, 3100]
})
df
~~~

---

### 5.2 Calculando média, mediana e moda

~~~python
df["idade"].mean()
df["idade"].median()
df["idade"].mode()
~~~

---

### 5.3 Calculando variância e desvio padrão

~~~python
df["salario"].var()
df["salario"].std()
~~~

---

### 5.4 Estatísticas completas com describe()

~~~python
df.describe()
~~~

---

### 5.5 Exemplo 2D — relação entre idade e salário

~~~python
import matplotlib.pyplot as plt

plt.scatter(df["idade"], df["salario"])
plt.xlabel("Idade")
plt.ylabel("Salário")
plt.title("Relação entre idade e salário")
plt.show()
~~~

---

### 5.6 Script conceitual — interpretando a saída de describe()

~~~text
count → quantas observações existem
mean → valor médio
std → variabilidade
min → menor valor
25% → primeiro quartil
50% → mediana
75% → terceiro quartil
max → maior valor
~~~

---

### 5.7 Fluxograma — Como interpretar describe()

~~~text
describe()
  ↓
Verifique média
  ↓
Compare com mediana
  ↓
Se média ≠ mediana → distribuição assimétrica
  ↓
Observe std → variabilidade
  ↓
Observe min/max → extremos
  ↓
Observe quartis → caudas e dispersão
~~~

</details>
<br>

## 6. Integração com capítulos anteriores
<details>
<br>

A estatística descritiva se conecta diretamente ao Capítulo 1:

### ✔ Do Capítulo 1:
- aprendemos o papel da estatística  
- entendemos o fluxo geral da análise  
- vimos como Python será usado  

### ✔ Neste capítulo:
- aplicamos o primeiro passo concreto do fluxo  
- aprendemos a resumir dados  
- entendemos variabilidade e posição  

### ✔ Para o próximo capítulo (Visualização):
A estatística descritiva fornece:

- valores típicos  
- variabilidade  
- extremos  
- quartis  

Essas informações são essenciais para:

- escolher o gráfico correto  
- interpretar histogramas  
- entender boxplots  
- identificar outliers  

### Fluxograma — Conexão entre capítulos

~~~text
Capítulo 1 → Fundamentos
  ↓
Capítulo 2 → Estatística Descritiva
  ↓
Capítulo 3 → Visualização
  ↓
Capítulo 4 → Probabilidade
  ↓
Capítulo 5 → Testes de Hipótese
  ↓
Capítulo 6 → Regressão
~~~

</details>
<br>

## 7. Boas práticas e limitações
<details>
<br>

A estatística descritiva é poderosa, mas precisa ser usada com cuidado.  
Nesta seção, organizamos boas práticas, limitações, armadilhas e interpretações equivocadas — exatamente como um cientista de dados deve pensar.

---

### 7.1 Boas práticas

#### ✔ Sempre comece pela estatística descritiva  
Antes de qualquer gráfico, modelo ou teste, entenda:

- valores típicos  
- variabilidade  
- extremos  
- simetria  

#### ✔ Combine média + desvio padrão  
A média sozinha engana.  
O desvio padrão revela consistência.

#### ✔ Use mediana quando houver assimetria  
Distribuições com caudas longas (salários, preços, tempos de espera) são melhor representadas pela mediana.

#### ✔ Use moda para variáveis categóricas  
Moda é a única medida válida para categorias.

#### ✔ Sempre verifique outliers  
Eles distorcem:

- média  
- variância  
- desvio padrão  

#### ✔ Use quartis e IQR para entender caudas  
Especialmente útil em:

- finanças  
- saúde  
- tempos de processo  
- desempenho esportivo  

---

### 7.2 Limitações

#### ⚠ Estatística descritiva não identifica causalidade  
Ela descreve, não explica.

#### ⚠ Não detecta relações entre variáveis  
Para isso, precisamos de:

- correlação  
- regressão  
- visualização  

#### ⚠ Pode ser enganosa em distribuições multimodais  
Exemplo: duas populações diferentes misturadas.

#### ⚠ Média é sensível a outliers  
Um único valor extremo pode distorcer tudo.

#### ⚠ Variância e desvio padrão assumem distribuição razoavelmente simétrica  
Em distribuições muito assimétricas, prefira IQR.

---

### 7.3 Armadilhas comuns

#### ❗ Confiar apenas na média  
Exemplo clássico:  
Dois jogadores com mesma média, mas variabilidade completamente diferente.

#### ❗ Ignorar a forma da distribuição  
Média ≠ mediana → assimetria.

#### ❗ Usar média para variáveis categóricas  
Exemplo:  
“média do meio de transporte” → não faz sentido.

#### ❗ Interpretar amplitude como medida robusta  
Amplitude é extremamente sensível a outliers.

---

### 7.4 Interpretações equivocadas

#### ❌ “A média representa todo mundo”  
Não representa — é apenas um resumo.

#### ❌ “Desvio padrão alto é ruim”  
Depende do contexto.  
Em finanças, pode significar oportunidade.

#### ❌ “Moda é sempre útil”  
Moda só faz sentido para categorias ou distribuições discretas.

#### ❌ “Mediana ignora informação”  
Ela é robusta — isso é uma vantagem, não uma limitação.

---

### 7.5 Fluxograma — Evitando erros comuns

~~~text
Início
  ↓
Calcule média e mediana
  ↓
São muito diferentes?
  ↓
Sim → Distribuição assimétrica → Use mediana
Não → Distribuição simétrica → Use média
  ↓
Verifique desvio padrão
  ↓
Desvio padrão alto?
  ↓
Sim → Verifique outliers
Não → Dados consistentes
~~~

---

### 7.6 Árvore de decisão — Qual medida NÃO usar

~~~text
Variável categórica?
├── Sim → NÃO usar média, mediana, variância
└── Não → Continuar
      ├── Distribuição assimétrica? → NÃO usar média
      ├── Muitos outliers? → NÃO usar variância
      └── Dados multimodais? → NÃO usar média ou moda isoladamente
~~~

</details>
<br>

## 8. Glossário técnico
<details>
<br>

Aqui estão as definições essenciais para consulta rápida.

---

### 8.1 Tendência central

#### **Média**  
Soma dos valores dividida pelo número de observações.

#### **Mediana**  
Valor central quando os dados estão ordenados.

#### **Moda**  
Valor mais frequente.

---

### 8.2 Dispersão

#### **Variância**  
Média dos quadrados dos desvios em relação à média.

#### **Desvio padrão**  
Raiz quadrada da variância; mede variabilidade na mesma unidade da variável.

#### **Amplitude (range)**  
Diferença entre máximo e mínimo.

---

### 8.3 Posição

#### **Quartis**  
Dividem os dados em quatro partes iguais.

#### **Percentis**  
Dividem os dados em 100 partes iguais.

#### **IQR (Intervalo Interquartil)**  
Q3 – Q1; mede dispersão robusta.

---

### 8.4 Tipos de dados

#### **Nominal**  
Categorias sem ordem.

#### **Ordinal**  
Categorias com ordem.

#### **Intervalo**  
Números com distâncias significativas, sem zero absoluto.

#### **Razão (proporção)**  
Números com zero absoluto e proporções significativas.

---

### 8.5 População e amostra

#### **População**  
Conjunto completo de interesse.

#### **Amostra**  
Subconjunto da população.

#### **Estimador**  
Valor calculado na amostra usado para inferir sobre a população.

---

### 8.6 Fluxograma — Como navegar no glossário

~~~text
Preciso entender um conceito?
  ↓
É sobre resumo? → Tendência central
  ↓
É sobre variabilidade? → Dispersão
  ↓
É sobre posição relativa? → Quartis / Percentis
  ↓
É sobre tipo de dado? → Nominal / Ordinal / Intervalo / Razão
~~~

</details>
<br>

## 9. Referência rápida
<details>
<br>

Esta seção resume os pontos-chave do capítulo.

---

### 9.1 Tendência central

- Média → melhor para distribuições simétricas  
- Mediana → melhor para distribuições assimétricas  
- Moda → melhor para variáveis categóricas  

---

### 9.2 Dispersão

- Variância → medida quadrática  
- Desvio padrão → interpretação direta  
- Amplitude → sensível a outliers  
- IQR → robusto  

---

### 9.3 Tipos de dados

- Nominal → categorias  
- Ordinal → categorias ordenadas  
- Intervalo → sem zero absoluto  
- Razão → com zero absoluto  

---

### 9.4 Fluxograma — Resumo operacional

~~~text
1. Identifique o tipo de variável
2. Escolha a medida de tendência central adequada
3. Calcule dispersão (std, var, IQR)
4. Compare média vs mediana
5. Verifique outliers
6. Interprete padrões
7. Prepare-se para visualização
~~~

</details>
<br>

## 10. Conclusão do capítulo
<details>
<br>

A estatística descritiva é o primeiro passo concreto da análise estatística.  
Ela permite transformar dados brutos em informação estruturada, revelando:

- valores típicos  
- variabilidade  
- extremos  
- simetria ou assimetria  
- padrões gerais  

Com isso, você está preparado para:

- interpretar dados com precisão  
- identificar problemas  
- escolher técnicas adequadas  
- avançar para visualização e modelagem  

### 🔗 Preparação para o notebook

O notebook do módulo 2 permitirá:

- calcular estatísticas descritivas em Python  
- interpretar a saída de `describe()`  
- comparar média, mediana e moda  
- analisar variância e desvio padrão  
- explorar quartis e percentis  

### 🎯 Gancho para o próximo capítulo

O próximo capítulo abordará **visualização de dados**, onde você aprenderá a:

- transformar estatísticas em gráficos  
- interpretar histogramas, boxplots e scatterplots  
- detectar padrões visuais  
- comunicar resultados de forma clara  

A estatística descritiva fornece a base;  
a visualização transforma essa base em insight visual.

</details>
</details>
<br>

# Capítulo 3 — Visualização de Dados
<details>


## 1. Introdução
<details>
<br>

A visualização de dados é a ponte entre **estatística descritiva** e **interpretação humana**.  
Ela transforma números em formas, padrões e histórias que o cérebro entende instantaneamente.

No Módulo 3 do curso *IBM Statistics for Data Science with Python*, os instrutores mostram como:

- gráficos revelam padrões invisíveis em tabelas  
- diferentes tipos de variáveis exigem diferentes tipos de gráficos  
- a escolha correta da visualização determina a clareza da análise  
- Python (Matplotlib e Seaborn) permite criar visualizações profissionais  

### 🎯 Motivação

Visualizar dados é essencial para:

- detectar tendências  
- identificar outliers  
- comparar grupos  
- comunicar resultados  
- validar hipóteses  
- preparar análises mais avançadas  

### 🔗 Conexão com o capítulo anterior

No Capítulo 2, aprendemos:

- média, mediana, moda  
- variância, desvio padrão  
- quartis e percentis  

Agora, vamos **ver** esses conceitos ganharem forma:

- histogramas mostram distribuição  
- boxplots mostram quartis e IQR  
- scatterplots mostram relações  
- gráficos de barras mostram categorias  

### 🎥 Relação com o vídeo correspondente

O vídeo “Fundamentos de Visualização” apresenta:

- gráficos de barras feitos por crianças (exemplo simples e intuitivo)  
- o Método de Apresentação Extrema (Andrew Abela)  
- como escolher o gráfico certo para cada tipo de variável  
- como gráficos comunicam melhor que tabelas  

Este capítulo organiza tudo isso em uma estrutura clara e aplicável.

</details>
<br>

## 2. Revisão do fluxo anterior
<details>
<br>

No capítulo anterior, aprendemos a **resumir dados** com estatística descritiva.  
Agora, avançamos para a etapa seguinte do fluxo analítico:

~~~text
Dados brutos
  ↓
Estatística descritiva
  ↓
Visualização de dados
  ↓
Probabilidade
  ↓
Inferência estatística
  ↓
Modelagem
~~~

### Por que isso importa agora?

Porque a visualização:

- confirma padrões observados nas estatísticas  
- revela padrões que as estatísticas não mostram  
- permite comparar grupos rapidamente  
- ajuda a detectar erros e outliers  
- prepara o terreno para testes e modelos  

### Como o conteúdo se encaixa no curso

- Capítulo 1 → visão geral  
- Capítulo 2 → estatística descritiva  
- **Capítulo 3 → visualização (este capítulo)**  
- Capítulo 4 → distribuições  
- Capítulo 5 → testes de hipótese  
- Capítulo 6 → regressão  

A visualização é o elo entre **resumo numérico** e **interpretação visual**.

</details>
<br>

## 3. Apresentação do problema
<details>
<br>

A visualização de dados responde a perguntas que números sozinhos não conseguem responder:

### **1. Como os dados estão distribuídos?**
- histogramas  
- densidades  
- boxplots  

### **2. Como variáveis se relacionam?**
- scatterplots  
- gráficos de bolhas  
- matrizes de dispersão  

### **3. Como grupos se comparam?**
- gráficos de barras  
- gráficos de colunas  
- boxplots por categoria  

### **4. Como comunicar resultados de forma clara?**
- títulos  
- rótulos  
- legendas  
- cores  

### Exemplos reais do cotidiano

#### 🏫 Educação
- comparar desempenho entre turmas  
- visualizar notas ao longo do tempo  

#### 🏥 Saúde
- distribuição de idades de pacientes  
- relação entre idade e pressão arterial  

#### 🏠 Economia
- evolução de preços de imóveis  
- comparação de salários por setor  

#### 🚗 Transporte
- distribuição de tempos de viagem  
- relação entre velocidade e consumo  

#### 🎮 Esportes
- consistência de desempenho  
- comparação entre atletas  

---

### Fluxograma — Como escolher o gráfico correto

~~~text
Início
  ↓
Qual é o tipo de variável?
  ↓
Categórica? → Gráfico de barras / pizza
  ↓
Numérica?
  ↓
Quero ver distribuição? → Histograma / Boxplot
  ↓
Quero ver relação entre variáveis? → Scatterplot
  ↓
Quero comparar grupos? → Boxplot / Barras agrupadas
~~~

---

### Árvore de decisão — Escolha de visualização

~~~text
Visualização de Dados
├── Variável Categórica
│   ├── Barras
│   ├── Colunas
│   └── Pizza
├── Variável Numérica
│   ├── Histograma
│   ├── Boxplot
│   └── Densidade
└── Relação entre Variáveis
    ├── Scatterplot
    ├── Bubble Chart
    └── FacetGrid (subgrupos)
~~~

---

### Script conceitual — Processo mental do analista

~~~text
1. Identifique o tipo de variável
2. Determine o objetivo da visualização
3. Escolha o gráfico adequado
4. Adicione rótulos e título
5. Adicione cores e legendas
6. Verifique se o gráfico comunica claramente
7. Ajuste e refine
~~~

</details>
<br>

## 4. Conceito central
<details>
<br>

A visualização de dados é o processo de transformar números em formas visuais que revelam padrões, tendências e relações que seriam invisíveis em tabelas.  
Ela é a ferramenta que permite ao analista **ver** o comportamento dos dados.

---

### 4.1 Explicação intuitiva

Imagine tentar entender o trânsito de uma cidade olhando apenas para uma tabela com milhares de números representando velocidades.  
Agora imagine ver um mapa de calor mostrando congestionamentos em vermelho e vias livres em verde.

A diferença é imediata.

A visualização:

- reduz complexidade  
- revela padrões  
- facilita comparações  
- comunica ideias rapidamente  

---

### 4.2 Explicação formal

A visualização de dados é composta por três pilares:

#### **1. Representação gráfica**
Transformar dados em elementos visuais:

- pontos  
- barras  
- linhas  
- caixas  
- áreas  

#### **2. Codificação visual**
Usar atributos como:

- posição  
- cor  
- tamanho  
- forma  

#### **3. Interpretação**
Extrair significado:

- tendências  
- agrupamentos  
- outliers  
- relações  

---

### 4.3 O que a técnica resolve

- Identificação de padrões  
- Comparação entre grupos  
- Comunicação clara  
- Detecção de outliers  
- Exploração inicial dos dados  
- Validação de hipóteses  

---

### 4.4 O que a técnica NÃO resolve

- Não substitui estatística descritiva  
- Não garante causalidade  
- Não corrige dados ruins  
- Não substitui testes estatísticos  
- Não garante interpretação correta sem contexto  

---

### 4.5 Fluxograma conceitual — Como escolher o gráfico ideal

~~~text
Início
  ↓
Qual é o tipo de variável?
  ↓
Categórica?
  ↓
Sim → Barras / Colunas / Pizza
  ↓
Não → Numérica
  ↓
Quero ver distribuição?
  ↓
Sim → Histograma / Densidade / Boxplot
  ↓
Não → Quero ver relação entre variáveis?
  ↓
Sim → Scatterplot / Bubble Chart
  ↓
Não → Comparar grupos?
  ↓
Sim → Boxplot / Barras agrupadas
~~~

---

### 4.6 Árvore conceitual — Tipos de gráficos

~~~text
Visualização de Dados
├── Distribuição
│   ├── Histograma
│   ├── Densidade
│   └── Boxplot
├── Comparação
│   ├── Barras
│   ├── Colunas
│   └── Barras empilhadas
├── Relação
│   ├── Scatterplot
│   ├── Bubble Chart
│   └── FacetGrid
└── Composição
    ├── Pizza
    ├── Área empilhada
    └── Colunas empilhadas
~~~

---

### 4.7 Script conceitual — Processo mental do analista ao visualizar

~~~text
1. Identifique o tipo de variável (categórica ou numérica)
2. Determine o objetivo (comparar, distribuir, relacionar)
3. Escolha o gráfico adequado
4. Adicione rótulos, título e legenda
5. Ajuste cores e escalas
6. Verifique se o gráfico comunica claramente
7. Refine e interprete
~~~

---

### 4.8 Fluxograma — Gráfico de barras vs histograma

~~~text
Tenho categorias?
  ↓
Sim → Gráfico de barras
  ↓
Não → Tenho valores contínuos?
  ↓
Sim → Histograma
~~~

---

### 4.9 Conclusão da seção

A visualização é uma ferramenta de raciocínio estatístico.  
Ela não é apenas estética — é analítica.  
Ela permite ver padrões que números não mostram e prepara o terreno para análises mais profundas.

</details>
<br>

## 5. Exemplos conceituais com código
<details>
<br>

Nesta seção, apresentamos exemplos sintéticos e curtos, usando Python, Matplotlib e Seaborn — sempre com dados fictícios.

---

### 5.1 Criando um conjunto de dados sintético

~~~python
import pandas as pd

df = pd.DataFrame({
    "idade": [22, 35, 29, 41, 30, 28, 33, 27],
    "salario": [2500, 4800, 3200, 6100, 4000, 3900, 4500, 3100],
    "genero": ["F","M","F","M","F","F","M","M"]
})
df
~~~

---

### 5.2 Gráfico de barras — variável categórica

~~~python
import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x="genero", data=df)
plt.title("Distribuição por gênero")
plt.show()
~~~

---

### 5.3 Histograma — distribuição de variável numérica

~~~python
sns.histplot(df["idade"], bins=5, kde=True)
plt.title("Distribuição de idades")
plt.show()
~~~

---

### 5.4 Boxplot — quartis e IQR

~~~python
sns.boxplot(x="genero", y="salario", data=df)
plt.title("Salário por gênero")
plt.show()
~~~

---

### 5.5 Scatterplot — relação entre duas variáveis

~~~python
sns.scatterplot(x="idade", y="salario", hue="genero", data=df)
plt.title("Idade vs Salário")
plt.show()
~~~

---

### 5.6 FacetGrid — múltiplos gráficos por categoria

~~~python
g = sns.FacetGrid(df, col="genero")
g.map(sns.histplot, "idade")
~~~

---

### 5.7 Script conceitual — Como interpretar um histograma

~~~text
1. Observe o formato (simétrico? assimétrico?)
2. Observe o pico (moda)
3. Observe a dispersão (largura)
4. Observe caudas (extremos)
5. Compare com média e mediana
~~~

---

### 5.8 Fluxograma — Como interpretar um boxplot

~~~text
Boxplot
  ↓
Linha central → Mediana
  ↓
Caixa → IQR (Q1 a Q3)
  ↓
Extremos → Min e Max
  ↓
Pontos isolados → Outliers
~~~

</details>
<br>

## 6. Integração com capítulos anteriores
<details>
<br>

A visualização de dados se conecta diretamente ao que já aprendemos:

---

### 6.1 Como complementa o Capítulo 2

A estatística descritiva fornece:

- média  
- mediana  
- variância  
- quartis  
- IQR  

A visualização transforma esses valores em:

- histogramas  
- boxplots  
- densidades  

Ou seja:

> **O Capítulo 2 descreve.  
O Capítulo 3 mostra.**

---

### 6.2 Como prepara para o próximo módulo

O próximo capítulo aborda **distribuições de probabilidade**.  
A visualização é essencial para:

- comparar dados reais com distribuições teóricas  
- identificar normalidade  
- observar caudas e assimetrias  
- validar suposições  

---

### 6.3 Fluxograma — Conexão entre capítulos

~~~text
Capítulo 1 → Fundamentos
  ↓
Capítulo 2 → Estatística Descritiva
  ↓
Capítulo 3 → Visualização de Dados
  ↓
Capítulo 4 → Distribuições de Probabilidade
  ↓
Capítulo 5 → Testes de Hipótese
  ↓
Capítulo 6 → Regressão e Correlação
~~~

---

### 6.4 Árvore conceitual — O papel da visualização no processo estatístico

~~~text
Processo Estatístico
├── Coleta
├── Limpeza
├── Estatística Descritiva
├── Visualização
│   ├── Exploração
│   ├── Comunicação
│   └── Validação
└── Inferência
~~~

---

### 6.5 Script conceitual — Quando visualizar

~~~text
1. Antes da análise → Explorar
2. Durante a análise → Validar
3. Depois da análise → Comunicar
~~~

</details>
<br>

## 7. Boas práticas e limitações
<details>
<br>

A visualização de dados é uma ferramenta poderosa, mas precisa ser usada com rigor técnico e clareza comunicativa.  
Nesta seção, organizamos boas práticas, limitações, armadilhas e interpretações equivocadas — exatamente como um cientista de dados deve pensar.

---

### 7.1 Boas práticas

#### ✔ Escolha o gráfico adequado ao tipo de variável  
- Categórica → barras, colunas, pizza  
- Numérica → histograma, boxplot, densidade  
- Relação entre variáveis → scatterplot  

#### ✔ Sempre adicione título, rótulos e legenda  
Um gráfico sem rótulos é como um mapa sem nomes de ruas.

#### ✔ Use cores com propósito  
- Diferenciar grupos  
- Destacar categorias  
- Evitar excesso de cores  

#### ✔ Verifique se o gráfico comunica a mensagem  
Pergunte-se:  
> “Alguém que nunca viu os dados entenderia o que estou mostrando?”

#### ✔ Use FacetGrid para múltiplas dimensões  
Excelente para comparar subgrupos.

#### ✔ Combine estatística descritiva + visualização  
Exemplo:  
- média + histograma  
- quartis + boxplot  

---

### 7.2 Limitações

#### ⚠ Visualização não substitui estatística  
Um gráfico pode sugerir padrões, mas não confirma hipóteses.

#### ⚠ Pode induzir interpretações erradas  
Escalas mal escolhidas distorcem percepções.

#### ⚠ Gráficos de pizza são limitados  
Difíceis de comparar quando há muitas categorias.

#### ⚠ Scatterplots podem esconder padrões  
Quando há muitos pontos, ocorre overplotting.

#### ⚠ Visualização depende de contexto  
Sem explicação, o gráfico perde significado.

---

### 7.3 Armadilhas comuns

#### ❗ Usar gráfico de barras para dados contínuos  
Histograma é a escolha correta.

#### ❗ Usar pizza para muitas categorias  
Fica ilegível.

#### ❗ Não padronizar escalas ao comparar gráficos  
Pode induzir conclusões erradas.

#### ❗ Usar cores sem contraste  
Prejudica acessibilidade.

#### ❗ Interpretar correlação visual como causalidade  
Pontos próximos não significam causa.

---

### 7.4 Interpretações equivocadas

#### ❌ “O gráfico mostra a verdade”  
Gráficos mostram **representações**, não verdades absolutas.

#### ❌ “Se a linha sobe, algo melhorou”  
Depende da variável — pode ser custo, erro, risco.

#### ❌ “Dois grupos parecem diferentes, logo são diferentes”  
Diferença visual ≠ diferença estatística.

#### ❌ “Distribuição parece normal, então é normal”  
Apenas testes formais confirmam normalidade.

---

### 7.5 Fluxograma — Evitando erros comuns

~~~text
Início
  ↓
Escolhi o gráfico certo?
  ↓
Sim → Adicione rótulos e título
  ↓
Verifique escala e cores
  ↓
Compare com estatísticas descritivas
  ↓
O gráfico comunica claramente?
  ↓
Sim → Finalizar
Não → Ajustar e revisar
~~~

---

### 7.6 Árvore de decisão — O que NÃO fazer

~~~text
Visualização
├── Gráfico de barras
│   └── NÃO usar para dados contínuos
├── Pizza
│   └── NÃO usar com muitas categorias
├── Scatterplot
│   └── NÃO usar sem verificar overplotting
└── Boxplot
    └── NÃO usar sem explicar quartis e IQR
~~~

</details>
<br>

## 8. Glossário técnico
<details>
<br>

Aqui estão as definições essenciais para consulta rápida.

---

### 8.1 Tipos de gráficos

#### **Gráfico de barras**  
Compara categorias.

#### **Histograma**  
Mostra distribuição de dados contínuos.

#### **Boxplot**  
Mostra mediana, quartis e outliers.

#### **Scatterplot**  
Mostra relação entre duas variáveis numéricas.

#### **FacetGrid**  
Cria múltiplos gráficos para subgrupos.

#### **Gráfico de pizza**  
Mostra composição percentual.

---

### 8.2 Conceitos visuais

#### **Eixo X / Eixo Y**  
Dimensões principais do gráfico.

#### **Hue (cor)**  
Codificação visual para categorias.

#### **Bins**  
Número de divisões em um histograma.

#### **Outlier**  
Valor extremo fora do padrão.

---

### 8.3 Estatística aplicada à visualização

#### **Distribuição**  
Forma como os dados se espalham.

#### **Densidade**  
Estimativa suave da distribuição.

#### **Quartis**  
Divisões em quatro partes iguais.

#### **IQR**  
Intervalo entre Q1 e Q3.

---

### 8.4 Fluxograma — Como navegar no glossário

~~~text
Preciso entender um gráfico?
  ↓
É categórico? → Barras / Pizza
  ↓
É numérico? → Histograma / Boxplot
  ↓
É relação? → Scatterplot
~~~

</details>
<br>

## 9. Referência rápida
<details>
<br>

Esta seção resume os pontos-chave do capítulo.

---

### 9.1 Tipos de gráficos

- Barras → categorias  
- Histograma → distribuição  
- Boxplot → quartis e outliers  
- Scatterplot → relação  
- FacetGrid → múltiplas dimensões  

---

### 9.2 Boas práticas

- Adicione rótulos e título  
- Use cores com propósito  
- Escolha o gráfico certo  
- Compare com estatísticas descritivas  

---

### 9.3 Fluxograma — Resumo operacional

~~~text
1. Identifique o tipo de variável
2. Escolha o gráfico adequado
3. Adicione rótulos, título e legenda
4. Ajuste cores e escalas
5. Compare com estatísticas descritivas
6. Interprete padrões
7. Refine e comunique
~~~

</details>
<br>

## 10. Conclusão do capítulo
<details>
<br>

A visualização de dados é uma das ferramentas mais poderosas da análise estatística.  
Ela permite:

- ver padrões  
- comparar grupos  
- identificar outliers  
- comunicar resultados  
- validar hipóteses  

Combinada com estatística descritiva, ela forma a base da análise exploratória.

### 🔗 Preparação para o notebook

O notebook do módulo 3 permitirá:

- criar gráficos com Matplotlib e Seaborn  
- comparar categorias  
- visualizar distribuições  
- explorar relações entre variáveis  
- usar FacetGrid para múltiplas dimensões  

### 🎯 Gancho para o próximo capítulo

O próximo capítulo abordará **distribuições de probabilidade**, onde você aprenderá:

- como distribuições teóricas funcionam  
- como comparar dados reais com distribuições  
- como interpretar curvas, caudas e simetria  

A visualização é o elo entre dados brutos e compreensão estatística profunda.

</details>
</details>
<br>

# Capítulo 4 — Distribuições de Probabilidade
<details>

## 1. Introdução
<details>
<br>

As distribuições de probabilidade são o coração da estatística inferencial.  
Elas permitem responder perguntas como:

- “Qual é a chance de um evento ocorrer?”  
- “Quão raro é um valor observado?”  
- “Meus dados seguem um padrão conhecido?”  
- “Posso comparar minha amostra com uma população?”  

No Módulo 4 do curso *IBM Statistics for Data Science with Python*, os instrutores introduzem:

- variáveis aleatórias  
- espaço amostral  
- distribuições discretas e contínuas  
- distribuição normal  
- distribuição t de Student  
- probabilidade acumulada (CDF)  
- padronização (pontuação Z)  

Este capítulo organiza esses conceitos em uma estrutura clara, visual e aplicada.

### 🎯 Motivação

Distribuições de probabilidade são essenciais para:

- testes de hipótese  
- intervalos de confiança  
- regressão  
- machine learning  
- análise de risco  
- previsão  

Sem distribuições, não existe inferência estatística.

### 🔗 Conexão com o capítulo anterior

No Capítulo 3, aprendemos a visualizar dados.  
Agora, vamos entender **por que** certas formas aparecem nos gráficos:

- por que histogramas parecem sinos  
- por que algumas variáveis têm caudas longas  
- por que médias variam de amostra para amostra  

### 🎥 Relação com o vídeo correspondente

O vídeo “Números aleatórios e distribuições de probabilidade” mostra:

- como eventos aleatórios geram distribuições  
- o exemplo clássico dos dois dados (36 resultados possíveis)  
- como probabilidades se acumulam  
- como histogramas podem ser comparados com distribuições teóricas  

Este capítulo transforma essas ideias em raciocínio estatístico sólido.

</details>
<br>

## 2. Revisão do fluxo anterior
<details>
<br>

Até agora, construímos:

### ✔ Capítulo 1 — Fundamentos  
O que é estatística e por que ela importa.

### ✔ Capítulo 2 — Estatística descritiva  
Como resumir dados.

### ✔ Capítulo 3 — Visualização  
Como ver padrões.

Agora entramos na parte mais conceitual:

~~~text
Dados brutos
  ↓
Estatística descritiva
  ↓
Visualização
  ↓
Distribuições de probabilidade   ← (Capítulo atual)
  ↓
Testes de hipótese
  ↓
Regressão e correlação
~~~

### Por que isso importa agora?

Porque distribuições permitem:

- quantificar incerteza  
- calcular probabilidades  
- comparar amostras com populações  
- fundamentar testes estatísticos  

### Como o conteúdo se encaixa no curso

Este capítulo prepara você para:

- Capítulo 5: Testes de hipótese  
- Capítulo 6: Regressão e correlação  

Sem distribuições, não existe teste t, valor p, alfa, nem inferência.

</details>
<br>

## 3. Apresentação do problema
<details>
<br>

A estatística inferencial responde perguntas como:

- “Qual é a chance de observar esse valor?”  
- “Esse resultado é raro ou esperado?”  
- “Minha amostra representa a população?”  
- “A diferença entre grupos é significativa?”  

Para responder a essas perguntas, precisamos de **distribuições de probabilidade**.

### Exemplos reais do cotidiano

#### 🌧 Meteorologia  
- chance de chuva  
- chance de temperatura acima de 30°C  

#### 📈 Finanças  
- probabilidade de retorno negativo  
- risco (volatilidade)  

#### 🏥 Saúde  
- probabilidade de pressão arterial acima de certo valor  
- distribuição de idades de pacientes  

#### 🎮 Esportes  
- probabilidade de um jogador marcar acima da média  

#### 🎲 Jogos de azar  
- soma de dois dados  
- probabilidade de tirar um número específico  

---

### Fluxograma — Quando usar distribuições de probabilidade

~~~text
Início
  ↓
Tenho um evento incerto?
  ↓
Sim → Identificar espaço amostral
  ↓
Definir variável aleatória
  ↓
Escolher distribuição adequada
  ↓
Calcular probabilidades
  ↓
Interpretar resultados
~~~

---

### Árvore de decisão — Tipo de distribuição

~~~text
Distribuições de Probabilidade
├── Discretas
│   ├── Dois dados
│   ├── Bernoulli
│   ├── Binomial
│   └── Poisson
└── Contínuas
    ├── Normal
    ├── t de Student
    ├── Exponencial
    └── Uniforme
~~~

---

### Script conceitual — Processo mental do analista

~~~text
1. Identifique o evento aleatório
2. Liste todos os resultados possíveis (espaço amostral)
3. Defina a variável aleatória (X)
4. Determine se X é discreta ou contínua
5. Escolha a distribuição apropriada
6. Calcule probabilidades (PDF, PMF, CDF)
7. Compare com dados reais
~~~

---

### Exemplo intuitivo — Dois dados

- 36 resultados possíveis  
- cada resultado tem probabilidade 1/36  
- algumas somas são mais prováveis que outras  

Isso gera uma distribuição discreta em forma de pirâmide.

---

### Exemplo intuitivo — Idade de instrutores

- variável contínua  
- tende a se aproximar de uma curva suave  
- pode ser comparada com uma distribuição normal  

---

### Conclusão da seção

Distribuições de probabilidade são modelos matemáticos que descrevem como valores se comportam.  
Elas são a base para:

- testes estatísticos  
- valores p  
- intervalos de confiança  
- regressão  
- machine learning  

</details>
<br>

## 4. Conceito central
<details>
<br>

Distribuições de probabilidade descrevem **como valores possíveis de uma variável aleatória se comportam**.  
Elas são modelos matemáticos que permitem calcular probabilidades, comparar amostras e fundamentar testes estatísticos.

---

### 4.1 Explicação intuitiva

Imagine lançar dois dados.  
Você sabe intuitivamente que:

- somar **7** é mais provável  
- somar **2** ou **12** é raro  

Isso acontece porque **alguns resultados têm mais combinações possíveis**.

Agora imagine medir a **altura** de milhares de pessoas.  
Você verá uma curva suave, com:

- muitos valores perto da média  
- poucos valores muito baixos ou muito altos  

Essa forma é a **distribuição normal**.

Distribuições são **padrões de comportamento**.

---

### 4.2 Explicação formal

Uma distribuição de probabilidade é definida por:

- um **espaço amostral** (todos os resultados possíveis)  
- uma **variável aleatória** (X)  
- uma função que atribui probabilidades:

#### Para variáveis discretas:
- PMF (Probability Mass Function)

#### Para variáveis contínuas:
- PDF (Probability Density Function)
- CDF (Cumulative Distribution Function)

---

### 4.3 O que a técnica resolve

- Calcula probabilidades  
- Compara amostras com populações  
- Fundamenta testes estatísticos  
- Permite padronização (Z-score)  
- Permite estimar incerteza  

---

### 4.4 O que a técnica NÃO resolve

- Não garante causalidade  
- Não substitui análise exploratória  
- Não corrige dados ruins  
- Não garante normalidade dos dados  

---

### 4.5 Fluxograma — Como identificar a distribuição correta

~~~text
Início
  ↓
A variável é discreta?
  ↓
Sim → Binomial / Poisson / Dois dados
  ↓
Não → É contínua?
  ↓
Sim → Normal / t / Exponencial / Uniforme
~~~

---

### 4.6 Árvore conceitual — Estrutura das distribuições

~~~text
Distribuições
├── Discretas
│   ├── Bernoulli
│   ├── Binomial
│   ├── Poisson
│   └── Soma de dois dados
└── Contínuas
    ├── Normal
    ├── t de Student
    ├── Exponencial
    └── Uniforme
~~~

---

### 4.7 Script conceitual — Processo mental do analista

~~~text
1. Identifique o tipo de variável (discreta/contínua)
2. Liste todos os resultados possíveis
3. Determine se há simetria ou caudas longas
4. Compare com distribuições conhecidas
5. Escolha a distribuição apropriada
6. Calcule probabilidades (PMF, PDF, CDF)
7. Compare com dados reais
~~~

---

### 4.8 Conclusão da seção

Distribuições são modelos que descrevem incerteza.  
Elas são a base para:

- testes t  
- valores p  
- intervalos de confiança  
- regressão  
- machine learning  

</details>
<br>

## 5. Exemplos conceituais com código
<details>
<br>

Nesta seção, usamos **dados sintéticos** para ilustrar distribuições, sempre com código curto e conceitual.

---

### 5.1 Exemplo — Distribuição discreta (soma de dois dados)

~~~python
import itertools
import pandas as pd

# todos os pares possíveis
dados = list(itertools.product([1,2,3,4,5,6], repeat=2))

# soma de cada par
somas = [x+y for x,y in dados]

pd.Series(somas).value_counts().sort_index()
~~~

---

### 5.2 Exemplo — Histograma da soma dos dados

~~~python
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(somas, bins=11)
plt.title("Distribuição da soma de dois dados")
plt.show()
~~~

---

### 5.3 Exemplo — Distribuição normal teórica

~~~python
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 200)
y = norm.pdf(x, 0, 1)

plt.plot(x, y)
plt.title("Distribuição Normal Padrão")
plt.show()
~~~

---

### 5.4 Exemplo — Padronização (Z-score)

~~~python
import numpy as np

x = 4.5
mu = 3.998
sigma = 0.554

z = (x - mu) / sigma
z
~~~

---

### 5.5 Exemplo — Probabilidade acumulada (CDF)

~~~python
from scipy.stats import norm

# probabilidade de obter valor <= 4.5
norm.cdf(4.5, loc=mu, scale=sigma)
~~~

---

### 5.6 Exemplo — Probabilidade de valor maior que 4.5

~~~python
1 - norm.cdf(4.5, loc=mu, scale=sigma)
~~~

---

### 5.7 Script conceitual — Como interpretar um Z-score

~~~text
Z = 0 → valor igual à média
Z = 1 → 1 desvio padrão acima da média
Z = -1 → 1 desvio padrão abaixo da média
Z > 2 → valor raro
Z > 3 → valor muito raro
~~~

---

### 5.8 Fluxograma — Como calcular probabilidade com distribuição normal

~~~text
Valor X
  ↓
Padronizar → Z = (X - μ) / σ
  ↓
Consultar tabela Z ou usar CDF
  ↓
Obter probabilidade acumulada
  ↓
Interpretar resultado
~~~

</details>
<br>

## 6. Integração com capítulos anteriores
<details>
<br>

Distribuições de probabilidade conectam tudo o que aprendemos até agora.

---

### 6.1 Como complementa o Capítulo 2 (Estatística Descritiva)

- média → parâmetro da normal  
- desvio padrão → parâmetro da normal  
- quartis → usados na CDF  
- variância → usada na padronização  

---

### 6.2 Como complementa o Capítulo 3 (Visualização)

- histogramas revelam forma da distribuição  
- curvas teóricas podem ser sobrepostas  
- boxplots mostram caudas e assimetria  

---

### 6.3 Como prepara para o Capítulo 5 (Testes de Hipótese)

Distribuições são essenciais para:

- valor p  
- estatística t  
- regiões de rejeição  
- alfa (nível de significância)  

---

### 6.4 Fluxograma — Conexão entre capítulos

~~~text
Capítulo 1 → Fundamentos
  ↓
Capítulo 2 → Estatística Descritiva
  ↓
Capítulo 3 → Visualização
  ↓
Capítulo 4 → Distribuições de Probabilidade
  ↓
Capítulo 5 → Testes de Hipótese
  ↓
Capítulo 6 → Regressão e Correlação
~~~

---

### 6.5 Árvore conceitual — O papel das distribuições

~~~text
Inferência Estatística
├── Distribuições
│   ├── Normal
│   ├── t
│   ├── Binomial
│   └── Poisson
├── Testes de Hipótese
│   ├── valor p
│   ├── alfa
│   └── estatística t
└── Modelos
    ├── Regressão
    └── Correlação
~~~

</details>
<br>

## 7. Boas práticas e limitações
<details>
<br>

Distribuições de probabilidade são ferramentas poderosas, mas exigem cuidado técnico e interpretação criteriosa.  
Aqui organizamos boas práticas, limitações, armadilhas e interpretações equivocadas — exatamente como um cientista de dados deve pensar.

---

### 7.1 Boas práticas

#### ✔ Verifique se a variável é discreta ou contínua  
A escolha da distribuição depende disso.

#### ✔ Compare dados reais com distribuições teóricas  
Use histogramas + curvas teóricas (normal, t, etc.).

#### ✔ Padronize valores quando necessário  
Z-scores facilitam comparações entre variáveis diferentes.

#### ✔ Use CDF para interpretar probabilidades acumuladas  
Especialmente útil para perguntas do tipo “≤ X”.

#### ✔ Use tabelas Z apenas para valores padronizados  
Nunca use tabelas Z com valores brutos.

#### ✔ Sempre interprete probabilidades no contexto  
Uma probabilidade de 20% pode ser alta ou baixa dependendo do problema.

---

### 7.2 Limitações

#### ⚠ Nem todos os dados seguem uma distribuição conhecida  
Muitos fenômenos reais são assimétricos ou multimodais.

#### ⚠ Normalidade não pode ser assumida automaticamente  
É comum, mas não garantido.

#### ⚠ Distribuições teóricas são modelos, não verdades absolutas  
Elas aproximam o comportamento real.

#### ⚠ Pequenas amostras podem distorcer estimativas  
Por isso existe a distribuição t.

#### ⚠ Probabilidades não garantem resultados individuais  
Elas descrevem comportamento agregado.

---

### 7.3 Armadilhas comuns

#### ❗ Assumir normalidade sem verificar  
Histograma e Q-Q plot ajudam a validar.

#### ❗ Usar média e desvio padrão em distribuições assimétricas  
Mediana e IQR podem ser melhores.

#### ❗ Interpretar probabilidade acumulada como probabilidade pontual  
CDF ≠ PDF.

#### ❗ Usar tabela Z com valores não padronizados  
Erro clássico.

#### ❗ Confundir probabilidade com frequência observada  
Probabilidade é teórica; frequência é empírica.

---

### 7.4 Interpretações equivocadas

#### ❌ “Se a probabilidade é baixa, o evento não ocorre”  
Eventos raros acontecem — e são importantes.

#### ❌ “Se a probabilidade é alta, o evento é garantido”  
Probabilidade ≠ certeza.

#### ❌ “Distribuição normal significa dados perfeitos”  
Normalidade é apenas um modelo.

#### ❌ “Valor p é a probabilidade da hipótese ser verdadeira”  
Valor p NÃO mede isso.

---

### 7.5 Fluxograma — Evitando erros comuns

~~~text
Início
  ↓
A variável é contínua?
  ↓
Sim → Verificar forma da distribuição
  ↓
Parece normal?
  ↓
Sim → Usar média, desvio padrão, Z-score
Não → Usar mediana, IQR, distribuições alternativas
  ↓
Calcular probabilidades com CDF
  ↓
Interpretar no contexto
~~~

---

### 7.6 Árvore de decisão — O que NÃO fazer

~~~text
Distribuições
├── Normal
│   └── NÃO assumir sem verificar
├── t de Student
│   └── NÃO usar com amostras enormes (normal é suficiente)
├── Tabela Z
│   └── NÃO usar sem padronizar
└── Probabilidades
    └── NÃO confundir CDF com PDF
~~~

</details>
<br>

## 8. Glossário técnico
<details>
<br>

Aqui estão as definições essenciais para consulta rápida.

---

### 8.1 Conceitos fundamentais

#### **Probabilidade**  
Medida entre 0 e 1 que indica a chance de um evento ocorrer.

#### **Variável aleatória (X)**  
Função que atribui valores numéricos a eventos aleatórios.

#### **Espaço amostral (Ω)**  
Conjunto de todos os resultados possíveis.

---

### 8.2 Funções de probabilidade

#### **PMF (Probability Mass Function)**  
Usada para variáveis discretas.

#### **PDF (Probability Density Function)**  
Usada para variáveis contínuas.

#### **CDF (Cumulative Distribution Function)**  
Probabilidade acumulada: P(X ≤ x).

---

### 8.3 Distribuições importantes

#### **Normal**  
Simétrica, em forma de sino, definida por média e desvio padrão.

#### **Normal padrão**  
Média 0, desvio padrão 1.

#### **t de Student**  
Semelhante à normal, mas com caudas mais largas; usada para amostras pequenas.

#### **Binomial**  
Número de sucessos em n tentativas.

#### **Poisson**  
Número de eventos raros em um intervalo.

---

### 8.4 Padronização

#### **Z-score**  
Z = (X − μ) / σ  
Transforma qualquer valor em unidades de desvio padrão.

---

### 8.5 Alfa e valor p

#### **Alfa (α)**  
Nível de significância; probabilidade de rejeitar H0 quando ela é verdadeira.

#### **Valor p**  
Probabilidade de observar um valor tão extremo quanto o observado, assumindo H0 verdadeira.

---

### 8.6 Fluxograma — Como navegar no glossário

~~~text
Preciso entender probabilidade?
  ↓
É sobre valores individuais? → PDF/PMF
  ↓
É sobre valores acumulados? → CDF
  ↓
É sobre padronização? → Z-score
  ↓
É sobre testes? → Alfa e valor p
~~~

</details>
<br>

## 9. Referência rápida
<details>
<br>

Esta seção resume os pontos-chave do capítulo.

---

### 9.1 Conceitos essenciais

- Probabilidade → 0 a 1  
- Variável aleatória → discreta ou contínua  
- Distribuição → modelo teórico  
- Normal → média + desvio padrão  
- t de Student → amostras pequenas  

---

### 9.2 Fórmulas importantes

#### Z-score  
Z = (X − μ) / σ

#### Probabilidade acumulada  
P(X ≤ x) = CDF(x)

#### Probabilidade complementar  
P(X > x) = 1 − CDF(x)

---

### 9.3 Fluxograma — Resumo operacional

~~~text
1. Identifique o tipo de variável
2. Escolha a distribuição adequada
3. Padronize se necessário (Z-score)
4. Use CDF para probabilidades acumuladas
5. Compare com dados reais
6. Interprete no contexto
~~~

</details>
<br>

## 10. Conclusão do capítulo
<details>
<br>

Distribuições de probabilidade são o alicerce da inferência estatística.  
Elas permitem:

- quantificar incerteza  
- calcular probabilidades  
- comparar amostras com populações  
- fundamentar testes estatísticos  
- interpretar valores extremos  

Com elas, passamos de **descrição** para **inferência**.

### 🔗 Preparação para o notebook

O notebook do módulo 4 permitirá:

- gerar distribuições teóricas  
- comparar dados reais com curvas normais  
- calcular probabilidades com CDF  
- padronizar valores (Z-score)  
- usar SciPy para PDF e CDF  

### 🎯 Gancho para o próximo capítulo

O próximo capítulo aborda **testes de hipótese**, onde você aprenderá:

- como usar alfa  
- como interpretar valor p  
- como usar a distribuição t  
- como comparar médias  
- como tomar decisões estatísticas  

As distribuições são a base para tudo isso.

</details>
</details>
<br>

# Capítulo 5 — Testes de Hipóteses
<details>


## 1. Introdução
<details>
<br>

Testes de hipótese são o mecanismo formal da estatística para responder perguntas como:

- “Existe diferença entre dois grupos?”  
- “Essa diferença é real ou apenas fruto do acaso?”  
- “A média observada é compatível com a média populacional?”  
- “Existe relação entre duas variáveis?”  

No Módulo 5 do curso *IBM Statistics for Data Science with Python*, os instrutores apresentam:

- teste z  
- teste t  
- testes bicaudais e unicaudais  
- regiões de rejeição  
- alfa (nível de significância)  
- valor p  
- variâncias iguais vs desiguais  
- ANOVA  
- testes de correlação (Pearson e Qui-quadrado)  

Este capítulo organiza tudo isso em uma estrutura clara, visual e matemática.

### 🎯 Motivação

Testes de hipótese permitem:

- tomar decisões baseadas em dados  
- avaliar diferenças entre grupos  
- validar modelos  
- medir significância estatística  
- evitar conclusões equivocadas  

### 🔗 Conexão com o capítulo anterior

No Capítulo 4 aprendemos:

- distribuições normal e t  
- Z-score  
- probabilidade acumulada (CDF)  
- regiões de cauda  

Agora aplicamos esses conceitos para **tomar decisões estatísticas**.

### 🎥 Relação com o vídeo correspondente

O vídeo “Teste z ou teste t” mostra:

- quando usar z  
- quando usar t  
- como interpretar regiões de rejeição  
- como comparar médias  

Este capítulo transforma essas ideias em raciocínio estatístico sólido.

</details>
<br>

## 2. Revisão do fluxo anterior
<details>
<br>

Até agora, construímos:

### ✔ Capítulo 1 — Fundamentos  
### ✔ Capítulo 2 — Estatística descritiva  
### ✔ Capítulo 3 — Visualização  
### ✔ Capítulo 4 — Distribuições de probabilidade  

Agora entramos na etapa central da inferência:

~~~text
Dados brutos
  ↓
Estatística descritiva
  ↓
Visualização
  ↓
Distribuições de probabilidade
  ↓
Testes de hipótese   ← (Capítulo atual)
  ↓
Regressão e correlação
~~~

### Por que isso importa agora?

Porque testes de hipótese permitem:

- comparar grupos  
- validar diferenças  
- medir significância  
- fundamentar decisões  

### Como o conteúdo se encaixa no curso

Este capítulo prepara você para:

- regressão  
- correlação  
- análise multivariada  
- projeto final  

</details>
<br>

## 3. Apresentação do problema
<details>
<br>

Testes de hipótese respondem perguntas como:

- “A média de um grupo é igual à média de outro?”  
- “Existe diferença significativa entre homens e mulheres?”  
- “A idade influencia a avaliação de ensino?”  
- “A beleza está associada à nota do instrutor?”  
- “Três grupos têm médias iguais?”  

Essas perguntas aparecem em:

### 🏥 Saúde  
- eficácia de tratamentos  
- comparação de grupos de pacientes  

### 📈 Negócios  
- impacto de campanhas  
- comparação de vendas  

### 🎮 Esportes  
- diferença entre atletas  
- desempenho médio  

### 🏫 Educação  
- diferença entre turmas  
- impacto de metodologias  

---

### Fluxograma — Quando usar testes de hipótese

~~~text
Início
  ↓
Quero comparar médias?
  ↓
Sim → Teste t ou z
  ↓
Quero comparar mais de dois grupos?
  ↓
Sim → ANOVA
  ↓
Quero testar relação entre variáveis?
  ↓
Variáveis categóricas → Qui-quadrado
Variáveis contínuas → Correlação de Pearson
~~~

---

### Árvore de decisão — Tipo de teste

~~~text
Testes de Hipótese
├── Comparação de médias
│   ├── Teste z (σ conhecido)
│   └── Teste t (σ desconhecido)
├── Mais de dois grupos
│   └── ANOVA (F)
└── Associação entre variáveis
    ├── Categóricas → Qui-quadrado
    └── Contínuas → Pearson
~~~

---

### Script conceitual — Processo mental do analista

~~~text
1. Declare a hipótese nula (H₀)
2. Declare a hipótese alternativa (H₁)
3. Escolha o teste adequado
4. Defina o nível de significância (α)
5. Calcule a estatística do teste
6. Calcule o valor p
7. Compare valor p com α
8. Decida: rejeitar ou não rejeitar H₀
9. Interprete no contexto
~~~

---

### Fórmulas fundamentais

### Hipótese nula e alternativa

\[
H_0: \mu_1 = \mu_2
\]


\[
H_1: \mu_1 \neq \mu_2
\]


### Estatística z

\[
z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}
\]


### Estatística t

\[
t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}
\]


### Diferença entre duas médias (variâncias iguais)

\[
t = \frac{\bar{x}_1 - \bar{x}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}
\]


\[
s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}
\]

---

### Conclusão da seção

Testes de hipótese são o mecanismo formal para transformar dados em decisões.  
Eles unem:

- distribuições  
- probabilidade  
- estatística descritiva  

…em um processo estruturado de inferência.

</details>
<br>

## 4. Conceito central
<details>
<br>

Testes de hipótese são o mecanismo formal da estatística para decidir, com base em dados, se uma afirmação deve ser rejeitada ou não.  
Eles combinam:

- distribuições de probabilidade  
- estatísticas de teste  
- regiões de rejeição  
- valor p  
- nível de significância (α)  

O objetivo é avaliar se um resultado observado é compatível com o acaso ou se indica uma diferença real.

---

### 4.1 Estrutura matemática de um teste de hipótese

Todo teste segue esta estrutura:

#### **1. Definir hipóteses**

\[
H_0: \text{hipótese nula (não há efeito/diferença)}
\]


\[
H_1: \text{hipótese alternativa (há efeito/diferença)}
\]


#### **2. Escolher o teste adequado**

- z → σ conhecido  
- t → σ desconhecido  
- t para duas amostras  
- ANOVA para mais de dois grupos  
- Qui-quadrado para variáveis categóricas  
- Pearson para variáveis contínuas  

#### **3. Definir nível de significância**


\[
\alpha = 0.05 \quad \text{(mais comum)}
\]


#### **4. Calcular estatística de teste**

Exemplo para teste t de uma amostra:


\[
t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}
\]


#### **5. Calcular valor p**

\[
p = P(|T| \geq |t_{\text{obs}}|)
\]


#### **6. Tomar decisão**

- Se \( p < \alpha \) → rejeitar \(H_0\)  
- Se \( p \geq \alpha \) → não rejeitar \(H_0\)

---

### 4.2 Teste z vs teste t

#### **Teste z (σ conhecido)**

\[
z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}
\]


#### **Teste t (σ desconhecido)**

\[
t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}
\]


#### Quando usar cada um?

~~~text
σ conhecido → Teste z
σ desconhecido → Teste t
Duas amostras → Teste t
Mais de dois grupos → ANOVA
~~~

---

### 4.3 Testes bicaudais e unicaudais

#### **Bicaudal**

\[
H_1: \mu_1 \neq \mu_2
\]

Região de rejeição:

\[
|z| > 1.96 \quad (\alpha = 0.05)
\]


#### **Unicaudal (direita)**

\[
H_1: \mu_1 > \mu_2
\]

Região:

\[
z > 1.64
\]

#### **Unicaudal (esquerda)**

\[
H_1: \mu_1 < \mu_2
\]

Região:

\[
z < -1.64
\]

---

### 4.4 Fluxograma — Como escolher o teste correto

~~~text
Início
  ↓
Comparar média com valor fixo?
  ↓
σ conhecido → Teste z
σ desconhecido → Teste t (1 amostra)
  ↓
Comparar duas médias?
  ↓
Amostras independentes → Teste t independente
Amostras pareadas → Teste t pareado
  ↓
Mais de dois grupos?
  ↓
Sim → ANOVA
  ↓
Variáveis categóricas?
  ↓
Sim → Qui-quadrado
  ↓
Variáveis contínuas?
  ↓
Sim → Correlação de Pearson
~~~

---

### 4.5 Árvore conceitual — Estrutura dos testes

~~~text
Testes de Hipótese
├── 1 amostra
│   ├── z (σ conhecido)
│   └── t (σ desconhecido)
├── 2 amostras
│   ├── t independente
│   └── t pareado
├── > 2 grupos
│   └── ANOVA (F)
└── Associação
    ├── Qui-quadrado (categóricas)
    └── Pearson (contínuas)
~~~

---

### 4.6 Script conceitual — Processo mental do analista

~~~text
1. Qual é a pergunta?
2. Qual é a variável?
3. Quantos grupos?
4. As variâncias são iguais?
5. A distribuição é normal?
6. Escolher teste adequado
7. Calcular estatística
8. Calcular valor p
9. Comparar com α
10. Interpretar no contexto
~~~

</details>
<br>

## 5. Exemplos conceituais com código
<details>
<br>

Nesta seção, usamos **dados sintéticos** para ilustrar testes de hipótese.

---

### 5.1 Teste t de uma amostra

~~~python
import numpy as np
from scipy.stats import ttest_1samp

dados = np.array([4.1, 3.9, 4.3, 4.0, 4.2])
t, p = ttest_1samp(dados, 4.0)
t, p
~~~

---

### 5.2 Teste t para duas amostras independentes

~~~python
from scipy.stats import ttest_ind

grupo_A = np.array([4.1, 4.0, 4.2, 4.3])
grupo_B = np.array([3.8, 3.9, 4.0, 3.7])

t, p = ttest_ind(grupo_A, grupo_B)
t, p
~~~

---

### 5.3 Teste de variâncias iguais (Levene)

~~~python
from scipy.stats import levene

stat, p = levene(grupo_A, grupo_B)
stat, p
~~~

---

### 5.4 ANOVA (3 grupos)

~~~python
from scipy.stats import f_oneway

g1 = [4.0, 4.1, 4.2]
g2 = [3.9, 4.0, 3.8]
g3 = [3.7, 3.8, 3.9]

F, p = f_oneway(g1, g2, g3)
F, p
~~~

---

### 5.5 Qui-quadrado para variáveis categóricas

~~~python
import pandas as pd
from scipy.stats import chi2_contingency

tabela = pd.DataFrame({
    "Feminino": [50, 145],
    "Masculino": [52, 216]
}, index=["Não Titular", "Titular"])

chi2, p, dof, expected = chi2_contingency(tabela)
chi2, p
~~~

---

### 5.6 Correlação de Pearson

~~~python
from scipy.stats import pearsonr

beleza = np.array([0.1, -0.2, 0.3, 0.0, 0.2])
avaliacao = np.array([4.0, 3.8, 4.3, 4.1, 4.2])

r, p = pearsonr(beleza, avaliacao)
r, p
~~~

---

### 5.7 Fórmulas matemáticas importantes

#### Estatística t (duas amostras, variâncias iguais)

\[
t = \frac{\bar{x}_1 - \bar{x}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}
\]

\[
s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}
\]


#### Estatística F (ANOVA)

\[
F = \frac{\text{Variância entre grupos}}{\text{Variância dentro dos grupos}}
\]

#### Qui-quadrado

\[
\chi^2 = \sum \frac{(O - E)^2}{E}
\]

#### Correlação de Pearson

\[
r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}
\]

---

### 5.8 Fluxograma — Como interpretar valor p

~~~text
Valor p < α → Rejeitar H₀
Valor p ≥ α → Não rejeitar H₀
~~~

</details>
<br>

## 6. Integração com capítulos anteriores
<details>
<br>

Testes de hipótese unem tudo o que aprendemos até agora.

---

### 6.1 Conexão com o Capítulo 2 (Estatística Descritiva)

- média → usada na estatística t  
- desvio padrão → usado em z e t  
- variância → usada em ANOVA  

---

### 6.2 Conexão com o Capítulo 3 (Visualização)

- boxplots ajudam a visualizar diferenças  
- histogramas mostram forma da distribuição  
- scatterplots mostram relações  

---

### 6.3 Conexão com o Capítulo 4 (Distribuições)

- testes t usam distribuição t  
- testes z usam distribuição normal  
- valor p vem da CDF dessas distribuições  

---

### 6.4 Fluxograma — Conexão entre capítulos

~~~text
Capítulo 1 → Fundamentos
  ↓
Capítulo 2 → Estatística Descritiva
  ↓
Capítulo 3 → Visualização
  ↓
Capítulo 4 → Distribuições de Probabilidade
  ↓
Capítulo 5 → Testes de Hipótese
  ↓
Capítulo 6 → Regressão e Correlação
~~~

---

### 6.5 Script conceitual — O papel dos testes

~~~text
1. Descrever → Capítulo 2
2. Visualizar → Capítulo 3
3. Modelar distribuições → Capítulo 4
4. Testar hipóteses → Capítulo 5
5. Modelar relações → Capítulo 6
~~~

</details>
<br>

## 7. Boas práticas e limitações
<details>
<br>

Testes de hipótese são extremamente poderosos, mas também são uma das áreas mais mal interpretadas da estatística.  
Aqui organizamos boas práticas, limitações, armadilhas e interpretações equivocadas — exatamente como um cientista de dados deve pensar.

---

### 7.1 Boas práticas

#### ✔ Sempre declare H₀ e H₁ antes de olhar os dados  
Evita viés de confirmação.

\[
H_0: \mu_1 = \mu_2
\qquad
H_1: \mu_1 \neq \mu_2
\]

#### ✔ Escolha o teste adequado ao tipo de variável  
- médias → t ou z  
- mais de dois grupos → ANOVA  
- categóricas → Qui-quadrado  
- contínuas → Pearson  

#### ✔ Defina α antes de calcular o valor p  
Evita manipulação posterior.

#### ✔ Verifique suposições do teste  
- normalidade  
- independência  
- homogeneidade de variâncias  

#### ✔ Use gráficos para validar resultados  
- boxplots  
- histogramas  
- scatterplots  

#### ✔ Interprete resultados no contexto  
Significância estatística ≠ significância prática.

---

### 7.2 Limitações

#### ⚠ Testes de hipótese não provam nada  
Eles apenas rejeitam ou não rejeitam H₀.

#### ⚠ Valor p não mede magnitude do efeito  
Ele mede compatibilidade com H₀.

#### ⚠ Testes t assumem normalidade  
Para amostras pequenas, isso é crítico.

#### ⚠ ANOVA não diz *qual* grupo difere  
Apenas que *algum* grupo difere.

#### ⚠ Qui-quadrado exige contagens mínimas  
Células com valores muito baixos invalidam o teste.

---

### 7.3 Armadilhas comuns

#### ❗ Confundir “não rejeitar H₀” com “aceitar H₀”  
Não rejeitar ≠ aceitar.

#### ❗ Usar teste t com variâncias desiguais sem verificar  
Use o teste de Levene:

\[
H_0: \sigma_1^2 = \sigma_2^2
\]

#### ❗ Usar teste z quando σ é desconhecido  
Erro clássico.

#### ❗ Interpretar valor p como probabilidade de H₀ ser verdadeira  
Valor p NÃO mede isso.

#### ❗ Fazer múltiplos testes sem correção  
Aumenta falsos positivos.

---

### 7.4 Interpretações equivocadas

#### ❌ “p < 0.05 significa que o efeito é grande”  
Não necessariamente.

#### ❌ “p > 0.05 significa que não há efeito”  
Pode haver efeito, mas a amostra é pequena.

#### ❌ “ANOVA mostra qual grupo é maior”  
ANOVA apenas detecta diferença global.

#### ❌ “Correlação implica causalidade”  
Nunca.

---

### 7.5 Fluxograma — Evitando erros comuns

~~~text
Início
  ↓
Declare H₀ e H₁
  ↓
Escolha o teste adequado
  ↓
Verifique suposições (normalidade, variâncias)
  ↓
Calcule estatística e valor p
  ↓
p < α?
  ↓
Sim → Rejeitar H₀
Não → Não rejeitar H₀
  ↓
Interpretar no contexto
~~~

---

### 7.6 Árvore de decisão — O que NÃO fazer

~~~text
Testes de Hipótese
├── Valor p
│   └── NÃO interpretar como probabilidade de H₀
├── Teste t
│   └── NÃO usar sem verificar variâncias
├── ANOVA
│   └── NÃO concluir qual grupo difere sem pós-teste
└── Qui-quadrado
    └── NÃO usar com contagens muito pequenas
~~~

</details>
<br>

## 8. Glossário técnico
<details>
<br>

Aqui estão as definições essenciais para consulta rápida.

---

### 8.1 Conceitos fundamentais

#### **Hipótese nula (H₀)**  
Afirmação de ausência de efeito.

#### **Hipótese alternativa (H₁)**  
Afirmação de presença de efeito.

#### **Nível de significância (α)**  
Probabilidade de rejeitar H₀ quando ela é verdadeira.

#### **Valor p**  
Probabilidade de observar um resultado tão extremo quanto o observado, assumindo H₀ verdadeira.

---

### 8.2 Estatísticas de teste

#### **Estatística z**

\[
z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}
\]

#### **Estatística t**

\[
t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}
\]

#### **Estatística F (ANOVA)**

\[
F = \frac{\text{Variância entre grupos}}{\text{Variância dentro dos grupos}}
\]

#### **Qui-quadrado**

\[
\chi^2 = \sum \frac{(O - E)^2}{E}
\]

---

### 8.3 Correlação

#### **Correlação de Pearson**

\[
r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}
\]

---

### 8.4 Variâncias iguais vs desiguais

#### **Variância combinada (pooled)**

\[
s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}
\]

#### **Teste de Levene**

\[
H_0: \sigma_1^2 = \sigma_2^2
\]

---

### 8.5 Fluxograma — Como navegar no glossário

~~~text
Preciso entender:
  ↓
Médias? → t ou z
  ↓
Mais de dois grupos? → ANOVA
  ↓
Categóricas? → Qui-quadrado
  ↓
Relação contínua? → Pearson
~~~

</details>
<br>

## 9. Referência rápida
<details>
<br>

Esta seção resume os pontos-chave do capítulo.

---

### 9.1 Estrutura do teste de hipótese

\[
H_0, H_1, \alpha, \text{estatística}, p, \text{decisão}
\]

---

### 9.2 Valores críticos importantes

#### **Bicaudal (α = 0.05)**  

\[
|z| > 1.96
\]

#### **Unicaudal (α = 0.05)**  

\[
z > 1.64
\]

---

### 9.3 Testes principais

- Teste z → σ conhecido  
- Teste t → σ desconhecido  
- Teste t independente → duas amostras  
- ANOVA → mais de dois grupos  
- Qui-quadrado → categóricas  
- Pearson → contínuas  

---

### 9.4 Fluxograma — Resumo operacional

~~~text
1. Declare H₀ e H₁
2. Escolha o teste adequado
3. Defina α
4. Calcule estatística
5. Calcule valor p
6. Compare p com α
7. Decida
8. Interprete
~~~

</details>
<br>

## 10. Conclusão do capítulo
<details>
<br>

Testes de hipótese são o mecanismo central da inferência estatística.  
Eles permitem transformar dados em decisões, avaliando se diferenças observadas são reais ou fruto do acaso.

Com eles, você pode:

- comparar médias  
- avaliar relações  
- testar associações  
- validar modelos  
- fundamentar conclusões  

### 🔗 Preparação para o notebook

O notebook do módulo 5 permitirá:

- executar testes t e z  
- comparar médias  
- realizar ANOVA  
- aplicar Qui-quadrado  
- calcular correlação de Pearson  
- interpretar valor p e estatísticas de teste  

### 🎯 Gancho para o próximo capítulo

O próximo capítulo aborda **regressão e correlação**, onde você aprenderá:

- como modelar relações entre variáveis  
- como interpretar coeficientes  
- como avaliar força e direção de relações  
- como usar regressão linear em Python  

Testes de hipótese são a base para tudo isso.

</details>
</details>
<br>

# Capítulo 6 — Análise de Regressão

## 1. Introdução
<details>
<br>

A regressão é apresentada no curso IBM como **o carro-chefe da análise estatística** — e com razão.  
Ela permite:

- modelar relações entre variáveis  
- quantificar efeitos  
- prever valores  
- substituir testes t, ANOVA e correlação  
- interpretar coeficientes  
- entender variáveis explicativas  

Enquanto testes de hipótese respondem “há diferença?”,  
a regressão responde:

> **“Quanto uma variável afeta a outra?”**

No Módulo 6, os instrutores mostram como:

- regressão linear simples substitui o teste t  
- regressão com variáveis dummy substitui ANOVA  
- regressão com variáveis contínuas substitui correlação  
- o termo de erro captura tudo o que o modelo não explica  

Este capítulo organiza esses conceitos em uma estrutura clara, visual e matemática.

### 🎯 Motivação

A regressão é essencial para:

- ciência de dados  
- machine learning  
- economia  
- saúde  
- marketing  
- engenharia  
- previsão  

Ela é a ferramenta mais importante para modelar relações.

### 🔗 Conexão com o capítulo anterior

No Capítulo 5 aprendemos:

- testes t  
- ANOVA  
- correlação  
- valor p  
- estatísticas de teste  

Agora veremos que **todos esses testes podem ser substituídos por regressão**.

### 🎥 Relação com o vídeo correspondente

O vídeo “Regressão — o carro-chefe da análise estatística” apresenta:

- variável dependente (Y)  
- variáveis explicativas (X)  
- coeficientes (β)  
- termo de erro (ε)  
- regressão simples e múltipla  

Este capítulo transforma essas ideias em raciocínio estatístico aplicado.

</details>
<br>

## 2. Revisão do fluxo anterior
<details>
<br>

Até agora, construímos:

### ✔ Capítulo 1 — Fundamentos  
### ✔ Capítulo 2 — Estatística descritiva  
### ✔ Capítulo 3 — Visualização  
### ✔ Capítulo 4 — Distribuições  
### ✔ Capítulo 5 — Testes de hipótese  

Agora entramos na etapa final da análise estatística clássica:

~~~text
Dados brutos
  ↓
Estatística descritiva
  ↓
Visualização
  ↓
Distribuições
  ↓
Testes de hipótese
  ↓
Regressão   ← (Capítulo atual)
~~~

### Por que isso importa agora?

Porque regressão:

- generaliza testes t  
- generaliza ANOVA  
- generaliza correlação  
- permite múltiplas variáveis simultaneamente  
- permite prever valores  

### Como o conteúdo se encaixa no curso

Este capítulo prepara você para:

- modelagem preditiva  
- machine learning supervisionado  
- análise multivariada  
- interpretação de coeficientes  

</details>
<br>

## 3. Apresentação do problema
<details>
<br>

A regressão responde perguntas como:

- “A beleza influencia a avaliação de ensino?”  
- “Instrutores do sexo feminino recebem notas menores?”  
- “A idade afeta a avaliação?”  
- “Qual é o impacto de múltiplas variáveis ao mesmo tempo?”  

Essas perguntas aparecem em:

#### 🏫 Educação  
- impacto de características do instrutor  

#### 📈 Negócios  
- efeito de preço sobre vendas  
- impacto de campanhas  

#### 🏥 Saúde  
- efeito de idade sobre risco  
- impacto de tratamentos  

#### 🎮 Esportes  
- relação entre treino e desempenho  

---

### Fluxograma — Quando usar regressão

~~~text
Início
  ↓
Quero prever Y?
  ↓
Sim → Regressão
  ↓
Quero medir impacto de X sobre Y?
  ↓
Sim → Regressão
  ↓
Quero comparar grupos?
  ↓
Sim → Regressão com variáveis dummy
  ↓
Quero medir relação entre variáveis contínuas?
  ↓
Sim → Regressão (substitui correlação)
~~~

---

### Árvore de decisão — Tipo de regressão

~~~text
Regressão Linear
├── Simples
│   └── 1 variável explicativa (X)
└── Múltipla
    ├── Variáveis contínuas
    ├── Variáveis categóricas (dummies)
    └── Mistura de ambas
~~~

---

### Script conceitual — Processo mental do analista

~~~text
1. Definir variável dependente (Y)
2. Definir variáveis explicativas (X)
3. Formular o modelo
4. Estimar coeficientes (β)
5. Interpretar coeficientes
6. Avaliar significância (valor p)
7. Avaliar ajuste (R²)
8. Analisar resíduos (ε)
9. Usar o modelo para previsão
~~~

---

### Fórmulas fundamentais

#### **Regressão linear simples**



\[
Y = \beta_0 + \beta_1 X + \varepsilon
\]



#### **Regressão múltipla**



\[
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \cdots + \beta_k X_k + \varepsilon
\]



#### **Coeficiente estimado**



\[
\hat{\beta} = (X'X)^{-1} X'Y
\]



#### **Erro (resíduo)**



\[
\varepsilon_i = Y_i - \hat{Y}_i
\]



#### **Coeficiente de determinação**



\[
R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}}
\]



---

### Conclusão da seção

Regressão é a ferramenta mais poderosa da estatística aplicada.  
Ela permite:

- modelar relações  
- quantificar efeitos  
- substituir testes t, ANOVA e correlação  
- prever valores  

</details>
<br>

## 4. Conceito central
<details>
<br>

A regressão é um modelo estatístico que descreve a relação entre uma variável dependente (Y) e uma ou mais variáveis explicativas (X).  
Ela generaliza:

- o teste t (comparação de duas médias)  
- a ANOVA (comparação de mais de duas médias)  
- a correlação (relação entre variáveis contínuas)  

Ou seja:

> **Se você sabe regressão, você sabe todos os testes anteriores — e mais.**

---

### 4.1 Estrutura matemática da regressão

#### **Regressão linear simples**

\[
Y = \beta_0 + \beta_1 X + \varepsilon
\]

Onde:

- \(Y\) = variável dependente  
- \(X\) = variável explicativa  
- \(\beta_0\) = intercepto  
- \(\beta_1\) = coeficiente (impacto de X sobre Y)  
- \(\varepsilon\) = erro (tudo que o modelo não explica)  

#### **Regressão múltipla**

\[
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \cdots + \beta_k X_k + \varepsilon
\]

#### **Estimador dos coeficientes (OLS)**

\[
\hat{\beta} = (X'X)^{-1} X'Y
\]

#### **Resíduos**

\[
\varepsilon_i = Y_i - \hat{Y}_i
\]

#### **Coeficiente de determinação**

\[
R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}}
\]

---

### 4.2 Regressão substitui o teste t

Comparar médias entre dois grupos é equivalente a:

- criar uma variável dummy (0/1)  
- rodar regressão linear  

Exemplo:

\[
Y = \beta_0 + \beta_1 \text{Mulher} + \varepsilon
\]

Se:

- Mulher = 1 → instrutora  
- Mulher = 0 → instrutor  

Então:

- \(\beta_0\) = média dos homens  
- \(\beta_1\) = diferença entre mulheres e homens  

O teste t do coeficiente \(\beta_1\) é **idêntico** ao teste t tradicional.

---

### 4.3 Regressão substitui ANOVA

ANOVA compara médias de 3 ou mais grupos.  
Regressão faz o mesmo usando **variáveis dummy**.

Exemplo com 3 faixas etárias:

\[
Y = \beta_0 + \beta_1 D_1 + \beta_2 D_2 + \varepsilon
\]


Onde:

- \(D_1 = 1\) se idade ≤ 40  
- \(D_2 = 1\) se 40 < idade ≤ 57  
- grupo base = idade > 57  

O teste F da regressão é **idêntico** ao teste F da ANOVA.

---

### 4.4 Regressão substitui correlação

Correlação mede força e direção da relação entre duas variáveis contínuas.

Regressão faz isso e mais:

\[
Y = \beta_0 + \beta_1 X + \varepsilon
\]


O coeficiente de correlação de Pearson é:


\[
r = \sqrt{R^2}
\]

Ou seja:

- regressão fornece **coeficiente**, **valor p**, **R²**, **previsão**  
- correlação fornece apenas **r**  

---

### 4.5 Fluxograma — Quando usar regressão

~~~text
Início
  ↓
Quero prever Y? → Regressão
  ↓
Quero medir impacto de X sobre Y? → Regressão
  ↓
Quero comparar grupos? → Regressão com dummies
  ↓
Quero medir relação contínua? → Regressão simples
  ↓
Quero substituir ANOVA? → Regressão múltipla com dummies
~~~

---

### 4.6 Árvore conceitual — Estrutura da regressão

~~~text
Regressão Linear
├── Simples
│   └── 1 variável explicativa
├── Múltipla
│   ├── Variáveis contínuas
│   ├── Variáveis categóricas (dummies)
│   └── Mistura de ambas
└── Testes derivados
    ├── Teste t (coeficientes)
    ├── Teste F (modelo)
    └── R² (qualidade do ajuste)
~~~

---

### 4.7 Script conceitual — Processo mental do analista

~~~text
1. Definir Y
2. Escolher X
3. Criar dummies se necessário
4. Ajustar modelo
5. Interpretar coeficientes
6. Verificar significância (t e p)
7. Verificar ajuste (R²)
8. Analisar resíduos
9. Usar para previsão
~~~

</details>
<br>

## 5. Exemplos conceituais com código
<details>
<br>

Nesta seção, usamos **dados sintéticos** para ilustrar regressão simples, múltipla e com dummies.

---

### 5.1 Regressão simples — beleza → avaliação

~~~python
import statsmodels.api as sm
import numpy as np

beleza = np.array([0.1, -0.2, 0.3, 0.0, 0.2])
avaliacao = np.array([4.0, 3.8, 4.3, 4.1, 4.2])

X = sm.add_constant(beleza)
modelo = sm.OLS(avaliacao, X).fit()
modelo.summary()
~~~

---

### 5.2 Regressão com variável dummy — gênero

~~~python
genero = np.array([1,0,1,0,1])  # 1 = mulher, 0 = homem
avaliacao = np.array([3.9, 4.1, 3.8, 4.2, 3.7])

X = sm.add_constant(genero)
modelo = sm.OLS(avaliacao, X).fit()
modelo.summary()
~~~

---

### 5.3 Regressão múltipla — beleza + gênero

~~~python
import pandas as pd

df = pd.DataFrame({
    "avaliacao": [4.0, 3.8, 4.3, 4.1, 4.2],
    "beleza": [0.1, -0.2, 0.3, 0.0, 0.2],
    "genero": [1,0,1,0,1]
})

X = sm.add_constant(df[["beleza", "genero"]])
y = df["avaliacao"]

modelo = sm.OLS(y, X).fit()
modelo.summary()
~~~

---

### 5.4 Regressão substituindo ANOVA — dummies de idade

~~~python
df = pd.DataFrame({
    "avaliacao": [4.0, 4.1, 3.9, 4.2, 3.8],
    "grupo": ["jovem", "meia", "meia", "idoso", "jovem"]
})

dummies = pd.get_dummies(df["grupo"], drop_first=True)
X = sm.add_constant(dummies)
y = df["avaliacao"]

modelo = sm.OLS(y, X).fit()
modelo.summary()
~~~

---

### 5.5 Regressão substituindo correlação

~~~python
X = sm.add_constant(beleza)
modelo = sm.OLS(avaliacao, X).fit()

r = np.sqrt(modelo.rsquared)
r
~~~

---

### 5.6 Fórmulas matemáticas importantes

#### Coeficiente estimado

\[
\hat{\beta}_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}
\]

#### Previsão

\[
\hat{Y} = \beta_0 + \beta_1 X
\]

#### Resíduo

\[
\varepsilon_i = Y_i - \hat{Y}_i
\]

#### Teste t do coeficiente

\[
t = \frac{\hat{\beta}_j}{SE(\hat{\beta}_j)}
\]

#### Teste F do modelo

\[
F = \frac{(SSR/k)}{(SSE/(n-k-1))}
\]

---

### 5.7 Fluxograma — Como interpretar coeficientes

~~~text
Coeficiente β
  ↓
β > 0 → relação positiva
β < 0 → relação negativa
β = 0 → sem relação
  ↓
Valor p < 0.05?
  ↓
Sim → efeito significativo
Não → efeito não significativo
~~~

</details>
<br>

## 6. Integração com capítulos anteriores
<details>
<br>

A regressão é o ponto culminante de tudo o que aprendemos até agora.

---

### 6.1 Conexão com o Capítulo 2 (Estatística Descritiva)

- média → interpretada via β₀  
- variância → usada no erro  
- desvio padrão → usado no teste t dos coeficientes  

---

### 6.2 Conexão com o Capítulo 3 (Visualização)

- scatterplots → base para regressão simples  
- boxplots → base para regressão com dummies  
- histogramas → análise de resíduos  

---

### 6.3 Conexão com o Capítulo 4 (Distribuições)

- coeficientes usam distribuição t  
- teste F usa distribuição F  
- resíduos assumem normalidade  

---

### 6.4 Conexão com o Capítulo 5 (Testes de Hipótese)

- regressão substitui teste t  
- regressão substitui ANOVA  
- regressão substitui correlação  

---

### 6.5 Fluxograma — Conexão entre capítulos

~~~text
Capítulo 1 → Fundamentos
  ↓
Capítulo 2 → Estatística Descritiva
  ↓
Capítulo 3 → Visualização
  ↓
Capítulo 4 → Distribuições
  ↓
Capítulo 5 → Testes de Hipótese
  ↓
Capítulo 6 → Regressão (síntese final)
~~~

</details>
<br>

## 7. Boas práticas e limitações
<details>
<br>

A regressão é extremamente poderosa, mas também é uma das técnicas mais mal interpretadas da estatística.  
Aqui organizamos boas práticas, limitações, armadilhas e interpretações equivocadas — exatamente como um cientista de dados deve pensar.

---

### 7.1 Boas práticas

#### ✔ Sempre comece com um gráfico de dispersão  
Antes de ajustar regressão simples, visualize a relação.

#### ✔ Padronize variáveis quando necessário  
Especialmente em regressão múltipla:

\[
Z = \frac{X - \bar{X}}{s}
\]

#### ✔ Use variáveis dummy para categorias  
Exemplo:

\[
\text{Mulher} = 
\begin{cases}
1 & \text{se instrutora} \\
0 & \text{se instrutor}
\end{cases}
\]

#### ✔ Interprete coeficientes no contexto  
Um coeficiente significativo não implica causalidade.

#### ✔ Verifique suposições da regressão  
- linearidade  
- independência  
- homocedasticidade  
- normalidade dos resíduos  

#### ✔ Analise resíduos  
Eles devem parecer “ruído aleatório”.

---

### 7.2 Limitações

#### ⚠ Regressão linear assume relação linear  
Se a relação for curva, o modelo falha.

#### ⚠ Regressão não prova causalidade  
Mesmo com valor p baixo.

#### ⚠ Multicolinearidade distorce coeficientes  
Variáveis altamente correlacionadas prejudicam o modelo.

#### ⚠ Dummies mal definidas geram interpretações erradas  
Sempre escolha um grupo base.

#### ⚠ Outliers influenciam fortemente o modelo  
Regressão é sensível a valores extremos.

---

### 7.3 Armadilhas comuns

#### ❗ Interpretar R² como qualidade absoluta  
R² alto não significa modelo bom; apenas que explica variação.

#### ❗ Usar regressão com variável dependente categórica  
Regressão linear não serve para classificação.

#### ❗ Esquecer de remover a dummy redundante  
Evite “dummy trap”:

\[
D_1 + D_2 + D_3 = 1 \quad \Rightarrow \quad \text{colinearidade perfeita}
\]

#### ❗ Interpretar coeficientes sem olhar valor p  
Coeficiente ≠ significância.

---

### 7.4 Interpretações equivocadas

#### ❌ “Coeficiente positivo significa causalidade”  
Pode ser apenas correlação.

#### ❌ “R² baixo significa modelo ruim”  
Em ciências sociais, R² baixos são comuns.

#### ❌ “Coeficiente não significativo significa ausência de efeito”  
Pode ser falta de poder estatístico.

#### ❌ “Regressão múltipla resolve tudo”  
Modelos ruins continuam ruins com mais variáveis.

---

### 7.5 Fluxograma — Evitando erros comuns

~~~text
Início
  ↓
Visualizar relação (scatterplot)
  ↓
Relação parece linear?
  ↓
Sim → Ajustar regressão
Não → Transformar variáveis ou usar outro modelo
  ↓
Coeficientes significativos?
  ↓
Sim → Interpretar
Não → Reavaliar modelo
  ↓
Analisar resíduos
  ↓
Resíduos aleatórios?
  ↓
Sim → Modelo adequado
Não → Ajustar modelo
~~~

---

### 7.6 Árvore de decisão — O que NÃO fazer

~~~text
Regressão Linear
├── NÃO usar com Y categórico
├── NÃO usar sem verificar resíduos
├── NÃO interpretar coeficientes sem valor p
├── NÃO incluir dummies redundantes
└── NÃO assumir causalidade
~~~

</details>
<br>

## 8. Glossário técnico
<details>
<br>

Aqui estão as definições essenciais para consulta rápida.

---

### 8.1 Estrutura do modelo

#### **Variável dependente (Y)**  
O que queremos explicar.

#### **Variáveis explicativas (X)**  
O que explica Y.

#### **Coeficientes (β)**  
Impacto de cada X sobre Y.

---

### 8.2 Fórmulas essenciais

### **Regressão simples**

\[
Y = \beta_0 + \beta_1 X + \varepsilon
\]

#### **Regressão múltipla**

\[
Y = \beta_0 + \beta_1 X_1 + \cdots + \beta_k X_k + \varepsilon
\]

#### **Estimador OLS**

\[
\hat{\beta} = (X'X)^{-1} X'Y
\]

#### **Resíduos**

\[
\varepsilon_i = Y_i - \hat{Y}_i
\]

#### **Coeficiente de determinação**

\[
R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}}
\]

---

### 8.3 Testes dentro da regressão

#### **Teste t (coeficientes)**

\[
t = \frac{\hat{\beta}_j}{SE(\hat{\beta}_j)}
\]

#### **Teste F (modelo)**

\[
F = \frac{(SSR/k)}{(SSE/(n-k-1))}
\]

---

### 8.4 Variáveis dummy

#### **Definição**

Variáveis categóricas convertidas em 0/1.

#### **Exemplo**

\[
\text{Idoso} =
\begin{cases}
1 & \text{se idade ≥ 57} \\
0 & \text{caso contrário}
\end{cases}
\]

---

### 8.5 Correlação e regressão

#### **Correlação de Pearson**

\[
r = \sqrt{R^2}
\]

---

### 8.6 Fluxograma — Como navegar no glossário

~~~text
Preciso entender:
  ↓
Impacto de X → β
  ↓
Qualidade do modelo → R²
  ↓
Significância → t e p
  ↓
Comparação de grupos → dummies
  ↓
Relação contínua → regressão simples
~~~

</details>
<br>

## 9. Referência rápida
<details>
<br>

Esta seção resume os pontos-chave do capítulo.

---

### 9.1 Estrutura do modelo

\[
Y = \beta_0 + \beta_1 X_1 + \cdots + \beta_k X_k + \varepsilon
\]

---

### 9.2 Testes dentro da regressão

- Teste t → coeficientes  
- Teste F → modelo  
- R² → ajuste  

---

### 9.3 Regressão substitui:

- teste t → dummies binárias  
- ANOVA → múltiplas dummies  
- correlação → regressão simples  

---

### 9.4 Fluxograma — Resumo operacional

~~~text
1. Definir Y
2. Escolher X
3. Criar dummies se necessário
4. Ajustar modelo
5. Interpretar coeficientes
6. Verificar significância
7. Avaliar ajuste (R²)
8. Analisar resíduos
9. Prever valores
~~~

</details>
<br>

## 10. Conclusão do capítulo
<details>
<br>

A regressão é a ferramenta mais poderosa da análise estatística aplicada.  
Ela permite:

- modelar relações  
- quantificar efeitos  
- substituir testes t, ANOVA e correlação  
- prever valores  
- analisar múltiplas variáveis simultaneamente  

Com regressão, você deixa de apenas testar hipóteses e passa a **modelar o comportamento dos dados**.

### 🔗 Preparação para o notebook

O notebook do módulo 6 permitirá:

- ajustar regressão simples e múltipla  
- criar variáveis dummy  
- interpretar coeficientes  
- analisar resíduos  
- comparar modelos  
- substituir testes t, ANOVA e correlação  

### 🎯 Conclusão geral

Com este capítulo, você completa o ciclo estatístico:

- descrição  
- visualização  
- probabilidade  
- testes  
- modelagem  

A partir daqui, você está pronto para avançar para:

- machine learning  
- modelos preditivos  
- análise multivariada  
- projetos reais de ciência de dados  

</details>
<br>
