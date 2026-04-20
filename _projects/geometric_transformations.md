---
title: Transformations of Figures
date: 2026-04-20
description: |
    <p>
    In this lesson, students learn how to describe and perform geometric 
    transformations, including translations, rotations, reflections, and 
    enlargements. Emphasis is placed on identifying and describing transformations precisely.
    </p>
    <hr>
    <h1>Class Objectives</h1>
    <ul>
      <li><b>Understand</b> different types of transformations.</li>
      <li><b>Perform</b> transformations on the coordinate plane.</li>
      <li><b>Describe</b> transformations using correct notation.</li>
      <li><b>Find</b> centers, lines, and vectors from given images.</li>
    </ul>

categories: [IGCSE, Geometry]
image: '/images/Geometry/transformations.png'
---

## What is a Transformation?

A **transformation** is a way of moving or changing a figure in the plane.

> The shape may change position, size, or orientation.

---

## Types of Transformations

Thwe main types of transformations are:

1. Translation  
2. Rotation  
3. Reflection  
4. Enlargement (Homothety)  

---

## Translation

A **translation** moves a figure without rotating or resizing it.

#### Representation

A translation is described by a **vector**:

$$
\begin{pmatrix} a \\ b \end{pmatrix}
$$

In order to perform a translation, we most move every point of the figure by using the vector. We do this by adding the vector components to the coordinates of each point:

- $a$ units horizontally  
- $b$ units vertically  



#### Example

Translate triangle $ABC$ with vertices:

$$
A(1,2), \quad B(3,1), \quad C(2,4)
$$

by the vector:

$$
\begin{pmatrix} 4 \\ -1 \end{pmatrix}
$$

**Translate each point**, we add the vector components to the coordinates of each point:

Add the vector to each vertex:

* $A(1,2) \rightarrow A'(5,1)$
* $B(2,2) \rightarrow B'(6,1)$
* $C(2,4) \rightarrow C'(6,3)$

The translated triangle has vertices:

$$
A'(5,1), \quad B'(6,1), \quad C'(6,3)
$$

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/translations_1.png" width="700">
</p>


#### Finding the Translation Vector

In the case we are given the original and the image of a point, we can find the translation vector by subtracting the coordinates of the original point from the coordinates of the new point:

$$
\text{vector} = (\text{new point}) - (\text{original point})
$$


<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/translations_2.png" width="700">
</p>


---

##  Rotation

A **rotation** turns a figure around a fixed point.


#### How to Describe a Rotation

You must specify:

* Angle (e.g., $90^\circ$, $180^\circ$)  
* Direction (clockwise or anticlockwise)  
* Center of rotation  


#### How to Perform a Rotation

1. Identify the center  
2. Rotate each point around the center  
3. Keep distance from the center constant  



#### Example

Rotate the triangle $ABC$ with vertices:

$$
A(1,2), \quad B(3,1), \quad C(2,4)
$$

clockwise about the point $(3,2)$ by $90^\circ$

**Rotate each point** around the center:

1. Draw new axis on the center of rotation
2. To help visualize, we can draw auxiliary right triangles to find the new positions of the points after rotation.
3. Rotate each point by $90^\circ$ clockwise 

The rotated triangle has vertices:

$$
A'(5,1), \quad B'(6,1), \quad C'(6,3)
$$

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/rotation_1.png" width="700">
</p>


#### Finding the Center of Rotation

1. Join corresponding points (original and image)

2. The center is where the perpendicular bisectors meet (you must draw the perpendicular bisectors of the segments joining corresponding points) 



<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/rotation_2.png" width="700">
</p>


---

## 3. Reflection

A **reflection** flips a figure across a line.


#### How to Describe a Reflection

You must specify the **line of reflection**, for example:

* $x = 2$  
* $y = -1$  
* $y = x$ 


#### How to Perform a Reflection

**Each point:**
- stays the same distance from the line  
- appears on the opposite side  of the line

#### Example

Reflect the triangle $ABC$ with vertices:

$$
A(1,2), \quad B(3,1), \quad C(2,4)
$$

across the line $y = x$.

1. First we draw the line of reflection and then we reflect each point across the line,
2. measure the distance from each point to the line and then mark the reflected point at the same distance on the opposite side of the line.


<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/reflection_1.png" width="700">
</p>


#### Finding the Line of Reflection

The line is the **perpendicular bisector** of corresponding points.

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/reflection_2.png" width="700">
</p>

---

## 4. Enlargement (Homothety)

An **enlargement** changes the size of a figure with a scale factor. The sides of the image are multiplied by the scale factor $k$.


#### How to Describe an Enlargement

You must specify:

* Scale factor $k$  
* Center of enlargement  


#### How to Perform an Enlargement

1. Draw a line from the center through each point  
2. Multiply the distance between the center and each point by $k$
3. Mark the new point on the line at the new distance from the center.

#### Example

Enlarge the triangle $ABC$ with vertices:

$$
A(1,2), \quad B(3,1), \quad C(2,4)
$$


with center $(2,3)$ and scale factor $-2$:


1. Draw lines from the center to each point.
2. Measure the distance from the center to each point, multiply by $-2$ and mark the new points on the lines at the new distance from the center.
3. The negative scale factor means the image will be on the opposite side of the center compared to the original points. 

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/enlargement_1.png" width="700">
</p>

---

### Finding the Center of Enlargement

1. Join corresponding points  
1. The lines intersect at the **center**

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/enlargement_2.png" width="700">
</p>

---

## Summary of Descriptions

| Transformation | What must be given |
|---------------|------------------|
| Translation   | Vector |
| Rotation      | Angle + direction + center |
| Reflection    | Line (equation) |
| Enlargement   | Scale factor + center |

---

## Common Mistakes

* Forgetting to include the center  
* Missing direction in rotations  
* Confusing reflection lines  
* Incorrect scale factor in enlargements  
