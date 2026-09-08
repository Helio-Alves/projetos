# Programa para calcular o consumo mensal de energia de um aparelho

nome = input("Nome do aparelho: ")

while True:
    try:
        potencia = input("Potência do aparelho (em Watts): ").replace(",", ".")
        horas = input("Tempo médio de uso diário (em horas): ").replace(",", ".")

        potencia = float(potencia)
        horas_dia = float(horas)

    except ValueError:
        print("\nErro: digite apenas números válidos para potência e horas. Tente novamente.\n")

    else:
        consumo_mensal = (potencia * horas_dia * 30) / 1000  # kWh

        valor_kwh = 0.75  # R$ por kWh
        custo_estimado = consumo_mensal * valor_kwh

        print("\n--- Resultado ---")
        print(f"Aparelho: {nome}")
        print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
        print(f"Custo estimado: R$ {custo_estimado:.2f}/mês")

        break  # sai do loop só quando tudo deu certo