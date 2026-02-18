---
title: 📝 Quadratic Functions
date: 2026-02-17
description: |
    <p>
    In this lesson, students are introduced to quadratic functions. They learn what a second-degree polynomial is, how it is written in standard form, and why its graph is called a parabola. Students explore how the leading coefficient controls the opening direction of the parabola and how to find key features such as y-intercept, x-intercepts, vertex, and axis of symmetry. The lesson also introduces vertex form and how to convert between standard and vertex form.
    </p>
    <hr>
    <h1>Class Objectives</h1>
    <ul>
      <li><b>Define</b> a polynomial of degree two (quadratic function).</li>
      <li><b>Identify</b> the standard (general) form and the leading coefficient.</li>
      <li><b>Recognize</b> that quadratic graphs are parabolas.</li>
      <li><b>Determine</b> opening direction from the sign of the leading coefficient.</li>
      <li><b>Find</b> y-intercept, x-intercepts, vertex, and axis of symmetry.</li>
      <li><b>Use</b> vertex form and convert between forms.</li>
    </ul>

categories: [IGCSE, Quadratics]
image: '/images/Functions/parabola_front.png'
---

## What is a Quadratic Function?

A **quadratic function** is a **polynomial of degree two**.  
That means the highest power of $x$ is $x^2$.

General structure:

$$
f(x) = ax^2 + bx + c
$$

This is called the **standard form** (also called **general form**).

**Conditions:**

- $a, b, c$ are constants  
- $a \neq 0$ (otherwise it would not be quadratic)

### Main (Leading) Coefficient

The **main coefficient** (m.c.) or **leading coefficient** is the number multiplying $x^2$.

$$
f(x) = \underbrace{\textcolor{#FFB86C
}{a}}_{\text{m. c.}}x^{2} + bx + c
$$

This value controls the overall shape and opening direction of the graph.

---

## The Graph of a Quadratic: The Parabola

The graph of every quadratic function is called a **parabola**.

A **parabola** is a smooth, U-shaped curve that is symmetric about a vertical line.

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/parabola_basic.png" width="600">
</p>

---

## Opening Direction: Up or Down

The sign of the **leading coefficient $a$** determines how the parabola opens:

- If **$a > 0$** → opens **upward** → **concave up / convex**
- If **$a < 0$** → opens **downward** → **concave down / concave**

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/convexity.png" width="600">
</p>

Examples:

$$
f(x) = \underbrace{2}_{>0}x^2 + x \quad \text{opens up}
$$

$$
f(x) = \underbrace{-3}_{<0}x^2 + x \quad \text{opens down}
$$

---

## Key Features of a Parabola

The most important features are:

- **y-intercept**
- **x-intercepts (roots)** — can be 0, 1, or 2
- **vertex**
- **axis of symmetry**

Quadratic graphs are always **symmetric** about a **vertical line** that passes through the vertex.

---

#### y-Intercept

The **y-intercept** is where the graph crosses the y-axis.  
It occurs when $x = 0$.

Using standard form:

