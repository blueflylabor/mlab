## Projection
### Dot product
Dot Product:
Angle $\theta$ between two vectors $x$ and $y$ in $\mathbb{R}^3$:

$$
\begin{aligned}
x \cdot y = x^T y = \Vert x \Vert \Vert y \Vert \cos\theta
\end{aligned}
$$

### Cross Product
Cross product between two vectors $u$ and $v$ in $\mathbb{R}^3$ is a vector $w = u \times v$, which is orthogonal to $u$ and $v$:
  $$
  \begin{aligned}
  w &= \det{\begin{bmatrix} i^1 & i^2 & i^3 \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{bmatrix}} \\
  &= +i^{1} \cdot \det{\begin{bmatrix} u_2 & u_3 \\ v_2 & v_3 \end{bmatrix}} - i^{2} \cdot \det{\begin{bmatrix} u_1 & u_3 \\ v_1 & v_3 \end{bmatrix}} + i^{3} \cdot \det{\begin{bmatrix} u_1 & u_2 \\ v_1 & v_2 \end{bmatrix}} \\
  &= w = (u_2v_3-u_3v_2)i^1+(u_3v_1-u_1v_3)i^2+(u_1v_2-u_2v_1)i^3\\
  &= w = (u_2v_3-u_3v_2)\begin{bmatrix}1\\0\\0\end{bmatrix}+(u_3v_1-u_1v_3)\begin{bmatrix}0\\1\\0\end{bmatrix}+(u_1v_2-u_2v_1)\begin{bmatrix}0\\0\\1\end{bmatrix}\\
  &= \begin{bmatrix} u_2v_3 - u_3v_2 \\ u_3v_1 - u_1v_3 \\ u_1v_2 - u_2v_1 \end{bmatrix}
  \end{aligned}
  $$
  with $i^k$ being the $k$-th unit vector

Furthermore: $\Vert u \times v\Vert = \Vert u \Vert \times \Vert v \Vert \sin \theta$

### Coordinates


Let $X = \begin{pmatrix}x^1, x^2, \ldots x^n \end{pmatrix}$ be a complete orthonormal coordinate frame for $\mathbb{R}^n$, any ponit/vector $p\in$ $\mathbb{R}^n$ can be uniquely expressed as a linear combination of the basis vectors:
$$
\begin{aligned}
p = \sum_{k=1}^{n}{[p]^X_k x^k}
\end{aligned}
$$
