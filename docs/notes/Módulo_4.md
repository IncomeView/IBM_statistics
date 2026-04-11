# 📝 Módulo 4 — Caderno de Anotações  
### Introdução às Distribuições de Probabilidade

---

# 📌 Item 1 — Números Aleatórios e Distribuições de Probabilidade

## 🎯 Ideia principal
O vídeo introduz os conceitos fundamentais de probabilidade, variáveis aleatórias e distribuições de probabilidade — a base para todo o restante do curso.

---

## 🧠 Conceitos importantes

### **1. Probabilidade**
- Medida entre **0 e 1** que indica a chance de um evento ocorrer.  
- Ex.: chance de chuva = 45% → 0,45.

### **2. Variável Aleatória**
- Função que associa cada resultado possível de um experimento a um valor numérico.  
- Ex.: resultado de um dado → {1, 2, 3, 4, 5, 6}.

### **3. Espaço Amostral**
- Conjunto de todos os resultados possíveis.  
- Ex.: lançar dois dados → 36 combinações possíveis.

### **4. Distribuição de Probabilidade**
- Modelo teórico que descreve:
  - valores possíveis de uma variável aleatória  
  - probabilidade de cada valor ocorrer  

### **5. Exemplo dos dois dados**
- Soma mínima = 2 (1+1) → probabilidade = 1/36  
- Soma máxima = 12 (6+6) → probabilidade = 1/36  
- Soma mais provável = 7 → probabilidade = 6/36  

### **6. Função de Distribuição Cumulativa (CDF)**
- Probabilidade de obter um valor **menor ou igual** a X.  
- Ex.: P(soma ≤ 6)

### **7. Ajuste de distribuição normal**
- Dados reais podem ser aproximados por uma curva normal usando:
  - média  
  - desvio padrão  

---

## 📚 Termos explicados
- **CDF**: probabilidade acumulada.  
- **Distribuição discreta**: valores isolados (ex.: soma de dados).  
- **Distribuição contínua**: valores em intervalo (ex.: altura, idade).  
- **Densidade**: altura da curva da distribuição contínua.

## ✍️ Minhas anotações
-  
-  
-  

---

# 📌 Item 2 — Declare sua Hipótese

## 🎯 Ideia principal
Antes de realizar qualquer teste estatístico, é necessário declarar **hipótese nula (H₀)** e **hipótese alternativa (Hₐ)**.

---

## 🧠 Conceitos importantes

### **1. Comparação de médias**
Exemplo: Jordan vs Chamberlain  
- Jordan: média ≈ 30,12  
- Chamberlain: média ≈ 30,06  

Mesmo valores próximos exigem teste formal.

### **2. Três formas de declarar hipóteses**

#### **a) Teste bilateral (duas caudas)**
- H₀: μ₁ = μ₂  
- Hₐ: μ₁ ≠ μ₂  

#### **b) Teste unilateral (uma cauda) — maior que**
- H₀: μ₁ ≥ μ₂  
- Hₐ: μ₁ < μ₂  

#### **c) Teste unilateral — menor que**
- H₀: μ₁ ≤ μ₂  
- Hₐ: μ₁ > μ₂  

---

## 📚 Termos explicados
- **H₀ (hipótese nula)**: afirmação inicial, assume “nenhuma diferença”.  
- **Hₐ (hipótese alternativa)**: afirmação que queremos testar.  
- **Teste unilateral**: direção específica.  
- **Teste bilateral**: diferença em qualquer direção.

## ✍️ Minhas anotações
-  
-  
-  

---

# 📌 Item 3 — Alfa (α) e Valor-p

## 🎯 Ideia principal
Alfa e valor-p são os pilares da decisão estatística: rejeitar ou não rejeitar H₀.

---

## 🧠 Conceitos importantes

### **1. Alfa (α) — nível de significância**
- Probabilidade de rejeitar H₀ quando ela é verdadeira (erro tipo I).  
- Valores comuns:
  - 0,05 (5%)  
  - 0,01 (1%)  
  - 0,001 (0,1%) em áreas críticas como medicina  

### **2. Valor-p**
- Probabilidade de observar um resultado tão extremo quanto o da amostra **se H₀ for verdadeira**.  
- Regra de decisão:
  - Se **p < α** → rejeita H₀  
  - Se **p ≥ α** → não rejeita H₀  

### **3. Testes de uma ou duas caudas**
- Em testes bilaterais, α é dividido entre as duas caudas.  
- Ex.: α = 0,05 → 0,025 em cada cauda.

