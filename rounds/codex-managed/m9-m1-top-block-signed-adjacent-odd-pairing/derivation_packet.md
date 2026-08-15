# Round 57 derivation packet: signed adjacent-odd pairing on the high shell

This packet freezes the first signed interaction left by Round 56. It
asserts no cancellation theorem.

## 1. Exact high-shell object

Let \(Y=R^2\asymp\sqrt X\), and let \(J=[A,B]\cap\mathbb Z\subset
[cY,CY]\) have \(|J|\le R\). On

\[
 {R\over4}<h\le {R\over2},
\tag{57.1}
\]

retain

\[
 P_J=\sum_h\sum_{\substack{q\ {m odd}\\hq\in J}}^{*}
 \chi_4(q)\mathcal A_X(h,q)e(\sqrt{Xhq}),
\tag{57.2}
\]

where

\[
 \mathcal A_X(h,q)=\Omega_X^*(hq,h)
\]

is the exact unweighted actual angular amplitude with all height floors,
profiles, hard top, angular stars, and inherited radial star retained.
The target is

\[
 |P_J|\ll_\varepsilon X^\varepsilon\sqrt R.
\tag{57.3}
\]

Restoring \((hq)^{-3/4}\asymp R^{-3/2}\) turns (57.3) into the required
normalized \(R^{-1}=Y^{-1/2}\) window bound.

## 2. Adjacent-odd identity

For odd \(q\),

\[
 \chi_4(q+2)=-\chi_4(q).
\tag{57.4}
\]

Whenever both \(hq\) and \(h(q+2)\) lie in \(J\), their signed row is

\[
 \chi_4(q)e(\sqrt{Xhq})
 \left\{\mathcal A_X(h,q)
 -\mathcal A_X(h,q+2)e(\Theta_h(q))\right\},
\tag{57.5}
\]

where

\[
 \Theta_h(q)=\sqrt{Xh(q+2)}-\sqrt{Xhq}
 ={2\sqrt{Xh}\over\sqrt{q+2}+\sqrt q}.
\tag{57.6}
\]

The pair spacing in product is \(2h\). In (57.1), it lies in
\((R/2,R]\), so a length-\(R\) window may contain two adjacent odd
products but never three. Pairing exists only for favourable alignment;
otherwise a row is unmatched. Derive the exact matched/unmatched
decomposition rather than assuming all rows pair.

## 3. Candidate cancellation and capacity

For a matched row, separate

\[
 \mathcal A(h,q)-\mathcal A(h,q+2)e(\Theta)
 =\{\mathcal A(h,q)-\mathcal A(h,q+2)\}
 +\mathcal A(h,q+2)\{1-e(\Theta)\}.
\tag{57.7}
\]

The fixed-\(h\) sampled-BV theorem controls the total amplitude
difference along its physical interval, but on this high shell there is
at most one matched pair, so a local Lipschitz gain must be derived from
the actual profile formula if needed. Likewise, \(1-e(\Theta)\) is small
only when \(\Theta\) is close to an integer; character sign reversal does
not make it small automatically.

Count all unmatched endpoints with their actual full/starred values. The
required aggregate over \(h\) is \(O(\sqrt R)\), while a termwise absolute
count permits \(R\). Any successful argument must keep the resulting
\(h\)-sum signed or prove that only \(O(\sqrt R)\) rows are unmatched.

## 4. Mandatory controls

- Treat \(X=K^4\), \(R=K\), windows near \(K^2\), and every alignment
  for which \(\Theta_h(q)\) is integral, half-integral, or bounded away
  from integers.
- The top-profile plateau can make the amplitude difference in (57.7)
  exactly zero, leaving only the phase increment. Conversely, profile or
  height edges can make the amplitude difference order one; retain them.
- Artificial window endpoints have full cutoff ownership. Use half
  weights only for inherited equality/radial stars.
- Round 57 owns only (57.1). The lower sector
  \((\log X)^B<h\le R/4\) remains open even if (57.3) is proved.
- This is physical. No alpha transfer or downstream theorem is automatic.

No numerical experiment is needed. The round is 100% analytical.
