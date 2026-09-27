import csv
from itertools import combinations
from collections import Counter
import random

class PredictorLotoCloud:
    def __init__(self, ruta_csv):
        self.historico = []
        self.frecuencia_trios = Counter()
        self._analizar(ruta_csv)

    def _analizar(self, ruta):
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                lector = csv.reader(f)
                for fila in lector:
                    fila_limpia = [x.strip() for x in fila if x.strip()]
                    if len(fila_limpia) < 6: continue
                    try:
                        nums = sorted([int(x) for x in fila_limpia[-6:]])
                        self.historico.append(frozenset(nums))
                        for trio in combinations(nums, 3):
                            self.frecuencia_trios[trio] += 1
                    except ValueError:
                        continue
            self.top_trios = [e for e, c in self.frecuencia_trios.most_common(30)]
            if not self.top_trios:
                self.top_trios = [(1, 2, 3)]
        except Exception:
            self.top_trios = [(1, 2, 3)]

    def generar(self, cantidad=5):
        jugadas = []
        intentos_totales = 0
        while len(jugadas) < cantidad and intentos_totales < 5000:
            intentos_totales += 1
            comb = set(random.choice(self.top_trios))
            while len(comb) < 6:
                comb.add(random.randint(1, 41))
            
            nums = sorted(list(comb))
            consec = 1
            valido = True
            for i in range(1, len(nums)):
                if nums[i] == nums[i-1] + 1:
                    consec += 1
                    if consec > 2: 
                        valido = False
                        break
                else:
                    consec = 1
            
            if not valido or frozenset(comb) in self.historico:
                continue
            if comb not in [set(j) for j in jugadas]:
                jugadas.append(comb)
        
        # Si por alguna razón faltaron jugadas por restricciones, rellenamos de forma rápida
        while len(jugadas) < cantidad:
            fallback = sorted(random.sample(range(1, 42), 6))
            if set(fallback) not in [set(j) for j in jugadas]:
                jugadas.append(set(fallback))
                
        return [sorted(list(j)) for j in jugadas]
