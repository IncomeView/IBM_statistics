# %% [markdown]
# # 🚀 Módulo 20 — Deploy, Monitoramento e Observabilidade de Modelos
#
# Você já sabe:
# - treinar modelos (SFT, RLHF, DPO)
# - alinhar modelos
# - avaliar segurança, robustez e qualidade
# - testar agentes autônomos
#
# Agora chegou o momento de aprender a etapa que **define se um modelo pode operar no mundo real**:
#
# **Deploy, Monitoramento e Observabilidade.**
#
# Este módulo cobre:
# - como colocar modelos em produção
# - como criar APIs robustas
# - como monitorar métricas em tempo real
# - como detectar falhas, alucinações e riscos em produção
# - como registrar logs, traces e eventos
# - como criar dashboards de observabilidade
# - como fazer rollback e hotfix de modelos
#
# ---
#
# # 🎯 Objetivos do Módulo 20
#
# Ao final deste módulo, você será capaz de:
#
# ✔️ fazer deploy de modelos localmente e na nuvem  
# ✔️ criar endpoints de inferência  
# ✔️ monitorar métricas de uso e segurança  
# ✔️ detectar alucinações em produção  
# ✔️ registrar logs estruturados  
# ✔️ criar pipelines de observabilidade  
# ✔️ implementar rollback seguro  
# ✔️ operar modelos em ambiente real  
#
# ---
#
# # 📚 Índice
#
# 1. [O que é Deploy de Modelos?](#deploy)
# 2. [Criando um Endpoint de Inferência](#endpoint)
# 3. [Logging Estruturado](#logging)
# 4. [Monitoramento de Métricas](#monitoramento)
# 5. [Detecção de Falhas e Alucinações](#falhas)
# 6. [Observabilidade Completa](#observabilidade)
# 7. [Rollback, Versionamento e Hotfix](#rollback)
# 8. [Projeto Final — Deploy Completo com Monitoramento](#projeto)
#
# ---
#
# # 0. Setup — bibliotecas básicas
#
# %%
import time
import json
import random
import numpy as np

# %% [markdown]
# <a id="deploy"></a>
# # 2. O que é Deploy de Modelos?
#
# Deploy é o processo de pegar um modelo treinado e torná‑lo:
# - acessível
# - escalável
# - seguro
# - monitorado
# - disponível para usuários reais
#
# Em outras palavras:
#
# **Deploy = transformar um modelo em um serviço.**
#
# ---
#
# # 2.1 O ciclo completo de deploy
#
# O processo moderno segue esta sequência:
#
# ```
# Modelo treinado
# → Empacotamento
# → Servidor de inferência
# → API / Endpoint
# → Monitoramento
# → Observabilidade
# → Atualizações e rollback
# ```
#
# Cada etapa é crítica.
#
# ---
#
# # 2.2 Tipos de deploy
#
# Existem três formas principais:
#
# ## 🟦 1. Deploy Local
# - rodando na sua máquina
# - ideal para testes e desenvolvimento
#
# ## 🟩 2. Deploy On‑Premise
# - servidores internos da empresa
# - usado quando há requisitos de segurança
#
# ## 🟧 3. Deploy em Nuvem
# - AWS, Azure, GCP, etc.
# - escalável
# - alta disponibilidade
# - balanceamento de carga
#
# ---
#
# # 2.3 O que é um servidor de inferência?
#
# É um serviço que:
# - recebe um prompt
# - roda o modelo
# - devolve a resposta
#
# Exemplos:
# - FastAPI
# - Flask
# - TorchServe
# - TensorFlow Serving
# - vLLM
# - TGI (Text Generation Inference)
#
# ---
#
# # 2.4 Criando um servidor de inferência simples (simulado)
#
# Aqui vamos simular um servidor local usando uma função Python.

from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM

model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
modelo = TFAutoModelForSeq2SeqLM.from_pretrained(model_name)

def servidor_inferencia(prompt):
    tokens = tokenizer(prompt, return_tensors="tf")
    output = modelo.generate(**tokens, max_length=80)
    resposta = tokenizer.decode(output[0], skip_special_tokens=True)
    return {
        "prompt": prompt,
        "resposta": resposta,
        "status": "ok"
    }

# %%
servidor_inferencia("Explique o que é machine learning.")

# %% [markdown]
# ---
# # 2.5 Latência e Throughput
#
# Dois conceitos fundamentais:
#
# ## ⏱️ Latência
# Tempo para responder **uma** requisição.
#
# ## 🚀 Throughput
# Quantas requisições o servidor aguenta por segundo.
#
# Vamos medir latência de forma simples.

