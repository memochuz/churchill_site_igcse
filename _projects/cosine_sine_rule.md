---
title: 📝 Sine Rule, Cosine Rule and Area of a Triangle
date: 2026-03-06
description: |
    <p>
    In this lesson, students study how to solve triangles using trigonometric rules. 
    The Sine Rule and Cosine Rule allow us to find missing sides or angles in any triangle, 
    not only right triangles. Students also learn how to calculate the area of a triangle 
    using trigonometry when the height is not known. Special attention is given to deciding 
    which formula to use and understanding cases where two triangles or no triangle are possible.
    </p>
    <hr>
    <h1>Class Objectives</h1>
    <ul>
      <li><b>Understand</b> when to use the Sine Rule and Cosine Rule.</li>
      <li><b>Solve</b> triangles using trigonometric relationships.</li>
      <li><b>Calculate</b> the area of a triangle using the sine formula.</li>
      <li><b>Identify</b> cases where two triangles are possible.</li>
      <li><b>Recognise</b> situations where no triangle can exist.</li>
    </ul>

categories: [IGCSE, Trigonometry]
image: '/images/Geometry/triangle.png'
---

## Solving Non-Right Triangles

Right triangles can be solved using **SOH CAH TOA**. However, many triangles **do not have a right angle**.

For these cases we use:

- **Sine Rule**
- **Cosine Rule**

These rules allow us to find **missing sides and angles in any triangle**.



#### Sine Rule

The **Sine Rule** relates the sides of a triangle with the sine of their opposite angles.

$$
\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}
$$

Where:

- $a$ is opposite angle $A$
- $b$ is opposite angle $B$
- $c$ is opposite angle $C$


#### When to Use the Sine Rule

Use the **Sine Rule** when you know:

1. **Two angles and one side (AAS or ASA)**
2. **Two sides and a non-included angle (SSA)**

#### Examples:

###### Case AAS

- $A = 40^\circ$
- $B = 65^\circ$
- $a = 8$
- Find $b$

<p align="center">
   <img src="{{ site.baseurl }}/images/Geometry/sinerule_1.png" width="600">
</p>

Then:

$$
\frac{8}{\sin (40^\circ)} = \frac{b}{\sin (65^\circ)}
$$

therefore

$$
b = \frac{8 \times \sin (65^\circ)}{\sin 40^\circ} \approx 8.88
$$


###### Case SSA:  Ambiguous (Two Possible Triangles)

Sometimes the **Sine Rule produces two different triangles**.

This happens when we know:

- **Two sides**
- **An angle NOT between them (SSA)**

Example situation:

- $a = 4$
- $b = 5$
- $A = 48^\circ$
- Find $B$

With these values we could generate two different triangles: one acute triangle or one obtuse triangle, both satisfying the initial conditions.

<p align="center">
   <img src="{{ site.baseurl }}/images/Geometry/sinerule_2.png" width="600">
</p>

Using the sine rule:

$$
\sin B = \frac{b \sin A}{a} \Rightarrow B = \frac{5 \times \sin(48)}{4} = 0.92893
$$

If we observe the graph of $\sin(x)$ and the unit circle, we notice that there are two values of $B$ that satisfy the equation (which makes sense since we have two possible triangles):

<p align="center">
   <img src="{{ site.baseurl }}/images/Geometry/sinerule_4.png" width="600">
</p>

$$
B = \sin^{-1}(0.92893)\approx \underbrace{68.27 ^{\circ}}_{\text{first $\triangle$}} \quad \text{or} \quad \underbrace{111.73^{\circ}}_{\text{second $\triangle$}}
$$

The second angle is obtained by subtraction: 

$$
180^{\circ}-68.27^{\circ}= 111.73^{\circ}
$$

Therefore:

- **Two different triangles may exist.**


<p align="center">
   <img src="{{ site.baseurl }}/images/Geometry/sinerule_3.png" width="600">
</p>

Puedes añadir una tercera situación dentro del caso **SSA** donde **no existe triángulo**. Te dejo el bloque listo para integrar con tu mismo estilo:

