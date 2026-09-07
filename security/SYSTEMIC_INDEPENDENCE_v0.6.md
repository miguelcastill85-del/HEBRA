# HEBRA Systemic Independence v0.6

Status: PROBADO EN MODELO / NO DEMOSTRADO EN PRODUCCIÓN

## 1. Effective BTR (eBTR)
BTR nominal cuenta posiciones de confianza.
eBTR cuenta causas independientes capaces de comprometer esas posiciones.

HEBRA no debe anunciar BTR-8 en una topología real si eBTR < 8.

## 2. Dependency Collapse Rule (DCR-1)
Si dos o más signers comparten una dependencia crítica cuyo compromiso puede dar autoridad sobre
ambos, se agrupan en un único failure-domain efectivo para esa decisión.

## 3. Unknown-is-not-independent (UNI-1)
Una dependencia crítica desconocida no prueba independencia.
Un signer con datos críticos incompletos no puede elevar el nivel de seguridad declarado.

## 4. Independence Certificate
Cada signer crítico debe publicar, como mínimo:
- signer_id
- operator_control_id
- organization_control_id
- key_custody_root_id
- identity_root_id
- signing_service_root_id
- recovery_controller_id
- verifier_implementation_family
- build_provenance_root

Los identificadores deben revelar relaciones de control sin necesitar publicar secretos.

## 5. Quorum validation
Para Evidence Gate:
- 2 approvals efectivos distintos en cada cámara;
- un failure-domain efectivo no puede contar en dos cámaras;
- al menos 8 dominios efectivos en total;
- dependencias críticas desconocidas reducen o invalidan el quorum.

## 6. Finding from v0.6 model
- 12 accounts controlled by 3 organizations -> effective cut 2.
- one shared signing root -> effective cut 1.
- 12 distinct control roots -> effective cut 8.
- distinct people with one shared identity root -> effective cut 1.

## 7. Remaining systemic risks
DCR-1 handles KNOWN control dependencies.
It does not magically detect:
- unknown shared vulnerabilities;
- universal cryptographic breaks;
- a bug in every verifier implementation;
- coercion or secret collusion;
- common hardware/firmware compromise.

Those remain separate red-team targets.
