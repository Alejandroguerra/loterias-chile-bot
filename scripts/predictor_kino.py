# ==============================================================================
# PREDICTOR ESTADÍSTICO KINO CHILE (MINERÍA DE DUPLAS Y TRÍOS)
# ==============================================================================
import csv
from itertools import combinations
from collections import Counter
import random

class PredictorKinoCloud:
    def __init__(self, ruta_csv):
        self.historico = []
        self.frecuencia_duplas = Counter()
        self._analizar(ruta_csv)

    def _analizar(self, ruta):
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                lector = csv.reader(f)
                next(lector)
                for fila in lector:
                    if len(fila) < 14: continue
                    try:
                        nums = sorted([int(x) for x in fila[-14:]])
                    except ValueError:
                        continue
                    self.historico.append(frozenset(nums))
                    for dupla in combinations(nums, 2):
                        self.frecuencia_duplas[dupla] += 1
            self.top_duplas = [e for e, c in self.frecuencia_duplas.most_common(40)]
        except FileNotFoundError:
            print(f"No se encontró el archivo en {ruta}")

    def generar(self, cantidad=5):
        jugadas = []
        while len(jugadas) < cantidad:
            comb = set(random.choice(self.top_duplas))
            while len(comb) < 14:
                comb.add(random.randint(1, 25))
            
            nums = sorted(list(comb))
            consec = 1
            valido = True
            for i in range(1, len(nums)):
                if nums[i] == nums[i-1] + 1:
                    consec += 1
                    if consec > 3:
                        valido = False
                        break
                else:
                    consec = 1
            
            if not valido or frozenset(comb) in self.historico:
                continue
            if comb not in [set(j) for j in jugadas]:
                jugadas.append(comb)
        return [sorted(list(j)) for j in jugadas]
