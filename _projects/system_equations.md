---
title: 📝 System of Equations
description: |
    <p>The topic of systems of equations centers on finding values that satisfy two or more equations simultaneously. Students will explore different methods of solving, such as substitution, elimination, graphical representation and determinants. A key skill is recognizing when a system has a unique solution, no solution, or infinitely many solutions. By practicing these approaches, students develop logical reasoning and algebraic manipulation skills. This knowledge builds a foundation for real-world applications, where multiple conditions must be satisfied at the same time.</p>
    <hr>
    <h1>Class Objectives</h1>
    <ul>
      <li><b>Understand</b> what it means for two or more equations to form a system and the types of solutions possible.</li>
      <li><b>Explore</b> different methods of solving systems, including substitution, elimination, graphing and determinants.</li>
      <li><b>Develop</b> algebraic manipulation skills by isolating variables and rearranging equations.</li>
      <li><b>Apply</b> systems of equations to model and solve real-world problems involving multiple conditions.</li>
    </ul>

date: 2025-09-24
categories: [Bimester-1, Algebra, Geometry]
image: '/images/Systems_Equations/graphs.png'
page_cover:
---

## What Is a System of Equations?

A **system of equations** is a set of two or more equations that share the same variables.  
Solving the system means finding the values of those variables that make **all the equations true at the same time**.

  > Each equation represents a **line** on the coordinate plane.  

When we have **two equations**, there are **three possible cases**:

1. **The lines intersect** → the system has **one solution** (the intersection point).  
2. **The lines are parallel** → the system has **no solution**.  
3. **The lines are the same** → the system has **infinitely many solutions**.

  > In our case, **solving a system of equations** means **finding the coordinates of the intersection point** of the two lines.

**This is what a general system of two equations with two unknowns looks like:**

$$
\begin{cases}
a_1x + b_1y = c_1 \\
a_2x + b_2y = c_2
\end{cases}
$$

---

##  Determinants Method (Cramer’s Rule)

The **determinants method**, also known as **Cramer’s Rule**, is an algebraic way to solve **systems of linear equations** when:

- The number of equations equals the number of unknowns.  
- The **lines intersect**, meaning there is a unique solution.



In order to solve a system using determinants, we follow these steps:

