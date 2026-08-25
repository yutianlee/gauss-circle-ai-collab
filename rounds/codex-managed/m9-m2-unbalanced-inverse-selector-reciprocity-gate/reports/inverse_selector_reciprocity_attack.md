# Round 160 discovery report: exact reciprocity kernel and canonical projective-capacity obstruction

Campaign: `m9-m2-unbalanced-inverse-selector-reciprocity-gate`

Task: `inverse_selector_reciprocity_attack`

Role: discovery

Generated at: 2026-08-25T18:38:23+08:00

Starting graph SHA-256: `4ad56f62aeb814c11c31fe655bc48da6d74639e3bd61077e9496d647c366c41d`

## 1. Result: an exact unweighted projective obstruction, not a weighted or vector-valued no-go

The exact additive-reciprocity insertion gives the literal centered scalar

\[
\begin{aligned}
\mathscr R_{D,L}^{\circ}(X)
={}&\sum_{\substack{g,n\ {\rm odd}\\gn\asymp R}}
 \sum_{\substack{j\in\mathcal J_{g,n}\\(j,n)=1}}
 \sum_{1\le h<n}
 \frac{\chi _4(g)}{gjn}
 W\!\left(\frac{X}{gnD}\right)
 q_L\!\left(\frac{4Xj}{gn^2}\right)                                      \\
&\qquad\qquad\times
 e\!\left(\frac{\xi j}{n}\right)
 e\!\left(\frac{h\overline n_j}{j}-\frac{h}{jn}\right)
 S^{\chi _4}_{\infty0}(4N_0,h;2n).
\end{aligned}
\tag{160.D1}
\]

No positive modulus norm has been taken in (160.D1).  Equivalently, the
last factor may be replaced by
\(\chi _4(n)S(N_0,h;n)\), leaving both character directions
\(\chi _4(g)\chi _4(n)\) visible.

The proposed low-projective-cost scalarization fails already for the exact
unweighted inverse kernel.  For every integer \(j>1\), put

\[
 U_j=(\mathbb Z/j\mathbb Z)^\times,
 \qquad
 F_j(a,s)=e\!\left(\frac{s\overline a_j}{j}\right),
 \quad a\in U_j,\quad 1\le s<j.
\tag{160.D2}
\]

Then

\[
 F_jF_j^*=jI_{\varphi(j)}-\mathbf 1\mathbf 1^*,
\tag{160.D3}
\]

so the singular values are

\[
 \sqrt j\quad(\varphi(j)-1\text{ times}),
 \qquad
 \sqrt{j-\varphi(j)}\quad(1\text{ time}).
\tag{160.D4}
\]

Consequently the least Hilbert-projective cost of separating the
\(h\bmod j\) and \(n\bmod j\) variables is exactly

\[
 \|F_j\|_*
 =\bigl(\varphi(j)-1\bigr)\sqrt j+\sqrt{j-\varphi(j)},
\tag{160.D5}
\]

whereas

\[
 \|F_j\|_{\rm HS}=\sqrt{\varphi(j)(j-1)}.
\tag{160.D6}
\]

Thus scalar common-test separation has nuclear/HS inflation
\(\asymp\sqrt{\varphi(j)}=j^{1/2-o(1)}\).  The first complete nonzero
\(h\)-residue block \(1\le h<j\) is contained in the full range
\(1\le h<n\), because \(n/j\asymp\Delta=X^{\delta-\ell}\to\infty\).
Coordinate restriction is contractive for the projective norm: restricting
any factorization of the full phase to this block gives a factorization of
\(F_j\) with no larger cost.  Hence (160.D5) is a lower bound for every
exact projective factorization of the full **unweighted** reciprocity
phase.

At the primitive stratum \(g=1\), \(j\asymp K\), so the omitted
projective factor has power scale

\[
 K^{1/2-o(1)}=X^{(1-\delta-a)/2-o(1)},
 \qquad a=\delta-\ell.
\tag{160.D7}
\]

