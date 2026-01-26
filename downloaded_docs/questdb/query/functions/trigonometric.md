On this page

This page describes the available functions to assist with performing
trigonometric calculations.

tip

Positive and negative infinity values are expressed as `'Infinity'` or
`'-Infinity'` in QuestDB.

## sin[​](#sin "Direct link to sin")

`sin(angleRadians)` returns the trigonometric sine of an angle.

### Arguments[​](#arguments "Direct link to Arguments")

* `angleRadians` is a numeric value indicating the angle in radians.

### Return value[​](#return-value "Direct link to Return value")

Return value type is `double`.

### Description[​](#description "Direct link to Description")

Special case: if the argument is `NaN` or an infinity, then the result is
`Null`.

### Examples[​](#examples "Direct link to Examples")

```prism-code
SELECT pi()/2 angle, sin(pi()/2) sin;
```

| angle | sin |
| --- | --- |
| 1.570796326794 | 1 |

## cos[​](#cos "Direct link to cos")

`cos(angleRadians)` returns the trigonometric cosine of an angle.

### Arguments[​](#arguments-1 "Direct link to Arguments")

* `angleRadians` numeric value for the angle, in radians.

### Return value[​](#return-value-1 "Direct link to Return value")

Return value type is `double`.

### Description[​](#description-1 "Direct link to Description")

Special case: if the argument is `NaN` or an infinity, then the result is
`Null`.

### Examples[​](#examples-1 "Direct link to Examples")

```prism-code
SELECT pi()/2 angle, cos(pi()/2) cos;
```

| angle | cos |
| --- | --- |
| 1.570796326794 | 6.123233995736766e-17 |

## tan[​](#tan "Direct link to tan")

`tan(angleRadians)` returns the trigonometric tangent of an angle.

### Arguments[​](#arguments-2 "Direct link to Arguments")

* `angleRadians` numeric value for the angle, in radians.

### Return value[​](#return-value-2 "Direct link to Return value")

Return value type is `double`.

### Description[​](#description-2 "Direct link to Description")

Special case: if the argument is `NaN` or an infinity, then the result is
`Null`.

### Examples[​](#examples-2 "Direct link to Examples")

```prism-code
SELECT pi()/2 angle, tan(pi()/2) tan;
```

| angle | tan |
| --- | --- |
| 1.570796326794 | 16331239353195370 |

## cot[​](#cot "Direct link to cot")

`cot(angleRadians)` returns the trigonometric cotangent of an angle.

### Arguments[​](#arguments-3 "Direct link to Arguments")

* `angleRadians` numeric value for the angle, in radians.

### Return value[​](#return-value-3 "Direct link to Return value")

Return value type is `double`.

### Description[​](#description-3 "Direct link to Description")

Special case: if the argument is `NaN`, 0, or an infinity, then the result is
`Null`.

### Examples[​](#examples-3 "Direct link to Examples")

```prism-code
SELECT pi()/2 angle, cot(pi()/2) cot;
```

| angle | cot |
| --- | --- |
| 1.570796326794 | 6.123233995736766e-17 |

## asin[​](#asin "Direct link to asin")

`asin(value)` the arcsine of a value.

### Arguments[​](#arguments-4 "Direct link to Arguments")

* `value` is a numeric value whose arcsine is to be returned.

### Return value[​](#return-value-4 "Direct link to Return value")

Return value type is `double`. The returned angle is between -pi/2 and pi/2
inclusively.

### Description[​](#description-4 "Direct link to Description")

Special case: if the argument is `NaN` or an infinity, then the result is
`Null`.

### Examples[​](#examples-4 "Direct link to Examples")

```prism-code
SELECT asin(1.0) asin;
```

| asin |
| --- |
| 1.570796326794 |

## acos[​](#acos "Direct link to acos")

`acos(value)` returns the arccosine of a value.

### Arguments[​](#arguments-5 "Direct link to Arguments")

* `value` is a numeric value whose arccosine is to be returned. The returned
  angle is between 0.0 and pi inclusively.

### Return value[​](#return-value-5 "Direct link to Return value")

Return value type is `double`.

### Description[​](#description-5 "Direct link to Description")

Special cases: if the argument is `NaN` or its absolute value is greater than 1,
then the result is `Null`.

### Examples[​](#examples-5 "Direct link to Examples")

```prism-code
SELECT acos(0.0) acos;
```

| acos |
| --- |
| 1.570796326794 |

## atan[​](#atan "Direct link to atan")

`atan(value)` returns the arctangent of a value.

### Arguments[​](#arguments-6 "Direct link to Arguments")

