# Taller 4 Sistemas Operativos
*José Alejandro Sánchez Sánchez*, *Juan Felipe Martínez Bedoya*

## ¿Qué se hizo?

Para lograr el objetivo del taller 4 en la consistencia de los datos se usó una librería de Python que maneja un servidor de API rest, y ejecuta las peticiones en orden que le vayan llegando. De este modo, si dos usuarios quieren reservar el mismo asiento, se le da prioiridad al primero que llegue, y al segundo se le envía nuevamente todas las sillas para que pueda elegir otra.

La información de los asientos y usuarios queda almacenado en el servidor, como listas y diccionarios.

## ¿Cómo funciona?

Para poder poner el código a funcionar, primero hay que poner a correr el servidor en una terminal, esto con el comando de (en este caso se está realizando el ejemplo en el puerto 800, sin embargo, este puede ser cualquiera, siempre que vaya después del *-p*):

```bash
python main_master.py -p 800
```

Luego se pueden conectar cualquier número de usuarios (sin tener en cuenta las limitaciones del servidor) utilizando el comando (el puerto debe ser el mismo que se ejecutó en el servidor master, ya que todo corre localmente):

```bash
python main_client.py -p 800
```

Una vez entrado en el cliente, se indica que se seleccione un nombre de usuario, el cual debe ser único. Este usuario es importante para manejar las reservas.

Una vez que se confirme el usuario se pueden realizar las siguientes operaciones con los comandos de:

- *sillas* : sirve para ver todos los asientos.

- *reservar f c* : *f* y *c* deben ser números enteros, correspondiente a la fila y columna que se desee reservar. Si los asientos están reservados, se entregan todas las sillas nuevamente y se usa este comando otra vez.

- *pagar* : sirve par pagar la reserva. Si no se hace después de 10 segundos, la reserva se levanta.

- *cancelar* : cancela la reserva, así sea que ya se haya pagado o no.

- *out* : sirve para salirse del programa. Es importante terminar con este comando para poder eliminar el usuario que se creó y liberar las sillas que se reservaron a este nombre.