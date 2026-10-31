# ======================================================================
# 🧠 GUIA INTERATIVO DE IA - MARCA: DREYBALES
# ======================================================================
# Desenvolvido por: André (dreybales)
# Objetivo: Praticar inputs, textos estruturados e condicionais.

print("=" * 60)
print("             🤖 BEM-VINDO AO GUIA DE IA DO DREY 🤖             ")
print("=" * 60)
print("Escolha um dos tópicos abaixo para eu te explicar:")
print("1. O que são LLMs (Large Language Models)?")
print("2. O que é Deep Learning (Aprendizado Profundo)?")
print("3. O que significa IA Multimodal?")
print("=" * 60)

# O comando input() captura o número que você digitar no teclado
opcao = int(input("Digite o número da sua opção (1, 2 ou 3): "))

print("-" * 60)

# Testando as condições com o IF, ELIF (Else If) e ELSE
if opcao == 1:
    print("DREY EXPLICA: LLMs são modelos gigantes treinados com bilhões")
    print("de frases da internet. Eles funcionam calculando a probabilidade")
    print("da próxima palavra ideal em um texto. Exemplo: O Gemini!")
elif opcao == 2:
    print("DREY EXPLICA: É um aprendizado baseado em redes neurais artificiais.")
    print("Funciona como várias camadas de filtros que processam dados")
    print("profundos sem precisar que um humano dê regras manuais passo a passo.")
elif opcao == 3:
    print("DREY EXPLICA: É o topo da tecnologia atual! Significa que a IA")
    print("consegue compreender e misturar diferentes tipos de dados ao mesmo")
    print("tempo, como textos, áudios, imagens e até vídeos de uma vez só.")
else:
    print("ALERTA: Opção inválida! Digite apenas 1, 2 ou 3 para rodar o guia.")

print("=" * 60)
print("             FIM DO PROGRAMA - ATÉ A PRÓXIMA!              ")
print("=" * 60)
