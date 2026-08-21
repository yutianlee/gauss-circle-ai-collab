# Conductor candidate: exact four-row self-return and directional survivor

Campaign: `m9-m1-joint-four-row-spectral-gap`.

Starting graph SHA-256:
`d59fac4b3be1d0773a9ab944eac0e3048d381353be6f3a5d7a11e3bc82456918`.

This candidate proves a mechanism obstruction and an exact reduction.  It
does not estimate the canonical hard Gram.

## 1. Literal hard atom

Retain the Round-92 successive hard complement, the unique global
\(u=0\) owner, every local class, sign, alias, reflection, modulus multiple,
Ramanujan term, prime-power factor, nonunit \(K\), and the full \(2\)-part.
One atom of the hard sum is

\[
 {\Omega_{b,d,u}(n,m)\over M^5}
 e_M(dV+nA-mB_2)\mathfrak T_M(u,A,B_2,V),
\]

where

\[
 \Omega_{b,d,u}(n,m)=
 I_b(n+d+u)\overline{I_b(n)}
 \overline{I_b(m+d)}I_b(m)
\]

and

\[
 \mathfrak T_M=M\sum_x^{\mathrm{four\ units}}
 e_M\!\left(ux+K\Phi_{A,B_2,V}(x)\right).
\]

Opening the trace changes \(M^{-5}\) to \(M^{-4}\), exactly the product of
the four normalized physical rows.  There is no unused power of \(M\).

## 2. Unimodular row coordinates

Put

\[
 r=n+d+u,\qquad s=m+d.
\]

For fixed \(n,m\), this is an integral bijection in \((d,u)\), with

\[
 d=s-m,\qquad u=r-s+m-n.
\]

The complete linear phase satisfies the exact identity

\[
 ux+dV+nA-mB_2
 =rx+n(A-x)+s(V-x)+m(x-V-B_2).
\]

Therefore the hard atom is a product of the four actual rows based at

\[
 x,\qquad x-A,\qquad x-V,\qquad x-V-B_2,
\]

and the fourfold symbol becomes

\[
 I_b(r)\overline{I_b(n)}\,
 \overline{I_b(s)}I_b(m).
\]

The Fejer factor is

\[
 (U-|r-s+m-n|)\mathbf1_{0<|r-s+m-n|<U},
\]

and the deep localizer is evaluated at \(s-m\).  Fourier inversion is thus
the original centered Toeplitz four-row Gram, not a new independent average.

## 3. Exact Hessian meaning

On one smooth stationary branch let the row phase be \(\psi_b\).  For

\[
 \Psi(d,u)=\psi_b(n+d+u)-\psi_b(m+d)+\text{linear terms},
\]

write \(a=\psi_b''(r)\) and \(c=\psi_b''(s)\).  Then

\[
 D^2_{d,u}\Psi=
 \begin{pmatrix}a-c&a\\a&a\end{pmatrix},
 \qquad \det D^2_{d,u}\Psi=-ac.
\]

With

\[
 L=\begin{pmatrix}1&1\\1&0\end{pmatrix}\in GL_2(\mathbb Z),
\]

one has

\[
 D^2_{d,u}\Psi
 =L^T\operatorname{diag}(a,-c)L.
\]

At \(r,s\asymp Q^2\), both curvatures have scale \(J^{-1/5}\), so the
determinant really is \(\asymp-J^{-2/5}\).  Its two directions are exactly
the two one-row directions.  A double B-process on a smooth pre-owner sum
reconstructs those rows and the same Fejer Gram.  Multiplying the already
charged row capacity by a further \(J^{-1/5}\) double-counts the same
stationary transform.

After the hard owners are imposed, the mask is arithmetic in the physical
labels and \(u\), while row entry and exit are moving.  It is not the fixed
compactly supported smooth amplitude required by a scalar multidimensional
B-process.  Opening its modes returns to the exact physical rows; estimating
the modes separately loses the required power.

## 4. High-trace obstruction

For fixed \(b,M,u,d,A,B_2,V,x\), the \((n,m)\)-coefficient factors as

\[
 \bigl[I_b(n+d+u)\overline{I_b(n)}e_M(nA)\bigr]
 \bigl[\overline{I_b(m+d)}I_b(m)e_M(-mB_2)\bigr].
\]

It is rank one.  Configuration-separated powers contain diagonal and
backtracking words at Schur capacity.  In row coordinates, every actual
phase is a gauge \(Z_\alpha\overline{Z_\beta}\), so it telescopes around a
closed trace cycle.  CRT and repeated-prime paired cycles remain paired, and
the accepted prime-power descent is exactly invertible.  Consequently an
ordinary high trace of the configuration-separated or post-absolute-value
operator supplies no spectral gap.

The global operator is a direct sum over conductor rows \(b\).  Its ordinary
operator norm is the maximum row-block norm and its trace moments are sums
of row-block trace moments.  Conductor-row cancellation can occur only in
the fixed scalar matrix coefficient before it is replaced by a uniform norm.

## 5. Exact two-adic control

For \(M=8\) and any nonempty unit cell, \(A,B_2,V\) are even and every unit
is self-inverse.  Hence

\[
 \mathfrak T_8(u,A,B_2,V)
 =8e_8(K(A-B_2))c_8(u),
\]

where

\[
 c_8(u)=
 \begin{cases}
 4,&8\mid u,\\
 -4,&u\equiv4\pmod8,\\
 0,&4\nmid u.
 \end{cases}
\]

In particular \((A,B_2,V)=(2,2,2)\) gives the nonzero residual mode
\(u=4\) with trace \(-32\).  This does not duplicate the owned \(u=0\)
coefficient.  Its local phase is a coboundary and telescopes on closed walks,
independently of whether \(K\) is a unit.  It is a mandatory coherent control,
not a global lower bound for the complete hard sum.

## 6. Correct remaining target

Let \(\mathsf C_U\) be the exact coefficient-blind Schur capacity after all
owners, and normalize the actual vectors and block operator.  The canonical
hard estimate is equivalent to the single directional inequality

\[
 \left|\widehat p_U^*\widehat{\mathcal K}_U\widehat q_U\right|
 \ll_\varepsilon X^\varepsilon
 { (U/B)J^{14/5}\over\mathsf C_U}.
\]

At the top this asks for \(J^{-1/6}=B^{-10/9}\).  A uniform operator-norm
bound is stronger than necessary.  If a Schur-normalized block of dimension
\(N\asymp B^2\) had a positive proportion of entries of size \(\asymp N^{-1}\),
Frobenius would force norm \(\gg B^{-1}\), short of \(B^{-10/9}\).  The
literal complete hard symbol has not been proved to contain such a dense
comparable-entry plateau, so this last statement is only a hostile control.

The first open analytic statement is therefore cancellation of the fixed
actual vector across physical configurations and, possibly, across the
outer scalar sum over conductor rows, with the literal hard mask and every
transition retained.  No coefficient-uniform or configuration-separated
version should replace it.

## 7. Scope and graph effect

Promote only the exact separable self-return/configuration-separated
obstruction and the directional reformulation.  Reject claims that the
\((d,u)\) Hessian gives an extra \(J^{-1/5}\), that a second completion gives
a new power, or that an ordinary direct-sum high trace automatically uses
conductor-row cancellation.  Keep the canonical hard estimate, the rest of
the global M1 route, blockwise M9-M1, M9-M2, endpoint uniformity, M9, and the
quarter theorem open.
