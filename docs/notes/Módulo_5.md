# 📝 Módulo 5 — Caderno de Anotações  
### Teste de Hipóteses

---

# 📌 Item 1 — Teste Z ou Teste T

## 🎯 Ideia principal
O vídeo explica quando usar **teste Z** e quando usar **teste t**, dependendo do conhecimento sobre o desvio padrão da população e do tipo de comparação.

---

## 🧠 Conceitos importantes

### **1. Quando usar Teste Z**
Use **teste Z** quando:
- o **desvio padrão da população é conhecido**  
- você compara **média da amostra vs média populacional**

### **2. Quando usar Teste t**
Use **teste t** quando:
- o **desvio padrão da população é desconhecido**  
- você compara:
  - média da amostra vs média populacional  
  - médias de **duas amostras independentes** (variâncias iguais ou desiguais)

### **3. Quatro cenários principais**
1. Média da amostra vs média populacional (σ conhecido) → **Z**  
2. Média da amostra vs média populacional (σ desconhecido) → **t**  
3. Duas amostras independentes, variâncias iguais → **t**  
4. Duas amostras independentes, variâncias desiguais → **t**

### **4. Valores críticos**
- Teste bilateral → |estatística| > **1,96** → rejeita H₀  
- Teste unilateral → |estatística| > **1,64** → rejeita H₀  

### **5. Regra geral**
- Estatística grande → rejeita H₀  
- Valor-p < 0,05 → rejeita H₀  

---

## 📚 Termos explicados
- **σ (sigma)**: desvio padrão populacional  
- **Estatística Z / t**: medida padronizada da diferença  
- **Teste bilateral**: diferença em qualquer direção  
- **Teste unilateral**: diferença em direção específica  

## ✍️ Minhas anotações
-  
-  
-  

---

# 📌 Item 2 — Lidando com Caudas e Rejeições

## 🎯 Ideia principal
O vídeo aprofunda a lógica por trás das regiões de rejeição em testes de hipóteses, usando a distribuição normal como referência.

---

## 🧠 Conceitos importantes

### **1. Teste bilateral (duas caudas)**
- Hₐ: diferença ≠ 0  
- Região de rejeição:
  - 2,5% na cauda esquerda  
  - 2,5% na cauda direita  
- Valor crítico: **±1,96**

### **2. Teste unilateral (cauda esquerda)**
- Hₐ: diferença < 0  
- Região de rejeição: 5% na cauda esquerda  
- Valor crítico: **–1,64**

### **3. Teste unilateral (cauda direita)**
- Hₐ: diferença > 0  
- Região de rejeição: 5% na cauda direita  
- Valor crítico: **+1,64**

### **4. Interpretação**
- Estatística cai na região de rejeição → rejeita H₀  
- Estatística cai fora → não rejeita H₀  

---

## 📚 Termos explicados
- **Região de rejeição**: área onde H₀ é rejeitada  
- **Cauda**: extremidade da distribuição  
- **Valor crítico**: limite para rejeitar H₀  

## ✍️ Minhas anotações
-  
-  
-  

---

# 📌 Item 3 — Variâncias Iguais ou Desiguais

## 🎯 Ideia principal
Antes de realizar um teste t entre dois grupos, é necessário determinar se as variâncias são iguais ou diferentes.

---

## 🧠 Conceitos importantes

### **1. Teste de Levene**
- H₀: variâncias são iguais  
- Se valor-p < 0,05 → rejeita H₀ → variâncias **desiguais**  
- Se valor-p ≥ 0,05 → não rejeita H₀ → variâncias **iguais**

### **2. Aplicação no exemplo**
- Avaliação média:
  - Mulheres: 3,90 (σ = 0,53)  
  - Homens: 4,06 (σ = 0,55)  
- Teste de Levene → p = 0,66 → variâncias iguais

### **3. Consequência**
- Teste t com `equal_var=True`

### **4. Regra prática (manual)**
- Variância maior / variância menor < **1,5** → assume variâncias iguais

---

## 📚 Termos explicados
- **Variância combinada**: usada quando variâncias são iguais  
- **Graus de liberdade**: n₁ + n₂ – 2  
- **equal_var**: parâmetro do teste t no SciPy  

## ✍️ Minhas anotações
-  
-  
-  

---

# 📌 Item 4 — ANOVA

## 🎯 Ideia principal
ANOVA é usada quando queremos comparar **médias de três ou mais grupos**.

---

## 🧠 Conceitos importantes

### **1. Quando usar ANOVA**
- Comparar médias de 3+ grupos  
- Ex.: idade dos instrutores → jovens, meia-idade, idosos

### **2. Hipóteses**
- H₀: todas as médias são iguais  
- Hₐ: pelo menos uma média é diferente

### **3. Estatística F**
- Calculada pela razão entre variância entre grupos e variância dentro dos grupos  
- Valor-p < 0,05 → rejeita H₀

### **4. Exemplos do vídeo**
- Pontuação de beleza → p = 4,32e-8 → rejeita H₀  
- Avaliação de ensino → p = 0,295 → não rejeita H₀

---

## 📚 Termos explicados
- **F-statistic**: razão entre variâncias  
- **Between-group variance**: variação entre grupos  
- **Within-group variance**: variação dentro dos grupos  

## ✍️ Minhas anotações
-  
-  
-  

---

# 📌 Item 5 — Testes de Correlação

## 🎯 Ideia principal
Agora o foco é verificar se existe **relação entre duas variáveis**, categóricas ou contínuas.

---

## 🧠 Conceitos importantes

### **1. Variáveis categóricas → Qui-quadrado**
- Exemplo: gênero vs titularidade  
- H₀: variáveis são independentes  
- Hₐ: variáveis são associadas  
- Valor-p > 0,05 → não rejeita H₀

### **2. Variáveis contínuas → Correlação de Pearson**
- Exemplo: beleza vs avaliação de ensino  
- Coeficiente r varia entre –1 e +1  
- r = 0,18 → correlação fraca positiva  
- p < 0,05 → rejeita H₀ → existe correlação

### **3. Interpretação do coeficiente r**
- r ≈ 1 → forte correlação positiva  
- r ≈ –1 → forte correlação negativa  
- r ≈ 0 → sem correlação linear  

---

## 📚 Termos explicados
- **Qui-quadrado**: teste para associação entre categorias  
- **Valor esperado**: contagem teórica se não houvesse associação  
- **Pearson r**: medida de correlação linear  
- **Independência**: ausência de relação estatística  

## ✍️ Minhas anotações
-  
-  
-  

---

# ✔ Módulo 5 — Finalizado
