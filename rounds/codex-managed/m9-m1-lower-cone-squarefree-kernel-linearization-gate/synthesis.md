# Round 145 synthesis: strict squarefree-kernel reduction

Campaign: `m9-m1-lower-cone-squarefree-kernel-linearization-gate`  
Starting graph SHA-256: `cc5e1b2597d6d233702d566f49884dc0530d0fa62395ce03684d2f55ae19e756`

## Decision

Round 145 closes under

\[
\boxed{\mathsf{strict\_squarefree\_kernel\_reduction}}.
\]

The squarefree-kernel change is exact and noninvertibly deletes a
target-safe large-square complement.  It does not estimate the remaining
signed scalar.

## Accepted reduction

Write \(m=st^2\) uniquely with \(s\) squarefree.  For the cone
coefficient

\[
C(m)=\sum_{\substack{hr=m\\r\ {\rm odd}\\r>4h}}\chi_4(r),
\]

one exact multiplicity-one formula is

\[
C(st^2)=
\sum_{\substack{\gamma\mid t\\\gamma\ {\rm squarefree}\\
(\gamma,s)=1\\\gamma\ {\rm odd}}}\chi_4(\gamma)
\sum_{\substack{de=s\\e\ {\rm odd}}}\chi_4(e)
\sum_{\substack{ab=t/\gamma\\b\ {\rm odd}\\eb^2>4da^2}}1.
\]

Equivalently, with \(G=(h,r)\),

\[
C(st^2)=
\sum_{de=s}^{\rm ord}
\sum_{\substack{Gab=t\\(da,eb)=1\\Geb\ {\rm odd}\\
eb^2>4da^2}}\chi_4(Ge).
\]

The first formula records the common part of the two squarefree kernels;
the second records the full gcd.  They have different internal variables
but are both bijective and retain every even case, character sign, strict
cone, and multiplicity.

For every literal half-open block
\(\mathcal I_M=\mathbb N\cap[M,B_M)\), \(B_M\leq2M\), the aggregate
with \(t\geq T\) has absolute price

\[
\ll_{\varepsilon,V}X^\varepsilon {M^{1/4}\over T}.
\]

Therefore the Round-144 survivor is target-equivalent to

\[
\boxed{
\sum_M\sum_{1\leq t<M^{1/4}}
\sum_{\substack{s\ {\rm squarefree}\\st^2\in\mathcal I_M\\
|k_{s,t}^2-Nst^2|>M^{3/4}}}
(st^2)^{-3/4}V_{\rm low}(R^2st^2/N)
C(st^2)e(t\sqrt{Ns}),}
\]

up to \(O_{\varepsilon,V}(X^\varepsilon)\).  The retained support has
\(s>M^{1/2}\).

## Why linearization does not close the bound

The exact mask is

\[
\|t\sqrt{Ns}\|={|j_{st^2}|\over k_{s,t}+t\sqrt{Ns}},
\qquad |j_{st^2}|>M^{3/4}.
\]

If \(N=Dw^2\), exact resonance is only \(s=D\); all other fibres are
generalized Pell norms.  But large \(|j|\) does not separate the base
frequency.  For \(X=N=sL^2+1\),

\[
\sqrt{Ns}=sL+\rho,\qquad
\rho={1\over\sqrt{L^2+1/s}+L},
\]

and, while \(t\rho<1/2\),

\[
j_{st^2}=-st^2=-m,\qquad e(t\sqrt{Ns})=e(t\rho).
\]

With \(L=s\), a literal profiled small-\(t\) range survives the mask
while \(t\rho\to0\).  Hence no uniform frequency-gap or bounded
continued-fraction shortcut is valid.

The \(t=1\) layer is mandatory and has no \(t\)-sum.  Its available
divisor-envelope upper capacity is \(M^{1/4+o(1)}\), reaching
\(R^{1/2+o(1)}\) on the top block.  This is not a lower bound; signed
cancellation across squarefree \(s\) remains possible and is precisely
what is missing.

The primary-source audit found no matching theorem.  Even after granting
favorable smoothing and separated coefficients, Sargos--Wu leaves
\(R^{2/5+\varepsilon}\) on the \(t=1\) top layer; Robert--Sargos leaves
\(R^{1/2+\varepsilon}\) or \(R^{3/4+\varepsilon}\), depending on the
coefficient slot.  Complete-divisor, Liouville, linear-squarefree, and
fixed-quadratic results each fail an exact coefficient, phase,
uniformity, or power hypothesis.

## Remaining frontier

The first open owner is the displayed small-\(t\), large-\(s\)
fixed-centre individual complex scalar.  A continuation must prove a
signed estimate across the actual squarefree kernels, or a stronger
joint estimate coupling \(s\) and \(t\), while retaining both exact
coefficient parametrizations, the mask, profile, terminal endpoints, and
Pell geometry.

The independent Round-138 collar-tail cross owner remains open.
M9-M1, M9-M2, endpoint uniformity, M9, and the conditional quarter bridge
remain open.  The strongest theorem proved internally remains exponent
\(1/3\).  The separately audited external exponent remains

\[
{3292+25\sqrt{1717}\over13762}
=0.3144831759740614\ldots.
\]

Round 145 proves no global exponent improvement and does not prove the
Gauss circle conjectural exponent \(1/4\).
