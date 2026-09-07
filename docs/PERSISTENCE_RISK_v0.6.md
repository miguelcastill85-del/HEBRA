# PERSISTENCE-001 — GitHub main branch unprotected

## Explicado simple
GitHub guarda nuestra memoria, pero la rama `main` fue observada sin protección.

Eso significa que una cuenta con permisos suficientes podría reescribir historial o cambiar archivos.

## Por qué no rompe la raíz de confianza
HEBRA ya establece que GitHub es almacenamiento y memoria versionada, no autoridad canónica de verdad.

## Qué debemos hacer
Cuando configuremos la gobernanza de repositorio:
- impedir force-push a `main`;
- exigir revisión antes de cambios críticos;
- exigir pruebas automáticas para archivos del Núcleo;
- publicar checkpoints fuera del propio repositorio;
- más adelante firmar releases/checkpoints.

## Estado
ABIERTO.

No es necesario gastar dinero para corregirlo.
