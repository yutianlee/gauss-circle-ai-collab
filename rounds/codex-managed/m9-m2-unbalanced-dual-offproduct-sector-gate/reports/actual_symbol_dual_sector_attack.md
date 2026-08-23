# Round 125 report: actual-symbol dual-sector attack

Campaign: `m9-m2-unbalanced-dual-offproduct-sector-gate`

Task: `actual_symbol_dual_sector_attack`

Role: discovery

Starting graph SHA-256:
`27bd4173fbdb16e5689595a02d42d82ffa8bb514b4610ea745ce2da6e2b8b152`

## 1. Result

### Joint Gram lemma, one-sided target, and a curvature-packet no-go

Put

$$
 B_{p,n}:=\sum_{0\le a<H}b_{p,n+a},
 \qquad
 \mathcal E_{\rm eq}:=C_H\sum_p\sum_n|B_{p,n}|^2,
$$

and retain the actual quarter character before forming the full block:

$$
 \mathcal E_\chi
 :=C_H\sum_n\left|\sum_p\chi _4(p)B_{p,n}\right|^2.
\tag{125.1}
$$

Literal zero extension and the exact half-open block convention give the
endpoint-complete identities

$$
 \boxed{\mathcal E_{\rm eq}=\mathcal D_0+
        \mathcal S_{\rm eq}^{\ne0}},
 \qquad
 \boxed{\mathcal E_\chi=\mathcal D_0+
        \mathcal S_{\rm eq}^{\ne0}+\mathcal S_{\rm neq}},
\tag{125.2}
$$

and consequently

$$
 \boxed{\mathcal S_{\rm neq}=\mathcal E_\chi-\mathcal E_{\rm eq}},
 \qquad
 \boxed{\mathcal S_{\rm off}=\mathcal E_\chi-\mathcal D_0}.
\tag{125.3}
$$

This is the exact joint signed inequality that survives the attack:

$$
 \boxed{\mathcal S_{\rm off}\ge-\mathcal D_0
        \ge-CX^{1/2}.}
\tag{125.4}
$$

Thus the negative part of the complete off-product scalar is already at
the square target.  Any fixed-power violation is necessarily a positive
violation and is equivalently a fixed-power excess of the single positive
but actual-character energy \(\mathcal E_\chi\).  Formula (125.3) also
shows exactly how the unequal-mode sector can cancel the stronger positive
fixed-\(p\) energy: it contributes
\(-\mathcal E_{\rm eq}+\mathcal E_\chi\).  No sectorwise modulus is
legitimate.

For the stronger positive fixed-\(p\) energy there is a complete
coefficient-sensitive curvature bound

$$
 \boxed{
 \mathcal E_{\rm eq}
 \ll_\varepsilon X^\varepsilon
 \min\left\{\frac XD,\frac{D^2}{L}\right\}
 =X^{1/2+\varepsilon}\min\{H,Q\}.}
\tag{125.5}
$$

Both losses tend to infinity in the strict-UNBAL range.  In particular,
the often quoted \(Q\)-deficit is the operative best elementary deficit
only when \(Q\le H\), equivalently \(K/D\ge1\) or
\(3\delta\le1+\ell\).  When \(K/D<1\), the original \(H\)-term triangle
is smaller, and the uniform deficit is \(\min(H,Q)\), not \(Q\) alone.

On a fixed smooth hard-block interior, a first \(k\)-B-process is audited
exactly.  It produces \(Q\) consecutive integer-gradient crossings, each
with coefficient \(-2i/p\), and the reciprocal packet

$$
 B_{p,n}^{\rm prin}
 =-\frac{2i}{p}q_L((X/M)p)
 \sum_{d\in I_{p,n}}
 W\!\left(\frac{Xd}{DM}\right)
 e\!\left(\frac{Mp}{4d}\right),
 \qquad |I_{p,n}|\asymp Q.
\tag{125.6}
$$

Cellwise triangle has energy \(QX^{1/2}=D^2/L\); square-root
cancellation across the complete \(d\)-packet would save exactly the
missing factor \(Q\) and reach the fixed-\(p\) target.  In the full row,
one additionally needs genuine cancellation in the \(p\)-modes, or one
joint substitute for the two cancellations.  A second B-process returns
the original \(H\)-term square-root block.

