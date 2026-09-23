# Literal four-corner allocation-commutator attack

- Campaign: m9-m1-t1-p2-four-corner-allocation-commutator-gate
- Round: 197
- Task: literal_four_corner_allocation_commutator_attack
- Role: discovery
- Starting graph SHA-256:
  b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae
- Evidence status: candidate analytical evidence only
- Numerical theorem evidence: none

## 1. Result

The physical four-corner algebra is genuine, but the proposed full
four-corner sector is not proved target-safe by the selected context.
There are two separate conclusions.

First, write

\[
 g=(d,d'),\qquad d=g\alpha,\qquad d'=g\beta,\qquad
 (\alpha,\beta)=1.
\tag{1.1}
\]

Under

\[
 (m,\beta)=(\alpha,m')=(m,m')=1
\tag{1.2}
\]

the two endpoint allocation swaps recompute the gcd as \(g\) at all four
corners, commute, and preserve the endpoint products.  On

\[
 s_0:=\chi _4(\alpha m)=-1,\qquad
 s_1:=\chi _4(\beta m')=-1,
\tag{1.3}
\]

their character table is exactly \((+,-,-,+)\).  The orbit sum is the
literal zero-extended mixed endpoint difference

\[
\begin{aligned}
 &\{\lambda_{N+r,\sigma}(g\beta)
       -\lambda_{N+r,\sigma}(gm')\}\\
 &\qquad\qquad\times
 \overline{\{\lambda_{N,\sigma}(g\alpha)
       -\lambda_{N,\sigma}(gm)\}}.
\end{aligned}
\tag{1.4}
\]

Moreover, a genuine four-corner atom lies only on the primitive
inward-cross-gcd slice:

\[
 \boxed{\kappa=1.}
\tag{1.5}
\]

Indeed, in the plus chart
\((\alpha,m')=(\kappa U,\kappa v)=\kappa\), and in the minus chart
\((m,\beta)=(\kappa v,\kappa U)=\kappa\).

Second, the lower swap alone does give the needed \(D_L/L\) gain, but only
after a further literal common-cell restriction.  Put

\[
 P_2=
 \mathbf 1_{\{|d-gm|\le D_L\}}
 \mathbf 1_{\{|d'-gm'|>D_L\}},
 \qquad D_L=\lceil\sqrt L\rceil,
\tag{1.6}
\]

\[
 P_0=P_2\,
 \mathbf1_{(m,\beta)=1}\,
 \mathbf1_{\chi _4(\alpha m)=-1}.
\tag{1.7}
\]

For the lower endpoint let
\(\mathfrak c_{N,\sigma}(u,v)\) be its complete literal sharp-cell code.
It records the zero-extension state and the values or branches of every
non-smooth lower field: shell and strict-cone support, profile branch,
floor, star, half weight, hard sample, literal cell, crossing, endpoint
trace, sign, and every other discrete support field in
\(a^{\rm lit,\sigma}_{L,X}(u,v)\).  A common dead value is represented by
one distinguished code.  The code does not include the Round-184
selector \(\rho_N\), which is audited separately, or the normalized BV
values, which are summed by translation variation.

Define the symmetric physical common-cell mask

\[
 C_{\rm lit}(x)=
 \mathbf1_{\{
 \mathfrak c_{N,\sigma}(m,g\alpha)
 =
 \mathfrak c_{N,\sigma}(\alpha,gm)\}},
\qquad
 P_{\rm cc}=P_0C_{\rm lit}.
\tag{1.8}
\]

The equality in (1.8) is symmetric under the lower swap, so
\(P_{\rm cc}\) is an orbit-invariant, pre-spectral physical mask.  No
nonemptiness or density is asserted.

For the complete outer aggregate over all high-height dyadic blocks,
with both orientations and frequency signs restored before the one outer
real part, the following strict-sector estimates hold:

\[
 \boxed{
 |\mathscr R_{\rm core,out}^{\sigma}(P_{\rm cc}W)|
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon,}
\tag{1.9}
\]

\[
 \boxed{
 |\mathscr R_{\rm open,out}^{\sigma}(P_{\rm cc}W)|
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon.}
\tag{1.10}
\]

Here \(\mathscr R_{\rm open,out}\) is the exact intersection with the
Round-195 packet complement

\[
 \kappa<D_L,\qquad
 \min(Y,D_L)>H_B\mathfrak m\kappa.
\tag{1.11}
\]

The packet condition is not used to form the physical orbit.  Equation
(1.10) is obtained only after proving the complete physical
\(P_{\rm cc}\) estimate, passing through the masked core, and subtracting
the accepted Round-195 safe packet union.

The exact disjoint physical complement is

\[
\begin{aligned}
 P_{g{\rm f}}&=P_2\mathbf1_{(m,\beta)>1},\\
 P_{s{\rm f}}&=P_2\mathbf1_{(m,\beta)=1}
                    \mathbf1_{\chi _4(\alpha m)\ne-1},\\
 P_{\partial{\rm lit}}&=P_0(1-C_{\rm lit}),
\end{aligned}
\tag{1.12}
\]

\[
 \boxed{
 P_2=P_{\rm cc}\ \dot\cup\ P_{\partial{\rm lit}}
        \ \dot\cup\ P_{s{\rm f}}\ \dot\cup\ P_{g{\rm f}}.}
\tag{1.13}
\]

The full lower single-swap mask \(P_0\) is therefore not a proved strict
repair.  The first unresolved part is
\(P_{\partial{\rm lit}}\).  A ratio or profile face aligned with the
swap-fixed line \(d/m=g\) can be crossed by all \(O(LD_L)\) lower-close
pairs.  With \(O(LX^\eta)\) upper completions this retains the full
\(D_LL^2X^\eta\) envelope.  The selected context supplies neither a
uniform transversality theorem nor continuity across every such literal
face for real \(X\).  Consequently no \(O(D_L^2)\) face count is claimed.

The supported terminal label is

strict_p2_common_cell_allocation_commutator_sector.

The broader label strict_p2_four_corner_allocation_commutator_sector is
not supported.

## 2. Exact statement and hypotheses

Fix real \(X\ge2\), one nonempty literal middle or lower hard-\(M_1\)
residual shell \(L\ge2\), \(\sigma\in\{+1,-1\}\), fixed \(B>0\), and

\[
 H_B=\lfloor(\log(2X))^B\rfloor,\qquad
 R_0=\lceil L\rceil,\qquad D_L=\lceil\sqrt L\rceil.
\tag{2.1}
\]

Use the exact accepted Round-185 zero-extended endpoint coefficient

\[
 \lambda_{N,\sigma}(d)
 =\mu^2(N)\rho_N(d)
   a_{L,X}^{\mathrm{lit},\sigma}(N/d,d),
\tag{2.2}
\]

on its literal support and zero elsewhere.  It contains every original
shell, height, strict \(4m<d<16m\) cone, profile, floor, star, half-weight,
hard-sample, cell, crossing, endpoint, sign, squarefree, allocation-
coprimality, and selector field.  On support,

\[
 |\lambda_{N,\sigma}(d)|\ll_\eta X^\eta
\tag{2.3}
\]

for every fresh \(\eta>0\).

The complete even-shift physical atom is

\[
 N=dm,\qquad N+r=d'm',\qquad d,d'\ {\rm odd},
 \qquad 0<r<R_0,\qquad 2\mid r,
\tag{2.4}
\]

with summand

\[
 \chi _4(d')\chi _4(d)\,
 \Phi_{r,\sigma}(N)\,
 \lambda_{N+r,\sigma}(d')
 \overline{\lambda_{N,\sigma}(d)},
\tag{2.5}
\]

where

\[
 \Phi_{r,\sigma}(N)=
 \left(1-\frac r{R_0}\right)
 e\!\left(
 \frac{\sigma\sqrt X\,r}{\sqrt{N+r}+\sqrt N}
 \right).
\tag{2.6}
\]

The Fejer factor and square-root phase depend only on
\((N,N+r,r)\).  The proof is made before conductor Fourier expansion,
height differencing, Farey selection, a separate orientation norm, or a
positive Gram bound.

The estimate in (1.9) is an outer estimate, not a bound for one fixed
dyadic \(Y\)-block.  All high opposing blocks are summed in their original
complex aggregate first.  A lower allocation swap may change the
canonical \(\kappa\), \(h\), orientation, or dyadic block.  Cross-block
cancellation is therefore retained.  Only after the full outer physical
estimate is established are the accepted linear core and packet
decompositions applied.

The exact Round-192 convention remains in force: at \(T=0\) the Farey
projector is zero and the complete inherited rho-large branch remains;
at \(T\ge1\) all simultaneous strict Farey-covector inequalities remain.

The accepted literal calculus used in (1.8) supplies, on a common sharp
cell, a finite product of normalized one-dimensional BV factors and a
scale-normalized \(C^1\) factor.  The \(C^1\) factor alone receives a
pointwise \(D_L/L\) estimate.  Normalized BV factors are treated only by
their discrete total variation.  No regularity is asserted across a
change of sharp-cell code.

## 3. Proof and derivation

### 3.1. The lower orbit and the four recomputed gcds

Squarefreeness of the two endpoint products gives

\[
 (g,\alpha)=(g,m)=(\alpha,m)=1,
\qquad
 (g,\beta)=(g,m')=(\beta,m')=1.
\tag{3.1}
\]

On \(P_0\), define

\[
 \tau_0(g\alpha,m,g\beta,m')
 =(gm,\alpha,g\beta,m').
\tag{3.2}
\]

The recomputed character-leg gcd is

\[
 (gm,g\beta)=g(m,\beta)=g.
\tag{3.3}
\]

The image satisfies the same cross condition because
\((\alpha,\beta)=1\).  Moreover,

\[
 |g\alpha-gm|=|gm-g\alpha|,
\qquad
 |g\beta-gm'|\ \text{is unchanged}.
\tag{3.4}
\]

Thus \(P_0\) is \(\tau_0\)-invariant.  Since
\(\chi _4(\alpha m)=-1\), the odd integers \(\alpha,m\) are unequal, so
every orbit has two elements.

Under (1.2), all five integers
\[
 g,\alpha,m,\beta,m'
\tag{3.5}
\]
are pairwise coprime.  The four recomputed gcds are

\[
\begin{array}{c|c}
(\text{lower character leg},\text{upper character leg})
 &\text{gcd}\\ \hline
(g\alpha,g\beta)&g(\alpha,\beta)=g,\\
(gm,g\beta)&g(m,\beta)=g,\\
(g\alpha,gm')&g(\alpha,m')=g,\\
(gm,gm')&g(m,m')=g.
\end{array}
\tag{3.6}
\]

Hence

\[
 \tau_1(g\alpha,m,g\beta,m')
 =(g\alpha,m,gm',\beta)
\tag{3.7}
\]

is also an involution, and
\(\tau_0\tau_1=\tau_1\tau_0\).  Both defects in (1.6) are invariant.

In the plus chart

\[
 \alpha=\kappa U,\qquad m'=\kappa v,\qquad (U,v)=1,
\]

so

\[
 (\alpha,m')=(\kappa U,\kappa v)=\kappa.
\tag{3.8}
\]

In the minus chart

\[
 \beta=\kappa U,\qquad m=\kappa v,\qquad (U,v)=1,
\]

so

\[
 (m,\beta)=(\kappa v,\kappa U)=\kappa.
\tag{3.9}
\]

The four-corner cross conditions therefore force (1.5).  This is a
literal algebraic restriction, not a density claim.

### 3.2. Character table and the actual endpoint differences

Let

\[
 C=\chi _4(g\beta)\chi _4(g\alpha).
\tag{3.10}
\]

The lower swap multiplies the character product by
\[
 s_0=\chi _4(\alpha m),
\tag{3.11}
\]
and the upper swap multiplies it by
\[
 s_1=\chi _4(\beta m').
\tag{3.12}
\]

On (1.3) the exact table is

\[
\begin{array}{c|cc}
 &\text{upper 0}&\text{upper 1}\\ \hline
\text{lower 0}&C&-C\\
\text{lower 1}&-C&C.
\end{array}
\tag{3.13}
\]

Also

\[
 r=g(\beta m'-\alpha m).
\tag{3.14}
\]

Both products in parentheses are \(3\pmod4\), and \(g\) is odd; hence

\[
 \boxed{4\mid r.}
\tag{3.15}
\]

This is not the Round-193 \(r\equiv2\pmod4\) simultaneous reversal.
Indeed, \(\tau_0\tau_1\) has multiplier \(s_0s_1=+1\) here.

For fixed \(N,r\), put

\[
 F(d_0,d_1)=
 \lambda_{N+r,\sigma}(d_1)
 \overline{\lambda_{N,\sigma}(d_0)}.
\tag{3.16}
\]

Ambient zero extension makes every corner meaningful.  The lower
two-corner orbit gives

\[
 C\Phi_{r,\sigma}(N)\lambda_{N+r,\sigma}(g\beta)
 \overline{
 \lambda_{N,\sigma}(g\alpha)-\lambda_{N,\sigma}(gm)}.
\tag{3.17}
\]

The four-corner orbit gives

\[
\begin{aligned}
 &F(g\alpha,g\beta)-F(gm,g\beta)
  -F(g\alpha,gm')+F(gm,gm')\\
 &\quad=
 \{\lambda_{N+r,\sigma}(g\beta)
    -\lambda_{N+r,\sigma}(gm')\}
 \overline{
 \{\lambda_{N,\sigma}(g\alpha)
    -\lambda_{N,\sigma}(gm)\}}.
\end{aligned}
\tag{3.18}
\]

Thus the mixed difference is exact.  The upper difference is used only
at its literal bounded size.  All power saving must come from the lower
close difference.

### 3.3. The orbit-stable common-cell sector

The inputs to the two lower endpoint coefficients are

\[
 (N/(g\alpha),g\alpha)=(m,g\alpha),
\qquad
 (N/(gm),gm)=(\alpha,gm).
\tag{3.19}
\]

Equality of the sharp-cell codes in (1.8) is symmetric under exchanging
these two inputs.  Therefore \(P_{\rm cc}\) is invariant under
\(\tau_0\).  If their common code is the dead code, both lower
coefficients vanish.  Otherwise both inputs lie in one certified literal
smooth cell, with the same sharp multipliers and branch formulas.

On such a live cell, write one term of the accepted finite product as

\[
 a^{\rm lit,\sigma}_{L,X}(u,v)
 =\Bigl(\prod_{j=1}^{J}\eta_j(\zeta_j(u,v))\Bigr)
   b^{\rm sm}_{L,X,\sigma}(u,v),
\tag{3.20}
\]

where \(J=O(1)\), each \(\eta_j\) has uniformly normalized discrete
variation, and \(b^{\rm sm}\) is scale-normalized \(C^1\).  The lower
displacement satisfies

\[
 |\alpha-m|\le D_L/g,\qquad |g\alpha-gm|\le D_L.
\tag{3.21}
\]

Only the smooth factor receives the pointwise estimate

\[
 |b^{\rm sm}(m,g\alpha)-b^{\rm sm}(\alpha,gm)|
 \ll_\eta \frac{D_L}{L}X^\eta.
\tag{3.22}
\]

The product is expanded by the exact finite telescoping rule.  No
pointwise bound is imposed on \(\eta_j(u')-\eta_j(u)\).

### 3.4. Selector and normalized-BV ledgers

The residual selector is

\[
 \rho_N(d)=
 1-\mathbf1_{p_N\mid d}-\mathbf1_{q_N\mid d}
   +2\mathbf1_{p_Nq_N\mid d},
\tag{3.23}
\]

with truth table \((1,0,0,1)\).  Under \(\tau_0\), a selected prime
outside \(g\) is complemented between \(\alpha\) and \(m\); a selected
prime in \(g\) stays on the character leg.  Thus the selector is
invariant unless exactly one selected prime lies in \(g\).

The lower-close relation, hard cone, and literal shell give the accepted
uniform bound \(g\le G_0\).  The Round-193 selector audit proves that the
exactly-one-in-\(g\) exception is absent for all sufficiently large
\(L\): the selected primes have logarithmic gap \(O(L^{-1/2})\), whereas
one of them would lie in the fixed finite prime set dividing
\(g\le G_0\).  The finitely many remaining shells are paid absolutely.
Hence the selector commutator is target-safe and need not be included in
the sharp-cell code.

For a normalized BV factor, the exact translation inequality is

\[
 \sum_n|\eta(n+j)-\eta(n)|
 \le |j|\,{\rm Var}(\eta).
\tag{3.24}
\]

The accepted pullback of each normalized BV coordinate changes by an
integer \(\Delta_k\) with
\(|\Delta_k|\ll|k|\), where \(k=\alpha-m\).  Therefore

\[
\begin{aligned}
 \sum_{|k|\le D_L/g}\sum_n
 |\eta(n+\Delta_k)-\eta(n)|
 &\ll
 \sum_{|k|\le D_L/g}|k|\,{\rm Var}(\eta)\\
 &\ll D_L^2.
\end{aligned}
\tag{3.25}
\]

This is the required weighted \(O(D_L^2)\) lower aggregate.  It is
uniform in real \(X\) because only the accepted normalized variation is
used.  For each completed lower pair,

\[
 \sum_{0<r<R_0}\tau(N+r)\ll_\eta LX^\eta
\tag{3.26}
\]

bounds all upper allocations.  Consequently one normalized BV term
contributes

\[
 O_\eta(D_L^2L X^\eta).
\tag{3.27}
\]

The finite product rule and \(J=O(1)\) preserve this power.  This
argument treats variation inside the common sharp cell only.  It does
not count a sharp profile, ratio, floor, star, support, or zero-extension
face.

### 3.5. Fixed-\(\kappa\) smooth count and the full power ledger

In either accepted primitive chart, the unweighted positive \(P_2\)
capacity at fixed inward cross gcd \(\kappa\) is

\[
 \mathcal C_\kappa
 \ll D_L\left(1+\frac L\kappa\right)^2.
\tag{3.28}
\]

In the plus chart, after \((\kappa,g,U,v,w)\) is fixed, the height
determinant confines \(S\) to an interval of length \(O(1)\), because
\(\kappa v\asymp L\); lower closeness gives \(O(D_L)\) choices for
\(w\).  In the minus chart the roles of \(S,w\) are reversed.  Each of
\(U,v\) has \(O(1+L/\kappa)\) choices.  Literal conditions only delete
atoms.

The raw sum is

\[
\begin{aligned}
 \sum_{\kappa\ll L}\mathcal C_\kappa
 &\ll
 D_L\sum_{\kappa\ll L}
 \left(1+\frac L\kappa\right)^2\\
 &\ll
 D_L\{L+L\log(2L)+L^2\}\\
 &\ll D_LL^2X^\eta.
\end{aligned}
\tag{3.29}
\]

The harmless \(X^\eta\) in the last line absorbs divisor and fixed
logarithmic losses.  Multiplying by the actual common-cell gain in
(3.22) gives

\[
\begin{aligned}
 \frac{D_L}{L}
 \sum_{\kappa\ll L}\mathcal C_\kappa X^\eta
 &\ll
 \frac{D_L^2}{L}
 \{L+L\log(2L)+L^2\}X^\eta\\
 &\ll D_L^2L X^{2\eta}.
\end{aligned}
\tag{3.30}
\]

Together with (3.27), the selector exception, and the bounded upper
coefficient, this gives

\[
 O_\varepsilon(D_L^2L X^\varepsilon)
 =O_\varepsilon(L^2X^\varepsilon),
\tag{3.31}
\]

because \(D_L^2\le4L\) for \(L\ge2\).  The direct replay is the same:
\(O(LD_L)\) lower-close pairs and \(O(LX^\eta)\) upper completions give
raw \(D_LL^2X^\eta\); the smooth factor replaces \(LD_L\) by
\(D_L^2\), while (3.25) gives that same weighted lower mass for each
normalized BV factor.

On the four-corner sector, (1.5) reduces (3.28) to the
\(\kappa=1\) term.  That term is still
\(O(D_LL^2)\) before the lower common-cell gain.  Thus
\(\kappa=1\) does not by itself price a sharp literal exit.

### 3.6. Why sharp literal faces are not priced

For a sharp face, no consequence of the selected context permits
replacing one full \(L/\kappa\) range in (3.28) by
\(D_L/\kappa\).  Such a replacement requires transversality of the face
to the lower swap direction, or continuity of the two branch formulas
across the face.

The obstruction is visible at the swap-fixed ratio line.  The two lower
ratios are

\[
 \frac{g\alpha}{m}
 \quad\text{and}\quad
 \frac{gm}{\alpha}.
\tag{3.32}
\]

For every \(\alpha\ne m\), these lie on opposite sides of \(g\).  Thus a
face at ratio \(g\) is crossed by every lower-close pair.  There can be
\(O(LD_L)\) such pairs, not \(O(D_L^2)\).  Completing the upper endpoint
by (3.26) leaves

\[
 O_\eta(D_LL^2X^\eta).
\tag{3.33}
\]

Equivalently, at fixed \(\kappa\) the available face bound remains
\(\mathcal C_\kappa\), and its \(\kappa\)-sum is (3.29).  This is a
route-scoped capacity self-return, not a lower bound and not an assertion
that the actual profile has nonzero jump on this face.  It proves that
the generic collar argument alone is insufficient uniformly in real
\(X\).

The mask \(P_{\partial{\rm lit}}\) in (1.12) can be split exactly and
disjointly by the first unequal component of the two sharp-cell codes.
This gives, in a fixed declared order, the zero-extension/support exit,
shell/cone exit, profile-branch exit, floor/star/half-weight exit,
hard-sample exit, cell/crossing exit, and endpoint-trace exit.  Every
piece is a symmetric physical orbit mask.  None is estimated here.

### 3.7. Source, orientation, and height exits

The lower orbit is formed on the complete ambient even-shift source
(2.4), before restricting to the high opposing source.  This is
necessary because \(\tau_0\) need not preserve the canonical
\(\kappa\), the quotient \(h\), the orientation, or one dyadic
\(Y\)-block.

The accepted Round-185 theorem (K185.7) gives the complete absolute
bound

\[
 O_{B,\varepsilon}(L^2X^\varepsilon)
\tag{3.34}
\]

for the whole monotone sector and both opposing orientations with
\(h\le H_B\).  Intersecting it with \(P_{\rm cc}\) only deletes atoms.
The complete high opposing outer aggregate equals the ambient paired
aggregate minus this accepted safe source.  This prices every genuine
monotone/low-height orientation exit.

A move from one high dyadic block to another is internal to the complete
outer aggregate and is not charged separately.  This report proves no
fixed-\(Y\) estimate.  On the narrower four-corner orbit
\(\kappa=1\), every opposing corner has \(h=r/(2g)\), so opposing
corners also remain in the same \(Y\)-block; the ambient argument is
still used to cover any monotone corner.

### 3.8. Exact masked-core and open-packet passage

Let \(M_{\rm cc}=P_{\rm cc}\) be imposed on the physical source.  Sum
the accepted identities over all high dyadic blocks before taking the
outer real part:

\[
 \mathscr H_{\rm out}^{\sigma}(M_{\rm cc}W)
 =
 \mathscr S_{\le192,{\rm out}}^{\sigma}(M_{\rm cc}W)
 +
 \mathscr R_{\rm core,out}^{\sigma}(M_{\rm cc}W).
\tag{3.35}
\]

Sections 3.2--3.7 prove

\[
 |\mathscr H_{\rm out}^{\sigma}(M_{\rm cc}W)|
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\tag{3.36}
\]

The deletion-stability result used here is exactly the accepted
Round-193 masked-operator passage
(193.C19b)--(193.C21).  It states that every Round-187--192 safe
projector can be rerun after coordinatewise physical deletion, using
positive atom or row counts, Fourier \(\ell^1\) mass, residue sparsity,
exact deleted-row Abel return, or the single Farey row indicator.  The
same interface is restated in the accepted Round-195 kernel, Section 4
and (195.C18).  Hence

\[
 |\mathscr S_{\le192,{\rm out}}^{\sigma}(M_{\rm cc}W)|
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon.
\tag{3.37}
\]

The transported mask identity is retained literally:

\[
 M_hB_h-\chi M_-^{\rm tr}B_-^{\rm tr}
 =
 M_h(B_h-\chi B_-^{\rm tr})
 +\chi(M_h-M_-^{\rm tr})B_-^{\rm tr}.
\tag{3.38}
\]

Thus affine births and deaths, carries, unequal endpoint translations,
cells, crossings, phases, zero extensions, both \(T\)-branches, the
complete anchor aggregate, and both frequency signs remain in the
recomputed core.  Equations (3.35)--(3.37) prove (1.9).

Now let \(\mathscr R_{\rm cap,out}\) be the accepted Round-195 safe
packet union: all \(\kappa\ge D_L\), together with the
\(\kappa<D_L\) packets satisfying

\[
 \min(Y,D_L)\le H_B\mathfrak m\kappa.
\tag{3.39}
\]

The exact accepted deletion-stable results are (195.C6a), (195.C20),
(195.C20b), together with Section 4 and (195.C18) of that kernel.
Their fixed-packet and outer ledgers are positive.  Since
\(M_{\rm cc}\le P_2\), the additional physical deletion only removes
terms, and

\[
 |\mathscr R_{\rm cap,out}^{\sigma}(M_{\rm cc}W)|
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon.
\tag{3.40}
\]

The packet split is exact and linear:

\[
 \mathscr R_{\rm open,out}^{\sigma}(M_{\rm cc}W)
 =
 \mathscr R_{\rm core,out}^{\sigma}(M_{\rm cc}W)
 -
 \mathscr R_{\rm cap,out}^{\sigma}(M_{\rm cc}W).
\tag{3.41}
\]

This proves (1.10).  One real part is taken only after each complete
complex outer aggregate in (3.35)--(3.41) has been restored.  No
orientation, \(Y\)-block, anchor mode, or frequency sign is normed
separately.

Applying the same linear operator to (1.13) gives the exact open
operator complement:

\[
\begin{aligned}
 \mathscr R_{\rm open,out}(P_2W)
 &=
 \mathscr R_{\rm open,out}(P_{\rm cc}W)
 +\mathscr R_{\rm open,out}(P_{\partial{\rm lit}}W)\\
 &\quad+
 \mathscr R_{\rm open,out}(P_{s{\rm f}}W)
 +\mathscr R_{\rm open,out}(P_{g{\rm f}}W).
\end{aligned}
\tag{3.42}
\]

For the formal four-corner sector \(P_{\rm rect}\) defined by
(1.2)--(1.3), the exact refinement is

\[
 P_{\rm rect}
 =
 P_{\rm rect}C_{\rm lit}
 \ \dot\cup\
 P_{\rm rect}(1-C_{\rm lit}).
\tag{3.43}
\]

The first term is target-safe by the proof above and has the exact mixed
difference (3.18).  The second is part of the unresolved literal-face
operator in (3.42).

## 4. First doubtful or unproved step

The first unproved step is extension from \(P_{\rm cc}\) to
\(P_0\), equivalently bounding
\(P_{\partial{\rm lit}}=P_0(1-C_{\rm lit})\).

The four-corner and lower two-corner identities themselves remain exact
there because zero extension keeps every coefficient value.  What fails
is the \(D_L/L\) estimate for the actual lower difference.  If the two
lower allocations lie on different profile branches, different literal
cells, or opposite sides of a support or zero-extension face, their
coefficient difference is only \(O(X^\eta)\).  The selected context
contains no uniform transversality or branch-continuity statement that
reduces the \(O(LD_L)\) lower-close pairs to \(O(D_L^2)\).  The explicit
ratio-aligned control (3.32)--(3.33) shows the first capacity
self-return.

This does not prove nonzero mass on the literal face and does not
disprove a coefficient-sensitive estimate.  A completion would require
one of:

1. an exact audit of every actual ratio/profile/support face proving
   transversality to the allocation-swap direction;
2. an exact continuity or matching identity for the actual branch
   formulas across each aligned face; or
3. a new signed estimate for the face operator retaining all actual
   coefficients, phases, selectors, masks, source exits, and the complete
   four-block orientation aggregate.

Beyond \(P_0\), the first exact orbit failure is \(P_{g{\rm f}}\), where

\[
 (gm,g\beta)=g(m,\beta)>g.
\tag{4.1}
\]

The swap then changes the physical gcd, defects, primitive chart, and
packet data.  On \(P_{s{\rm f}}\) a same-\(g\) orbit may exist, but its
character multiplier is not \(-1\), so it gives a lower coefficient sum
rather than a difference.

For the full four-corner proposal there is also the sharp scope
restriction \(\kappa=1\).  Even at \(\kappa=1\), the literal-face term
has the raw \(D_LL^2X^\eta\) envelope.  Hence neither the complete
four-corner sector nor the full lower single-swap \(P_0\) sector is proved
target-safe.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| exact_physical_even_shift_source | PASS. Equations (2.4)--(2.6) retain the exact products, even shift, Fejer factor, radical phase, conjugation, characters, and zero extension. |
| physical_mask_before_spectral_operations | PASS. \(P_{\rm cc}\le P_2\) is imposed before every Round-187--192 operation. |
| four_corner_recomputed_gcd | PASS. All four recomputed gcds are displayed in (3.6). |
| cross_coprimality_orbit_closure | PASS with the exact restriction \(\kappa=1\), proved in (3.8)--(3.9). |
| commuting_independent_allocation_swaps | PASS. The endpoint swaps are commuting involutions on the cross-coprime rectangle. |
| four_corner_character_table | PASS. The exact table is (3.13). |
| r_mod_four_sign_split | PASS. The rectangle has \(4\mid r\), not the Round-193 \(r\equiv2\pmod4\) reversal. |
| actual_endpoint_mixed_difference | PASS algebraically. Equation (3.18) is the exact literal zero-extended mixed difference. |
| lower_close_D_L_over_L_gain | PASS only on \(P_{\rm cc}\). The actual common-cell smooth factor gives (3.22); no arbitrary array is substituted. |
| normalized_BV_and_literal_face_collars | PARTIAL PASS / SELF-RETURN. Normalized BV variation gives the replayable \(O(D_L^2)\) lower aggregate (3.25) and total (3.27). Sharp literal faces do not have a certified collar; (3.32)--(3.33) retain full capacity. |
| residual_selector_truth_table | PASS. The only mismatch is exactly one selected prime in \(g\), handled by the accepted Round-193 finite-shell audit. |
| opposing_source_and_cone_exits | PASS / OPEN as separated. Monotone and low-\(h\) source exits are paid by K185.7; cone exits inside \(P_{\partial{\rm lit}}\) remain open unless the sharp codes agree. |
| squarefree_coprimality_divisibility | PASS. Equations (3.1)--(3.6) prove allocation validity and \(g\mid r\). |
| complete_four_corner_zero_extension | PASS algebraically. Every corner in (3.18) is evaluated at its literal value, including zero. A live/dead mismatch is not discarded; it lies in \(P_{\partial{\rm lit}}\). |
| both_T_branches_if_core_used | PASS. Equation (3.35) retains \(T=0\) and every strict \(T\ge1\) row. |
| complete_anchor_recombination_if_core_used | PASS. The orbit is physical; the masked passage uses the complete outer anchor aggregate. |
| carry_birth_death_mask_commutators | PASS. Equation (3.38) retains the exact mask commutator and unmatched affine sites. |
| one_outer_real_part | PASS. No fixed-\(Y\), orientation, anchor, or frequency-sign modulus is taken. |
| complete_outer_power_ledger | PASS for \(P_{\rm cc}\), OPEN for \(P_{\partial{\rm lit}}\). Equations (3.28)--(3.31) restore the full \(\kappa\)-sum; (3.33) exposes the face deficit. |
| no_arbitrary_coefficient_replacement | PASS. Only the actual endpoint coefficient, its accepted common-cell \(C^1\)/BV structure, and its actual selector are used. |
| original_t1_only_downstream_scope | PASS. The result concerns only the stated original-\(t=1\), rho-large \(P_2\) sub-sector. |
| exponent_quarantine | PASS. No owner, parent, bridge, theorem, endpoint-uniformity statement, or exponent is changed. |

The mandatory shadows give the following outcomes.

1. **Lower single swap.** It is algebraically valid and proves the
   common-cell sector \(P_{\rm cc}\). It is not a proof for all of
   \(P_0\), because the sharp literal-face complement has (3.33).
2. **Simultaneous swap only.** It fails on the rectangle: its multiplier
   is \(s_0s_1=+1\), so it supplies no coefficient difference.
3. **Unsigned or character-erased.** It fails: the two lower endpoint
   values add and the raw \(D_LL^2\) envelope remains.
4. **Phase-conjugated or arbitrary coefficients.** It fails: an
   arbitrary lower array need not satisfy (3.22) or (3.25).
5. **Missing corner.** It fails if the corner is simply deleted. This
   proof evaluates the literal zero; a live/dead lower transition is
   quarantined in \(P_{\partial{\rm lit}}\).
6. **Mask deleted.** It fails: without \(P_2\), the lower displacement
   is not \(O(D_L)\).
7. **Separate \(Y\)-blocks, orientations, or anchor modes.** It fails:
   \(\tau_0\) can change these data. The proof uses the complete outer
   physical aggregate before the one real part.

No computation was used.

## 6. Dependencies and exact artifacts used

Only the selected context named in the task brief was used:

1. protocol.md;
2. state/proof_obligations.yml at the stated graph hash;
3. state/active_campaign.yml;
4. state/failure_ledger.md;
5. strategy/round197_m1_t1_p2_four_corner_allocation_commutator_strategy.md;
6. proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md;
7. proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md;
8. proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md;
9. proofs/kernels/m9_m1_hard_top_t1_p2_on_shell_carrier_normalization_self_return.md;
10. rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/reports/literal_p2_determinant_fibre_vector_attack.md;
11. rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/reviews/conductor_round195_adjudication.md;
12. rounds/codex-managed/m9-m1-t1-core-gcd-scaled-orientation-gate/reviews/conductor_round193_report_reconciliation.md; and
13. the assigned Round-197 task brief.

No sibling Round-197 report, unlisted artifact, web source, or diagnostic
was used.  The divisor losses use only the accepted elementary divisor
bound already present in the selected graph and kernels.

## 7. Recommended state effect

**Revise the proposed mechanism.**  After the required independent seam
reviews, promote at most one subordinate strict-sector node for
\(P_{\rm cc}\), with terminal label
strict_p2_common_cell_allocation_commutator_sector.

Record all of the following.

1. The two independent swaps form the claimed four-corner orbit, have
   table \((+,-,-,+)\), and give the exact mixed difference (3.18).
2. Full cross-coprimality forces \(\kappa=1\).  The four-corner proposal
   therefore does not cover general small-\(\kappa\) packets.
3. The lower single swap proves the target only on the symmetric
   common-sharp-cell sector \(P_{\rm cc}\); normalized BV variation and
   the selector exception are target-safe there.
4. The full physical \(P_{\rm cc}\) core and its intersection with the
   exact Round-195 open packet complement are distinct claims.  The
   latter follows by the exact subtraction (3.41), not by inserting the
   packet condition into the orbit.
5. The exact physical complement is (1.13), and the exact open-operator
   complement is (3.42).
6. The first unresolved term is \(P_{\partial{\rm lit}}\).  Without an
   actual face-transversality or branch-continuity theorem, its available
   bound self-returns to \(D_LL^2X^\eta\).

Do not promote the full \(P_0\) single-swap sector, the full
four-corner \(P_{\rm rect}\) sector, complete \(P_2\), \(P_1\), complete
original \(t=1\), any other original-\(t\) incidence, the hard
small-\(t\) owner, either \(M_1\) parent, GAR, any \(M_2\) parent,
endpoint uniformity, \(M_9\), either bridge, the Gauss-circle target, or
any exponent.
