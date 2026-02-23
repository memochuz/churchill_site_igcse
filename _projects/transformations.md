---
title: 📝 Transformations of Functions
date: 2026-02-23
description: |
    <p>
    In this lesson, students study how graphs of functions can be transformed. They learn how to translate graphs horizontally and vertically, stretch and compress them both vertically and horizontally, and reflect them across the axes. Students focus on understanding how the correspondence rule changes and how the diagram is affected.
    </p>
    <hr>
    <h1>Class Objectives</h1>
    <ul>
      <li><b>Understand</b> how graphs can be translated horizontally and vertically.</li>
      <li><b>Describe</b> how the correspondence rule changes under translations.</li>
      <li><b>Understand</b> vertical and horizontal expansions and contractions.</li>
      <li><b>Correctly interpret</b> horizontal scale factors and reciprocal relationships.</li>
      <li><b>Recognise</b> reflections across the <i>x</i>-axis and <i>y</i>-axis.</li>
      <li><b>Use</b> vector notation to describe translations of functions.</li>
    </ul>

categories: [IGCSE, Functions]
image: '/images/Functions/transformations_front.png'
---

## Transformations of Functions

We will work with:

$$
f(x)=\sqrt{1-x^2}
$$

This represents the **upper semicircle** of radius 1 centered at the origin.

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/semicircle.png" width="600">
</p>

Domain:
$$
-1 \leq x \leq 1
$$

Range:
$$
0 \leq y \leq 1
$$

---

## Horizontal Translations

#### What happens to the graph?

- If we move the graph to the **right**, every point shifts right.
- If we move the graph to the **left**, every point shifts left.

#### General Rule

$$
f(x-a)
$$

- If \(a>0\): move **right**
- If \(a<0\): move **left**

> Horizontal shifts work in the opposite direction of the sign.


#### Example: Move 2 units right

$$
f(x-2)=\sqrt{1-(x-2)^2}
$$

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/semicircleright.png" width="600">
</p>

Effect:
- Center moves to \(x=2\)
- Domain becomes:
$$
1 \leq x \leq 3
$$

---

#### Example: Move 3 units left

$$
f(x+3)=\sqrt{1-(x+3)^2}
$$

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/semicircleleft.png" width="600">
</p>

Effect:
- Center moves to \(x=-3\)
- Domain:
$$
-4 \le x \le -2
$$

---

## Vertical Translations

#### What happens?

The whole graph moves **up or down**.

#### General Rule

$$
f(x)+k
$$

- If $k>0$: move **up**
- If $k<0$: move **down**


#### Example: Move up 2 units

$$
f(x)+2=\sqrt{1-x^2}+2
$$

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/semicircleup.png" width="600">
</p>

Range becomes:
$$
2 \leq y \leq 3
$$



#### Example: Move down 1 unit

$$
f(x)-1=\sqrt{1-x^2}-1
$$

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/semicircledown.png" width="600">
</p>

Range becomes:
$$
-1 \leq y \leq 0
$$

--- 

## Vertical Expansions and Contractions

#### General Rule

$$
a f(x)
$$

- If $a>1$: **Vertical Expansion (Stretch)**
- If $0<a<1$: **Vertical Contraction (Compression)**

We multiply the **output (y-values)**.



#### Example: Vertical Expansion by factor 2

$$
2f(x)=2\sqrt{1-x^2}
$$

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/semicircleve.png" width="600">
</p>

Range:
$$
[0,2]
$$


#### Example: Vertical Contraction by factor 1/2

$$
\frac{1}{2}f(x)=\frac{1}{2}\sqrt{1-x^2}
$$

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/semicirclevc.png" width="600">
</p>

Range:
$$
[0,\frac{1}{2}]
$$

---

## Horizontal Expansions and Contractions

#### General Rule

$$
f(bx)
$$

We modify the **input (x-values)**.


#### Interpretation of $b$

- If $b>1$: **Horizontal Contraction**
- If $0<b<1$: **Horizontal Expansion**

> The horizontal scale factor is $\frac{1}{b}$


#### Example: Horizontal Contraction with scaling factor $\frac{1}{2}$

$$
f(2x)=\sqrt{1-(2x)^2}
$$

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/semicirclehc.png" width="600">
</p>

Here:
- $b=2$
- Scale factor = $1/2$

New domain:

$$
-\frac{1}{2} \leq x \leq \frac{1}{2}
$$


#### Example: Horizontal Expansion with scaling factor $2$

$$
f(\frac{1}{2}x)=\sqrt{1-(\frac{1}{2} x)^2}
$$

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/semicirclehe.png" width="600">
</p>

Here:
- $b=\frac{1}{2}$
- Scale factor = $2$

New domain:
$$
-2 \leq x \leq 2
$$

---

## Reflections

#### Reflection across the x-axis

General rule:

$$
g(x)=-f(x)
$$

#### Example: Reflection Across the x-axis

$$
-f(x)=-\sqrt{1-x^2}
$$

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/semicirclerx.png" width="600">
</p>

Now it represents the lower semicircle.


#### Reflection Across the y-axis

General rule:

$$
g(x)=f(-x)
$$

#### Example: Reflection Across the y-axis

$$
f(-x)=\sqrt{1-(-x)^2}=\sqrt{1-x^2}
$$

Since $(-x)^2=x^2$, the graph does not change because it is symmetric. Instead, consider the function $g(x)=x^{3}$: 

$$
g(-x)=(-x)^{3}
$$

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/cubicry.png" width="600">
</p>



---

# Translations Using Vectors

A translation can be written as:

$$
\vec{v}=\begin{pmatrix}
a \\
b
\end{pmatrix}
$$

Meaning:
- Move $a$ units horizontally
- Move $b$ units vertically

#### General Combined Rule

$$
g(x)=f(x-a)+b
$$

Corresponds to translation vector:

$$
\vec{v}=
\begin{pmatrix}
a \\
b
\end{pmatrix}
$$

#### Example: Translations Using Vectors

$$
f(x)=\sqrt{1-(x-3)^2}+2
$$

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/cubicry.png" width="600">
</p>

Translation vector:

$$
\vec{v}=
\begin{pmatrix}
3 \\
2
\end{pmatrix}
$$

Meaning:
- Right 3
- Up 2

---

# Final Key Ideas

- **Horizontal shifts**: change inside brackets.
- **Vertical shifts**: change outside brackets.
- **Vertical stretch**: multiply the function.
- **Horizontal stretch**: multiply the variable.
- **Horizontal scale factor** = reciprocal.
- **Reflection in $x$-axis** → multiply whole function by $-1$.
- **Reflection in $y$-axis** → replace $x$ with $-x$.
- **Translations** can be written as vectors.