The main exponent strictly dominates the missing target factor throughout
every fixed strict point of the frozen polytope (so the \(o(1)\) is
absorbed inside the displayed strict margins):

\[
\frac{1-\delta-a}{2}-\left(a-\frac14\right)
=\frac{3-2\delta-6a}{4}>0,
\qquad \frac14<a\le\frac13,
\tag{160.D8}
\]

and

\[
\frac{1-\delta-a}{2}-\frac{1-2a}{4}
=\frac{1-2\delta}{4}>0,
\qquad \frac13\le a<\frac12.
\tag{160.D9}
\]

At \(a=1/3\), the main exponent in (160.D7) is
\(1/3-\delta/2\), larger than \(1/12\) by
\((1-2\delta)/4\).  This proves the exit label

\[
 \boxed{\mathsf{inverse\_selector\_projective\_capacity\_no\_go}}
\]

for the canonical scalar-common-test route: a decomposition charged only
\(X^\varepsilon\) projective cost omits at least the whole power it was
supposed to save.  It does **not** prove a lower bound for the literal
signed scalar, does not exclude a scalar theorem with an additional
larger saving, and does not exclude a bespoke vector-valued theorem that
keeps the whole kernel, Kloosterman family, and \(\chi _4\) together.

There is one further essential qualification.  The exact theorem above is
unweighted.  The supplied context gives upper profile estimates and exact
moving support, but no pointwise lower bound for
\(q_L(4Xj/(gn^2))W(X/(gnD))\).  Hence (160.D5) may not be promoted as a
lower bound for the literal weighted coefficient matrix.  It is stable on
any buffered interior cell on which the literal weight is bounded above
and below, as proved below, but existence of such a nonvanishing cell is
an additional hypothesis not supplied to this task.

## 2. Exact statement and hypotheses

Let

\[
 X=N_0+\xi,\quad 0\le\xi<1,\quad
 D=X^\delta,\quad L=X^\ell,\quad
 R=\frac XD,\quad K=\frac{XL}{D^2},\quad
 \Delta=\frac RK=\frac DL,
\tag{160.D10}
\]

under

\[
 \frac14\le\delta<\frac12,
 \qquad 0\le\ell<\delta-\frac14,
 \qquad 178\ell+1638\delta>463.
\tag{160.D11}
\]

Write

\[
 N_g=\frac Rg,\qquad J_g=\frac Kg,\qquad
 \frac{N_g}{J_g}=\Delta.
\tag{160.D12}
\]

The literal support has \(n\asymp N_g\), \(j\asymp J_g\), with
\(g,n\) odd, arbitrary parity of \(j\), and \((j,n)=1\).  All statements
below use the zero-extended literal support; no endpoint is silently
filled.

The exact scoped obstruction consists of the following assertions.

1.  Formula (160.D1) holds for every choice of inverse representatives,
    every even or odd \(j\), every \((N_0,n)\), and every
    \(1\le h<n\).

2.  For fixed \(g,j,h\), exact residue splitting is

    \[
    \sum_{a\in U_j}e\!\left(\frac{h\overline a_j}{j}\right)
    \sum_{\substack{n\ {\rm odd}\\n\equiv a\ (j)}}
    \Omega_{g,j,h}(n),
    \tag{160.D13}
    \]

    where \(\Omega_{g,j,h}\) contains the literal zero-extended support,
    the factors in (160.D1) other than
    \(e(h\overline n_j/j)\), and the condition \(h<n\).  Thus there are
    exactly \(\varphi(j)\) possible unit classes.

3.  Put

    \[
    \lambda_j=\operatorname{lcm}(2,j)
    =\begin{cases}j,&2\mid j,\\2j,&2\nmid j.\end{cases}
    \tag{160.D14}
    \]

    For every interval of integers \(I\) and every \(a\in U_j\), the
    simultaneous conditions \(n\) odd and \(n\equiv a\pmod j\) define
    one class modulo \(\lambda_j\), and

    \[
    \#\{n\in I:n\ {\rm odd},\ n\equiv a\ (j)\}
    =\frac{|I|}{\lambda_j}+O(1).
    \tag{160.D15}
    \]

    Hence an interior support interval of length \(\asymp N_g\) contains
    \(\asymp\Delta\) points per class (\(\asymp\Delta/2\) when \(j\)
    is odd) and has an aggregate \(O(\varphi(j))\) endpoint discrepancy.