---

## 📚 Termos explicados
- **Erro tipo I**: rejeitar H₀ quando ela é verdadeira.  
- **Região de rejeição**: área da distribuição onde rejeitamos H₀.  
- **Extremidade (cauda)**: parte final da distribuição.

## ✍️ Minhas anotações
-  
-  
-  

---

# 📌 Item 4 — Distribuição Normal

## 🎯 Ideia principal
A distribuição normal é uma das mais importantes da estatística — base para testes, intervalos e inferência.

---

## 🧠 Conceitos importantes

### **1. Características da distribuição normal**
- Curva em forma de sino  
- Simétrica  
- Definida por:
  - **média (μ)**  
  - **desvio padrão (σ)**  

### **2. Fórmula da densidade normal**
A função depende de:
- x (valor)  
- μ (média)  
- σ (desvio padrão)  

### **3. Normal padrão**
- Média = 0  
- Desvio padrão = 1  
- Usada para tabelas Z

### **4. Geração da curva**
- Usando valores de x entre -4 e 4  
- Usando `scipy.stats.norm.pdf`  

---

## 📚 Termos explicados
- **PDF (função densidade)**: altura da curva.  
- **Z-score**: padronização (x - μ) / σ.  
- **Simetria**: lados iguais da curva.

## ✍️ Minhas anotações
-  
-  
-  

---

# 📌 Item 5 — Distribuição t de Student

## 🎯 Ideia principal
A distribuição t é usada quando trabalhamos com **amostras pequenas** ou quando a variância populacional é desconhecida.

---

## 🧠 Conceitos importantes

### **1. Origem**
- Criada por William Gosset (pseudônimo “Student”).  
- Usada inicialmente na Guinness para controle de qualidade.

### **2. Diferenças entre normal e t**
- t tem **caudas mais largas** (mais incerteza).  
- À medida que o tamanho da amostra cresce → t se aproxima da normal.

### **3. Aplicações**
- Teste t para comparação de médias.  
- Exemplo do vídeo: diferença entre avaliações de ensino de homens e mulheres.

### **4. Suposições do teste t**
- Dados contínuos ou ordinais  
- Amostra aleatória  
- Distribuição aproximadamente normal  
- Homogeneidade de variâncias  

---

## 📚 Termos explicados
- **Graus de liberdade (df)**: n – 1  
- **Homogeneidade de variância**: variâncias semelhantes entre grupos  
- **Teste t independente**: compara dois grupos distintos

## ✍️ Minhas anotações
-  
-  
-  

---

# 📌 Item 6 — Probabilidade de Obter Avaliação Alta ou Baixa

## 🎯 Ideia principal
Mostra como calcular probabilidades usando a distribuição normal e Z-scores.

---

## 🧠 Conceitos importantes

### **1. Padronização (Z-score)**
Z = (x – μ) / σ  
Ex.: avaliação 4,5 → Z ≈ 0,906

### **2. Probabilidade acumulada**
- Usamos tabelas Z ou `scipy.stats.norm.cdf`  
- CDF retorna P(X ≤ x)

### **3. Probabilidade complementar**
- P(X > x) = 1 – P(X ≤ x)

### **4. Exemplo**
- P(avaliação ≤ 4,5) ≈ 0,818  
- P(avaliação > 4,5) ≈ 0,182  

---

## 📚 Termos explicados
- **CDF**: probabilidade acumulada.  
- **Complemento**: 1 – probabilidade acumulada.  
- **Área sob a curva**: representa probabilidade.

## ✍️ Minhas anotações
-  
-  
-  

---

# 📌 Item 7 — Tabela Normal Padrão

## 🎯 Ideia principal
A tabela Z permite encontrar probabilidades sem computador.

---

## 🧠 Como usar a tabela Z

1. Pegue o **primeiro dígito** e o **primeiro decimal** → linha  
   - Ex.: Z = 1,44 → linha = 1,4  
2. Pegue o **segundo decimal** → coluna  
   - Ex.: 0,04  
3. Interseção = P(Z < valor)

Exemplo:
- P(Z < 1,44) = 0,92507  
- P(Z > 1,44) = 1 – 0,92507  

---

## 📚 Termos explicados
- **Tabela Z**: tabela da normal padrão.  
- **Probabilidade acumulada**: área à esquerda.  
- **Probabilidade complementar**: área à direita.

## ✍️ Minhas anotações
-  
-  
-  

---

# ✔ Módulo 4 — Finalizado
