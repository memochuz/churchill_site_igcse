---
title: Data Analysis and Representation
date: 2026-04-03
description: |
    <p>
    In this lesson, students learn how to organize, summarize, and represent data using different statistical tools. These include stem-and-leaf plots, frequency tables, grouped data, and graphical representations.
    </p>
    <hr>
    <h1>Class Objectives</h1>
    <ul>
      <li><b>Understand</b> stem-and-leaf diagrams.</li>
      <li><b>Use</b> frequency and relative frequency tables.</li>
      <li><b>Estimate</b> mean, median, and mode from grouped data.</li>
      <li><b>Interpret</b> graphs such as bar charts and box plots.</li>
      <li><b>Work with</b> cumulative frequency graphs.</li>
    </ul>

categories: [IGCSE, Statistics]
image: '/images/Statistics/statistics_data_portada.png'
---

## Stem-and-Leaf Plots

A **stem-and-leaf plot** is a way to organize and display numerical data. It allows us to see the distribution of the data while keeping the original values.

**How it works:**

* The stem represents the first digit(s) of each number.
* The leaf represents the last digit.
* Each data value is split into a stem and a leaf.

**Why we use stem-and-leaf plots**

* They show the shape of the data distribution
* They allow us to quickly find:
    * The smallest and largest values
    * The mode
    * The spread of the data

#### Steps to create a stem-and-leaf plot

* Order the data from smallest to largest
* Identify the stems (usually the tens)
* Write the stems in a vertical column
* Add the leaves (units) next to the correct stem
* Sort the leaves in ascending order

#### Example

Data:

$$
12, 14, 15, 18, 21, 23, 25, 27
$$

Stem-and-leaf plot:

```
1 | 2 4 5 8
2 | 1 3 5 7
```
#### How to Read It

* $1\|2$ means 12  
* $2\|7$ means 27  


---

## Frequency Tables (Ungrouped Data)

A **frequency table** counts how often each value appears.


#### Example

| Value | 1 | 2 | 3 | 4 |
|------|---|---|---|---|
| Frequency | 2 | 3 | 4 | 1 |

This means that:

* the value 1 appears 2 times, 
* the value 2 appears 3 times, 
* the value 3 appears 4 times, and
* the value 4 appears 1 time.

#### Finding the Mean

When data is grouped in a frequency table, we use the formula:

$$
\text{Mean} = \frac{\sum fx}{\sum f}
$$

* $\sum$: means "the sum of"
* $x$: the value
* $f$: the frequency, meaning how many times the value appears
* $fx$: the product of the value and its frequency

#### Example

| Value: $x$ | Frequency: $f$ | $fx$ |
|------------|----------------|------|
| 1          | 2              | 2    |
| 2          | 3              | 6    |
| 3          | 4              | 12   |
| 4          | 1              | 4    |
| Total      | $\sum f = 10$  | $\sum fx = 24$|     |

$$
\text{Mean} = \frac{\sum fx}{\sum f} = \frac{24}{10} = 2.4
$$



#### Relative Frequency

Relative frequency shows proportion:

$$
\text{Relative Frequency} = \frac{\text{frequency}}{\text{total}}
$$


#### Example

| Value: $x$ | Frequency: $f$ | Relative Frequency |
|------|----------|-------------------|
| 1    | 2        | $\frac{2}{10}$    |
| 2    | 3        | $\frac{3}{10}$    |
| 3    | 4        | $\frac{4}{10}$    |
| 4    | 1        | $\frac{1}{10}$    |
| Total| 10       |                  |

#### Uses

* Estimate probabilities  
* Compare data sets  

---

## Grouped Data

When we have a **large data set**, values are often grouped into intervals.

#### Example

| Class Interval | Frequency: $f$ |
|----------------|----------|
| 0 – 10         | 3        |
| 10 – 20        | 5        |
| 20 – 30        | 7        |



#### Estimating the Mean

We use **midpoints** of each interval.

| Interval | Midpoint | Frequency: $f$ | $fx$ |
|----------|----------|----------|-------------|
| 0–10     | 5        | 3        | 15          |
| 10–20    | 15       | 5        | 75          |
| 20–30    | 25       | 7        | 175         |

$$
\text{Mean}  \approx \frac{\sum fx}{\sum f}
$$

Therefore,

$$
\text{Mean}  \approx \frac{15 + 75 + 175}{3 + 5 + 7} = \frac{265}{15} \approx 17.67
$$

#### Estimating the Median

1. Find total frequency: $n = 15$  
2. Find median position:

    $$
    \frac{n+1}{2} = 8
    $$

