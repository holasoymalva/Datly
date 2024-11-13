import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configurar seed para reproducibilidad
np.random.seed(42)

# Generar fechas
start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 12, 31)
dates = pd.date_range(start=start_date, end=end_date, freq='D')

# Crear datos base
data = {
    'Fecha': dates,
    'Region': np.random.choice(['Norte', 'Sur', 'Este', 'Oeste', 'Centro'], len(dates)),
    'Categoria_Producto': np.random.choice(['Electrónicos', 'Muebles', 'Ropa', 'Alimentos', 'Deportes'], len(dates)),
    'Vendedor': np.random.choice(['Juan Pérez', 'María García', 'Carlos López', 'Ana Martínez', 'Pedro Sánchez'], len(dates))
}

# Generar ventas base con estacionalidad y tendencia
base_sales = np.random.normal(10000, 2000, len(dates))
seasonal_pattern = np.sin(np.linspace(0, 4*np.pi, len(dates))) * 2000
trend = np.linspace(0, 3000, len(dates))
data['Ventas'] = base_sales + seasonal_pattern + trend

# Agregar costos y márgenes
data['Costo_Producto'] = data['Ventas'] * np.random.uniform(0.4, 0.6, len(dates))
data['Gastos_Operativos'] = data['Ventas'] * np.random.uniform(0.1, 0.2, len(dates))
data['Gastos_Marketing'] = data['Ventas'] * np.random.uniform(0.05, 0.1, len(dates))
data['Gastos_Administrativos'] = data['Ventas'] * np.random.uniform(0.08, 0.12, len(dates))

# Calcular métricas financieras
data['Margen_Bruto'] = data['Ventas'] - data['Costo_Producto']
data['EBITDA'] = data['Margen_Bruto'] - data['Gastos_Operativos'] - data['Gastos_Marketing'] - data['Gastos_Administrativos']
data['Margen_Neto'] = data['EBITDA'] * 0.7  # Simulando impuestos y otros gastos

# Agregar KPIs de ventas
data['Unidades_Vendidas'] = np.round(data['Ventas'] / np.random.uniform(100, 200, len(dates)))
data['Devolucion_Producto'] = np.round(data['Unidades_Vendidas'] * np.random.uniform(0, 0.05, len(dates)))
data['Satisfaccion_Cliente'] = np.random.uniform(3.5, 5, len(dates))

# Crear DataFrame
df = pd.DataFrame(data)

# Redondear valores numéricos
columns_to_round = ['Ventas', 'Costo_Producto', 'Gastos_Operativos', 'Gastos_Marketing', 
                    'Gastos_Administrativos', 'Margen_Bruto', 'EBITDA', 'Margen_Neto']
df[columns_to_round] = df[columns_to_round].round(2)

# Ordenar por fecha
df = df.sort_values('Fecha')

# Guardar en CSV
df.to_csv('ventas_finanzas_2022_2023.csv', index=False)

# Mostrar las primeras filas y estadísticas básicas
print("\nPrimeras filas del dataset:")
print(df.head())
print("\nEstadísticas descriptivas:")
print(df.describe())
print("\nInformación del dataset:")
print(df.info())