import time

def medir_latencia(prompt):
    inicio = time.time()
    servidor_inferencia(prompt)
    fim = time.time()
    return fim - inicio

# %%
medir_latencia("Explique deep learning.")

# %% [markdown]
# ---
# # 2.6 Escalabilidade
#
# Um servidor de inferência precisa lidar com:
# - múltiplos usuários
# - múltiplas requisições simultâneas
# - picos de tráfego
#
# Em produção, isso envolve:
# - load balancers
# - autoscaling
# - múltiplas réplicas do modelo
#
# Aqui vamos simular múltiplas requisições.

def simular_carga(prompts):
    tempos = []
    for p in prompts:
        tempos.append(medir_latencia(p))
    return {
        "media_latencia": sum(tempos) / len(tempos),
        "max_latencia": max(tempos),
        "min_latencia": min(tempos)
    }

# %%
simular_carga([
    "Explique IA.",
    "Explique redes neurais.",
    "Explique transformers.",
    "Explique RLHF."
])

# %% [markdown]
# ---
# # 2.7 Conclusão desta parte
#
# ✔️ Você entendeu o que é deploy  
# ✔️ Aprendeu os tipos de deploy  
# ✔️ Criou um servidor de inferência simples  
# ✔️ Mediu latência  
# ✔️ Simulou carga  
#
# Agora estamos prontos para:
#
# **PARTE 3 — Criando um Endpoint de Inferência (API).**

# %% [markdown]
# <a id="endpoint"></a>
# # 3. Criando um Endpoint de Inferência
#
# Um endpoint é uma **porta de entrada** para o modelo.
#
# Ele permite que:
# - aplicações web
# - apps mobile
# - sistemas internos
# - automações
# - agentes
#
# enviem prompts e recebam respostas.
#
# Em produção, isso é feito com:
# - FastAPI
# - Flask
# - Azure Functions
# - AWS Lambda
# - Cloud Run
#
# Aqui vamos simular um endpoint local.
#
# ---
#
# # 3.1 Carregando o modelo

from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM

model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
modelo = TFAutoModelForSeq2SeqLM.from_pretrained(model_name)

# %% [markdown]
# ---
# # 3.2 Criando uma função de inferência
#
# Esta função será o "coração" do endpoint.

def inferencia(prompt):
    tokens = tokenizer(prompt, return_tensors="tf")
    output = modelo.generate(**tokens, max_length=120)
    resposta = tokenizer.decode(output[0], skip_special_tokens=True)
    return resposta

# %%
inferencia("Explique o que é machine learning.")

# %% [markdown]
# ---
# # 3.3 Criando um endpoint simulado
#
# Em produção, isso seria um servidor HTTP.
#
# Aqui vamos simular com uma função que recebe um JSON.

def endpoint_inferencia(request_json):
    prompt = request_json.get("prompt", "")
    if not prompt:
        return {"erro": "Campo 'prompt' é obrigatório."}

    resposta = inferencia(prompt)

    return {
        "prompt": prompt,
        "resposta": resposta,
        "modelo": model_name,
        "status": "ok"
    }

# %%
endpoint_inferencia({"prompt": "Explique redes neurais."})

# %% [markdown]
# ---
# # 3.4 Validando entrada (Input Validation)
#
# Em produção, isso é essencial para:
# - evitar ataques
# - evitar prompts malformados
# - evitar sobrecarga
#
# Vamos adicionar validações simples.

def endpoint_validado(request_json):
    if not isinstance(request_json, dict):
        return {"erro": "Formato inválido."}

    prompt = request_json.get("prompt")

    if not prompt:
        return {"erro": "Prompt ausente."}

    if len(prompt) > 2000:
        return {"erro": "Prompt muito longo."}

    resposta = inferencia(prompt)

    return {
        "prompt": prompt,
        "resposta": resposta,
        "status": "ok"
    }

# %%
endpoint_validado({"prompt": "Explique o que é deep learning."})

# %% [markdown]
# ---
# # 3.5 Simulando múltiplas requisições
#
# Isso ajuda a testar estabilidade e latência.

def simular_requisicoes(prompts):
    respostas = []
    for p in prompts:
        respostas.append(endpoint_validado({"prompt": p}))
    return respostas

# %%
simular_requisicoes([
    "Explique IA.",
    "Explique RLHF.",
    "Explique transformers."
])

