# HEBRA — Protocolo de Continuidad v0.4

## Objetivo
Que HEBRA pueda continuar correctamente aunque cambie la conversación, la persona que lo revise o la
herramienta usada.

## Regla principal
La memoria oficial de HEBRA está en archivos versionados, no en recuerdos.

## Al comenzar una nueva conversación
1. Abrir `CANON.md`.
2. Abrir `STATE.json`.
3. Confirmar que ambos hablan de la misma versión.
4. Leer `next_recommended_step`.
5. Explicar al usuario, en pocas palabras:
   - qué es HEBRA;
   - qué ya está hecho;
   - qué problema estamos resolviendo ahora.
6. No reconstruir el proyecto desde memoria si los archivos están disponibles.

## Antes de un cambio importante
Explicar al usuario:
- “Voy a hacer X.”
- “Esto sirve para Y.”
- “El riesgo principal es Z.”

## Después del cambio
Explicar:
- qué se ejecutó;
- si funcionó o falló;
- qué archivos cambiaron;
- qué decisión nueva quedó permanente;
- cuál es el siguiente paso.

## Cuando haya un fallo
Nunca ocultarlo.
Registrar:
- qué intentamos;
- por qué falló;
- si el fallo cambia una decisión;
- cómo se evita repetirlo.

## Cuando aparezca una idea nueva
No reemplaza una regla existente automáticamente.
Se clasifica como:
- propuesta;
- experimento;
- aceptada;
- rechazada;
- pendiente.

## Versionado
Cambios grandes: 0.x → 0.(x+1)
Cambios pequeños: mantener versión y añadir revisión si hace falta.
No borrar versiones anteriores.

## Determinismo
Un archivo `STATE.json` debe poder ser leído por una persona y por una máquina.
Los campos principales deben ser estables y ordenados.
El hash del estado permite detectar cambios.

## Durabilidad
GitHub (`miguelcastill85-del/HEBRA`) es la memoria versionada principal actual.
No debe ser la única copia para siempre.
Siguientes mejoras sin coste:
- tags/releases;
- checksums verificados;
- mirrors gratuitos;
- exportación local completa.