* `value` is a numeric value whose arctangent is to be returned.

### Return value[​](#return-value-6 "Direct link to Return value")

Return value type is `double`. The returned angle is between -pi/2 and pi/2
inclusively.

### Description[​](#description-6 "Direct link to Description")

Special cases:

* If the argument is `NaN`, then the result is `Null`.
* If the argument is infinity, then the result is the closest value to pi/2 with
  the same sign as the input.

### Examples[​](#examples-6 "Direct link to Examples")

Special case where input is `'-Infinity'`:

```prism-code
SELECT atan('-Infinity');
```

Returns the closest value to pi/2 with the same sign as the input:

| atan |
| --- |
| -1.570796326794 |

```prism-code
SELECT atan(1.0) atan;
```

| atan |
| --- |
| 0.785398163397 |

## atan2[​](#atan2 "Direct link to atan2")

`atan2(valueY, valueX)` returns the angle *theta* from the conversion of
rectangular coordinates (x, y) to polar (r, theta). This function computes
*theta* (the phase) by computing an arctangent of y/x in the range of -pi to pi
inclusively.

### Arguments[​](#arguments-7 "Direct link to Arguments")

* `valueY` numeric ordinate coordinate.
* `valueX` numeric abscissa coordinate.

note

The arguments to this function pass the y-coordinate first and the x-coordinate
second.

### Return value[​](#return-value-7 "Direct link to Return value")

Return value type is `double` between -pi and pi inclusively.

### Description:[​](#description-7 "Direct link to Description:")

`atan2(valueY, valueX)` measures the counterclockwise angle *theta*, in radians,
between the positive x-axis and the point (x, y):

![Atan2 trigonometric function](/docs/assets/images/atan2-91669677e453f5a7ad2f396dd8254bf2.svg)

Special cases:

| input `valueY` | input `valueX` | `atan2` return value |
| --- | --- | --- |
| 0 | Positive value | 0 |
| Positive finite value | 'Infinity' | 0 |
| -0 | Positive value | 0 |
| Negative finite value | 'Infinity' | 0 |
| 0 | Negative value | Double value closest to pi |
| Positive finite value | '-Infinity' | Double value closest to pi |
| -0 | Negative value | Double value closest to -pi |
| Negative finite value | '-Infinity' | Double value closest to -pi |
| Positive value | 0 or -0 | Double value closest to pi/2 |
| 'Infinity' | Finite value | Double value closest to pi/2 |
| Negative value | 0 or -0 | Double value closest to -pi/2 |
| '-Infinity' | Finite value | Double value closest to -pi/2 |
| 'Infinity' | 'Infinity' | Double value closest to pi/4 |
| 'Infinity' | '-Infinity' | Double value closest to 3/4 \* pi |
| '-Infinity' | 'Infinity' | Double value closest to -pi/4 |
| '-Infinity' | '-Infinity' | Double value closest to -3/4 \* pi |

### Examples[​](#examples-7 "Direct link to Examples")

```prism-code
SELECT atan2(1.0, 1.0) atan2;
```

| atan2 |
| --- |
| 0.785398163397 |

## radians[​](#radians "Direct link to radians")

`radians(angleDegrees)` converts an angle measured in degrees to the equivalent
angle measured in radians.

### Arguments[​](#arguments-8 "Direct link to Arguments")

* `angleDegrees` numeric value for the angle in degrees.

### Return value[​](#return-value-8 "Direct link to Return value")

Return value type is `double`.

### Examples[​](#examples-8 "Direct link to Examples")

```prism-code
SELECT radians(180);
```

| radians |
| --- |
| 3.141592653589 |

## degrees[​](#degrees "Direct link to degrees")

`degrees(angleRadians)` converts an angle measured in radians to the equivalent
angle measured in degrees.

### Arguments[​](#arguments-9 "Direct link to Arguments")

* `angleRadians` numeric value for the angle in radians.

### Return value[​](#return-value-9 "Direct link to Return value")

Return value type is `double`.

### Examples[​](#examples-9 "Direct link to Examples")

```prism-code
SELECT degrees(pi());
```

| degrees |
| --- |
| 180 |

## pi[​](#pi "Direct link to pi")

`pi()` returns the constant pi as a double.

### Arguments[​](#arguments-10 "Direct link to Arguments")

None.

### Return value[​](#return-value-10 "Direct link to Return value")

Return value type is `double`.

### Examples[​](#examples-10 "Direct link to Examples")

```prism-code
SELECT pi();
```

| pi |
| --- |
| 3.141592653589 |