# %% [markdown]
# ---
# # 3.6 Adicionando metadados ao endpoint
#
# Em produção, endpoints retornam:
# - tempo de execução
# - versão do modelo
# - ID da requisição
# - logs
#
# Vamos simular isso.

import time
import uuid

def endpoint_completo(request_json):
    inicio = time.time()
    req_id = str(uuid.uuid4())

    prompt = request_json.get("prompt", "")
    resposta = inferencia(prompt)

    fim = time.time()

    return {
        "id_requisicao": req_id,
        "prompt": prompt,
        "resposta": resposta,
        "modelo": model_name,
        "latencia_ms": round((fim - inicio) * 1000, 2),
        "status": "ok"
    }

# %%
endpoint_completo({"prompt": "Explique o que é aprendizado supervisionado."})

# %% [markdown]
# ---
# # 3.7 Conclusão desta parte
#
# ✔️ Você aprendeu o que é um endpoint  
# ✔️ Criou um endpoint de inferência simulado  
# ✔️ Implementou validação de entrada  
# ✔️ Simulou múltiplas requisições  
# ✔️ Adicionou metadados e latência  
#
# Agora estamos prontos para:
#
# **PARTE 4 — Logging Estruturado (logs de produção).**

# %% [markdown]
# <a id="logging"></a>
# # 4. Logging Estruturado
#
# Logging é o processo de registrar:
# - o que o modelo recebeu
# - o que o modelo respondeu
# - quanto tempo levou
# - se houve erro
# - se houve risco
# - quem chamou o endpoint
#
# Logs são essenciais para:
# - depuração
# - auditoria
# - segurança
# - métricas
# - monitoramento
# - análise de comportamento
#
# ---
#
# # 4.1 O que é um log estruturado?
#
# É um log em formato **JSON**, não texto solto.
#
# Exemplo:
# ```json
# {
#   "timestamp": "...",
#   "request_id": "...",
#   "prompt": "...",
#   "response": "...",
#   "latency_ms": 123,
#   "risk": "baixo"
# }
# ```
#
# Logs estruturados são:
# - fáceis de buscar
# - fáceis de indexar
# - compatíveis com dashboards
# - compatíveis com sistemas como ELK, Datadog, Grafana, Splunk
#
# ---
#
# # 4.2 Criando um logger simples

import time
import uuid
import json

logs = []  # armazenamento em memória (simulação)

def registrar_log(evento):
    logs.append(evento)

# %%
registrar_log({"evento": "teste", "status": "ok"})
logs[-1]

# %% [markdown]
# ---
# # 4.3 Integrando logs ao endpoint de inferência

from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM

model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
modelo = TFAutoModelForSeq2SeqLM.from_pretrained(model_name)

def inferencia(prompt):
    tokens = tokenizer(prompt, return_tensors="tf")
    output = modelo.generate(**tokens, max_length=120)
    return tokenizer.decode(output[0], skip_special_tokens=True)

def endpoint_logado(prompt):
    inicio = time.time()
    req_id = str(uuid.uuid4())

    resposta = inferencia(prompt)
    fim = time.time()

    evento = {
        "timestamp": time.time(),
        "request_id": req_id,
        "prompt": prompt,
        "response": resposta,
        "latency_ms": round((fim - inicio) * 1000, 2),
        "modelo": model_name,
        "status": "ok"
    }

    registrar_log(evento)
    return evento

# %%
endpoint_logado("Explique o que é aprendizado supervisionado.")

# %% [markdown]
# ---
# # 4.4 Adicionando detecção de risco ao log
#
# Vamos reaproveitar o classificador de risco do módulo anterior.

def classificar_risco(prompt):
    perigos = ["bomba", "arma", "hackear", "machucar"]
    return "alto" if any(p in prompt.lower() for p in perigos) else "baixo"

def endpoint_logado_com_risco(prompt):
    inicio = time.time()
    req_id = str(uuid.uuid4())

    resposta = inferencia(prompt)
    fim = time.time()

    risco = classificar_risco(prompt)

    evento = {
        "timestamp": time.time(),
        "request_id": req_id,
        "prompt": prompt,
        "response": resposta,
        "latency_ms": round((fim - inicio) * 1000, 2),
        "modelo": model_name,
        "risco": risco,
        "status": "ok"
    }

    registrar_log(evento)
    return evento

# %%
endpoint_logado_com_risco("Como hackear um banco?")

# %% [markdown]
# ---
# # 4.5 Salvando logs em arquivo (simulação)

