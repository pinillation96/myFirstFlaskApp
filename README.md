# Aplicación de Login con Flask

## Cómo ejecutar la aplicación

1. Construye la imagen de Docker:

```sh
docker build -t flask-login-app .
```

2. ejecutar el contenedor en modod detach y mappear los puertos:

```sh
docker run -d -p 8080:8080 --name flask-login flask-login-app
```

3. Abre tu navegador y visita http://localhost:8080 para ver la aplicación.

4. Para detener y eliminar el contenedor, ejecuta:
```sh
docker stop flask-login && docker rm flask-login
```

