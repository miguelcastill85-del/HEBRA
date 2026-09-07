# HEBRA — Cryptographic Agility Policy v0.7

## Idea sencilla

No queremos construir una casa cuya única cerradura sea de un modelo que algún día pueda romperse.

## Principios

### CA-1 — Ningún algoritmo es eterno
El CANON no fija para siempre un algoritmo concreto.

### CA-2 — Root Dual-Suite
Cambios de raíz, política constitucional, recuperación y checkpoints canónicos requieren pruebas
válidas bajo dos suites criptográficas independientes activas.

### CA-3 — Diferencia matemática
Las suites raíz deben pertenecer a familias criptográficas suficientemente diferentes para que una
misma ruptura matemática obvia no destruya ambas.

### CA-4 — Implementaciones separadas
Siempre que sea viable, los tres resolvers no comparten una única implementación de cada suite.

### CA-5 — Agilidad con epoch
Cambiar suites crea una nueva época. No reescribe firmas antiguas.

### CA-6 — Deprecation
Si una suite se considera insegura:
1. congelar nuevos usos;
2. mantener verificación histórica según epoch;
3. activar suite sustituta mediante la puerta de raíz todavía segura;
4. nunca “aceptar temporalmente sin criptografía”.

### CA-7 — Fail closed
Si una suite raíz requerida no puede verificarse, el cambio de raíz se detiene.

## Importante

Dos algoritmos aumentan resiliencia pero también aumentan código.
Por eso HEBRA no añadirá algoritmos sin un motivo de amenaza concreto, pruebas interoperables y
mantenimiento viable.
