# Round 145 conductor candidate: strict squarefree-kernel reduction

- Campaign: `m9-m1-lower-cone-squarefree-kernel-linearization-gate`
- Round: `145`
- Role: conductor-selected proof kernel
- Starting graph SHA-256: `cc5e1b2597d6d233702d566f49884dc0530d0fa62395ce03684d2f55ae19e756`
- Allocation: 100% analytic/algebraic/source verification; 0% numerical

## 1. Result

Let

\[
 C(m)=\sum_{\substack{hr=m\\r\ {\rm odd}\\r>4h}}\chi _4(r),\qquad
 k_m=\left\lfloor\sqrt{Nm}+\frac12\right\rfloor,\qquad
 j_m=k_m^2-Nm,
\]

where \(R=X^{1/4}\), \(N=\lfloor X\rfloor\), and
\(\mathcal I_M=\mathbb N\cap[M,B_M)\), \(B_M\leq2M\), are the
inherited disjoint half-open blocks.  Here \(B_M\) is the literal
endpoint of a terminal truncation, and the union of the active blocks
lies in \([1,M_*]\) with \(M_*\ll_VR^2\).  Write every \(m\)
uniquely as

\[
 m=s t^2,\qquad s\ \text{squarefree},\quad t\geq1.
\tag{145.C1}
\]

Then the exact Round-144 survivor admits the owner-complete reduction

\[
\boxed{
 \mathfrak T_N=
 \sum_M\sum_{1\leq t<M^{1/4}}
 \sum_{\substack{s\ {\rm squarefree}\\st^2\in\mathcal I_M\\
 |k_{s,t}^2-Nst^2|>M^{3/4}}}
 (st^2)^{-3/4}V_{\rm low}(R^2st^2/N)
 C(st^2)e(t\sqrt{Ns})
 +O_{\varepsilon,V}(X^\varepsilon),}
\tag{145.C2}
\]

where \(k_{s,t}=\lfloor t\sqrt{Ns}+1/2\rfloor\).  On the retained
range,

\[
 \boxed{s>M^{1/2}.}
\tag{145.C3}
\]

The complement \(t\geq\lceil M^{1/4}\rceil\) is target-safe by an
absolute count.  This is a strict arithmetic support reduction, not a
bound for the displayed survivor.  The exact coefficient formula is
proved below in two equivalent parametrizations.

The bounded-\(t\), especially \(t=1\), layers receive no cancellation
from linear summation in \(t\).  Their currently certified
divisor-envelope upper capacity is \(M^{1/4+o(1)}\), or
\(R^{1/2+o(1)}\) on the top block.  An explicit legal family also shows
that the large-displacement mask does not force the base frequency
\(\sqrt{Ns}\) away from integers.  These are scoped mechanism
obstructions, not lower bounds for the signed scalar.

The round therefore closes, if the remaining review seams are green,
under

\[
 \boxed{\mathsf{strict\_squarefree\_kernel\_reduction}}.
\tag{145.C4}
\]

No lower GAR, direct M1 parent, M9-M1 theorem, M2 owner, endpoint
theorem, M9 theorem, quarter bound, or global exponent improvement is
claimed.

## 2. Exact coefficient algebra

### 2.1 Squarefree-kernel parametrization

For a positive integer \(n\), let \({\rm sf}(n)\) be its squarefree
kernel.  Given \(hr=st^2\), put

\[
 \gamma=\gcd({\rm sf}(h),{\rm sf}(r)),\qquad
 d={{\rm sf}(h)\over\gamma},\qquad
 e={{\rm sf}(r)\over\gamma}.
\]

Then \(\gamma,d,e\) are pairwise coprime and squarefree,
\(de=s\), and there are unique \(a,b\geq1\) such that

\[
 h=\gamma d a^2,\qquad r=\gamma e b^2,\qquad t=\gamma ab.
\tag{145.C5}
\]

Conversely, every tuple in (145.C5) reconstructs one ordered divisor
pair and has squarefree product kernel \(s\).  Thus

\[
\boxed{
C(st^2)=
\sum_{\substack{\gamma\mid t\\
                  \gamma\ {\rm squarefree}\\
                  (\gamma,s)=1\\
                  \gamma\ {\rm odd}}}
\chi _4(\gamma)
\sum_{\substack{de=s\\e\ {\rm odd}}}\chi _4(e)
\sum_{\substack{ab=t/\gamma\\b\ {\rm odd}\\
                  eb^2>4da^2}}1.}
\tag{145.C6}
\]