4.  The projective spectrum is exactly (160.D3)--(160.D6).  In
    particular, if

    \[
    F_j(a,s)=\sum_\nu u_\nu(a)v_\nu(s),
    \tag{160.D16}
    \]

    then

    \[
    \sum_\nu\|u_\nu\|_2\|v_\nu\|_2
    \ge \bigl(\varphi(j)-1\bigr)\sqrt j+\sqrt{j-\varphi(j)}.
    \tag{160.D17}
    \]

5.  The exact additive common-test expansion, valid also at nonunits, is

    \[
    \boxed{
    \mathbf 1_{(n,j)=1}e\!\left(\frac{h\overline n_j}{j}\right)
    =\frac1j\sum_{t\bmod j}S(h,-t;j)e\!\left(\frac{tn}{j}\right),}
    \tag{160.D18}
    \]

    with

    \[
    S(h,-t;j)=\sum_{x\bmod j}^{*}
       e\!\left(\frac{h\overline x_j-tx}{j}\right).
    \tag{160.D19}
    \]

    For the complete block \(1\le h<j\), a fixed positive fraction of
    the coefficient \(\ell^2\)-mass in (160.D18) lies at centered
    frequencies \(|t|\ge j/4\).  On a modulus interval \(n\asymp N_g\),
    these modes have logarithmic Sobolev frequency
    \(|t|N_g/j\gg N_g\), not \(O(1)\).

6.  Conditionally, suppose a fixed \((g,j)\) support cell contains one
    complete parity block of length \(\lambda_j\) and satisfies

    \[
    0<c_0\le
    \left|q_L\!\left(\frac{4Xj}{gn^2}\right)
    W\!\left(\frac{X}{gnD}\right)\right|
    \le C_0
    \tag{160.D20}
    \]

    there.  Choosing one representative \(n_a\) for each \(a\in U_j\),
    multiplication by the literal smooth row weights preserves
    (160.D5) up to constants and an \(O(N_g^{-1})\) relative perturbation
    from \(e(-s/(jn_a))\).  This conditional statement is a robustness
    lemma only; (160.D20) is not asserted for the supplied literal profile.

## 3. Proof and complete ledger

### 3.1 Reciprocity, representatives, parity, and the centered matrix

Choose arbitrary inverses \(\overline j_n\pmod n\) and
\(\overline n_j\pmod j\).  The integer

\[
 j\overline j_n+n\overline n_j
\]

is congruent to \(1\) modulo both \(j\) and \(n\), hence modulo \(jn\)
because \((j,n)=1\).  Therefore

\[
 \frac{\overline j_n}{n}+\frac{\overline n_j}{j}
 \equiv\frac1{jn}\pmod1
\tag{160.D21}
\]

and

\[
 e\!\left(-\frac{h\overline j_n}{n}\right)
 =e\!\left(\frac{h\overline n_j}{j}-\frac{h}{jn}\right).
\tag{160.D22}
\]

Changing either inverse representative alters the exponent by an integer.
No division by \(2\) was used, so (160.D22) holds unchanged for even
\(j\).  Substitution into the normalized inverse-residue Fourier
coefficient gives

\[
 \widehat\gamma_{g,n}(h)=\frac1n
 \sum_{\substack{j\in\mathcal J_{g,n}\\(j,n)=1}}
 \frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n)
 e\!\left(\frac{h\overline n_j}{j}-\frac{h}{jn}\right),
\tag{160.D23}
\]

and insertion into the already centered owner proves (160.D1).  The
index remains exactly \(1\le h<n\); the safe \(h=0\) row has not been
subtracted a second time.

Using the accepted arithmetic identity