$$
f(x) = ax^2 + bx + \textcolor{#FFB86C}{c}
$$

$$
f(0) = \textcolor{#FFB86C}{c}
$$


<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/yintercept.png" width="600">
</p>

Therefore, the **y-intercept is $c$**.

Point: $(0, c)$

---

#### x-Intercepts (Roots)

The **x-intercepts** are where the graph crosses the x-axis.  
They occur when:

$$
f(x) = 0
$$

We solve using the **quadratic formula**:

$$
x = \frac{-b \pm \sqrt{\textcolor{#FFB86C}{b^2 - 4ac}}}{2a}
$$

###### Number of x-intercepts

Look at the value inside the square root:

$$
\Delta = \textcolor{#FFB86C}{b^2 - 4ac}
$$

- If **$\Delta > 0$** → **2 real solutions** → parabola crosses x-axis twice
- If **$\Delta = 0$** → **1 real solution** → touches x-axis once
- If **$\Delta < 0$** → **0 real solutions** → does not cross x-axis


<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/xintercepts.png" width="600">
</p>

---

#### Vertex of the Parabola (Turning Point)

The **vertex** is the highest or lowest point of the parabola.

Formula:

$$
x_{v} = \frac{-b}{2a}
$$

Then evaluate the function:

$$
y_{v} = f\!\left(\frac{-b}{2a}\right)
$$

Vertex:

$$
\text{Vertex} = (x_{v},y_{v}) = \left(\frac{-b}{2a},\; f\left(\frac{-b}{2a}\right)\right)
$$

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/vertex.png" width="600">
</p>

---

#### Axis of Symmetry

The parabola is symmetric about a vertical line through the vertex.

Equation of the axis:

$$
x = \frac{-b}{2a}
$$


> The graph is a mirror image on both sides of this vertical line.

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/simetria.png" width="600">
</p>


---

## Full Example (Standard Form)

Given:

$$
f(x) = x^2 - 4x + 3
$$

1. Identify the **coefficients** $a$, $b$, $c$  
1. State **whether the parabola opens up or down**  
1. Find the **y-intercept**  
1. Find the **x-intercepts** (if they exist)  
1. Find the **vertex**  
1. Find the **axis of symmetry**  
1. Sketch the parabola

**Step 1** — Identify coefficients

- $a = 1$
- $b = -4$
- $c = 3$

**Step 2** — Opening direction

$a>0$ → opens upward.

**Step 3** — y-intercept

$f(0)= (0)^{2}-4(0)+3=3$, therefore the $y$-intercept is
 
$$(0,3)$$

**Step 4** — x-intercepts

Using the quadratic formula:

$$
x = \frac{-(-4) \pm \sqrt{(-4)^2 - 4(1)(3)}}{2(1)}
= \frac{4 \pm \sqrt{16-12}}{2}
= \frac{4 \pm 2}{2}
$$

Solutions:

$$
x=1,\; x=3
$$

Intercepts: $(1,0)$, $(3,0)$

**Step 5** — Vertex

$$
x_v = \frac{-(-4)}{2(1)} = 2
$$

$$
y_v = f(2)=4-8+3=-1
$$

Vertex: $(2,-1)$

**Step 6** — Axis of symmetry

$$
x=2
$$

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/ejemplo.png" width="600">
</p>

---

## Vertex Form

Another way to write a quadratic is **vertex form**:

$$
f(x) = a(x-h)^2 + k
$$

### Meaning of the parameters

- $a$ → **opening & stretch**
- $h$ → **x-coordinate of vertex**
- $k$ → **y-coordinate of vertex**

Vertex:

$$
(h,k)
$$

---

## Converting Between Forms

#### From Vertex to Standard Form and Viceversa

Let's use the previous example of the parabola: $f(x)=x^{2}-4x+3$

**From standard to vertex form:**

First we find the vertex using: $\left(\frac{-b}{2a},\; f\left(\frac{-b}{2a}\right)\right)$

$$(x_{v},y_{v})=(2,-1)$$

and since $a=1$, then 


$$
f(x) = 1(x-2)^2 -1 = \textcolor{#FFB86C}{(x-2)^2 -1}.
$$

**From vertex to standard form:**

We just need to expand and simplify:

$$f(x)=(x-2)^2 -1=(x^{2}-4x+4)-1= \textcolor{#FFB86C}{x^{2}-4x+3}$$

---

## Summary

- A **quadratic function** is a degree-2 polynomial
- Standard form: $ax^2+bx+c$
- Graph is a **parabola**
- Sign of $a$ controls opening direction
- Key features:
  - y-intercept = $c$
  - x-intercepts → quadratic formula
  - vertex → $\left(-\frac{b}{2a}, f(-\frac{b}{2a})\right)$
  - axis → $x=-\frac{b}{2a}$
- Vertex form: $a(x-h)^2+k$
- We can convert between forms by finding the vertex or expanding
