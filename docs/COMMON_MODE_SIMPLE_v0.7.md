# HEBRA v0.7 — Explicación sencilla

## El nuevo problema

Supón que tenemos ocho guardianes diferentes.

Muy bien.

Pero todos usan la misma calculadora.

Si esa calculadora tiene un error, los ocho pueden equivocarse de la misma forma.

## Nuestra solución

HEBRA tendrá tres “calculadoras” hechas de forma diferente.

Las tres reciben exactamente el mismo problema.

Para cambiar el libro confiable, las tres tienen que responder exactamente lo mismo.

Si una dice 10, otra 10 y otra 11:

**HEBRA no elige 10 porque sean mayoría. Se detiene.**

¿Por qué?

Porque la diferencia demuestra que todavía no sabemos cuál está mal.

## También usamos dos tipos de cerradura para la raíz

Los cambios más peligrosos —los que podrían cambiar las reglas principales— deben superar dos
familias criptográficas diferentes.

Romper una sola no basta.

## Qué descubrimos con la simulación

- un solo resolver + una sola criptografía: una falla puede bastar;
- tres resolvers + una sola criptografía: la criptografía sigue siendo un punto único;
- tres resolvers + dos criptografías distintas: la ruta técnica más corta estudiada necesita dos
  fallas catastróficas distintas;
- si descubrimos que los tres resolvers comparten una misma raíz peligrosa, la seguridad vuelve a 1
  y esa configuración debe rechazarse.

## Nueva regla

**Una diferencia se convierte en una parada, no en una votación.**

Y una dependencia compartida conocida se cuenta como una sola debilidad, aunque tenga muchos nombres.
