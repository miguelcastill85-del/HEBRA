# HEBRA Local Pilot v0.9

## Qué es
La primera utilidad real y local-first de HEBRA.

Permite:
- crear un Contrato de Resolución de bajo riesgo;
- definir una medida y un umbral antes del resultado;
- bloquear el contrato con SHA-256;
- registrar el resultado;
- calcular si cumplió la regla original;
- exportar/importar un JSON;
- guardar localmente sólo si el usuario lo activa.

## Coste
0.

## Cómo abrirlo
Opción más simple:
1. descarga `index.html`;
2. ábrelo con un navegador moderno.

Si tu navegador no permite Web Crypto en archivos locales:
1. abre una terminal en esta carpeta;
2. ejecuta `python -m http.server 8000`;
3. abre `http://localhost:8000`.

No requiere backend de HEBRA.

## Privacidad
La página tiene una Content Security Policy que bloquea conexiones externas.
No contiene:
- analítica;
- anuncios;
- fuentes externas;
- APIs;
- fetch;
- WebSocket.

Guardar en `localStorage` está apagado por defecto.

## Límites
Sólo aprendizaje, organización y hábitos cotidianos de bajo riesgo.
No salud, medicación, finanzas, derecho, emergencias, seguridad física ni autolesión.

Este cliente todavía NO promueve resultados al Núcleo Cristal ni afirma que una experiencia individual
sea evidencia global.
