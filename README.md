# Análisis de Datos Gerencial - Gimnasio

Este repositorio contiene el pipeline de datos y el análisis de inteligencia de negocio (BI) simulado para la gestión de un gimnasio, desarrollado como proyecto de portfolio.

## Stack Tecnológico
* **Procesamiento y ETL:** Python, Pandas.
* **Inteligencia de Negocio:** Power BI, DAX.
* **Control de Versiones:** Git, GitHub.

## Descripción del Proyecto
El proyecto abarca el ciclo completo de los datos:
1. **Generación y Limpieza:** Extracción y modelado de datos transaccionales (Socios, Planes, Pagos) utilizando scripts de Python y la librería Pandas.
2. **Modelado Relacional:** Estructuración de los datos exportados para su consumo analítico.
3. **Visualización y KPIs:** Diseño de un tablero interactivo en Power BI aplicando expresiones DAX para calcular métricas críticas de negocio (ingresos, retención, métodos de pago).

## 📂 Estructura
* `generador_datos.py`: Script de Python para la creación y limpieza del dataset inicial.
* `DB_Gimnasio.xlsx`: Base de datos procesada y lista para ingestar.
* *(Próximamente)* Archivo `.pbix` con el tablero de Power BI.