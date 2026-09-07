# HEBRA Security Status v0.6

## Decidido
- ICC-0.
- ICE-0.
- Piso Constitucional de Seguridad.
- DCR-1: dependencias compartidas conocidas se colapsan.
- UNI-1: desconocido no equivale a independiente.

## Probado en modelo
- BTR-8 estructural para tres rutas principales.
- eBTR puede caer a 2 con 3 organizaciones compartidas.
- eBTR puede caer a 1 con una raíz de firma o identidad compartida.
- El validador rechaza 8 firmas que en realidad dependen de sólo 2 raíces.

## No demostrado todavía
- Seguridad de producción.
- Resistencia a fallos comunes de software/compilador/criptografía.
- Independencia real de futuros guardianes.
- Checkpoints firmados y externos.

## Siguiente
COMMON-MODE-001.
