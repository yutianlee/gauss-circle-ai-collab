# Conductor candidate: curvature cells and the complete reciprocal crossing packet

Campaign: `m9-m2-unbalanced-dual-offproduct-sector-gate`

Starting graph SHA-256:
`27bd4173fbdb16e5689595a02d42d82ffa8bb514b4610ea745ce2da6e2b8b152`

Status: revised after independent and hostile review.  The strict-interior
stationary phase and amplitude in Section 2 survive.  The discrete-cell
interpretation and the second-stage alias lattice have been corrected
below.  Hard-block endpoints, aggregate errors, and every target estimate
remain unproved.

## 1. Natural cell scale

For fixed active \(p\), put

$$
 f_p(k)=\sqrt{Mpk},\qquad
 f_p'(k)=\frac{\sqrt{Mp}}{2\sqrt k}\asymp D,
 \qquad |f_p''(k)|\asymp\frac DK.
\tag{125.C1}
$$

The interval on which the derivative changes by one has length

$$
 H_c=K/D.
\tag{125.C2}
$$

The derivative image of the literal block has length

$$
 \frac H{H_c}=\frac{DH}{K}\asymp
 Q=\frac{D^2}{L\sqrt X}\to\infty
\tag{125.C3}
$$

and hence meets nominally \(Q\) consecutive integer-gradient labels.  If
\(H_c\geq1\), these may be viewed as \(Q\) lattice-resolved curvature
cells.  If \(H_c<1\), however, the original block has only \(H\) lattice
spacings even though its dual derivative interval has length \(Q>H\).
Thus the elementary coefficient-blind excess is at most
\(\min\{H,Q\}\) at energy level, not universally \(Q\).  Any target
argument still has to aggregate the actual signed family before a norm.

## 2. Interior B-process packet

For one hard block beginning at \(n\), write

$$
 B_{p,n}=\sum_{a=0}^{H-1}b_{p,n+a}.
\tag{125.C4}
$$

Poisson in \(k\), with Fourier phase \(f_p(x)-dx\), has stationary point

$$
 x_{p,d}=\frac{Mp}{4d^2},\qquad
 f_p(x_{p,d})-dx_{p,d}=\frac{Mp}{4d},\qquad
 f_p''(x_{p,d})=-\frac{2d^3}{Mp}.
\tag{125.C5}
$$

The stationary amplitude in (125.B1), including its existing
\(e(-1/8)\) unit and the new negative Gaussian unit, simplifies exactly to

$$
 -\frac{2i}{p}.
\tag{125.C6}
$$

Moreover the moving profile becomes

$$
 \mathcal A_{p,x_{p,d}}
 =W\!\left(\frac{Xd}{DM}\right)q_L((X/M)p).
\tag{125.C7}
$$

Thus on a fixed smooth block interior the candidate principal packet is

$$
 B_{p,n}^{\rm prin}
 =-\frac{2i}{p}q_L((X/M)p)
 \sum_{d\in I_{p,n}}
 W\!\left(\frac{Xd}{DM}\right)e\!\left(\frac{Mp}{4d}\right),
\tag{125.C8}
$$

where

$$
 I_{p,n}=\left\{d\in\mathbb Z_{>0}:
 n<x_{p,d}<n+H\right\},qquad |I_{p,n}|\asymp Q
\tag{125.C9}
$$

on a fixed central patch.  Endpoint saddles require the literal half-open
convention and Fresnel transition modules; (125.C8) is not yet a complete
hard-block transform.

After summing the character modes, the corresponding central block is

$$
 \sum_p\chi_4(p)B_{p,n}^{\rm prin}
 =-2i\sum_{p>0\atop p\text{ odd}}
 \frac{\chi_4(p)}p q_L((X/M)p)
 \sum_{d\in I_{p,n}}W\!\left(\frac{Xd}{DM}\right)
 e\!\left(\frac{Mp}{4d}\right).
\tag{125.C10}
$$

This is the formal complete \(Q\)-label reciprocal principal packet that
must remain signed.  A second B-process in \(d\) returns the original
\(H\)-term square-root block, so inversion itself proves no estimate.

## 3. Capacity before an inequality

On the central ranges, one \((p,d)\) term in (125.C10) has size
\(\asymp L^{-1}\).  There are \(Q\) values of \(d\), \(L\) values of
\(p\), \(K\) block positions, and outer factor \(C_H\asymp L\).
Consequently the reciprocal principal-symbol ledger is:

