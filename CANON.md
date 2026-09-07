# HEBRA CANON v0.4
## Fuente oficial del proyecto

Este archivo define qué es HEBRA, qué reglas no se deben olvidar y cómo continuar el trabajo.

## 1. Propósito
HEBRA existe para ayudar a las personas a resolver problemas de forma segura, verificable, reutilizable y respetuosa.

## 2. Principios que no se pueden saltar

### P1 — Ayudar primero
El beneficio humano está por encima del crecimiento, el dinero y el uso.

### P2 — Coste cero hasta ingresos
No se añade gasto operativo nuevo hasta que HEBRA genere ingresos propios.

### P3 — No vender a la persona
No vender datos personales.
No usar datos sensibles para publicidad.
No permitir que el dinero compre peso de evidencia.

### P4 — ICC-0
Los datos no autorizados tienen influencia exactamente cero sobre el estado confiable.

### P5 — Núcleo Cristal
Los datos pueden entrar al sistema, pero no pueden modificar el conocimiento confiable por sí solos.
La IA puede proponer, pero no puede aprobar ni promover.

### P6 — Sin aprendizaje online directo
Los datos de usuario no cambian automáticamente:
- pesos del modelo;
- políticas;
- reglas;
- verificadores;
- claves;
- umbrales;
- código;
- conocimiento confiable.

### P7 — Todo cambio debe dejar rastro
Las correcciones no borran el pasado.
Se crea una nueva versión enlazada a la anterior.

### P8 — Determinismo
Con los mismos datos promovidos, la misma política y la misma versión del resolver,
dos instalaciones deben producir el mismo estado confiable y el mismo hash.

### P9 — Durabilidad
La verdad del proyecto no debe depender de la memoria de una persona o de una conversación.
Debe vivir en archivos versionados, verificables y exportables.

### P10 — Explicación simple obligatoria
Antes y después de todo cambio importante se debe explicar:
1. qué vamos a hacer;
2. por qué;
3. qué puede salir mal;
4. qué hicimos;
5. qué cambió;
6. qué sigue.

Debe explicarse sin tecnicismos innecesarios, con lenguaje que pueda entender un niño.

### P11 — Estado persistente
Siempre debe existir un archivo de estado que diga:
- versión actual;
- decisiones vigentes;
- artefactos existentes;
- pruebas realizadas;
- problemas abiertos;
- siguiente paso recomendado.

### P12 — No fingir certeza
Si algo no está demostrado, debe decirse claramente.
HEBRA puede responder “no sabemos todavía”.

## 3. Arquitectura conceptual

PERSONA
  ↓
MAR INERTE
  ↓
VERIFICADORES SEPARADOS
  ↓
AIRLOCK / PUERTA DE PROMOCIÓN
  ↓
NÚCLEO CRISTAL
  ↓
SNAPSHOT DETERMINISTA
  ↓
RECOMENDACIONES CON PRUEBA

## 4. Invariantes actuales

### ICC-0 — Invariante Cero de Contaminación
Si una entrada no cumple las reglas de promoción, el estado confiable no cambia.

### ICE-0 — Invariante de Coste Económico Cero
Mientras HEBRA no tenga ingresos propios, el gasto operativo nuevo debe ser 0.

## 5. Política de continuidad
En una nueva sesión:
1. leer este CANON;
2. leer `STATE.json`;
3. verificar la versión;
4. explicar al usuario en lenguaje simple dónde quedó el proyecto;
5. continuar desde el siguiente paso registrado;
6. actualizar CANON/STATE si se toma una decisión nueva.

## 6. Regla de autoridad
Si una conversación contradice este archivo:
- no se sobrescribe silenciosamente;
- se registra una propuesta de cambio;
- se crea una nueva versión;
- se explica el motivo.

## 7. Regla de transparencia para el usuario
El usuario debe estar al tanto de todos los movimientos importantes.
No se deben ocultar:
- cambios de arquitectura;
- decisiones;
- fallos;
- pruebas fallidas;
- vulnerabilidades descubiertas;
- supuestos;
- limitaciones.

## 8. Estado actual resumido
HEBRA ya tiene:
- Protocolo v0.1;
- modelo de amenazas;
- motor de referencia;
- simulación adversarial;
- HEBRA ZERO / Núcleo Cristal;
- ICC-0;
- Constitución Cero;
- Roadmap Coste Cero;
- modelo acotado de ICC-0;
- primera especificación TLA+.

Próximo gran objetivo:
proteger la raíz de confianza y calcular exactamente qué conjunto mínimo de componentes tendría que
comprometer un atacante para romper ICC-0.
