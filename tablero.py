import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'scripts')))

from predictor_loto import PredictorLotoCloud
from predictor_kino import PredictorKinoCloud

def mostrar_tablero():
    print("=" * 60)
    print(" 🎯 TABLERO INTELIGENTE DE COMBINATORIAS - CHILE 🇨🇱")
    print("=" * 60)
    
    print("\n[📊] Analizando histórico de LOTO (6 de 41)...")
    try:
        loto_bot = PredictorLotoCloud("datos/loto_historico.csv")
        jugadas_loto = loto_bot.generar(5)
        print("\n✨ TOP 5 COMBINACIONES RECOMENDADAS PARA LOTO:")
        print("-" * 50)
        for idx, jugada in enumerate(jugadas_loto, 1):
            print(f"  Cartilla Loto #{idx}: {jugada}")
    except Exception as e:
        print(f"  ⚠️ Error en Loto: {e}")

    print("\n" + "=" * 60)
    print("\n[📊] Analizando histórico de KINO (14 de 25)...")
    try:
        kino_bot = PredictorKinoCloud("datos/kino_historico_completo.csv")
        jugadas_kino = kino_bot.generar(5)
        print("\n✨ TOP 5 COMBINACIONES RECOMENDADAS PARA KINO:")
        print("-" * 50)
        for idx, jugada in enumerate(jugadas_kino, 1):
            print(f"  Cartilla Kino #{idx}: {jugada}")
    except Exception as e:
        print(f"  ⚠️ Error en Kino: {e}")
    print("=" * 60)

if __name__ == "__main__":
    mostrar_tablero()
