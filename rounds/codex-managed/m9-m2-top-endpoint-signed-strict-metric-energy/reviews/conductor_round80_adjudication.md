# Round 80 conductor adjudication

Campaign: `m9-m2-top-endpoint-signed-strict-metric-energy`  
Round: 80  
Starting graph SHA-256:  
`cb007911c1e9d407d9adbc8919ce44cc3eaab411a212d0925e1176f5a154a43a`

## Decision

Promote one exact route obstruction: the complete Round-77 coefficient
cancels both the nearest-integer quotient sign and the apparent
half-integer Fourier gap.  The period-one metric window therefore retains
its integer zero mode, and the resulting kernel is exactly the residual
transposed two-character energy in its original variables.

Reject the quotient-parity, half-frequency-gap, and discrepancy-only
closures.  Retain the signed strict-metric target, the complete top cone,
\(M9\!-!M2\), \(M9\!-!M1\), \(M9\), endpoint uniformity, and the
global exponent open.  No new hard parameter subrange closes in this
round.

The clean statement-only report, the independent analytic report, the
hostile/source report, and the conductor calculation agree on the exact
carrier, every sign, the restored density mode, and the original-variable
return.  No numerical experiment or unverified external theorem is used.

## Exact promoted interface

Let

\[
 \theta={\Lambda\over k}
 ={X(\sqrt b-\sqrt a)^2\over2k},\qquad
 q={b-a\over2},
\]

and retain the complete collar-extracted coefficient

\[
 \mathfrak B^\circ_{a,b,k}(g)
 =g\int_{b/4}^{a}A^\circ_{ga,gb}(gu)
 e\!\left(g\left[-J(\sqrt b-\sqrt a)\sqrt u+ku
                   +{\theta\over2}\right]\right)du.
\]

Define

\[
 \mathfrak C^\circ_{a,b,k}(g)
 :=e(-g\theta/2)\mathfrak B^\circ_{a,b,k}(g).
\]

Then, exactly and with every floor, star, profile, physical collar, lift
endpoint, and saddle transition unchanged,

\[
 \boxed{
 \mathfrak C^\circ_{a,b,k}(g)
 =g\int_{b/4}^{a}A^\circ_{ga,gb}(gu)
 e\!\left(g\left[ku-J(\sqrt b-\sqrt a)\sqrt u\right]\right)du.}
                                                               \tag{80.A}
\]

If \(\theta=\ell+\eta\), \(p=\ell k\), and \(g\) is odd, then

\[
 \boxed{
 (-1)^{q+\ell}\mathfrak B^\circ(g)e(-g\eta/2)
 =(-1)^q\mathfrak C^\circ(g).}                    \tag{80.B}
\]

Thus \((-1)^\ell=(-1)^{p/k}\) is not an additional character of the
complete summand.  It cancels pointwise against the carrier
\(e(g\theta/2)\) already present in \(\mathfrak B^\circ\).

Let

\[
 W_R(t)=\mu_R+\sum_{r\ne0}\widehat W_R(r)e(rt),
 \qquad \mu_R\asymp R^{-1}.
\]

The exact complete-symbol window identity is

\[
 W_R(\theta)e(-g\theta/2)\mathfrak B^\circ(g)
 =\mu_R\mathfrak C^\circ(g)
  +\sum_{r\ne0}\widehat W_R(r)e(r\theta)
    \mathfrak C^\circ(g).                           \tag{80.C}
\]

The half-integral frequencies seen before restoring the carrier are
therefore spurious.  Integer frequencies, including the literal density
mode \(r=0\), return.

Finally, under

\[
 h=ga,\qquad s=gb,\qquad x=gu,
\]

one has

\[
 \mathfrak C^\circ_{a,b,k}(g)
 =\int_{s/4}^{h}A^\circ_{h,s}(x)
 e\!\left(kx-J(\sqrt s-\sqrt h)\sqrt x\right)dx,   \tag{80.D}
\]

and

\[
 (-1)^q=\chi_4(a)\chi_4(b)=\chi_4(h)\chi_4(s).    \tag{80.E}
\]

Unique primitive-ray factorisation makes (80.D)--(80.E) a literal
return to the residual transposed character kernel, not merely an
analogy of phase or scale.

## Density and quantitative ledger

For one residual block put

\[
 \rho={AJD^3\over L^3}>1.
\]

