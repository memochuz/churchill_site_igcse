---
title: Statistics Basics
date: 2026-04-02
description: |
    <p>
    In this lesson, students learn how to summarize and interpret data using key statistical measures. These include averages, spread, and quartiles, which help us understand the distribution of data.
    </p>
    <hr>
    <h1>Class Objectives</h1>
    <ul>
      <li><b>Understand</b> measures of central tendency (mean, median, mode).</li>
      <li><b>Calculate</b> median for even and odd data sets.</li>
      <li><b>Interpret</b> mode and its variations.</li>
      <li><b>Compute</b> range and quartiles.</li>
      <li><b>Understand</b> interquartile range (IQR).</li>
    </ul>

categories: [IGCSE, Statistics]
image: '/images/Statistics/statistics_portada.png'
---

## Mean (Average)

The **mean** is the sum of all values divided by the number of values.

$$
\text{Mean} = \frac{\text{Sum of values}}{\text{Number of values}}
$$

#### Example

| Values | $x_1$ | $x_2$ | $x_3$ | $x_4$ |
|------|---|---|---|---|
| | 2 | 4 | 6  |8 |

$$
\text{Mean} = \frac{2+4+6+8}{4} = \frac{20}{4} = 5
$$

---

## Median

The **median** is the middle value when the data is **arranged in order.**


#### Case 1: Odd Number of Values

| Values | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $x_5$ |
|------|---|---|---|---|---|
|  | 1 | 3 | 5 | 7 | 9 |

Middle value:

$$
\text{Median} = 5
$$

In case we have a large amount of data, we can find the position of the median using:

$$
\text{Position} = \frac{n+1}{2}
$$

where $n$ is the number of values. For example, if we have 9 values in increasing order: $x_1, x_2, \ldots, x_9$

$$
\text{Position} = \frac{9+1}{2} = 5
$$

So the median is the 5th value, which is $x_5$.



#### Case 2: Even Number of Values

| Values | $x_1$ | $x_2$ | $x_3$ | $x_4$  |
|------|---|---|---|---|
|  | 2 | 4 | 6 | 8 |

Middle values: 4 and 6

$$
\text{Median} = \frac{4+6}{2} = 5
$$

In case we have a large amount of data, we can find the positions of the two middle values using:

$$
\text{Positions} = \frac{n}{2} \quad \text{and} \quad \frac{n}{2} + 1
$$

where $n$ is the number of values. For example, if we have 10 values in increasing order: $x_1, x_2, \ldots, x_{10}$

$$
\text{Positions} = \frac{10}{2} = 5 \quad \text{and} \quad 6
$$

So the median is the average of the 5th and 6th values:

$$
\text{Median} = \frac{x_5 + x_6}{2}
$$

---

## Mode

The **mode** is the value that appears most frequently.

#### Example

| Values | $x_1$ | $x_2$ | $x_3$ | $x_4$  | $x_5$ |
|------|---|---|---|---|---|
|  | 1 | 2 | 2 | 3 | 4 |

Mode = 2



**Important**:

* There can be **more than one mode** (bimodal or multimodal)  
* If all values appear the same number of times, there is **no mode**  
* We do **not** say all values are the mode  

---

## Range

The **range** measures how spread out the data is.

$$
\text{Range} = \text{Maximum} - \text{Minimum}
$$

### Example

| Values | $x_1$ | $x_2$ | $x_3$ | $x_4$  |
|------|---|---|---|---|
|  | 3 | 7 | 8 | 10 |

$$
\text{Range} = 10 - 3 = 7
$$

---

## Quartiles

Quartiles divide the data into four equal parts.

* $Q_1$ → lower quartile (25%)  
* $Q_2$ → median (50%)  
* $Q_3$ → upper quartile (75%)  



#### How to Find Quartiles

1. Order the data  
2. Find the position using:

$$
\text{Position} = \text{percentage} \times \text{number of data}
$$


#### Important Rule

* If the position is an **integer**, take the **average of that value and the next one**  
* If the position is **decimal**, round **up** to the next whole number  


#### Example

Consider the following ordered data:

|Values| $x_1$ | $x_2$ | $x_3$ | $x_4$ | $x_5$ | $x_6$ | $x_7$ | $x_8$ | $x_9$ | $x_{10}$ |
|------|---|---|---|---|---|----|----|----|----|----|
|  | 1 | 3 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 |

$n = 10$



**Find $Q_1$:**

$$
0.25 \times 10 = 2.5
$$

Position is decimal → round up to position 3:

$$
Q_1 = x_3 = 4
$$


**Find Median $Q_2$:**

$$
0.5 \times 10 = 5
$$

Position is decimal → average of 5th and 6th values:

$$
Q_2 = \frac{x_5 + x_6}{2} = \frac{8 + 10}{2} = 9
$$


**Find $Q_3$:**

$$
0.75 \times 10 = 7.5
$$

Position is decimal → round up to position 8:

$$
Q_3 = x_8 = 14
$$

---

## Interquartile Range (IQR)

The **interquartile range (IQR)** measures the spread of the middle 50% of the data.

$$
\text{IQR} = Q_3 - Q_1
$$


#### What Does IQR Measure?

* It shows how spread out the **middle half** of the data is  
* It is less affected by extreme values (outliers)  
* It gives a better idea of the “typical spread”  

Using the previous example:

$$
\text{IQR} = 7.5 - 2.5 = 5
$$

---

## Common Mistakes

* Not ordering data before finding median or quartiles  
* Forgetting to average when needed  
* Rounding quartile positions incorrectly  
* Confusing mean, median, and mode  
* Using range instead of IQR when data has outliers  

