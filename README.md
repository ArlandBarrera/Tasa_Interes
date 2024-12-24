# 📊 Calculadora de Intereses

Programa que cálcula el interés acumulado a partir de un monto incial.

## ✨ Características

* 💻 Fácil de entender y utilizar.
* 🎨 Colores para indicar errores.

## Tipos de Interés

### 📈 Interés Simple

El más sencillo y el que menos rentabilidad aporta.

```python
# P = Monto incial
# r = Tasa de interès
# n = Nùmero de periodos acumulados
IS = P * r * n
```
### 💸 Interés Compuesto

La octava maravilla del mundo.

```python
# P = Monto incial
# r = Tasa de interés
# n = Cantidad de acumulaciones respecto a un año
# t = cantidad de tiempo trancurrido en años
IC = P * ( ( 1 + ( r / n) ) ** ( n * t) )
```
