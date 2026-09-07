# HEBRA CANON v0.6
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
GitHub, servidores, nubes y copias guardan HEBRA, pero ninguno decide por sí solo qué es verdad.

### P14 — Piso Constitucional de Seguridad
Las políticas normales pueden aumentar la seguridad, pero no reducir los mínimos del Núcleo Cristal.

### P15 — Independencia real
Dos cuentas no cuentan como dos controles independientes si dependen de la misma raíz de control.

### P16 — Colapso de Dependencias (DCR-1)
Si varias aprobaciones comparten una dependencia crítica conocida que puede controlarlas,
HEBRA las agrupa como un único dominio de fallo efectivo para esa decisión.

### P17 — Desconocido no es independiente (UNI-1)
Si no se puede demostrar la independencia de una dependencia crítica, HEBRA no puede usarla para
aumentar el nivel de seguridad declarado.

## 3. Invariantes y propiedades

### ICC-0 — Invariante Cero de Contaminación
Una entrada que no cumple la promoción no cambia el estado confiable.

### ICE-0 — Invariante de Coste Económico Cero
Mientras HEBRA no tenga ingresos propios, el gasto operativo nuevo es 0.

### BTR-8 — Barrera estructural candidata
El modelo v0.5 exige 8 posiciones independientes para las tres rutas estudiadas.

### eBTR — Barrera efectiva
La seguridad real se calcula después de colapsar dependencias compartidas.
HEBRA sólo puede afirmar BTR-8 para una topología real si su eBTR comprobado es al menos 8.

Estado actual: PROBADO EN MODELOS / NO DEMOSTRADO EN PRODUCCIÓN.

## 4. Arquitectura conceptual

PERSONA
  ↓
MAR INERTE
  ↓
CERTIFICADOS DE INDEPENDENCIA
  ↓
COLAPSO DE DEPENDENCIAS
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
ROOT-TRUST-001 y SYSTEMIC-RISK-001 están completados a nivel de modelo.

Hallazgo clave de v0.6:
- 12 cuentas en 3 organizaciones pueden equivaler a sólo 2 raíces efectivas;
- una raíz de firma o identidad compartida puede reducir la barrera efectiva a 1;
- 12 raíces de control realmente separadas restauran el corte estructural 8.

Siguiente objetivo:
estudiar fallos comunes de software, criptografía, compiladores y otros componentes compartidos.