| Treatment | Energy capacity |
|---|---:|
| all \((p,d)\) coherent | \(LKQ^2=D^2\) |
| coherent \(d\), square-root only in \(p\) | \(KQ^2=D^2/L\) |
| fixed-\(p\) positive row, coherent \(d\) | \(KQ^2=D^2/L\) |
| fixed-\(p\) positive row, square-root in \(d\) | \(KQ=X^{1/2}\) |
| full actual row, square-root in both \(d\) and \(p\) | \(KQ=X^{1/2}\) |
| full actual row, square-root in \(d\) but coherent \(p\) | \(LKQ=LX^{1/2}\) |

The original \(H\)-term triangle gives \(X^{1/2}H\) for the positive
\(p\)-row energy, whereas the coherent reciprocal ledger gives
\(X^{1/2}Q=D^2/L\).  Hence the best of these two elementary charts is

$$
 X^{1/2}\min\{H,Q\}.
\tag{125.C11}
$$

In particular the missing coefficient-blind factor is
\(\min\{H,Q\}\), and a claim of a universal full \(Q\)-deficit is false
when \(Q>H\).  Neither chart reaches the target because both \(H\) and
\(Q\) tend to infinity.  The table remains a norm ledger, not a lower
bound for any signed packet.

The reciprocal phase

$$
 g_{M,p}(d)=Mp/(4d)
$$

has

$$
 g_{M,p}''(d)\asymp K/D=H/Q,
\tag{125.C12}
$$

so its derivative sweeps \(\asymp H\) integers across a \(Q\)-packet.
A second-derivative bound produces the same invertible capacity rather
than the required square-root \(Q\) estimate.

## 4. Corrected second-stage alias seam

If the stronger fixed-\(p\) positive row is expanded after (125.C8), a
\((d,d')\) pair has phase

$$
 e\!\left(\frac{Mp}{4}\left(\frac1d-\frac1{d'}\right)\right).
\tag{125.C13}
$$

Because \(p\) is restricted to odd integers, coherence in the \(p\)-sum
is modulo \(\tfrac12\mathbb Z\), not modulo \(\mathbb Z\).  Put
\(\Delta=d'-d\), let \(A\) be a nearest integer to
\(M\Delta/(2dd')\), and define

$$
 E_d^*=M\Delta-2Add'.
\tag{125.C14}
$$

Then

$$
 e\!\left(\frac{Mp\Delta}{4dd'}\right)
 =(-1)^A e\!\left(\frac{pE_d^*}{4dd'}\right),
\tag{125.C15}
$$

and the exact factor identity is

$$
 (M-2Ad)(M+2Ad')-M^2=2AE_d^*.
\tag{125.C16}
$$

If one had an independent smooth odd-\(p\) interval of length \(L\), its
nonoscillatory defect window would be nominally

$$
 0<|E_d^*|\lesssim D^2/L.
\tag{125.C17}
$$

The literal moving intervals do not supply that independent sum.  At fixed
\((n,d,d')\), the simultaneous conditions
\(d,d'\in I_{p,n}\) leave a \(p\)-interval of length

$$
 O(D^2H/X)=O(1/H),
\tag{125.C18}
$$

so there is no length-\(L\) \(p\)-sum on which to integrate by parts.
Summing \(n\) first instead creates the exact moving overlap

$$
 \mu(p;d,d')=#\{n:\ n<x_{p,d},x_{p,d'}<n+H\},
\tag{125.C19}
$$

with its floor jumps, support entries, and Fresnel endpoints.  No far
estimate for this multiplier has been proved.  The original
\(M\Delta-4add'\) lattice sees only even \(A\) and can misclassify an exact
half-integer coherent packet as far.  Thus the proposed second-stage
near-defect theorem is rejected; only (125.C14)--(125.C16) are exact
algebraic diagnostics for the strict-interior positive-row model.

## 5. First open seam

The first analytic gap is a complete actual-symbol estimate of

$$
 \sum_{d\in I_{p,n}}
 W\!\left(\frac{Xd}{DM}\right)e(Mp/(4d))
\tag{125.C20}
$$

at square-root scale on average in the exact correlated \((p,n)\) family,
or a joint estimate in (125.C10) that gains the needed factor without first
forming the stronger positive \(p\)-row energy.  Summing (125.C13)
separately in \((p,n)\), applying Cauchy across lattice-resolved cells, or
re-Poissonizing it all lose or return the operative factor
\(\min\{H,Q\}\).

Independent review must decide whether (125.C8) can be made endpoint
complete with target-safe aggregate error, whether its capacity arithmetic
is exact, and whether the equal-mode and unequal-mode sectors can be
separated without discarding an essential cancellation.  No target,
sector saving, lower bound, or downstream implication is claimed here.
