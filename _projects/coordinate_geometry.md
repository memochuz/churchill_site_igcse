---
title: 📝 Coordinate Geometry
date: 2025-09-25
description: |
    <p>This lesson introduces students to the fundamental forms and tools used in coordinate geometry. By understanding different ways to express the equation of a line, as well as how to calculate gradient, midpoint, and distance between two points, students develop strong analytical skills for solving geometric problems in the coordinate plane. These methods allow learners to interpret geometric information, verify whether points lie on a line, and apply coordinate techniques to real-world contexts such as navigation, engineering design, and data interpretation.</p>
    <hr>
    <h1>Class Objectives</h1>
    <ul>
      <li><b>Recognize</b> the different forms of linear equations: standard form, gradient–intercept form, point–slope form, and two–point form.</li>
      <li><b>Calculate</b> the gradient using $ \frac{y_2 - y_1}{x_2 - x_1} $ when two points are known.</li>
      <li><b>Find</b> the midpoint and distance between two points in the coordinate plane.</li>
      <li><b>Determine</b> whether a point lies on a given line by substituting its coordinates into the equation.</li>
    </ul>


categories: [Bimester-2, Geometry]
image: '/images/Coordinate_Geometry/cover.png'
---

## Coordinate Geometry – Forms of Linear Equations

We already know that equations of the form $y = mx + b$ represent straight lines. Now we will explore the different ways in which a line can be written.

Just as numbers can be represented in different forms but still represent the same value (for example: $2 = \frac{4}{2} = \frac{8}{4} = \dots$), in geometry a straight line can also be expressed in different but equivalent forms.

Below are the most common forms of linear equations:

---

### 1. **Standard Form**

A line can be written as:

$$ax + by = c$$

This is known as the **standard form** of a line. Observe that both variables are on one side of the equation and the constant term is on the other.

---

### 2. **Gradient-Intercept Form**

If we isolate $y$, we obtain:

$$y = mx + d$$

Where:

* $m$ is the **gradient (slope)**,
* $d$ is the **y-intercept**, the point where the line crosses the y-axis.

---

### 3. **Gradient-Point Form**

If we know a point that belongs to the line, $(x_0, y_0)$, and its gradient $m$, we can write:

$$y - y_0 = m(x - x_0)$$

This is useful when we have the slope and one point on the line.

---

### 4. **Two-Point Form**

If two points on the line are known, $(x_1, y_1)$ and $(x_2, y_2)$, the equation can be written as:

$$y - y_1 = \dfrac{y_2 - y_1}{x_2 - x_1}(x - x_1)$$

This formula comes from calculating the gradient using two points and then applying the point–slope form. It tells us how to calculate the gradient using two points.

$$m = \frac{y_{2}-y_{1}}{x_{2}-x_{1}}$$

---

Each of these forms represents the same geometric object: **a straight line**, but each form is useful in different situations **depending on the information we are given.**


## Formula of the gradient

To understand where the formula for the gradient comes from (the two-point form), it is important to look at the following idea:

We already know that the gradient (slope) is calculated as:

$$ \text{gradient} = \dfrac{\text{rise}}{\text{run}} $$

<p align="center">
   <img src="{{ site.baseurl }}/images/Coordinate_Geometry/gradient.png" alt="Gradient" width="700">
</p>

In this context, rise represents how much we move in the vertical $y$ direction, and run represents how much we move in the horizontal $x$ direction.

If we use two points that lie on the same line, we can always form a right triangle between them. In this right triangle:

* The vertical change (rise) is calculated as $y_2 - y_1$

* The horizontal change (run) is calculated as $x_2 - x_1$




Therefore, the gradient of the line is:

$$m = \dfrac{y_2 - y_1}{x_2 - x_1}$$

This gives us the standard formula for finding the gradient when two points on a line are known.

<p align="center">
   <img src="{{ site.baseurl }}/images/Coordinate_Geometry/two_point.png" alt="Two-Point Form" width="700">
</p>

## Midpoint

Since we are working with two points, we can also ask how to calculate the midpoint between them. If we connect both points, we form a line segment, and we may want to find the point that lies exactly in the middle of that segment.

Let’s look at the following idea:

When we project the coordinates of the midpoint onto the coordinate axes, we see that the midpoint lies halfway between the $x$-coordinates and halfway between the $y$-coordinates of the original points. From middle school mathematics, we know that the midpoint on the real number line is calculated by averaging the two values.

<p align="center">
   <img src="{{ site.baseurl }}/images/Coordinate_Geometry/midpoint.png" alt="Midpoint" width="700">
</p>

Therefore, for two points with coordinates $(x_1, y_1)$ and $(x_2, y_2)$, the midpoint is:

$$(\frac{x_{1}+x_{2}}{2}, \frac{y_{1}+y_{2}}{2})$$

This formula gives the coordinates of the point that lies halfway between the two original points on the segment.

## Distance

When connecting the two points and visualizing the right triangle formed, we notice that the distance between the points is simply the length of the hypotenuse. Therefore, using Pythagoras’ Theorem:

$$\text{distance}^2=(x_2−x_1)^2+(y_2−y_1)^2$$

So the distance between the two points is:

$$\text{distance} =\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

<p align="center">
   <img src="{{ site.baseurl }}/images/Coordinate_Geometry/distance.png" alt="Distance" width="700">
</p>

## Does a Point Belong to a Line?

Finally, if we have a point in the coordinate plane and the equation of a line, how can we check whether the point lies on that line?
The process is simple:

* Substitute the $x$ and $y$ coordinates of the point into the equation of the line.
* If the resulting equality is true, then the point belongs to the line.
* If the equality is false, then the point is not on the line.

### 1. Example

Line equation:

$$y=2x+1.$$

Point: 

$$P(2,5)$$

Substitute into the equation:
* Left-hand side: $y = 5$
* Right-hand side: $2(2) + 1 = 5$

Since both sides are equal:

$$5 = 5,$$

we can conclude the point $P$ lies on the line.

### 2. Example

Line equation:

$$3x-y=4.$$

Point: 

$$Q(1,5)$$

Substitute into the equation:
* Left-hand side: $3(1) - 5 = -2$
* Right-hand side: $4$

Since:

$$-2\neq 4,$$

we can conclude the point $Q$ does not belong to the line.

## Conclusion

We have learned that there are several ways to express the equation of a straight line, and each is useful depending on the information provided in the problem. If two points of a line are known, we can:


* Find the equation of the line that passes through them
* Compute the gradient (slope)
* Calculate the distance between the points
* Determine the midpoint of the segment connecting them

These tools allow us to work flexibly with line equations in coordinate geometry.