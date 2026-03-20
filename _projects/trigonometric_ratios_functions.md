---
title: 📝 Trigonometric Ratios and Functions
date: 2026-03-19
description: |
    <p>
    In this lesson, students are introduced to trigonometric ratios in right-angled triangles and how these ratios extend to trigonometric functions. Students learn how sine, cosine, and tangent compare the sides of a triangle, why these ratios depend only on the angle, and how they connect to the unit circle. The lesson also explores key angle values, graphs of trigonometric functions, and their main properties such as range, period, and asymptotes.
    </p>
    <hr>
    <h1>Class Objectives</h1>
    <ul>
      <li><b>Understand</b> trigonometric ratios as relationships between triangle sides.</li>
    <li><b>Identify</b> opposite, adjacent, and hypotenuse using a reference angle.</li>
    <li><b>Apply</b> SOH CAH TOA to calculate ratios.</li>
    <li><b>Use</b> trigonometric ratios to find missing sides and angles in right triangles.</li>
    <li><b>Memorize</b> exact values for 30°, 45°, and 60°.</li>
    <li><b>Explore</b> the unit circle and its connection to trig functions.</li>
    <li><b>Describe</b> graphs of sine, cosine, and tangent functions.</li>
    <li><b>Determine</b> amplitude and period from trigonometric functions.</li>
    </ul>

categories: [IGCSE, Trigonometry]
image: '/images/Trigonometry/portada_trig.png'
---

## What are Trigonometric Ratios?

Trigonometric ratios **compare the sides of a right-angled triangle**. We do this by **dividing one side by another**, these ratios tell us how the **lengths of sides relate to an angle**.

---

## Identifying the Sides

To use trigonometry, we choose a **reference angle** (NOT the $90^{\circ}$ angle).

With respect to that angle:

- **Opposite (O)** → side across from the angle  
- **Adjacent (A)** → side next to the angle  
- **Hypotenuse (H)** → longest side (opposite $90^{\circ}$)

<p align="center">
   <img src="{{ site.baseurl }}/images/Trigonometry/sides.png" width="600">
</p>

---

## The Three Main Ratios

The three trigonometric ratios are:

$$
\sin(\theta) = \frac{\text{Opposite}}{\text{Hypotenuse}}
$$

$$
\cos(\theta) = \frac{\text{Adjacent}}{\text{Hypotenuse}}
$$

$$
\tan(\theta) = \frac{\text{Opposite}}{\text{Adjacent}}
$$



#### Memory Trick: SOH CAH TOA

- **SOH** → Sine = Opposite / Hypotenuse  
- **CAH** → Cosine = Adjacent / Hypotenuse  
- **TOA** → Tangent = Opposite / Adjacent  

---

## Why Do Ratios Depend Only on the Angle?

If two right triangles have the **same angle**, they are **similar triangles**.

That means:
- Their shapes are the same  
- Their sides are **proportional**  

So the ratios:

$$
\frac{\text{Opposite}}{\text{Hypotenuse}}, \quad \frac{\text{Adjacent}}{\text{Hypotenuse}}, \quad \frac{\text{Opposite}}{\text{Adjacent}}
$$

**do not change**.

<p align="center">
   <img src="{{ site.baseurl }}/images/Trigonometry/proportional.png" width="600">
</p>


> This is why we define trigonometric ratios **as functions of the angle**.


---

## The Unit Circle

The **unit circle** is a circle with:

* Center at $(0,0)$
* Radius = $1$

If we draw a right-angled triangle inside the circle with angle $\theta$:

* The **hypotenuse = 1**

If we calculate $\sin(\theta)$ and $\cos(\theta)$, we get:

$$
\sin(\theta) = \frac{\text{opposite}}{\text{hypotenuse}} = \frac{\text{opposite}}{1} = \text{opposite}
$$

and

$$
\cos(\theta) = \frac{\text{adjacent}}{\text{hypotenuse}} = \frac{\text{adjacent}}{1} = \text{adjacent}
$$

<p align="center">
   <img src="{{ site.baseurl }}/images/Trigonometry/unitcircle.png" width="600">
</p>

Therefore:

* $\cos(\theta)$ = length of the red segment
* $\sin(\theta)$ = length of the purple segment

