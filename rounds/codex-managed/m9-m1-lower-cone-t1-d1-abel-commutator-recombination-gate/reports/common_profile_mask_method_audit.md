# Round 159 primary-source and analytic-method audit: common-profile residual mask

- Campaign: `m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate`
- Task: `common_profile_mask_method_audit`
- Role: source auditor
- Graph SHA-256: `8a0f917fb8117e9dbaf287d9f773046ff201729d2d8d8c3df1a51bca7815574b`
- Allocation: 100% analytic; no numerical or symbolic experiment

## 1. Result

### Common-profile mask method no-go, with a target-safe shifted zero mode

Assume that the sibling algebra reviews validate the full six-line Abel
recombination and the selected-coordinate identity

\[
 \mathcal S_U(V)=
 \sum_{\ell\geq1}\chi _4(\ell)w_U(\ell)e(\sqrt{N\ell})
 \mathbf 1_{V<|r(\ell)|\leq2V},
 \qquad
 r(\ell)=\kappa(\ell)^2-N\ell,
\tag{159.MA1}
\]

where \(\kappa(\ell)=\lfloor\sqrt{N\ell}+1/2\rfloor\).  Write
\(w_U=M^{-3/4}\widetilde w_U\).  The required raw estimate is

\[
 T_U(V):=
 \sum_{\ell\asymp M}\chi _4(\ell)\widetilde w_U(\ell)
 e(\sqrt{N\ell})\mathbf 1_{V<|r(\ell)|\leq2V}
 \ll_\varepsilon M^{3/4}X^\varepsilon.
\tag{159.MA2}
\]

The audit gives one genuine positive sublemma and one route-scoped no-go.

1. In the exact residual-band Fourier expansion, multiplication by
   \(e(\sqrt{N\ell})\) changes mask frequency \(h\) to square-root
   frequency \(q=h+1\).  The exceptional mode is therefore \(h=-1\),
   not \(h=0\).  Its square-root phase disappears, but \(\chi _4\)
   remains.  The exact moving-band coefficient has bounded variation, so
   ordinary Abel summation against the bounded partial sums of \(\chi _4\)
   gives a raw \(O(X^\varepsilon)\) bound.  This mode is target-safe.
2. Vaaler's theorem can be applied separately to the literal interval(s)
   belonging to each nearest cell.  Its continuous integral excess is not
   the discrete error.  Combining the actual Fejer kernels with the
   accepted quadratic-root count gives the literal raw boundary ledger

   \[
     E_J\ll_\varepsilon
     \left(\frac KJ+\sqrt V+\sqrt M+1\right)X^\varepsilon,
     \qquad K=\sqrt{NM},
   \tag{159.MA3}
   \]

   for a degree-\(J\) polynomial.  Thus this unsigned truncation route can
   reach the raw target only if

   \[
      J\geq J_{\mathrm{lit}}:=K M^{-3/4},
      \qquad V\leq M^{3/2},
   \tag{159.MA4}
   \]

   up to harmless integral ceilings and \(X^\varepsilon\).  For
   \(V>M^{3/2}\), no audited source supplies the missing signed control of
   the hard boundary incidences.
3. Even on the range in (159.MA4), absolute summation of the available
   pointwise exponent-pair bounds over the nonzero Fourier modes does not
   close (159.MA2).  In the most favorable coefficient treatment, the
   audited pair

   \[
     \left(\frac{195}{796},\frac{235}{398}\right)
   \]

   at \(J=J_{\mathrm{lit}}\) gives the raw capacity

   \[
     N^{195/796}M^{1295/3184+\varepsilon}.
   \tag{159.MA5}
   \]

   After restoring \(M^{-3/4}\), this is

   \[
      \left(\frac{N^{780}}{M^{1093}}\right)^{1/3184}X^\varepsilon.
   \tag{159.MA6}
   \]

   It is target-sized only if \(M^{1093}\geq N^{780}\), which is
   disjoint from \(M\leq N^{1/2}\).  The straightforward moving-coefficient
   Abel treatment is worse by the factor \(1+V/M^{3/4}\).
4. For every \(q=h+1\ne0\), character splitting followed by the
   Poisson/van-der-Corput \(B\)-process has stationary denominators
   \(d=4n\mp1\) and phase

   \[
      e\!\left(\frac{q^2N}{d}\right).
   \tag{159.MA7}
   \]

   For \(q=\pm1\), this is exactly the reciprocal carrier
   \(e(N/(4n\mp1))\) already present in the graph-recorded Round-154
   reciprocal \(B\)-process self-return.  For general \(q\), it is the
   same interface with numerator \(q^2N\).  The dual length and stationary
   amplitude restore exactly the \(B\)-transformed exponent-pair capacity;
   no extra power appears.
5. Exact projector/incomplete-quadratic completion gives, even after the
   favorable joint-BV grants needed to insert the common profile, raw
   capacity \(N^{1/2}X^\varepsilon\).  It would require
   \(M\geq N^{2/3}\), again outside the frozen cone.  No audited
   character-sum or Hilbert-inequality theorem controls the remaining
   coupled modulus/frequency family pointwise at fixed \(N\).

