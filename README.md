# 💱 Dólar Actual - Argentina

**Aplicación de escritorio para consultar tipos de cambio del dólar en Argentina**

Una herramienta completa desarrollada en Python con Tkinter que permite consultar cotizaciones actuales e históricas del dólar en Argentina, realizar conversiones y verificaciones de cálculos.

## 🌟 Características

- **Cotizaciones en tiempo real** de múltiples tipos de dólar (Oficial, Nación, Blue, Mayorista, Turista, MEP, CCL, Cripto)
- **Conversión automática** de USD a ARS con el tipo de cambio seleccionado
- **Verificación de cálculos** con validación de datos ingresados
- **Consulta histórica** con selección de fechas mediante calendario interactivo
- **Interfaz intuitiva** con tres pestañas organizadas
- **Efectos visuales** como parpadeo al actualizar valores

## 📋 Requisitos del Sistema

- **Python 3.7+**
- **Sistema operativo:** Windows, macOS, Linux
- **Conexión a internet** para obtener cotizaciones

## 🚀 Instalación

### Opción 1: Ejecutable (Recomendado)
1. Descarga el archivo `dolar_actual.exe` de la carpeta `dist/`
2. Ejecuta directamente sin necesidad de instalar Python

### Opción 2: Código fuente
1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/dolar-actual.git
   cd dolar-actual
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta la aplicación:
   ```bash
   python dolar_actual.py
   ```

## 📦 Dependencias

```
requests>=2.25.0
pandas>=1.3.0
numpy>=1.21.0
```

## 🎯 Uso

### Pestaña "TC" - Tipo de Cambio
1. **Selecciona el tipo de dólar** del menú desplegable
2. **Haz clic en "ACTUALIZAR"** para obtener las cotizaciones más recientes
3. **Ingresa el monto en USD** y haz clic en "CALCULAR" para convertir a ARS
4. **Usa "LIMPIAR"** para resetear los campos

### Pestaña "Verificación" - Validación de Cálculos
1. **Ingresa el tipo de cambio** ($/USD)
2. **Ingresa pesos** ($) o **dólares** (USD)
3. **Haz clic en "CALCULAR"** para verificar el cálculo
4. El sistema valida que tengas al menos 2 datos completos

### Pestaña "Histórico" - Consulta de Datos Históricos
1. **Selecciona el tipo de dólar** del menú desplegable
2. **Haz clic en los campos de fecha** para abrir el calendario
3. **Selecciona fecha inicial y final** (formato YYYY-MM-DD)
4. **Haz clic en "ACTUALIZAR"** para obtener los datos históricos
5. Los resultados se muestran en formato de tabla

## 🛠️ Desarrollo

### Estructura del Proyecto
```
dolar_actual/
├── dolar_actual.py          # Aplicación principal
├── funciones_TC.py          # Funciones auxiliares para cálculos
├── operaciones_math.py      # Operaciones matemáticas
├── dolar_actual.spec        # Configuración PyInstaller
├── Icono.ico                # Icono de la aplicación
├── requirements.txt         # Dependencias
└── README.md               # Este archivo
```

### Generar Ejecutable
```bash
pyinstaller dolar_actual.spec
```

## 📊 Fuentes de Datos

La aplicación obtiene las cotizaciones desde la API de **Mercados Ámbito**:
- Dólar Oficial
- Dólar Nación  
- Dólar Blue/Informal
- Dólar Mayorista
- Dólar Turista
- Dólar MEP
- Dólar CCL
- Dólar Cripto

## 🔧 Configuración

### Personalización de Colores
Los colores de la interfaz se pueden modificar en las variables del archivo principal:
```python
colorGeneral = '#502A4F'      # Color principal
colorSeleccion = '#944D93'    # Color de selección
colorComentario = '#E075DF'   # Color de comentarios
```

### Fuentes
```python
fuenteGeneral = 'Comic Sans MS'  # Familia de fuente
```

## 🐛 Solución de Problemas

### Error de conexión
- Verifica tu conexión a internet
- La API de Ámbito puede tener mantenimiento ocasional

### Error de importación
- Asegúrate de tener todas las dependencias instaladas
- Verifica que Python esté en tu PATH

### Problemas con el ejecutable
- Ejecuta como administrador si es necesario
- Verifica que tu antivirus no bloquee el archivo

## 📝 Changelog

### Versión 1.5 (Octubre 2025)
- ✅ Limpieza y optimización del código
- ✅ Mejora en comentarios y documentación
- ✅ Corrección de warnings de linter
- ✅ Interfaz más estable

### Versión 1.4 (Octubre 2025)
- ✅ Añadido calendario interactivo
- ✅ Mejoras en la consulta histórica

### Versión 1.3 (Marzo 2025)
- ✅ Nuevos tipos de dólar (CCL, Cripto)
- ✅ Mejoras en la interfaz

## 👥 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Contacto

**Desarrollador:** Luis Augusto Rodríguez Colmenares  
**Email:** rodriguezcolmenaresl@gmail.com

---

⭐ **¡Si te gusta este proyecto, no olvides darle una estrella!** ⭐
