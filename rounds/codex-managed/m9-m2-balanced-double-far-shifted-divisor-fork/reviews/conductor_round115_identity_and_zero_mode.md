# Conductor review: literal charts and phase-free mode

Campaign: m9-m2-balanced-double-far-shifted-divisor-fork

Decision: pass after scope repair.

## 1. Claims reviewed

This review covers:

1. the full-product divisor-pair chart;
2. the endpoint-increment and character chart;
3. the determinant angular and fixed-shift Hessian identities;
4. the fully assembled phase-free double-far estimate; and
5. the reduction to the oscillatory nonzero-mode remainder.

The blind and hostile reports derived the first, second, and fourth items
independently. The discovery report independently recovered the first two
and audited the latter geometric identities.

## 2. Exact algebra

With \(n=hk\), \(n+r=h'k'\),

\[
 hk'-h'k
 ={h(n+r)\over h'}-{h'n\over h}
 ={h^2(n+r)-h'^2n\over hh'}.
\]

With \(h'=h+p\), \(k'=k+q\),

\[
 r=hq+kp+pq,\qquad \rho=hq-kp,
\]

\[
 r+\rho=q(2h+p),\qquad r-\rho=p(2k+q).
\]

Nonzero character factors force \(h,h'\) odd and \(p=2s\), with

\[
 \chi_4(h)\chi_4(h+p)=(-1)^s=e(s/2).
\]

These identities are coefficientwise and retain both gcd weights and both
copies of the slanted symbol. The character is a constant sign on each
fixed even shift; it is not an inner-\(h\) oscillation there.

For

\[
 t=\log(h/\sqrt n),\qquad
 t'=\log(h'/\sqrt{n+r}),
\]

direct substitution gives

\[
 \rho=2\sqrt{n(n+r)}\sinh(t-t').
\]

Thus determinant-far is angular divisor-ratio separation, while the outer
phase remains radial.

Finally, writing

\[
 F_{p,q}(x,y)=\sqrt{(x+p)(y+q)}-\sqrt{xy},
\]

the rank-one formula

\[
 \nabla^2\sqrt{xy}
 =-{(y,-x)^{\mathsf T}(y,-x)\over4(xy)^{3/2}}
\]

and the determinant formula for a difference of two rank-one matrices give

\[
 \det\nabla^2F_{p,q}
 =-{(qx-py)^2\over
 16\{xy(x+p)(y+q)\}^{3/2}}.
\]

This agrees with both nonblind reports. At \(R\asymp L^3\), its magnitude
after phase scaling is \(\asymp\rho^2\). This is continuous
nondegeneracy, not modulo-one separation.

## 3. Phase-free double-far lemma

Define

\[
 M_B^{(0)}
 =\sum_{\mathrm{df}}
 a_B^{<}(h,k)\overline{a_B^{<}(h',k')}.
\]

The hostile proof fixes \(h,k,k'\) and expands

\[
 \eta((h',k')/G_0)
 =\sum_{d\mid h',\,d\mid k'}\gamma_d,
\qquad
 \gamma_d=\sum_{e\mid d}\mu(e)\eta((d/e)/G_0).
\]

The divisor cost satisfies

\[
 \sum_{d\mid k'}|\gamma_d|\ll_\varepsilon X^\varepsilon.
\]

After \(h'=d\ell\), the support and the two strict far gates split the
\(\ell\)-line into only \(O(1)\) intervals. On each interval the literal
amplitude has total variation \(O(1)\), including gate jumps. Bounded
partial sums of \(\chi_4(\ell)\) then give an
\(O_\varepsilon(X^\varepsilon)\) bound for the complete \(h'\)-sum.
There are \(O(L^3)\) outer triples. Therefore

\[
 |M_B^{(0)}|\ll_\varepsilon L^3X^\varepsilon.
\]

The statement-only proof supplies an independent route. It first proves

\[
 \left|\sum_{h,k}a_B^{<}(h,k)\right|
 \ll L\log^2(2L)
\]

by exact-gcd coordinates, Möbius inversion, and linewise character
summation, and then removes the two accepted corridors at cost
\(O_\varepsilon(L^3X^\varepsilon)\). The same conclusion follows.

Both proofs require the fully assembled signed sum. Neither survives an
earlier absolute value over shifts, residue classes, gcd pieces, or divisor
pairs.

## 4. Corrected survivor

Put

\[
 \mathcal R_B^{\mathrm{osc}}
 =
 \sum_{\mathrm{df}}a_B^{<}(h,k)
 \overline{a_B^{<}(h',k')}
 \left[
 e\!\left(R(\sqrt{hk}-\sqrt{h'k'})\right)-1
 \right].
\]

Then exactly

\[
 E_{B,\mathrm{df}}=M_B^{(0)}+\mathcal R_B^{\mathrm{osc}}.
\]

Since the first term is now target-safe, the open double-far estimate is
equivalent, modulo a proved term, to

\[
 |\mathcal R_B^{\mathrm{osc}}|
 \ll_\varepsilon L^3X^\varepsilon.
\]

The bracket is not small and has full variation. This is a zero-mode
subtraction, not a power saving for the oscillatory remainder.

## 5. Hostile controls and scope

On a nondegenerate actual interior block, \(p=0\) supplies a coherent
target-sized \(L^3\) coefficient sector. Two separated constant-sign cores
and the restriction \(h'\equiv h\pmod4\) supply an \(L^4\)-capacity
coherent residue sector; the opposite residue sector has the opposite sign
and the same capacity. These are coefficient-mass controls, not lower
bounds for the complex exponential sum. They reject algebraic or termwise
annihilation, while remaining compatible with the assembled
\(O(L^3X^\varepsilon)\) phase-free bound.

The exact-square \(j=2\) boundary and all high-gcd, square, near-square, and
transform-error owners remain unchanged. No balanced estimate or downstream
theorem is proved.

## 6. Review decision

Promote the literal chart plus phase-free mode as a proved reduction after
the graph patch passes. Retain the oscillatory remainder and the original
double-far node open. Reject only the character-annihilation and
continuous-Hessian shortcut claims.

Evidence:

- rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/reports/blind_shifted_divisor_rederivation.md
- rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/reports/actual_symbol_main_term_hostile.md
- rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/reports/literal_dispersion_attack.md
- rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/controls/conductor_round115_prechecks.md