Consequently there is **no source-legal target theorem and no new strict
owner-complete range**.  In particular, nothing here extends below the
already graph-recorded Round-154 range \(M^{449}\gg R^{780}\), and nothing
extends the already owned fixed-polylogarithmic root-defect collar.  The
appropriate terminal label is
`paired_interior_abel_commutator_no_go`, qualified as a no-go for the
audited Fourier, pointwise exponent-pair, \(B\)-process,
incomplete-quadratic, character-sum, and Hilbert interfaces—not as a lower
bound or a mathematical impossibility theorem.

## 2. Exact statement and hypotheses

### 2.1 Frozen parameters, coefficient class, and normalization

The audit keeps

\[
 q_0=4N,\qquad K=\sqrt{NM},\qquad
 M^{3/4}(\log(2X))^A<V\leq K,\qquad M\leq N^{1/2}.
\tag{159.MA8}
\]

The symbol \(q_0\) denotes the physical modulus; below, \(q=h+1\)
denotes a shifted Fourier frequency.  These must not be confused.

For the coefficient-sensitive steps, the exact required profile hypothesis
is

\[
 \|\widetilde w_U\|_\infty+
 \operatorname {Var}_{\ell\asymp M}(\widetilde w_U)
 \ll_\varepsilon X^\varepsilon.
\tag{159.MA9}
\]

The stationary-phase card additionally uses the inherited smooth dyadic
version

\[
 \sup_{x\asymp M}|(M\partial_x)^j\widetilde w_U(x)|
 \ll_{j,\varepsilon}X^\varepsilon
\tag{159.MA10}
\]

after a compact interior partition.  If only (159.MA9) is available at a
hard transition, Abel summation is legal but every resulting endpoint term
must be retained.  No arbitrary bounded coefficient is admitted.

The actual scalar is \(M^{-3/4}T_U(V)\).  Therefore:

\[
 \boxed{\text{raw target }M^{3/4}X^\varepsilon
 \quad\Longleftrightarrow\quad
 \text{scalar target }X^\varepsilon.}
\tag{159.MA11}
\]