There is no coprimality condition on \(a,b\), nor between
\(\gamma\) and either of them.  Common square powers of \(h,r\) are
carried by \(a,b\), while \(\gamma\) records only the common part of
their two squarefree kernels.

The parity ledger in (145.C6) is complete.  Since \(r\) is odd,
\(\gamma,e,b\) are odd.  If \(2\mid s\), the prime \(2\) is forced
into \(d\); if \(2^{q}\Vert t\), its entire exponent is forced into
\(a\).  Finally,

\[
 \chi _4(r)=\chi _4(\gamma e b^2)
 =\chi _4(\gamma)\chi _4(e),
\]

and cancellation of \(\gamma\) gives the literal strict cone
\(eb^2>4da^2\).

### 2.2 Full-gcd parametrization

The same coefficient has a second useful exact form.  Put
\(G=(h,r)\), \(h=GH\), and \(r=GQ\).  Prime valuations give
\(G\mid t\); since \((H,Q)=1\), there are unique squarefree
\(d,e\) and positive \(a,b\) with

\[
 de=s,\qquad H=da^2,\qquad Q=eb^2,
 \qquad (da,eb)=1,\qquad Gab=t.
\tag{145.C7}
\]

Hence, equivalently,

\[
\boxed{
C(st^2)=
\sum_{de=s}^{\rm ord}
\sum_{\substack{Gab=t\\(da,eb)=1\\
                 Geb\ {\rm odd}\\eb^2>4da^2}}
\chi _4(Ge).}
\tag{145.C8}
\]

Writing \(G=c\ell^2\), \(c={\rm sf}(G)\), exposes the squarefree
kernel of the full gcd.  Unlike \(\gamma\) in (145.C5), this \(c\)
may share primes with \(d,e,a\), or \(b\); no extra coprimality with
\(G,c,\ell\) is legal.  Equations (145.C6) and (145.C8) simply package
the common prime powers differently.  Both are multiplicity one.

## 3. The target-safe large-square tail

For fixed \(t\), the literal half-open count satisfies

\[
\begin{aligned}
\#\{s\geq1:st^2\in\mathcal I_M\}
&\leq
\left\lceil{2M\over t^2}\right\rceil
-\left\lceil{M\over t^2}\right\rceil\\
&\leq {M\over t^2}+1.
\end{aligned}
\tag{145.C9}
\]

If the set is nonempty, then \(t^2<2M\), so the last expression is at
most \(3M/t^2\).  Replacing the upper endpoint by \(2M\) only enlarges
a truncated terminal block; the exact sum continues to use its literal
endpoint and profile.

Since \(|C(m)|\leq\tau(m)\ll_\varepsilon X^\varepsilon\) on
\(m\ll_VR^2\), the part of a fixed block with integer \(t\geq T\)
obeys

\[
\begin{aligned}
 \mathcal L_M(T)
&\ll_{\varepsilon,V}
 X^\varepsilon M^{-3/4}
 \sum_{t\geq\lceil T\rceil}{M\over t^2}\\
&\ll_{\varepsilon,V}
 X^\varepsilon{M^{1/4}\over T},
 \qquad T\geq1.
\end{aligned}
\tag{145.C10}
\]

The squarefree condition, mask, phase, and profile were retained before
triangle inequality and may be discarded only in this discharged
majorant.  Exact radicals are absent from the strict mask in any event.
Taking \(T=M^{1/4}\) gives \(O(X^\varepsilon)\) per block.  The
\(O_V(\log(2X))\) blocks, including the smallest and terminal blocks,
are absorbed by epsilon renaming.  This proves (145.C2).

For integral \(t\), the split is exact:

\[
t\geq M^{1/4}\iff t\geq\lceil M^{1/4}\rceil,
\qquad
t<M^{1/4}\iff t<\lceil M^{1/4}\rceil.
\tag{145.C11}
\]

On the retained side, \(t^2<M^{1/2}\) and \(st^2\geq M\), proving
(145.C3).  More generally a dyadic \(t\)-shell \(t\asymp T\) has
available absolute upper price

\[
 \ll X^\varepsilon {M^{1/4}\over T}.
\tag{145.C12}
\]

