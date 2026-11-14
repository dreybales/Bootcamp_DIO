# ======================================================================
# 🧠 GERADOR AUTOMÁTICO DE PROMPTS - MARCA: DREYBALES
# ======================================================================
# Desenvolvido por: André (dreybales)
# Objetivo: Praticar templates estruturados e f-strings com Python.

print("=" * 65)
print("          🤖 GERADOR DE PROMPTS ESTRUTURADOS DO DREY 🤖          ")
print("=" * 65)
print("Qual template você deseja montar hoje?")
print("1. Plano de Desenvolvimento Pessoal (6 Meses)")
print("2. Simulação de Entrevista de Emprego")
print("=" * 65)

opcao = int(input("Digite 1 ou 2 para escolher o template: "))
print("-" * 65)

if opcao == 1:
    foco = input("Qual será o foco principal (ex: Cibersegurança com Python)? ")
    tempo = input("Qual sua disponibilidade diária (ex: 1 hora por dia)? ")
    
    print("\n" + "=" * 65)
    print("📋 COPIE O PROMPT GERADO ABAIXO:")
    print("=" * 65)
    print(f"Crie um plano detalhado de desenvolvimento para os próximos 6 meses.")
    print(f"- Foco: {foco}")
    print(f"- Limitações de tempo: {tempo}")
    print("Estruture com: 1. Metas mensuráveis, 2. Cronograma semanal e 3. Estratégias para superar obstáculos.")

elif opcao == 2:
    cargo = input("Para qual cargo você quer simular a entrevista? ")
    nivel = input("Qual o nível da vaga (ex: Júnior / Iniciante)? ")
    
    print("\n" + "=" * 65)
    print("📋 COPIE O PROMPT GERADO ABAIXO:")
    print("=" * 65)
    print(f"Atue como um recrutador e simule uma entrevista de emprego.")
    print(f"- Cargo desejado: {cargo}")
    print(f"- Nível de senioridade: {nivel}")
    print("Passo 1: Faça apenas a primeira pergunta mais provável para essa vaga e aguarde minha resposta.")

else:
    print("❌ ALERTA: Opção inválida! Rode novamente e digite apenas 1 ou 2.")

print("=" * 65)
print("             SISTEMA FINALIZADO - MARCA: DREYBALES             ")
print("=" * 65)
