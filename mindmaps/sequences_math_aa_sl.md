---
title: Sequences and Series Mind Map - IB Mathematics AA SL
markmap:
  colorFreezeLevel: 2
  maxWidth: 350
  theme: default
  initialExpandLevel: 4
---

<!-- # Sequences and Series

$$ S_n = \frac{n}{2} (2a + (n-1)d) $$

```mermaid
mindmap
  root((Sequences and Series))
    Sequences
      Arithmetic Sequence
        ["an = a1 + (n-1)d"]
        ["Each term increases by a constant difference d"]
      Geometric Sequence
        ["an = a1 * r^(n-1)"]
        ["Each term is multiplied by a common ratio r"]
``` -->


# **Sequences and Series</br>IB Mathematics AA SL**

## **Arithmetic Sequence**
- **n-th Term Formula**: 
  $a_n = a_1 + (n-1)d$
  - **Explanation**: 
    Each term increases by a constant difference $d$.
  - **Example**: 
    Find the $n$-term:
    $2, 4, 6, 8, 10, ...$ 
    Given that $a _{1}=2$ and $d = 2$, 
    we have: $a_{n}=2+(n-1)2$
    $\Rightarrow \boxed{a_{n}=2n}$
      

## **Geometric Sequence**
- **n-th Term Formula**:
   $a_{n} = a_{1} \cdot r^{n-1}$
  - **Explanation**: 
    Each term is multiplied by a common 
    ratio $r$.
  - **Example**: 
    Find the $n$-term:
    $3, 6, 12, 24, ...$
    Given that $r=2$ and $a_{1}=3$,
    we have: $a_{n}=3(2^{n-1})$
    $\Rightarrow \boxed{a_{n}=3(2^{n-1})}$

## **Arithmetic Series**
- **Sum Formula**: 
  $S_{n} = \frac{n}{2} (2a_{1} + (n-1)d)$
  - **Explanation**: 
    Sum of the first $n$ terms of an arithmetic sequence. This formula is useful when we know the first term and the common difference.
  - **Example**: 
    Find $S_{10}$:
    $2, 4, 6, 8, 10, ...$ 
    Given that $a_{1}=2$, $d=2$ and $n=10$,
    we have: $S_{10}= \frac{10}{2}(2(2)+(10-1)2)$
    $\Rightarrow \boxed{S_{10}=110}$
- **Sum Formula**: 
  $S_{n} = \frac{n}{2} (a_{1} + a_{n})$
  - **Explanation**: 
    Sum of the first $n$ terms of an arithmetic sequence. This formula is useful when we know the first and last terms.
  - **Example**: 
    Find $S_{10}$:
    $2,4, ...,20$ where $20=a_{10}$,
    Given that $a_{1}=2$, $a_{10}=20$ and $n=10$,
    we have: $S_{10}= \frac{10}{2}(2+20)$
    $\Rightarrow \boxed{S_{10}=110}$
## **Geometric Series**
- **Finite Sum**: 
$S_n = \frac{a_{1} (1 - r^{n})}{1 - r}, \quad r \neq 1$
  - **Explanation**:
    Sum of the first $n$ terms of a geometric sequence. This formula is useful when we know the first term and the common ratio. The common ratio must be different from 1, otherwise, we would be dividing by 0.
  - **Example**:
    Find $S_{8}$:  
    $3, 6, 12...$ 
    Given that $a_{1} = 3$ and $r = 2$,
    we have: $S_{8} = \frac{3(1-2^{8})}{1-2}$
    $\Rightarrow \boxed{S_{8}=765}$

- **Infinite Sum**: 
  $S_{\infty} = \frac{a_{1}}{1 - r}, \quad |r| < 1$
  - **Explanation**: 
    The sum of an infinite geometric series only make sense if:  $-1<r< 1$. Once again, we need to know the first term and the common ratio.
  - **Example**:
    Find $S_{\infty}$:  
    $\frac{1}{2}, \frac{1}{4}, \frac{1}{8}...$ 
    then $a_{1} = \frac{1}{2}$ and $r = \frac{1}{2}$,
    therefore $S_{\infty} = \frac{\frac{1}{2}}{1-\frac{1}{2}}$
    $\Rightarrow \boxed{S_{\infty}=1}$