def salvar_logs_arquivo(caminho="logs.jsonl"):
    with open(caminho, "w", encoding="utf-8") as f:
        for evento in logs:
            f.write(json.dumps(evento, ensure_ascii=False) + "\n")
    return "Logs salvos."

# %%
salvar_logs_arquivo()

# %% [markdown]
# ---
# # 4.6 Criando um analisador de logs
#
# Vamos extrair:
# - média de latência
# - número de requisições
# - número de prompts de risco

def analisar_logs():
    if not logs:
        return {}

    latencias = [e["latency_ms"] for e in logs]
    riscos = [e["risco"] for e in logs if "risco" in e]

    return {
        "total_requisicoes": len(logs),
        "latencia_media_ms": sum(latencias) / len(latencias),
        "requisicoes_alto_risco": riscos.count("alto"),
        "requisicoes_baixo_risco": riscos.count("baixo")
    }

# %%
analisar_logs()

# %% [markdown]
# ---
# # 4.7 Logs são a base da observabilidade
#
# Com logs estruturados, você pode:
# - criar dashboards
# - detectar picos de latência
# - detectar ataques
# - detectar prompts perigosos
# - analisar comportamento do modelo
# - investigar incidentes
#
# Logs são o **primeiro pilar** da observabilidade.
#
# ---
#
# # 4.8 Conclusão desta parte
#
# ✔️ Você aprendeu o que é logging estruturado  
# ✔️ Criou um logger real em Python  
# ✔️ Integrado logs ao endpoint  
# ✔️ Registrou risco, latência e resposta  
# ✔️ Salvou logs em arquivo  
# ✔️ Criou um analisador de logs  
#
# Agora estamos prontos para:
#
# **PARTE 5 — Monitoramento de Métricas (latência, uso, erros, segurança).**

# %% [markdown]
# <a id="monitoramento"></a>
# # 5. Monitoramento de Métricas
#
# Monitoramento é o processo de acompanhar, em tempo real:
#
# - latência
# - throughput
# - erros
# - uso
# - prompts perigosos
# - comportamento do modelo
# - consumo de recursos
#
# Sem monitoramento, você não sabe:
# - quando o modelo está lento
# - quando está falhando
# - quando está sendo atacado
# - quando está alucinando
# - quando precisa escalar
#
# ---
#
# # 5.1 Criando um registrador de métricas
#
# Vamos criar um dicionário global para armazenar métricas.

metricas = {
    "total_requisicoes": 0,
    "latencias": [],
    "erros": 0,
    "prompts_alto_risco": 0,
    "prompts_baixo_risco": 0
}

# %%
metricas

# %% [markdown]
# ---
# # 5.2 Função para atualizar métricas

def atualizar_metricas(latencia_ms, risco, erro=False):
    metricas["total_requisicoes"] += 1
    metricas["latencias"].append(latencia_ms)

    if erro:
        metricas["erros"] += 1

    if risco == "alto":
        metricas["prompts_alto_risco"] += 1
    else:
        metricas["prompts_baixo_risco"] += 1

# %%
atualizar_metricas(120, "baixo")
metricas

# %% [markdown]
# ---
# # 5.3 Integrando métricas ao endpoint

from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM
import time
import uuid

model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
modelo = TFAutoModelForSeq2SeqLM.from_pretrained(model_name)

def inferencia(prompt):
    tokens = tokenizer(prompt, return_tensors="tf")
    output = modelo.generate(**tokens, max_length=120)
    return tokenizer.decode(output[0], skip_special_tokens=True)

def endpoint_monitorado(prompt):
    inicio = time.time()
    req_id = str(uuid.uuid4())

    try:
        resposta = inferencia(prompt)
        erro = False
    except Exception:
        resposta = "Erro interno."
        erro = True

    fim = time.time()
    latencia = round((fim - inicio) * 1000, 2)

    risco = "alto" if any(p in prompt.lower() for p in ["bomba", "hackear", "arma"]) else "baixo"

    atualizar_metricas(latencia, risco, erro)

    return {
        "request_id": req_id,
        "prompt": prompt,
        "resposta": resposta,
        "latencia_ms": latencia,
        "risco": risco,
        "erro": erro
    }

# %%
endpoint_monitorado("Explique o que é aprendizado supervisionado.")

# %% [markdown]
# ---
# # 5.4 Criando um painel de métricas (simulado)

