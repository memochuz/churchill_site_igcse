---
title: 📝 Recognising and Finding Functions
date: 2026-02-18
description: |
    <p>
    In this lesson, students learn how to recognise different types of functions from their graphs and from their rule of correspondence. They explore how coefficients affect the shape of linear, quadratic, cubic, reciprocal and exponential graphs. Students also learn how to sketch these functions using key features and how to determine equations from graphs or given points.
    </p>
    <hr>
    <h1>Class Objectives</h1>
    <ul>
      <li><b>Recognise</b> linear and quadratic functions from their graphs and equations.</li>
      <li><b>Sketch</b> graphs using coefficients and key features.</li>
      <li><b>Identify</b> cubic, reciprocal and exponential graphs.</li>
      <li><b>Find</b> intercepts and asymptotes where appropriate.</li>
      <li><b>Determine</b> the equation of a function from a graph or given points.</li>
    </ul>

categories: [IGCSE, Functions]
image: '/images/Functions/type_functions_front.png'
---


## Linear Functions

#### Standard Form

$$
f(x)=mx+c
$$

- $m$ → **gradient (slope)**
- $c$ → **y-intercept**

#### How to Recognise from the Graph

- Straight line
- Constant gradient
- No curves

#### How Coefficients Help Sketch

- $c$ gives starting point on y-axis
- $m>0$ → increasing line
- $m<0$ → decreasing line
- Larger gradient steeper line

#### Sketching Steps

1. Plot $(0,c)$
2. Use gradient (rise/run)
3. Draw straight line

#### Graph

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/linear.png" width="600">
</p>

---

## Quadratic Functions

#### Standard Form

$$
f(x)=ax^2+bx+c
$$

- $a$ → leading (main) coefficient
- $c$ → y-intercept

#### How to Recognise from the Graph

- U-shaped curve
- Symmetric about vertical line
- Has a vertex (turning point)

#### How Coefficients Help Sketch

- $a>0$ → opens up
- $a<0$ → opens down
- Larger $a$ → narrower parabola
- $c$ → y-intercept
- Axis of symmetry: $x=-\frac{b}{2a}$

#### Key Features to Sketch

- y-intercept: $(0,c)$
- x-intercepts (if any): solve $ax^2+bx+c=0$
- vertex: $\left(-\frac{b}{2a}, f\left(-\frac{b}{2a}\right)\right)$

#### Graph

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/parabola_sketch.png" width="600">
</p>

---

## Cubic Functions

#### Standard Form

$$
f(x)=ax^3+bx^2+cx+d
$$

#### How to Recognise

- S-shaped curve
- Has a point of inflection (change from convex to concave or viceversa)
- Can have up to 2 turning points

#### Coefficient Effect

- $a>0$ → falls left, rises right
- $a<0$ → rises left, falls right
- $d$ → y-intercept

#### Intercepts

- y-intercept: $(0,d)$
- x-intercepts: solve $f(x)=0$ (use the calculator to find these values)

#### Graphs

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/cubic.png" width="600">
</p>

---

## Rational Functions

#### Basic Form

$$
f(x)=\frac{a}{x}
$$

#### How to Recognise

- Two separate curves (Hyperbola)
- Never touches axes
- Has asymptotes

#### Asymptotes

- Vertical asymptote: $x=0$
- Horizontal asymptote: $y=0$

#### Coefficient Effect

- $a>0$ → branches in Quadrants I & III
- $a<0$ → branches in Quadrants II & IV

#### Graphs

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/rational_basic.png" width="600">
</p>

## General Rational Function

A more general form of a rational function is:

$$
f(x)=\frac{ax+b}{cx+d}
$$

where:

- $a,b,c,d$ are constants  
- $c \neq 0$


#### How to Recognise from the Graph

- Two branches (usually)
- Has vertical and horizontal asymptotes
- Curve approaches asymptotes but never touches them


#### Finding the Asymptotes

**Vertical Asymptote**

Occurs when the denominator equals zero:

