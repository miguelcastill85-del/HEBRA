# HEBRA Root Trust Architecture v0.5

Status: PROBADO EN MODELO / NO DEMOSTRADO EN PRODUCCIÓN

## 1. Constitutional Safety Floor (CSF)
El Núcleo Cristal contiene mínimos que una política ordinaria no puede reducir:

- ICC-0 permanece obligatorio.
- No aprendizaje online directo desde inputs de usuario.
- Una promoción exige Provenance, Measurement, Methodology y Safety.
- Cada cámara exige al menos 2 firmas independientes.
- Una identidad o dominio de fallo no puede satisfacer dos cámaras en la misma transición.
- El registro promovido es append-only.
- La lista de claves autorizadas no puede modificarse mediante política ordinaria.
- Una política puede elevar umbrales, nunca bajarlos por debajo del CSF.

Cambiar el CSF requiere una nueva versión mayor del Núcleo Cristal.

## 2. Evidence Gate
Promoción ordinaria:
- Provenance: 2-of-3
- Measurement: 2-of-3
- Methodology: 2-of-3
- Safety: 2-of-3
- No overlap entre las aprobaciones contadas

Corte mínimo estructural: 8 dominios independientes.

## 3. Kernel Release Gate
Para aceptar una versión capaz de modificar el CSF:
- Release Guardians: 4-of-7
- Reproducible Builders: 2-of-3
- Independent Release Auditors: 2-of-3
- No overlap entre aprobaciones contadas
- Hash público
- periodo de enfriamiento
- registro append-only de la versión

Corte mínimo estructural: 8.

## 4. Emergency Root Recovery
Sólo para pérdida o compromiso grave de claves:
- Recovery Guardians: 5-of-9
- Recovery Auditors: 3-of-5
- No overlap
- nueva época
- revocación explícita de claves antiguas
- declaración pública de recuperación

Corte mínimo estructural: 8.

## 5. Componentes con autoridad canónica cero
Por sí solos no pueden cambiar el estado confiable:
- usuario ordinario;
- servidor/API;
- modelo de IA;
- repositorio GitHub;
- frontend;
- almacén inerte;
- buscador/analytics.

Pueden afectar disponibilidad o mostrar información falsa en un dispositivo comprometido, pero no
deben alterar la raíz canónica.

## 6. Independencia real
“Independiente” significa distinto dominio de fallo, no sólo distinta cuenta.

Dos firmas no cuentan como independientes si dependen de la misma:
- persona;
- organización administradora;
- credencial raíz;
- automatización de despliegue;
- secreto compartido;
- servicio de firma.

## 7. Realidad actual
HEBRA todavía NO opera con estas cámaras distribuidas.
El repositorio actual es memoria de investigación y prototipo.

Por tanto, HEBRA no puede afirmar todavía “seguridad de 8 partes en producción”.
