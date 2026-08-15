# Conductor check: exact translation divided-difference identity

Campaign: `m9-m1-beta-translation-divided-difference`  
Role: coordinate and sign seam  
Allocation: analytical/algebraic only

Freeze a phase-removed cell and put

\[
y=L-\nu,\qquad F(L,y)=H(L,L-y).
\]

The relevant derivatives must be distinguished carefully. At fixed
translation coordinate \(y\),

\[
F_L=(\partial_L+\partial_\nu)H,
\qquad F_y=-\partial_\nu H.
\]

At fixed physical height \(\nu\), however,

\[
\partial_LH(L,\nu)=F_L(L,y)+F_y(L,y).
\]

On the diagonal, \((\partial_L+\partial_\nu)H(L,L)=F_L(L,0)\).
Consequently the exact Round-39 survivor is

\[
\mathfrak E_H(L,L-y)
=\frac{F_L(L,y)-F_L(L,0)}y
 \frac{F_y(L,y)}y
-\frac{F(L,y)-F(L,0)}{y^2}.                 \tag{40.C1}
\]

The fundamental theorem of calculus gives

\[
\frac{F_L(L,y)-F_L(L,0)}y
=\int_0^1F_{Ly}(L,ty)\,dt,
\]

and

\[
\frac{F_y(L,y)}y-\frac{F(L,y)-F(L,0)}{y^2}
=\int_0^1tF_{yy}(L,ty)\,dt.
\]

Thus

\[
\boxed{
\mathfrak E_H(L,L-y)
=\int_0^1F_{Ly}(L,ty)\,dt
+\int_0^1tF_{yy}(L,ty)\,dt.}                \tag{40.C2}
\]

As a control, if \(F(L,y)=ay+by^2/2\) is independent of \(L\), then
both the defining expression and (40.C2) equal \(b/2\). A formula with
\(-F_y(L,0)/y\) fails this test. My earlier conductor note made exactly
that error by replacing the fixed-\(\nu\) derivative with a fixed-\(y\)
derivative; it is retracted.

This correction does not settle the full norm. In particular, the
separate diagonal component of the singular hard-top regularizer,

\[
K_C(L,\nu)=-\frac{iH(L,L)}{2A(L)D(L,\nu)},
\]

has its own signed Cauchy/logarithmic finite-section behavior. That
behavior is independent of (40.C2) and must not be inserted into the
translation divided difference.

No numerical experiment or external theorem is used.
