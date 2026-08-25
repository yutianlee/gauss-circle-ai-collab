# Round 145 post-unmask cross-review: blind squarefree-fibre report

- Campaign: m9-m1-lower-cone-squarefree-kernel-linearization-gate
- Role: discovery claimant reviewing the blind report after unmasking
- Artifacts audited: blind_squarefree_linearization_feasibility.md and squarefree_kernel_fibre_attack.md
- Scope: the four seams assigned by the conductor; no graph or downstream claim is reviewed here

## 1. Seam verdicts

| Seam | Verdict | Short reason |
|---|---|---|
| Full-gcd tuple versus squarefree-common-kernel tuple | **GREEN** | The two formulae are the same multiplicity-one parametrization after a literal renaming and the unique decomposition \(g=c\ell^2\).  Neither formula may acquire a coprimality condition involving \(g\). |
| Half-open and terminal-block tail at \(t\geq\lceil M^{1/4}\rceil\) | **GREEN** | The blind ceiling count is exact; the discovery count is the same estimate specialized to \([M,2M)\), where its missing \(+1\) is absorbed by nonemptiness.  Integer \(t\geq M^{1/4}\) is exactly \(t\geq\lceil M^{1/4}\rceil\). |
| Exceptional family \(N=sL^2+1\) | **GREEN, with an owner-complete range clarification required** | The nearest integer, sign, and value \(j=-st^2\) are exact.  Taking \(X=N\), \(L=s\), and \(t\leq c s^{1/4}\) puts a nonempty range simultaneously inside the profile, the small-\(t\) survivor, and the strict large-displacement mask. |
| Capacity versus lower-bound wording | **RED as presently worded; GREEN after the repair in §5** | Both reports intend an upper-capacity statement, but one discovery sentence says a method “pays (145.24),” although (145.24) is only an upper bound.  Nonvanishing examples do not prove aggregate absolute mass. |

## 2. Exact equivalence of the coefficient formulae

Use distinct names to remove the collision between the two reports.  The blind tuple is

\[
 (g,s_h,s_r,u_0,v_0),
\]

with

\[
 s_hs_r=s,\qquad u_0v_0=t/g,\qquad
 (s_hu_0,s_rv_0)=1.
\]

The discovery full-gcd tuple is

\[
 (g,u_{\mathrm{sf}},v_{\mathrm{sf}},a,b),
\]

with

\[
 u_{\mathrm{sf}}v_{\mathrm{sf}}=s,\qquad
 gab=t,\qquad
 (u_{\mathrm{sf}}a,v_{\mathrm{sf}}b)=1.
\]

The bijection is exactly

\[
 s_h=u_{\mathrm{sf}},\qquad s_r=v_{\mathrm{sf}},
 \qquad u_0=a,\qquad v_0=b.
\]

Thus \(u_0v_0=t/g\) is equivalent to \(gab=t\), and the two
coprimality conditions coincide.  In both forms the reconstructed pair is

\[
 h=g\,s_hu_0^2,\qquad r=g\,s_rv_0^2.
\tag{R145.1}
\]

The oddness conditions also coincide:

\[
 g\ \hbox{odd and }s_rv_0\ \hbox{odd}
 \iff g,s_r,v_0\ \hbox{all odd}.
\]

They give

\[
 \chi_4(r)=\chi_4(g)\chi_4(s_r),\qquad
 r>4h\iff s_rv_0^2>4s_hu_0^2.
\tag{R145.2}
\]

Now write the full gcd uniquely as \(g=c\ell^2\), with \(c\) squarefree.
Then \(g\) odd is equivalent to \(c\ell\) odd, and

\[
 \chi_4(g)\chi_4(s_r)=\chi_4(cs_r).
\]

This is exactly the discovery squarefree-common-kernel formula.  The
factor \(c\) is the squarefree kernel of the full common divisor, not a
new divisor allocated independently between \(h\) and \(r\).  It may
share a prime with one side of the coprime pair.  No condition such as
\((g,s_hs_ru_0v_0)=1\), \((c,\ell)=1\), or
\((c,s_hs_r)=1\) is valid.  The sole cross-side coprimality is
\((s_hu_0,s_rv_0)=1\).

There is one typesetting repair required in the discovery report:
its displayed (145.6) must read (R145.1), not
\(h=g,ua^2,\ r=g,vb^2\).  This is not a mathematical disagreement,
because (145.1), (145.5), and the surrounding proof use the correct
products.

## 3. Literal large-\(t\) tail

Let the literal block be

\[
 \mathcal I_M=\mathbb N\cap[A_M,B_M),
\qquad A_M\asymp M,\quad B_M-A_M\ll M,
\]

with the actual \(B_M\) used on a terminal truncation.  For fixed \(t\),
the exact unmasked integer count is

\[
 \#\{s\geq1:A_M\leq st^2<B_M\}
 =
 \left\lceil\frac{B_M}{t^2}\right\rceil
 -
 \left\lceil\frac{A_M}{t^2}\right\rceil
 \leq \frac{B_M-A_M}{t^2}+1.
\tag{R145.3}
\]

The blind report therefore obtains

\[
\begin{aligned}
 |T_{M,\mathrm{large}}|
 &\ll_{\eta,V}M^{-3/4+\eta}
 \sum_{\lceil M^{1/4}\rceil\leq t<\sqrt{B_M}}
 \left(\frac{M}{t^2}+1\right)\\
 &\ll_{\eta,V}M^\eta+M^{-1/4+\eta}.
\end{aligned}
\tag{R145.4}
\]

