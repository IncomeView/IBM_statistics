import os
import pathlib

# Pega a versão da tag no GitHub Actions
version = os.getenv("GITHUB_REF_NAME")

# Se estiver rodando localmente (sem tag), define uma versão padrão
if not version:
    version = "v0.0.0"

# Remove o "v" se quiser só o número
clean_version = version.lstrip("v")

# Escreve no arquivo VERSION
pathlib.Path("VERSION").write_text(clean_version)

print(f"Versão gerada: {clean_version}")
