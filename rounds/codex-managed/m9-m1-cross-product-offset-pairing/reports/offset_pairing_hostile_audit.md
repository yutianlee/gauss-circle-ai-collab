# Hostile audit of paired-offset stability

- Campaign: `m9-m1-cross-product-offset-pairing`
- Round: 12
- Task: `offset_pairing_hostile_audit`
- Role: hostile falsifier
- Status: candidate evidence only; no shared state was edited

## 1. Result

The proposed termwise pairing of product offsets on opposite sides of a
center is false.  More precisely,
let

\[
 C_{D,L}(n;X)=
 \sum_{d:n_X(d)=n}\chi _4(d)w_D(d)
 \mathcal V_{L,H}\!\left(\frac{X-n}{d}\right),
 \qquad
 n_X(d)=d\left\lfloor \frac Xd+\frac12\right\rfloor,
\]

where \(\mathcal V_{L,H}\) is the accepted odd two-sided Vaaler kernel.  If
\(X\) is real, its product centers lie on the integer lattice.  Hence the
only reflection which can pair all centers is

\[
 n\longmapsto 2X-n,
\]

and it preserves the lattice if and only if \(2X\in\mathbb Z\).  Even at an
integral center \(X=N\), where the reflection is legitimate, the divisor
sets

\[
 \mathcal D_\pm(t)=
 \{d:w_D(d)\ne0, d\mid N\pm t, t<d/2\}
\]

need not resemble one another.  The exact paired subtotal is

\[
 \boxed{
 C_{D,L}(N-t;N)+C_{D,L}(N+t;N)
 =\sum_{d\in\mathcal D_-(t)}\chi_4(d)w_D(d)\mathcal V(t/d)
  -\sum_{d\in\mathcal D_+(t)}\chi_4(d)w_D(d)\mathcal V(t/d).}
 \tag{1.1}
\]

Oddness changes the plus-side sign; it does not match the two divisor
sets.  There are exact prime-product controls for which
\(\mathcal D_-(t)\) is a singleton with \(|\mathcal V(t/d)|\gg1\), while
a same-denominator reflected mate is impossible.  The stronger natural
mismatch-norm claim

\[
 \sum_{c_1D/L\le t\le c_2D/L}
 \left|C_{D,L}(N-t;N)+C_{D,L}(N+t;N)\right|
 \gg \frac{D/L}{(\log X)^2}.
 \tag{1.2}
\]

is **not** proved: it requires controlling factorization of both
\(N-t\) and \(N+t\), a shifted-divisor correlation unavailable in the
accepted graph.

Thus oddness alone gives no divisor-set stability.  This is a rigorous
obstruction to naive divisor-preserving termwise pairing, but not by itself
to every separately absolute paired-offset estimate.  It is **not** an
obstruction to all cross-product cancellation:
the signed sum of the mismatches over different offsets may still cancel,
as happens in the accepted exact-square ordered-denominator control.

## 2. Exact statement and hypotheses

Let \(X\asymp Y\) be large,

\[
 Y^{1/4}\ll D\ll Y^{1/2},\qquad
 H\asymp DY^{-1/4},\qquad
 1\ll L\le u_0H,
 \tag{2.1}
\]

where \(u_0>0\) is fixed and small enough that the actual cutoff
\(v_L\) contains a fixed interval on which it is positive and
\(\Phi(h/(H+1))\gg1\).  Let the actual nonnegative spatial profile
\(w_D\) contain a fixed closed interval \(J_D\asymp D\) on which
\(w_D(d)\ge w_0>0\), strictly inside its support.  This includes the
explicit project profile

\[
 W(u)=\eta(u)-\eta(2u),\qquad W(u)=1\quad(3/4\le u\le1),
\]

and, by choosing a shorter interval below \(d\le\lfloor\sqrt X\rfloor\),
also includes the hard top block.  Put

\[
 u_{L,H}(h)=v_L(h)\frac{\Phi(h/(H+1))}{h},
 \qquad
 \mathcal V_{L,H}(z)=\frac4\pi
 \sum_{h>0}u_{L,H}(h)\sin(2\pi hz).
 \tag{2.2}
\]

For an integral center \(N\), define

