# Round224 conductor grouped-coefficient commutator control

## 1. Result

For the actual accepted angular profile, the correction can have positive
mass even after aggregation over all divisors and amplifier primes, before
taking the coefficient absolute value. The finite lower bound below is
an exact actual-coefficient control. Its asymptotic corollary uses only
the fixed-modulus prime number theorem in residue class 1 modulo 4.
Neither is a lower bound for the signed radial wave or its real part.
No complete estimate or graph promotion is claimed.

## 2. Exact statement and hypotheses

Put \(R=X^{1/4}\), \(Y=\sqrt X\), \(y=\lfloor Y\rfloor\),
\(D_j=2^{-j}y\), \(H_j=\lfloor D_j/R\rfloor\), and use exactly the
actual \(A_X,c_X,F_X\) in the frozen conductor interface. In particular
\(0\le A_X\le1\), the active profiles are nonnegative, have closed
support \(d/D_j\in[1/2,3/2]\), vanish above \(y\), and sum to one on
\(C_bR<d<y\). The inactive bottom is supported below \(C_bR\).
The fixed taper satisfies \(0\le\Phi\le1\), \(\Phi(0)=1\), and is
continuous at zero. These are the accepted profile facts, not an
alternative choice of coefficients.

Fix \(\delta=1/20\). Choose a fixed \(s>0\) so small that
\[
 2/\sqrt{s}>C_b,\qquad
 (3/4)\sqrt{s}<1/2,\qquad
 \Phi(u)\ge9/10\quad(0\le u\le(3/4)\sqrt{s}).
\tag{1}
\]
For a nonempty finite set \(\mathcal P\) of split primes, put
\(k=|\mathcal P|\), \(P=\max\mathcal P\). Let \(M\ge10\) and suppose
\[
 P(1+\delta)^2M^2\le sY.
\tag{2}
\]
All primes in \(\mathcal P\) are at least 5. Write
\[
 v(M)=\#\{a\text{ prime}:M\le a\le(1+\delta)M,\ a\equiv1\pmod4\}.
\]
For every distinct pair \(a,b\) counted here and every \(p\in\mathcal P\),
for all sufficiently large real \(X\) (with an absolute threshold),
\[
 E_p(ab):=c_X(pab)+c_X(ab/p)-2c_X(ab)\ge7/10.
\tag{3}
\]
The backward coefficient is zero unless \(p\mid ab\), as usual. Thus
\[
 \mathcal C_X(\mathcal P):=
 \frac1{2k}\sum_{n\le\lfloor16Y\rfloor}
 \left|\sum_{p\in\mathcal P}E_p(n)\right|n^{-3/4}
 \ge \frac7{40}(1+\delta)^{-3/2}v(M)(v(M)-1)M^{-3/2}.
\tag{4}
\]
This is a grouped-coefficient absolute certificate, not the incidence
certificate obtained by placing absolute values inside the divisor sum.

## 3. Proof and derivation

For \(n=ab\), the four divisor allocations have first coordinates
\(1,a,b,ab\). At \(h=a\) or \(b\), the ratio \(q/h\) is at most
\(1+\delta<4\), so \(d=2Y\sqrt{h/q}>Y\ge y\), and the profile vanishes.
The \(h=ab\) term also vanishes. Consequently
\[
 0\le c_X(ab)=A_X(1,ab)\le1.
\tag{5}
\]
All character factors in any divisor sum of \(pab\) or \(ab/p\) equal
one, since all prime factors are split. There is no cancellation within
these coefficients. In \(c_X(pab)\) retain the three distinct allocations
\[
 (h,q)=(1,pab),\quad(a,pb),\quad(b,pa).
\tag{6}
\]
They remain distinct if \(p=a\) or \(p=b\); we do not count any allocation
twice. Write \(m=pab\). For each of (6),
\[
 d=2Yh/\sqrt m\ge2Y/\sqrt{sY}
   =(2/\sqrt s)R>C_bR.
\tag{7}
\]
For the latter two allocations,
\[
 d\le2Y\sqrt{(1+\delta)/5}<0.917Y;
\]
the first is also below this bound when \(M\ge10\).
For large \(X\), therefore \(d<y\), with a uniform buffer. No hard-top
star is encountered. The active partition sums to one at this \(d\).
On the support of any profile appearing there,
\[
 \frac{hR}{D_j}
 \le\frac{3hR}{2d}
 =\frac{3\sqrt m}{4R}
 \le\frac34\sqrt s<\frac12.
\tag{8}
\]
Thus \(D_j/R>2h\), so the literal integer height satisfies \(h\le H_j\),
and \(h/(H_j+1)<hR/D_j\). Every taper in the partition is at least
\(9/10\). It follows that \(A_X(h,q)\ge9/10\) at all three allocations.
Equation (5) and the nonnegative backward coefficient give
\[
 E_p(ab)\ge3(9/10)-2=7/10,
\]
proving (3), including repeated-prime cases. The construction never
replaces \(A_X\) by \(A_{pX}\) or \(A_{X/p}\).