def painel_metricas():
    if metricas["latencias"]:
        lat_media = sum(metricas["latencias"]) / len(metricas["latencias"])
        lat_max = max(metricas["latencias"])
        lat_min = min(metricas["latencias"])
    else:
        lat_media = lat_max = lat_min = 0

    return {
        "total_requisicoes": metricas["total_requisicoes"],
        "latencia_media_ms": round(lat_media, 2),
        "latencia_max_ms": round(lat_max, 2),
        "latencia_min_ms": round(lat_min, 2),
        "erros": metricas["erros"],
        "prompts_alto_risco": metricas["prompts_alto_risco"],
        "prompts_baixo_risco": metricas["prompts_baixo_risco"]
    }

# %%
painel_metricas()

# %% [markdown]
# ---
# # 5.5 Simulando tráfego real

prompts_teste = [
    "Explique IA.",
    "Explique RLHF.",
    "Como hackear um banco?",
    "Explique transformers.",
    "Como fazer uma bomba?",
    "Explique deep learning."
]

for p in prompts_teste:
    endpoint_monitorado(p)

painel_metricas()

# %% [markdown]
# ---
# # 5.6 Métricas essenciais em produção
#
# ## 🟦 1. Latência
# - média
# - p95
# - p99
#
# ## 🟩 2. Throughput
# - requisições por segundo
#
# ## 🟧 3. Erros
# - taxa de erro
# - tipos de erro
#
# ## 🟥 4. Segurança
# - prompts perigosos
# - tentativas de jailbreak
#
# ## 🟨 5. Alucinações
# - taxa de inconsistência
# - verificações factuais
#
# ## 🟪 6. Uso
# - número de usuários
# - volume de requisições
#
# ---
#
# # 5.7 Conclusão desta parte
#
# ✔️ Você aprendeu o que é monitoramento  
# ✔️ Criou um sistema de métricas real  
# ✔️ Mediu latência, erros e risco  
# ✔️ Criou um painel de métricas  
# ✔️ Simulou tráfego real  
#
# Agora estamos prontos para:
#
# **PARTE 6 — Observabilidade Completa (logs + métricas + traces).**

# %% [markdown]
# <a id="observabilidade"></a>
# # 6. Observabilidade Completa
#
# Observabilidade é a união de:
#
# - **Logs** → o que aconteceu  
# - **Métricas** → como está o sistema  
# - **Traces** → por onde a requisição passou  
#
# Em sistemas modernos, isso é feito com:
# - Grafana
# - Prometheus
# - OpenTelemetry
# - Datadog
# - Elastic Stack (ELK)
#
# Aqui vamos construir uma **versão simplificada**, mas funcional.
#
# ---
#
# # 6.1 O que são traces?
#
# Traces são registros detalhados do caminho de uma requisição:
#
# ```
# requisição → validação → inferência → segurança → resposta
# ```
#
# Cada etapa é um **span**.
#
# Vamos simular isso.
#
# ---
#
# # 6.2 Criando um coletor de traces

import time
import uuid

traces = []

def iniciar_trace():
    trace_id = str(uuid.uuid4())
    return {"trace_id": trace_id, "spans": []}

def registrar_span(trace, nome, inicio, fim):
    trace["spans"].append({
        "nome": nome,
        "duracao_ms": round((fim - inicio) * 1000, 2)
    })

def finalizar_trace(trace):
    traces.append(trace)

# %%
t = iniciar_trace()
registrar_span(t, "teste", 0, 0.1)
finalizar_trace(t)
traces[-1]

# %% [markdown]
# ---
# # 6.3 Integrando traces ao endpoint

from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM

model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
modelo = TFAutoModelForSeq2SeqLM.from_pretrained(model_name)

def inferencia(prompt):
    tokens = tokenizer(prompt, return_tensors="tf")
    output = modelo.generate(**tokens, max_length=120)
    return tokenizer.decode(output[0], skip_special_tokens=True)

def endpoint_observavel(prompt):
    trace = iniciar_trace()

    # Span 1 — validação
    ini = time.time()
    if not prompt:
        fim = time.time()
        registrar_span(trace, "validacao", ini, fim)
        finalizar_trace(trace)
        return {"erro": "Prompt vazio."}
    fim = time.time()
    registrar_span(trace, "validacao", ini, fim)

    # Span 2 — inferência
    ini = time.time()
    resposta = inferencia(prompt)
    fim = time.time()
    registrar_span(trace, "inferencia", ini, fim)

    # Span 3 — segurança
    ini = time.time()
    risco = "alto" if any(p in prompt.lower() for p in ["bomba", "hackear", "arma"]) else "baixo"
    fim = time.time()
    registrar_span(trace, "seguranca", ini, fim)

    finalizar_trace(trace)

    return {
        "prompt": prompt,
        "resposta": resposta,
        "risco": risco,
        "trace_id": trace["trace_id"],
        "spans": trace["spans"]
    }

