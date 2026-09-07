# HEBRA ZERO v0.2 — Núcleo Cristal

## Objetivo
Eliminar por construcción la ruta clásica de *data poisoning*: los datos externos nunca entrenan,
reescriben ni modifican directamente el estado confiable. Todo input entra como evidencia inerte.
El núcleo sólo cambia mediante eventos que satisfacen una política de promoción verificable.

## Límite honesto
HEBRA ZERO puede garantizar **integridad y no-contaminación del estado bajo un modelo de amenazas
declarado**. No puede demostrar la verdad metafísica de una afirmación humana ni sobrevivir a una
ruptura simultánea de todas sus raíces de confianza, de la criptografía y del hardware. Por eso
"cero" significa:

> Para todo input no autorizado U, `TrustedState(T ∪ U, P) = TrustedState(T, P)`.

Es decir: entradas no autorizadas tienen influencia exactamente 0 sobre el estado confiable.

## 1. Dos universos separados

### Mar Inerte
Acepta cualquier entrada:
- testimonios;
- archivos;
- resultados;
- prompts;
- datos de sensores;
- propuestas de IA;
- cuentas nuevas.

Propiedades:
- content-addressed;
- append-only;
- no ejecutable;
- sin autoridad;
- nunca usado para entrenamiento online;
- nunca cambia una regla.

### Núcleo Cristal
Contiene únicamente:
- políticas firmadas;
- registros promovidos;
- attestations verificadas;
- snapshots deterministas;
- hashes de artefactos aprobados.

No acepta escritura directa.

## 2. Cápsula de Evidencia Inerte (CEI)
Cada input se convierte en bytes canónicos y recibe un hash. Una CEI puede contener una afirmación
falsa sin dañar al núcleo, porque **existir no equivale a ser confiable**.

Correcciones no sobrescriben. Crean una nueva CEI enlazada a la anterior.

## 3. Promoción por pruebas heterogéneas
Una CEI sólo puede influir en el Núcleo Cristal si satisface simultáneamente las clases exigidas por
la política, por ejemplo:

- `provenance`: el origen y la cadena de custodia son válidos.
- `measurement`: la medición/resultados fueron verificados.
- `methodology`: el contrato preregistrado y el análisis cumplen reglas.
- `independence`: las verificaciones requeridas provienen de entidades independientes.
- `safety`: la intervención está dentro del perfil de riesgo permitido.

Cada clase tiene su propio conjunto de claves y umbral. Una firma de usuario no sustituye una firma
de medición; diez cuentas nuevas no sustituyen una entidad independiente.

## 4. Regla de no-aprendizaje online
Ningún input de usuario:
- cambia pesos del modelo;
- cambia embeddings de una base usada como autoridad;
- cambia umbrales;
- cambia listas de verificadores;
- cambia código;
- cambia política.

La IA del sistema es **read-only respecto al Núcleo Cristal**. Puede proponer; no puede promover.

## 5. Snapshots deterministas
El conocimiento confiable no es una base mutable. Es una función pura:

`Snapshot = F(ledger_promovido, policy_hash, resolver_version)`

Dos nodos con los mismos inputs deben producir el mismo root hash.

## 6. Cambios de política
Las reglas del sistema son artefactos versionados y content-addressed.

Para cambiar una política se requiere:
1. propuesta explícita;
2. revisión independiente;
3. firmas por umbral de guardianes offline;
4. build reproducible del verificador;
5. nuevo hash de política;
6. activación futura explícita.

Datos ordinarios nunca pueden convertirse en política.

## 7. Código y supply chain
El kernel:
- no ejecuta contenido de CEI;
- no usa `eval`, plantillas ejecutables ni plugins dinámicos dentro del TCB;
- valida longitudes/tipos antes de parsear estructuras más complejas;
- usa dependencias fijadas;
- exige provenance de build;
- favorece builds reproducibles;
- publica hash de cada release;
- distribuye roots/actualizaciones con roles y firmas por umbral.

## 8. Modelos y algoritmos
Un modelo puede ser envenenado incluso offline. Por eso no es raíz de confianza.

Un modelo candidato:
1. se entrena sólo sobre un snapshot congelado explícito;
2. no sustituye el ledger;
3. queda content-addressed;
4. se evalúa en suites adversariales congeladas;
5. requiere promoción separada;
6. sus respuestas deben poder volver a evidencia/procedencia;
7. nunca tiene autoridad para aprobar sus propios datos o pesos.

La decisión crítica permanece en un resolver pequeño, determinista y auditable.

## 9. Invariante Cero de Contaminación

### Propiedad
Sea:
- `T`: conjunto de eventos promovidos;
- `U`: cualquier secuencia de entradas no autorizadas;
- `P`: política activa;
- `F`: resolver determinista.

Entonces:

`F(T ∪ U, P) = F(T, P)`

si ningún elemento de `U` satisface una transición autorizada de promoción.

### Consecuencia
Un atacante puede llenar el Mar Inerte con mil millones de falsedades. El coste operativo puede
subir (DoS es otro problema), pero el contenido confiable permanece idéntico.

## 10. Lo que el invariante NO demuestra
- Que una medición externa represente la realidad.
- Que un quorum entero de verificadores no colabore maliciosamente.
- Que una primitiva criptográfica jamás sea rota.
- Que hardware/compilador/OS estén libres de fallos.
- Que un método científicamente válido sea universalmente transferible.

Para datos humanos no verificables, HEBRA debe mantenerlos como `observational/untrusted` o usarlos
sólo para generar hipótesis, nunca para promover una afirmación fuerte.

## 11. Ataques y respuesta

| Ataque | Resultado esperado |
|---|---|
| 1M cuentas Sybil | 0 cambio en trusted root |
| dataset falso | 0 cambio sin attestations válidas |
| prompt injection | texto inerte; sin autoridad de control |
| modelo comprometido | puede proponer mal; no puede promover |
| una clave verificadora robada | insuficiente si no cumple todos los umbrales/clases |
| servidor DB comprometido | ledger/snapshot se detecta por hashes y firmas |
| reescritura histórica | rompe cadena/hash/proofs |
| dependencia maliciosa | build/hash/provenance no coinciden |
| política maliciosa enviada como "dato" | tratada como CEI; 0 autoridad |
| cambio legítimo de política | requiere canal separado y quorum de guardianes |

## 12. Regla de oro
**Nada que pueda ser aprendido del mundo tiene permiso automático para cambiar cómo HEBRA decide qué
es confiable.**

Esto separa para siempre:
- evidencia;
- decisión;
- política;
- código;
- identidad;
- ejecución.
