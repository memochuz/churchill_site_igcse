---
title: 📝 System of Inequalities
description: |
    <p>The topic of graphing linear inequalities introduces students to regions rather than single lines on the coordinate plane. Each inequality in two variables represents a half-plane bounded by a line, showing all possible solutions that satisfy the condition. Understanding how to graph inequalities helps students visualize constraints, distinguish between strict and inclusive boundaries, and interpret how multiple conditions overlap. In a system of inequalities, the solution is found by identifying the region of intersection of all half-planes, allowing students to connect algebraic reasoning with geometric representation in meaningful, real-world contexts.</p>
    <hr>
    <h1>Class Objectives</h1>
    <ul>
      <li><b>Understand</b> that a linear inequality in two variables represents a half-plane on the coordinate grid.</li>
      <li><b>Learn</b> how to graph inequalities using solid or dashed boundary lines and shading the correct region.</li>
      <li><b>Interpret</b> a system of inequalities as overlapping half-planes, whose intersection forms the solution region.</li>
      <li><b>Apply</b> systems of inequalities to model real-world situations involving restrictions or feasible sets.</li>
    </ul>

date: 2025-11-18
categories: [Bimester-2, Algebra, Geometry]
image: '/images/System_Inequalities/system.png'
page_cover:
---

## What Is a System of Inequalities?

A **system of inequalities** is a set of two or more inequalities that share the same variables.  


Solving the system means finding all the points that **satisfy every inequality at the same time**.

> Each inequality represents a **half-plane** on the coordinate plane, not just a line.

**This is what a general system of three inequalities with two unknowns looks like:**

$$
\begin{cases}
a_1x + b_1y \leq c_1 \\
a_2x + b_2y > c_2 \\
a_3x + b_3y \geq c_3
\end{cases}
$$

---

## Understanding a Single Inequality

If we **temporarily replace** the inequality symbol with an equal sign, we obtain a linear equation.  
This line divides the coordinate plane into **two half-planes**.   The line is called the **boundary line** of the inequality.

<p align="center">
   <img src="{{ site.baseurl }}/images/System_Inequalities/single_1.png" alt="Single Inequality" width="700">
</p>

The original inequality tells us **which** of the two half-planes represents the solution set.

### Steps

To correctly interpret and graph an inequality we follow these steps:

1. Isolate $y$ and replace the inequality with an equal sign to find the **boundary line**. For this example we'll use the inequalities $-x-1+y>0$ and $-x-1+y\leq 0$:
2. Draw the resulting line. Depending on the original inequality symbol, draw the boundary line as **solid** (≤, ≥) or **dashed** (<, >).

<p align="center">
   <img src="{{ site.baseurl }}/images/System_Inequalities/type_line.png" alt="Single Inequality" width="700">
</p>
3. Chage the inequality back to its original form.:
   * If the result is $ y \geq \dots$ or $y > \dots$, shade the region **above** the line.
   * If the result is $ y \leq \dots$ or $y < \dots$, shade the region **below** the line.

<p align="center">
   <img src="{{ site.baseurl }}/images/System_Inequalities/type_plane.png" alt="Single Inequality" width="700">
</p>
### Boundary Line Rules

Depending on the symbol (≤, ≥, <, >):

- **≤ or ≥** → the boundary line is **solid** (included).  
- **< or >** → the boundary line is **dashed** (not included).

---

## What Happens in a System?

Each inequality shades a **region** of the plane.  
When we have **two or more inequalities**, the solution is not a single point but a **shared region**, formed by the intersection of all half-planes.

Here are the two most typical scenarios:

1. **The half-planes overlap** → the system has a **non-empty solution region**.  
2. **The half-planes do not overlap** → the system has **no solution region**.  

> In our case, solving a system of inequalities means **finding the common shaded region** formed by all half-planes in the system.

### Steps

Consider the following system of inequalities:

$$
\begin{cases}
  -x - 1 + y &\leq 0 \\
  -y-x+2 &> 0 \\
  y &\geq -2
\end{cases}
$$

1. **Isolate the variable $y$** in each inequality to rewrite them in a more convenient form for graphing.

  $$
  \begin{cases}
   y & \leq x + 1 \\
   y &< -x+2 \\
   y &\geq -2
  \end{cases}
  $$
  
2.**Graph the boundary line and the region** for each inequality.

  * Use a solid line if the inequality includes the equals sign (≥ or ≤).
  * Use a dashed line if it is a strict inequality (< or >). Then determine the correct half-plane by interpreting the sign.

  <p align="center">
     <img src="{{ site.baseurl }}/images/System_Inequalities/regions.png" alt="Single Inequality" width="700">
  </p>
3. **Identify the intersection region** where all shaded areas overlap.
   That overlapping region represents the solution set of the system.


  <p align="center">
     <img src="{{ site.baseurl }}/images/System_Inequalities/solution.png" alt="Single Inequality" width="700">
  </p>