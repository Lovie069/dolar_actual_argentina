# 📦 Guía para Generar Ejecutable .exe

Esta guía te mostrará cómo crear un archivo ejecutable (.exe) de la aplicación **Dólar Actual** usando PyInstaller.

## 📋 Requisitos Previos

1. **Python 3.7+** instalado
2. **Todas las dependencias instaladas**:
   ```bash
   pip install -r requirements.txt
   ```

3. **PyInstaller instalado**:
   ```bash
   pip install pyinstaller
   ```
   O descomenta la línea en `requirements.txt`:
   ```
   pyinstaller>=4.0
   ```

## 🚀 Paso 1: Verificar Archivos Necesarios

Asegúrate de tener estos archivos en el directorio del proyecto:

```
DOLAR_ACTUAL/
├── dolar_actual.py          ✅ Archivo principal
├── funciones_TC.py          ✅ Funciones auxiliares
├── operaciones_math.py      ✅ Operaciones matemáticas
├── Icono.ico                ✅ Icono de la aplicación
└── dolar_actual.spec        ✅ Configuración PyInstaller
```

## 🔧 Paso 2: Generar el Ejecutable

### Opción A: Usando el archivo .spec (Recomendado)

```bash
pyinstaller dolar_actual.spec
```

### Opción B: Comando directo

```bash
pyinstaller --onefile --windowed --icon=Icono.ico --name=dolar_actual dolar_actual.py
```

### Explicación de los parámetros:

- `--onefile` o `-F`: Crea un solo archivo ejecutable
- `--windowed` o `-w`: Oculta la consola (para aplicaciones GUI)
- `--icon=Icono.ico`: Asigna el icono especificado
- `--name=dolar_actual`: Nombre del archivo ejecutable
- `dolar_actual.py`: Archivo principal de la aplicación

## 📁 Paso 3: Ubicación del Ejecutable

Una vez completado el proceso, encontrarás el ejecutable en:

```
dist/
└── dolar_actual.exe
```

## ⚙️ Configuración del archivo .spec

El archivo `dolar_actual.spec` contiene la configuración optimizada:

```python
# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['dolar_actual.py'],
    pathex=[],
    binaries=[],
    datas=[],                    # Aquí puedes agregar datos adicionales
    hiddenimports=[],            # Importaciones ocultas si es necesario
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='dolar_actual',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,                    # Comprime el ejecutable
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,               # Sin ventana de consola
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['Icono.ico'],          # Icono de la aplicación
)
```

### Si necesitas agregar archivos adicionales:

```python
datas=[
    ('ruta/origen/archivo.txt', 'ruta/destino'),
    ('imagenes', 'imagenes'),  # Copiar toda una carpeta
],
```

## 🔍 Resolución de Problemas

### Error: "No module named 'funciones_TC'"

**Solución**: PyInstaller debe detectar automáticamente estos módulos. Si no lo hace:
1. Verifica que `funciones_TC.py` esté en el mismo directorio
2. Agrega a `hiddenimports` en el .spec:
   ```python
   hiddenimports=['funciones_TC', 'operaciones_math'],
   ```

### Error: "No se encuentra requests/pandas/numpy"

**Solución**: Asegúrate de tener todas las dependencias instaladas:
```bash
pip install requests pandas numpy
```

### El ejecutable es muy grande

**Solución**: PyInstaller incluye el intérprete de Python y todas las librerías. Esto es normal. Para reducir tamaño:
1. Usa `--onefile` (ya está configurado)
2. Comprueba que `upx=True` esté activado (ya está)
3. Considera usar entornos virtuales para evitar dependencias innecesarias

### La aplicación no inicia

**Solución**: Prueba generar con consola visible temporalmente para ver errores:
```bash
pyinstaller --onefile --icon=Icono.ico dolar_actual.py
```

### El icono no aparece

**Solución**: Verifica que:
1. El archivo `Icono.ico` existe en el directorio raíz
2. La ruta en el .spec es correcta: `icon=['Icono.ico']`
3. El formato .ico es válido

## 🎯 Comandos Rápidos

### Generar ejecutable (método simple):
```bash
pip install pyinstaller
pyinstaller dolar_actual.spec
```

### Limpiar build anterior y regenerar:
```bash
rmdir /s /q build dist
pyinstaller dolar_actual.spec
```

### Solo generar sin build previo:
```bash
pyinstaller --clean dolar_actual.spec
```

## 📝 Notas Importantes

1. **Configuración de personalización**: La aplicación genera automáticamente `config_personalizacion.json` en la carpeta del ejecutable
2. **Compatible con .exe**: El sistema de personalización está diseñado para funcionar con ejecutables
3. **Primera ejecución**: Puede tardar un poco más en iniciar la primera vez
4. **Antivirus**: Algunos antivirus pueden marcar el .exe como sospechoso (falso positivo)

## 🧪 Probar el Ejecutable

1. Navega a la carpeta `dist/`
2. Ejecuta `dolar_actual.exe`
3. Verifica que todas las funcionalidades trabajen correctamente:
   - ✅ Consulta de cotizaciones
   - ✅ Conversión de monedas
   - ✅ Verificación de cálculos
   - ✅ Consulta histórica
   - ✅ Personalización de colores y fuentes

## 📦 Distribuir la Aplicación

Para distribuir la aplicación, solo necesitas compartir:
- `dolar_actual.exe` (archivo del ejecutable)

**No es necesario** incluir:
- ❌ Archivos .py
- ❌ Carpeta de dependencias
- ❌ Configuración de Python

El ejecutable contiene todo lo necesario para ejecutar la aplicación.

## 🔗 Enlaces Útiles

- [Documentación PyInstaller](https://pyinstaller.readthedocs.io/)
- [PyInstaller GitHub](https://github.com/pyinstaller/pyinstaller)
- [Solución de problemas comunes](https://pyinstaller.readthedocs.io/en/stable/when-things-go-wrong.html)

---

**¡Listo!** Ahora puedes generar tu ejecutable .exe fácilmente. 🎉

