# PROMPT DEFINITIVO — GERAR NOTEBOOK DIDÁTICO (JUPYTEXT + LATEX + LIVRO APLICADO)

## OBJETIVO PRINCIPAL
Gerar um notebook completo no formato **Jupytext (.py:percent)**, estruturado como um **Livro Didático Aplicado (Híbrido)**, seguindo exatamente o estilo, profundidade, narrativa e organização do *Notebook 2 — Estatística Descritiva (versão final revisada)*.

O notebook deve unir:
- clareza didática
- profundidade conceitual
- rigor matemático
- explicações intuitivas
- demonstrações formais opcionais
- aplicações práticas
- visualizações interpretadas
- narrativa fluida e coerente
- estética matemática impecável
- estrutura modular e navegável

---

# 1. ESTRUTURA OBRIGATÓRIA DO NOTEBOOK

O notebook deve conter, **nesta ordem**, as seguintes seções:

1. **Título do Módulo**
2. **Índice navegável**
3. **Setup (bibliotecas e dados)**
4. **Seções principais**, cada uma contendo:
   - 🔵 Conteúdo oficial (IBM)
   - 🟣 Conteúdo expandido (Livro Didático)
   - 🟠 Conteúdo avançado (opcional, matemático)
5. **Aplicações práticas**
6. **Exercícios guiados**
7. **Diagramas conceituais**
8. **Apêndice matemático avançado**
9. **Encerramento**

Cada seção deve seguir o estilo e a lógica do Notebook 2.

---

# 2. FORMATO JUPYTEXT (.py:percent)

Usar **exatamente**:

~~~codigo
# %% [markdown]
# texto aqui

# %%
# código aqui
~~~

- Gráficos com `matplotlib` ou `seaborn`
- Código limpo, comentado e didático
- Sem células vazias ou redundantes

---

# 3. PADRÃO DE RENDERIZAÇÃO LATEX (OBRIGATÓRIO)

### Inline
Usar **somente** `$ ... $`.

### Bloco
Usar **somente**:

~~~codigo
$$
...
$$
~~~

### Texto dentro da equação
Usar **somente** `\text{...}`.

### Proibições
- ❌ `\(` `\)`
- ❌ `

\[` `\]

`
- ❌ HTML para alinhar equações
- ❌ `aligned` inline
- ❌ ambientes LaTeX não suportados pelo Jupyter

---

# 4. PADRÃO PEDAGÓGICO (OBRIGATÓRIO)

Cada conceito deve incluir:

- definição clara
- explicação dos símbolos
- lógica da fórmula
- interpretação intuitiva
- aplicação prática
- exemplos numéricos
- gráficos quando apropriado
- conexões históricas quando relevante
- relação com problemas reais
- aprofundamento opcional em `<details>`

---

# 5. USO DE <details> PARA CONTEÚDO AVANÇADO

Sempre que houver:

- demonstração formal
- prova matemática
- derivação longa
- contexto histórico
- observações avançadas

usar:

~~~codigo
<details>
<summary>🟠 Conteúdo avançado (opcional)</summary>

(conteúdo aprofundado aqui)

</details>
~~~

---

# 6. ESTILO E TOM

O notebook deve ter:

- linguagem clara, elegante e acessível
- narrativa fluida e coerente
- tom de livro didático moderno
- foco em entendimento profundo
- exemplos que constroem raciocínio
- estética matemática impecável
- coerência entre seções
- explicações que conectam teoria e prática

---

# 7. APLICAÇÕES PRÁTICAS

Sempre incluir:

- exemplos com dados reais ou simulados
- gráficos interpretados
- explicações passo a passo
- conexão com o mundo real

Quando possível, usar o dataset **teachingratings**.

---

# 8. EXERCÍCIOS GUIADOS

Cada exercício deve:

- ter enunciado claro
- conter células com:

~~~codigo
# TODO: seu código aqui
~~~

- incluir dicas
- seguir o estilo do Notebook 2

---

# 9. DIAGRAMAS CONCEITUAIS

Incluir mapas mentais em Markdown, seguindo o padrão do Notebook 2.

---

# 10. APÊNDICE MATEMÁTICO AVANÇADO

Incluir:

- demonstrações formais
- propriedades matemáticas
- identidades úteis
- resultados clássicos

Sempre organizado em subseções claras.

---

# 11. INSTRUÇÃO FINAL

Gerar o notebook **seguindo exatamente este prompt**, no estilo do **Notebook 2 (versão final)**, adaptado ao conteúdo do módulo solicitado (ex.: Módulo 3, Módulo 4, etc.).