The support estimate
\(\#\operatorname {supp}T_U(V)\ll\min(M,V)X^\varepsilon\) is unsigned
and is not (159.MA2).

### 2.2 Literal variable band

Put

\[
 y=\sqrt{N\ell},\qquad k=\kappa(\ell),\qquad
 \delta=y-k\in[-1/2,1/2).
\tag{159.MA12}
\]

Then, exactly,

\[
 r=k^2-y^2=-\delta(2k+\delta).
\tag{159.MA13}
\]

For fixed \(k\), the positive- and negative-defect parts are at most two
half-open intervals in \(\delta\).  Their non-cell-edge endpoints are
obtained from

\[
 u_s^+(k)=k-\sqrt{k^2-s},\qquad
 u_s^-(k)=\sqrt{k^2+s}-k,\qquad s\in\{V,2V\},
\tag{159.MA14}
\]

and are intersected with \([0,1/2]\) using the literal half-open
convention.  Explicitly, on \(\delta=-u<0\),
\(|r|=u(2k-u)\); on \(\delta=u\geq0\),
\(|r|=u(2k+u)\).  This is the variable band used throughout.  No fixed
fractional interval replaces it.

Let \(m_{k,V}(\delta)\) be its indicator on the circle and define its exact
Fourier coefficients

\[
 \gamma_h(k;V)=
 \int_{-1/2}^{1/2}m_{k,V}(t)e(-ht)\,dt.
\tag{159.MA15}
\]

Writing the at most two component intervals as \([a_\nu(k),b_\nu(k)]\),

\[
 \gamma_0=\sum_\nu(b_\nu-a_\nu),\qquad
 \gamma_h=\sum_\nu
 \frac{e(-ha_\nu)-e(-hb_\nu)}{2\pi i h}\quad(h\ne0).
\tag{159.MA16}
\]

Since \(k\asymp K\) on the profile support, put \(\alpha=V/K\).  Direct
differentiation of (159.MA14) gives

\[
 \left|\frac{d}{dk}u_s^\pm(k)\right|
 \ll \frac{s}{k^2}.
\tag{159.MA17}
\]

Clipping at a cell edge does not increase total variation.  Hence

\[
 \begin{aligned}
  |\gamma_0|+\operatorname {Var}_k\gamma_0&\ll\alpha,\\
  |\gamma_h|&\ll\min(\alpha,|h|^{-1}),\\
  \operatorname {Var}_k\gamma_h&\ll\alpha\qquad(h\ne0).
 \end{aligned}
\tag{159.MA18}
\]

Because \(\kappa(\ell)\) is nondecreasing, composition with
\(k=\kappa(\ell)\) does not enlarge these variation bounds.

### 2.3 Exact external theorem cards

**Vaaler interval polynomials.**  Vaaler, Theorems 18--19, gives for a
fixed periodic interval a degree-\(J\) majorant and minorant.  The integral
excess is \(1/(J+1)\), the nonzero coefficient is the exact interval
coefficient plus \(O((J+1)^{-1})\), and the pointwise difference is
dominated by normalized Fejer kernels at the endpoints.  The theorem is
legal for each fixed value of \(k\); it does not turn its continuous
integral excess into a bound for the sampled moving endpoints in
(159.MA12).

**Bourgain exponent pair.**  Bourgain, Theorem 6, proves

\[
 \left(\frac{13}{84}+\varepsilon,
       \frac{55}{84}+\varepsilon\right)
\tag{159.MA19}
\]

as a global exponent pair.  For a standard phase on an interval of length
\(M\), phase parameter \(\mathcal T\), and \(1\leq M\leq\mathcal T\), it
gives

\[
 \sum_{n\in I}e(\mathcal TF(n/M))
 \ll_\varepsilon(\mathcal T/M)^{\kappa+\varepsilon}
 M^{\lambda+\varepsilon},
\tag{159.MA20}
\]

uniformly for proper subintervals after the source's logarithmic
partial-sum device.  A BV weight is inserted only afterwards by Abel
summation.

**Audited transformed pair.**  The permitted Round-158 source report
audits the Tao--Trudgian--Yang \(D\)- and \(B\)-process formulas and the
pair

\[
 D\left(\frac{13}{84},\frac{55}{84}\right)
 =\left(\frac{18}{199},\frac{593}{796}\right),
 \qquad
 BD\left(\frac{13}{84},\frac{55}{84}\right)
 =\left(\frac{195}{796},\frac{235}{398}\right).
\tag{159.MA21}
\]

The standard derivative class and coefficient restrictions in (159.MA20)
remain mandatory.

**Incomplete quadratic sums.**  Muellner, Theorem 5.3 and Lemma 5.4,
allow arbitrary integers \(a,b\), arbitrary composite \(m\geq1\), and an
arbitrary consecutive interval.  In the notation of the permitted source
report,

\[
 \left|\sum_{x=n_0+1}^{n_0+L}e_m(ax^2+bx)\right|
 <\left(\frac Lm+1+\frac2\pi\log\frac{2m}{\pi}\right)
 \sqrt{2m(a,m)}.
\tag{159.MA22}
\]

It does not accept an arbitrary two-variable moving coefficient.  Such a
coefficient may be inserted only after a proved BV decomposition.

**Montgomery--Vaughan Hilbert inequality.**  Their Theorem 2 concerns a
finite family of distinct real frequencies separated on the real line by
\(\Delta>0\) and gives a continuous \(t\)-interval mean square with cost
\(|I|+\Delta^{-1}\).  It is not a pointwise theorem at one fixed \(N\),
and it is not the modulo-one large sieve.

**Huxley 2003.**  The repository source card contains no theorem,
notation translation, hypotheses, or uniformity statement.  The paper can
be identified bibliographically as *Exponential sums and lattice points
III*, Proc. London Math. Soc. 87 (2003), 591--609, DOI
10.1112/S0024611503014485, but no result from it is source-legal in this
campaign.  In particular, the value usually associated with Huxley's
lattice-point work may not be inserted as a black-box exponent pair here.

## 3. Proof or derivation

### 3.1 Abel recombination is kept ahead of every estimate

The permitted kernel gives, separately on the positive block, the right
outer endpoint, the positive moving atom, and the negative of the positive
profile-difference remainder.  It gives, separately on the negative block,
the left outer endpoint, the negative moving atom with a positive sign, and
the positive negative-block profile-difference remainder.  These are the
three lines of (K158.7) and the three lines of (K158.8).  Their sum is the
original \(\sum_j\widehat B_j(2dv)K(-v^2,-j;c)\) for each odd \(d\mid N\)
and each interior \(v\).  This audit estimates none of those six lines in
isolation.

Only after their full recombination may complete-frequency inversion give
the candidate common quotient profile \(w_U(\ell)\).  The boundary-frozen
profiles \(W_+\) and \(W_-\) from the isolated Round-158 trace never enter
the present method ledger.  Likewise,

\[
 e(\sqrt{N\ell}-\kappa(\ell))=e(\sqrt{N\ell})
\tag{159.MA23}
\]

uses only the integrality of \(\kappa(\ell)\).  This does not modify the
isolated-trace statement.

### 3.2 Fourier shift and the \(h=-1\) mode

For a degree-\(J\) approximation write schematically

\[
 m_{k,V}(\delta)
 =\sum_{|h|\leq J}b_{h,J}(k;V)e(h\delta)+\mathcal R_J(k,\delta),
\tag{159.MA24}
\]

where \(b_{h,J}=\gamma_h+O((J+1)^{-1})\), with the endpoint phases
retained.  Since \(k\) is integral,

\[
 e(\sqrt{N\ell})e(h\delta)
 =e((h+1)\sqrt{N\ell}).
\tag{159.MA25}
\]

Thus \(q=h+1\).  When \(h=-1\), (159.MA25) equals one.  The corresponding
raw term is

\[
 Z_{-1}=\sum_{\ell\asymp M}
 \chi_4(\ell)\widetilde w_U(\ell)b_{-1,J}(\kappa(\ell);V).
\tag{159.MA26}
\]

The partial sums of \(\chi_4\) are bounded.  Equations (159.MA9) and
(159.MA18), including the \(O(J^{-1})\) endpoint-coefficient correction,
give

\[
 \sup|\widetilde w_U b_{-1,J}|+
 \operatorname {Var}_\ell(\widetilde w_U b_{-1,J})
 \ll_\varepsilon X^\varepsilon.
\tag{159.MA27}
\]

Finite Abel summation therefore proves

\[
 Z_{-1}\ll_\varepsilon X^\varepsilon.
\tag{159.MA28}
\]

Even \(\ell\) have not been silently deleted: they contribute zero because
\(\chi_4(\ell)=0\).  After restoring the atom scale, (159.MA28) is
\(O(M^{-3/4}X^\varepsilon)\).  The Fourier remainder
\(\mathcal R_J\) is separate and is not charged to this mode.

### 3.3 Literal Vaaler truncation and moving-boundary incidence

Let

\[
 \mathfrak F_J(t):=\frac1{(J+1)^2}
 \left(\frac{\sin\pi(J+1)t}{\sin\pi t}\right)^2.
\tag{159.MA29}
\]

This is the Vaaler endpoint-error kernel normalized to have peak
\(\mathfrak F_J(0)=1\) and integral \(1/(J+1)\).  Equivalently, if
\(K_J\) denotes the standard Fejer kernel of integral one and peak
\(J+1\), then \(\mathfrak F_J=K_J/(J+1)\).  It satisfies

\[
 \mathfrak F_J(t)\ll
 \min\left(1,\frac1{J^2\|t\|^2}\right).
\tag{159.MA30}
\]

Vaaler's pointwise error for the two-component band is bounded by a fixed
constant times the sum of (159.MA29) at its at most four endpoints.  The
fact that its integral is \(O(J^{-1})\) does **not** yield a discrete
\(M/J\) estimate for the sequence (159.MA12).

Here the discrete incidence can be bounded explicitly, including periodic
wrap across the centered-cell seam.  Put \(y=\sqrt{N\ell}\) and define the
equivalent pointwise endpoint shifts

\[
 p_s(y)=\sqrt{y^2+s}-y,\qquad
 n_s(y)=y-\sqrt{y^2-s}.
\tag{159.MA31}
\]

On the circle, rather than only within one chosen half-cell,

\[
 \|\delta+p_s(y)\|=\|\sqrt{N\ell+s}\|,
 \qquad
 \|\delta-n_s(y)\|=\|\sqrt{N\ell-s}\|.
\tag{159.MA31a}
\]

Choose the nearest integer \(m\) to the square root on the right and put
\(t=m^2-N\ell\).  The mean value theorem gives

\[
 |t\mp s|\asymp K\|\sqrt{N\ell\pm s}\|.
\tag{159.MA31b}
\]

The supported \(m\)-hull has length \(O(K)<N\).  For a fixed nonzero
integer \(t\), the accepted root estimate therefore gives

\[
 \#\{\ell\asymp M:m^2-N\ell=t\}
 \ll_\varepsilon X^\varepsilon\sqrt{(N,t)}.
\tag{159.MA32}
\]

If \(I\) is an integer interval of length \(D\leq V/2\) lying at
\(|t|\asymp V\), then

\[
\begin{aligned}
 \sum_{t\in I}\sqrt{(N,t)}
 &\leq
 \sum_{d\mid N}\sqrt d\,\#\{t\in I:d\mid t\}\\
 &\ll_\varepsilon (D+\sqrt V)X^\varepsilon.
\end{aligned}
\tag{159.MA33}
\]

Indeed, the terms \(D/d\) sum to \(D X^\varepsilon\), and a divisor of a
nonzero \(t\) in this interval is at most \(O(V)\), so all rounding terms
sum to \(O(\sqrt V X^\varepsilon)\).  For shells reaching zero, the
accepted small-defect count adds only \(O((D+\sqrt M)X^\varepsilon)\).

Take dyadic shells

\[
 |t\mp s|\asymp 2^mK/J.
\tag{159.MA34}
\]

Equation (159.MA30) contributes \(O(2^{-2m})\), while (159.MA33)
contributes \(O(2^mK/J+\sqrt V)X^\varepsilon\).  Summing the shells before
and after they reach zero gives

\[
 \sum_{\ell\asymp M}
 \left[
 \mathfrak F_J(\delta(\ell)+p_s(y))+
 \mathfrak F_J(\delta(\ell)-n_s(y))
 \right]
 \ll_\varepsilon
 \left(\frac KJ+\sqrt V+\sqrt M+1\right)X^\varepsilon.
\tag{159.MA35}
\]

If an interval clips at \(\delta=\pm1/2\), put \(m=2k\pm1\).  Near that
edge,

\[
 |m^2-4N\ell|\asymp K\,\|\delta\mp1/2\|.
\tag{159.MA36}
\]

There is no exact half-integer tie, and the same small-defect root argument
modulo \(4N\) costs \(O((K/J+1)X^\varepsilon)\).  Thus cell-edge clipping
does not add an unprinted endpoint loss.  Equations (159.MA35)--(159.MA36)
prove (159.MA3), including exact hard-boundary atoms.  They also show why
the prior favorable replacement \(M/J\) was not the literal ledger.

To make (159.MA3) at most \(M^{3/4}X^\varepsilon\), this unsigned route
requires (159.MA4).  These conditions are capacities of this truncation
method.  Failure of \(V\leq M^{3/2}\) is not a lower bound for the signed
boundary contribution.

### 3.4 Pointwise exponent pairs with every restored power

For \(q\ne0\), splitting into the two odd residue progressions and applying
an exponent pair \((\kappa_0,\lambda_0)\) gives, uniformly for every proper
subinterval,

\[
 \sum_{\ell\in I}\chi_4(\ell)e(q\sqrt{N\ell})
 \ll_\varepsilon
 |q|^{\kappa_0}N^{\kappa_0/2}
 M^{\lambda_0-\kappa_0/2+\varepsilon}.
\tag{159.MA37}
\]

Here the phase parameter is \(\mathcal T=|q|K\), and
\(\mathcal T/M=|q|\sqrt{N/M}\geq1\), so the source convention is
satisfied.  The linear phases introduced by the mod-four split do not
alter the higher derivative class.

The exact coefficient bounds (159.MA18) show two lawful but distinct
treatments.

1. Direct Abel summation regards the moving endpoint factor as a
   coefficient.  Its variation is \(O(\alpha)\), so the nonzero-mode
   aggregate is bounded by

   \[
    N^{\kappa_0/2}M^{\lambda_0-\kappa_0/2+\varepsilon}
    \left(J^{\kappa_0}+\alpha J^{\kappa_0+1}\right).
   \tag{159.MA38}
   \]

2. In a favorable smooth model one may retain the endpoint exponential in
   the phase, preserving the \(1/|h|\) coefficient.  This gives the smaller
   benchmark

   \[
    N^{\kappa_0/2}M^{\lambda_0-\kappa_0/2+\varepsilon}
    J^{\kappa_0}.
   \tag{159.MA39}
   \]

   The literal phase then has a small endpoint perturbation and is not an
   exact unperturbed reciprocal transform.  Equation (159.MA39) is used
   only as the most favorable pointwise-source capacity.

Because \(V>M^{3/4}(\log(2X))^A\), (159.MA4) implies

\[
 \alpha J_{\mathrm{lit}}=\frac{V}{M^{3/4}}>1.
\tag{159.MA40}
\]

Thus the narrow-band factor cannot reduce the high-frequency end once the
literal boundary error has been restored.

For (159.MA21), substituting \(J=J_{\mathrm{lit}}=N^{1/2}M^{-1/4}\) into
(159.MA39) gives

\[
\begin{aligned}
 &N^{195/1592}M^{745/1592}
 (N^{1/2}M^{-1/4})^{195/796}\\
 &\hspace{25mm}=
 N^{195/796}M^{1295/3184},
\end{aligned}
\tag{159.MA41}
\]

which is (159.MA5).  Its scalar form is (159.MA6).  The literal direct-Abel
bound (159.MA38) has the additional factor
\(1+V/M^{3/4}\).

This must be reconciled with the Round-158 favorable-model threshold.  If
one replaces the literal sampled boundary cost in (159.MA3) by the
unproved equidistributed cost \(M/J\), then one may take \(J=M^{1/4}\), and
(159.MA39) becomes

\[
 N^{195/1592}M^{1685/3184+\varepsilon}.
\tag{159.MA42}
\]

After the atom scale, (159.MA42) is

\[
 \left(\frac{N^{390}}{M^{703}}\right)^{1/3184}X^\varepsilon,
\tag{159.MA43}
\]

giving \(M\geq N^{390/703}\).  Equation (159.MA6) is more restrictive
because it pays the literal root-count boundary incidence; it is a
method-specific capacity, not a replacement theorem and not a universal
barrier.  Both thresholds lie strictly above \(N^{1/2}\).

For comparison, Bourgain's untransformed pair at \(J=J_{\mathrm{lit}}\) gives

\[
 N^{13/84}M^{181/336+\varepsilon},
\qquad
 M^{71}\geq N^{52}
\tag{159.MA44}
\]

as its target condition, also outside the cone.  No audited pointwise pair
therefore closes even the subrange \(V\leq M^{3/2}\) where (159.MA3) is
target-safe.

### 3.5 The exact shifted-mode \(B\)-process is a reciprocal self-return

For every integer \(\ell\), including even \(\ell\),

\[
 \chi_4(\ell)=\frac{e(\ell/4)-e(-\ell/4)}{2i}.
\tag{159.MA45}
\]

Let \(q=h+1\ne0\) and first take a smooth compactly supported amplitude
\(A\) satisfying (159.MA10).  The two phases are

\[
 F_{\sigma,q}(x)=q\sqrt{Nx}+\frac{\sigma x}{4},
 \qquad \sigma\in\{1,-1\},
\tag{159.MA46}
\]

with coefficient \(\sigma/(2i)\).  In Poisson frequency \(n\), a stationary
point satisfies

\[
 F'_{\sigma,q}(x)=n,\qquad
 d:=4n-\sigma,\qquad qd>0,
\tag{159.MA47}
\]

and hence

\[
 x_{q,d}=\frac{4q^2N}{d^2},\qquad
 F_{\sigma,q}(x_{q,d})-nx_{q,d}=\frac{q^2N}{d}.
\tag{159.MA48}
\]

Moreover

\[
 F''_{\sigma,q}(x)=-\frac{q\sqrt N}{4x^{3/2}},\qquad
 |F''_{\sigma,q}(x_{q,d})|^{-1/2}
 =\frac{4\sqrt2\,|q|N^{1/2}}{|d|^{3/2}}.
\tag{159.MA49}
\]

When \(\sigma=1\), \(d\equiv3\pmod4\); when \(\sigma=-1\),
\(d\equiv1\pmod4\).  Thus \(\sigma=-\chi_4(d)\), and the two stationary
branches recombine as

\[
\begin{aligned}
 \sum_\ell \chi_4(\ell)A(\ell)e(q\sqrt{N\ell})
 ={}&2\sqrt2\,i\,e(-\operatorname {sgn}(q)/8)
 |q|N^{1/2}\\
 &\times\sum_{\substack{d\ \mathrm{odd}\\qd>0}}
 \frac{\chi_4(d)}{|d|^{3/2}}
 A\!\left(\frac{4q^2N}{d^2}\right)
 e\!\left(\frac{q^2N}{d}\right)
 +\mathcal E_q.
\end{aligned}
\tag{159.MA50}
\]

Only \(|d|\asymp |q|Q_0\) occurs, where

\[
 Q_0=\sqrt{N/M}.
\tag{159.MA51}
\]

With a compact smooth buffer, the ordinary nonstationary and one-term
stationary remainders have the standard capacity
\(M/\sqrt{|q|K}+\log(2X)\).  After the Fourier coefficient is restored and
summed over \(q\), this is \(O(M^{3/4}X^\varepsilon)\).  At a hard profile
or moving-band transition, (159.MA50) is not invoked silently: one uses
Abel summation and retains its endpoints, or absorbs the endpoint
oscillation into the phase and accepts a perturbed reciprocal phase.

The exact constant and \(e(-\operatorname {sgn}(q)/8)\) in (159.MA50)
are conditional on the printed Poisson convention and have not received
an independent normalization-seam review in this task.  The stationary
point, reciprocal phase, character, dual length, and absolute amplitude
in (159.MA47)--(159.MA51) are convention-independent.  Formula
(159.MA50) supplies no gain by itself.  If a reciprocal exponent
pair \((\kappa,\lambda)\) is applied to its dual interval, then

\[
 \mathcal T_d\asymp |q|K,\qquad
 \frac{\mathcal T_d}{|q|Q_0}=M,
\tag{159.MA52}
\]

and the result is

\[
 |q|^{\lambda-1/2}N^{\lambda/2-1/4}
 M^{3/4+\kappa-\lambda/2+\varepsilon}.
\tag{159.MA53}
\]

This is exactly the direct square-root bound for

\[
 B(\kappa,\lambda)
 =\left(\lambda-\frac12,\kappa+\frac12\right).
\tag{159.MA54}
\]

In particular, \(B(18/199,593/796)=(195/796,235/398)\), so the reciprocal
route reproduces (159.MA41).  Bourgain's pair is fixed by \(B\) and also
reproduces its direct capacity.

For \(q=1\), (159.MA50) has exactly the phases
\(e(N/(4n-1))\) and \(e(N/(4n+1))\).  This is the principal reciprocal
carrier already recorded in
`M9-M1-lower-cone-t1-squarefree-reciprocal-bprocess-self-return-obstruction`
and in the Round-154 direct root-wave method obstruction.  The factor
\(q^2\) for other modes creates a family of the same interface, not a new
independent cancellation.  The coefficients for \(q=1\) and \(q=-1\)
are not equal or conjugate merely from (159.MA16), so they may not be
paired away.

### 3.6 Incomplete quadratic, character, and Hilbert interfaces

There is also an exact finite projector

\[
 \mathbf1_{N\mid t}\chi_4(t/N)
 =-\frac{i}{2N}
 \sum_{\substack{a\bmod4N\\a\ \mathrm{odd}}}
 \chi_4(a)e_{4N}(at).
\tag{159.MA55}
\]

Reintroducing \(r=k^2-N\ell\) and inserting (159.MA55) produces quadratic
\(k\)-phases modulo \(4N\) and geometric \(r\)-intervals.  Even after
granting the joint BV needed to move the literal quotient profile,
residual phase, cell clipping, and hard transitions through the two Abel
steps, (159.MA22) gives

\[
 |T_U(V)|\ll_\varepsilon N^{1/2}X^\varepsilon.
\tag{159.MA56}
\]

The calculation is the same restored projector ledger as in the permitted
Round-158 audit: the geometric interval contributes
\(|1-e_{4N}(a)|^{-1}\ll N/\min(a,4N-a)\), the incomplete quadratic sum
contributes \(\sqrt{N(a,N)}X^\varepsilon\), the projector contributes
\(N^{-1}\), and

\[
 \sum_{\substack{a\bmod4N\\a\ \mathrm{odd}}}
 \frac{(a,N)^{1/2}}{\min(a,4N-a)}
 \ll_\varepsilon X^\varepsilon.
\tag{159.MA57}
\]

Thus (159.MA56), after the atom scale, is
\(N^{1/2}M^{-3/4}X^\varepsilon\), target-sized only for
\(M\geq N^{2/3}\).  If the joint BV grant fails at a moving cell edge, the
literal application stops earlier; it never improves (159.MA56).

One may instead insert (159.MA50) for all \(q\) and try to sum the phases
\(e_d(Nq^2)\) quadratically in \(q\).  Muellner's theorem then supplies at
best the same square-root completion scale after the dual amplitude and
the full \(d\)-sum are restored; gcd spikes and the low modes can add the
unsigned \(V\)-capacity.  Further cancellation would have to be joint in
\((q,d)\) and retain the moving Fourier coefficients.  No audited theorem
has that statement.

The fixed character \(\chi_4\) alone closes only (159.MA28).  For
\(q\ne0\), exact character Poisson is precisely (159.MA50), so it restores
the reciprocal character rather than deleting it.  Growing-modulus
character theorems do not apply to a conductor-four character placed on
the quotient after the \(N\)-divisibility selector.

Finally, Montgomery--Vaughan cannot average the modes in (159.MA24): the
project needs a pointwise value at fixed \(N\), while its theorem averages
a continuous parameter; the relevant square-root or reciprocal
frequencies also have exact and near collisions and no audited uniform
real-line separation after grouping.  Invoking it would require precisely
the missing multimode energy theorem.

## 4. First doubtful or unproved step

The exact ordered frontier is as follows.

1. Vaaler's fixed-interval theorem is legal pointwise in \(k\), but its
   integral excess does not estimate the sampled moving-boundary error.
   The first extra argument required is the root-incidence derivation
   (159.MA31)--(159.MA36).  It yields (159.MA3), not the favorable \(M/J\)
   surrogate.
2. When \(V>M^{3/2}\), the first remaining unproved step is a signed
   estimate for the exact hard-boundary/Fejer incidences.  The available
   unsigned root bound has the \(\sqrt V\) term and is above the raw target.
3. When \(V\leq M^{3/2}\), choose \(J=J_{\mathrm{lit}}\) so that the boundary
   error is target-safe.  The first remaining unproved step is then a
   genuinely joint estimate for the \(J\) nonzero shifted modes with their
   moving coefficients.  Pointwise exponent pairs followed by absolute
   Fourier summation give (159.MA6); the \(B\)-process returns the existing
   reciprocal interface; incomplete quadratic completion gives
   (159.MA56).

This is a precise method and source obstruction.  It does not prove that
\(T_U(V)\) is large, that a future joint theorem cannot work, or that the
common-profile compression is false.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| `literal_full_Abel_six_line_package` | **PASS / SCOPE.** The three positive and three negative lines are kept together through (K158.7)--(K158.8); no source bound is applied to an isolated outer, moving, or profile-difference piece. The selected scalar remains conditional on the independent algebra review. |
| `quotient_profile_not_boundary_profile` | **PASS.** Every analytic formula uses \(w_U(\ell)\) or \(\widetilde w_U(\ell)\). Neither Round-158 boundary profile is substituted, and no isolated-trace statement is changed. |
| `integral_phase_shift` | **PASS.** Equation (159.MA23) uses \(\kappa(\ell)\in\mathbb Z\); no approximate phase deletion is made. |
| `variable_residual_band` | **PASS.** Equations (159.MA13)--(159.MA18) retain \(r=-\delta(2k+\delta)\), both defect signs, clipping, half-open endpoints, and their \(k\)-variation. |
| `chi4_shifted_zero_mode` | **PASS / TARGET-SAFE.** The exceptional index is \(h=-1\). Equations (159.MA26)--(159.MA28) retain \(\chi_4\), including zero on even \(\ell\), and prove the raw \(O(X^\varepsilon)\) bound. |
| `Fourier_truncation_and_boundary_errors` | **PASS / METHOD OBSTRUCTION.** \(J\) is the polynomial degree. The literal Fejer incidence is (159.MA3); the exact shell/root derivation is (159.MA31)--(159.MA36). The favorable \(M/J\) surrogate is separated explicitly in (159.MA42)--(159.MA43). |
| `N_M_V_power_and_scalar_target` | **PASS.** Raw versus scalar normalization is (159.MA11). Literal masked BD capacity is (159.MA5)--(159.MA6); direct moving-coefficient variation costs an additional \(1+V/M^{3/4}\); incomplete completion restores \(N^{1/2}M^{-3/4}\). |
| `source_theorem_common_profile_match` | **NO MATCH FOR THE TARGET.** Vaaler matches each fixed cell interval but not its sampled error without (159.MA3); Bourgain/TTY match individual smooth modes only; Muellner matches unweighted quadratic intervals plus proved BV; Montgomery--Vaughan has the wrong averaging interface; the Huxley card is unaudited. |
| `upper_capacity_vs_signed_bound` | **PASS.** Equations (159.MA5), (159.MA42), (159.MA44), and (159.MA56) are capacities of named upper-bound routes. Their failure is not a lower bound. The support count remains unsigned. |
| `external_scalar_and_downstream_scope` | **PASS / QUARANTINED.** The \(M^{-3/4}\) atom is restored in every conclusion. This audit does not close the external \(B_{1,U}(1)\) seam, zero/fold subtraction normalization, any other \(D,d,L,t\) owner, cross term, M2 component, endpoint uniformity, M9, bridge, quarter target, or global exponent. |

No computation was used.

## 6. Dependencies and exact artifacts used

### Permitted repository evidence

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `strategy/round159_d1_abel_commutator_recombination_strategy.md`
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate/barrier_packet.md`
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate/candidates/conductor_round159_common_profile_seed.md`
- `proofs/kernels/m9_m1_d1_paired_interior_cell_trace_reduction.md`
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/reports/cell_trace_source_audit.md`
- `sources/bourgain_2017_exponent_pair.md`
- `sources/huxley_2003.md`
- `sources/montgomery_vaughan_1974.md`

The proof-graph comparison uses the accepted Round-154
root-defect/logarithmic-collar and reciprocal-\(B\)-process self-return
statements as recorded inside the permitted `state/proof_obligations.yml`.
No nonpermitted Round-154 artifact was opened.

### Primary sources

1. Jeffrey D. Vaaler, [*Some extremal functions in Fourier analysis*](https://doi.org/10.1090/S0273-0979-1985-15349-2), Bull. Amer. Math. Soc. 12 (1985), Theorems 18--19.
2. Jean Bourgain, [*Decoupling, exponential sums and the Riemann zeta function*](https://arxiv.org/abs/1408.5794v2), J. Amer. Math. Soc. 30 (2017), Theorem 6 and Section 5.
3. Terence Tao, Tim Trudgian, and Andrew Yang, [*New exponent pairs, zero density estimates, and zero additive energy estimates: a systematic approach*](https://arxiv.org/html/2501.16779v1), Definitions 11--12, Lemmas 13--15, Table 1.
4. Clemens Muellner, [*The Rudin--Shapiro Sequence and Similar Sequences Are Normal Along Squares*](https://doi.org/10.4153/CJM-2017-053-1), Theorem 5.3 and Lemma 5.4.
5. H. L. Montgomery and R. C. Vaughan, [*Hilbert's Inequality*](https://doi.org/10.1112/jlms/s2-8.1.73), J. London Math. Soc. (2) 8 (1974), Theorem 2.
6. M. N. Huxley, [*Exponential sums and lattice points III*](https://doi.org/10.1112/S0024611503014485), Proc. London Math. Soc. 87 (2003), 591--609. Bibliography only; no theorem is imported because the repository card has not audited one.

## 7. Recommended state effect

Recommend **no promotion of the common-profile target and no new strict
range**.

The conductor may retain as candidate evidence, subject to independent
review:

1. the target-safe \(h=-1\) shifted-zero lemma (159.MA26)--(159.MA28);
2. the literal Vaaler/root-incidence ledger (159.MA3)--(159.MA4);
3. the exact stationary phase carrier (159.MA45)--(159.MA54), whose
   \(q=\pm1\) branch is a rederivation of the already recorded reciprocal
   self-return rather than a new graph node.

Do not promote (159.MA6) or (159.MA56): they are failed method capacities.
Do not reinterpret the stronger method threshold
\(M^{1093}\geq N^{780}\) as a lower bound, a universal exponent-pair
barrier, or a replacement for the prior favorable-model threshold
\(M^{703}\geq N^{390}\).  Do not relabel the Round-154
\(M^{449}\gg R^{780}\) direct-wave range or the fixed-polylogarithmic
root-defect collar as Round-159 progress.

If a terminal campaign label is required from this report, use
`paired_interior_abel_commutator_no_go` in the precise sense “the audited
literal-mask method and source interfaces do not prove the target or a new
strict owner-complete range.”  No conclusion transfers downstream.