Thus \(M^{1/4}\) is the first target-safe fixed-power cutoff for this
absolute squarefree-fibre ledger.  This statement concerns an upper
price only.

## 4. Exact mask and exceptional frequencies

Put

\[
 x=t\sqrt{Ns},\qquad k=\lfloor x+1/2\rfloor,
 \qquad\delta=k-x.
\]

A half-integer tie is impossible because it would make the multiple of
four \(4Nst^2\) an odd square.  Therefore \(-1/2<\delta<1/2\), and

\[
 j_{st^2}=\delta(2x+\delta),\qquad
 {\rm sgn}(j_{st^2})={\rm sgn}(\delta),
\tag{145.C13}
\]

with

\[
 \|t\sqrt{Ns}\|={|j_{st^2}|\over k+t\sqrt{Ns}}.
\tag{145.C14}
\]

The mask is the literal strict inequality \(|j_{st^2}|>M^{3/4}\);
on \(st^2\asymp M\), its fractional-phase scale is

\[
 \|t\sqrt{Ns}\|\asymp {M^{1/4}\over\sqrt N}
\quad\text{at the boundary}.
\tag{145.C15}
\]

Write \(N=Dw^2\), \(D\) squarefree.  Then \(Ns\) is a square if
and only if \(s=D\).  That entire exact-radical fibre has \(j=0\) and
is absent from the strict survivor.  For \(s\ne D\), set

\[
 g_s=(D,s),\qquad q_s={Ds\over g_s^2}>1.
\]

Then \(q_s\) is squarefree and

\[
 \sqrt{Ns}=g_sw\sqrt{q_s},\qquad
 j_{st^2}=k^2-q_s(g_swt)^2.
\tag{145.C16}
\]

Thus the retained values are literal generalized Pell norms.  The mask
removes the small norms through \(M^{3/4}\), but supplies no uniform
continued-fraction bound as \(q_s\) varies.

There is an exact family showing that even a large displacement does not
separate the base linear frequency.  Let \(s>1\) be squarefree and set

\[
 X=N=sL^2+1,\qquad
 \sqrt{Ns}=sL+\rho,\qquad
 \rho={1\over\sqrt{L^2+1/s}+L}.
\tag{145.C17}
\]

Whenever \(t\rho<1/2\), the nearest integer is \(k=sLt\), and

\[
 \boxed{j_{st^2}=-st^2=-m,\qquad
 e(t\sqrt{Ns})=e(t\rho).}
\tag{145.C18}
\]

The inherited lower cutoff is flat at the origin.  Choose
\(\eta_0>0\) with \(V_{\rm low}(y)=1\) for
\(0\leq y\leq\eta_0\), choose \(c>0\) with
\(c^2\leq\eta_0\), set \(L=s\), and take sufficiently large
squarefree \(s\) and
\(1\leq t\leq\lfloor c s^{1/4}\rfloor\).  Because \(X=N\),

\[
 {R^2m\over N}={m\over\sqrt N}
 ={st^2\over\sqrt{s^3+1}}\leq c^2,
\]

so the literal profile is active.  For all sufficiently large \(s\),
the same range lies in \(t<M^{1/4}\) for the literal block containing
\(m=st^2\), and \(|j|=m>M^{3/4}\) for \(M>1\).  Yet
\(t\rho\to0\) uniformly on that range, while the next
continued-fraction quotient is of order \(L\).  For the nonvacuity
control \(s=p>4\) prime and \(t=1\),

\[
 C(p)=\chi _4(p)\ne0.
\tag{145.C19}
\]

Equations (145.C17)--(145.C19) refute only a proposed uniform
frequency-gap or bounded-quotient inference.  They do not give an
aggregate absolute or signed lower bound.

## 5. Capacity and primary-source audit

The retained small-\(t\) sum has only the divisor-envelope estimate

\[
 |\mathfrak T_{N,M}^{<}|
 \ll X^\varepsilon M^{1/4}.
\tag{145.C20}
\]

At \(t=1\),

\[
 C(s)=\sum_{\substack{de=s\\e\ {\rm odd}\\e>4d}}\chi _4(e).
\tag{145.C21}
\]

For each \(s\in[M,2M)\), this layer has one \(t\)-sample.  Therefore
an argument whose only gain is linear cancellation in \(t\) supplies no
gain on this layer; without a signed estimate across \(s\), its only
presently certified general bound is (145.C20).  Cancellation across
\(s\), between \(t\)-layers, or between blocks remains possible.