This retains the literal half-open endpoint.  A terminal block only
decreases \(B_M\) and the number of terms.  The exact mask, squarefree
condition, and profile are present before triangle inequality and may be
removed only in this discharged absolute majorant.

For the standard block \([M,2M)\), the discovery proof writes
\(3M/t^2\) instead of \(M/t^2+1\).  This is legitimate: nonemptiness
implies \(t^2<2M\), so \(M/t^2>1/2\) and
\(M/t^2+1\leq3M/t^2\).  It remains legitimate on a terminal subset of
that block.  Finally, because \(t\) is integral,

\[
 t\geq M^{1/4}\iff t\geq\lceil M^{1/4}\rceil,\qquad
 t<M^{1/4}\iff t<\lceil M^{1/4}\rceil.
\tag{R145.5}
\]

The candidate should use the ceiling notation in the exact split and
may use \(t<M^{1/4}\) only after recording (R145.5).

## 4. Exact \(N=sL^2+1\) exceptional family

Let \(s>1\) be squarefree, \(L\geq1\), and choose the fixed real centre
\[
 X=N=sL^2+1.
\]
Then

\[
 \sqrt{Ns}=sL+\rho,\qquad
 \rho=\frac{1}{\sqrt{L^2+1/s}+L},
\qquad 0<\rho<\frac1{2L}.
\tag{R145.6}
\]

If \(t\rho<1/2\), then \(sLt\) is the unique nearest integer to
\(t\sqrt{Ns}\), with the inherited rounding convention:

\[
 k_{s,t}=sLt,\qquad
 k_{s,t}-t\sqrt{Ns}=-t\rho<0.
\tag{R145.7}
\]

Consequently the sign and norm are exactly

\[
\boxed{
 j_{st^2}=k_{s,t}^2-Nst^2=-st^2=-m.}
\tag{R145.8}
\]

If \(m\in[M,2M)\) and \(M>1\), then
\[
 |j|=m\geq M>M^{3/4},
\]
so this near-integer phase lies in the strict large-displacement
survivor, not in the deleted near-radical window.

The profile and small-\(t\) ranges can be made simultaneous, rather than
left as a geometric possibility.  Choose \(L=s\), take \(s\) arbitrarily
large and squarefree, and fix \(c>0\) so small that
\(V_{\rm low}(y)=1\) for \(0\leq y\leq c^2\).  For

\[
 1\leq t\leq c\,s^{1/4},
\tag{R145.9}
\]

one has

\[
 \frac{R^2m}{N}=\frac{m}{\sqrt N}
 =\frac{s t^2}{\sqrt{s^3+1}}\leq c^2,
\tag{R145.10}
\]

so the literal profile is active and flat.  Also
\(t\rho\leq c s^{1/4}/(2s)<1/2\).  If \(M\leq m<2M\), then
\(M>m/2=st^2/2\), and (R145.9) implies, for large \(s\),

\[
 t<M^{1/4};
\tag{R145.11}
\]

equivalently \(t<\lceil M^{1/4}\rceil\).  Thus (R145.8) occurs on a
literal active range of the exact small-\(t\) survivor.  Moreover,

\[
 \frac1\rho=\sqrt{L^2+1/s}+L
\]

has integer part \(2L\), so the first continued-fraction quotient after
the integer part is unbounded with \(L\).  This family rigorously
refutes a uniform frequency-gap or uniformly bounded-quotient inference.

It does not lower-bound the signed scalar.  The coefficient may vary or
vanish along the longer range (R145.9).  For a nonvacuity control one may
take \(s=p>4\) prime and \(t=1\); then \(C(p)=\chi_4(p)\ne0\), the
profile is flat for large \(p\), and (R145.8) is an actual nonzero
survivor term.  This single-term control still gives no aggregate lower
bound.

## 5. Capacity wording repair and final verdict

The valid conclusions are:

1. The divisor-envelope triangle estimate for bounded \(t\) has upper
   capacity \(M^{1/4+o(1)}\), reaching \(R^{1/2+o(1)}\) at the top
   block.
2. The \(t=1\) layer receives no cancellation from summation in \(t\),
   because that isolated layer has one \(t\)-sample per \(s\).
3. Values such as \(C(p)=\chi_4(p)\) prove that the layer is not
   identically zero.

They do not prove that the absolute \(t=1\) mass is
\(M^{1/4+o(1)}\), that the signed scalar has this size, or that
cancellation between \(s\), different \(t\)-layers, or dyadic blocks
cannot occur.

Accordingly, replace the discovery sentence

> “Any procedure ... therefore pays (145.24) already on these singleton fibres.”

by

> “On the isolated \(t=1\) layer such a procedure receives no gain from
> the \(t\)-variable; without an additional signed estimate across \(s\),
> the only presently certified general bound is the
> \(M^{1/4+o(1)}\) divisor-envelope upper capacity.”

In both reports, phrases such as “the layer has size” or “retains
capacity” should be read and, in the conductor candidate, written as
“the available triangle/divisor-envelope bound has upper capacity.”
The explicit disclaimers against a signed lower bound should remain.

**Final verdict: conditional GREEN.**  The coefficient bijection, the
large-\(t\) deletion, and the exceptional family are mathematically
correct.  Before promotion, repair the discovery product notation,
state the ceiling split and the active exceptional range explicitly, and
remove the one forced-price sentence identified above.  With those
repairs, the reports support a strict squarefree-kernel reduction and a
scoped failure of \(t\)-linearity by itself, but no target estimate or
lower bound.