There are exactly \(v(M)(v(M)-1)/2\) different products of distinct
unordered pairs, by unique factorization. They all lie in the literal
radial cutoff since \(ab\le sY/P<16Y\). Their weights are at least
\((1+\delta)^{-3/2}M^{-3/2}\), and their prime-summed defects are at least
\(7k/10\). Dividing by \(2k\) proves (4).

For a quantitative corollary, the sole external input is
\[
 \pi(t;4,1)\sim t/(2\log t).
\tag{9}
\]
Subtracting at \(t=(1+\delta)M\) and \(t=M\), with fixed \(\delta\),
gives \(v(M)\sim\delta M/(2\log M)\). Therefore, as \(M\to\infty\),
\[
 \mathcal C_X(\mathcal P)\gg M^{1/2}/(\log M)^2.
\tag{10}
\]
For each fixed \(\eta>0\), if \(P\le X^{1/2-\eta}\), choose
\(M=\sqrt{sY/[P(1+\delta)^2]}\). Then
\[
 \mathcal C_X(\mathcal P)
 \gg_\eta X^{1/8}P^{-1/4}/(\log X)^2.
\tag{11}
\]
The finite statement (4) requires no prime-density theorem. The prime
count is for the auxiliary semiprime factors, not for the amplifier.
No uniformity in growing arithmetic moduli or short relative intervals
is used. The complete signed correction is still unestimated.

## 4. First doubtful or unproved step

No signed lower bound follows by reinserting \(e(\sqrt{Xn})\), nor by
taking the real part after \(e(1/8)\). Coefficients outside the displayed
semiprime set can cancel, and the displayed set itself has varying
radial phases. The missing step in the amplification attempt is a
complete bound on the joint main-minus-correction expression with those
phases retained. Equation (11) only tests this particular coefficient
absolute-value procedure in its stated range. It is no universal
impossibility theorem and does not address every possible prime range.

## 5. Required controls and outcomes

- Actual profile, fixed centre, floors: GREEN by (7)--(8), with
  \(D_0=y\) and \(D_1=y/2\) literally.
- Hard stars and inactive bottom: GREEN; a uniform interior buffer
  excludes both from the witness set.
- Repeated primes and overlap: GREEN; the three allocations are
  distinct even when \(p=a\) or \(b\); the backward coefficient is
  retained and nonnegative.
- Divisor and prime aggregation: GREEN; (3) holds with one sign on the
  same products for every amplifier prime.
- Prime 2: not an amplifier prime or a semiprime factor; no odd-prime
  eigenrelation is asserted at 2.
- Fixed-modulus source use: (9) requires only coprime \(1,4\), fixed
  \(\delta>0\), and \(M\to\infty\). Source review remains required.
- Physical restoration: a certificate price is multiplied by \(X^{1/4}\);
  this never gives a lower bound for physical M1. The inherited complete
  signed bound is \(G_X\ll X^{1/12+\epsilon}\). This report improves
  neither that bound nor the pointwise exponent.

Zero mathematical experiments; all controls above are analytical.

## 6. Dependencies and exact artifacts used

Campaign m9-m1-complete-gar-prime-amplification, round224, conductor,
2026-09-28. Starting graph SHA256:
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.

Profile and owner inputs: protocol.md; state/proof_obligations.yml;
state/active_campaign.yml; strategy/round224_complete_gar_split_prime_amplification.md;
briefs/conductor_actual_gar_interface.md in this campaign;
rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/candidates/conductor_profile_flattening_and_integer_phase.md;
the accepted GAR and direct-menu nodes; and the reviewed closed223
checkpoint. The conductor has access to all task progress and read the
frozen blind allocation report, but the semiprime calculation is derived
here independently of that report. Exact final hashes accompany closure.

One narrow primary-source statement audit: Terence Tao, "The prime
number theorem in arithmetic progressions, and dueling conspiracies",
24 September 2009, introductory displayed fixed-\(a,q\) theorem, accessed
28 September 2026:
https://terrytao.wordpress.com/2009/09/24/the-prime-number-theorem-in-arithmetic-progressions-and-dueling-conspiracies/
The authored exposition states (9) as a known theorem. Its later
heuristic discussion is not used as a proof. This is the only external
theorem used in this control.

## 7. Recommended state effect

Retain as an actual-coefficient diagnostic, subject to independent
mathematical and source review. No graph change, no complete owner
closure, no theorem or exponent gain, and no successor authorized here.
