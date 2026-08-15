# Blind addendum: finite character Dirichlet kernel

Campaign: `m9-m1-beta-transition-connector`  
Task: independent elementary-kernel addendum  
Role: statement-only blind rederivation  
Status: candidate evidence only

## 1. Result

The proposed elementary package is true.  Uniformly for (Q\ge1),

\[
 D_M^\chi(\theta)=\sum_{q\le M}\chi_4(q)e^{-iq\theta}
\]

satisfies

\[
 \sup_{0\le M\le Q}|D_M^\chi(\theta)|
 \ll \min\!\left(Q,1+|\cos\theta|^{-1}\right),                 \tag{A.1}
\]

with the right side interpreted as (Q) at a zero of (\cos\theta), and

\[
 \int_0^{2\pi}\sup_{0\le M\le Q}|D_M^\chi(\theta)|\,d\theta
 \ll \log(2Q).                                                   \tag{A.2}
\]

Also, for every integer (D_0) and odd integer (q),

\[
 |D_0-q/2|\ge\frac12.                                           \tag{A.3}
\]

These statements do not alone estimate the actual beta-transition
operator.  The (L^1) gain is usable only after an exact representation
supplies genuine integration in (\theta) with controlled density and a
uniform discrete-BV amplitude.

## 2. Exact statement and hypotheses

Let (\chi_4(2m)=0), (\chi_4(4m+1)=1), and
(\chi_4(4m+3)=-1).  Take (Q\ge1), with (M) ranging over nonnegative
integers (M\le\lfloor Q\rfloor), and take (\theta\in\mathbb R/2\pi\mathbb Z).
Then (A.1)--(A.2) hold with absolute constants.

More generally, on an arbitrary real interval (I),

\[
 \int_I\sup_{M\le Q}|D_M^\chi(\theta)|\,d\theta
 \ll \left(1+\frac{|I|}{2\pi}\right)\log(2Q).                  \tag{A.4}
\]

For integers (L\le U\le Q) and a complex sequence (a_q), define

\[
 \|a\|_{\mathrm{BV}[L,U]}
 :=|a_U|+\sum_{q=L}^{U-1}|a_{q+1}-a_q|.
\]

Then

\[
 \left|\sum_{q=L}^{U}\chi_4(q)e^{-iq\theta}a_q\right|
 \ll \min\!\left(Q,1+|\cos\theta|^{-1}\right)
       \|a\|_{\mathrm{BV}[L,U]},                               \tag{A.5}
\]

and, when (a_q) is independent of (\theta), integration over one full
period gives

\[
 \int_0^{2\pi}
 \left|\sum_{q=L}^{U}\chi_4(q)e^{-iq\theta}a_q\right|d\theta
 \ll \log(2Q)\|a\|_{\mathrm{BV}[L,U]}.                         \tag{A.6}
\]

For a (\theta)-dependent amplitude, (A.6) requires an integrable uniform
majorant for its discrete-BV norm; it is not an automatic consequence of
pointwise BV at each (\theta).

## 3. Proof or derivation

Only odd indices contribute.  If (K=\lfloor(M-1)/2\rfloor), then

\[
 D_M^\chi(\theta)
 =e^{-i\theta}\sum_{k=0}^{K}(-e^{-2i\theta})^k.
\]

The trivial bound is (K+1\le Q).  Away from (\cos\theta=0), the
geometric-sum formula gives

\[
 |D_M^\chi(\theta)|
 \le \frac{2}{|1+e^{-2i\theta}|}
 =\frac1{|\cos\theta|}.
\]

Taking the smaller bound proves (A.1).  Near each of the two zeros of
(\cos\theta) in a (2\pi)-period, one has
(|\cos\theta|\asymp|\theta-\theta_0|).  Therefore

\[
 \int_0^c\min(Q,t^{-1})\,dt\ll1+\log Q,
\]

while the complement contributes (O(1)).  This proves (A.2), and
periodic subdivision proves (A.4).

For (A.5), let

\[
 B_m=\sum_{q=L}^{m}\chi_4(q)e^{-iq\theta}.
\]

Writing (B_m) as a difference of two prefix sums and applying (A.1)
gives

\[
 |B_m|\ll\min(Q,1+|\cos\theta|^{-1}).
\]

Discrete summation by parts,

\[
 \sum_{q=L}^{U}\chi_4(q)e^{-iq\theta}a_q
 =B_Ua_U+\sum_{q=L}^{U-1}B_q(a_q-a_{q+1}),
\]

proves (A.5); integration and (A.2) prove (A.6).

Finally, if (q) is odd then (q/2\in\mathbb Z+1/2), whereas
(D_0\in\mathbb Z).  Their distance is a positive half-integer, proving
(A.3), with equality possible.

## 4. First doubtful or unproved step

The first unproved seam is the passage from the exact transition formula
to a (\theta)-average of the form (A.6).  One must identify the actual
phase map (\theta=\theta(\text{radial, Mellin, scale variables})), prove
that its pushforward has controlled density even at degeneracies, and
establish a uniform discrete-BV bound for the complete signed amplitude
with actual profiles, floors, top star, connector, and radial integration.
None of these facts is contained in the elementary kernel lemma.

## 5. Control tests and outcomes

**Interval/BV scope.**  The logarithmic estimate is over a complete
(\theta)-period, or over intervals via (A.4).  It is not a pointwise
logarithmic bound: at (\theta=\pi/2\pmod\pi), the maximal partial sum can
have size (\asymp Q).  Discrete BV is required in the summation index on
the exact finite support; a moving hard edge contributes its jump and an
equality half-star contributes its actual sampled value.

**Exact versus near resonance.**  Equation (A.3) excludes the exact lattice
identity (D_0=q/2) for odd (q), but the sharp gap is only (1/2).  It
does not exclude a near-resonant continuous phase, nor does it give decay
after rescaling by a large or small parameter.

**Signed versus unsigned/adversarial.**  The character moves the geometric
kernel singularity to (\cos\theta=0).  At that singularity an adversarial
phase can neutralize (\chi_4), producing coherent size (Q).  Moreover,
the analogous ordinary Dirichlet kernel also has logarithmic (L^1) norm.
Thus (A.2) alone does not distinguish the desired signed operator from a
false unsigned analogue; the surrounding physical measure and amplitude
must supply the distinguishing structure.

## 6. Dependencies and exact artifacts used

- The elementary statement supplied in the Round-26 addendum assignment.
- `protocol.md` and `state/active_campaign.yml` for scope and reporting
  requirements.

No claimant report, other Round-26 report, numerical experiment, web
source, proof graph, or proof draft was used.

## 7. Recommended state effect

**Promote**, after conductor verification, (A.1)--(A.6) as elementary
finite-kernel and discrete-BV lemmas with the stated interval scope.

**Promote** (A.3) only as an exact-parity separation lemma, not as a
near-resonance estimate.

**Retain open** the actual beta-transition bound.  The elementary package
becomes applicable only after an exact physicalization supplies a
nondegenerate or controlled-density (\theta)-integration and uniform BV
for the complete actual-profile amplitude.
