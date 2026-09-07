# HEBRA v0.6 — Ocho llaves no sirven si están en el mismo llavero

## El problema
Podemos tener ocho personas distintas y seguir teniendo una sola debilidad.

Ejemplo:
- ocho cuentas;
- ocho contraseñas;
- pero todas dependen del mismo administrador de empresa.

Si cae ese administrador, podrían caer las ocho.

## La nueva regla: Colapso de Dependencias
HEBRA no contará “personas” o “firmas”.

Contará **raíces de fallo realmente independientes**.

Si varias aprobaciones comparten una raíz capaz de controlarlas, se juntan y cuentan como una.

## Qué raíces miraremos
Por ejemplo:
- quién controla la cuenta;
- qué organización la administra;
- quién guarda la llave de firma;
- qué sistema de identidad puede recuperar la cuenta;
- qué servicio puede firmar;
- quién puede recuperar la llave.

## Desconocido no significa independiente
Si no podemos demostrar que dos guardianes son independientes, HEBRA no debe darles automáticamente
dos votos de confianza.

## Regla de las cuatro habitaciones
Para aceptar una evidencia:
- Origen necesita 2 raíces distintas.
- Medición necesita 2 raíces distintas.
- Método necesita 2 raíces distintas.
- Seguridad necesita 2 raíces distintas.

Además, una misma raíz efectiva no puede contar en dos habitaciones diferentes.

Así volvemos a necesitar 8 raíces independientes reales, no 8 nombres.
