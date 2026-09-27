# ==============================================================================
# PREDICTOR ESTADÍSTICO LOTO CHILE (ROBUSTO)
# ==============================================================================
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
                    # Limpiar celdas vacías o filas muy cortas
                    fila_limpia = [x.strip() for x in fila if x.strip()]
                    if len(fila_limpia) < 6: 
                        continue
                    
                    # Intentar extraer los últimos 6 elementos que sean números enteros válidos
                    try:
                        nums = []
                        for x in fila_limpia[-6:]:
                            nums.append(int(x))
                        nums.sort()
                        self.historico.append(frozenset(nums))
                        for trio in combinations(nums, 3):
                            self.frecuencia_trios[trio] += 1
                    except ValueError:
                        continue # Salta filas de encabezados o textos que no sean números
                        
            self.top_trios = [e for e, c in self.frecuencia_trios.most_common(30)]
            if not self.top_trios:
                # Fallback por si el archivo no tiene suficientes datos procesables
                self.top_trios = [tuple(range(1, 4))]
        except Exception as e:
            print(f"Error leyendo Loto: {e}")
            self.top_trios = []

    def generar(self, cantidad=5):
        if not self.top_trios: return []
        jugadas = []
        while len(jugadas) < cantidad:
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
        return [sorted(list(j)) for j in jugadas]
