# Instalación Python

Versiones:

|python:|2.X,|3.X|
|-|-|-|

[Fuente](https://www.digitalocean.com/community/tutorials/install-python-windows-10)

# Paso 1 Descargar el instalador.
https://www.python.org/downloads/windows/


![](https://deved-images.nyc3.digitaloceanspaces.com/CONTINT-1526%2Fpy_download.png)

# Paso 2 Instalar.
  
    Cuidar la ruta de instalación, se recomienda usar una dirección más corta como:

    C:\Python310

    C:\Users\usuario\Python310

    C:\Program Files\Python310

![](https://deved-images.nyc3.digitaloceanspaces.com/CONTINT-1526%2Fpy-installer-customize.png)

![](https://deved-images.nyc3.digitaloceanspaces.com/CONTINT-1526%2Fpy-installer-optional.png)

# Paso 3 Opción avanzada

![](https://deved-images.nyc3.digitaloceanspaces.com/CONTINT-1526%2Fpy-installer-advanced.png)

# Paso 4 Agregar python a las variables de entorno (en caso de no tenerlo).

```
C:\Program Files\Python310
```

```
C:\Users\Sammy\AppData\Local\Programs\Python\Python310
```

* En Inicio ingresar a configuración avanzada del sistema en la barra de búsqueda.

* Click en Ver configuración avanzada del sistema.

* En el cuadro de diálogo Propiedades del sistema, haga clic en la pestaña Avanzado y luego click en Variables de entorno.

* Según la instalación:

   * Si seleccionó Instalar para todos los usuarios
      
       Seleccione Ruta de la lista de Variables del sistema y haga clic en Editar.
   * Si no seleccionó Instalar para todos los usuarios
      
       Seleccione Ruta de la lista de Variables de usuario y haga clic en Editar.

* Haga clic en Nuevo e ingrese la ruta del directorio de Python, luego haga clic en Aceptar hasta que se cierren todos los cuadros de diálogo.

# Paso 5 Verificación
```bash
python --version
```
