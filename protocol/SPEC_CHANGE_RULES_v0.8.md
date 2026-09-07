# HEBRA — Spec Change Rules v0.8

## Idea sencilla

Las reglas de HEBRA no pueden cambiar porque alguien edite una frase y todos sigan adelante como si
nada hubiera ocurrido.

Si cambia el significado, cambia la versión.

## SCR-1 — Semántica congelada por versión

Cada versión del protocolo tiene una semántica fija.

Un evento de época antigua se interpreta usando la versión que estaba activa en esa época.

Nunca reinterpretamos el pasado con reglas nuevas.

## SCR-2 — Todo cambio semántico requiere

1. nueva versión;
2. explicación humana sencilla;
3. actualización del executable specification core;
4. nuevos golden vectors;
5. nuevos negative vectors cuando corresponda;
6. metamorphic tests;
7. differential test sin divergencias;
8. registro en CHANGELOG;
9. actualización de STATE;
10. aprobación por la puerta de gobernanza correspondiente cuando exista en producción.

## SCR-3 — Divergencia bloquea release

Si dos implementaciones válidas de una versión producen resultados distintos para el mismo input:

**la versión no puede promoverse.**

No se decide por mayoría.

## SCR-4 — Orden de validación también es semántica

Si un input tiene dos errores, diferentes implementaciones podrían detectar primero errores distintos.

Por eso el orden de validación está especificado y `reason_code` también forma parte del resultado
determinista.

## SCR-5 — Campos desconocidos se rechazan

Un programa no puede ignorar silenciosamente un campo que otro programa interprete.

Esto evita que el mismo mensaje tenga dos significados.

## SCR-6 — Vectores oficiales son inmutables

Una vez publicados para una versión:

- no se corrigen silenciosamente;
- una corrección crea una revisión/version nueva;
- se conserva el vector viejo y la explicación del error.

## SCR-7 — La IA no puede cambiar la especificación

Una IA puede:

- encontrar ambigüedades;
- proponer vectores;
- sugerir cambios;
- generar implementaciones candidatas.

No puede declarar por sí sola una semántica nueva como oficial.

## SCR-8 — Compatibilidad explícita

Un cambio debe declarar si es:

- editorial: no cambia resultado;
- compatible: añade capacidad sin reinterpretar eventos válidos anteriores;
- incompatible: cambia semántica y exige nueva versión/epoch.

## SCR-9 — Fail closed

Si una implementación no reconoce la versión exacta de un evento, debe rechazar o detenerse.

Nunca debe “probar con la versión más parecida”.