\[
 P_N(t)=C_{D,L}(N-t;N)+C_{D,L}(N+t;N),
 \qquad t\in\mathbb Z_{>0}.
 \tag{2.3}
\]

Choose fixed \(0<c_1<c_2\) sufficiently small.  The natural quantitative
mismatch conjecture would assert that there are arbitrarily large integral
centers \(N\asymp Y\) such that

\[
 \sum_{c_1D/L\le t\le c_2D/L}|P_N(t)|
 \gg \frac{D/L}{(\log Y)^2},
 \tag{2.4}
\]

and

\[
 \sum_{c_1D/L\le t\le c_2D/L}|P_N(t)|^2
 \gg \frac{D/L}{(\log Y)^2}.
 \tag{2.5}
\]

To prove this, one would need a construction imposing that, for every
counted offset,
\(N-t=dp\) with \(d,p\equiv1\pmod4\), \(d\in J_D\), and \(p\) outside
the spatial support, while \(N+t\) has no supported divisor.  Consequently
each counted \(P_N(t)\) is a single actual-profile term of fixed sign and
size \(\gg1\).  Section 3.3 proves the one-sided singleton family and
identifies why simultaneous reflected emptiness is an additional unproved
shifted-correlation assertion; (2.4)--(2.5) are therefore not claimed as
lemmas.

## 3. Proof and derivation

### 3.1 Exact reflection algebra and the lattice obstruction

For \(n=N-t\), every participating denominator satisfies
\(d\mid N-t\) and \(t<d/2\).  For \(n=N+t\), it satisfies
\(d\mid N+t\) and the same nearest-product inequality.  Since
\(\mathcal V\) is odd,

\[
 \mathcal V((N-(N+t))/d)=\mathcal V(-t/d)=-\mathcal V(t/d),
\]

which proves (1.1).  Cancellation requires equality of the two weighted
character-divisor measures, not merely oddness of the kernel.

If \(X\notin\tfrac12\mathbb Z\), the reflected point \(2X-n\) is not an
integer for every integer \(n\).  More generally, writing
\(k=\lfloor2X\rfloor\) and \(\lambda=2X-k\), the integer reflection
\(n\mapsto k-n\) changes an offset \(u=X-n\) to \(\lambda-u\), not
\(-u\).  The alternative \(n\mapsto k+1-n\) changes it to
\((\lambda-1)-u\).  Therefore no exact odd-kernel pairing exists at a
generic real center.  At a half-integer center the lattice reflection
exists but the divisibility mismatch below remains unchanged.

### 3.2 Singleton unmatched fibers

Take primes

\[
 d\equiv p\equiv1\pmod4,qquad d\in J_D,qquad p
 \text{ outside the support of }w_D,
\]

and put \(n=dp\).  The four divisors of \(n\) are \(1,d,p,dp\), so
\(d\) is the unique supported divisor and \(\chi_4(d)=1\).  For a center
\(N=n+t\) with

\[
 c_1D/L\le t\le c_2D/L,
\]

the nearest-product inequality \(t<d/2\) holds.  On a fixed subinterval of
these \(t\), all relevant angles lie in a fixed subinterval of
\((0,\pi/2)\), and the nonvanishing actual profiles give

\[
 \mathcal V_{L,H}(t/d)
 \gg \frac{t}{D}
 \sum_{h\asymp L}v_L(h)\Phi(h/(H+1))gg1.
 \tag{3.1}
\]

Thus \(C(n;N)\gg1\).  If additionally \(N+t=n+2t\) has no supported
divisor, then \(C(N+t;N)=0\) and \(|P_N(t)|\gg1\).

### 3.3 There are many such unmatched offsets

Let \(\mathcal P_Y\) be the set of the above unique products \(n=dp\) in
a fixed interval of length \(\asymp Y\).  The fixed-modulus prime number
theorem in the progression \(1\pmod4\) gives

\[
 |\mathcal P_Y|\gg \frac{Y}{(\log Y)^2}.
 \tag{3.2}
\]

The primary source sufficient for (3.2) is Bennett--Martin--O'Bryant--
Rechnitzer, *Explicit bounds for primes in arithmetic progressions*,
arXiv:1802.00085.  Their displayed estimate

\[
 |\vartheta(x;4,1)-x/2|<x/(160\log x),\qquad x\ge8\cdot10^9,
\]