$$
\begin{cases}
\textcolor{#FF5555}{a_1}x + \textcolor{#50FA7B}{b_1}y = \textcolor{#8BE9FD}{c_1} \\
\textcolor{#FF5555}{a_2}x + \textcolor{#50FA7B}{b_2}y = \textcolor{#8BE9FD}{c_2}
\end{cases}
$$

### Steps

1. **Find the main determinant $\Delta$:**

   $$
   \Delta =det 
   \begin{pmatrix}
   \textcolor{#FF5555}{a_1} & \textcolor{#50FA7B}{b_1} \\
   \textcolor{#FF5555}{a_2} & \textcolor{#50FA7B}{b_2}
   \end{pmatrix}
   = \textcolor{#FF5555}{a_1}\textcolor{#50FA7B}{b_2} - \textcolor{#FF5555}{a_2}\textcolor{#50FA7B}{b_1}
   $$
2. **Determinant for $x$:**

   $$
   \Delta_x = det
   \begin{pmatrix}
   \textcolor{#8BE9FD}{c_1} & \textcolor{#50FA7B}{b_1} \\
   \textcolor{#8BE9FD}{c_2} & \textcolor{#50FA7B}{b_2}
   \end{pmatrix}
   = \textcolor{#8BE9FD}{c_1}\textcolor{#50FA7B}{b_2} - \textcolor{#8BE9FD}{c_2}\textcolor{#50FA7B}{b_1}
   $$
3. **Determinant for $y$:**

   $$
   \Delta_y = det
   \begin{pmatrix}
   \textcolor{#FF5555}{a_1} & \textcolor{#8BE9FD}{c_1} \\
   \textcolor{#FF5555}{a_2} & \textcolor{#8BE9FD}{c_2}
   \end{pmatrix}
   = \textcolor{#FF5555}{a_1}\textcolor{#8BE9FD}{c_2} - \textcolor{#FF5555}{a_2}\textcolor{#8BE9FD}{c_1}
   $$
4. **Solution of the System**:

   $$
   x = \frac{\Delta_x}{\Delta}, \quad y = \frac{\Delta_y}{\Delta}
   $$
5. **Write the solution** as an ordered pair:

   $$
   (x, y) = \left(\frac{\Delta_x}{\Delta}, \frac{\Delta_y}{\Delta}\right)
   $$

### Example

$$
\begin{cases}
2x + 3y = 8 \\
x - y = 1
\end{cases}
$$

**Determinants:**

$$
\begin{align}
\Delta   &= \det\begin{pmatrix} 2 & 3 \\ 1 & -1 \end{pmatrix}
          = (2)(-1) - (1)(3)
          = -5, \\
\Delta_x &= \det\begin{pmatrix} 8 & 3 \\ 1 & -1 \end{pmatrix}
          = (8)(-1) - (1)(3)
          = -11, \\
\Delta_y &= \det\begin{pmatrix} 2 & 8 \\ 1 & 1 \end{pmatrix}
          = (2)(1) - (1)(8)
          = -6.
\end{align}
$$

**Solution:**

$$
\textcolor{#FFB86C}{x} = \frac{\Delta_x}{\Delta} = \frac{-11}{-5} = \textcolor{#FFB86C}{2.2}, \quad
\textcolor{#FF79C6}{y} = \frac{\Delta_y}{\Delta} = \frac{-6}{-5} = \textcolor{#FF79C6}{1.2}
$$

Therefore, the solution is:

$$
(\textcolor{#FFB86C}{x}, \textcolor{#FF79C6}{y}) = \left(\textcolor{#FFB86C}{2.2}, \textcolor{#FF79C6}{1.2}\right)
$$

---

## Sustitution Method

The **substitution method** is  used to solve systems of equations by isolating one variable in one equation and substituting that expression into the other equation. This method is particularly useful when one of the equations is already solved for one variable.


### Steps 

$$
\begin{cases}
2x + 3y = 8 \\
x - y = 1
\end{cases}
$$

1. **Isolate one variable** in one equation:

    From the second equation:

    $$
    \textcolor{#FFB86C}{x} - y = 1 \implies \underbrace{\textcolor{#FFB86C}{x} = \textcolor{#FF5555}{y + 1}}_{*}
    $$

2. **Substitute** this expression into the first equation:

$$
2(\textcolor{#FF5555}{y + 1}) + 3y = 8
$$

3. **Simplify** and solve for $y$:

$$
\begin{aligned}
2(\textcolor{#FF5555}{y + 1}) + 3y &= 8 \\
2y + 2 + 3y &= 8 \\
5y + 2 &= 8 \\
5y &= 6 \\
\textcolor{#8BE9FD}{y} &= \textcolor{#8BE9FD}{\frac{6}{5}}
\end{aligned}
$$

4. **Substitute** the value of $y$ back into the first equation (*) to find $x$:

$$
x = \frac{6}{5} + 1 = \frac{6}{5} + \frac{5}{5} = \frac{11}{5}
$$


5. **Write the solution** as an ordered pair:

$$
(x, y) = \left(\frac{11}{5}, \frac{6}{5}\right) = \left(\textcolor{#FFB86C}{2.2}, \textcolor{#FF79C6}{1.2}\right)
$$

---

## Elimination Method

The **elimination method** is  used to solve systems of equations by adding or subtracting the equations to eliminate one variable. This method is useful when the coefficients of one variable are the same or can easily be made the same.

### Steps

$$
\begin{cases}
2x + 3y = 8 \\
x - y = 1
\end{cases}
$$

1. **Multiply one or both equations** (if necessary) so that the coefficients of one variable are the same (or opposites).

   Multiply the second equation by **2** to match the coefficient of $x$::

   $$
   \begin{cases}
   2x + 3y = 8 \\
   2x - 2y = 2
   \end{cases}
   $$

2. **Subtract** one equation from the other to eliminate $x$:

   $$
   (2x + 3y) - (2x - 2y) = 8 - 2
   $$

3. **Simplify** and solve for $y$:

   $$
   \begin{aligned}
   \textcolor{#FF5555}{2x} + 3y \textcolor{#FF5555}{- 2x} + 2y &= 6 \\
   5y &= 6 \\
   y &= \frac{6}{5}
   \end{aligned}
   $$

4. **Substitute** the value of $y$ into one of the original equations to find $x$:

   From $x - \textcolor{#FFB86C}{y} = 1$:

   $$
   x - \textcolor{#FFB86C}{\frac{6}{5}} = 1 \implies x = 1 + \frac{6}{5} = \frac{11}{5}
   $$

5. **Write the solution** as an ordered pair:

   $$
   (x, y) = \left(\frac{11}{5}, \frac{6}{5}\right) = \left(\textcolor{#FFB86C}{2.2}, \textcolor{#FF79C6}{1.2}\right)
   $$

--- 

## Graphical Method

Finally, the **graphical method** is a visual technique used to solve systems of equations by representing each equation as a line on a coordinate plane.  
The **solution** is the **point where the two lines intersect**, since that point satisfies both equations.

### Steps

$$
\begin{cases}
2x + 3y = 8 \\
x - y = 1
\end{cases}
$$

1. **Isolate $y$** in both equations to express them in **slope-intercept form** $y = mx + b$.

   From the first equation:

   $$
   2x + 3y = 8 \implies 3y = -2x + 8 \implies \textcolor{#FF5555}{y = -\frac{2}{3}x + \frac{8}{3}}
   $$

   From the second equation:

   $$
   x - y = 1 \implies -y = -x + 1 \implies \textcolor{#FF5555}{y = x - 1}
   $$

2. **Identify the slope** $m$ and the **y-intercept** $b$ of each line:

   - For $y = -\frac{2}{3}x + \frac{8}{3}$:  
     - Slope $m_1 = -\frac{2}{3}$  
     - y-intercept $b_1 = \frac{8}{3}$

   - For $y = x - 1$:  
     - Slope $m_2 = 1$  
     - y-intercept $b_2 = -1$

3. **Graph both lines** on the coordinate plane:  
   - Start at the y-intercept $b$ for each line.  
   - Use the slope $m = \frac{\text{rise}}{\text{run}}$ to plot a second point on each line.  
   - Draw both lines extending in both directions.

4. **Locate the intersection point**, this point represents the **solution** to the system because it satisfies both equations.

   By observation or algebraic verification, the lines intersect at:

   $$
   (x, y) = \left(\frac{11}{5}, \frac{6}{5}\right) = \left(\textcolor{#FFB86C}{2.2}, \textcolor{#FF79C6}{1.2}\right)
   $$

<p align="center">
  <img src="{{ site.baseurl }}/images/Systems_Equations/graphs_front.png" alt="Systems of Equations">
</p>