#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Carreguem les dades
df = pd.read_csv("mortality.csv")

# Triem les variables a mostrar al contour plot
x = 'Year'
y = 'Age'
z = 'Total'

# Transformem a dades numèriques
df[y] = pd.to_numeric(df[y].str.replace('+', ''), errors='coerce')

# Transformem la variable de morts a escala logarítmica per millorar la visualització
df[z] = np.log1p(df[z])

print(df)

# Creem el contour plot
contour = plt.tricontourf(df[x], df[y], df[z], cmap='viridis')

# Afegim etiquetes
plt.xlabel('Any')
plt.ylabel('Edat')
plt.title(f'Mortalitat per edat a Espanya (1908-2021)')
plt.colorbar(contour, label='Total de mortalitat a escala logarítmica')

# Mostrem el plot
plt.show()
