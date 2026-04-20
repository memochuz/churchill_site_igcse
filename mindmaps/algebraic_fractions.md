---
title: "Algebraic Fractions"
markmap:
  theme: default
  colorFreezeLevel: 2
  maxWidth: 400
  initialExpandLevel: 2
---

#  Algebraic Fractions

## Definition
* **Concept**: A fraction where the numerator and/or denominator are algebraic expressions (usually polynomials).
* **Examples**: $\frac{3x}{2y}$, $\frac{x^2+1}{x-3}$, $\frac{yx^3}{x^4y}$.

## Addition and Subtraction Methods

### **Method 1:** Cross Multiplication (Quick Way) 
*  Solve: $\frac{yx^3}{x^4y} + \frac{xy}{x^3y}$
* **Step 1:** Multiply Denominators
    $(x^4y)(x^3y)$.
* **Step 2:** Cross Multiply Numerators
    * Multiply numerator 1 by denominator 2 and vice versa.
    $ (yx^3)(x^3y)$ and $(xy)(x^4y)$.
* **Step 3:** Add Numerators
    * Combine the results over the new denominator.
    $\frac{(yx^3)(x^3y) + (xy)(x^4y)}{(x^4y)(x^3y)} = \frac{y^2x^6 + x^5y^2}{x^7y^2}$
* **Step 4:** Simplify
    * Factor out common terms and cancel.
    $\frac{y^2x^6 + x^5y^2}{x^7y^2} = \frac{y^2x^5(x + 1)}{x^7y^2} = \frac{x + 1}{x^2}$

### **Method 2:** Least Common Denominator 
*  Solve: $\frac{yx^3}{x^4y} + \frac{xy}{x^3y}$
* **Step 1:** Identify Denominators.
    * Denominator 1: $x^4y$
    * Denominator 2: $x^3y$
* **Step 2:** Find Least Common Multiple (LCM)
    * Find the LCM for each variable.
    * LCM of $x^4y$ and $x^3y$ is $x^4y$.
* **Step 3: Rewrite Fractions**
    * Adjust each fraction to have the LCD as its denominator.
    $\frac{yx^3}{x^4y} + \frac{xy}{x^3y} = \frac{yx^3}{x^4y} + \frac{xy \cdot x}{x^3y \cdot x} = \frac{yx^3}{x^4y} + \frac{x^2y}{x^4y}$
* **Step 4: Add and Simplify**
    * Add the numerators and simplify the resulting expression.
      $\frac{yx^3}{x^4y} + \frac{x^2y}{x^4y} = \frac{yx^3 + x^2y}{x^4y} = \frac{y(x^3 + x^2)}{x^4y} = \frac{x^2(x + 1)}{x^4} = \frac{x + 1}{x^2}$
## Simplification Process
* **Factoring**: Break down polynomials into their simplest factors (factorize).
* **Canceling**: Remove common terms found in both numerator and denominator.
* **Goal**: Express results with clarity and precision for problem-solving.
* **Example**: Simplify $\frac{y^2x^6 + x^5y^2}{x^7y^2}$
    * Factor out common terms: $\frac{y^2x^5(x + 1)}{x^7y^2}$
    * Cancel common factors: $\frac{x + 1}{x^2}$