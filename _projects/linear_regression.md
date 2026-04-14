---
title: Linear Regression
date: 2026-04-13
description: |
    <p>
    In this lesson, students learn how to analyze the relationship between two variables using scatter plots and linear regression. This allows us to identify trends and make predictions based on data.
    </p>
    <hr>
    <h1>Class Objectives</h1>
    <ul>
      <li><b>Understand</b> what correlation is.</li>
      <li><b>Interpret</b> scatter plots.</li>
      <li><b>Identify</b> types of correlation.</li>
      <li><b>Use</b> a line of best fit.</li>
      <li><b>Make</b> predictions using linear models.</li>
    </ul>

categories: [IGCSE, Statistics]
image: '/images/Statistics/linear_regression_portada.png'
---

## Scatter Plots

A **scatter plot** is a graph used to display the relationship between two variables.

* Each point represents a pair of values $(x,y)$
* The horizontal axis shows the independent variable  
* The vertical axis shows the dependent variable  

#### Example

Suppose we record the number of hours a student studies and their test score:

| Hours Studied: $x$ | 1 | 2 | 3 | 4 | 5 |
|----------------------|---|---|---|---|---|
| Score: $y$        | 50 | 55 | 65 | 70 | 80 |

Each pair $(x,y)$ represents a point:

$$
(1,50),\ (2,55),\ (3,65),\ (4,70),\ (5,80)
$$

When we plot these points on a graph, we get a **scatter plot** that shows the relationship between hours studied and test score. From the plot, we can observe that as the number of hours studied increases, the score also tends to increase (positive correlation).

<p align="center">
   <img src="{{ site.baseurl }}/images/Statistics/scatter_example.png" width="800">
</p>

---

## Correlation

**Correlation** describes the relationship between two variables.

### Types of Correlation

* **Positive correlation** → as $x$ increases, $y$ increases  

    <p align="center">
    <img src="{{ site.baseurl }}/images/Statistics/positive_correlation.png" width="800">
    </p>

* **Negative correlation** → as $x$ increases, $y$ decreases  

    <p align="center">
    <img src="{{ site.baseurl }}/images/Statistics/negative_correlation.png" width="800">
    </p>

* **No correlation** → no clear pattern, it looks random or as a cloud of points

    <p align="center">
    <img src="{{ site.baseurl }}/images/Statistics/no_correlation.png" width="800">
    </p>

---

## Line of Best Fit

A **line of best fit** is a straight line that best represents the trend of the data. Using a calculator, software, or by estimating (eye-balling), we can draw a line of best fit.

* It should pass through the middle of the points
* It should have roughly the same number of points above and below the line


> To obtain an accurate equation and graph of the line of best fit, we need a calculator


<p align="center">
<img src="{{ site.baseurl }}/images/Statistics/positive_correlation_line.png" width="800">
</p>

---

## Linear Regression

**Linear regression** is the process of finding the equation of the line of best fit.

The general form is:

$$
y = mx + b
$$

Where:

* $m$ = slope (rate of change)  
* $b$ = y-intercept  

These values can be calculated using statistical software or a calculator, which will give us the equation of the line of best fit based on the data points.


#### Example

Suppose we have the following data:

| $x$ | 1 | 2 | 3 | 4 | 5 |
|------|---|---|---|---|---|
| $y$ | 2 | 4 | 5 | 4 | 5 |

We plot the points and use a calculator to find the equation, which we then use to draw the line of best fit:

$$
y = 0.6x + 2.2
$$


<p align="center">
<img src="{{ site.baseurl }}/images/Statistics/linear_regression_example.png" width="800">
</p>


---

## Making Predictions

We can use the equation to estimate values.

**Example:**

Using the equation $y = 0.6x + 2.2$, we can predict $y$ for a given $x$. 

When $x = 6$:

$$
y = 0.6(6) + 2.2 = 5.8
$$

---

## Strength of Correlation

The closer the points are to the line:

* Closer → strong correlation  
* More spread out → weak correlation 

---

## Limitations

* **Correlation does not imply causation**
    Correlation means that two variables are related or follow a pattern (for example, as one increases, the other also increases). However, **causation** means that one variable directly causes a change in the other. Just because two variables are correlated does not mean that one causes the other.

    **Example: Correlation vs Causation**

        During summer, we observe that:

        * Ice cream sales increase
        * The number of people swimming also increases

        These two variables are correlated (they increase at the same time).

        However:

        * Eating ice cream does not cause people to go swimming
        * Swimming does not cause people to eat ice cream

        What is actually happening?

        There is a third variable: Hot weather

        * Hot weather → more people buy ice cream
        * Hot weather → more people go swimming

* **Predictions are estimates, not exact values**
    The line of best fit gives an approximation, so predicted values may not be perfectly accurate.
* **Extrapolation can be unreliable**
    Predictions made outside the range of the data may not follow the same pattern and can be misleading.

    * **Interpolation** → predicting within the data range  
    * **Extrapolation** → predicting outside the data range (less reliable)  


