---
title: "Significant Figures"
markmap:
  theme: default
  colorFreezeLevel: 2
  maxWidth: 350
  initialExpandLevel: 2
---

# Significant Figures

## Definition & Importance
* **Concept**: Represent the **precision** and reliability of a measurement.
* **Function**: Indicate how carefully a value was measured.
* **Comparison**: $3.2$ (2 sig figs) is less precise than $3.200$ (4 sig figs).

## Counting Rules
### The Sandwich Rule
* Zeros between the first and last non-zero digits **always count**.
* **Examples**: $1002$ (4 sig figs), $10.03$ (4 sig figs).
### Leading Zeros
* Zeros at the beginning **NEVER count**, they are just placeholders.
* **Examples**: $0.00908$ (3 sig figs), $0.0045$ (2 sig figs).
### Trailing Zeros
* **In Decimals**: Zeros at the end **ARE significant** (they show measured precision).
    * **Examples**: $4.20$ (3 sig figs), $12.00$ (4 sig figs).
* **In Integers**: **Ambiguous case**.
    * Usually assume only non-zero digits count unless context or scientific notation is provided.
    * Example: $2300$ (usually 2 sig figs).

## Scientific Notation
* **Purpose**: Best practice to avoid ambiguity with trailing zeros in integers.
* **Logic**: The number of digits in the coefficient represents the number of sig figs.
* **Example**: $2.30 \times 10^{3}$ (3 sig figs).

## Rules in Calculations
### Addition & Subtraction
* Round the result to the **least number of decimal places**.
* **Example**: $2.34 + 1.2 = 3.5$.
### Multiplication & Division
* Round the result to the **least number of significant figures**.
* **Example**: $2.3 \times 4.56 = 10$ (2 sig figs).