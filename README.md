# Trabajo de Fin de Grado
## Grado en Ingeniería en Tecnología de la Telecomunicación

### Datos  
**Título:** DISEÑO DE UN SISTEMA CONTROLADOR DE TEMPERATURA PARA LA VALIDACIÓN DE COMPONENTES ESPACIALES BASADO EN EL EMPLEO DE CÉLULAS PELTIER  
**Autora:** MARÍA DE LOS ÁNGELES SALOMÓN PÉREZ  
**Tutor:** ÁNGEL ÁLVARO SÁNCHEZ  
**Tutor Industrial:** JORGE MAYO  VILCHES  
**Curso:** 2024/2025  
**Titulación:** Doble Grado en Ingeniería en Tecnologías de la Telecomunicación e Ingeniería Aeroespacial en Aeronavegación  
**Universidad:** Universidad Rey Juan Carlos

### Resumen
Este Trabajo de Fin de Grado se centra en el diseño de un sistema controlador de temperatura basado en el uso de una célula Peltier, capaz de regular la temperatura de un componente bajo prueba (DUT). Este sistema aprovecha el efecto Peltier para producir un cambio de estado entre enfriar y calentar siguiendo una lógica de control ON/OFF que permite realizar una comparación entre la temperatura del DUT y la temperatura objetivo, programada en un microcontrolador Arduino.  

Además, se implementará una interfaz de usuario que permita al usuario introducir la temperatura objetivo deseada, simplificando asi la interacción sistema-usuario.  

Este sistema ofrecerá una solución sencilla y económica que cumpla con los requisitos establecidos por Thales Alenia Space.

## Contenido del repositorio
- Script main_Arduino.ino donde se implementa la lógica de control del sistema.
- Script main_python.py con la implementación de la interfaz de usuario y el gráfico de control.
- Fichero requirements.txt que incluye las librerías necesarias para ejecutar el código de Python.
- README.md con toda la información necesaria acerca del sistema controlador de temperatura.

## Intrucciones para la puesta en marcha del sistema.
1. Requisitos
- Arduino IDE (versión 2.3.4 o superior).  
- Python (version 3.12.0 o superior).  
- Librerias indicadas en el fichero requirements.txt.
- Componentes: placa Arduino UNO, LM35, célula Peltier, Arduino Motor Shield Rev3.  
2. Conexión hardware
- Acoplar placa Arduino UNO a la placa de expansión Arduino Motor Shield Rev3.
- Conectar LM35 a la alimentación de 5V, entrada analógica A5 y GND del acople anterior.  
- Conectar célula Peltier al canal B de la placa de expansión (rojo a B+ y negro a B-).  
- Unir LM35 a la cara activa de la Peltier.  
- Conectar placa Arduino UNO al puerto USB del PC.  
3. Cargar Firmware
- Abrir archivo main_Arduino.ino
- Seleccionar placa (Arduino UNO) y puerto.
- Ejecutar y cargar el programa sobre la placa.
4. Ejecución Python
- Antes de ejecutar el script de pyhton se debe ejecutar el comando:  
 pip install -r requirements.txt
- Ejecutar script de Python main_pyhton.py con el comando  
 python main_python.py  
5. Introducir temperatura objetivo en la ventana emergente con la interfaz de usuario.






