# proyecto del minibanco

primero crean el entorno virtual usando pip, eso lo explican en el video del canal de Gregory Vicent que les voy
a enviar para que se puedan guiar de lo que hice, estas son las lineas para instalar y ejecitar pip

instalan pip
```
sudo apt install -y python3 -venv
```
crean el entorno virtual
```
python3 -m venv env
```
activan y desactivan al finalizar de programar el entorno virtual
```
source env/bin/activate
deactivate
```

este es el codigo para instalar todas librerias que yo use en el proyecto, estan almacenadas en el archivo
requirements.txt, deben usar pip para descargarlas todas de una vez con el archivo
```
pip3 install -r requirements.txt
```
si quieren ver lo que hay adentro desde la terminal pueden usar el siguiente codigo
```
cat requirements.txt
```
para generar su propio archivo con todas las librerias actualizadas usan
```
pip3 freeze > requirements.txt
```

En resumen para ejecutar todo el proyecto deben realizar los siguientes pasos:

clonan todo el proyecto de github
```
git clone
```
crean el environment, sin meter el main.py dentro porque genera errores de scope
```
python -m venv env
```
lo activan
```
source env/bin/activate
```
instalan las librerias
```
pip3 install -r requirements.txt
```
ejecutan el siguiente codigo para abrir el servidor web que hace funcionar el proyecto, esto tambien sale en el video que les envio
```
uvicorn main:app --reload
```

Por ultimo para subir todo en el github siguen estos pasos:

subimos los archivos al repositorio
```
git remote add origin "enlace del repositorio"
```
verificar el enlace del repositorio actual
```
git remote -v
```
agrega cambios hechos en el proyecto
```
git add *
```
agregamos los archivos, con un subnombre que le damos al commit entre comillas
```
git commit -m "primer commit del proyecto"
```
enlazamos y subimos cambios al repositorio
```
git push origin
```
para lo anterior aveces pide su usuario de github y una contraseña, si pasa entonces para esta contraseña debe ser un token
entonces van a (settings,developer settings,personal access token, tokens classic, generate new token)
por ultimo le da los permisos necesarios al token par que funcione como contraseña de un repositorio
lo genera lo copia y lo pega en la contraseña y listo todo debe quedar subido en el github