\[
 S^{\chi _4}_{\infty0}(4N_0,h;2n)=\chi _4(n)S(N_0,h;n)
\tag{160.D24}
\]

shows explicitly that \(\chi _4(g)\) is outside and \(\chi _4(n)\) is
inside the modulus sum.  In particular, \(g=1\) has no outer character
cancellation.

### 3.2 Exact residue and long-frequency decomposition

Extend all weights by zero outside the literal moving support.  Since
\(\overline n_j=\overline a_j\) when \(n\equiv a\pmod j\), (160.D13)
is just a partition of the allowed \(n\)'s.  The parity claim follows from
the Chinese remainder theorem.  If \(j\) is even, every unit \(a\) is
odd and the period is \(j\).  If \(j\) is odd, exactly one of the two
lifts modulo \(2j\) is odd.  This proves (160.D14)--(160.D15) with an
exact floor count and an \(O(1)\) discrepancy per class.

Write

\[
 h=qj+s,\qquad 0\le s<j.
\tag{160.D25}
\]

Then the exact reciprocal phase is

\[
 e\!\left(\frac{s\overline a_j}{j}\right)
 e\!\left(-\frac qn-\frac{s}{jn}\right).
\tag{160.D26}
\]

The pair \((q,s)=(0,0)\) is absent, but all \(q\ge1,s=0\) multiples of
\(j\) remain.  There are \(\asymp N_g/j=\Delta\) complete or partial
blocks in the full range.  Thus reciprocity does not shorten the
\(h\)-sum: it makes the inverse part periodic in \(h\bmod j\), with a
long quotient of length \(\Delta\).

The inherited Linnik comparison range is

\[
 H_{\rm Lin}(g)\asymp\frac{K}{Lg^2}.
\tag{160.D27}
\]

Relative to one residue block,

\[
 \frac{H_{\rm Lin}(g)}{J_g}\asymp\frac1{Lg},
\tag{160.D28}
\]

while the full number of blocks is \(\Delta\).  Hence the scalar Linnik
range covers at most a constant part of the first block (one block only
when \(L\asymp g\asymp1\)) and leaves the remaining long complement.
The exact matrix obstruction below already occurs in the first complete
block; the rest cannot be deleted or inferred from it.

### 3.3 Exact projective spectrum

For \(a,b\in U_j\),

\[
\begin{aligned}
(F_jF_j^*)_{a,b}
&=\sum_{s=1}^{j-1}
e\!\left(\frac{s(\overline a_j-\overline b_j)}j\right)\\
&=\begin{cases}j-1,&a=b,\\-1,&a\ne b.\end{cases}
\end{aligned}
\tag{160.D29}
\]

The second line uses the complete additive-character sum and remains true
for composite and even \(j\).  Thus (160.D3) holds.  The all-ones vector
has eigenvalue \(j-\varphi(j)\), and its orthogonal complement has
eigenvalue \(j\).  This proves (160.D4)--(160.D6).  The equality between
the nuclear norm and the least value of
\(\sum_\nu\|u_\nu\|_2\|v_\nu\|_2\) proves (160.D17).

The same price appears in the multiplicative-character scalarization.  If
\(\widehat U_j\) is the full character group and

\[
 \tau_s(\psi;j)=\sum_{u\in U_j}\psi(u)e(su/j),
\tag{160.D30}
\]

then

\[
 e(s\overline a_j/j)
 =\frac1{\varphi(j)}
 \sum_{\psi\in\widehat U_j}\tau_s(\psi;j)\psi(a).
\tag{160.D31}
\]

Group Parseval gives
\(\sum_\psi|\tau_s(\psi;j)|^2=\varphi(j)^2\).  For a prime
\(j=p\) and \(1\le s<p\), the principal coefficient has magnitude
\(1\), every nonprincipal Gauss sum has magnitude \(\sqrt p\), and the
normalized coefficient \(\ell^1\)-cost is exactly

\[
 \frac{1+(p-2)\sqrt p}{p-1}\asymp\sqrt p.
\tag{160.D32}
\]

