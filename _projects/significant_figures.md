---
title: Significant Figures 
date: 2026-03-26
description: |
    <p>
    In this lesson, students learn how to identify and use significant figures 
    to represent the precision of measurements. Significant figures are essential 
    in science and mathematics to communicate how reliable a value is and to 
    avoid overestimating accuracy in calculations.
    </p>
    <hr>
    <h1>Class Objectives</h1>
    <ul>
      <li><b>Understand</b> what significant figures represent.</li>
      <li><b>Identify</b> significant figures in different types of numbers.</li>
      <li><b>Distinguish</b> between significant and non-significant zeros.</li>
      <li><b>Apply</b> rules of significant figures in calculations.</li>
      <li><b>Round</b> numbers correctly to a given number of significant figures.</li>
    </ul>

categories: [IGCSE, Number]
image: '/images/Numbers/sig_figs_portada.png'
---

## What Are Significant Figures?

Significant figures (or **sig figs**) represent the **precision** of a number.

They tell us:
* How carefully a measurement was taken  
* How reliable the digits are  

For example:
* $3.2$ → measured to 2 significant figures (we are not sure about the values of the following digits) 
* $3.200$ → measured to 4 significant figures (we know the next two decimal places are exactly zero, so the measurement is more precise)

---

## Rules of Significant Figures

These rules help us determine **which digits count**.


### The "Sandwich Rule"

Every digit between the **first non-zero** and the **last non-zero** counts.

**Example:**


* $1002$ → 4 significant figures
* $10.03$ → 4 significant figures



Zeros are **trapped**, so they **count**.



####  Leading Zeros (Placeholders)

Zeros at the **beginning** NEVER count.

Most of the time they only show the position of the decimal point.

**Example:**

* $0.00908$ → 3 significant figures
* $0098$ → 2 significant figures



#### Trailing Zeros in Decimals

Zeros at the **end of a decimal ARE significant**. That zero is there because it was exactly measured to that spot, not just rounded. **Unless specified otherwise**, always assume they are significant.

**Examples:**

* $4.20$ → 3 significant figures
* $12.00$ → 4 significant figures


### Trailing Zeros in Integers (Ambiguous Case)

For whole numbers, zeros at the end **may or may not count**, it depends on the rounding context.

**Example:**

* $2300$ → could be 2, 3, or 4 significant figures

    - If the problem does not give any context, we usually assume it has 2 significant figures (only the non-zero digits are clearly significant).
    - If the problem states it is an exact measurement, then it can have 4 significant figures.
    - If the problem says it has been rounded, then:
        - 2300 (to 3 sig figs) → the third digit is known, so 3 significant figures
        - 2300 (to 2 sig figs) → only 2 significant figures



Depends on:
* Measurement precision  
* Context  
* Scientific notation (preferred to clarify)



#### Scientific Notation (Best Practice)

To avoid ambiguity with integers containing trailing zeros, we use scientific notation. 

* $2.3 \times 10^{3}$ → 2 sig figs
* $2.30 \times 10^{3}$ → 3 sig figs
* $2.300 \times 10^{3}$ → 4 sig figs

The number of digits in the coefficient (the number in front) represents the number of significant figures.

---

## Significant Figures in Calculations

#### Addition & Subtraction

Round to the **least number of decimal places**.

**Example:**

$2.34 + 1.2 = 3.54 \rightarrow 3.5 \quad (\text{2 sig figs})$ 

#### Multiplication & Division

Round to the **least number of significant figures**.

**Example:**
$2.3 × 4.56 = 10.488 \rightarrow 10 \quad (\text{2 sig figs})$


---

## Common Mistakes

- Counting leading zeros  
- Forgetting trailing decimal zeros count   
- Not rounding at the final step  

---

## Example

| Number | Sig Figs | Why?                                                                         |
| ------ | -------- | ---------------------------------------------------------------------------- |
| 45.7   | 3        | All digits are non-zero, so they all count.                                  |
| 1005   | 4        | Zeros are between non-zero digits (“sandwiched”), so they count.             |
| 0.0045 | 2        | Leading zeros are placeholders and do not count.                             |
| 6.00   | 3        | Trailing zeros after a decimal point indicate precision.                     |
| 2300   | 2        | Trailing zeros in integers are ambiguous; assume only non-zero digits count. |
| 0.0908 | 3        | Leading zeros do not count, but the zero between 9 and 8 does.               |
| 12.030 | 5        | All digits count: trapped zero and trailing decimal zero show precision.     |