The primary-source audit found no theorem matching (145.C6) or
(145.C8), the individual positive complex direction, the growing fixed
centre, and every mask/profile endpoint.  The exact failures are:

1. Uchiyama's complete-divisor square-root twist and the
   Kaczorowski--Perelli standard twist require coefficients of one fixed
   complete degree-two \(L\)-function; their fixed-frequency or weakly
   uniform conclusions do not accept \(C(st^2)\).
2. Sun's frequency-uniform nonlinear Liouville twist has the wrong
   coefficient and, at \(|\alpha|\asymp M\asymp R^2\), is no better
   than the normalized trivial capacity needed here.
3. Schlage-Puchta's squarefree theorem has a linear phase in the
   squarefree variable, whereas the target has \(e(t\sqrt{Ns})\); in
   the linear \(t\)-orientation the actual coefficient and mask vary
   with \(t\).
4. Fixed-quadratic continued-fraction estimates do not have uniform
   constants as the discriminant \(q_s\) varies; (145.C17) is a direct
   control against such an inference.
5. Robert--Sargos and Sargos--Wu accept favorable smoothed monomial
   models but not the full joint coefficient and target power.

For the last point, even grant target-free smoothing and separation of
the squarefree/coprimality factors on the mandatory \(t=1\), balanced
top block.  With \(d,e\asymp R\), phase scale \(Z\asymp R^3\), and
normalizing weight \(R^{-3/2}\), Sargos--Wu Theorem 9 leaves

\[
 \boxed{R^{2/5+\varepsilon}.}
\tag{145.C22}
\]

Robert--Sargos leaves \(R^{1/2+\varepsilon}\) in its favorable
separated specialization and \(R^{3/4+\varepsilon}\) with the exact
joint slot.  These are upper-bound limitations, not lower bounds for the
target.  The full theorem cards and hypotheses are recorded in the
Round-145 source report.

## 6. First open step and owner scope

The first unproved estimate is exactly the displayed small-\(t\) scalar
in (145.C2).  Already its \(t=1\) layer would require the uniform signed
bound

\[
\sum_{\substack{s\asymp M\ {\rm squarefree}\\
 |\lfloor\sqrt{Ns}+1/2\rfloor^2-Ns|>M^{3/4}}}
 V_{\rm low}(R^2s/N)C(s)e(\sqrt{Ns})
 \ll_{\varepsilon,V}M^{3/4}X^\varepsilon,
\tag{145.C23}
\]

or a stronger joint estimate that permits cancellation between
\(t\)-layers.  No reviewed derivation or source proves (145.C23).

The Round-138 collar-tail cross owner is independent and unchanged.
The result here does not prove the complete lower-radial estimate, lower
GAR, either direct blockwise M1 parent, M9-M1, any M2 parent, M9-M2,
endpoint uniformity, M9, the conditional bridge, or the quarter theorem.
The internally proved exponent remains \(1/3\); the separately audited
external exponent remains

\[
 {3292+25\sqrt{1717}\over13762}
 =0.3144831759740614\ldots.
\tag{145.C24}
\]

## 7. Recommended state effect

Subject to final independent review:

- create a proved squarefree-kernel reduction recording
  (145.C1)--(145.C12), including both exact coefficient
  parametrizations and the target-safe \(t\geq M^{1/4}\) complement;
- create or update a scoped obstruction recording
  (145.C13)--(145.C23): the mask/Pell geometry, the explicit
  near-integer surviving family, the absence of \(t\)-gain on the
  singleton \(t=1\) layer, and the exact primary-source/power mismatch;
- update the Round-144 cone reduction and global lower-radial owner so
  that the first open scalar is (145.C2);
- reject claims that the squarefree change alone proves cancellation,
  that the mask separates \(\sqrt{Ns}\) uniformly, that fixed
  quadratic-irrational constants are uniform in \(N,s\), that a
  complete-divisor or linear-squarefree theorem accepts the coefficient,
  or that an upper capacity is a signed lower bound;
- make no downstream theorem or exponent change.

Accepted dependencies, if the review chain closes, are the three
Round-145 reports, the two post-unmask fibre cross-reviews, the final
candidate reviews, and the accepted Round-144 graph state.
