# HEBRA v0.8 — La regla escrita también puede equivocarse

## El problema

Antes dijimos:

“Usaremos tres calculadoras diferentes.”

Pero existe otro peligro.

¿Qué pasa si las tres leyeron mal el mismo libro de instrucciones?

Las tres podrían dar la misma respuesta equivocada.

## Qué hicimos

Convertimos una parte de las reglas de HEBRA en una **regla ejecutable**.

Eso significa que podemos darle un ejemplo y obtener una respuesta exacta:

- ACEPTAR;
- RECHAZAR;
- y por qué.

Después creamos ejemplos oficiales.

### Ejemplos buenos

Son problemas donde ya sabemos exactamente cuál debe ser la respuesta.

### Ejemplos malos

Son trampas donde HEBRA debe rechazar, por ejemplo:

- falta un guardián;
- dos habitaciones comparten la misma raíz;
- falta una de las dos cerraduras criptográficas;
- aparece un campo que la regla no conoce.

## La prueba

Probamos 14 ejemplos.

La especificación y una segunda implementación coincidieron en los 14.

Después hicimos una tercera implementación con un error intencional.

Nuestra alarma encontró el error.

## Nueva regla

Si cambia el significado de una regla:

**cambia la versión.**

No se puede editar el libro silenciosamente.

## Otra regla importante

Si un mensaje contiene algo que HEBRA no entiende, no lo ignora.

Lo rechaza.

Porque “ignorar y seguir” puede hacer que dos programas entiendan cosas diferentes.

## Lo que todavía no hemos demostrado

Catorce ejemplos no demuestran que nunca exista un error.

Lo que sí tenemos ahora es una máquina para añadir miles de ejemplos y descubrir diferencias antes
de que entren al Núcleo Cristal.