The proposed second-stage defect algebra requires a material correction.
Because \(p\) is odd, coherence in the squared \(d,d'\) packet is modulo
\(\tfrac12\mathbb Z\), not modulo \(\mathbb Z\).  With
\(\Delta=d'-d\), choose \(A\in\mathbb Z\) nearest to
\(M\Delta/(2dd')\) and put

$$
 E^*=M\Delta-2Add'.
\tag{125.7}
$$

Then

$$
 e\!\left(\frac{Mp\Delta}{4dd'}\right)
 =(-1)^A e\!\left(\frac{pE^*}{4dd'}\right),
 \qquad
 (M-2Ad)(M+2Ad')-M^2=2AE^*.
\tag{125.8}
$$

The nonoscillatory window is
\(0<|E^*|\lesssim D^2/L\), and the fixed-\(p\) square contains no
\(\chi _4(p)\): it has squared to one.  However, (125.8) is not yet a
complete inverse theorem.  At fixed \((n,d,d')\), the permitted
\(p\)-interval has length \(\asymp D^2H/X\asymp1/H\), not \(L\), so
there is no \(p\)-sum on which to perform summation by parts.  Summing
\(n\) first creates a moving integer overlap with unresolved floor jumps.
This is the first invalid seam in the proposed exact/far/near
second-stage reduction.

Accordingly, this report proves a one-sided joint theorem and the complete
positive-row capacity bound (125.5), and it validates (125.6) only as a
strict-interior principal packet and method obstruction.  It does not
prove the missing upper bound for \(\mathcal E_\chi\), a target bound for
either sector separately, or a cancellation theorem between them.

## 2. Exact statement and hypotheses

Let \(X\ge2\) be real, let \(M\in\mathbb Z\) satisfy \(M\asymp X\), and
freeze every physical amplitude at the original real \(X\).  Write

$$
 D=X^\delta,
 \qquad L=X^\ell,
 \qquad K=\frac{XL}{D^2},
 \qquad H=\left\lceil\frac{X^{1/2}}D\right\rceil,
\tag{125.9}
$$

where

$$
 \frac14\le\delta<\frac12,
 \qquad 0\le\ell<\delta-\frac14,
 \qquad 178\ell+1638\delta>463.
\tag{125.10}
$$

Thus

$$
 K\asymp LH^2,
 \qquad
 Q:=\frac{DH}{K}\asymp\frac{D^2}{L\sqrt X}\longrightarrow\infty,
 \qquad
 \frac QL\longrightarrow\infty.
\tag{125.11}
$$

Fix one literal flat-smooth strict-UNBAL owner.  For positive odd \(p\),
put, with literal smooth zero extension in \(k\),

$$
 \begin{aligned}
 \mathcal A_{p,k}
 &:=W\!\left(\frac{X}{2D}\sqrt{\frac p{Mk}}\right)
 q_L((X/M)p),\\
 b_{p,k}
 &:=e(-1/8)M^{1/4}k^{-3/4}p^{-3/4}
 \mathcal A_{p,k}e(\sqrt{Mpk}).
 \end{aligned}
\tag{125.12}
$$

All profiles, entries, exits, and inactive values are those of the literal
owner.  In particular \(p\asymp L\), \(k\asymp K\) on active interiors,
and the normalized smooth symbol has the usual bounded-variation and
derivative bounds.  Let

$$
 C_H=\frac{J+H-1}{H^2},
 \qquad C_HH^2=J+H-1\asymp K,
 \qquad C_H\asymp L.
\tag{125.13}
$$

Define

$$
 \begin{aligned}
 \mathcal D_0
 &:=C_HH\sum_{p,k}|b_{p,k}|^2,\\
 \mathcal S_{\rm eq}^{\ne0}
 &:=C_H\sum_p\sum_{0<|h|<H}(H-|h|)
       \sum_k b_{p,k+h}\overline{b_{p,k}},\\
 \mathcal S_{\rm neq}
 &:=C_H\sum_{p\ne q}\chi _4(p)\chi _4(q)
       \sum_{|h|<H}(H-|h|)
       \sum_k b_{p,k+h}\overline{b_{q,k}}.
 \end{aligned}
\tag{125.14}
$$

The sums contain positive and negative shifts, both ordered conjugates,
moving \(p/k\) and \(q/k\) profiles, and zero-extended block entries and
exits.  The accepted diagonal estimate is

$$
 \mathcal D_0\ll X^{1/2}.
\tag{125.15}
$$

Under these hypotheses, the exact claims proved here are (125.2)--(125.5)
and the saddle calculation (125.6)--(125.8) on a fixed smooth block
interior.  The fixed-interior qualification applies only to the B-process
asymptotic, not to the Gram identities or to (125.5), which are
endpoint-complete.

The open upper target is equivalently

$$
 \boxed{\mathcal E_\chi\ll_\varepsilon X^{1/2+\varepsilon}.}
\tag{125.16}
$$

Indeed (125.3) and (125.15) show that (125.16) is equivalent at target
scale to the complete scalar bound for \(\mathcal S_{\rm off}\).  This
formulation keeps the possible cancellation between the two named sectors
inside one actual-character norm.

## 3. Proof or derivation

### 3.1 Exact Fejer block algebra and sector cancellation

For any zero-extended rows \(u_p(k)\), direct expansion gives

$$
 \sum_n\left(\sum_{0\le a<H}u_p(n+a)\right)
 \overline{\left(\sum_{0\le b<H}u_q(n+b)\right)}
 =\sum_{|h|<H}(H-|h|)\sum_k
 u_p(k+h)\overline{u_q(k)}.
\tag{125.17}
$$

There is no boundary remainder: every entry and exit is represented by
zero extension.  Taking \(u_p=b_p\), first with \(p=q\), and then after
summing \(\chi _4(p)u_p\), proves (125.2).  The \(p=q,h=0\) term is
\(\mathcal D_0\), since \(\chi _4(p)^2=1\).  Subtraction proves (125.3).

The transformation

$$
 (p,q,h,k)\longmapsto(q,p,-h,k+h)
\tag{125.18}
$$

conjugates each summand and preserves its Fejer multiplicity.  Hence all
quantities in (125.2)--(125.4) are real.  Positivity of
\(\mathcal E_\chi\) proves (125.4).  Notice also the exact lower bound
\(\mathcal S_{\rm neq}\ge-\mathcal E_{\rm eq}\).  Neither statement
calls the negative-shift conjugate a cancellation.

The algebra explains why a positive-row estimate is stronger than the
actual target.  If \(\mathcal E_{\rm eq}\) is large but
\(\mathcal E_\chi\) is target-sized, then

$$
 \mathcal S_{\rm neq}
 =-\mathcal E_{\rm eq}+O(X^{1/2+\varepsilon}),
\tag{125.19}
$$

so the unequal sector cancels the positive equal-row packet.  Conversely,
nothing in the Gram identity proves that this cancellation occurs for the
literal symbol.

### 3.2 A complete fixed-\(p\) curvature bound

On an active \(k\)-interval set

$$
 f_p(k)=\sqrt{Mpk}.
\tag{125.20}
$$

Uniformly for \(p\asymp L\), \(k\asymp K\),

$$
 f_p'(k)\asymp D,
 \qquad |f_p''(k)|\asymp\frac DK.
\tag{125.21}
$$

The nonoscillatory amplitude in (125.12) has size and total variation on
each block bounded by

$$
 \beta X^\varepsilon,
 \qquad
 \beta:=X^{1/4}K^{-3/4}L^{-3/4}.
\tag{125.22}
$$

Partial summation and the standard second-derivative estimate, combined
with the trivial estimate, therefore give for every literal block,
including support intersections,

$$
 \begin{aligned}
 |B_{p,n}|
 &\ll_\varepsilon \beta X^\varepsilon
 \min\left\{H,
 H\sqrt{D/K}+\sqrt{K/D}\right\}\\
 &\ll_\varepsilon \beta X^\varepsilon
 \min\left\{H,\sqrt{D/L}\right\}.
 \end{aligned}
\tag{125.23}
$$

Here the ratio of the first curvature term to the second is
\(HD/K=Q\to\infty\), and
\(H^2D/K\asymp D/L\).  There are \(O(L)\) active \(p\)'s and \(O(K)\)
active block positions.  Thus

$$
 \mathcal E_{\rm eq}
 \ll_\varepsilon C_HLK\beta^2X^\varepsilon
 \min\{H^2,D/L\}.
\tag{125.24}
$$

Using \(C_H\asymp L\), \(K\asymp LH^2\), and (125.22), the two entries
in (125.24) simplify respectively to

$$
 \frac XD=H\sqrt X,
 \qquad
 \frac{D^2}{L}=Q\sqrt X.
\tag{125.25}
$$

This proves (125.5).  It also proves

$$
 |\mathcal S_{\rm eq}^{\ne0}|
 \le \mathcal E_{\rm eq}+\mathcal D_0
 \ll_\varepsilon X^{1/2+\varepsilon}
       \{1+\min(H,Q)\},
\tag{125.26}
$$

but (125.26) is not the square target.  It loses exactly the best of the
original-block and reciprocal-packet deficits.

### 3.3 Audit of the reciprocal crossing packet

The derivative in (125.21) changes by one on the continuous scale

$$
 H_c:=\frac KD,
 \qquad \frac H{H_c}=\frac{DH}{K}=Q.
\tag{125.27}
$$

When \(H_c<1\), this is a continuous gradient-cell scale, not a partition
of the integer \(k\)-lattice into nonempty cells; that is precisely the
range in which the raw \(H\)-term triangle can beat the \(Q\)-packet
ledger.

On a fixed smooth interior of the hard block, apply Poisson in \(k\) with
phase \(f_p(x)-dx\).  Its unique saddle is

$$
 x_{p,d}=\frac{Mp}{4d^2},
 \qquad
 f_p(x_{p,d})-dx_{p,d}=\frac{Mp}{4d},
 \qquad
 f_p''(x_{p,d})=-\frac{2d^3}{Mp}.
\tag{125.28}
$$

The new negative Gaussian unit is \(e(-1/8)\).  Multiplying it by the
existing unit \(e(-1/8)\) in (125.12) gives \(e(-1/4)=-i\), while

$$
 M^{1/4}x_{p,d}^{-3/4}p^{-3/4}
 |f_p''(x_{p,d})|^{-1/2}=\frac2p.
\tag{125.29}
$$

This proves the exact saddle constant \(-2i/p\).  At the same saddle,

$$
 \mathcal A_{p,x_{p,d}}
 =W\!\left(\frac{Xd}{DM}\right)q_L((X/M)p).
\tag{125.30}
$$

The stationary labels are

$$
 I_{p,n}:={d\in\mathbb Z_{>0}:n<x_{p,d}<n+H\}.
\tag{125.31}
$$

On central blocks, the length of the derivative image is

$$
 f_p'(n)-f_p'(n+H)\asymp\frac{DH}{K}=Q,
\tag{125.32}
$$

so \(|I_{p,n}|\asymp Q\).  Equations (125.28)--(125.32) prove (125.6)
as a strict-interior principal expression.

The character-complete central packet is therefore

$$
 -2i\sum_{p>0\atop p\text{ odd}}
 \frac{\chi _4(p)}p q_L((X/M)p)
 \sum_{d\in I_{p,n}}W\!\left(\frac{Xd}{DM}\right)
 e\!\left(\frac{Mp}{4d}\right).
\tag{125.33}
$$

No moving profile has been rectangularized in (125.33).  There is also no
hidden \(L\)-fold \(p\)-sum at fixed \((d,n)\).  Indeed (125.31) is
equivalent to

$$
 \frac{4d^2n}{M}<p<\frac{4d^2(n+H)}M,
\tag{125.34}
$$

whose length is

$$
 \asymp\frac{D^2H}{X}\asymp\frac D{\sqrt X}\asymp\frac1H.
\tag{125.35}
$$

Thus it contains only \(O(1)\) integers, and eventually no long
progression.  An argument that fixes \((d,n)\) and invokes
\(\chi _4(p)\)-cancellation over length \(L\) fails at (125.35).

### 3.4 Capacity ledger and the full missing factor

One \((p,d)\) term in (125.33) has size \(\asymp L^{-1}\).  In the
reciprocal chart there are \(Q\) labels \(d\), \(L\) modes \(p\),
\(K\) block positions, and the outer energy factor is
\(C_H\asymp L\).  The exact capacity arithmetic is:

| Treatment in the reciprocal chart | Energy capacity | Excess over \(X^{1/2}\) |
|---|---:|---:|
| all \((p,d)\) coherent | \(LKQ^2=D^2\) | \(LQ\) |
| coherent \(d\), square-root only in \(p\) | \(KQ^2=D^2/L\) | \(Q\) |
| fixed-\(p\) positive rows, coherent \(d\) | \(KQ^2=D^2/L\) | \(Q\) |
| fixed-\(p\) positive rows, square-root in \(d\) | \(KQ=X^{1/2}\) | \(1\) |
| full row, square-root in \(d\) but coherent \(p\) | \(LKQ=LX^{1/2}\) | \(L\) |
| full row, square-root jointly in \((p,d)\), or in each variable | \(KQ=X^{1/2}\) | \(1\) |

These are capacities, not lower bounds and not grants of random
cancellation.  In particular, ordinary square-root credit from the
\(L^2\) mode pairs leaves \(QX^{1/2}\), so a factor \(Q\) is still
missing in this chart.  For the complete uniform parameter range it must
be compared with the original-block capacity \(HX^{1/2}\); the best
elementary positive-row capacity is (125.5).

The reciprocal phase

$$
 g_{M,p}(d)=\frac{Mp}{4d}
\tag{125.36}
$$

satisfies

$$
 |g_{M,p}''(d)|\asymp\frac{XL}{D^3}
 =\frac KD=\frac HQ.
\tag{125.37}
$$

Its derivative therefore crosses \(\asymp H\) integers over a
\(Q\)-packet.  The corresponding B-process returns the original
\(H\)-term block.  Second-derivative rank or inversion does not supply
the square-root \(d\)-packet inequality recorded in the fourth row of the
table.

### 3.5 Correct odd-lattice defect and the first failed seam

Squaring the fixed-\(p\) principal packet produces a \((d,d')\) phase

$$
 e\!\left(\frac{Mp}{4}
       \left(\frac1d-\frac1{d'}\right)\right)
 =e\!\left(\frac{Mp(d'-d)}{4dd'}\right).
\tag{125.38}
$$

The \(p\)-sum is over odd integers, whose step is two.  It is therefore
the doubled frequency, not the frequency itself, that must approach an
integer.  Let

$$
 \Delta=d'-d,
 \qquad
 A=\operatorname{nint}\!\left(\frac{M\Delta}{2dd'}\right),
 \qquad
 E^*=M\Delta-2Add'.
\tag{125.39}
$$

A fixed deterministic rule resolves a nearest-integer tie.  Since
\(p\) is odd,

$$
 \begin{aligned}
 e\!\left(\frac{Mp\Delta}{4dd'}\right)
 &=e(pA/2)e\!\left(\frac{pE^*}{4dd'}\right)\\
 &=(-1)^Ae\!\left(\frac{pE^*}{4dd'}\right).
 \end{aligned}
\tag{125.40}
$$

Direct multiplication gives the exact factorization

$$
 (M-2Ad)(M+2Ad')-M^2=2AE^*.
\tag{125.41}
$$

The formerly proposed integer-frequency variables
\(a\approx M\Delta/(4dd')\) and
\(E_d=M\Delta-4add'\) omit the half-integer aliases and are false as a
complete coherence classification.  They must be rejected.

If a genuinely smooth \(p\)-sum of length \(L\) were present, (125.40)
would make the nonoscillatory window

$$
 |E^*|\lesssim\frac{D^2}{L}.
\tag{125.42}
$$

The exact branch \(E^*=0\) has the divisor factorization (125.41), and
outside a power-enlargement of (125.42) repeated summation by parts would
be available for a smooth coefficient.  But the literal block energy
does not provide that smooth sum in the required order.

Before the \(n\)-sum, (125.35) leaves only \(O(1)\) possible values of
\(p\).  After summing \(n\), the coefficient of a \((d,d')\) pair
contains the exact moving overlap

$$
 \mu_{p,H}(d,d')
 :=\#\{n\in\mathbb Z:
        n<x_{p,d}<n+H,\ n<x_{p,d'}<n+H\}.
\tag{125.43}
$$

It equals a triangular continuous length only up to a floor-dependent
error:

$$
 \mu_{p,H}(d,d')
 =(H-|x_{p,d}-x_{p,d'}|)_++O(1).
\tag{125.44}
$$

The \(O(1)\) is a moving sawtooth, not an error that may be summed
absolutely over all \((p,d,d')\), and the exact multiplier has support
entries whenever either saddle crosses a hard block face.  No bounded
variation ledger for (125.43) at the square target has been proved.
Consequently the proposed separate-row decomposition into exact, far,
and nonzero-near \(E^*\) sectors stops first at (125.43), before any far
estimate.

Even after replacing (125.43) by an ideal smooth triangle, the remaining
nonzero window (125.42) is another reciprocal near-defect packet.  In
\(\mathcal E_{\rm eq}\), \(\chi _4(p)^2=1\), so it has no quarter
character in the \(p\)-sum.  The parity factor \((-1)^A\) must be
retained, but no inequality for its complete aggregate is known.  Thus
the idealized route also returns the missing signed problem instead of
supplying the factor \(Q\).

### 3.6 Unequal modes, character persistence, and adversarial controls

For \(p\ne q\), the literal phase retains the distinct product and
gradient defects

$$
 \mathcal N=(p-q)k+ph,
 \qquad
 \mathcal G=(p-q)k-qh
 =\mathcal N-(p+q)h.
\tag{125.45}
$$

Nothing in (125.1)--(125.44) identifies them or converts their progression
counts into a signed estimate.  The unequal sector remains exactly the
cross Gram in (125.3).  Its character persists; for odd \(p,q\),

$$
 \chi _4(p)\chi _4(q)=(-1)^{(p-q)/2},
\tag{125.46}
$$

but this is one sign per mode difference, not an independent sign on the
\(Q\) reciprocal crossings.

There is no coefficient-blind Gram inequality that supplies the missing
cancellation.  To see this, take a balanced set of odd modes and a
nonzero block vector \(v\) in the range of the length-\(H\) convolution.
If \(B_p=v\) for every \(p\), then
\(\sum_p\chi _4(p)B_p=0\) after exact residue balancing, so
\(\mathcal S_{\rm neq}=-\mathcal E_{\rm eq}\).  If instead
\(B_p=\chi _4(p)v\), then
\(\sum_p\chi _4(p)B_p=(\#p)v\), and the unequal sector reinforces the
equal sector by the maximal Gram factor.  These are adversarial
coefficient controls, not counterexamples to the literal symbol.  They
prove that support, norm, and character placement alone cannot decide the
sign or size of (125.3); an actual reciprocal-phase inequality is
indispensable.

## 4. First doubtful or unproved step

The first open analytic estimate is the upper half of the positive joint
energy bound

$$
 \boxed{
 C_H\sum_n\left|
   \sum_{p>0\atop p\text{ odd}}\chi _4(p)
   \sum_{0\le a<H}b_{p,n+a}
 \right|^2
 \ll_\varepsilon X^{1/2+\varepsilon}.}
\tag{125.47}
$$

This is exactly \(\mathcal E_\chi\), not
\(\mathcal E_{\rm eq}\), not an aliaswise norm, and not a model with
rectangular profiles.  It keeps
\(\mathcal S_{\rm eq}^{\ne0}\) and \(\mathcal S_{\rm neq}\) together.
The lower half is already proved by positivity and (125.15).

The Q-crossing B-process does not prove (125.47).  On its own chart,
square-root credit in \(p\) while treating the \(d\)-packet coherently
leaves \(QX^{1/2}\); the missing gain is exactly \(Q\).  A fixed-\(p\)
positive-row norm also leaves \(QX^{1/2}\) unless the full crossing packet
has square-root cancellation.  Uniformly, one should record the smaller
elementary deficit \(\min(H,Q)\) because the original triangle wins when
\(H_c<1\).

There are two earlier seams in any claimed completion of the candidate
packet method:

1. Formula (125.6) is a strict-interior stationary principal module.  A
   complete hard-block transform must retain both half-open endpoints,
   endpoint saddles, Fresnel transitions, the literal moving support
   entries and exits, and an aggregate error after the \(p,n\) energy.
2. The second-stage defect must use the half-integer odd lattice
   (125.39), not the rejected \(4a\) lattice.  More decisively, fixed
   \((n,d,d')\) leaves no long \(p\)-sum, while summing \(n\) first creates
   the unresolved multiplier (125.43).  Therefore neither the far branch
   nor a complete nonzero-near inverse localization has yet been proved.

Even if both ledger seams were repaired, the nonzero window (125.42)
would remain over target and character-free inside the separate positive
row.  This parks re-Poissonization, cellwise Cauchy, and a separate
positive-row norm as standalone mechanisms.  It does not park a genuinely
joint estimate of (125.47), because (125.19) shows that the unequal modes
may cancel the entire positive-row excess.

## 5. Control tests and outcomes

| Required control | Test and outcome |
|---|---|
| `literal_Round124_dual_offproduct_survivor` | **Pass.** Equations (125.12)--(125.16) reproduce the literal complete dual survivor, and (125.3) is its exact full-character block-energy form. |
| `H_K_Q_normalization` | **Pass with a capacity correction.** \(K\asymp LH^2\), \(H_c=K/D\), and \(H/H_c=Q=D^2/(L\sqrt X)\to\infty\). The best elementary deficit is \(\min(H,Q)\); a universal Q-only claim fails when \(H_c<1\). |
| `bpk_profile_and_character_placement` | **Pass.** Equation (125.12) retains the existing Gaussian unit, the moving \(W\)-profile, \(q_L((X/M)p)\), and places \(\chi _4(p)\) outside \(b_{p,k}\) but inside the full block before squaring. |
| `Fejer_block_square_identity` | **Pass exactly.** Equation (125.17) gives the triangle, both shift signs, and every block entry/exit with no remainder. |
| `equal_mode_offzero_vs_positive_energy` | **Pass.** \(\mathcal S_{\rm eq}^{\ne0}=\mathcal E_{\rm eq}-\mathcal D_0\); the positive norm is stronger and has only the over-target bound (125.5). |
| `equal_mode_integer_crossings_and_curvature` | **Pass for scale and complete upper bound; principal-packet only for the asymptotic.** A block crosses \(Q\) integer gradients, the saddle coefficient is \(-2i/p\), and coherent crossing energy is \(QX^{1/2}\). Hard-block stationary endpoints are not claimed complete. |
| `unequal_mode_product_gradient_defects` | **Pass as retained data; no gain.** Equation (125.45) keeps \(\mathcal N\ne\mathcal G\). The unequal sector is the exact cross Gram in (125.3), not a product-defect count. |
| `unequal_mode_character_persistence` | **Pass.** The full energy retains \(\chi _4(p)\chi _4(q)\); (125.46) shows it is a mode-difference sign and not a crossing-by-crossing random sign. |
| `sector_intercancellation` | **Pass exactly.** \(\mathcal S_{\rm neq}=\mathcal E_\chi-\mathcal E_{\rm eq}\). Equation (125.19) quantifies the possible cancellation, and no sectorwise modulus is taken. |
| `negative_shift_conjugacy` | **Pass.** The map (125.18) pairs negative shifts as conjugates and is used only to prove reality. |
| `mode_shift_multiplicity` | **Pass with a new obstruction.** \(|I_{p,n}|\asymp Q\), but at fixed \((d,n)\) the \(p\)-interval has length \(\asymp1/H\), so a presumed length-\(L\) character sum is absent. |
| `moving_profile_and_zero_extension` | **Pass for the exact Gram and the complete bound.** Zero extension makes (125.17) exact and bounded variation proves (125.23). The B-process formula retains (125.30), but its hard-face transition ledger remains open. |
| `stationary_endpoint_and_error_scope` | **Split.** The inequality (125.5) uses no stationary asymptotic and is endpoint-complete. Formula (125.6), the overlap multiplier (125.43), and the exact/far/near proposal are not endpoint-complete. |
| `signed_vs_unsigned_and_adversarial_coefficients` | **Pass.** Capacities are never called lower bounds. The two block-vector adversaries in Section 3.6 show that Gram algebra alone permits maximal cancellation or reinforcement and hence cannot prove the literal target. |
| `capacity_before_and_claimed_gain` | **Pass after repair.** The reciprocal chart loses Q after ordinary p-mode square-root credit; the positive row needs Q-crossing square-root cancellation. The raw chart supplies the smaller H loss when \(H<Q\). No unproved gain is claimed. |
| `owner_and_downstream_scope` | **Pass.** Every statement concerns one literal flat-smooth strict-UNBAL owner. Nothing is asserted for nonflat, sharp, clipped, starred, arithmetic, transition, hard TOP, BAL, complete UNBAL, M9-M2, either M1 route, endpoint uniformity, M9, any exponent, or the quarter theorem. |

All tests are analytic.  No numerical experiment, web source, or external
theorem was used.

## 6. Dependencies and exact artifacts used

This report used exactly the assigned selected context, plus the live
conductor candidate explicitly supplied for independent audit:

1. `protocol.md`, for graph authority, signed/unsigned separation, scope,
   and the report contract;
2. `state/proof_obligations.yml`, for the accepted Round-124 reduction,
   open flat-smooth parent, principal-return obstruction, character
   guardrail, and downstream nonimplications;
3. `state/active_campaign.yml`, for the frozen Round-125 formula,
   parameter range, controls, and completion gate;
4. `strategy/conductor_0821_full_proof_strategy.md`, for the
   noninvertibility requirement, capacity discipline, and Round-124 stop
   rule;
5. `rounds/codex-managed/m9-m2-unbalanced-joint-stationary-lattice-gate/synthesis.md`,
   for the accepted full-minus-safe dual reduction and exact remaining
   aggregate;
6. `rounds/codex-managed/m9-m2-unbalanced-joint-stationary-lattice-gate/reviews/conductor_round124_stationary_lattice_adjudication.md`,
   for the promoted seams, capacity scope, and joint endpoint exclusions;
7. `rounds/codex-managed/m9-m2-unbalanced-joint-stationary-lattice-gate/reports/double_poisson_product_defect_attack.md`,
   for the literal \(b_{p,k}\), scalar stationary constants, product and
   gradient defects, and prior principal-return calculation;
8. `rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/derivation_packet.md`,
   for the Round-125 sector split and proposed curvature directions;
9. `rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/briefs/actual_symbol_dual_sector_attack.md`,
   for this task's exact access, target, and report contract; and
10. `rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/candidates/conductor_curvature_cell_reciprocal_packet.md`,
    supplied by the conductor during the task, for independent checking of
    the saddle constant, crossing count, capacity table, and proposed
    second-stage defect.

The added arguments are exact Hilbert-space expansion, the elementary
second-derivative estimate with partial summation, one-dimensional
stationary phase on a fixed interior, and integer parity algebra.  No
Round-125 sibling report, shared proof draft, validation matrix, synthesis,
web source, or computation was read.

## 7. Recommended state effect

**Promote after independent seam review** the exact joint Gram identities
(125.2)--(125.3) and the genuinely noninvertible one-sided inequality
(125.4).  Record that every fixed-power violation of the complete
off-product scalar is positive and is equivalently a violation of the
single actual-character energy \(\mathcal E_\chi\).  This is an inverse
sign localization, not the missing upper estimate.

**Retain as a proved capacity bound**, subject only to checking the already
assumed literal symbol-variation constants, the complete fixed-\(p\)
estimate (125.5).  Record both charts: the raw loss is \(H\), the
reciprocal-packet loss is \(Q\), and the best uniform elementary loss is
\(\min(H,Q)\).  Do not state a universal Q-only deficit when
\(3\delta>1+\ell\).

**Promote only as a strict-interior method diagnostic** the saddle
calculation (125.28)--(125.33), including the exact coefficient
\(-2i/p\), literal returned profile, \(Q\)-crossing multiplicity, and the
capacity table in Section 3.4.  It proves that cellwise triangle/Cauchy or
a second B-process does not supply the missing crossing cancellation.  It
is not an endpoint-complete transform or an estimate.

**Reject and replace** the proposed \(4a\) integer defect lattice.  The
correct odd-\(p\) coherence variables are \(A,E^*\) in
(125.39)--(125.41), with the indispensable sign \((-1)^A\).

**Do not promote** a complete exact/far/nonzero-near positive-row inverse
theorem.  Its first invalid seam is the order-of-summation obstruction
(125.35), followed by the moving floor multiplier (125.43) and the
unpriced hard-block transition ledger.  Even its ideal smooth main leaves
the character-free nonzero near window (125.42).  This rigorously parks a
separate positive-row norm, cellwise Cauchy, and re-Poissonization as
standalone continuations; it does not rule out the joint cancellation in
(125.3).

**Retain open** the upper bound (125.47) and hence the flat-smooth
strict-UNBAL target.  If no other Round-125 report supplies a genuine
signed contraction, park this UNBAL lane at the exact full-character block
energy

$$
 \boxed{
 \mathcal E_\chi
 =C_H\sum_n\left|\sum_p\chi _4(p)
     \sum_{0\le a<H}b_{p,n+a}\right|^2,}
\tag{125.48}
$$

equivalently \(\mathcal S_{\rm off}=\mathcal E_\chi-\mathcal D_0\).
This is the narrowest endpoint-complete functional found here that retains
all possible cancellation between the equal-mode shifted and unequal-mode
sectors before an outside sectorwise norm.

**No change** is licensed for any nonflat UNBAL owner, hard TOP, BAL,
complete UNBAL, M9-M2, either M1 route, endpoint uniformity, M9, the
internal one-third exponent, the audited external exponent, or the
Gauss-circle quarter target.
