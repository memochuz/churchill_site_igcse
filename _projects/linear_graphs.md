---
title: Graphing Linear Equations
description: |
    <p>The topic of graphing linear equations introduces students to visual representations of algebraic relationships. Each equation in two variables represents a straight line on the coordinate plane, defined by its <b>slope</b> and <b>y-intercept</b>. Understanding how to graph lines helps students interpret relationships between quantities, identify intersections, and connect algebraic and geometric reasoning.</p>
    <hr>
    <h1>Class Objectives</h1>
    <ul>
      <li><b>Understand</b> the structure of a linear equation and its connection to a line on the coordinate plane.</li>
      <li><b>Learn</b> how to isolate <i>y</i> and identify the slope (<i>m</i>) and y-intercept (<i>b</i>).</li>
      <li><b>Graph</b> lines by using the y-intercept and the slope to plot points.</li>
      <li><b>Compare</b> the slopes and intercepts of different lines to identify whether they are parallel, perpendicular, or intersecting.</li>
    </ul>

date: 2025-09-24
categories: [Bimester-1, Algebra, Geometry]
image: '/images/Line_Graph/line_front.png'
page_cover:
---

## What Is a Linear Equation?

A **linear equation** in two variables has the general form:

$$
ax + by = c
$$

Each equation represents a **straight line** on the coordinate plane.  
To graph it easily, we express it in **slope-intercept form** (that is, solved for $y$):

$$
y = mx + d
$$

where:
- $m$ is the **slope** of the line (which indicates its steepness, is always the coefficient of $x$)
- $d$ is the **y-intercept** (the point where the line crosses the y-axis, is always the constant term)

---

## How to Graph a Line

Let’s graph the line:

$$
2x + 3y = 6
$$


**Step 1.** Isolate $y$

To find the slope and y-intercept, isolate $y$:

$$
2x + 3y = 6 \implies 3y = -2x + 6 \implies \textcolor{#FFB86C}{y = -\frac{2}{3}x + 2}
$$

**Step 2.** Identify the slope and intercept

From the equation $y = \textcolor{#50FA7B}{-\frac{2}{3}}x + \textcolor{#8BE9FD}{2}$:

- **Slope:** $m = -\frac{2}{3}$  
- **Y-intercept:** $b = 2$

**Step 3.** Plot the y-intercept

Start at $(0, 2)$ on the y-axis.

**Step 4.** Use the slope to find another point

The slope $-\frac{2}{3}$ means that for every **3 units you move right**, you move **2 units down**.  
So from $(0, 2)$, move to the point $(3, 0)$.

**Step 5.** Draw the line

Connect the two points and extend the line in both directions.  
Label the line with its equation.

<p align="center">
  <img src="{{ site.baseurl }}/images/Line_Graph/line.png" alt="Line Graph Example" width="500">
</p>

---

## Parallel and Perpendicular Lines

1. **Parallel Lines:**  
   Two lines are parallel if they have the **same slope** but **different y-intercepts**.

   $$
   y = 2x + 1 \quad \text{and} \quad y = 2x - 3
   $$

   <p align="center">
       <img src="{{ site.baseurl }}/images/Line_Graph/parallel.png" alt="Parallel Lines" width="300">
   </p>

   In this case, both lines have a slope of $2$ but different y-intercepts ($1$ and $-3$), so they will never intersect.

2. **Perpendicular Lines:**  
   Two lines are perpendicular if their slopes are **negative reciprocals** of each other. That means if one line has a slope of $m$, the other line must have a slope of $-\frac{1}{m}$, or if the solope is a fraction $\frac{a}{b}$, the other line's slope is $-\frac{b}{a}$. We can think of this as switching the numerator and denominator and changing the sign. Being perpendicular means the lines intersect at a right angle (90 degrees).

   $$
   y = 2x + 1 \quad \text{and} \quad y = -\frac{1}{2}x + 4
   $$

   <p align="center">
       <img src="{{ site.baseurl }}/images/Line_Graph/perpendicular.png" alt="Perpendicular Lines" width="300">
   </p>

   Observe that the slopes $2$ and $-\frac{1}{2}$ are negative reciprocals, so the lines will intersect at a right angle.


