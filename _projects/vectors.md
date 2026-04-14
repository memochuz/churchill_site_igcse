---
title: Vectors
date: 2026-04-13
description: |
    <p>
    In this lesson, students learn the fundamental concepts of vectors. 
    Vectors are essential in mathematics and physics, as they allow us 
    to represent objects that have both magnitude and direction.
    </p>
    <hr>
    <h1>Class Objectives</h1>
    <ul>
      <li><b>Understand</b> what a vector is.</li>
      <li><b>Represent</b> vectors algebraically and geometrically.</li>
      <li><b>Perform</b> operations with vectors.</li>
      <li><b>Interpret</b> vectors geometrically.</li>
      <li><b>Apply</b> vectors in problem solving.</li>
    </ul>

categories: [IGCSE, Algebra]
image: '/images/Vectors/vectors_portada.png'
---

## What is a Vector?

A **vector** is an object that has:

* **Magnitude** (size or length)  
* **Direction**  

Vectors are often represented as arrows in a coordinate plane, where the length of the arrow represents the magnitude and the direction of the arrow shows the direction of the vector.

A vector is drawn as an arrow from the origin $(0,0)$ to a point in the plane.

<p align="center">
<img src="{{ site.baseurl }}/images/Vectors/vectors.png" width="800">
</p>

However, vectors *can be moved* anywhere in the plane as long as their **magnitude and direction remain the same**. We do this to help visualize geometric operations such as addition, subtraction, or physical situations like forces.

A vector can be written as:

$$
\vec{v} = \begin{pmatrix} x \\ y \end{pmatrix} = (x,y)
$$

The first component $x$ is called the **horizontal component**, and the second component $y$ is called the **vertical component**. It behaves like a coordinate point, but it actually represents an **arrow from the origin to that point** when drawn in standard position.

---

## Vector Operations

#### Addition

When we add two vectors, we add their corresponding components:

$$
\begin{pmatrix} a \\ b \end{pmatrix}
+
\begin{pmatrix} c \\ d \end{pmatrix}
=
\begin{pmatrix} a+c \\ b+d \end{pmatrix}
$$


###### Geometrically (Parallelogram Law)

To add two vectors:

1. Place them tail-to-tail  
2. Complete a parallelogram  
3. The diagonal represents the sum  


<p align="center">
<img src="{{ site.baseurl }}/images/Vectors/vectors_sum.png" width="800">
</p>

This is called the **parallelogram law**


#### Vector Subtraction

To subtract two vectors, we can think of it as adding the opposite vector, which is equivalent to subtracting their components:

$$
\begin{pmatrix} a \\ b \end{pmatrix}
-
\begin{pmatrix} c \\ d \end{pmatrix}
=
\begin{pmatrix} a-c \\ b-d \end{pmatrix}
$$



###### Geometrically

To visualize vector subtraction:

1. Draw the two vectors starting from the origin  
2. Join the tips (endpoints) of the vectors  
3. Draw a new arrow from the tip of the second vector to the tip of the first vector (head minus tail)  

<p align="center">
<img src="{{ site.baseurl }}/images/Vectors/vectors_resta.png" width="800">
</p>

This new arrow represents the difference between the vectors. Since this vector does not start at the origin, we can translate it back to the origin. The resulting vector is the subtraction.



#### Scalar Multiplication

Multiplying a vector by a number (scalar) changes its magnitude and possibly its direction. We multiply each component by the scalar:

$$
k \begin{pmatrix} a \\ b \end{pmatrix}
=
\begin{pmatrix} ka \\ kb \end{pmatrix}
$$


###### Geometrically

* $k > 1$ → vector becomes **longer**, the magnitude increases by multiplying by $k$
* $0 < k < 1$ → vector becomes **shorter**, the magnitude decreases by multiplying by $k$
* $k < 0$ → vector **reverses direction** , the arrow points in the opposite direction, and depending on the value of $k$, it can also change in length.

<p align="center">
<img src="{{ site.baseurl }}/images/Vectors/vectors_scalar_mult.png" width="800">
</p>

---

## Magnitude (Norm) of a Vector

The **magnitude** (or norm) represents the **length** of the vector. For a vector $\vec{v} = \begin{pmatrix} x \\ y \end{pmatrix}$, the magnitude is calculated using the Pythagorean theorem:

$$
|\vec{v}| = \sqrt{x^2 + y^2}
$$

This formula comes from the fact that the vector forms a right triangle with its horizontal and vertical components, where the magnitude is the hypotenuse.

<p align="center">
<img src="{{ site.baseurl }}/images/Vectors/vectors_norms.png" width="800">
</p>



#### Example

Find the magnitude of the vector:

$$
\vec{v} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}
$$

Then,

$$
|\vec{v}| = \sqrt{3^2 + 4^2} = 5
$$


---

## Vector Between Two Points

Given two points:

$$
A(x_1, y_1), \quad B(x_2, y_2)
$$

The vector from $A$ to $B$ is:

$$
\overrightarrow{AB} = \begin{pmatrix} x_2 - x_1 \\ y_2 - y_1 \end{pmatrix}
$$

> Head minus tail (tip minus start)

Remember that the order matters in subtraction, as it determines the direction of the resulting vector. The vector $\overrightarrow{AB}$ points from $A$ to $B$, while $\overrightarrow{BA}$ would point from $B$ to $A$ and would be the opposite vector. Also, at the end, we may need to translate the resulting vector **back to the origin** for calculations, as we are interested in its magnitude and direction rather than its position in the plane.

<p align="center">
<img src="{{ site.baseurl }}/images/Vectors/vectors_points.png" width="800">
</p>

---

## Examples

### Example 1: Addition

$$
\begin{pmatrix} 2 \\ 3 \end{pmatrix}
+
\begin{pmatrix} 4 \\ 1 \end{pmatrix}
=
\begin{pmatrix} 6 \\ 4 \end{pmatrix}
$$

---

### Example 2: Scalar Multiplication

$$
2 \begin{pmatrix} 3 \\ -1 \end{pmatrix}
=
\begin{pmatrix} 6 \\ -2 \end{pmatrix}
$$

---

### Example 3: Vector Between Points

Let:

$$
A(1,2), \quad B(5,6)
$$

$$
\overrightarrow{AB} = \begin{pmatrix} 5-1 \\ 6-2 \end{pmatrix}
=
\begin{pmatrix} 4 \\ 4 \end{pmatrix}
$$

---

## Common Mistakes

* Forgetting direction matters  
* Subtracting in the wrong order   
* Forgetting to use Pythagoras for magnitude  
* Not translating back to the origin when needed