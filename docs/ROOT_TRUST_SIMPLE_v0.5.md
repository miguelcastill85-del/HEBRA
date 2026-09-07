# HEBRA v0.5 — La seguridad explicada como una casa

## Qué estamos protegiendo
Imagina que HEBRA guarda un libro donde sólo deben entrar cosas que pasaron suficientes controles.

No queremos una sola cerradura. Si alguien roba una llave, la casa no debe abrirse.

## Para aceptar una nueva evidencia
HEBRA exige cuatro comprobaciones distintas:

1. **Origen:** ¿sabemos de dónde salió?
2. **Medición:** ¿se midió correctamente?
3. **Método:** ¿la prueba se hizo como se prometió?
4. **Seguridad:** ¿no estamos ignorando un daño importante?

Cada comprobación tiene tres guardianes y hacen falta dos.

Por eso un atacante necesita, como mínimo:

2 + 2 + 2 + 2 = **8 guardianes independientes**.

## Para cambiar el propio Núcleo Cristal
Hace falta otra puerta:

- 4 de 7 guardianes de versión;
- 2 de 3 personas que reconstruyen el programa;
- 2 de 3 auditores.

Mínimo: **8**.

## Para usar la recuperación de emergencia
Hace falta:

- 5 de 9 guardianes de recuperación;
- 3 de 5 auditores independientes.

Mínimo: **8**.

## Una persona no puede contar dos veces
Dos cuentas distintas de la misma persona no son dos guardianes.
Dos empleados controlados por la misma llave maestra tampoco cuentan como dos partes independientes.

## El piso de seguridad
Las reglas normales pueden hacer HEBRA más estricto, pero no más débil.

Es como una pared de hormigón debajo de las cerraduras: el panel de configuración puede añadir
cerraduras, pero no puede quitar la pared.

## Qué significa BTR-8
**BTR-8 candidato** significa:

> En nuestro modelo actual, un atacante necesita comprometer al menos 8 dominios de confianza
> realmente independientes para contaminar la raíz por las rutas estudiadas.

Todavía NO es una garantía de producción. Falta comprobar fallos compartidos, implementación real,
criptografía, dispositivos y personas verdaderamente independientes.