3. Locate the interval containing the 8th value.
    Before doing this, we use the cumulative frequency, which is the running total of frequencies up to each interval.

    | Interval | Frequency | Cumulative |
    |----------|----------|-----------|
    | 0–10     | 3        | 3         |
    | 10–20    | 5        | 8         |
    | 20–30    | 7        | 15        |

    The cumulative frequency tells us how many data values we have up to that interval. Since the 8th value falls in the cumulative frequency of 8, the median lies in the interval: **10–20**, we might estimate it as **15**.


#### Estimating the Mode

The **modal class** is the interval with the highest frequency.

From the table:

* Modal class = **20–30**


---

## Bar Charts

Bar charts represent frequencies using bars.

* Each bar = category or interval  
* Height = frequency  

They are clear and easy to interpret.

#### Example

Consider the frequency table:

Cumulative frequency:

| Interval | Frequency |
|----------|----------|
| 0–10     | 3        | 
| 10–20    | 5        | 
| 20–30    | 7        | 

<p align="center">
   <img src="{{ site.baseurl }}/images/Statistics/bar_chart.png" width="600">
</p>


---

## Pie Charts

Pie charts represent data as proportions of a whole.

$$
\text{Angle} = \text{fraction} \times 360^\circ
$$


#### Important Note

Although pie charts are commonly taught:

* They are **not very precise**  
* It is hard to compare slices  
* Humans are bad at comparing angles  

For this reason, they are **rarely used in real data analysis today**. Bar charts are usually preferred.

#### Example    

Consider the frequency table:

| Interval | Frequency | Relative Frequency | Angle (degrees) |
|----------|----------|----------|------------------|
| 0–10     | 3        | $\frac{3}{15} \approx 20\%$ | $\frac{3}{15} \times 360^\circ = 72^\circ$ |
| 10–20    | 5        | $\frac{5}{15} \approx 33.33\%$ | $\frac{5}{15} \times 360^\circ = 120^\circ$ |
| 20–30    | 7        | $\frac{7}{15} \approx 46.67\%$ | $\frac{7}{15} \times 360^\circ = 168^\circ$ |

<p align="center">
   <img src="{{ site.baseurl }}/images/Statistics/pie_chart.png" width="600">
</p>

---

## Box-and-Whisker Plots

A **box-and-whisker plot** (box plot) is a way to summarise and visualise the **distribution of data** using five key values:

* Minimum  
* $Q_1$  
* Median  
* $Q_3$  
* Maximum  

#### What does each part represent?

<p align="center">
   <img src="{{ site.baseurl }}/images/Statistics/box_plot_1.png" width="600">
</p>


* The box goes from $Q_1$ to $Q_3$, this contains the middle $50\%$ of the data
* The line inside the box shows the median
* The whiskers extend to the minimum and maximum values

This helps us see:

* How the data is spread out
* Whether the data is skewed
* Where most values are concentrated


#### Example

Consider the following data set:

$$
2, 5, 8, 13, 20
$$

Then,

$$
\text{Min} = 2, \quad Q_1 = 5, \quad \text{Median} = 8, \quad Q_3 = 13, \quad \text{Max} = 20
$$

<p align="center">
   <img src="{{ site.baseurl }}/images/Statistics/box_plot.png" width="600">
</p>

---

## Cumulative Frequency

Cumulative frequency is the **running total of frequencies up to each interval.**

#### Example

| Interval | Frequency | Cumulative |
| -------- | --------- | ---------- |
| 0–5      | 2         | 2          |
| 5–10     | 3         | 5          |
| 10–15    | 4         | 9          |
| 15–20    | 5         | 14         |
| 20–25    | 6         | 20         |
| 25–30    | 4         | 24         |
| 30–35    | 3         | 27         |


#### Cumulative Frequency Graphs

1. Plot upper class boundary vs cumulative frequency  
2. Join points with a smooth curve  


<p align="center">
   <img src="{{ site.baseurl }}/images/Statistics/smooth_cumulative_curve.png" width="600">
</p>

#### Finding Quartiles from Graph

**Steps:**

1. Find total frequency  
2. Calculate positions (25%, 50%, 75%)  
3. Draw horizontal line to curve  
4. Drop down to x-axis  

**Example:**

From the data above:
* Total frequency = 27
* $Q_1$ position = $0.25 \times 27 = 6.75$
* $Q_2$ position = $0.5 \times 27 = 13.5$
* $Q_3$ position = $0.75 \times 27 = 20.25$

<p align="center">
   <img src="{{ site.baseurl }}/images/Statistics/cumulative_quartiles.png" width="600">
</p>

---

## Common Mistakes

* Using endpoints instead of midpoints  when calculating the statistics in grouped data
* Forgetting cumulative frequency  
* Misreading graphs  
* Assuming grouped data gives exact values  
* Using pie charts for precise comparisons  

