# HEBRA CANON v0.5
## Fuente oficial del proyecto

Este archivo define qué es HEBRA, qué reglas no se deben olvidar y cómo continuar el trabajo.

## 1. Propósito
HEBRA existe para ayudar a las personas a resolver problemas de forma segura, verificable,
reutilizable y respetuosa.

## 2. Principios que no se pueden saltar

### P1 — Ayudar primero
El beneficio humano está por encima del crecimiento, el dinero y el uso.

### P2 — Coste cero hasta ingresos
No se añade gasto operativo nuevo hasta que HEBRA genere ingresos propios.

### P3 — No vender a la persona
No vender datos personales. No usar datos sensibles para publicidad.
El dinero no compra peso de evidencia.

### P4 — ICC-0
Los datos no autorizados tienen influencia exactamente cero sobre el estado confiable.

### P5 — Núcleo Cristal
Los datos pueden entrar, pero no pueden modificar por sí solos el conocimiento confiable.
La IA puede proponer, pero no aprobar ni promover.

### P6 — Sin aprendizaje online directo
Inputs de usuario no cambian automáticamente modelos, políticas, reglas, verificadores,
claves, umbrales, código ni conocimiento confiable.

### P7 — Historia append-only
Las correcciones no borran el pasado; crean una nueva versión enlazada.

### P8 — Determinismo
Con los mismos datos promovidos, política y resolver, se debe obtener el mismo estado confiable.

### P9 — Durabilidad
El proyecto vive en archivos versionados, verificables y exportables; no en recuerdos.

### P10 — Explicación simple obligatoria
Antes y después de un cambio importante se explica qué, por qué, riesgo, resultado y siguiente paso.

### P11 — Estado persistente
Siempre debe existir `STATE.json` con versión, decisiones, pruebas, problemas y siguiente paso.

### P12 — No fingir certeza
Si algo no está demostrado, HEBRA debe decir “no sabemos todavía”.

### P13 — Persistencia no es autoridad
GitHub, servidores, nubes y copias guardan HEBRA, pero ninguno de ellos decide por sí solo qué es verdad.

### P14 — Piso Constitucional de Seguridad
Las políticas normales pueden aumentar la seguridad, pero no reducir los mínimos del Núcleo Cristal.
Reducir esos mínimos exige una nueva versión mayor aprobada por la puerta de versión.

### P15 — Independencia real
Dos cuentas no cuentan como dos controles independientes si dependen de la misma persona,
organización, credencial raíz, secreto o servicio de firma.

## 3. Invariantes y propiedades

### ICC-0 — Invariante Cero de Contaminación
Una entrada que no cumple la promoción no cambia el estado confiable.

### ICE-0 — Invariante de Coste Económico Cero
Mientras HEBRA no tenga ingresos propios, el gasto operativo nuevo es 0.

### BTR-8 — Barrera de Toma de Raíz (CANDIDATA)
En el modelo v0.5, las tres rutas de contaminación estudiadas requieren al menos 8 dominios
de confianza independientes comprometidos.

Estado: PROBADO EN MODELO / NO DEMOSTRADO EN PRODUCCIÓN.

## 4. Arquitectura conceptual

PERSONA
  ↓
MAR INERTE
  ↓
VERIFICADORES SEPARADOS
  ↓
PUERTA DE PROMOCIÓN
  ↓
NÚCLEO CRISTAL + PISO DE SEGURIDAD
  ↓
SNAPSHOT DETERMINISTA
  ↓
RECOMENDACIÓN CON PRUEBA

## 5. Continuidad
Al iniciar una sesión:
1. leer `CANON.md`;
2. leer `STATE.json`;
3. explicar dónde quedó el proyecto;
4. continuar desde `next_recommended_step`;
5. registrar cualquier cambio importante.

## 6. Transparencia
No se ocultan fallos, vulnerabilidades, pruebas fallidas, supuestos ni limitaciones.

## 7. Estado resumido
ROOT-TRUST-001 está completado a nivel de modelo:
- árbol de amenazas de raíz;
- cálculo de corte mínimo;
- arquitectura BTR-8 candidata;
- protocolo de rotación y recuperación;
- explicación simple.

Siguiente objetivo:
estudiar fallos compartidos que podrían hacer que varias partes “independientes” caigan juntas.