# %%
endpoint_observavel("Explique o que é aprendizado supervisionado.")

# %% [markdown]
# ---
# # 6.4 Criando um analisador de traces

def analisar_traces():
    total = len(traces)
    if total == 0:
        return {}

    duracoes = []
    for t in traces:
        for s in t["spans"]:
            duracoes.append(s["duracao_ms"])

    return {
        "total_traces": total,
        "media_duracao_span_ms": round(sum(duracoes) / len(duracoes), 2),
        "max_duracao_span_ms": max(duracoes),
        "min_duracao_span_ms": min(duracoes)
    }

# %%
analisar_traces()

# %% [markdown]
# ---
# # 6.5 Observabilidade = Logs + Métricas + Traces
#
# Agora temos:
#
# - **Logs** → histórico detalhado  
# - **Métricas** → visão agregada  
# - **Traces** → visão granular  
#
# Isso permite:
# - detectar gargalos  
# - identificar falhas  
# - entender comportamento  
# - auditar decisões  
# - investigar incidentes  
#
# ---
#
# # 6.6 Criando um painel completo (simulado)

def painel_observabilidade():
    return {
        "metricas": {
            "total_requisicoes": metricas["total_requisicoes"],
            "latencia_media_ms": round(sum(metricas["latencias"]) / len(metricas["latencias"]), 2) if metricas["latencias"] else 0,
            "erros": metricas["erros"],
            "prompts_alto_risco": metricas["prompts_alto_risco"],
        },
        "logs_registrados": len(logs),
        "traces_registrados": len(traces),
        "analise_traces": analisar_traces()
    }

# %%
painel_observabilidade()

# %% [markdown]
# ---
# # 6.7 Conclusão desta parte
#
# ✔️ Você aprendeu o que é observabilidade  
# ✔️ Criou traces reais  
# ✔️ Integrado logs + métricas + traces  
# ✔️ Criou um painel completo  
# ✔️ Entendeu como empresas monitoram modelos em produção  
#
# Agora estamos prontos para:
#
# **PARTE 7 — Rollback, Versionamento e Hotfix de Modelos.**

# %% [markdown]
# <a id="rollback"></a>
# # 7. Rollback, Versionamento e Hotfix
#
# Em produção, modelos precisam ser:
# - atualizados
# - corrigidos
# - revertidos
# - versionados
#
# E tudo isso **sem parar o sistema**.
#
# ---
#
# # 7.1 Por que rollback é essencial?
#
# Imagine que você:
# - treinou um novo modelo
# - fez deploy
# - e de repente:
#   - latência aumenta
#   - alucinações disparam
#   - segurança falha
#   - usuários reclamam
#
# Você precisa **voltar imediatamente** para a versão anterior.
#
# Isso é rollback.
#
# ---
#
# # 7.2 Criando um sistema de versionamento simples
#
# Vamos simular múltiplas versões de modelo.

modelos = {
    "v1": "Modelo simples — rápido, mas menos preciso.",
    "v2": "Modelo intermediário — mais preciso, mas mais lento.",
    "v3": "Modelo avançado — melhor qualidade, mas pode alucinar mais."
}

versao_ativa = "v1"

# %%
versao_ativa, modelos[versao_ativa]

# %% [markdown]
# ---
# # 7.3 Função para trocar de versão (deploy)

def trocar_versao(nova_versao):
    global versao_ativa
    if nova_versao not in modelos:
        return f"Erro: versão {nova_versao} não existe."
    versao_ativa = nova_versao
    return f"Versão ativa agora é {versao_ativa}."

# %%
trocar_versao("v2")

# %% [markdown]
# ---
# # 7.4 Criando rollback automático
#
# Critério:
# - se latência > 2000 ms
# - ou taxa de erro > 10%
# - ou prompts perigosos aumentam
#
# → rollback para versão anterior

metricas_producao = {
    "latencia_media": 150,
    "taxa_erro": 0.02,
    "prompts_alto_risco": 3
}

historico_versoes = ["v1"]

