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

## Implementación del Cifrado
### Generación de Clave Privada RSA
Para generar una nueva clave privada RSA cifrada con AES-256, ejecuta el siguiente comando:

```bash
openssl genpkey -algorithm RSA -out server-key.key -aes256
```

Este comando generará una clave privada cifrada y la guardará en un archivo llamado __`server-key.key`__. Asegúrate de recordar la contraseña que establezcas.


### Creación de Solicitud de Firma de Certificado (CSR)
Crea una nueva Solicitud de Firma de Certificado (CSR) utilizando la clave privada RSA generada:

```bash
openssl req -new -key server-key.key -out server.csr
```

La CSR se guardará en un archivo llamado __`server.csr`__.

### Generación de Certificado Autofirmado
Genera un certificado autofirmado basado en la CSR:

```bash
openssl x509 -req -days 365 -in server.csr -signkey server-key.key -out server-cert.pem
```

Este comando generará un certificado válido por un año y lo guardará en un archivo llamado __`server-cert.pem`__.


### Eliminación de Contraseña de la Clave Privada (Opcional pero precaucionado)
Si decides eliminar la contraseña de la clave privada para simplificar la automatización, ejecuta el siguiente comando:

```bash
openssl rsa -in server-key.key -out server-key.key
```
Este paso es opcional y se realiza para facilitar la automatización en entornos donde ingresar una contraseña manualmente no es práctico. Sin embargo, ten en cuenta que al eliminar la contraseña, la clave privada se vuelve más vulnerable al acceso no autorizado. Asegúrate de entender las implicaciones antes de realizar este paso.




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
python3 client.py
```

Se abrirá una ventana de chat donde puedes ingresar tu nombre y conectarte al servidor.