Thus the \(\sqrt j\) cost is not an artifact of using residue indicators.

### 3.4 Exact additive expansion and high Sobolev/Bessel bandwidth

Expanding the right side of (160.D18) and summing over \(t\) gives

\[
 \frac1j\sum_{x\bmod j}^{*}e(h\overline x_j/j)
 \sum_{t\bmod j}e(t(n-x)/j).
\tag{160.D33}
\]

The inner sum is \(j\) exactly when \(x\equiv n\pmod j\), and zero
otherwise.  This proves (160.D18), including its zero value at nonunits.

Let

\[
 \mathfrak c_j(t)=\sum_{x\bmod j}^{*}e(tx/j)
\tag{160.D34}
\]

be the Ramanujan sum.  Orthogonality in \(h\) gives, for every \(t\),

\[
 \sum_{h=1}^{j-1}|S(h,-t;j)|^2
 =j\varphi(j)-|\mathfrak c_j(t)|^2,
\tag{160.D35}
\]

and orthogonality in \(t\) gives

\[
 \sum_{t\bmod j}|\mathfrak c_j(t)|^2=j\varphi(j).
\tag{160.D36}
\]

Choose centered representatives and

\[
 \mathcal H_j=\{t\bmod j:j/4\le |t|\le j/2\}.
\tag{160.D37}
\]

For \(j\ge12\), its cardinality \(m_j\) satisfies
\(m_j-1\ge j/4\).  Therefore (160.D35)--(160.D36) imply, without a
Weil bound,

\[
\begin{aligned}
\sum_{t\in\mathcal H_j}\sum_{h=1}^{j-1}
\left|\frac{S(h,-t;j)}j\right|^2
&\ge \frac{m_jj\varphi(j)-j\varphi(j)}{j^2}\\
&\ge\frac14\varphi(j).
\end{aligned}
\tag{160.D38}
\]

The total coefficient mass is

\[
 \sum_{t\bmod j}\sum_{h=1}^{j-1}
 \left|\frac{S(h,-t;j)}j\right|^2
 =\frac{j-1}{j}\varphi(j).
\tag{160.D39}
\]

Thus a fixed fraction of the complete block lies at genuinely high
additive frequencies for every sufficiently large \(j\), including
composite and even \(j\).

For an order-\(\nu\) logarithmic modulus Sobolev ledger define

\[
 \mathfrak S_\nu(j,N_g)^2
 =\sum_{h=1}^{j-1}\sum_{t\bmod j}
 \left|\frac{S(h,-t;j)}j\right|^2
 \left(1+\frac{N_g|t|}{j}\right)^{2\nu}.
\tag{160.D40}
\]

Equations (160.D38)--(160.D39) give the exact phase-only prices

\[
 \mathfrak S_0(j,N_g)\asymp\sqrt{\varphi(j)},
 \qquad
 \mathfrak S_\nu(j,N_g)\gg_\nu
 N_g^\nu\sqrt{\varphi(j)}\quad(\nu>0).
\tag{160.D41}
\]

Indeed \(e(tn/j)\) has logarithmic derivative
\(n\partial_n=2\pi itn/j\), of size \(\gg N_g\) on
\(\mathcal H_j\).  In the level-\(4/8\) standard-cusp realization
\(C=4n\), the Bessel argument is proportional to \(C^{-1}\), so the
same modes carry this logarithmic bandwidth into the Bessel test.  The
audited scalar formula supplies no free compensation for (160.D41).
This is a Sobolev input-norm obstruction, not a claim about cancellation
inside an unaudited vector Bessel transform.

### 3.5 Moving weights, conditional robustness, and endpoint price

For fixed \(g,j\), the smooth row multiplier before the reciprocal phase
is

\[
 d_{g,j}(n)=\frac1{gjn}
 W\!\left(\frac{X}{gnD}\right)
 q_L\!\left(\frac{4Xj}{gn^2}\right)e(\xi j/n).
\tag{160.D42}
\]

