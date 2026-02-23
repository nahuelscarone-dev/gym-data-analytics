import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("Iniciando proceso ETL...")

# ==========================================
# 1. EXTRACCIÓN: GENERACIÓN DE DATOS "SUCIOS"
# ==========================================
np.random.seed(42)

# Socios (con nombres mal escritos y edades faltantes)
ids_socios = range(1001, 1051)
nombres_sucios = [' ANA ', 'juan', 'VICTORIA', ' maxi', 'José', 'pedro ', 'SOFIA', 'lucas', ' María ', 'carlos', 'Agustín']
edades_sucias = np.random.randint(18, 60, size=50).astype(float)
edades_sucias[np.random.choice(50, 5, replace=False)] = np.nan # Metemos 5 valores nulos (NaN)

df_socios = pd.DataFrame({
    'ID_Socio': ids_socios,
    'Nombre': np.random.choice(nombres_sucios, size=50),
    'Edad': edades_sucias,
    'Estado': np.random.choice(['Activo', 'Inactivo'], size=50, p=[0.8, 0.2])
})

# Planes
df_planes = pd.DataFrame({
    'ID_Plan': ['P1', 'P2', 'P3', 'P4'],
    'Nombre_Plan': ['Musculación', 'Pase Libre', 'Crossfit', 'Yoga'],
    'Precio_Mensual': [15000, 22000, 25000, 18000]
})

# Pagos (con métodos de pago inconsistentes)
metodos_sucios = ['efectivo', ' TARJETA', 'Transferencia', 'EFECTIVO ', 'tarjeta', 'TRANSF.']
ids_pago = range(5001, 5061)
socios_pago = np.random.choice(ids_socios, size=60)
planes_pago = np.random.choice(df_planes['ID_Plan'], size=60)
fechas = [datetime(2026, 2, 1) + timedelta(days=np.random.randint(0, 22)) for _ in range(60)]

df_pagos = pd.DataFrame({
    'Ticket_Pago': ids_pago,
    'ID_Socio': socios_pago,
    'ID_Plan': planes_pago,
    'Fecha_Pago': fechas,
    'Metodo_Pago': np.random.choice(metodos_sucios, size=60)
})

# ==========================================
# 2. TRANSFORMACIÓN: LIMPIEZA CON PANDAS (ETL)
# ==========================================

# Limpieza de Socios
# a) Sacamos espacios extra y ponemos la primera letra en mayúscula
df_socios['Nombre'] = df_socios['Nombre'].str.strip().str.title()
# b) Imputamos las edades nulas (NaN) con el promedio de edad del gimnasio
edad_promedio = round(df_socios['Edad'].mean())
df_socios['Edad'] = df_socios['Edad'].fillna(edad_promedio).astype(int)

# Limpieza de Pagos
# a) Estandarizamos los métodos de pago (todo a mayúscula sin espacios)
df_pagos['Metodo_Pago'] = df_pagos['Metodo_Pago'].str.strip().str.upper()
# b) Reemplazamos abreviaturas
df_pagos['Metodo_Pago'] = df_pagos['Metodo_Pago'].replace({'TRANSF.': 'TRANSFERENCIA'})

# ==========================================
# 3. CARGA: EXPORTAMOS LA BASE LIMPIA
# ==========================================
with pd.ExcelWriter('DB_Gimnasio.xlsx') as writer:
    df_socios.to_excel(writer, sheet_name='Socios', index=False)
    df_planes.to_excel(writer, sheet_name='Planes', index=False)
    df_pagos.to_excel(writer, sheet_name='Pagos', index=False)

print("¡Proceso ETL finalizado! Datos limpiados y guardados en 'DB_Gimnasio.xlsx'")