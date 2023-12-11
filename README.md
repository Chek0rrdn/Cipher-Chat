# Proyecto de Chat en Python con un enfoque del Cifrado en Telecomunicaciones

## Descripción del Proyecto
Este proyecto implementa un chat cliente-servidor en Python utilizando la biblioteca Tkinter para la interfaz gráfica. El objetivo principal del proyecto es destacar la importancia del cifrado en las telecomunicaciones. Para lograr esto, se examinará primero el funcionamiento del chat sin cifrado, utilizando herramientas como Wireshark para capturar el tráfico y visualizar los mensajes sin cifrar. Posteriormente, se implementará un cifrado para asegurar la confidencialidad de las comunicaciones y se demostrará cómo el cifrado protege la información de ser interceptada.



### Requisitos Previos
Asegúrate de tener instalado Python en tu sistema. Puedes descargarlo desde [python](python.org).



## Configuración del Entorno Virtual (Opcional pero recomendado)
Se recomienda utilizar un entorno virtual para evitar conflictos con las dependencias. Puedes crear un entorno virtual con el siguiente comando:

```bash
python3 -m venv venv
```

Luego, activa el entorno virtual:

- En Windows:
```bash
venv\Scripts\activate
```

- En macOS y Linux:
```bash
source venv/bin/activate
```



## Instalación de Dependencias

Instala las dependencias necesarias ejecutando el siguiente comando:
```bash
pip install -r requirements.txt
```



## Ejecución

### Ejecución del Servidor
Ejecuta el servidor utilizando el siguiente comando:

```bash
python3 server.py
```

El servidor estará escuchando en el puerto especificado (por defecto, el puerto 1234).



### Ejecución del Cliente
Ejecuta el cliente utilizando el siguiente comando:

```bash
python client.py
```

Se abrirá una ventana de chat donde puedes ingresar tu nombre y conectarte al servidor.
