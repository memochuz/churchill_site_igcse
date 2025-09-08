---
title: 📝 Algebraic Fractions
description: |
    <p>The topic of algebraic fractions focuses on expressions where both the numerator and denominator are polynomials. Students will learn how to simplify these fractions by factoring, canceling common terms, and applying the rules of operations with fractions. By mastering these techniques, students will be able to manipulate algebraic fractions confidently and use them as building blocks in more advanced algebraic processes.</p>
    <hr>
    <h1>Class Objectives</h1>
    <ul>
      <li><b>Understand</b> the definition of algebraic fractions.</li>
      <li><b>Simplify</b> algebraic fractions by factoring and canceling common factors.</li>
      <li><b>Perform</b> addition, subtraction, multiplication, and division of algebraic fractions.</li>
      <li><b>Develop</b> clarity and precision in expressing simplified results for effective problem solving.</li>
    </ul>


date: 2025-08-22
categories: [Bimester-1, Algebra]
image: '/images/Algebraic_Fractions/algebraic_fractions.png'
page_cover:
---

# What are Algebraic Fractions?  

An **algebraic fraction** is a fraction where the numerator and/or denominator are algebraic expressions (usually polynomials).  

For example:  

$$
\frac{3x}{2y}, \quad \frac{x^2+1}{x-3}, \quad \frac{yx^3}{x^4y}
$$

The rules for adding, subtracting, multiplying, and dividing algebraic fractions are the same as those for numerical fractions. The easiest way to work with the addition or subtraction of algebraic fractions is to apply the following diagram, which is Method 1 that we will use in this class. 

<p align="center">
  <img src="{{ site.baseurl }}/images/Algebraic_Fractions/algebraic_fractions_2.png" alt="Algebraic Fractions" width="170px">
</p>


---

# Example: Adding Algebraic Fractions  

We want to add:  

$$
\frac{yx^3}{x^4y} + \frac{xy}{x^3y}
$$

---

## Method 1: Cross Multiplication (Quick Way)

<p align="center">
  <img src="{{ site.baseurl }}/images/Algebraic_Fractions/example.png" alt="Algebraic Fractions" width="150px">
</p>

### Step 1. Multiply denominators

$$
\color{#FBB56A}{(x^4y)(x^3y)} = \color{#FBB56A}{x^7y^2}
$$

### Step 2. Cross multiply numerators

- First numerator:  

  $$
  \color{#50FA7B}{yx^3 \cdot (x^3y)} =\color{#50FA7B}{x^6y^2}
  $$

- Second numerator:  

  $$
  \color{#BD93F9}{xy \cdot (x^4y)} = \color{#BD93F9}{x^5y^2}
  $$

### Step 3. Add numerators

$$
\frac{\color{#50FA7B}{x^6y^2} + \color{#BD93F9}{x^5y^2}}{\color{#FBB56A}{x^7y^2}}
$$

### Step 4. Simplify

$$
\frac{x^5y^2(x+1)}{x^7y^2} = \frac{x+1}{x^2}
$$


---

## Method 2: Least Common Denominator (Formal Way)

### Step 1. Identify denominators

- First denominator: $x^4y$  
- Second denominator: $x^3y$  

### Step 2. Find the Least Common Multiple (LCM)  

- LCM of $x^4$ and $x^3$ is $x^4$.  
- LCM of $y$ and $y$ is $y$.  

So the LCD is:  

$$
x^4y
$$

### Step 3. Rewrite fractions with the LCD

- First fraction stays the same:  
  $$
  \frac{yx^3}{x^4y}
  $$  

- Second fraction: multiply top and bottom by $x$:  
  $$
  \frac{xy}{x^3y} \cdot \frac{x}{x} = \frac{x^2y}{x^4y}
  $$

### Step 4. Add numerators

$$
\frac{yx^3 + x^2y}{x^4y}
$$

### Step 5. Simplify

$$
\frac{y(x^3 + x^2)}{x^4y} = \frac{x^2(x+1)}{x^4} = \frac{x+1}{x^2}
$$

---

## ✅ Final Answer  

Both methods give the same result:  

$$
\frac{x+1}{x^2}
$$