On an interior normalized cell its logarithmic derivatives are \(O(1)\):
the real-centre phase costs \(j/n\asymp\Delta^{-1}\), while for all
\(1\le h<n\)

\[
 n\partial_n\!\left(-\frac{h}{jn}\right)
 =\frac{h}{jn}\ll\frac1j.
\tag{160.D43}
\]

For the first block \(1\le s<j\), the extra factor satisfies

\[
 e(-s/(jn))=1+O(N_g^{-1}).
\tag{160.D44}
\]

If (160.D20) holds on a parity block, choose one \(n_a\) in each unit
class and form

\[
 M_j(a,s)=d_{g,j}(n_a)F_j(a,s)e(-s/(jn_a)).
\tag{160.D45}
\]

Diagonal singular-value monotonicity and
\(\|E\|_*\le\sqrt{\operatorname{rank}E}\|E\|_{\rm HS}\) show

\[
 \|M_j\|_*
 \ge \bigl(\min_a|d_{g,j}(n_a)|\bigr)\|F_j\|_*
 -O\!\left(\frac{\max_a|d_{g,j}(n_a)|}{N_g}
             \varphi(j)\sqrt j\right).
\tag{160.D46}
\]

This proves the conditional robustness statement.

The zero extension and moving support do not create a free common test.
On each literal interval they give the exact \(O(1)\) discrepancy in
(160.D15), hence \(O(\varphi(j))\) boundary samples per fixed \(j\).
Exact interpolation of those discontinuous samples has the high-frequency
price exposed by (160.D38)--(160.D41).  They must either remain inside the
literal sequence or be bounded as separate endpoint pieces.  This report
does not assert they are target-safe.  More importantly, without the
lower bound (160.D20), diagonal weighting may delete enough rows that no
literal nuclear lower bound follows from (160.D5).

### 3.6 Restored coefficient powers

On a nonvanishing normalized cell, \(n\asymp N_g=R/g\) and
\(j\asymp J_g=K/g\), so

\[
 |d_{g,j}(n)|\asymp\frac1{gJ_gN_g}=\frac g{KR}.
\tag{160.D47}
\]

For one complete parity/residue block and
\(\varphi(j)=j^{1-o(1)}\), (160.D5)--(160.D6) give, before geometric
\(S/c\) normalization,

\[
 \|dF_j\|_{\rm HS}\asymp R^{-1}X^{o(1)},
 \qquad
 \|dF_j\|_*\asymp
 \frac{\sqrt{K/g}}{R}X^{o(1)}.
\tag{160.D48}
\]

The conditional cross-cusp sample multiplies by \(2n\), and the sourced
standard-cusp sample by \(4n\).  Fixed factors apart, both therefore have

\[
 \|B_{g,j}\|_{\rm HS}\asymp g^{-1}X^{o(1)},
 \qquad
 \|B_{g,j}\|_*\asymp
 \frac{\sqrt K}{g^{3/2}}X^{o(1)}.
\tag{160.D49}
\]

Their ratio is \(\sqrt{K/g}\), exactly the projective inflation.  These
are conditional weighted-cell norms, included only to restore the powers;
the unconditional claims are (160.D3)--(160.D6) and (160.D38)--(160.D41).

At \(g=1\), the outer character is \(1\), and

\[
 K=X^{1+\ell-2\delta}=X^{1-\delta-a}.
\tag{160.D50}
\]

Equations (160.D8)--(160.D9) compare its square-root projective price with
the complete boundary saving requirement.  The auxiliary inequality in
(160.D11) creates no improving chamber.  The comparison is strict at
every fixed strict point, but the margin in (160.D9) tends to zero as
\(\delta\to1/2\).  Therefore this report makes no endpoint-uniform claim.
At the seam \(a=1/3\), both required-saving formulas agree and the strict
margin is \((1-2\delta)/4\).  The limits \(a\to1/4\), \(a\to1/2\), and
the joint scale-collapse corner are not promoted to other owners.

### 3.7 Spectral and full-frequency ledgers

