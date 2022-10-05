# Mi Primer MVT Django

Este MVT contiene:
- Vistas
- Formulario de carga
- Fromulario de busqueda
- Modelo con 3 clases
- Templates


## Clonar el projecto con git

windows:

```PS
C:\> git clone https://github.com/Oliver-Barrett/proyecto-formularioFamiliar.git
```

Linux/Mac:
```bash
$ git clone https://github.com/Oliver-Barrett/proyecto-formularioFamiliar.git
```

## Correr el Servidor

Los siguientes comandos son analogos en Mac/Linux/Windows:

```bash
cd proyecto-formularioFamiliar
python manage.py migrate
```
La consola mostrara las migraciones de la base de datos que se realizaron.

Luego arrancamos el servidor web

```bash
python manage.py runserver
```
Listo ya tenes corriendo el ejemplo.

ahora Hace click en el siguiente link para ver el ejemplo corriendo: 

[http://localhost:8000/](http://localhost:8000/)


## Funcionalidad

Se podrá agregar familiares a traves de un formulario de carga, donde se pedirán todos los datos puestos en las diferentes clases. Una ves completado el formulario, el familiar, se guardará en la base de datos para luego verlo a traves de un template con toda la informacion.

Se podrá buscar familiares a traves de un formulario de busqueda, donde se pedirá el nombre del familiar y, en caso de que exista en la base de datos, se mostrará a traves de un template con toda su informacion. Si no existe dicho familiar no se mostrará nada.