$$
f(x)=\frac{ax+b}{\textcolor{#C99DF2}{cx+d}}
$$

We need to solve:

$$
cx+d=0.
$$


Therefore,

$$
\underbrace{x=-\frac{d}{c}}_{\text{vertical asymptote}}
$$

**Horizontal Asymptote**

The horizontal asymptote is found by looking at the coefficients of the highest power of $x$ in the numerator and the denominator, and simply dividing them.

$$
f(x)=\frac{\textcolor{#3CEA82}{a}x+b}{\textcolor{#3CEA82}{c}x+d}
$$

Since numerator and denominator have the same degree (both degree 1):

$$
\underbrace{y=\frac{a}{c}}_{\text{horizontal asymptote}}
$$


#### y-Intercept

To find the y-intercept, substitute $x=0$ in the formula:

$$f(x)=\frac{ax+\textcolor{#FF5555}{b}}{cx+\textcolor{#FF5555}{d}},$$

$$
f(0)=\frac{b}{d}
$$

So the y-intercept is:

$$
\left(0,\frac{b}{d}\right)
$$

(provided $d \neq 0$)


#### x-Intercept

The x-intercept occurs when:

$$
f(x)=0
$$

A fraction equals zero when the **numerator equals zero**:  

$$f(x)=\frac{\overbrace{\textcolor{#FFB86C}{ax+b}}^{=0}}{cx+d},$$

$$
ax+b=0
$$

Solve:

$$
x=-\frac{b}{a}
$$

So the x-intercept is:

$$
\left(-\frac{b}{a},0\right)
$$

(provided this value does not make the denominator zero)

#### Position of the Graph (Quadrants)

The position of the branches depends on:

- The vertical asymptote $x=-\frac{d}{c}$
- The horizontal asymptote $y=\frac{a}{c}$
- The sign of $ad - bc$

**The $ad-bc$ test**

If:

$$
ad - bc<0
$$

The branches behave like $\frac{1}{x}$ (similar orientation as Quadrants I & III relative to the asymptotes).

If:

$$
ad - bc>0
$$

The branches behave like $-\frac{1}{x}$ (similar orientation as Quadrants II & IV relative to the asymptotes).

#### Graphs

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/rational_general.png" width="600">
</p>

---

## Exponential Functions

#### Standard Form

$$
f(x)=a \cdot b^x
$$

where $b>0$, $b\neq 1$

#### How to Recognise

- Rapid growth or decay
- Horizontal asymptote at $y=0$
- Never touches x-axis

### Coefficient Effect

- $b>1$ → exponential growth
- $0<b<1$ → exponential decay
- $a$ → y-intercept

Since:

$$
f(0)= a \cdot \underbrace{ b ^{0}}_{1} = a
$$

#### Graphs

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/exponential.png" width="600">
</p>

---

## Finding the Equation from a Graph or Points

#### Linear Function from Two Points

Given $(x_1,y_1)$ and $(x_2,y_2)$:

**Step 1 — Find gradient**

$$
m=\frac{y_2-y_1}{x_2-x_1}
$$

**Step 2 — Use point-slope form**

$$
y-y_1=m(x-x_1)
$$

Then rearrange to:

$$
y=mx+c
$$

---

#### Quadratic from Graph Features

If you know:

- Vertex $(h,k)$
- Another point

Use vertex form:

$$
f(x)=a(x-h)^2+k
$$

Substitute the known point to find $a$.

---
#### Quadratic from Three Points

If you know **three points** on a parabola, you can find its equation.

Suppose the three points are:

$$
(x_1,y_1), \quad (x_2,y_2), \quad (x_3,y_3)
$$

**Step 1 — Use Standard Form**

Start with the general quadratic form:

$$
f(x)=ax^2+bx+c
$$


**Step 2 — Substitute Each Point**

Substitute each point into the equation.

For $(x_1,y_1)$:

$$
ax_1^2 + bx_1 + c = y_1
$$

For $(x_2,y_2)$:

$$
ax_2^2 + bx_2 + c = y_2
$$

For $(x_3,y_3)$:

$$
ax_3^2 + bx_3 + c = y_3
$$


**Step 3 — Solve the System**

You now have **three equations** with three unknowns, $a,\; b,\; c$:

$$
\begin{cases}
ax_1^2 + bx_1 + c & = y_1\\
\\
ax_2^2 + bx_2 + c & = y_2 \\
\\
ax_3^2 + bx_3 + c & = y_3
\end{cases}
$$

Solve the system (by substitution, elimination or calculator).

**Step 4 — Write the Final Equation**

Once you find $a$, $b$, and $c$, write:

$$
f(x)=ax^2+bx+c
$$

###### Example

Suppose the parabola passes through:

$$
(0,1), \quad (1,3), \quad (2,9)
$$

**Step 1 — Start with**

$$
f(x)=ax^2+bx+c
$$

**Step 2 — Substitute Points**

From $(0,1)$:

$$
c=1
$$

From $(1,3)$:

$$
a+b+1=3 \Rightarrow a+b=2
$$


From $(2,9)$:

$$
4a+2b+1=9 \Rightarrow 4a+2b=8
$$


**Step 3 — Solve the System**

We have:

$$
\begin{cases}
a+b & =2 \\
4a+2b&=8 \\
c&=1
\end{cases}
$$

Multiply the first equation by 2:

$$
\begin{cases}
2a+2b & =4 \\
4a+2b&=8
\end{cases}
$$

Subtract:

$$
(4a+2b)-(2a+2b)=8-4 \Rightarrow 2a=4 \Rightarrow a=2
$$


Then:

$$
b=0
$$

**Step 4 — Final Equation**

$$
f(x)=2x^2+1
$$


---

#### Exponential from Two Points

If:

$$
f(x)=ab^x
$$

1. Use $f(0)=a$
2. Substitute another point to find $b$

---

#### Reciprocal from Graph

If asymptotes are:

- Vertical: $x=p$
- Horizontal: $y=q$

General form:

$$
f(x)=\frac{a}{x-p}+q
$$

Use a known point to find $a$.

---

## Cubic from Graph

If intercepts are known:

$$
f(x)=a(x-r_1)(x-r_2)(x-r_3)
$$

Use a known point to find $a$.

---

# Summary Table

| Function Type | Shape | Key Feature | Asymptotes |
|--------------|--------|------------|------------|
| Linear | Straight line | Gradient constant | None |
| Quadratic | U-shape | Vertex | None |
| Cubic | S-shape | Inflection point | None |
| Exponential | Growth/decay | Rapid increase/decrease | $y=0$ |
| Reciprocal | Two branches | Undefined at $x=0$ | $x=0$, $y=0$ |
| Rational | Two branches | Undefined at $x=\frac{-d}{c}$ | $x=\frac{-d}{c}$, $y=\frac{a}{c}$ |

---

# Final Teaching Focus

Students should be able to:

- Recognise function types from shape
- Use coefficients to predict behaviour
- Sketch using intercepts and symmetry
- Find equations from graphs or data
- Identify asymptotes where appropriate