If one remains with the sourced Blomer--Milićević implementation, every
scalar test produced by (160.D13), (160.D18), or (160.D31) must pass
through both the level-\(4\) and level-\(8\) terms with the same test.
The full ledger remains:

- odd holomorphic weights \(k\ge3\);
- the complete weight-one Maaß spectrum, including exceptional parameters
  and \(t=0\) if present;
- Eisenstein integrals over \(\infty,0\) at level \(4\);
- Eisenstein integrals over \(\infty,0,1/2,1/4\) at level \(8\); and
- the level-\(4\) oldclasses inside level \(8\).

No one of these pieces removes the projective or Sobolev input price.
Alternatively, (160.D31) inserts a variable character \(\psi(n)\) of
conductor dividing \(j\) into the modulus twist \(\chi _4(n)\).  For odd
and even \(j\), including every two-adic conductor subclass, this lies
outside the audited fixed-\(\chi _4\), level-\(4/8\) identity.  The exact
new levels, cusps, oldclasses, and continuous spectra would require a new
source card or derivation; none is invoked here.  It is therefore invalid
to treat (160.D31) as a free common smooth test at levels \(4/8\).

Finally, full \(h\)-summation is exactly self-return.  From the normalized
definition and additive orthogonality,

\[
 \sum_{h\bmod n}\widehat\gamma_{g,n}(h)S(N_0,h;n)
 =\sum_{\substack{j\in\mathcal J_{g,n}\\(j,n)=1}}
 b_{g,n}(j)e(N_0j/n).
\tag{160.D51}
\]

Hence the centered sum is exactly

\[
\begin{aligned}
\sum_{h=1}^{n-1}\widehat\gamma_{g,n}(h)
S^{\chi _4}_{\infty0}(4N_0,h;2n)
=\chi _4(n)\biggl{&
\sum_{\substack{j\in\mathcal J_{g,n}\\(j,n)=1}}
b_{g,n}(j)e(N_0j/n)\\
&-\widehat\gamma_{g,n}(0)c_n(N_0)\biggr\}.
\end{aligned}
\tag{160.D52}
\]

The second term is the already accepted target-safe zero row.  Thus
adding it back reconstructs the original reciprocal row exactly and
offers no gain.  The inherited positive complete-frequency closure remains
\(R\sqrt\Delta=X^{1-(\delta+\ell)/2}\), worse than the accepted envelope;
this report does not reuse it as an estimate.

## 4. First doubtful or unproved step

