import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/ventas.csv')
print(df.head())
print("Promedio de ventas: ", df['ventas'].mean())

plt.plot(df["mes"], df["ventas"], marker="o")
plt.title("Ventas mensuales")
plt.xlabel("Mes")
plt.ylabel("Ventas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_ventas.png")