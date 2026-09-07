# HEBRA — Deterministic Cross-Check Protocol v0.7

## Explicado en una frase

Tres calculadoras diferentes reciben exactamente la misma cuenta; HEBRA sólo acepta el resultado
si las tres entregan exactamente la misma respuesta.

## Entrada canónica

Cada resolver recibe los mismos bytes canónicos:

- candidate_event;
- active_policy;
- key_registry;
- previous_trusted_root;
- required_proofs;
- resolver_protocol_version.

El input completo recibe `input_hash`.

## Salida obligatoria

Cada resolver produce:

- `verdict`: ACCEPT / REJECT / HALT
- `reason_code`
- `input_hash`
- `transition_hash`
- `next_trusted_root`
- `resolver_family`
- `resolver_version`
- `build_hash`
- `dependency_manifest_hash`

## Regla

Una transición sólo es elegible si:

1. los tres `input_hash` coinciden;
2. los tres verdict son ACCEPT;
3. los tres `transition_hash` coinciden;
4. los tres `next_trusted_root` coinciden;
5. los tres resolvers poseen certificados de independencia válidos;
6. ninguna dependencia crítica compartida invalida la diversidad mínima;
7. las pruebas criptográficas raíz cumplen todas las suites activas requeridas.

Cualquier diferencia produce `HALT_DIVERGENCE`.

## Nunca hacer

- escoger la mayoría;
- pedir a una IA que decida cuál resolver “parece correcto”;
- reintentar con datos ligeramente distintos hasta obtener acuerdo;
- ocultar una divergencia;
- degradar automáticamente de tres resolvers a uno.

## Paquete de divergencia

Cuando hay diferencia se conserva:

- input exacto;
- tres outputs;
- manifests de dependencias;
- hashes de build;
- política activa;
- key registry;
- timestamp/epoch.

Esto permite reproducir el problema sin alterar el estado confiable.
