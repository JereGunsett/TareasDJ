# Tareas Project

## Descripción del Proyecto

Tareas Project es una aplicación web de gestión de tareas que permite a los usuarios organizar proyectos, asignar tareas y colaborar de manera eficiente.

## Estructura del Proyecto

La estructura del proyecto se organiza en diferentes aplicaciones dentro de la carpeta `applications`. Cada aplicación se encarga de una parte específica de la funcionalidad.

- **categoria**: Gestiona las categorías de los proyectos.
- **comentario**: Maneja los comentarios relacionados con las tareas.
- **home**: Contiene vistas y plantillas para la página principal y de inicio.
- **notificacion**: Maneja las notificaciones del sistema.
- **proyecto**: Gestiona la creación, modificación y eliminación de proyectos.
- **tarea**: Maneja las tareas dentro de un proyecto.
- **usuario**: Administra la autenticación y la gestión de usuarios.

## Requisitos de Instalación

Antes de comenzar, asegúrate de tener Python y Django instalados en tu entorno de desarrollo. Se recomienda el uso de un entorno virtual. Puedes crear y activar un entorno virtual con los siguientes comandos:

```bash
python -m venv myenv
```
Para sistemas basados en Unix/Linux
```
source myenv/bin/activate
```
Para sistemas basados en Windows
```
.\myenv\Scripts\activate
```

Luego, instala las dependencias del proyecto ejecutando:

```bash
pip install -r requirements.txt
```
Configuración
Asegúrate de configurar correctamente las variables de entorno en el archivo settings.py para adaptar el proyecto a tus necesidades específicas.

Configuración de PostgreSQL
Instala PostgreSQL (si aún no lo has hecho):

Linux:

```bash
sudo apt-get update
sudo apt-get install postgresql
```

Mac:

```bash
brew install postgresql
```
Windows:
Descarga e instala PostgreSQL desde https://www.postgresql.org/download/windows/.

Crea una base de datos y un usuario en PostgreSQL:

Accede a PostgreSQL:
```bash
psql -U postgres
```
<br>
Crea una base de datos:

```sql
CREATE DATABASE tareas_project;
```
Crea un usuario:

```sql
CREATE USER usuario_tareas WITH PASSWORD 'contraseña_segura';
```
Concede privilegios al usuario sobre la base de datos:
```sql
ALTER ROLE usuario_tareas SET client_encoding TO 'utf8';
ALTER ROLE usuario_tareas SET default_transaction_isolation TO 'read committed';
ALTER ROLE usuario_tareas SET timezone TO 'UTC';
ALTER USER usuario_tareas CREATEDB;
```
Sal del entorno de PostgreSQL:
```sql
\q
```
Actualiza las configuraciones de la base de datos en settings.py:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tareas_project',
        'USER': 'usuario_tareas',
        'PASSWORD': 'contraseña_segura',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Realiza las migraciones de la base de datos:
```bash
python manage.py migrate
```
##Instrucciones de Uso
Clona este repositorio:
```bash
git clone https://github.com/TuUsuario/TareasProject.git
cd TareasProject
```
Realiza las migraciones de la base de datos:
```bash
python manage.py migrate
```
Crea un superusuario ejecutando el siguiente comando:
```bash
python manage.py createsuperuser
```
Te saldra para que completes los datos de tu usuario como por ejemplo:
```bash
python manage.py createsuperuser

Username: admin
Email address: admin@example.com
Password: password123
Password (again): password123
Superuser created successfully.
```
Inicia el servidor de desarrollo:
```bash
python manage.py runserver
```
Visita http://127.0.0.1:8000/ en tu navegador para acceder a la aplicación.

##Ejemplos de Uso
A continuación, se presentan algunos ejemplos de cómo utilizar las funcionalidades clave del proyecto:

Crear un Proyecto: [Instrucciones]

Asignar Tareas: [Instrucciones]

Gestionar Usuarios: [Instrucciones]

Contribución
Si deseas contribuir al proyecto, sigue estos pasos:

Haz un fork del repositorio.
Crea una rama para tu contribución: 
```git checkout -b feature/nueva-funcionalidad```
Realiza tus cambios y haz un commit: 
```git commit -m "Añadir nueva funcionalidad"```
Sube tu rama al repositorio remoto: 
```git push origin feature/nueva-funcionalidad```
Abre un Pull Request.