###### Case SSA: No Triangle Exists

In some SSA situations **no triangle can be formed**. This occurs when the side opposite the given angle is **too short to reach the other side**.

<p align="center">
   <img src="{{ site.baseurl }}/images/Geometry/sinerule_5.png" width="600">
</p>

Example:

* $a = 2$
* $b = 6$
* $A = 30^\circ$
* Find $b$

Using the sine rule:

$$
\sin (B) = \frac{b \sin (A)}{a}
$$

Substitute the values:

$$
\sin (B) = \frac{6 \times \sin(30^\circ)}{2} =1.5
$$


But the sine function **cannot be greater than 1**:

$$
-1 \leq \sin(x) \leq 1
$$

Since

$$
\sin B = 1.5
$$

there is **no possible angle $B$**.

Therefore:

* **No triangle exists with these measurements.**


---

## Cosine Rule

The **Cosine Rule** is used when the Sine Rule cannot be applied.

There are two forms.

#### Finding a Side

$$
c^2 = a^2 + b^2 - 2ab\cos(C)
$$

Observe that in this formula, in order to find $c$, we need the other two sides and the angle between them. Therefore, we may need to rearrange the formula depending on the information given in the problem.

$$
a^2 = b^2 + c^2 - 2bc\cos(A) \quad \text{or} \quad b^2 = a^2 + c^2 - 2ac\cos(B)
$$

#### Finding an Angle

If we isolate the angle in each of the previous formulas, we obtain three different formulas for finding the angle.

$$
\begin{align*}
C & =\cos^{-1}\left( \frac{c^2 - a^2 - b^2}{-2ab}\right) \\
B & =\cos^{-1}\left( \frac{b^2 - a^2 - c^2}{-2ac}\right) \\
A & =\cos^{-1}\left( \frac{a^2 - b^2 - c^2}{-2bc}\right) \\
\end{align*}
$$



#### When to Use the Cosine Rule

Use the **Cosine Rule** when you know:

1. **Two sides and the included angle (SAS)**
2. **All three sides (SSS)**

#### Examples:

###### Case SAS
- $b = 7$
- $c = 9$
- $A = 50^\circ$
- Find $a$

$$
a^2 = 7^2 + 9^2 - 2(7)(9)\cos 50^\circ \Rightarrow a = 7.00063
$$

###### Case SSS
- $b = 10$
- $c = 9$
- $a = 11$
- Find $C$


$$C= \cos^{-1}\left( \frac{9^2 - 11^2 - 10^2}{-2(11)(10)}\right) = \cos^{-1}(\frac{7}{11}) \approx 50.46^{\circ} $$

---

## Area of a Triangle Using Sine

Sometimes we cannot use

$$
Area = \frac{1}{2} \times base \times height
$$

because **the height is unknown**.

Instead we use:

$$
Area = \frac{1}{2}ab\sin (C)
$$

Where:

- $a$ and $b$ are two sides
- $C$ is the **included angle**


#### Example

Given:

- $a = 10$
- $b = 7$
- $C = 40^\circ$

$$
Area = \frac{1}{2}(10)(7)\sin 40^\circ \approx 22.5
$$



---

## Choosing the Correct Formula

#### Use **Sine Rule**

- ASA
- AAS
- SSA

#### Use **Cosine Rule**

- SAS
- SSS

#### Use **Area Formula**

- Two sides and the included angle.

---

## Important Exam Ideas

- Always label **opposite sides and angles correctly**.
- Check your calculator is in **degree mode**.
- The Sine Rule may give **two possible triangles**.
- If $ \sin(\theta) > 1 $, **no triangle exists**.
- Clearly show which rule you are using.

---

## Final Key Ideas

- The **Sine Rule** connects sides and opposite angles.
- The **Cosine Rule** works like an extended Pythagorean theorem.
- The **Area formula using sine** avoids needing the height.
- Some triangles can produce **two solutions**.
- Some measurements produce **no possible triangle**.