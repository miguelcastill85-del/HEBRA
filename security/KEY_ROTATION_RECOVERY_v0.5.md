# HEBRA Key Rotation & Recovery v0.5

## Explicado simple
Una llave vieja no debe abrir HEBRA para siempre.
Y quien pierde una llave no puede inventarse otra por sí solo.

## Rotación normal
Para reemplazar una llave de un verificador:

1. Crear la nueva llave fuera del sistema activo.
2. Publicar su huella como propuesta.
3. Obtener aprobación de 2 miembros válidos actuales de esa cámara.
4. Obtener un testigo de rotación independiente.
5. Activar la nueva llave en una nueva época.
6. Marcar la vieja como revocada.
7. Conservar la clave pública vieja para poder verificar firmas históricas.

## Llave comprometida
1. Congelar inmediatamente la llave.
2. Desde ese momento aporta autoridad cero para nuevas acciones.
3. Las firmas históricas no se borran.
4. Reemplazarla mediante rotación normal si todavía existe quorum.
5. Si el quorum se perdió, usar Recuperación de Emergencia.

## Recuperación de emergencia
Requiere:
- 5-of-9 Recovery Guardians;
- 3-of-5 Recovery Auditors;
- dominios de fallo distintos.

Crea:
- nueva época raíz;
- nuevo registro de claves;
- conjunto explícito de revocaciones;
- motivo firmado;
- enlace a la raíz anterior;
- recibo determinista.

## Reglas que sólo avanzan
Una rotación no puede:
- bajar umbrales;
- borrar una revocación;
- reescribir firmas antiguas;
- reducir el número de época;
- reactivar silenciosamente una llave comprometida.

## Si falta gente para aprobar
HEBRA se detiene.

Es preferible dejar de aceptar nuevas evidencias antes que rebajar silenciosamente la seguridad.
