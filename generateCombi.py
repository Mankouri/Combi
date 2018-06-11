import pandas as pd
import math
import numpy as np
import sys
import time
from multiprocessing import Process
from scipy.spatial import distance
import dask.dataframe as dd


# On charge chaque categorie d'ingredients dans des dataframes differents
df_fruits = pd.read_csv('fruits.csv', sep=';', engine='python')
df_choco = pd.read_csv('choco.csv', sep=';', engine='python')
df_nuts = pd.read_csv('nuts.csv', sep=';', engine='python')
df_seeds = pd.read_csv('seeds.csv', sep=';', engine='python')

# Fusion des dataframes selectionne pour l'ingredient N
ingr_1 = [df_seeds] # Graine
ingr_2 = [df_nuts,df_choco] # Noix ou Choco
ingr_3 = [df_seeds,df_nuts] # Noix ou Graine
ingr_4 = [df_fruits] # Fruits only !
ingr_5 = [df_fruits,df_choco] # Fruits ou Choco

df_ingr_1 = pd.concat(ingr_1, ignore_index=True, join_axes=None, sort=False)
df_ingr_2 = pd.concat(ingr_2, ignore_index=True, join_axes=None, sort=False)
df_ingr_3 = pd.concat(ingr_3, ignore_index=True, join_axes=None, sort=False)
df_ingr_4 = pd.concat(ingr_4, ignore_index=True, join_axes=None, sort=False)
df_ingr_5 = pd.concat(ingr_5, ignore_index=True, join_axes=None, sort=False)

nb=0
for a in range(0, len(df_ingr_1)):
	for b in range(0, len(df_ingr_2)):
		for c in range(a+1, len(df_ingr_3)):
			for d in range(0, len(df_ingr_4)):
				for e in range(d+1, len(df_ingr_5)):
					# Pour eviter les doublons de seed 
					if(df_ingr_1.iloc[a,0] != df_ingr_3.iloc[c,0]):
						# Pour eviter les doublons de noix et choco
						if(df_ingr_2.iloc[b,0] != (df_ingr_3.iloc[c,0] or df_ingr_5.iloc[e,0])):
							# Pour eviter les doublons de fruits
							if(df_ingr_4.iloc[b,0] != df_ingr_5.iloc[e,0]):
								print(str(a)+","+str(b)+","+str(c)+","+str(d)+","+str(e))
								nb+=1

print("Nombre de combinaison: "+ str(nb))