If we do the same for another angle $\phi$, we can again form a right-angled triangle. The horizontal and vertical values correspond to the cosine and sine of that angle.

<p align="center">
   <img src="{{ site.baseurl }}/images/Trigonometry/unitcircle3.png" width="600">
</p>

If we do not have a calculator but we do have a ruler, we can measure the sides of these triangles to approximate the sine and cosine of an angle.

To calculate the tangent, we can draw a tangent line that passes through the point $(0,1)$. Using the angle $\theta$, we form a new right-angled triangle. In this case, the triangle is not completely inside the circle.

<p align="center">
   <img src="{{ site.baseurl }}/images/Trigonometry/unitcircle2.png" width="600">
</p>

If we calculate the tangent of $\theta$, we get:

$$
\tan(\theta) = \frac{\text{opposite}}{\text{adjacent}} = \frac{\text{opposite}}{1} = \text{opposite}
$$

Therefore:

* $\tan(\theta)$ = length of the green segment

We can use any angle to calculate these ratios. We can always construct these types of triangles; the only difference is that the side lengths may sometimes be negative (depending on their position on the $x$- or $y$-axis). This is why the sine, cosine, and tangent functions can take both positive and negative values.


#### Exact Values Table

These are the key angles you must memorize:

|        | $30^\circ$ | $45^\circ$ | $60^\circ$ |
|--------|------------|------------|------------|
| $\sin$ | $\frac{1}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{3}}{2}$ |
| $\cos$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ |
| $\tan$ | $\frac{\sqrt{3}}{3}$ | $1$ | $\sqrt{3}$ |

---

## Trigonometric Functions

Now we extend ratios into **functions**:

- $\sin(x)$
- $\cos(x)$
- $\tan(x)$

These functions take an **angle** as **input** and produce a **numerical value** as **output**.

Using the **unit circle**, as we continuously change the angle, the corresponding sides of the right triangle also change. Since the sine, cosine, and tangent depend on these side lengths, their values vary with the angle. This variation is what defines them as functions.

If we plot the angle on the horizontal axis and the corresponding side length on the vertical axis, we obtain the graphs of the trigonometric functions. Here is a video that shows how these graphs are generated. 


<div style="display: flex; justify-content: center; gap: 30px; flex-wrap: wrap; text-align: center;">

  <div>
    <a href="https://www.youtube.com/shorts/PKdHoKX8AW0" target="_blank">
      <img src="https://img.youtube.com/vi/PKdHoKX8AW0/hqdefault.jpg" width="350">
    </a>
    <p style="margin: 8px 0 0 0; font-size: 14px;">
      Click to watch
    </p>
  </div>

  <div>
    <a href="https://www.youtube.com/shorts/MzWlINUj1R4" target="_blank">
      <img src="https://img.youtube.com/vi/MzWlINUj1R4/hqdefault.jpg" width="350">
    </a>
    <p style="margin: 8px 0 0 0; font-size: 14px;">
      Click to watch
    </p>
  </div>

</div>
---

## Graph of Sine and Cosine

#### Key Properties

- Range: from $-1$ to $1$
- Period: $360^{\circ}$
- Smooth wave pattern

<p align="center">
   <img src="{{ site.baseurl }}/images/Trigonometry/sine_cosine_functions.png" width="700">
</p>

#### Important Points

Every $90^{\circ}$, something important happens:

| Angle | $\sin$ | $\cos$ |
|------|--------|--------|
| $0^\circ$ | $0$ | $1$ |
| $90^\circ$ | $1$ | $0$ |
| $180^\circ$ | $0$ | $-1$ |
| $270^\circ$ | $-1$ | $0$ |
| $360^\circ$ | $0$ | $1$ |

They **repeat every $360^{\circ}$**

---

## Graph of Tangent

Tangent behaves differently.

#### Key Properties

- Range: all real numbers  
- Period: $180^{\circ}$*  
- Has **vertical asymptotes**

<p align="center">
   <img src="{{ site.baseurl }}/images/Trigonometry/tangent_function.png" width="700">
</p>

### Asymptotes

Tangent is undefined when:

$$
Opposite = 0
$$

This happens at:

$$
90^\circ,\; 270^\circ,\; 450^\circ,\; \dots
$$

