# HEBRA CANON v0.9
## Fuente oficial del proyecto

## 1. Propósito
HEBRA existe para ayudar a las personas a aprender de intentos reales de forma segura, verificable,
reutilizable y respetuosa.

## 2. Principios no negociables

1. Ayudar primero.
2. Gasto operativo nuevo = 0 hasta ingresos propios.
3. No vender datos personales.
4. Datos no autorizados tienen influencia cero sobre el estado confiable (ICC-0).
5. La IA puede proponer, no promover.
6. No aprendizaje online directo desde inputs de usuario.
7. Historia append-only.
8. Mismos inputs y mismas reglas deben dar el mismo resultado.
9. La memoria oficial vive en archivos versionados, no en recuerdos.
10. Cada cambio importante se explica en lenguaje sencillo.
11. `STATE.json` dice siempre dónde estamos.
12. No fingir certeza.
13. GitHub es persistencia, no autoridad de verdad.
14. Políticas normales no pueden debilitar el Piso Constitucional de Seguridad.
15. Dependencias compartidas se colapsan antes de contar independencia.
16. Divergencia entre resolvers críticos significa HALT.
17. Diversidad técnica sólo cuenta si está demostrada.
18. Criptografía debe poder migrar por épocas.
19. Cambiar semántica exige cambiar versión.
20. Las reglas críticas deben tener especificación ejecutable y vectores de prueba.
21. Campos o versiones desconocidos se rechazan.
22. El primer producto debe ser local-first y útil sin servidor.
23. Guardar datos localmente requiere decisión explícita del usuario.
24. El piloto inicial sólo cubre aprendizaje, organización y hábitos cotidianos de bajo riesgo.
25. Una huella SHA-256 local es compromiso/consistencia, no prueba de autoría.

## 3. Estado del producto

HEBRA Local Pilot v0.9 existe como una sola página HTML.

Puede:
- crear un Contrato de Resolución;
- definir una regla numérica de éxito antes del resultado;
- bloquear los campos del contrato en la sesión;
- calcular una huella SHA-256;
- cerrar un resultado;
- calcular éxito según la regla original;
- exportar/importar JSON;
- recalcular huellas al importar;
- usar localStorage sólo si el usuario lo activa.

No puede todavía:
- convertir una experiencia en evidencia global;
- firmar externamente identidad/autoría;
- promover al Núcleo Cristal;
- garantizar seguridad de producción.

## 4. Privacidad del piloto

La página:
- no usa servidor HEBRA;
- no usa fetch;
- no usa WebSocket;
- no usa analítica;
- no usa anuncios;
- bloquea conexiones externas mediante CSP;
- no guarda localmente por defecto.

## 5. Continuidad

Leer `CANON.md`, después `STATE.json`, explicar el estado y continuar desde el siguiente paso.

## 6. Siguiente objetivo

Ejecutar el primer ensayo real del cliente en navegador con un problema de bajo riesgo, exportar el
registro y comprobar que el ciclo completo persona → contrato → bloqueo → resultado → exportación
funciona de punta a punta.
