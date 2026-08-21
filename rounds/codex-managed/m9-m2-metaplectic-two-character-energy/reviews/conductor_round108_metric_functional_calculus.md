# Conductor review: exact metric functional calculus

Campaign: m9-m2-metaplectic-two-character-energy

Starting graph SHA-256:
7347081c1a765acafc6a4d1e3a96171d7b971079c2af144f7a0eaa825309bb2a

## Exact operator

Fix \(g,k\), put

\[
 c={X\over2gk},
 \qquad
 K_\alpha(u)
 ={e(\operatorname {sgn}(\alpha)/8)\over\sqrt{2|\alpha|}}
 e\!\left(-{u^2\over4\alpha}\right)
\]

for \(\alpha\ne0\), and let \(T_0=I\).  For nonzero \(\alpha\),
define \(T_\alpha f=K_\alpha*f\) in the oscillatory sense.  With

\[
 \widehat f(y)=\int_{\mathbb R}f(\beta)e(-\beta y)\,d\beta,
\]

the Gaussian identity gives

\[
 \widehat{T_\alpha f}(y)=e(\alpha y^2)\widehat f(y),
 \qquad
 T_{-\alpha}=T_\alpha^{-1}=T_\alpha^*.
\]

Now retain the complete metric coefficient

\[
 W_R(t)=\sum_{r\in\mathbb Z}\widehat W_R(r)e(rt),
 \qquad
 \widehat W_R(0)=\mu_R,
\]

and define the coherent metaplectic sum

\[
 \mathcal M_{c,R}
 =\sum_{r\in\mathbb Z}\widehat W_R(r)T_{rc}.
\]

Symmetric Fourier truncation followed by the accepted smooth limit gives
the exact functional-calculus identity

\[
 \boxed{\quad
 \widehat{\mathcal M_{c,R}f}(y)
 =W_R(cy^2)\widehat f(y).
 \quad}
\]

The density is the \(r=0\) identity operator.  It is not a separate
error or a removable zero frequency.

## Match to the complete physical coefficient

For one literal collared physical amplitude set

\[
 \beta=J\sqrt x,
 \qquad
 f(\beta)
 ={2\beta\over X}
 A^\circ_{h,s}(\beta^2/X)
 e(k\beta^2/X).
\]

If \(y=\sqrt s-\sqrt h\), then \(dx=(2\beta/X)d\beta\) and

\[
\begin{aligned}
 &W_R\!\left({Xy^2\over2gk}\right)
 \int A^\circ_{h,s}(x)e(kx-J\sqrt x\,y)\,dx\\
 &\qquad
 =W_R(cy^2)\widehat f(y)
 =\widehat{\mathcal M_{c,R}f}(y).
\end{aligned}
\]

Thus the Gaussian density-plus-discrepancy construction is exactly the
Fourier conjugate of multiplication by the original punctured metric
window.  No approximation, saddle evaluation, or pointwise owner
interpolation is involved.

## Capacity and inversion

Plancherel gives

\[
 \lVert\mathcal M_{c,R}f\rVert_2^2
 =\int_{\mathbb R}|W_R(cy^2)|^2
          |\widehat f(y)|^2\,dy.
\]

This is precisely the metric-windowed capacity already present before
Gaussian separation.  The individual \(T_{rc}\) are unitary, while
their coherent sum is the original bounded multiplier.  Moreover,

\[
 \lVert\mathcal M_{c,R}\rVert_{2\to2}
 =\lVert W_R\rVert_\infty\asymp1,
\]

because \(cy^2\) ranges through every residue class modulo one as
\(y\) varies.  Concentrating \(\widehat f\) near a point where
\(|W_R|\) is maximal gives the matching lower bound.  This is the
precise arbitrary-coefficient control: no coefficient-uniform
\(\rho^{-1/2}\) contraction is possible, although the literal
arithmetic vector could still have additional cancellation.

Consequently:

- the visible factor \((2|rc|)^{-1/2}\) is not a saving;
- density and discrepancies cannot be estimated as unrelated positive
  pieces;
- deleting \(r=0\), taking absolute values over \(r\), or retaining a
  bounded \(\tau\)-window changes the operator;
- inversion of the Gaussian transform reconstructs the original
  metric coefficient exactly.

The identity does not rule out cancellation after the discrete
\(\chi_4\)-weighted actual vector is inserted.  It proves that such
cancellation is an additional restriction or correlation theorem, not
a consequence of the metaplectic representation.

## Relation to the fixed-\(a\) Gram

In the accepted character-free row notation, the linear block is
\(\sum_{a,q}(-1)^qF_a(q)\).  The shift-\(s\) Gram multiplier satisfies

\[
 (-1)^s
 \chi_4(a)\chi_4(a+2q+2s)
 \chi_4(a)\chi_4(a+2q)=1.
\]

Hence the fixed-\(a\) Gram has no residual primitive-ray character
orthogonality for the Gaussian transform to exploit.  The exact
functional calculus therefore returns to the character-neutral,
actual-phase cross-\(q\) correlation at the same capacity.

No \(\rho^{-1}\) energy gain, hard-cone theorem, \(M9\!-\!M2\), or
global exponent follows from this identity alone.
