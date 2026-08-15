# Blind rederivation: moving-amplitude near-product energy

## 1. Result

**No-go result for the identity as stated.**  The quarter-shift algebra, the odd dual index, the Gaussian phase, the \(dm=2xt\,dt\) Jacobian, the exact identity \(W(\sqrt{q_X}/(2t_0))=W(l/y)\), and the resulting *leading* coefficient

\[
e(1/8)L^{3/2}X^{-1/4}
\]

are correct.  The hard boundary strips also have the claimed \(O(L^{3/2})\) absolute capacity under the implicit bounded-weight hypothesis.

The complete moving-amplitude identity (75.7), however, is not an exact consequence of (75.6).  After \(m=xt^2\), the angular amplitude contains at least the nonconstant factor \(t^{-1/2}\), in addition to \(W(\sqrt{q_X}/(2t))\) and the true additive collars.  Integrating this amplitude against the quadratic Gaussian produces nonzero algebraic stationary-phase corrections.  Evaluating the symbol only at \(t_0\), as stipulated before (75.8), omits those corrections, so the remainder cannot in general be \(O_A(L^{3/2}X^{-A})\) for every \(A\).  One can make an exact identity only by replacing the evaluated symbol by the full Fresnel transform (or by retaining the complete stationary expansion); the symbol estimates in (75.15) would then have to be proved anew.

Independently, (75.15) does not imply the signed energy bound (75.16).  Its diagonal is of size \(LJX^\varepsilon\), but its off-diagonal remains an unproved correlation of the actual coupled symbol.  The infinite character comb has the correct signs and density, while the asserted finite, margin-sensitive self-return is not established.  Thus the leading near-product normal form survives, but neither the claimed complete identity nor the actual-symbol off-diagonal bound is validated.

A separate statement-only replacement does survive: regrouping the original finite \(\mathcal T_L\) by \(m\) and applying Cauchy gives an exact transposed energy \(\mathcal E_L\).  Its character product is exactly \((-1)^r\) at offset \(2r\), its diagonal is \(O(L^2)\), and \(\mathcal E_L\ll_\varepsilon L^2X^\varepsilon\) is sufficient for (75.2).  This finite lemma is independent of, and promotable despite, the rejection of (75.7).

## 2. Exact statement and hypotheses

Let \(e(z)=e^{2\pi iz}\), \(J=\sqrt X\), \(y=\lfloor J\rfloor\), \(q_X=X/y^2\), and let \(1\le L\le H\) be as in the packet.  Assume only for the local calculation that the interior extensions are \(C^\infty_c\), the displayed weights are bounded, and a contributing stationary point \(t_0=J/(2l)\) is separated from the angular support boundary.  Write \(R_{\tau,x}(t)\) for all angular, collar, layer, and wavelet factors after the change \(m=xt^2\), except for the algebraic factor \(t^{-1/2}\), and put

\[
g_{\tau,x}(t)=t^{-1/2}R_{\tau,x}(t),\qquad \lambda=xl.
\]

If \(\mathcal K_{\tau,l}\) in (75.8) is formed by replacing \(g_{\tau,x}(t)\) with its value at \(t_0\), then uniformly on an interior branch

\[
\int g_{\tau,x}(t)e\!\left(-xl(t-t_0)^2\right)dt
=\frac{e(-1/8)}{\sqrt{2xl}}
\left(g_{\tau,x}(t_0)+
\frac{g_{\tau,x}''(t_0)}{8\pi i\,xl}
+O\!\left((xl)^{-2}\mathcal M_4(g_{\tau,x})\right)\right),
\tag{R75.1}
\]

with the usual finite seminorm \(\mathcal M_4\) after a local stationary/nonstationary decomposition.  Consequently, the evaluated-symbol formula (75.7) can have a remainder \(O_A(L^{3/2}X^{-A})\) for every \(A\) only if all of the omitted even-derivative contributions cancel after the complete summation.  No such cancellation is among the hypotheses.  It is false uniformly for the unspecified smooth weights: on a flat collar/layer with \(W\) constant near \(t_0\),

\[
g_{\tau,x}''(t_0)=\frac34t_0^{-5/2}R_{\tau,x}(t_0)\ne0.
\]

For a concrete nonoscillatory branch, take \(J=15r\), \(X=225r^2\), \(r\) odd, \(j=25r\), and \(l=9r\).  Then \(j\) is odd, \(J<j<2J\), \(J/2<l<J\), \(jl=X\), \(q_X=1\), and \(t_0=5/6\), well inside the cone.  With a smooth weight nonzero and flat near \(l/y=3/5\), (R75.1) has a nonzero correction of relative size \(1/(LJ)\) on \(x\asymp L\), rather than a super-polynomial error.  Since the packet specifies no narrower class of \(W\) or collars, this is a counterexample to the universal literal formulation and, at minimum, prevents validation for the hidden actual symbol.