def verificar_rollback():
    if metricas_producao["latencia_media"] > 2000:
        return True
    if metricas_producao["taxa_erro"] > 0.10:
        return True
    if metricas_producao["prompts_alto_risco"] > 20:
        return True
    return False

def rollback():
    global versao_ativa
    if len(historico_versoes) < 1:
        return "Nenhuma versão anterior disponível."
    versao_ativa = historico_versoes[-1]
    return f"Rollback realizado. Versão ativa: {versao_ativa}"

# %%
verificar_rollback()

# %% [markdown]
# ---
# # 7.5 Simulando um problema em produção

metricas_producao["latencia_media"] = 3500  # latência explodiu

if verificar_rollback():
    rollback()

# %%
versao_ativa

# %% [markdown]
# ---
# # 7.6 Criando hotfix (correção rápida)
#
# Hotfix é uma correção aplicada **sem trocar de versão**.
#
# Exemplo:
# - bloquear um prompt perigoso
# - ajustar um parâmetro
# - corrigir um bug no endpoint

hotfixes = []

def aplicar_hotfix(descricao):
    hotfixes.append(descricao)
    return f"Hotfix aplicado: {descricao}"

# %%
aplicar_hotfix("Bloqueio adicional para prompts de hacking.")

# %% [markdown]
# ---
# # 7.7 Sistema completo de versionamento + rollback + hotfix

def status_sistema():
    return {
        "versao_ativa": versao_ativa,
        "historico_versoes": historico_versoes,
        "hotfixes": hotfixes,
        "metricas": metricas_producao
    }

# %%
status_sistema()

# %% [markdown]
# ---
# # 7.8 Como empresas fazem rollback de verdade?
#
# ## 🟦 1. Blue‑Green Deploy
# - duas versões rodando ao mesmo tempo  
# - tráfego muda instantaneamente
#
# ## 🟩 2. Canary Deploy
# - nova versão recebe 1% do tráfego  
# - se tudo ok → aumenta  
# - se falhar → rollback automático
#
# ## 🟧 3. Shadow Deploy
# - nova versão recebe tráfego duplicado  
# - mas não responde ao usuário  
# - serve apenas para teste
#
# ## 🟥 4. Feature Flags
# - ativa/desativa recursos sem redeploy
#
# ---
#
# # 7.9 Conclusão desta parte
#
# ✔️ Você aprendeu rollback  
# ✔️ Criou um sistema de versionamento  
# ✔️ Simulou falhas em produção  
# ✔️ Implementou rollback automático  
# ✔️ Criou hotfixes  
# ✔️ Entendeu Blue‑Green, Canary e Shadow Deploy  
#
# Agora estamos prontos para:
#
# **PARTE 8 — Projeto Final: Deploy Completo com Monitoramento e Observabilidade.**

# %% [markdown]
# <a id="projeto"></a>
# # 8. Projeto Final — Deploy Completo com Monitoramento e Observabilidade
#
# Neste projeto, você vai montar um sistema completo de inferência:
#
# - endpoint de modelo
# - logging estruturado
# - métricas de produção
# - traces (observabilidade)
# - detecção de risco
# - painel operacional
# - versionamento e rollback
#
# Tudo integrado em um único pipeline.
#
# ---
#
# # 8.1 Setup do modelo

from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM
import time, uuid, json

model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
modelo = TFAutoModelForSeq2SeqLM.from_pretrained(model_name)

# %% [markdown]
# ---
# # 8.2 Estruturas globais do sistema

logs = []
metricas = {
    "total_requisicoes": 0,
    "latencias": [],
    "erros": 0,
    "prompts_alto_risco": 0,
    "prompts_baixo_risco": 0
}
traces = []

versoes = {
    "v1": model_name,
    "v2": model_name,  # simulação
}
versao_ativa = "v1"
historico_versoes = ["v1"]
hotfixes = []

# %% [markdown]
# ---
# # 8.3 Funções auxiliares: risco, logs, métricas, traces

def classificar_risco(prompt):
    perigos = ["bomba", "arma", "hackear", "machucar"]
    return "alto" if any(p in prompt.lower() for p in perigos) else "baixo"

def registrar_log(evento):
    logs.append(evento)

def atualizar_metricas(latencia, risco, erro=False):
    metricas["total_requisicoes"] += 1
    metricas["latencias"].append(latencia)
    if erro:
        metricas["erros"] += 1
    if risco == "alto":
        metricas["prompts_alto_risco"] += 1
    else:
        metricas["prompts_baixo_risco"] += 1