applies because the modulus is the fixed \(q=4\), the residue is coprime,
the interval endpoint ratios are fixed, and all endpoints tend to infinity.

For a given \(n\in\mathcal P_Y\), let

\[
 I_n=\{N\in\mathbb Z:c_1D/L\le N-n\le c_2D/L\}.
\]

Then \(|I_n|\asymp D/L\).  Count bad incidences

\[
 \mathfrak B=\{(n,N,d):n\in\mathcal P_Y, N\in I_n,
               w_D(d)\ne0, d\mid 2N-n\}.
\]

For fixed \((n,d)\), the congruence \(d\mid2N-n\) has at most
\(O(1+(D/L)/d)=O(1)\) solutions in \(I_n\), because \(d\asymp D\) and
\(D/L\le D\).  There are \(O(D)\) possible supported denominators, while
\(|\mathcal P_Y|\gg Y/(\log Y)^2\).  Hence

\[
 |\mathfrak B|\ll D|\mathcal P_Y|,
 \]

which alone is not yet useful when \(D/L\ll D\).  The divisor congruence
must instead be counted from the center side.  For each \(N\), the plus
products \(m=2N-n\) lie in an interval of length \(\asymp Y\), but in the
short reflected window only \(O(D/L)\) integers occur; divisor
multiplicity gives only \(O((D/L)Y^\varepsilon)\) possible bad offsets.
This is target-sized, so it does not prove that a positive proportion of
the prime products are unmatched at every center.

