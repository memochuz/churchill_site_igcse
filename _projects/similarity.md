---
title: 📝 Similarity
date: 2025-11-18
description: |
    <p>The topic of similarity introduces students to proportional reasoning within geometric figures, focusing on how shapes can maintain the same form while varying in size. When two shapes are similar, their corresponding angles are equal and their corresponding sides are in the same ratio. Understanding similarity helps students recognize scale factors, compare geometric figures, and solve problems involving enlargement, reduction, and indirect measurement. Through similarity, learners connect geometric properties with practical applications such as maps, models, architectural drawings, and real-life scaling situations.</p>
    <hr>
    <h1>Class Objectives</h1>
    <ul>
      <li><b>Understand</b> that similar shapes have equal corresponding angles and proportional corresponding sides.</li>
      <li><b>Identify</b> similarity in figures using angles reasoning and side ratio comparisons.</li>
      <li><b>Use</b> scale factors to calculate missing side lengths and interpret enlargements or reductions.</li>
      <li><b>Apply</b> similarity to real-world contexts including maps, scale drawings, shadows, areas, volumes and modelling problems.</li>
    </ul>

categories: [Bimester-2, Geometry]
image: '/images/Similarity/similarity.png'
---

## What Is Similarity?

The definition of **similarity** in geometry states that two shapes are similar if: 

> Two shapes have the same shape but different sizes. Their corresponding angles are equal, and their corresponding sides are in the same ratio.

For example consider the following figure:

<p align="center">
   <img src="{{ site.baseurl }}/images/Similarity/cubes.png" alt="Similar Cubes" width="700">
</p>

The shapes shown are cubes. Since all their faces meet at right angles, their corresponding angles are equal. Additionally, the ratio of corresponding side lengths is the same for every pair of sides:

$$
\frac{8}{2}=4
$$

Because the side-length ratio is constant and the angles match, we can conclude that the two cubes are similar shapes. In other words, one is simply an enlarged or reduced version of the other.

The ratio between **corresponding sides** (which is always the same for similar shapes) is called the scale factor. To avoid mistakes, we will always compute it using:

$$
\text{Scale Factor} = \frac{\text{larger side}}{\text{smaller side}}
$$

In our example, the scale factor is:

$$
\text{Scale Factor} = \frac{8}{2} = 4
$$

This means the larger cube is an enlargement of the smaller one by a factor of $4$, meaning every side has been multiplied by $4$.

## What happens with Areas and Volumes?

When two shapes are similar, their areas and volumes are also related by the scale factor but in a different way. In the previous example, the scale factor between the two cubes is $4$. What about their areas and volumes? 

$$
\frac{\text{Larger Area}}{\text{Smaller Area}} = \frac{64}{4} = 16 = 4^{2}= \text{(Scale Factor)}^{2}
$$

and 

$$
\frac{\text{Larger Volume}}{\text{Smaller Volume}} = \frac{512}{8} = 64 = 4^{3}= \text{(Scale Factor)}^{3}
$$

This means that: 
- The ratio of their areas is equal to the square of the scale factor. 

    $$\text{(Scale Factor)}^{2} = \frac{\text{Larger Area}}{\text{Smaller Area}}$$
- The ratio of their volumes is equal to the cube of the scale factor.

    $$\text{(Scale Factor)}^{3} = \frac{\text{Larger Volume}}{\text{Smaller Volume}}$$

## Example

Consider two similar drinking glasses. We know the following information:

<p align="center">
   <img src="{{ site.baseurl }}/images/Similarity/glasses.png" alt="Similar Glasses" width="700">
</p>

- The **volume of the smaller glass** is $5 \text{ mm}^3$.
- The **volume of the larger glass** is $625 \text{ mm}^3$.
- The **radius of the base of the larger glass** is $10 \text{ mm}$.

Let's find the radius of the base of the smaller glass.

Since we have the volumes of both glasses, we can use the relationship between the volumes and the scale factor:

$$
\text{Scale Factor}^{3} = \frac{\text{larger volume}}{\text{smaller volume}} \longrightarrow \text{Scale Factor} = \sqrt[3]{\frac{\text{larger volume}}{\text{smaller volume}}}
$$

Substituting the given values:

$$
\text{Scale Factor} = \sqrt[3]{\frac{625}{5}} =  \sqrt[3]{125} = 5
$$

Now we find the radius of the smaller glass:

$$
\text{Scale Factor} = \frac{r_{\text{large}}}{r_{\text{small}}} \longrightarrow r_{\text{small}} = \frac{r_{\text{large}}}{\text{Scale Factor}}
$$

Therefore, the radius of the smaller glass is:

$$
r_{\text{small}} = \frac{10}{5}= 2 \text{ mm}
$$

This gives the corresponding radius using the scale factor for similar solids.
