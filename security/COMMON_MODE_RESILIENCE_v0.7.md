# HEBRA — Common-Mode Resilience v0.7

Estado: PROBADO EN MODELO / NO DEMOSTRADO EN PRODUCCIÓN

## Objetivo

Evitar que una sola falla técnica compartida pueda convertir una transición inválida en estado
canónico confiable.

## Nueva propiedad candidata: CMC-2

**Common-Mode Cut 2 (CMC-2)**

En la topología objetivo, ninguna causa técnica catastrófica modelada por sí sola basta para saltarse
la validación canónica. La ruta técnica más corta estudiada requiere al menos dos causas independientes.

CMC-2 NO reemplaza ICC-0, BTR-8 ni eBTR. Es otra defensa.

## 1. Tres resolvers independientes

Una transición crítica debe ser evaluada por tres familias de implementación distintas:

- Resolver A
- Resolver B
- Resolver C

Requisitos:

- código independiente;
- lenguaje/runtime o toolchain independiente cuando sea posible;
- build provenance independiente;
- librería de parsing/canonicalización independiente;
- implementación criptográfica independiente cuando sea posible;
- mismo conjunto de vectores de prueba públicos.

### Regla de unanimidad

Los tres deben producir exactamente:

- mismo verdict;
- mismo transition hash;
- mismo next-state root.

Si hay una sola diferencia:

**HALT / NO PROMOTION**

No se usa mayoría 2-de-3 para decidir una verdad canónica.

## 2. Separar diversidad de implementación de diversidad de especificación

Tres programas distintos pueden repetir el mismo error de diseño.

Por eso todos se contrastan también contra:

- especificación formal;
- vectores de prueba congelados;
- casos negativos/adversariales;
- tests metamórficos;
- differential testing entre implementaciones.

Una discrepancia abre un incidente; no se “promedia”.

## 3. Diversidad criptográfica en cambios de raíz

Para checkpoints y operaciones capaces de cambiar raíz/política:

- Suite criptográfica A
- Suite criptográfica B, de familia matemática diferente

La prueba raíz debe satisfacer **AMBAS** suites.

Una sola suite rota no autoriza el cambio.

La elección concreta de algoritmos queda versionada en una Crypto Suite Policy y no se incrusta
como verdad eterna en el CANON.

## 4. Diversidad de implementación criptográfica

Usar dos algoritmos no sirve si todos los resolvers llaman a la misma biblioteca defectuosa.

Por eso, siempre que sea viable:

- Resolver A usa implementación criptográfica A1/B1;
- Resolver B usa A2/B2;
- Resolver C usa A3/B3.

Dependencias compartidas se registran en el grafo DCR y reducen la seguridad efectiva.

## 5. Compiler / Runtime / Build

Un build válido necesita:

- source hash;
- toolchain identity;
- dependency lock;
- build provenance;
- output hash;
- reproducibility evidence cuando aplique.

No se considera independiente a dos resolvers construidos por la misma raíz de build si esa raíz
puede alterar ambos.

## 6. Plataformas

En producción, los resolvers críticos no deben depender todos de la misma combinación de:

- sistema operativo;
- runtime;
- proveedor de ejecución;
- firmware/hardware root.

Durante el arranque de coste cero esto se diseña y simula, pero no se comprará hardware para fingir
diversidad antes de tener ingresos.

## 7. Núcleo sin red

El Resolver Canónico no necesita navegar Internet.

Inputs:
- ledger/promoted candidate;
- policy;
- key registry;
- proofs;
- frozen test vectors.

Outputs:
- verdict;
- transition hash;
- next root.

Cuanto menos pueda hacer, menos maneras existen de engañarlo.

## 8. Disagreement Freeze

Si A, B y C no coinciden:

1. no hay promoción;
2. se guarda el paquete exacto que produjo la diferencia;
3. se crea un incidente reproducible;
4. ninguna IA decide quién “tiene razón”;
5. una nueva versión sólo entra después de entender la causa.

## 9. Riesgos que siguen abiertos

CMC-2 no elimina:

- error compartido en la propia especificación;
- dos familias criptográficas rotas;
- coerción/colusión humana;
- vulnerabilidad universal de hardware;
- fallo desconocido compartido que no aparece en nuestro grafo;
- compromiso del dispositivo final que muestra una vista falsa.

La respuesta correcta a esos casos sigue siendo: detectar, abstenerse y parar antes que degradar.