The first unproved step in turning the exact kernel obstruction into a
claim about the **literal weighted owner** is (160.D20): the permitted
context supplies no pointwise lower profile hypothesis ensuring that, for
each relevant fixed \(j\) (or for a quantitatively sufficient signed set
of \(j\)'s), one complete parity block survives with comparable nonzero
weights.  Moving support is geometrically long because
\(N_g/j\asymp\Delta\to\infty\), but upper support and derivative bounds do
not imply the lower bound needed for a nuclear-norm restriction.  A weight
may vanish or become arbitrarily small on selected representatives.

Even if a later profile lemma supplies (160.D20), (160.D46) is only a
lower bound for positive scalar projective separation of the coefficient.
It is not a lower bound for
\(\mathscr R_{D,L}^{\circ}(X)\): the literal Kloosterman entries can
correlate with the inverse kernel, the \(j\)-sum can cancel, and a new
vector-valued trace theorem need not sum singular components absolutely.
The first analytic theorem still missing is therefore a signed
vector-valued estimate for the whole centered matrix, with the long
\(h\)-range, moving weights, both character directions, and full spectral
ledger.  No such theorem is proved or sourced here.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `exact_inverse_selector_reciprocity` | Pass: (160.D21)--(160.D23) give the exact sign and normalization. |
| `even_odd_j_and_representatives` | Pass: no parity division occurs; representative changes add integers.  Parity class modulus is exactly (160.D14). |
| `centered_h_nonzero_once` | Pass: (160.D1) retains exactly \(1\le h<n\); \(h=0\) is not removed again. |
| `full_h_self_return` | Pass: (160.D51)--(160.D52) reconstruct the original reciprocal row and the one safe zero correction. |
| `primitive_g1` | Pass: (160.D7)--(160.D9) use \(g=1\), where \(\chi _4(g)=1\), and absorb the totient \(X^{o(1)}\) only inside the strict power margin. |
| `chi4_before_positive_norm` | Pass: (160.D1), (160.D24), and (160.D52) retain both \(\chi _4(g)\) and \(\chi _4(n)\). |
| `moving_j_support_and_zero_extension` | Pass with caveat: exact zero extension is kept in (160.D13); (160.D15) prices endpoints; lack of a lower profile prevents a literal weighted lower bound. |
| `n_mod_j_class_price` | Pass: exactly \(\varphi(j)\) unit classes, period \(j\) for even \(j\) and \(2j\) for odd \(j\), with \(\asymp\Delta\) points per interior class. |
| `projective_Sobolev_Bessel_norms` | Pass for the canonical scalarization: exact nuclear price (160.D5), additive high-frequency mass (160.D38), and Sobolev price (160.D41).  No unaudited Bessel compensation is asserted. |
| `long_h_complement` | Pass: (160.D25)--(160.D28) retain \(\asymp\Delta\) residue blocks and locate the short Linnik range. |
| `level_four_eight_spectral_ledger` | Pass: all level-\(4/8\) H+M+E, singular-cusp, and oldclass pieces are retained; variable-\(\psi\) levels are explicitly left unproved. |
| `boundary_power_saving` | Pass: (160.D8)--(160.D9) compare the exact projective exponent with both envelope branches and the \(a=1/3\) seam; endpoint-uniformity is not claimed. |
| `flat_owner_and_downstream_scope` | Pass: only the one flat-smooth strict-UNBAL reciprocity/common-test mechanism is obstructed. |

The work was 100 percent analytical and algebraic.  No numerical
experiment, web source, arbitrary replacement of the literal scalar, or
unsigned-to-signed inference was used.

## 6. Dependencies and exact artifacts used

The report used exactly the selected context in the task brief:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/round160_m2_unbalanced_inverse_selector_reciprocity_strategy.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/candidates/conductor_round160_reciprocity_seed.md`;
- `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/candidates/conductor_round143_level_four_matrix_obstruction.md`;
- `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reviews/conductor_round143_level_four_matrix_adjudication.md`; and
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/synthesis.md`.

The accepted graph dependencies used mathematically are
`M9-M2-unbalanced-truncated-divisor-fixed-centre-return`,
`M9-M2-unbalanced-flat-wave-curvature-envelope`,
`M9-M2-unbalanced-Kloosterman-dispersion-interface-obstruction`,
`M9-M2-unbalanced-level-four-spectral-matrix-obstruction`, and
`M9-M2-character-factor`.  No sibling Round-160 report or excluded
artifact was read.

## 7. Recommended state effect

**Promote**, after the required independent and seam reviews, only the
route-scoped statement
`inverse_selector_projective_capacity_no_go`: the exact unweighted
reciprocity kernel has spectrum (160.D4), canonical scalar
common-test separation costs \(j^{1/2-o(1)}\), the additive realization
has the high Sobolev bandwidth (160.D41), the long \(h\)-range is not
shortened, and at \(g=1\) the omitted \(\sqrt K\) projective power is at
least the entire required boundary saving.

Do **not** promote (160.D48)--(160.D49) as literal weighted lower bounds
without a separately proved nonvanishing profile lemma.  Do not infer a
signed lower bound, a no-go for bespoke vector-valued trace methods, a
target theorem, an endpoint theorem, or any exponent improvement.  Retain
`M9-M2-smooth-unbalanced-three-quarter-estimate`, complete M9-M2,
endpoint uniformity, M9, the conditional bridge, and `GC-target` open.
The next possible attack would have to keep the full reciprocity kernel
inside a genuinely signed vector theorem, rather than scalarize it at a
positive projective norm.