There is also a separate logical obstruction to deriving (75.16) from (75.15).  On any set \(I\) of \(N\asymp J\) odd \(j\)'s, take one layer and

\[
b_{j,0}=\chi_4(j),\qquad b_{j,k}=0\quad(k\ne0).
\]

These coefficients satisfy both bounds in (75.15) (indeed their total square mass is \(N\ll LJ\)), but \(S_0=N\), so the energy is \(N^2\asymp J^2\), which exceeds \(LJX^\varepsilon\) throughout \(L\le J^{1/2}\) for a fixed sufficiently small \(\varepsilon\) and large \(J\).  This does not refute a possible bound for the *actual* symbol; it proves that an additional actual-symbol cancellation theorem is indispensable.

## 3. Proof or derivation

The character decomposition has the coefficient

\[
\chi_4(h)=\sum_{\rho=\pm1}\frac{\rho}{2i}e(\rho h/4).
\]

For a Poisson frequency pair \((u,l)\), put \(m=xt^2\).  Then

\[
dm=2xt\,dt,
\qquad
\left(\frac{L^2}{xm}\right)^{3/4}dm
=2L^{3/2}x^{-1/2}t^{-1/2}dt,
\tag{R75.2}
\]

and the phase is

\[
x\left(Jt+\frac\rho4-u-lt^2\right).
\]

With \(t_0=J/(2l)\) and \(j=4u-\rho\),

\[
Jt+\frac\rho4-u-lt^2
=\frac{X-jl}{4l}-l(t-t_0)^2.
\tag{R75.3}
\]

The index \(j\) is odd and \(\chi_4(j)=-\rho\).  Moreover

\[
\frac{\sqrt{q_X}}{2t_0}
=\frac{J/y}{J/l}=\frac ly,
\tag{R75.4}
\]

so no replacement \(q_X=1\) is involved.  Applying only the leading term of (R75.1), the complete quarter-shift, Gaussian, and Jacobian coefficient is

\[
\frac{\rho}{2i}\,2\,
\frac{e(-1/8)}{\sqrt{2l}}t_0^{-1/2}
=\frac{\rho}{i}e(-1/8)J^{-1/2}
=\chi_4(j)e(1/8)J^{-1/2}.
\tag{R75.5}
\]

The remaining \(x^{-1}dx\) becomes \(z^{-1}dz\) under \(x=Lz\), and the radial phase becomes

\[
e\!\left(z\frac{L(X-jl)}{4l}\right).
\]

This proves the normalization and sign in the leading version of (75.7)-(75.10).

Formula (R75.1) follows by Taylor expansion at \(t_0\).  If

\[
I_0(\lambda)=\int_{\mathbb R}e(-\lambda v^2)dv
=\frac{e(-1/8)}{\sqrt{2\lambda}},
\]

then differentiation gives

\[
\int_{\mathbb R}v^2e(-\lambda v^2)dv
=\frac{e(-1/8)}{4\pi i\sqrt2}\lambda^{-3/2}.
\]

Multiplication by the Taylor coefficient \(g''(t_0)/2\) yields exactly the second term in (R75.1).  Thus exact quadraticity of the phase removes higher phase derivatives; it does not remove derivatives of the moving amplitude.

An exact replacement for the evaluated symbol is possible.  If the whole wavelet is absorbed into the symbol, define, up to the already displayed radial factors,

\[
\kappa^{\mathrm{ex}}_{\tau,l}(z)
=e(1/8)\sqrt{LJ}\,z^{-1/2}
\int t^{-1/2}R_{\tau,Lz}(t)
e\!\left(-Lzl(t-t_0)^2\right)dt.
\tag{R75.6}
\]

Then the branch is exactly \(e(1/8)L^{3/2}J^{-1/2}\) times the radial Fourier transform of (R75.6).  Its leading term is the evaluated symbol \(z^{-1}R_{\tau,Lz}(t_0)\).  However, (R75.6) includes the off-stationary values of \(W\); retaining a separate factor \(W(l/y)\) as in (75.10) requires division by that value and is not uniform at its zeros.  More importantly, the \(z\)- and \(l\)-derivative estimates, collar behavior, \(k\)-decay, and square-mass estimate for this exact Fresnel symbol are not supplied by the packet.