The accepted strict-metric incidence and lift-Abel estimates still give
only

\[
 |\mathcal S^{\rm hard}_{A,D,K,G,R}|
 \ll_\varepsilon X^\varepsilon
 A\sqrt G\sqrt J D^{3/2}
 \asymp X^\varepsilon L^2\sqrt\rho.                \tag{80.F}
\]

The factor \(1/R\) from ordinary metric density cancels the Abel factor
\(R\).  Formula (80.C) shows that one cannot declare the density absent
and estimate only centered discrepancy.  Estimate (80.F) closes only
the fixed transition \(\rho=O(1)\), already owned by the Round-79
positive-safe boundary; it closes no unbounded hard range.

The exact remaining one-count object is the coupled kernel

\[
\begin{aligned}
 \mathfrak Q_{A,D,K,G,R}
 ={}&\sum_{\substack{a,b\ \mathrm{residual}}}
 \sum_{g\in\mathcal G_{a,b}}\chi_4(ga)\chi_4(gb)
 \int_{gb/4}^{ga}A^\circ_{ga,gb}(x)
 e\!\left(-J(\sqrt{gb}-\sqrt{ga})\sqrt x\right)\\
 &\qquad\times
 \sum_{k}\omega(k)W_R(\Lambda/k)e(kx)\,dx,
\end{aligned}                                      \tag{80.G}
\]

with the square rays, exact nonsquare centers, and
\(AJD^3\ll L^3\) blocks removed exactly once.  Its density and nonzero
integer modes must be controlled jointly.  Extending the \(k\)-sum and
applying the adjoint Poisson formula returns the original discrete
cross-row energy, so it supplies no independent curvature saving.

## Hostile controls

The near-square Pell family has \(b=a+2\) and hence \(q=1\) identically;
there is no uniform alternation of the surviving primitive sign.  The
hostile report gives the explicit primitive nonsquare pair \((25,27)\)
and four strict modes on one odd-quotient product fiber.  Perfect-square
and fourth-power choices populate either nearest-integer parity in strict
metric windows.  These are route controls, not lower bounds for the
actual energy.

The Round-77 variation estimate cannot be transferred mechanically to
\(\mathfrak C^\circ\), since

\[
 \partial_g\mathfrak C^\circ(g)
 =e(-g\theta/2)
 \left(\partial_g\mathfrak B^\circ(g)
       -\pi i\theta\mathfrak B^\circ(g)\right).
\]

Phase-conjugating proxy coefficients show that coefficient-uniform or
variation-only closure is false, but no proxy is asserted to be the
actual symbol.  Empty and singleton intervals, both collars, floors,
stars, and all transitions remain fully owned in (80.A)--(80.G).

The hostile source audit finds no literal application of the classical
circle large sieve, Heath-Brown's real-character mean value theorem, or
DFI bilinear Kloosterman-fraction estimates to (80.G).  Weyl's theorem is
used only for the qualitative perfect-power recurrence control, not for
the bound.

## Rejected shortcuts and first survivor

The following routes are rejected.

1. Nearest-integer quotient parity survives the complete coefficient.
2. Odd lifts create a half-integer Fourier gap which removes density.
3. A theorem for the nonzero metric Fourier modes implies the full
   strict-metric estimate.
4. Step-two variation of \(\mathfrak B^\circ\) transfers unchanged to
   the decentered coefficient.
5. Product-fiber re-enumeration or adjoint Poisson gives a second saving.
6. The remaining \((-1)^q\) sign is new arithmetic information beyond
   the original \(\chi_4(h)\chi_4(s)\) correlation.

The first unproved object is (80.G), or an equivalent one-count signed
cross-row correlation which estimates its density and discrepancy modes
together.  A future proof must exploit structure of the complete
two-character actual symbol across distinct rows.  Another positive
incidence classification, quotient-parity count, or reciprocal transform
cannot close it.

## Downstream scope

Round 80 is a useful exact falsification of the planned Gate-III parity
mechanism, but it proves no new polynomial \(L\)-range and no energy
estimate.  The transposed-energy reduction remains valid; its residual
hard part remains open.

There is no status change for `M9-M2-top-endpoint-signed-cone`,
\(M9\!-!M2\), \(M9\!-!M1\), \(M9\), endpoint uniformity,
`R5-Full`, or the Gauss-circle exponent.
