# 📝 Módulo 6 — Caderno de Anotações  
### Análise de Regressão

---

# 📌 Item 1 — Regressão em vez de Teste de Hipótese

## 🎯 Ideia principal
A regressão é apresentada como a ferramenta central da análise estatística, capaz de substituir testes como t, ANOVA e correlação.  
Ela permite analisar relações entre variáveis de forma integrada.

---

## 🧠 Conceitos importantes

### 1. Variável dependente (Y)
É a variável que queremos explicar.  
Ex.: pontuação de avaliação de ensino.

### 2. Variáveis explicativas (X)
Variáveis que explicam Y.  
Ex.: beleza, gênero, proficiência em inglês.

### 3. Estrutura do modelo
Y = β0 + β1X1 + β2X2 + ... + ε

- β0: intercepto  
- β1, β2: pesos das variáveis  
- ε: termo de erro (diferença entre valor real e previsto)

### 4. Exemplo do vídeo
Avaliação = 3.998 + 0.133 * Beleza + ε

---

## 📚 Termos explicados
- Regressão linear  
- Coeficiente β  
- Termo de erro  

## ✍️ Minhas anotações
-  
-  
-  

---

# 📌 Item 2 — Regressão no lugar do Teste t

## 🎯 Ideia principal
A regressão substitui o teste t quando transformamos variáveis categóricas em dummies (0/1).

---

## 🧠 Conceitos importantes

### 1. Dummy para gênero
Mulher = 1  
Homem = 0

### 2. Modelo
Avaliação = β0 + β1(Mulher) + ε

### 3. Resultado do vídeo
- Estatística t = –3,25  
- p < 0,05 → diferença significativa  
- Mulheres têm ~0,17 ponto a menos

### 4. Conclusão
Regressão e teste t chegam à mesma conclusão.

---

## 📚 Termos explicados
- Dummy  
- Coeficiente β1  
- Resumo do modelo  

## ✍️ Minhas anotações
-  
-  
-  

---

# 📌 Item 3 — Regressão em vez de ANOVA

## 🎯 Ideia principal
ANOVA compara médias de 3+ grupos, mas regressão pode fazer o mesmo usando dummies.

---

## 🧠 Conceitos importantes

### 1. Exemplo do vídeo
Grupos de idade:
- ≤ 40  
- 40–57  
- ≥ 57  

### 2. ANOVA tradicional
- p < 0,05 → rejeita H0  
→ médias diferentes

### 3. Regressão equivalente
Criar dummies para cada faixa etária e rodar OLS.

### 4. Resultado
Regressão produz:
- mesma estatística F  
- mesmo valor-p  
- mesma conclusão da ANOVA

---

## 📚 Termos explicados
- ANOVA  
- Estatística F  
- Dummies múltiplas  

## ✍️ Minhas anotações
-  
-  
-  

---

# 📌 Item 4 — Regressão no lugar de Correlação

## 🎯 Ideia principal
A regressão também substitui o teste de correlação de Pearson quando lidamos com duas variáveis contínuas.

---

## 🧠 Conceitos importantes

### 1. Exemplo do vídeo
X = beleza  
Y = avaliação de ensino

### 2. Pearson r
Mede força da relação linear.

### 3. Regressão equivalente
Y = β0 + β1X + ε

### 4. Resultado
- p < 0,05 → relação significativa  
- R² = 0,036 → r = 0,189 (mesmo valor do Pearson)

### 5. Conclusão
Regressão e correlação produzem o mesmo diagnóstico.

---

## 📚 Termos explicados
- Correlação de Pearson  
- R²  
- Inclinação β1  

## ✍️ Minhas anotações
-  
-  
-  

---

# ✔ Módulo 6 — Finalizado