To obtain the claimed existence statement without assuming a shifted-prime
or shifted-divisor theorem, enlarge the prime-product family by excluding
the plus-side divisor incidences before averaging.  For each supported odd
\(d'\), the simultaneous conditions

\[
 n=dp,qquad n+2t=d'm',qquad
 c_1D/L\le t\le c_2D/L
 \tag{3.3}
\]

put \(dp\) in one residue class modulo \(d'/(2,d')=d'\).  If \(d'=d\),
then (3.3) is impossible for odd \(d\), since it would require
\(d\mid2t\) while \(0<2t<d\).  If \(d'\ne d\), the assertion that the
union of these moving residue classes removes only a fixed fraction of the
prime products is a nontrivial shifted-prime distribution statement and is
not supplied by (3.2).

Therefore the last sentence of the theorem in Section 2 -- simultaneous
prime-product density and an empty reflected fiber for \(\gg D/L\)
offsets at one center -- is **not proved** by the available elementary
count.  What is rigorously proved without an imported correlation theorem
is the stronger local falsifier needed against a deterministic pairing
identity: for any admissible singleton product \(n=dp\) and any
\(t\in[c_1D/L,c_2D/L]\), choose \(N=n+t\); the same-denominator reflected
match is impossible, and a termwise rule pairing \(d\) with itself fails
exactly.  It is also elementary to choose at least one \(t\) for which
\(n+2t\) is prime (hence has no supported divisor) only under an unproved
prime-pair assertion, so that stronger infinite family must not be claimed.

Accordingly, (2.4)--(2.5) are **not established** by this argument.  They
are the natural mismatch-norm conjecture exposed by the hostile audit, and
they require a shifted-divisor correlation theorem.  The certified result
of this report is the exact identity (1.1), the generic-center lattice
obstruction, and the no-go for divisor-preserving termwise pairing.

### 3.4 Controls beyond singleton products

**Exact squares.**  At \(X=N=y^2\), the exact product \(n=N\) vanishes
because \(\mathcal V(0)=0\); it gives no paired saving for \(t>0\).  The
accepted family \(d=y-s\), even \(s\), has
\(n=y^2-s^2\) and alternating \(\chi_4(y-s)\).  Its \(O(1)\) subtotal is
cancellation among different negative offsets, not cancellation with
the reflected products \(y^2+s^2\).

**Highly composite products.**  If \(n\) is a product of primes
\(1\pmod4\), then every divisor has \(\chi_4=+1\).  The full divisor
fiber is sign-locked; reflection to \(2N-n\) has unrelated factorization.
High divisor multiplicity therefore makes equality of the two weighted
measures less, not more, automatic.

**Endpoint.**  For \(D=y=\lfloor\sqrt X\rfloor\), the support is
\([y/2,y]\) and the actual profile equals one on \([3y/4,y]\).  Reflection
does not preserve the moving cutoff or the unique top endpoint \(d=y\).
Any stability assertion must include this one-sided seam explicitly.

**Actual versus adversarial profile.**  The failures above use a
nonvanishing plateau of the actual fixed profile; no adversarial spatial
weight is introduced.  Replacing \(w_D\) by arbitrary signs only makes
termwise pairing less plausible and is not needed for the no-go.

## 4. First doubtful or unproved step

The first genuinely unproved step is an averaged signed estimate for (1.1)
over distinct offsets.  Oddness reduces the problem to the discrepancy of
two reflected, truncated character-divisor measures, but no accepted
lemma bounds

\[
 \sum_t\left(
 \sum_{d\mid N-t}\chi_4(d)w_D(d)\mathcal V(t/d)
 -\sum_{d\mid N+t}\chi_4(d)w_D(d)\mathcal V(t/d)
 \right)
\]

at the required scale.  Proving the proposed mismatch lower bound
(2.4), or proving cancellation in the signed sum without taking the inner
absolute values, both require information on shifted divisor correlations
that is absent from the current graph.  In particular, the prime number
theorem in one fixed progression does not control simultaneous
factorization of \(n\) and \(n+2t\).

## 5. Required controls and outcomes

1. **Unmatched fiber: pass.**  A singleton supported divisor \(d\) below
   \(N\) has no same-denominator reflected mate because \(d\mid N-t\) and
   \(d\mid N+t\) would force \(d\mid2t\), impossible when \(0<2t<d\).

2. **Prime product: pass, scoped.**  Products \(dp\) with
   \(d,p\equiv1\pmod4\) give an actual-profile singleton of fixed sign.
   A positive-density simultaneous assertion for the reflected fiber is
   not proved and is explicitly withheld.

3. **Exact square: pass.**  The center fiber vanishes by kernel oddness;
   the known useful cancellation is across different one-sided offsets,
   so it refutes the claim that all cross-product cancellation is
   impossible.

4. **Highly composite: pass.**  Products of primes \(1\pmod4\) have
   sign-locked divisor fibers.  Reflection supplies no multiplicative
   relation.

5. **Endpoint: pass.**  The one-sided top support and the included endpoint
   are not invariant under reflected product pairing.

6. **Generic center: pass.**  Unless \(2X\in\mathbb Z\), reflection about
   \(X\) does not preserve integer product centers; a fractional offset
   remains in the kernel.

7. **Actual profile: pass.**  The singleton construction lies on the
   unit plateau of the accepted profile and uses the actual Vaaler
   nonvanishing range.  No arbitrary coefficient replacement occurs.

8. **Signed versus unsigned: pass.**  The no-go concerns deterministic
   termwise pairing.  Taking absolute values in \(t\) would demand the
   unproved mismatch norm; keeping the outside signed sum leaves a viable
   cancellation mechanism.

9. **Numerical use: none.**  The report is analytical.  No finite test is
   used as proof.

## 6. Dependencies and exact artifacts used

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `state/best_proof_draft.md`
- `rounds/codex-managed/m9-m1-near-product-character-kernel/synthesis.md`
- `state/control_models.md`
- `rounds/codex-managed/m9-endpoint-fixed-profile-attack/reports/dyadic_profile_certificate.md`
- Bennett, Martin, O'Bryant, Rechnitzer,
  [*Explicit bounds for primes in arithmetic progressions*](https://arxiv.org/abs/1802.00085),
  used only for the one-variable count (3.2), not for a shifted correlation.

No other Round-12 report was read.

## 7. Recommended state effect

**Promote a scoped no-go:** paired-offset oddness does not give termwise
cancellation, because the reflected divisor sets and actual kernel weights
are unrelated; at generic real centers there is not even an exact lattice
reflection.  Same-denominator matching is exactly impossible throughout
the critical window \(0<2t<d\).

**Retain open:** the full cross-product odd-kernel discrepancy estimate and
any quantitative mismatch norm such as (2.4).  The surviving route is an
outside-absolute signed shifted-divisor correlation or ordered-denominator
operator estimate.  Do not infer an obstruction to all cross-product
cancellation from the failure of the naive pairing.