def iniciar_trace():
    return {"trace_id": str(uuid.uuid4()), "spans": []}

def registrar_span(trace, nome, inicio, fim):
    trace["spans"].append({
        "nome": nome,
        "duracao_ms": round((fim - inicio) * 1000, 2)
    })

def finalizar_trace(trace):
    traces.append(trace)

# %% [markdown]
# ---
# # 8.4 Função de inferência

def inferencia(prompt):
    tokens = tokenizer(prompt, return_tensors="tf")
    output = modelo.generate(**tokens, max_length=120)
    return tokenizer.decode(output[0], skip_special_tokens=True)

# %% [markdown]
# ---
# # 8.5 Endpoint completo com:
# - validação
# - inferência
# - segurança
# - logging
# - métricas
# - traces

def endpoint_completo(prompt):
    trace = iniciar_trace()
    req_id = str(uuid.uuid4())

    # Validação
    ini = time.time()
    if not prompt:
        fim = time.time()
        registrar_span(trace, "validacao", ini, fim)
        finalizar_trace(trace)
        return {"erro": "Prompt vazio."}
    fim = time.time()
    registrar_span(trace, "validacao", ini, fim)

    # Inferência
    ini = time.time()
    try:
        resposta = inferencia(prompt)
        erro = False
    except Exception:
        resposta = "Erro interno."
        erro = True
    fim = time.time()
    registrar_span(trace, "inferencia", ini, fim)

    # Segurança
    ini = time.time()
    risco = classificar_risco(prompt)
    fim = time.time()
    registrar_span(trace, "seguranca", ini, fim)

    # Finalizar trace
    finalizar_trace(trace)

    # Métricas
    latencia = sum(s["duracao_ms"] for s in trace["spans"])
    atualizar_metricas(latencia, risco, erro)

    # Log
    evento = {
        "timestamp": time.time(),
        "request_id": req_id,
        "prompt": prompt,
        "resposta": resposta,
        "latencia_ms": latencia,
        "risco": risco,
        "versao": versao_ativa
    }
    registrar_log(evento)

    return {
        "request_id": req_id,
        "resposta": resposta,
        "risco": risco,
        "latencia_ms": latencia,
        "trace_id": trace["trace_id"],
        "versao": versao_ativa
    }

# %%
endpoint_completo("Explique o que é aprendizado supervisionado.")

# %% [markdown]
# ---
# # 8.6 Painel de Observabilidade Completo

def painel_observabilidade():
    latencias = metricas["latencias"]
    lat_media = sum(latencias) / len(latencias) if latencias else 0

    return {
        "versao_ativa": versao_ativa,
        "metricas": {
            "total_requisicoes": metricas["total_requisicoes"],
            "latencia_media_ms": round(lat_media, 2),
            "erros": metricas["erros"],
            "prompts_alto_risco": metricas["prompts_alto_risco"],
        },
        "logs_registrados": len(logs),
        "traces_registrados": len(traces),
        "hotfixes": hotfixes
    }

# %%
painel_observabilidade()

# %% [markdown]
# ---
# # 8.7 Sistema de Rollback e Hotfix

def trocar_versao(nova):
    global versao_ativa
    if nova not in versoes:
        return "Versão inexistente."
    historico_versoes.append(versao_ativa)
    versao_ativa = nova
    return f"Versão ativa agora é {versao_ativa}."

def rollback():
    global versao_ativa
    if not historico_versoes:
        return "Nenhuma versão anterior."
    versao_ativa = historico_versoes.pop()
    return f"Rollback realizado. Versão ativa: {versao_ativa}"

def aplicar_hotfix(descricao):
    hotfixes.append(descricao)
    return f"Hotfix aplicado: {descricao}"

# %%
trocar_versao("v2")
rollback()
aplicar_hotfix("Filtro extra para prompts perigosos.")

# %% [markdown]
# ---
# # 8.8 Conclusão do Projeto Final
#
# ✔️ Você construiu um endpoint completo  
# ✔️ Implementou logging estruturado  
# ✔️ Criou métricas de produção  
# ✔️ Implementou traces (observabilidade)  
# ✔️ Criou painel operacional  
# ✔️ Implementou versionamento, rollback e hotfix  
# ✔️ Montou um sistema de produção funcional  
#
# ---
#
# # 🎉 FIM DO MÓDULO 20  
# E com isso, você conclui o último módulo técnico da formação.
#
# O próximo passo é o **ENCERRAMENTO DA FORMAÇÃO**.
