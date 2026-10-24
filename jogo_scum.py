# ======================================================================
# 🏕️ SIMULADOR DE STATUS - SCUM
# ======================================================================
# Criado por: André (dreybales)

print("=" * 50)
print("     STATUS DE SOBREVIVÊNCIA DO PRISIONEIRO     ")
print("=" * 50)

# Configurando as variáveis do nosso personagem
nome_jogador = "Drey Bales"
energia_fisiologia = 35  # Escala de 0 a 100
esta_infectado = False

print(f"Prisioneiro: {nome_jogador}")
print(f"Nível de Energia: {energia_fisiologia}%")

print("-" * 50)

# Testando a lógica de decisão (Condicionais)
# Bloco 1: Teste da Energia (Tem IF e tem ELSE)
if energia_fisiologia < 80:
    print("ALERTA: Você está exausto! Procure comida e descanse no acampamento.")
else:
    print("STATUS: Pronto para explorar o mapa e caçar suprimentos!")

# Bloco 2: Teste da Infecção (Tem IF e tem ELSE)
if esta_infectado == True:
    print("CUIDADO: Infecção detectada! Use antibióticos imediatamente.")
else:
    print("SAÚDE: Corpo limpo de infecções.")