Conditional on a genuinely smooth compactly supported \(F_{\tau,j}\), (75.13) is an exact definition and one-dimensional Poisson gives

\[
\sum_{l\in\mathbb Z}F_{\tau,j}(l)
=\sum_{k\in\mathbb Z}\widehat F_{\tau,j}(k),
\qquad
\widehat F_{\tau,j}(k)=L^{-1}b_{\tau,j,k}e(-kX/j).
\tag{R75.7}
\]

There is no missing measure factor in (R75.7).  If \(B_{j,k}=\sum_\tau b_{\tau,j,k}\), the energy expands exactly as

\[
\sum_k|S_k|^2
=\sum_{k,j,j'}\chi_4(j)\chi_4(j')
B_{j,k}\overline{B_{j',k}}
e\!\left(-kX\left(\frac1j-\frac1{j'}\right)\right).
\tag{R75.8}
\]

The \(j=j'\) portion is at most \(O(\log L)\sum_{\tau,j,k}|b_{\tau,j,k}|^2\), hence has the desired size if (75.15) is assumed.  Nothing in (75.15) bounds the \(j\ne j'\) part.  Equivalently, since \(b_{\tau,j,k}e(-kX/j)=L\widehat F_{\tau,j}(k)\), with \(G(\lambda)=\sum_{\tau,j}\chi_4(j)F_{\tau,j}(\lambda)\), periodic Parseval gives

\[
\sum_k|S_k|^2
=L^2\sum_k|\widehat G(k)|^2
=L^2\int_0^1\left|\sum_{n\in\mathbb Z}G(\theta+n)\right|^2d\theta.
\tag{R75.9}
\]

This identity exposes the unresolved aliases between packets centered near \(X/j\); it is not a diagonal Parseval identity unless their periodizations are proved almost orthogonal.

Finally, the infinite character comb itself is correct.  After the scaling used by the radial transform it reads

\[
\sum_{j\in\mathbb Z}\chi_4(j)e(-jLz/4)
=\frac{2}{iL}\sum_{\substack{h\in\mathbb Z\\h\ \mathrm{odd}}}
\chi_4(h)\,\delta(z-h/L).
\tag{R75.10}
\]

Both quarter lattices, the signs, and the density \(4/L\) are present.  The dual sum in (75.9), however, is finite and carries \(j\)-dependent margins and an \(l\)-dependent symbol.  Replacing it by (R75.10), discarding the complementary \(j\)'s, and recovering the exact collars all require estimates not stated in the packet.  Moreover, an evaluated stationary symbol cannot be the exact inverse of the original moving-amplitude transform.

### Statement-only addendum: exact \(m\)-transposed energy

Let \(\mathscr H_L\) be the exact finite set of odd \(h\)'s occurring in (75.2), and define

\[
\mathscr M_L
=\bigcup_{h\in\mathscr H_L}
\{\lceil h/4\rceil,\lceil h/4\rceil+1,\ldots,h\}.
\]

Since \(h\asymp L\), one has \(\#\mathscr M_L\ll L\).  For integer \(m\),

\[
\lceil h/4\rceil\le m\le h
\quad\Longleftrightarrow\quad
m\le h\le4m.
\]

Thus the original finite sum, with no smoothing, extension, or endpoint loss, is

\[
\mathcal T_L=\sum_{m\in\mathscr M_L}A_m,
\qquad
A_m=
\sum_{\substack{h\in\mathscr H_L\\m\le h\le4m}}
\chi_4(h)a(h,m)e(J\sqrt{hm}).
\tag{R75.11}
\]

Cauchy in the \(m\)-variable gives

\[
|\mathcal T_L|^2
\le \#\mathscr M_L\,\mathcal E_L
\ll L\mathcal E_L,
\qquad
\mathcal E_L:=\sum_{m\in\mathscr M_L}|A_m|^2.
\tag{R75.12}
\]

Expanding the square and writing the second odd index as \(h+2r\) gives the exact all-offset identity

\[
\begin{aligned}
\mathcal E_L
={}&\sum_{r\in\mathbb Z}(-1)^r
\sum_{\substack{h\in\mathscr H_L\\h+2r\in\mathscr H_L}}
\sum_{m=\left\lceil\max(h,h+2r)/4\right\rceil}^{\min(h,h+2r)}
a(h,m)\overline{a(h+2r,m)}
\\
&\hspace{35mm}\times
e\!\left(J\sqrt m\,
\bigl(\sqrt h-\sqrt{h+2r}\bigr)\right).
\end{aligned}
\tag{R75.13}
\]

Here an inner sum is empty when its lower endpoint exceeds its upper endpoint.  The sign is exact because, for every odd \(h\) and integer \(r\),

\[
\chi_4(h)\chi_4(h+2r)=(-1)^r.
\tag{R75.14}
\]

Pairing the \(r\) and \(-r\) terms displays the diagonal and positive offsets:

\[
\begin{aligned}
\mathcal E_L
={}&\mathcal E_{L,\mathrm{diag}}
+2\Re\sum_{r\ge1}(-1)^r
\sum_{\substack{h,h+2r\in\mathscr H_L}}
\sum_{m=\lceil(h+2r)/4\rceil}^{h}
a(h,m)\overline{a(h+2r,m)}
\\
&\hspace{27mm}\times
e\!\left(
-\frac{2rJ\sqrt m}{\sqrt h+\sqrt{h+2r}}
\right),
\end{aligned}
\tag{R75.15}
\]

where

\[
\mathcal E_{L,\mathrm{diag}}
=\sum_{h\in\mathscr H_L}
\sum_{m=\lceil h/4\rceil}^{h}|a(h,m)|^2.
\tag{R75.16}
\]

The exact positive-offset endpoint conditions are

\[
h,h+2r\in\mathscr H_L,\qquad
1\le r\le\left\lfloor\frac{3h}{2}\right\rfloor,\qquad
\left\lceil\frac{h+2r}{4}\right\rceil\le m\le h;
\tag{R75.17}
\]

the bound on \(r\) is precisely the nonemptiness condition for the \(m\)-interval.  On this cone \(h\asymp L\) and \(h/4\le m\le h\), so the algebraic factor in (75.1) is \(O(1)\).  Under the same implicit bounded-weight hypothesis used for the hard collars, \(a(h,m)=O(1)\).  There are \(O(L^2)\) admissible pairs, and hence

\[
\mathcal E_{L,\mathrm{diag}}\ll L^2.
\tag{R75.18}
\]

Finally, (R75.12) shows that

\[
\boxed{\ \mathcal E_L\ll_\varepsilon L^2X^\varepsilon\ }
\quad\Longrightarrow\quad
\mathcal T_L\ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{R75.19}
\]

This is an exact finite regrouping followed by one explicit Cauchy inequality.  It does not use the candidate collars, two-dimensional Poisson, stationary phase, the moving dual symbol, or character self-return.  Therefore (R75.11)-(R75.19) are promotable as a self-contained reduction lemma, while the estimate in the box remains a new open obligation rather than a proved bound.

## 4. First doubtful or unproved step

After the conditionally valid collar decomposition and two-dimensional Poisson formula, the first substantive failure is the use of the scalar Gaussian integral (75.6) as though the angular amplitude were constant.  The phase is exactly quadratic, but the measure and symbol are not: \(t^{-1/2}W(\sqrt{q_X}/(2t))\) and the additive collars move with \(t\).  Equation (R75.1) shows the first omitted term explicitly.  Therefore “evaluate the complete symbol at \(t_0\)” and “error \(O_A(X^{-A})\)” cannot both be true without a new all-orders cancellation argument.  No later use of Poisson or Parseval repairs this loss of information.

## 5. Control tests and outcomes

| Required control | Outcome | Audit |
|---|---|---|
| External normalization and conjugate ownership | Not auditable | The packet states the factor \(-2\pi^{-1}e(1/8)X^{1/4}L^{-3/2}\) but gives no antecedent from which to derive it.  The negative frequency is the conjugate only when the primal amplitude is real, also not stated.  The *internal* factor (R75.5) is correct and must not be counted twice. |
| `hard_and_flat_boundary_collars` | Partial pass | For \(h\asymp L\), each strip has at most \(2B+O(1)\) values of \(m\); the ceiling changes this by at most one.  With bounded weights, their union is \(O(LB)=O(L^{3/2})\) absolutely.  A valid smooth lower collar must depend on \(x(t^2-1/4)/B\), and the upper one on \(x(1-t^2)/B\).  No actual collar functions, flat upper profile, or one-count partition is supplied, so exact reconstruction and summed derivative costs cannot be checked. |
| Actual \(q_X\), upper edge, and layers | Partial pass | The stationary identity (R75.4) is exact for \(q_X=X/y^2\).  The \(O(\log L)\) layer count is harmless only after a partition-of-unity and uniform seminorm lemma; neither is stated.  Terminal \(L\asymp H\) is merely declared inherited safe. |
| `quarter_shift_and_Gaussian_constant` and `Poisson_measure` | Pass for the leading term | Equations (R75.2)-(R75.5) verify the odd \(j\), \(\chi_4(j)=-\rho\), Gaussian \(e(-1/8)/\sqrt{2xl}\), the Jacobian, and the resulting \(e(1/8)\chi_4(j)\).  Two-dimensional Poisson itself remains conditional on the unspecified smooth compact extensions. |
| `moving_l_symbol` | Fail in the literal formulation | Evaluation at \(t_0\) drops the nonzero term in (R75.1).  The exact symbol must be a full Fresnel symbol such as (R75.6), with the full wavelet absorbed, and is more strongly dependent on \(l,z,L,J\) than (75.8) records. |
| `alias_and_layer_errors` | Unproved | Smooth radial decay would imply (75.11) only from uniform \(z\)-seminorms.  The packet provides none for the actual moving symbol.  The omitted stationary corrections are algebraic, so they cannot be included in the asserted \(O_A(L^{3/2}X^{-A})\) alias/layer error. |
| Exact Poisson definition and \(k\)-tail | Conditional pass | Equation (75.13) may always define \(b\), and (R75.7) has the correct \(1/L\).  Decay on the scale \(\lvert k\rvert/L\) requires uniform smoothness of the rescaled \(l\)-packet, including all \(l\)-derivatives of the moving symbol and zero-extension margins; this is not proved. |
| `Parseval_diagonal` | Conditional pass | Given (75.15), the \(j=j'\) contribution is \(\ll LJX^\varepsilon\), with the \(O(\log L)\) layer loss absorbed.  The second assertion of (75.15) itself is not a consequence of the displayed definitions.  It would follow from a separate uniform width-\(1/L\), bounded-overlap lemma for the exact \(F_{\tau,j}\). |
| `signed_offdiagonal` | Fail / open | Formula (R75.8) is the exact survivor.  The explicit adversarial array in Section 2 satisfies (75.15) and violates (75.16), so only the detailed coupled symbol could close it.  No such estimate is present. |
| `character_self_return` | Partial pass only for the infinite comb | Equation (R75.10) verifies both quarter lattices, signs, and density.  Finite \(j\asymp J\), layer margins, collar images, and omitted-index errors prevent the asserted exact self-return.  With the evaluated rather than exact Fresnel symbol, exact inversion is impossible. |
| `perfect_powers_and_adversarial_weights` | Capacity checks pass; they do not close energy | If \(hm\) is a square, write \(h=dr^2,m=ds^2\) with \(d\) squarefree; the count in a dyadic \(L\)-box is \(O(L\log L)=O_\varepsilon(L^{1+\varepsilon})\), and fourth powers are no worse.  Exact \(jl=X\) is absent for nonintegral \(X\) and divisor-bounded for integral \(X\).  For \(X=R^4\), \(j=J+s,l=J-s\) gives \(X-jl=s^2\), hence \(O(\sqrt{J/L}\,X^\varepsilon)\) points in (75.11).  These sparse sets do not control the general periodized correlations in (R75.9); adversarial coefficients give the stated obstruction. |
| Exact finite \(m\)-transposition | Pass / promotable | Equations (R75.11)-(R75.19) preserve the ceiling, both endpoint inequalities, and the character.  The diagonal is \(O(L^2)\), and the boxed transposed-energy bound is sufficient for (75.2).  This lemma does not depend on (75.7). |
| `downstream_scope` | Pass as a stopping control | Even a corrected identity plus (75.16) would address only the exact top-\(M2\) cone.  Nothing here promotes smooth packets, \(M1\), full \(M2\), \(M9\), or the global exponent. |

## 6. Dependencies and exact artifacts used

- `rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/briefs/blind_near_product_energy_rederivation.md`
- `rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/derivation_packet.md`

No other repository artifact, source card, literature source, or numerical computation was used.

## 7. Recommended state effect

**Revise the near-product candidate and promote only the exact finite transposition lemma.**  Retain the hard-collar capacity calculation, the exact \(q_X\) substitution, the leading quarter-shift/Gaussian/Jacobian normalization, and the formal one-dimensional Poisson interface only as candidate lemmas.  Replace the evaluated wavelet by an exact Fresnel symbol such as (R75.6), or explicitly retain and bound enough stationary corrections; then prove uniform collar/layer seminorms, the actual version of (75.15), finite-comb error bounds, and a genuinely signed off-diagonal estimate.  Equations (R75.11)-(R75.19), by contrast, are an exact finite identity and Cauchy reduction and may be promoted independently; their boxed energy estimate is not proved.  The near-product identity (75.7), complete self-return, dual energy (75.16), and every downstream claim should remain unpromoted.
