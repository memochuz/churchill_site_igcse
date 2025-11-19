---
title: 📝 Graphing Linear Equations
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
image: '/images/Graph_Linear_Equations/line_1.png'
page_cover:
---

## What Is a Linear Equation?

A **linear equation** in two variables has the general form:

$$
ax + by = c,
$$

where $a,b$ and $c$ are real numbers. Each such equation represents a **straight line** on the coordinate plane.

Notice that a linear equation in two variables: 
  * Contains only two variables. 
  * The highest exponent of each variable is $1$.
  * At least one of the variables ($x$ or $y$) must be present (that is, either $a$ or $b$ must be different from zero).

 This is what makes the equation linear. Linear equations **do not include** squared terms, square roots, products of the variables, or any other non-linear expressions.

To graph it easily, we express it in **slope-intercept form** (that is, solved for $y$):

$$
y = mx + d
$$

where:
- $m$ is the **slope** of the line (which indicates its steepness, **is always the coefficient of $x$**)
- $d$ is the **y-intercept** (the point **where the line crosses the y-axis**, is always the constant term)

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

<p align="center">
  <img src="{{ site.baseurl }}/images/Graph_Linear_Equations/line_2.png" alt="Y-intercept" width="700">
</p>

**Step 4.** Use the slope to find another point. 

From the y-intercept $(0, 2)$, use the slope $-\frac{2}{3}$. 

Remember that the slope is *rise over run*, meaning the numerator represents the rise (change in $y$) and the denominator represents the run (change in $x$). In other words, the **numerator** tells you how many units to **go up or down**, and the **denominator** tells you how many units to go **left or right**. Remember that if the **numerator is negative, you move down**; and if the **denominator is negative, you move to the left.**

In this case, the slope $\frac{-2}{3}$ means that for every **3 units you move right**, you move **2 units down**.  
So from $(0, 2)$, move to the point $(3, -1)$.

<p align="center">
  <img src="{{ site.baseurl }}/images/Graph_Linear_Equations/line_3.png" alt="Gradient" width="700">
</p>

**Step 5.** Draw the line

Connect the two points and extend the line in both directions.  
Label the line with its equation.

<p align="center">
  <img src="{{ site.baseurl }}/images/Graph_Linear_Equations/line_1.png" alt="Line Graph Example" width="700">
</p>

---

## Parallel and Perpendicular Lines

1. **Parallel Lines:**  
   Two lines are parallel if they have the **same slope** but **different y-intercepts**.

   $$
   y = \underbrace{\frac{-3}{2}}_{gradient}x + 2 \quad \text{and} \quad y = \underbrace{\frac{-3}{2}}_{gradient}x + 4
   $$

   <p align="center">
       <img src="{{ site.baseurl }}/images/Graph_Linear_Equations/parallels.png" alt="Parallel Lines" width="700">
   </p>

   In this case, both lines have a slope of $\frac{-3}{2}$ but different y-intercepts ($2$ and $4$), so they will never intersect.

2. **Perpendicular Lines:**  
   Two lines are perpendicular if their slopes are **negative reciprocals** of each other. That means if one line has a **slope of $m$**, the other line must have a **slope of $-\frac{1}{m}$**, or if the slope is a **fraction $\frac{a}{b}$**, the other line's **slope is $-\frac{b}{a}$**. 
   
   > We can think of this as switching the numerator and denominator and changing the sign. Being perpendicular means the lines intersect at a right angle (90 degrees).

   $$
   y = \underbrace{\frac{-3}{2}}_{gradient}x + 2 \quad \text{and} \quad y = \underbrace{\frac{2}{3}}_{gradient}x + 1 
   $$

   <p align="center">
       <img src="{{ site.baseurl }}/images/Graph_Linear_Equations/perpendiculars.png" alt="Perpendicular Lines" width="700">
   </p>

   Observe that the slopes $\frac{-3}{2}$ and $\frac{2}{3}$ are negative reciprocals, so the lines will intersect at a right angle.


--- 
## Vertical and Horizontal Lines
Up to this point, we have learned how to graph an equation of the form

$$ax+by=c,$$

which represents a slanted line as long as **both variables** $x$ and $y$ appear in the equation.

However, there are two special cases of linear equations: **vertical lines** and **horizontal lines**. These are also linear equations, but they are very easy to recognize, especially because **each one contains only one variable.**

1. **Vertical lines**

    A vertical line has the form

    $$
    x = k
    $$

    where $k$ is a constant.

    * This equation contains only the variable $x$.
    * The value of $x$ never changes, so the line goes straight up and down.
    * The constant $k$ tells us where the line crosses the **x-axis**.
    
    * A vertical line has **no slope** because calculating the slope would require dividing by zero.

    <p align="center">
       <img src="{{ site.baseurl }}/images/Graph_Linear_Equations/vertical.png" alt="Vertical Line" width="700">
    </p>

2. **Horizontal lines**

    A horizontal line has the form

    $$y=k,$$

    where $k$ is a constant.

    * This equation contains only the variable $y$.
    * The value of $y$ stays fixed, so the line extends left and right.
    * The constant $k$ tells us where the line crosses the **y-axis**.
    * The **slope** of a horizontal line is **$0$**, since there is no vertical change.

    <p align="center">
       <img src="{{ site.baseurl }}/images/Graph_Linear_Equations/horizontal.png" alt="Horizontal Line" width="700">
    </p>

  **These two special forms help us immediately recognize a completely vertical or completely horizontal line, simply by noticing that the equation uses only one variable and that the constant shows where the line intersects its corresponding axis.**