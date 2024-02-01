# Proyecto de Python curso Coderhouse Roberto Chaile

# Proyecto Final

# App: Musicalm
Musicalm es una aplicación web basada en python y Django 5.0 que te permite buscar y descubrir canciones en función de tu estado de ánimo, banda favorita y género preferido. Utiliza la API de Spotify para obtener resultados de búsqueda precisos y relevantes, proporcionando información detallada sobre las canciones encontradas.

Este proyecto consta de una app para poder encontrar esa canción que necesitas escuchar según tu estado de ánimo.
El MVP consta de las siguientes funciones:
- Buscar una canción segun mis preferencias musicales y estado de ánimo
- Crear un repositorio de canciones
- Crear un repositorio de discos
- Crear un repositorio de artistas

Para probar la implementación de este proyecto en tu ordenador primero debes hacer

Abra Terminal.

Cambia el directorio de trabajo actual a la ubicación en donde quieres clonar el directorio.

Escriba ```git clone``` y pegue la dirección URL: https://github.com/rechaile/python-coder-RobertoChaile.git

Este es un proyecto hecho en Python y usando Django version 5.0
Para poder probar este proyecto en tu dispositivo debes tener instalada la version 5.0 de Django

Para eso primero debes tener instalado Python en tu dispositivo
Una vez instalado Python, ejecutar el siguiente comando en tu terminal:
```pip3 install django```

El proyecto contiene cuatro modelos de objetos que serviran para crear los elementos de la base de datos:
- Modelo de Canciones
- Modelo de Artistas
- Modelo de Albums o discos

Si se quiere editar o administrar los elementos de la base de datos, debe user las credenciales de administrador:
**Usuario:** roberto
**Contraseña:** python2024

# Implementación de la API de Spotify
La aplicación Musicalm integra la API de Spotify para ofrecer resultados de búsqueda de canciones. La API se utiliza para realizar consultas basadas en el estado de ánimo del usuario, su banda favorita y su género preferido. La búsqueda se realiza en tiempo real, proporcionando resultados actualizados y relevantes.

La aplicación Musicalm integra la API de Spotify para ofrecer resultados de búsqueda de canciones. Para interactuar con la API de Spotify en Python, se utiliza la librería spotipy, que proporciona una interfaz sencilla para realizar consultas y obtener datos de la API de Spotify.

# Pasos para utilizar la librería de Spotify para Python:
Instalación de la librería: La librería spotipy se puede instalar fácilmente a través de pip. Ejecuta el siguiente comando en tu terminal:

```pip install spotipy```

# Obtención de credenciales de Spotify: 
Para utilizar la API de Spotify, necesitas obtener credenciales de la API de Spotify. Esto incluye un Client ID y un Client Secret. Puedes obtener estas credenciales registrando tu aplicación en el Dashboard de Desarrolladores de Spotify.

# Configuración de credenciales: 
Una vez que tengas tus credenciales de Spotify, configúralas en tu aplicación Python. Esto puede implicar establecer variables de entorno o incluir las credenciales directamente en tu código (ten cuidado de no compartir estas credenciales públicamente).

# Utilización de la librería: 
Con spotipy instalado y tus credenciales configuradas, puedes comenzar a interactuar con la API de Spotify en tu aplicación Python. Puedes realizar consultas de búsqueda, obtener detalles de canciones, álbumes y artistas, entre otras funcionalidades.

# Uso de API keys
Para utilizar la API de Spotify, se requiere una API key válida. La aplicación Musicalm está configurada para aceptar API keys proporcionadas por el usuario. Al clonar este repositorio, puedes agregar tu propia API key de Spotify en la configuración de la aplicación para habilitar la funcionalidad de búsqueda de canciones.

Ver documentación aqui: https://developer.spotify.com/documentation/web-api

# Diferencias de funcionalidad según el rol del usuario
Musicalm ofrece diferentes funcionalidades dependiendo del rol del usuario:

# Usuario común: 
Los usuarios pueden buscar canciones en función de su estado de ánimo, banda favorita y género preferido. También pueden ver los resultados de búsqueda y reproducir las canciones directamente desde la aplicación.

# Administrador: 
Los administradores tienen acceso a funcionalidades adicionales, como la administración de consultas de búsqueda almacenadas en la base de datos. Pueden ver y gestionar consultas realizadas por usuarios comunes, lo que les permite analizar tendencias y mejorar la experiencia de búsqueda.

Link al DEMO: https://drive.google.com/file/d/12GLVHcRcW1r8sq3OL6gWUpzLkB1WBSBx/view?usp=sharing

# Casos de Testeo:

| Case de test | Requerimiento | Aceptado? | 
|--------------|---------------|-----------|
| Login        | El usuario debe poder hacer login | Si | 
| Registro     | El usuario debe poder registrarse | Si |
| Buscar canción por esstado de ánimo | El usuario debe poder buscar una canción según su estado de ánimo, artista y género, al enviar el formulario debe ver un listado de canciones, que indiquen artista, album, genero y un botón para ir al link de la canción en Spotify | Si |
