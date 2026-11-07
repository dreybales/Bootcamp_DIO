# ======================================================================
# 🛡️ MONITOR DE SEGURANÇA: VALIDADOR DE LOGINS SUSPEITOS
# ======================================================================
# Desenvolvido por: André (dreybales)
# Objetivo: Praticar lógica condicional aplicada à Cibersegurança.

print("=" * 60)
print("             🚨 SISTEMA DE DETECÇÃO DE ANOMALIAS 🚨            ")
print("=" * 60)

# Simulando os dados que chegariam de uma tentativa de acesso
usuario = input("Digite o nome de usuário: ")
tentativas_falhas = int(input("Número de tentativas de login falhas: "))
horario_acesso = int(input("Digite a hora atual do acesso (apenas o número de 0 a 23): "))

print("-" * 60)
print(f"Analisando requisição do usuário: {usuario}...")
print("-" * 60)

# Regras de Cibersegurança usando IF, ELIF e ELSE
if tentativas_falhas >= 5:
    print("❌ ALERTA MÁXIMO: Conta bloqueada por excesso de tentativas falhas!")
    print("Motivo: Suspeita de ataque de Força Bruta (Brute Force).")
elif horario_acesso >= 22 or horario_acesso <= 5:
    print("⚠️ ALERTA INTERMEDIÁRIO: Acesso fora do horário comercial permitido.")
    print("Ação: Solicitar verificação de identidade em duas etapas (2FA).")
else:
    print("✅ ACESSO NORMAL: Nenhuma atividade suspeita detectada no momento.")

print("=" * 60)
print("             SISTEMA MONITORANDO - MARCA: DREYBALES            ")
print("=" * 60)
