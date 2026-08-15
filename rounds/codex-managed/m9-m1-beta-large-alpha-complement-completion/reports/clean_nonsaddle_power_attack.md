# 1. Result

There is an exact finite, smooth, nonnegative, one-count partition of
the direct positive-line complement into signed inner, middle, and outer
pieces.  The inner and outer pieces have the required fixed lower bound
for \(\lvert\Psi'\rvert\), and every transition collar lies in the middle
package.

**Correction/addendum on the nonsaddle normalization.**  The first
version of this report incorrectly required each nonsaddle cell to have
the Round-41 normalized \(\lambda^{-2}\) bound and incorrectly inserted
the stationary numerator \((D_j/q)\lambda\) into its ledger.  A genuinely
nonstationary cell has no such numerator.  The fixed
\(\chi _0'\)-collar is also harmless when it is estimated directly as a
compact piece rather than differentiated in an \(L\)-integration by
parts.  Those two alleged obstructions are withdrawn.

The proposed direct-amplitude repair is analytically sound under the
four global signed-section estimates stated in Section 2 and the
condition \(\kappa<1\): absolute integration controls the amplitude,
one \(L\)-integration by parts controls its logarithmic \(x\)-derivative,
and the resulting radial amplitude has the same raw \(q^{-p}\) ledger as
the compact terminal.  It would therefore be target-safe by the
radial-BV reduction recorded in Round 45.

The repair cannot, however, be proved from the four permitted artifacts.
The first unavailable inequality is the global outer estimate

\[
 \lvert\mathcal P(L,x)\rvert
 \ll P_X(1+\lvert\alpha\rvert)^{\kappa-2},
 \qquad \lvert\alpha\rvert\ge \frac{4\lambda}{3},
 \tag{46.1a}
\]

for the complete signed Plemelj section.  Round 41 proves only a
fixed-ratio, \(\lvert\alpha\rvert\asymp\lambda\), normalized mixed norm;
the permitted files give neither the exact global \(R_\alpha\) formula
nor its unbounded-tail estimates.  They also do not state the contour
range implying \(\kappa<1\), the two global \(x\)-derivative estimates,
or the literal Round-41 cutoff multipliers.  The result is therefore a
conditional analytic completion and a rigorous frozen-data no-go, not a
refutation of the repaired mechanism.

# 2. Exact statement and hypotheses

Assume, as required by the packet's nonnegativity control, that
\(0\leq\chi _0\leq1\), that \(1-\chi _0\) vanishes on a fixed
neighborhood of the signed origin, and that \(\lambda>0\).  Put
\(t=\lvert\alpha\rvert/\lambda\).  Choose
\(i,o\in C^\infty([0,\infty))\) satisfying

\[
 0\leq i,o\leq1,\qquad
 i(t)=1\ \text{for }t\leq\frac23,\qquad
 i(t)=0\ \text{for }t\geq\frac34,
\]

\[
 o(t)=0\ \text{for }t\leq\frac43,\qquad
 o(t)=1\ \text{for }t\geq\frac32,
\]

with \(i\) nonincreasing and \(o\) nondecreasing.  Set
\(m=1-i-o\).  Then \(0\leq m\leq1\), \(m=1\) on
\([3/4,4/3]\), and \(\operatorname{supp}m\subset(2/3,3/2)\).

Choose nonnegative \(s_+,s_-\in C^\infty(\mathbb R)\) with
\(s_++s_-=1\), whose transition is contained in the region where
\(1-\chi _0=0\), and which agree with the positive and negative
half-line indicators on the active complement.  For
\(k\in\{0,1,\infty\}\), define

\[
 \eta_{\sigma,k}^{I}
 =(1-\chi _0)s_\sigma\widetilde\vartheta_k(t)i(t),\qquad
 \eta_{\sigma,k}^{M}
 =(1-\chi _0)s_\sigma\widetilde\vartheta_k(t)m(t),
 \tag{46.2a}
\]

\[
 \eta_{\sigma,k}^{O}
 =(1-\chi _0)s_\sigma\widetilde\vartheta_k(t)o(t).
 \tag{46.2b}
\]

These eighteen multipliers are smooth and nonnegative, and

\[
 \sum_{\sigma=\pm}\sum_{k\in\{0,1,\infty\}}
 \left(\eta_{\sigma,k}^{I}+\eta_{\sigma,k}^{M}
 +\eta_{\sigma,k}^{O}\right)=1-\chi _0
 \tag{46.3}
\]

pointwise.  The inner and outer supports satisfy, respectively,

\[
 \lvert\alpha\rvert\leq\frac{3\lambda}{4},\qquad
 \lvert\alpha\rvert\geq\frac{4\lambda}{3},
\]

so \(\lvert\Psi'\rvert\geq\log(4/3)\) on both nonsaddle groups.

Here is the exact conditional direct-amplitude theorem.  After the
signed Plemelj operation in \(\nu\), let \(\mathcal P(L,x)\) be the
complete singular section after extraction of the canonical phase
\(e^{i\Psi_\sigma(L,x)}\); for smooth shares use the analogous complete
section.  All moving traces, the signed logarithmic diagonal, and cutoff
factors other than the displayed \(\eta\) are included in
\(\mathcal P\).  Define the phase-conjugated logarithmic radial
derivative

\[
 \mathcal Q(L,x)
 =e^{-i\Psi_\sigma(L,x)}x\partial_x
 \left(e^{i\Psi_\sigma(L,x)}\mathcal P(L,x)\right).
 \tag{46.4}
\]

Suppose \(\kappa<1\) and, globally in \(\alpha=L+\beta\),

\[
 \lvert\mathcal P\rvert
 \leq P_X(1+\lvert\alpha\rvert)^{\kappa-2},\qquad
 \lvert\partial_L\mathcal P\rvert
 \leq P_X(1+\lvert\alpha\rvert)^{\kappa-3},
 \tag{46.5a}
\]

\[
 \lvert\mathcal Q\rvert
 \leq P_X(1+\lvert\alpha\rvert)^{\kappa-1},\qquad
 \lvert\partial_L\mathcal Q\rvert
 \leq P_X(1+\lvert\alpha\rvert)^{\kappa-2}.
 \tag{46.5b}
\]

The same claims may be summed over the finite smooth shares.  Then the
complete inner-plus-outer direct radial amplitude satisfies

\[
 \lvert\mathcal A_{\rm ns}(x)\rvert
 +\lvert x\mathcal A_{\rm ns}'(x)\rvert\ll P_X,
 \tag{46.6}
\]

uniformly in the arithmetic and dyadic scales.  Its coefficient ledger
contains \(q^{-p}\), not the saddle factor \(q^{-p-2}\).

# 3. Proof or derivation

The partition identity follows from
\(\sum_k\widetilde\vartheta_k=1\), \(i+m+o=1\), and
\(s_++s_-=1\).  Every factor in (46.2a)--(46.2b) is nonnegative.  The
sign transition is smooth because it is multiplied by the identically
zero factor \(1-\chi _0\).  Splitting each original
\(\widetilde\vartheta_k\) among \(i,m,o\) moves every near-saddle overlap
into the middle group without losing or duplicating mass.

For the singular \(j=0\) top, the signed Cauchy section is formed before
absolute values.  With moving endpoints \(p_*(L),q_*(L)\), its structure
is

\[
 \mathcal P_0(L)=
 \int_{p_*(L)}^{q_*(L)}K_\Delta(L,\nu)\,d\nu+C(L),
 \tag{46.7}
\]

where

\[
 K_\Delta(L,\nu)
 =G(L)\frac{p(\nu)-p(L)}{(L-\nu)D(L,\nu)}
\]

is continuous at \(\nu=L\), and \(C(L)\) is the signed logarithmic
diagonal section from Round 41.  The full moving derivative is

\[
 \mathcal P_0'(L)=
 \int_{p_*}^{q_*}\partial_L^\nu K_\Delta(L,\nu)\,d\nu
 +q_*'(L)K_\Delta(L,q_*)-p_*'(L)K_\Delta(L,p_*)+C'(L).
 \tag{46.8}
\]

Thus the two moving traces occur once and with opposite Leibniz signs.
For a smooth share the same formula holds with \(K_W\), including the
derivative of its translated Mellin profile.

**Correction/addendum: direct nonstationary estimate.**  Let
\(\eta_{\rm ns}\) be any finite sum of the inner and outer multipliers.
From the first estimate in (46.5a) and \(\kappa<1\),

\[
 \int_{\mathbb R}\lvert\mathcal P(L,x)\rvert\,dL
 \ll P_X\int_0^\infty(1+t)^{\kappa-2}\,dt
 \ll_\kappa P_X.
 \tag{46.9}
\]

Consequently \(\mathcal A_{\rm ns}\) is bounded absolutely; no
\(L\)-integration by parts and no \(\lambda^{-2}\) target are needed for
the undifferentiated amplitude.

For the logarithmic radial derivative, first isolate a fixed compact
\(\alpha\)-set containing \(\operatorname{supp}\chi _0'\) and the sign
smoothing.  Its contribution is \(O(P_X)\) directly by (46.5b).  On the
remaining nonsaddle support,

\[
 \Psi_\sigma'(L)=\log\frac{\lvert\alpha\rvert}{\lambda},
 \qquad \Psi_\sigma''(L)=\frac1\alpha,
 \qquad \lvert\Psi_\sigma'\rvert\geq\log\frac43.
 \tag{46.10}
\]

One integration by parts gives

\[
 \int e^{i\Psi}\eta_{\rm ns}\mathcal Q\,dL
 =\left[\frac{e^{i\Psi}\eta_{\rm ns}\mathcal Q}
 {i\Psi'}\right]_{\mathrm{ends}}
 -\int e^{i\Psi}
 \left(
 \frac{\partial_L(\eta_{\rm ns}\mathcal Q)}{i\Psi'}
 -\frac{\eta_{\rm ns}\mathcal Q\Psi''}{i(\Psi')^2}
 \right)dL.
 \tag{46.11}
\]

The boundary at infinity vanishes because
\(\mathcal Q=O(\lvert\alpha\rvert^{\kappa-1})\) and \(\kappa<1\).
Finite endpoints either vanish with the partition cutoffs or contribute
\(O(P_X)\).  The last two estimates in (46.5b) give

\[
 \int_1^\infty
 \left((1+t)^{\kappa-2}+t^{-1}(1+t)^{\kappa-1}\right)dt
 \ll_\kappa1.
 \tag{46.12}
\]

Every derivative of a ratio cutoff is \(O(\lambda^{-1})\) on a collar
\(c\lambda\leq\lvert\alpha\rvert\leq C\lambda\).  Uniformly for all
\(\lambda>0\),

\[
 \frac1\lambda
 \int_{c\lambda}^{C\lambda}(1+t)^{\kappa-1}\,dt\ll_\kappa1:
 \tag{46.13}
\]

for \(\lambda\leq1\) this follows from boundedness on a fixed interval,
and for \(\lambda\geq1\) it is \(O(\lambda^{\kappa-1})\).  The fixed
\(\chi _0'\)-collar was already estimated directly, so it never needs to
supply an inverse power of \(\lambda\).  Differentiating the ratio
cutoffs in \(x\) gives
\(x\partial_x f(\lvert\alpha\rvert/\lambda)
=-\tfrac12t f'(t)\), which is uniformly bounded on the same collars.
The logarithmic derivative of the explicit power
\(x^{-3/2-b/2}\) is a fixed scalar.  Equations (46.9)--(46.13) prove the
conditional estimate (46.6).

The corrected raw ledger has no stationary numerator.  Before the
external physical operator, the exact coefficient contribution is

\[
 \pi\sqrt X\,P_X
 \sum_{j,h,q}^{*,\,\mathrm{eq}}
 \lvert c_{\sigma,\zeta}\chi _4(q)\rvert
 h^{-r}q^{-p}
 \left(\frac{D_j}{2\sqrt X}\right)^a
 (H_j+1)^b x^{-3/2-b/2}.
 \tag{46.14}
\]

Floors, stars, equality restrictions, radial endpoints, and the
character remain attached once.  The external \(X^{1/4}\) normalization
is applied once only after the radial-BV step.  Because (46.6) adds no
\(\lambda\), \(q\), \(D_j\), or \(x\) power, (46.14) is the same direct
\(q^{-p}\) coefficient-and-scale ledger used by the compact terminal in
Round 45.  That synthesis states that its absolute \(h,q\) sums and
dyadic scale sum cost only a polylogarithm and that the accepted
radial-BV reduction then gives \(O(X^{1/4}\log^C X)\).  Thus the repaired
nonsaddle argument would close with the same reduction if (46.5a)--
(46.5b) were proved.  No saddle numerator, connector, collision,
artificial residue, or second external factor appears in (46.14).

# 4. First doubtful or unproved step

The first unproved step is (46.1a), equivalently the first global estimate
in (46.5a), for the complete signed Plemelj section on the unbounded
outer sector.  The permitted Round-41 synthesis gives

\[
 \sup_L\int\lvert K_\Delta\rvert\,d\nu\ll P_X\lambda^{-2}
\]

only after fixed-ratio normalization on
\(\lvert\alpha\rvert\asymp\lambda\).  This supplies no implication of

\[
 \sup_{\lvert\alpha\rvert\geq4\lambda/3}
 (1+\lvert\alpha\rvert)^{2-\kappa}
 \lvert\mathcal P(L,x)\rvert\ll P_X.
 \tag{46.15}
\]

In particular, its symbol \(G\) is defined only after removing the
fixed-ratio factor \(\lambda^\kappa\), while the permitted packet gives
no exact formula or global Stirling bounds for \(R_\alpha(\alpha)\).
The nonzero unintegrated \(1/\nu\)-tail also means that one cannot replace
the missing signed-section estimate by termwise absolute integration.

Even if (46.15) were granted, the proof of the radial seminorm still
needs the last estimate in (46.5b), including all terms in the moving
derivative (46.8).  Round 41 supplies fixed-ratio \(L\)-mixed norms but no
global \(x\)-differentiated version; Round 45 supplies the exact
\(x\)-derivative identity only for the compact core.  Finally, the
permitted files define \(\kappa=3/4+(a+b)/2\) but give no range for
\(a+b\) from which \(\kappa<1\) follows.  These are missing hypotheses,
not adverse power terms in the repaired ledger.

There is a separate logical seam: the Round-41 synthesis does not display
its actual saddle, entry, and exit cutoffs.  The middle multiplier in
(46.2a) has the required support, but support compatibility does not
prove literal equality with those accepted cells.  A literal match needs
the old multipliers or a cutoff-invariance theorem.

# 5. Control tests and outcomes

1. **Same positive-line antecedent — pass.**  Every multiplier in
   (46.2a)--(46.2b) multiplies the single raw terminal (46.1) from the
   derivation packet; no terminal is retransferred.
2. **Finite partition exactness — pass.**  Equation (46.3) is pointwise,
   smooth, finite, nonnegative, and one-count.
3. **Round-41 literal cell match — unavailable.**  The accepted synthesis
   gives the fixed-ratio region but not its cutoff formulas or a
   cutoff-invariance theorem.
4. **Inner nonsaddle sector — conditional pass.**  Absolute integration
   proves (46.9), and the fixed \(\chi _0'\)-collar is compact and direct.
5. **Outer nonsaddle sector — conditional pass, frozen-data failure.**
   Equations (46.11)--(46.13) prove the analytic tail theorem from
   (46.5a)--(46.5b); equation (46.15) is not available.
6. **Signed Cauchy before absolute values — pass.**  Equations
   (46.7)--(46.8) assemble the divided difference and signed logarithmic
   diagonal first.
7. **Moving traces and cutoff derivatives — conditional pass.**  Both
   trace signs appear in (46.8), while all ratio, sign, fixed, and radial
   cutoff derivatives are accounted for in (46.11)--(46.13).
8. **Coefficient, scale, and radial ledger — corrected pass conditional
   on the analytic bounds.**  Equation (46.14) retains the raw
   \(h^{-r}q^{-p}\) ledger and invokes the same stated compact reduction;
   it contains no stationary numerator.
9. **Collision and external one-count — pass.**  No already owned module
   is reinserted, and the external factor is reserved for one final
   application of the accepted radial-BV reduction.

# 6. Dependencies and exact artifacts used

Only these four artifacts were used:

1. `rounds/codex-managed/m9-m1-beta-large-alpha-complement-completion/derivation_packet.md` — raw terminal, phase, normalized weights,
   nonsaddle supports, and ownership controls.
2. `rounds/codex-managed/m9-m1-beta-off-diagonal-product-cell/synthesis.md` — fixed-ratio normalization, signed divided difference,
   moving-trace formula, diagonal logarithmic section, and the distinction
   between the stationary numerator and the raw coefficient monomial.
3. `rounds/codex-managed/m9-m1-beta-positive-line-localization/synthesis.md` — same-antecedent requirement, compact radial-amplitude
   seminorm, absolute \(h,q\) and dyadic reductions, and the accepted
   radial-BV conclusion.
4. `rounds/codex-managed/m9-m1-beta-large-alpha-complement-completion/briefs/nonsaddle_completion_attack.md` — frozen question, access
   restriction, required controls, and report contract.

No graph, proof draft, validation matrix, other report or synthesis, web
source, external theorem, or numerical computation was used.

# 7. Recommended state effect

Retain the full positive-line localization certificate as open, but
revise the recorded obstruction.  Promote, if desired, only the finite
nonnegative partition (46.2a)--(46.3).  Do not record a nonsaddle power
loss from a stationary numerator or from the fixed \(\chi _0'\)-collar;
both were artifacts of the superseded normalization.

The next proof interface should establish the four global signed-section
bounds (46.5a)--(46.5b), including moving Plemelj traces, and explicitly
record the contour hypothesis \(\kappa<1\).  With those inputs, the direct
argument (46.9)--(46.14) supplies a target-safe nonsaddle theorem under
the already stated raw coefficient and radial reductions.  Separately,
provide the literal Round-41 middle-cell multipliers or prove
cutoff-invariance before identifying the new middle package with the
accepted saddle/entry/exit theorem.  No shared proof state should change
on the present frozen evidence.
