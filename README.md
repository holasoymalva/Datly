# Datly - Asistente Inteligente para Análisis de Datos 🤖📊

Datly es una herramienta potente que combina la interfaz intuitiva de Streamlit con la inteligencia de Claude para ayudar a los analistas de datos en su trabajo diario.

## 🚀 Características Principales

- 📊 Exploración automática de datos
- ❓ Consultas en lenguaje natural
- 📝 Generación automática de reportes
- 🔍 Detección de anomalías
- 📈 Visualización inteligente de datos

## 📋 Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git
- Una clave API de Anthropic (Claude)

## 🛠️ Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/Datly.git
cd Datly
```

2. **Crear y activar un entorno virtual**

En Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

En macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

## 📁 Estructura del Proyecto
```
Datly/
├── .streamlit/
│   └── config.toml
├── src/
│   ├── __init__.py
│   ├── analysis.py
│   ├── visualization.py
│   └── utils.py
├── tests/
│   └── __init__.py
├── .gitignore
├── requirements.txt
├── README.md
└── app.py
```

## 📝 Archivo requirements.txt
```
streamlit>=1.31.0
pandas>=2.0.0
anthropic>=0.7.0
plotly>=5.18.0
numpy>=1.24.0
python-dotenv>=1.0.0
openpyxl>=3.1.0
```

## ⚙️ Configuración

1. **Crear archivo .env**
```bash
touch .env  # En Windows: type nul > .env
```

2. **Agregar las variables de entorno**
```env
ANTHROPIC_API_KEY=tu_clave_api_aquí
```

3. **Configurar Streamlit (opcional)**

Crear archivo `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

[server]
port = 8501
enableCORS = false
```

## 🚀 Ejecución

1. **Activar el entorno virtual** (si no está activado)
```bash
source venv/bin/activate  # En Windows: .\venv\Scripts\activate
```

2. **Ejecutar la aplicación**
```bash
streamlit run app.py
```

La aplicación estará disponible en `http://localhost:8501`

## 🧪 Testing

Para ejecutar las pruebas:
```bash
python -m pytest tests/
```

## 📊 Uso Básico

1. Accede a la aplicación a través de tu navegador
2. Carga tu archivo de datos (CSV o Excel)
3. Selecciona el módulo que deseas utilizar
4. Sigue las instrucciones en pantalla para cada funcionalidad

## 🔒 Seguridad

- No almacenes tu clave API directamente en el código
- Utiliza variables de entorno para las credenciales
- Revisa regularmente los permisos de acceso
- Mantén todas las dependencias actualizadas

## 🤝 Contribución

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Logs y Monitoreo

La aplicación genera logs en `logs/Datly.log`. Configura la rotación de logs y monitoreo según tus necesidades.

```python
# Ejemplo de configuración de logging
import logging

logging.basicConfig(
    filename='logs/Datly.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

## 🐳 Docker (Opcional)

También puedes ejecutar la aplicación en Docker:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
```

Para construir y ejecutar:
```bash
docker build -t Datly .
docker run -p 8501:8501 Datly
```

## ⚠️ Solución de Problemas Comunes

1. **Error al cargar la API key**
   - Verifica que el archivo .env existe y contiene la clave
   - Asegúrate de que la clave API es válida

2. **Problemas con la carga de archivos**
   - Verifica que el formato del archivo es compatible
   - Comprueba los permisos de lectura

3. **Errores de memoria**
   - Considera usar chunks para archivos grandes
   - Ajusta la configuración de memoria en Streamlit

## 📚 Recursos Adicionales

- [Documentación de Streamlit](https://docs.streamlit.io/)
- [API de Anthropic](https://docs.anthropic.com/)
- [Guía de Plotly](https://plotly.com/python/)

## 📫 Soporte

Para reportar problemas o sugerir mejoras:
1. Abre un issue en GitHub
2. Envía un correo a support@Datly.com
3. Únete a nuestro canal de Discord

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

Desarrollado con ❤️ por el equipo de Datly