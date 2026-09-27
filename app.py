import streamlit as st
import sys
import os

# Configurar la ruta para importar los scripts de predicción
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'scripts')))

from predictor_loto import PredictorLotoCloud
from predictor_kino import PredictorKinoCloud

st.set_page_config(page_title="Tablero Loterías Chile", page_icon="🎯", layout="centered")

st.title("🎯 Tablero Inteligente de Loterías Chile 🇨🇱")
st.markdown("Generador automático de combinaciones optimizadas para **Loto** y **Kino** basado en minería de datos y estadísticas históricas.")

st.divider()

# --- SECCIÓN LOTO ---
st.header("🎲 Predicciones para LOTO (6 de 41)")
if st.button("Generar Cartillas de Loto"):
    with st.spinner("Analizando histórico y calculando tríos..."):
        try:
            loto_bot = PredictorLotoCloud("datos/loto_historico.csv")
            jugadas_loto = loto_bot.generar(5)
            st.success("¡Top 5 de Loto generado con éxito!")
            for idx, jugada in enumerate(jugadas_loto, 1):
                st.markdown(f"**Cartilla #{idx}:** `{jugada}`")
        except Exception as e:
            st.error(f"No se pudo procesar Loto: {e}")

st.divider()

# --- SECCIÓN KINO ---
st.header("🎯 Predicciones para KINO (14 de 25)")
if st.button("Generar Cartillas de Kino"):
    with st.spinner("Analizando histórico y calculando duplas..."):
        try:
            kino_bot = PredictorKinoCloud("datos/kino_historico_completo.csv")
            jugadas_kino = kino_bot.generar(5)
            st.success("¡Top 5 de Kino generado con éxito!")
            for idx, jugada in enumerate(jugadas_kino, 1):
                st.markdown(f"**Cartilla #{idx}:** `{jugada}`")
        except Exception as e:
            st.error(f"No se pudo procesar Kino: {e}")

st.markdown("---")
st.caption("🚀 Sistema conectado en la nube de GitHub & Streamlit.")