These are **vertical asymptotes**.


---

## Applications of Trigonometric Ratios

Trigonometric ratios are useful because they allow us to find **missing sides** or **missing angles** in right-angled triangles.

#### Finding a Missing Side

Suppose we have a right triangle with:

* Angle $\theta = 30^\circ$
* Hypotenuse = $10$

<p align="center">
   <img src="{{ site.baseurl }}/images/Trigonometry/missingside.png" width="500">
</p>

We want to find the **opposite side**.

Using **SOH**:

$$
\sin(30^\circ) = \frac{\text{opposite}}{10}.
$$

Therefore,

$$
\frac{1}{2} = \frac{\text{opposite}}{10}
\quad \Rightarrow \quad
\text{opposite} = 5
$$

#### Finding a Missing Angle

Suppose we know:

* Opposite = $4$
* Adjacent = $3$

<p align="center">
   <img src="{{ site.baseurl }}/images/Trigonometry/missingangle.png" width="500">
</p>

We want to find the angle $\theta$.

Using **TOA**:

$$
\tan(\theta) = \frac{4}{3}
$$

To **isolate the angle**, we use the **inverse function**:

$$
\theta = \tan^{-1}\left(\frac{4}{3}\right).
$$

Therefore, 

$$
\theta \approx 53.13^\circ
$$



#### Key Idea

* To find a **side** → use $\sin$, $\cos$, or $\tan$
* To find an **angle** → use **inverse functions**:
  * $\sin^{-1}(x)$
  * $\cos^{-1}(x)$
  * $\tan^{-1}(x)$

---

## Amplitude and Period

When we graph trigonometric functions, two key features help us understand their behavior:

#### Amplitude

The **amplitude** measures how far the graph moves **up and down** from its center (midline).


<p align="center">
   <img src="{{ site.baseurl }}/images/Trigonometry/amplitude.png" width="500">
</p>

For functions of the form:

$$
y = a\sin(x) \quad \text{or} \quad y = a\cos(x)
$$

the amplitude is defined as: 

$$amplitude = |a|$$

**Example:**

* $y = 3\sin(x)$ → amplitude = $3$
* $y = -2\cos(x)$ → amplitude = $2$

The negative sign reflects the graph, but does not change the amplitude.


#### Period

The **period** is the length of one full cycle of the function (how long it takes to repeat).

<p align="center">
   <img src="{{ site.baseurl }}/images/Trigonometry/period.png" width="500">
</p>


For functions of the form:

$$
y = \sin(bx), \quad y = \cos(bx), \quad y = \tan(bx)
$$

* **Period of $\sin$ and $\cos$:**

  $$
  \frac{360^\circ}{|b|}
  $$

* **Period of $\tan$:**

  $$
  \frac{180^\circ}{|b|}
  $$

**Examples:**

* $y = \sin(2x)$ → period = $180^\circ$
* $y = \cos\left(\frac{1}{2}x\right)$ → period = $720^\circ$
* $y = \tan(3x)$ → period = $60^\circ$

#### Key Ideas

* **Amplitude** controls the vertical stretch
* **Period** controls how “compressed” or “stretched” the graph is horizontally

---

## Summary

* Trigonometric ratios compare triangle sides
* Defined using a reference angle
* **SOH CAH TOA** helps remember formulas
* Ratios depend only on the angle (similar triangles)
* Unit circle connects trig to coordinates
* **Applications:**
  * Used to find missing sides in right triangles
  * Used to find missing angles using inverse functions
  * Inverse functions ($\sin^{-1}, \cos^{-1}, \tan^{-1}$) are used to isolate angles
* **Amplitude:**
  * Measures vertical stretch
  * For $\sin$ and $\cos$: absolute value of $a$ in $y = a\sin(x)$ or $y = a\cos(x)$
* **Period:**
  * Length of one full cycle
  * $\sin$ and $\cos$: $\frac{360^\circ}{b}$
  * $\tan$: $\frac{180^\circ}{b}$
* $\sin$ and $\cos$:
  * Range: $[-1, 1]$
  * Period: $360^{\circ}$
* $\tan$:
  * Period: $180^{\circ}$
  * Has asymptotes
* Key values $(30^{\circ}, 45^{\circ}, 60^{\circ})$ must be memorized