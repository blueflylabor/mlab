#  Mathematical Background
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
### Orthonormal Coordinates Propostion
the $k$-th coordinate of $p$ with respect to frame $X$ is obtained by othogonal projection(dot product) onto $x^k$:
$$
\begin{aligned}
[p]_k^X = p \cdot x^k, \quad 1 \le k \le n
\end{aligned}
$$
In $\mathbb{R}^3$, for a fixed base frame $F = \begin{Bmatrix} f^1, f^2, f^3\end{Bmatrix}$ and a mobile link frame $M = \begin{Bmatrix} m^1, m^2, m^3\end{Bmatrix}$ sharing the same origin:
$$
\begin{aligned}
[p]^F = \begin{bmatrix} p \cdot f^1\\ p \cdot f^2\\ p \cdot f^3 \end{bmatrix}, [p]^M = \begin{bmatrix} p \cdot m^1\\ p \cdot m^2\\ p \cdot m^3 \end{bmatrix}
\end{aligned}
$$

### Coordinate Transformation Matrix & Its Inverse
Let $F$ = $\begin{Bmatrix} f^1, \ldots, f^n \end{Bmatrix}$ and $M$ = $\begin{Bmatrix} m^1, \ldots m^n\end{Bmatrix}$ be two orthonoramal frames with the same origin. Define the $n \times n$ matrix $A$ with entries :
$$
\begin{aligned}
A_{kj} = f^k \cdot m^j, A_{kj} = f^k \cdot m^j, \quad 1 \le k, j \le n\
\end{aligned}
$$
Then $A$ maps coordinates from frame $M$ into frames $F$:
$$
\begin{aligned}
[p]^F = A[p]^M
\end{aligned}
$$
Notice that the $j$-th column of A is simply $[m^j]^F = [f^1 \cdot m^j, f^2 \cdot m^j, f^3 \cdot m^j]$, i.e., the unit axis $m^j$ expressed in frame $F$\. 
Inverse Coordinate Transformation: Since A is an orthogonal matrix ($A^TA = I$), mapping coordinates from F back into M is given by the transpose:
$$
\begin{aligned}
[p]^M = A^{-1}[p]^F = A^T[p]^F
\end{aligned}
$$

#### Example 2
Suppose mobile frame $M$ is rotated by $90^\circ$ counter-clockwise around $f^3$ relative to fixed frame $F$. Then in frame $F$:

$$
\begin{aligned}
&m^1 \space points \space along +f^2 \implies [m^1]^F = \begin{bmatrix} 0 & 1 & 0 \end{bmatrix}^T\\

&m^2 \space points \space along -f^1 \implies [m^2]^F = \begin{bmatrix} -1 & 0 & 0 \end{bmatrix}^T\\

&m^3 \space coincides \space with +f^3 \implies [m^3]^F = \begin{bmatrix} 0 & 0 & 1 \end{bmatrix}^T
\end{aligned}
$$
Assembing these three columns gives the transformation matrix $A$:
$$
\begin{aligned}
A = \begin{bmatrix} 0, -1, 0\\ 1, 0, 0\\ 0, 0, 1\end{bmatrix}
\end{aligned}
$$
If a point has coodinates $[p]^M = \begin{bmatrix}0.5\\0.6\\1.4\end{bmatrix}$ in frame $M$, its coordinates in frame F are:
$$
\begin{aligned}
[p]^F = A[p]^M = \begin{bmatrix} 0, -1, 0\\ 1, 0, 0\\ 0, 0, 1\end{bmatrix}\begin{bmatrix}0.5\\0.6\\1.4\end{bmatrix} = \begin{bmatrix}-0.6\\0.5\\1.4\end{bmatrix}
\end{aligned}
$$
Conversely, given$[p]^F$, we recover $[p]^M = A^T[p]^F= {\begin{bmatrix} 0, -1, 0\\ 1, 0, 0\\ 0, 0, 1\end{bmatrix}}^T\begin{bmatrix}-0.6\\0.5\\1.4\end{bmatrix} = \begin{bmatrix}0.5\\0.6\\1.4\end{bmatrix}$

## Fundamental Rotations
Assume frames $F$ and $M$ initially coincide, and we rotate $M$ about axis $f^1$ by angle $\phi$(counter-clockwise according to the right-hand rule)
<img src="./pics/slide10.png" width = "50%">

Using $R_1(\phi)_{kj} = f^k \cdot m^j$:
Since $m^1 = f^1$, we have $f^1 \cdot m^1 =1$, and $m^1 \perp f^2, f^3 \implies f^2 \cdot m^1 = f^3 \cdot m^1 = 0$

And $f^2 \cdot m^2 = \cos\phi$
$$
\begin{aligned}
f^2 \cdot m^2 =& \cos\phi\\
f^3 \cdot m^2 =& \cos(\frac{\pi}{2}-\phi)=\sin\phi\\
f^2 \cdot m^3 =& \cos(\frac{\pi}{2}+\phi)=-\sin\phi\\
f^3 \cdot m^3 =& \
\end{aligned}
$$