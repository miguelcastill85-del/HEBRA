# HEBRA CANON v0.8
## Fuente oficial del proyecto

## 1. Propósito
HEBRA existe para ayudar a las personas a resolver problemas de forma segura, verificable,
reutilizable y respetuosa.

## 2. Principios no negociables

### P1 — Ayudar primero
El beneficio humano está por encima del crecimiento, el dinero y el uso.

### P2 — Coste cero hasta ingresos
No se añade gasto operativo nuevo hasta que HEBRA genere ingresos propios.

### P3 — No vender a la persona
No vender datos personales. El dinero no compra peso de evidencia.

### P4 — ICC-0
Datos no autorizados tienen influencia cero sobre el estado confiable.

### P5 — Núcleo Cristal
La IA puede proponer, pero no aprobar ni promover.

### P6 — Sin aprendizaje online directo
Inputs de usuario no cambian automáticamente modelos, políticas, claves, código ni conocimiento.

### P7 — Historia append-only
El pasado no se reescribe silenciosamente.

### P8 — Determinismo
Mismos inputs + misma versión + misma política => mismo resultado canónico.

### P9 — Durabilidad
La memoria oficial vive en archivos versionados y exportables.

### P10 — Explicación sencilla obligatoria
Cambios importantes se explican antes y después en lenguaje claro.

### P11 — Estado persistente
`STATE.json` indica siempre dónde estamos y qué sigue.

### P12 — No fingir certeza
Si algo no está demostrado, se dice.

### P13 — Persistencia no es autoridad
GitHub guarda el proyecto pero no decide por sí solo qué es verdad.

### P14 — Piso Constitucional de Seguridad
Políticas ordinarias pueden endurecer, nunca debilitar mínimos constitucionales.

### P15 — Independencia real
Dependencias compartidas conocidas se colapsan antes de contar autoridad.

### P16 — Divergencia significa parada
Tres resolvers críticos deben coincidir exactamente; una diferencia produce HALT.

### P17 — Diversidad técnica comprobada
Una diversidad sólo cuenta cuando sus raíces de fallo están declaradas y son suficientemente distintas.

### P18 — Agilidad criptográfica
Operaciones de raíz deben poder migrar entre suites por épocas.

### P19 — Semántica versionada
La interpretación de una versión del protocolo queda congelada.
Cambiar el significado exige nueva versión.

### P20 — Especificación ejecutable y vectores
Las reglas críticas deben tener:
- especificación ejecutable;
- ejemplos buenos;
- ejemplos malos;
- propiedades metamórficas;
- comparación entre implementaciones.

### P21 — Desconocido se rechaza
Campos o versiones desconocidas no se ignoran silenciosamente.

## 3. Propiedades

### ICC-0
Entrada no autorizada no cambia estado confiable.

### ICE-0
Sin ingresos propios, gasto operativo nuevo = 0.

### BTR-8 / eBTR
Barrera de autoridad modelada, ajustada por dependencias reales.

### CMC-2
En topología técnica objetivo, ninguna causa técnica catastrófica modelada aislada basta.
No demostrado en producción.

### Determinismo semántico v0.8
14 vectores oficiales fueron ejecutados contra dos implementaciones prototipo sin divergencias.
Un bug intencional fue detectado por el differential harness.

Esto es evidencia de prueba, no demostración universal.

## 4. Continuidad
Leer `CANON.md`, luego `STATE.json`, explicar el estado y continuar desde el siguiente paso.

## 5. Estado resumido
SPEC-COMMON-001 está completado a nivel de prototipo de especificación y pruebas.

Siguiente objetivo:
construir la primera utilidad local y de coste cero para una persona real en dominios de bajo riesgo,
sin necesitar servidor ni datos sensibles.
