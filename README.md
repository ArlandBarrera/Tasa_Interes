# 📊 Calculadora de Intereses

Programa para calcular el interés acumulado a partir de:
- monto inicial
- tasa de interés (%)
- periodo (mensual, trimestral, anual, etc)
- fecha de emisión
- fecha de terminación

## ✨ Características

* 💻 Fácil de entender y utilizar.

## Tipos de Intereses

### 📈 Interés Simple

El más sencillo y el que menos rentabilidad aporta. Crecimiento lineal.

```python
# P = Monto incial
# r = Tasa de interés
# n = Número de periodos acumulados
IS = P * r * n
```
### 💸 Interés Compuesto

La octava maravilla del mundo. Crecimiento exponencial.

```python
# P = Monto incial
# r = Tasa de interés
# n = Cantidad de acumulaciones respecto a un año
# t = cantidad de tiempo trancurrido en años
IC = P * ( ( 1 + ( r / n) ) ** ( n * t) )
```
