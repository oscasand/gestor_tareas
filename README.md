# Gestor de Tareas (To-Do List)

Una aplicación web simple y elegante para gestionar tareas pendientes, desarrollada con Flask.

## Características

- ✅ **Agregar tareas**: Crea nuevas tareas fácilmente
- ✅ **Marcar como completadas**: Cambia el estado de las tareas
- ✅ **Eliminar tareas**: Borra tareas que ya no necesites
- ✅ **Interfaz moderna**: Diseño responsive con Bootstrap 5
- ✅ **Persistencia de datos**: Las tareas se guardan en un archivo JSON
- ✅ **Fechas de creación**: Cada tarea incluye fecha de creación y completado

## Instalación

1. **Clona o descarga el proyecto**
2. **Activa el entorno virtual** (si usas uno):
   ```bash
   # En Windows
   venv\Scripts\activate
   
   # En Linux/Mac
   source venv/bin/activate
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. **Ejecuta la aplicación**:
   ```bash
   python app.py
   ```

2. **Abre tu navegador** y ve a: `http://127.0.0.1:5000`

3. **¡Comienza a gestionar tus tareas!**

## Funcionalidades

### Agregar Tarea
- Escribe tu tarea en el campo de texto
- Haz clic en "Agregar" o presiona Enter
- La tarea aparecerá en la lista de pendientes

### Gestionar Tareas
- **Marcar como completada**: Haz clic en el botón verde ✓
- **Marcar como pendiente**: Haz clic en el botón verde con flecha ↶
- **Eliminar**: Haz clic en el botón rojo de basura 🗑️

### Organización
- Las tareas se dividen en dos secciones:
  - **Pendientes**: Tareas por hacer (color amarillo)
  - **Completadas**: Tareas terminadas (color verde)

## Estructura del Proyecto

```
gestor_tareas/
├── app.py              # Aplicación principal Flask
├── requirements.txt    # Dependencias del proyecto
├── tasks.json         # Archivo de datos (se crea automáticamente)
├── templates/
│   └── index.html     # Plantilla HTML principal
└── static/
    └── style.css      # Estilos CSS personalizados
```

## Tecnologías Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Iconos**: Font Awesome
- **Almacenamiento**: Archivo JSON

## Características Técnicas

- **Persistencia**: Los datos se guardan automáticamente en `tasks.json`
- **Responsive**: Funciona perfectamente en móviles y tablets
- **Sin base de datos**: Usa archivos JSON para simplicidad
- **Mensajes flash**: Notificaciones de éxito/error
- **Validación**: Previene tareas vacías

## Personalización

Puedes modificar fácilmente:
- **Colores**: Edita `static/style.css`
- **Funcionalidades**: Modifica `app.py`
- **Interfaz**: Cambia `templates/index.html`

## Solución de Problemas

### La aplicación no inicia
- Verifica que Flask esté instalado: `pip install Flask`
- Asegúrate de estar en el directorio correcto

### Las tareas no se guardan
- Verifica que el archivo `tasks.json` tenga permisos de escritura
- Revisa que no haya errores en la consola

### Problemas de estilo
- Asegúrate de que el archivo `static/style.css` existe
- Verifica que el navegador no esté bloqueando recursos

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar la aplicación, no dudes en:
1. Reportar bugs
2. Sugerir nuevas funcionalidades
3. Enviar pull requests

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

