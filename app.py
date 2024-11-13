import streamlit as st
import pandas as pd
import anthropic
from io import StringIO
import plotly.express as px
import json

st.set_page_config(page_title="Asistente de Análisis de Datos", layout="wide")

# Configuración de la API de Anthropic
def initialize_claude():
    if 'ANTHROPIC_API_KEY' not in st.secrets:
        st.error("Por favor configura tu API key de Anthropic en los secrets")
        return None
    return anthropic.Client(api_key=st.secrets['ANTHROPIC_API_KEY'])

# Función para analizar datos con Claude
def analyze_data_with_claude(client, data_description, question):
    prompt = f"""Actúa como un experto analista de datos. 
    Datos disponibles: {data_description}
    
    Pregunta del usuario: {question}
    
    Por favor proporciona un análisis detallado y recomendaciones."""
    
    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        temperature=0,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content

def main():
    st.title("🤖 Asistente Inteligente para Análisis de Datos")
    
    # Sidebar para configuración
    st.sidebar.header("Configuración")
    
    # Módulos disponibles
    modules = {
        "📊 Exploración de Datos": "explore",
        "❓ Consultas en Lenguaje Natural": "query",
        "📝 Generación de Reportes": "report",
        "🔍 Detección de Anomalías": "anomalies",
        "📈 Visualización Automática": "viz"
    }
    
    selected_module = st.sidebar.radio("Selecciona un módulo", list(modules.keys()))
    
    # Carga de datos
    uploaded_file = st.file_uploader("Carga tu archivo CSV o Excel", type=['csv', 'xlsx'])
    
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            st.success("Archivo cargado exitosamente!")
            
            # Módulo de Exploración de Datos
            if modules[selected_module] == "explore":
                st.header("Exploración de Datos")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("Información General")
                    buffer = StringIO()
                    df.info(buf=buffer)
                    st.text(buffer.getvalue())
                
                with col2:
                    st.subheader("Estadísticas Descriptivas")
                    st.write(df.describe())
                
                st.subheader("Primeras Filas")
                st.write(df.head())
                
                # Detección automática de tipos de columnas
                numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
                categorical_cols = df.select_dtypes(include=['object']).columns
                
                st.subheader("Distribuciones")
                selected_col = st.selectbox("Selecciona una columna para visualizar", numeric_cols)
                fig = px.histogram(df, x=selected_col)
                st.plotly_chart(fig)
            
            # Módulo de Consultas en Lenguaje Natural
            elif modules[selected_module] == "query":
                st.header("Consultas en Lenguaje Natural")
                
                client = initialize_claude()
                if client:
                    data_description = f"""
                    Columnas disponibles: {', '.join(df.columns)}
                    Tipos de datos: {df.dtypes.to_dict()}
                    Resumen estadístico: {df.describe().to_dict()}
                    """
                    
                    user_question = st.text_input("¿Qué te gustaría saber sobre tus datos?")
                    
                    if user_question:
                        with st.spinner("Analizando..."):
                            analysis = analyze_data_with_claude(client, data_description, user_question)
                            st.write(analysis)
            
            # Módulo de Generación de Reportes
            elif modules[selected_module] == "report":
                st.header("Generación Automática de Reportes")
                
                report_type = st.selectbox("Tipo de reporte", 
                    ["Resumen Ejecutivo", "Análisis Detallado", "Reporte Técnico"])
                
                if st.button("Generar Reporte"):
                    with st.spinner("Generando reporte..."):
                        # Aquí se integraría la generación del reporte con Claude
                        st.success("Reporte generado!")
            
            # Módulo de Detección de Anomalías
            elif modules[selected_module] == "anomalies":
                st.header("Detección de Anomalías")
                
                selected_col = st.selectbox("Selecciona una columna para analizar", numeric_cols)
                
                if st.button("Detectar Anomalías"):
                    # Implementar detección de anomalías usando métodos estadísticos
                    Q1 = df[selected_col].quantile(0.25)
                    Q3 = df[selected_col].quantile(0.75)
                    IQR = Q3 - Q1
                    outliers = df[(df[selected_col] < (Q1 - 1.5 * IQR)) | 
                                (df[selected_col] > (Q3 + 1.5 * IQR))]
                    
                    st.write(f"Se encontraron {len(outliers)} posibles anomalías")
                    st.write(outliers)
            
            # Módulo de Visualización Automática
            elif modules[selected_module] == "viz":
                st.header("Visualización Automática")
                
                viz_type = st.selectbox("Tipo de visualización", 
                    ["Scatter Plot", "Line Plot", "Bar Chart", "Box Plot"])
                
                col1, col2 = st.columns(2)
                
                with col1:
                    x_col = st.selectbox("Eje X", df.columns)
                
                with col2:
                    y_col = st.selectbox("Eje Y", numeric_cols)
                
                if viz_type == "Scatter Plot":
                    fig = px.scatter(df, x=x_col, y=y_col)
                elif viz_type == "Line Plot":
                    fig = px.line(df, x=x_col, y=y_col)
                elif viz_type == "Bar Chart":
                    fig = px.bar(df, x=x_col, y=y_col)
                else:
                    fig = px.box(df, x=x_col, y=y_col)
                
                st.plotly_chart(fig)
                
        except Exception as e:
            st.error(f"Error al procesar el archivo: {str(e)}")

if __name__ == "__main__":
    main()