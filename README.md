# Flask-WebToDo

Aplicación web de gestión de tareas pendientes (ToDo List) desarrollada con Flask, que permite a los usuarios registrarse, autenticarse y administrar sus tareas de manera eficiente.

## 📋 Descripción

Flask-WebToDo es una aplicación web completa que implementa un sistema CRUD (Crear, Leer, Actualizar, Eliminar) para la gestión de tareas. Incluye un sistema de autenticación de usuarios con registro y login, permitiendo que cada usuario maneje sus propias tareas de forma segura.

## ✨ Características

- **Sistema de Autenticación**
  - Registro de nuevos usuarios
  - Inicio de sesión seguro
  - Hash de contraseñas con Werkzeug
  - Gestión de sesiones
  - Protección de rutas con decorador `@login_required`

- **Gestión de Tareas**
  - Crear nuevas tareas con título y descripción
  - Listar todas las tareas del usuario
  - Actualizar tareas existentes
  - Marcar tareas como completadas
  - Eliminar tareas
  - Timestamp automático de creación

- **Interfaz de Usuario**
  - Templates Jinja2 responsivos
  - Sistema de mensajes flash para feedback
  - CSS personalizado
  - Diseño limpio y moderno

## 🛠️ Tecnologías Utilizadas

- **Backend**: Flask 3.1.2
- **Base de Datos**: SQLAlchemy 3.1.1
- **Autenticación**: Werkzeug Security
- **Variables de Entorno**: python-dotenv 1.2.1
- **Python**: >= 3.14

## 📁 Estructura del Proyecto

```
Flask-WebToDo/
├── main.py                 # Punto de entrada de la aplicación
├── pyproject.toml          # Configuración y dependencias del proyecto
├── README.md               # Documentación del proyecto
├── LICENSE                 # Licencia MIT
├── instance/               # Directorio para base de datos SQLite
└── todoapp/                # Paquete principal de la aplicación
    ├── __init__.py         # Factory pattern y configuración de la app
    ├── auth.py             # Blueprint de autenticación
    ├── todo.py             # Blueprint de gestión de tareas
    ├── models.py           # Modelos de base de datos (User, TodoItem)
    ├── extensions.py       # Extensiones de Flask (SQLAlchemy)
    ├── static/
    │   └── css/
    │       └── styles.css  # Estilos personalizados
    └── templates/
        ├── base.html       # Template base
        ├── index.html      # Página de inicio
        ├── auth/
        │   ├── login.html  # Página de inicio de sesión
        │   └── register.html # Página de registro
        └── todo/
            ├── index.html   # Lista de tareas
            ├── create.html  # Crear nueva tarea
            └── update.html  # Actualizar tarea
```

## 🗄️ Modelos de Base de Datos

### User
```python
- id: Integer (Primary Key)
- username: String(20) (Unique, Not Null)
- password: Text (Not Null, hashed)
```

### TodoItem
```python
- id: Integer (Primary Key)
- user: Integer (Foreign Key -> User.id)
- title: String(100) (Not Null)
- description: Text (Optional)
- completed: Boolean (Default: False)
- created_at: DateTime (Auto-generated)
```

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.14 o superior
- uv (gestor de paquetes ultrarrápido para Python)

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/BrayanTM/Flask-WebToDo.git
   cd Flask-WebToDo
   ```

2. **Instalar uv (si aún no lo tienes)**
   ```bash
   # En Windows (PowerShell)
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # En Linux/Mac
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Crear un entorno virtual con uv**
   ```bash
   uv venv
   
   # Activar el entorno virtual
   # En Windows
   .venv\Scripts\activate
   
   # En Linux/Mac
   source .venv/bin/activate
   ```

4. **Instalar dependencias con uv**
   ```bash
   uv pip install -e .
   ```
   
   O instalar paquetes individuales:
   ```bash
   uv pip install flask flask-sqlalchemy python-dotenv
   ```

4. **Configurar variables de entorno**
   
   Crear un archivo `.env` en la raíz del proyecto:
   ```env
   DEBUG=True
   SECRET_KEY=tu_clave_secreta_super_segura_aqui
   SQLALCHEMY_DATABASE_URI=sqlite:///todo.db
   CRYPT_METHOD=pbkdf2:sha256
   ```

5. **Ejecutar la aplicación**
   ```bash
   python main.py
   ```

6. **Acceder a la aplicación**
   
   Abrir el navegador en: `http://127.0.0.1:5000`

## 📝 Uso

### Registro de Usuario
1. Navegar a `/auth/register`
2. Ingresar nombre de usuario y contraseña
3. Hacer clic en "Registrar"

### Iniciar Sesión
1. Navegar a `/auth/login`
2. Ingresar credenciales
3. Hacer clic en "Iniciar Sesión"

### Gestión de Tareas
- **Listar tareas**: `/todo/list`
- **Crear tarea**: `/todo/add`
- **Actualizar tarea**: `/todo/update/<id>`
- **Eliminar tarea**: `/todo/delete/<id>` (POST)

## 🔒 Seguridad

- Las contraseñas se almacenan hasheadas usando `pbkdf2:sha256`
- Protección CSRF mediante tokens de sesión de Flask
- Validación de sesiones en cada request
- Rutas protegidas con decorador `@login_required`

## 🎨 Características Técnicas

- **Factory Pattern**: Uso de `create_app()` para la instanciación de la aplicación
- **Blueprints**: Organización modular con blueprints para auth y todo
- **ORM**: SQLAlchemy para manejo de base de datos
- **Templates**: Jinja2 con herencia de templates
- **Flash Messages**: Sistema de mensajes para feedback al usuario
- **Context Globals**: Uso de Flask `g` para usuario actual

## 🔄 Rutas de la Aplicación

### Autenticación (`/auth`)
- `GET/POST /auth/register` - Registro de usuario
- `GET/POST /auth/login` - Inicio de sesión
- `GET /auth/logout` - Cerrar sesión

### Tareas (`/todo`)
- `GET /todo/list` - Listar tareas (requiere autenticación)
- `GET/POST /todo/add` - Agregar tarea (requiere autenticación)
- `GET/POST /todo/update/<id>` - Actualizar tarea (requiere autenticación)
- `POST /todo/delete/<id>` - Eliminar tarea (requiere autenticación)

### General
- `GET /` - Página de inicio

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

Copyright (c) 2025 Brayan Tebelán

## 👨‍💻 Autor

**Brayan Tebelán** - [@BrayanTM](https://github.com/BrayanTM)

## 📞 Contacto

Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue en el repositorio.

---

⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub