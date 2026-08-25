# Round 145 conductor adjudication: strict squarefree-kernel reduction

- Campaign: `m9-m1-lower-cone-squarefree-kernel-linearization-gate`
- Round: `145`
- Starting graph SHA-256: `cc5e1b2597d6d233702d566f49884dc0530d0fa62395ce03684d2f55ae19e756`
- Generated: `2026-08-24T06:38:36+08:00`

## Decision

The repaired conductor candidate is accepted after three definitive
independent GREEN confirmations.  Round 145 closes under

\[
 \boxed{\mathsf{strict\_squarefree\_kernel\_reduction}}.
\]

The exact Round-144 survivor is target-equivalent to its part with

\[
 m=st^2,\qquad s\ \text{squarefree},\qquad
 t<M^{1/4},\qquad s>M^{1/2}.
\]

The complement \(t\geq\lceil M^{1/4}\rceil\) is
\(O_{\varepsilon,V}(X^\varepsilon)\) after all dyadic blocks.  This is
a genuine strict support reduction.  The retained signed scalar is not
estimated.

No lower GAR, direct M1 parent, M9-M1, M2 owner, endpoint theorem, M9,
quarter theorem, or global exponent improvement is proved.

## Accepted proof kernel

Every \(m\) has the unique form \(m=st^2\), \(s\) squarefree.  If
\(\gamma\) is the common part of the two squarefree kernels of \(h,r\),
then

\[
\begin{aligned}
C(st^2)=
\sum_{\substack{\gamma\mid t\\\gamma\ {\rm squarefree}\\
(\gamma,s)=1\\\gamma\ {\rm odd}}}\chi_4(\gamma)
\sum_{\substack{de=s\\e\ {\rm odd}}}\chi_4(e)
\sum_{\substack{ab=t/\gamma\\b\ {\rm odd}\\
eb^2>4da^2}}1.
\end{aligned}
\tag{145.J1}
\]

This is multiplicity one.  Its equivalent full-gcd form is

\[
C(st^2)=
\sum_{de=s}^{\rm ord}
\sum_{\substack{Gab=t\\(da,eb)=1\\Geb\ {\rm odd}\\
eb^2>4da^2}}\chi_4(Ge).
\tag{145.J2}
\]

The two common factors have different meanings: \(\gamma\) is
squarefree and coprime to \(s\), while \(G=(h,r)\) contains the full
common prime powers.  If \(G=c\ell^2\), then
\(c={\rm sf}(G)\) may overlap the quotient variables; no extra
coprimality with \(G,c,\ell\) is legal.  Oddness forces all powers of
two from \(s,t\) onto the \(h\)-side, exactly as recorded in the
candidate.

For a literal block
\(\mathcal I_M=\mathbb N\cap[M,B_M)\), \(B_M\leq2M\), fixed \(t\)
supports at most \(M/t^2+1\leq3M/t^2\) kernels when nonempty.  Since
\(|C(m)|\leq\tau(m)\),

\[
 \mathcal L_M(T)
 \ll_{\varepsilon,V}X^\varepsilon{M^{1/4}\over T}.
\tag{145.J3}
\]

Taking \(T=M^{1/4}\), retaining the literal profile and terminal
endpoint in the exact scalar, and summing the logarithmic block family
proves

\[
\boxed{
\mathfrak T_N=
\sum_M\sum_{1\leq t<M^{1/4}}
\sum_{\substack{s\ {\rm squarefree}\\st^2\in\mathcal I_M\\
|k_{s,t}^2-Nst^2|>M^{3/4}}}
(st^2)^{-3/4}V_{\rm low}(R^2st^2/N)
C(st^2)e(t\sqrt{Ns})
+O_{\varepsilon,V}(X^\varepsilon).}
\tag{145.J4}
\]

Because \(t^2<M^{1/2}\) and \(st^2\geq M\), the retained support has
\(s>M^{1/2}\).

## Exact mask and mechanism obstruction

With \(x=t\sqrt{Ns}\), \(k=\lfloor x+1/2\rfloor\), and
\(\delta=k-x\), a half-integer tie is impossible and

\[
 j=\delta(2x+\delta),\qquad
 \|t\sqrt{Ns}\|={|j|\over k+t\sqrt{Ns}}.
\tag{145.J5}
\]

If \(N=Dw^2\), \(D\) squarefree, exact resonance is precisely
\(s=D\), already absent from the strict mask.  Every other fibre is a
generalized Pell norm

\[
 j=k^2-q_s(g_swt)^2,\qquad
 g_s=(D,s),\quad q_s=Ds/g_s^2>1.
\tag{145.J6}
\]

The mask does not separate the base frequency uniformly.  For squarefree
\(s>1\), set \(X=N=sL^2+1\).  Then

\[
 \sqrt{Ns}=sL+\rho,\qquad
 \rho={1\over\sqrt{L^2+1/s}+L}.
\]

For \(t\rho<1/2\), the nearest integer is \(sLt\) and

\[
 j=-st^2=-m,\qquad e(t\sqrt{Ns})=e(t\rho).
\tag{145.J7}
\]

Taking \(L=s\), sufficiently large squarefree \(s\), and
\(1\leq t\leq\lfloor cs^{1/4}\rfloor\) inside the inherited flat
profile gives literal retained terms with \(t\rho\to0\).  Hence large
displacement does not imply a uniform frequency gap or bounded
continued-fraction constants.  This is not a lower bound.

At \(t=1\),

\[
 C(s)=\sum_{\substack{de=s\\e\ {\rm odd}\\e>4d}}\chi_4(e),
\qquad C(p)=\chi_4(p)\ne0\quad(p>4\ \text{prime}).
\tag{145.J8}
\]

There is no \(t\)-sum on this isolated layer.  Its currently certified
divisor-envelope upper capacity is \(M^{1/4+o(1)}\), but cancellation
across \(s\) and other owners remains possible.

## Source and power decision

The completed source audit found no theorem accepting the exact
coefficient, squarefree support, mask, growing fixed centre, and
individual positive direction.  Complete-divisor standard twists have
the wrong coefficient and fixed/weak frequency uniformity; the
frequency-uniform Liouville theorem has the wrong coefficient and power;
the linear squarefree theorem has the wrong phase orientation; and
fixed-quadratic constants are not uniform as the discriminant varies.

Even after optimistically granting smoothing and coefficient separation
on the mandatory balanced \(t=1\) top block, Sargos--Wu leaves
\(R^{2/5+\varepsilon}\).  Robert--Sargos leaves
\(R^{1/2+\varepsilon}\) in the favorable separated specialization and
\(R^{3/4+\varepsilon}\) in the exact-joint specialization.  These are
limitations of available upper bounds, not signed lower bounds.

## Review chain and first open step

The discovery and statement-only reports independently proved the
coefficient bijection and large-square tail.  Their post-unmask reviews
reconciled the full-gcd and squarefree-kernel formulas, corrected one
notation typo, and tightened the capacity wording.  The source report
was then finalized with exact theorem cards and a reproducible power
ledger.  Three final audits initially returned two presentation/evidence
REDs; the conductor repaired the literal terminal endpoint, restored the
source artifact, and quantified the exceptional profile range.  The
three definitive rechecks are GREEN.

The first open estimate is (145.J4) without its error term, equivalently
the candidate's equation (145.C2).  The \(t=1\) subproblem already asks
for a genuine \(M^{1/4}\) signed saving across squarefree \(s\).  No
accepted derivation or source provides it.

## State decision

Promote the exact coefficient identities and the target-safe
\(t\geq M^{1/4}\) complement as a proved reduction.  Promote the scoped
linearization/source obstruction without treating any capacity as a
lower bound.  Update the Round-144 cone and global lower-radial owners to
the small-\(t\), large-\(s\) survivor.  Reject the unqualified
linearization, uniform frequency-gap, complete-coefficient substitution,
uniform partial-quotient, direct source-import, and downstream-exponent
claims.  Make no other theorem-status change.
