# HEBRA CANON v0.7
## Fuente oficial del proyecto

Este archivo define qué es HEBRA, qué reglas no deben olvidarse y cómo continuar el trabajo.

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
Los datos no autorizados tienen influencia exactamente cero sobre el estado confiable.

### P5 — Núcleo Cristal
La IA puede proponer, pero no aprobar ni promover.

### P6 — Sin aprendizaje online directo
Inputs de usuario no cambian automáticamente modelos, políticas, claves, código ni conocimiento confiable.

### P7 — Historia append-only
Las correcciones crean nuevas versiones; no borran silenciosamente el pasado.

### P8 — Determinismo
Mismos inputs confiables + misma política + misma versión => mismo resultado canónico.

### P9 — Durabilidad
El proyecto vive en archivos versionados y exportables, no en recuerdos.

### P10 — Explicación sencilla obligatoria
Antes y después de cambios importantes se explica qué, por qué, riesgo, resultado y siguiente paso.

### P11 — Estado persistente
`STATE.json` debe decir siempre dónde estamos y qué sigue.

### P12 — No fingir certeza
Si algo no está demostrado, se dice.

### P13 — Persistencia no es autoridad
GitHub guarda HEBRA, pero no decide por sí solo qué es verdad.

### P14 — Piso Constitucional de Seguridad
Una política normal puede aumentar seguridad, nunca bajar los mínimos constitucionales.

### P15 — Independencia real
Dos nombres no cuentan como dos controles si comparten una raíz capaz de controlarlos.

### P16 — Divergencia significa parada
Para una transición canónica crítica, resolvers independientes deben producir exactamente el mismo
verdict, transition hash y next trusted root.

Una diferencia no se resuelve por mayoría ni por IA:
**HALT / NO PROMOTION**.

### P17 — Diversidad técnica comprobada
Diversidad de software, build, runtime o criptografía sólo cuenta si sus raíces de fallo son
suficientemente distintas y están declaradas.

### P18 — Agilidad criptográfica
Ningún algoritmo concreto es eterno. Las operaciones de raíz deben poder migrar de suites por épocas,
sin borrar la verificabilidad histórica.

## 3. Propiedades actuales

### ICC-0
Una entrada no autorizada no cambia el estado confiable.

### ICE-0
Sin ingresos propios, gasto operativo nuevo = 0.

### BTR-8 — candidata
En el modelo estructural v0.5, las rutas principales estudiadas requieren 8 dominios independientes.
No demostrado en producción.

### eBTR
Antes de contar dominios se colapsan dependencias compartidas conocidas.

### CMC-2 — candidata
En la topología técnica objetivo v0.7, ninguna causa técnica catastrófica modelada por sí sola basta
para saltarse la validación canónica. La ruta técnica más corta modelada requiere 2 causas independientes.

No demostrado en producción.

## 4. Arquitectura resumida

PERSONA
  ↓
MAR INERTE
  ↓
EVIDENCIA + VERIFICADORES INDEPENDIENTES
  ↓
PUERTA DE PROMOCIÓN
  ↓
3 RESOLVERS INDEPENDIENTES
  ↓
ACUERDO EXACTO O PARADA
  ↓
NÚCLEO CRISTAL
  ↓
SNAPSHOT DETERMINISTA
  ↓
RECOMENDACIÓN CON PRUEBA

## 5. Continuidad
Al iniciar una sesión:
1. leer `CANON.md`;
2. leer `STATE.json`;
3. explicar en palabras sencillas dónde quedó HEBRA;
4. continuar desde `next_recommended_step`;
5. registrar decisiones, pruebas y fallos.

## 6. Transparencia
No ocultar vulnerabilidades, pruebas fallidas, supuestos ni limitaciones.

## 7. Estado resumido
COMMON-MODE-001 está completado a nivel de modelo.

Siguiente objetivo:
proteger la especificación misma y estudiar cómo detectar errores que podrían repetirse en tres
implementaciones diferentes porque todas interpretaron mal la misma regla.
