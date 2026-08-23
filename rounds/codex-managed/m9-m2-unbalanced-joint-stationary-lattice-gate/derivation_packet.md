# Conductor derivation packet: candidate joint stationary lattice

Campaign: `m9-m2-unbalanced-joint-stationary-lattice-gate`

Starting graph SHA-256:
`2b60eca238542d4f321a19c90f20163c6dd4cd7c60da6f324910b6db10b638c6`

Status: candidate calculations only. None of the stationary expansion,
error ledger, dual-sector bounds, or conclusions below is accepted until
independently derived and hostilely reviewed.

## 1. Literal input and target

Use the exact Round-123 correlation

$$
 \mathcal F_{M,H}=
 \frac{J+H-1}{H^2}
 \sum_{|h|<H}(H-|h|)
 \sum_k\sum_{r,s\ \mathrm{odd}}
 \chi_4(r)\chi_4(s)W_r\overline{W_s}
 \frac{q_{r,k+h}\overline{q_{s,k}}}{(k+h)k}
 e\!\left(\frac{M(k+h)}r-\frac{Mk}s\right).
\tag{124.D1}
$$

Here \(H=H_0=\lceil X^{1/2}/D\rceil\), \(J\asymp K\), and

$$
 R=X/D,qquad K=XL/D^2\asymp L H_0^2.
\tag{124.D2}
$$

The open target is the complete signed part of (124.D1) with
\(j\ne0\), \(E\ne0\), and \(|E|\leq X^{1+\rho}/L\), bounded by
\(X^{1/2+\varepsilon}\). The already proved zero alias, nonzero exact
aliases, and far tail must remain separate real packages.

## 2. Candidate double-character stationary map

Fix the Fourier convention

$$
 \chi_4(n)=\frac{e(n/4)-e(-n/4)}{2i},
$$

so that

$$
 \sum_n\chi_4(n)F(n)
 =\frac1{2i}\sum_{\sigma=\pm1}\sigma
 \sum_{m\in\mathbb Z}\int F(x)e(-(m-\sigma/4)x)\,dx.
\tag{124.D3}
$$

On the \(r\)-leg put \(\mu=m-\sigma/4<0\) and

$$
 p=-4\mu=-4m+\sigma>0.
$$

Then \(p\) is odd, \(\chi_4(p)=\sigma\), and the candidate interior
saddle and phase are

$$
 r_*=2\sqrt{\frac{M(k+h)}p},qquad
 \frac{M(k+h)}{r_*}+\frac{pr_*}{4}
 =\sqrt{Mp(k+h)}.
\tag{124.D4}
$$

The second derivative is positive,

$$
 \phi_r''(r_*)=\frac{p^{3/2}}{4\sqrt{M(k+h)}},
$$

so the candidate Gaussian unit is \(e(1/8)\) and the scalar stationary
amplitude is \(2(M(k+h))^{1/4}p^{-3/4}\).

On the \(s\)-leg put \(\nu=n-\tau/4>0\) and

$$
 q=4\nu=4n-\tau>0.
$$

Then \(q\) is odd, \(\chi_4(q)=-\tau\), and

$$
 s_*=2\sqrt{\frac{Mk}q},qquad
 -\frac{Mk}{s_*}-\frac{qs_*}{4}
 =-\sqrt{Mqk}.
\tag{124.D5}
$$

The Gaussian unit is \(e(-1/8)\). The two units cancel, while the two
Poisson coefficients give

$$
 -\frac{\sigma\tau}{4}
 =\frac{\chi_4(p)\chi_4(q)}4.
\tag{124.D6}
$$

Thus the candidate strict-interior dual phase is

$$
 \Theta_{p,q,h}(k)
 =\sqrt M\{\sqrt{p(k+h)}-\sqrt{qk}\},
\tag{124.D7}
$$

and the product of stationary amplitudes with the literal denominators is

$$
 \frac{4M^{1/2}}
 {(k+h)^{3/4}k^{3/4}p^{3/4}q^{3/4}},
\tag{124.D8}
$$

before evaluating the two literal profiles at (124.D4)--(124.D5) and
restoring the exact prefactor and Fejer multiplicity. At the saddles,

$$
 q_L(4X(k+h)/r_*^2)=q_L((X/M)p),qquad
 q_L(4Xk/s_*^2)=q_L((X/M)q),
\tag{124.D9}
$$

so the active dual modes should satisfy \(p,q\asymp L\). Every support
entry, exit, endpoint saddle, and nonstationary mode still requires an
aggregate proof.

## 3. Candidate exact lattice identities

Define the dual product defect

$$
 \mathcal N=p(k+h)-qk=ph-(q-p)k.
\tag{124.D10}
$$

Then exactly

$$
 \Theta_{p,q,h}(k)
 =\sqrt M\,
 \frac{\mathcal N}
 {\sqrt{p(k+h)}+\sqrt{qk}}.
\tag{124.D11}
$$

The key gradient identity is also exact at the candidate saddle:

$$
 \partial_k\Theta
 =\frac{\sqrt M}{2}
 \left(\frac{\sqrt p}{\sqrt{k+h}}-
       \frac{\sqrt q}{\sqrt k}\right)
 =M\left(\frac1{r_*}-\frac1{s_*}\right).
\tag{124.D12}
$$

Thus an integer \(k\)-Poisson or stationary label is expected to be the
original reciprocal alias \(j\), not a new independent oscillation. Also

$$
 \mathcal G:=pk-q(k+h)=\mathcal N-(p+q)h,
$$

and rationalization gives

$$
 \partial_k\Theta
 =\frac{\sqrt M\,\mathcal G}
 {2\sqrt{k(k+h)}\{\sqrt{pk}+\sqrt{q(k+h)}\}}.
$$

Thus \(\mathcal N\) is not the gradient numerator. Also

$$
 \partial_h\Theta=M/r_*,\qquad
 \partial_p\Theta=r_*/4,qquad
 \partial_q\Theta=-s_*/4.
\tag{124.D13}
$$

These identities are evidence of a possible full stationary involution;
they are not themselves a no-go theorem.

At a simultaneous \((k,h)\) saddle with dual integers \(j,d\), one has
\(r_*=M/d\), \(s_*=M/(d-j)\), and hence

$$
 M(s_*-r_*)-jr_*s_*=0.
$$

Thus the principal saddle belongs to the exact-alias manifold.  The live
nonexact near-alias restriction couples the original \(r,s\) variables
and cannot be inserted as two independent row amplitudes before character
Poisson summation.

Because \(p,q\asymp L\), \(|h|<H_0\), and
\(K\asymp L H_0^2\), the candidate defect geometry predicts, for large
\(X\),

$$
 \mathcal N=0\quad\Longleftrightarrow\quad p=q, h=0,
\tag{124.D14}
$$

with

$$
 |\mathcal N|\asymp |p-q|K\quad(p\ne q),qquad
 |\mathcal N|\asymp L|h|\quad(p=q, h\ne0).
\tag{124.D15}
$$

This separates exact product equality. It does not control stationary
points modulo one: (124.D12) can still cross integers, and those integers
are precisely the live aliases from Round 123.

## 4. Candidate capacity and branch audit

On \(p,q\asymp L\), \(k\asymp K\), the principal coefficient after the
outer Fejer prefactor is nominally

$$
 A_0\asymp
 \frac{X^{1/2}}{H_0K^{1/2}L^{3/2}}
 =\frac{D^2}{X^{1/2}L^2}
\tag{124.D16}
$$

per \((p,q,k,h)\). Its unsigned total is \(XL/D\), far above the
\(X^{1/2}\) target. This is only a scale ledger.

The dual diagonal \(p=q,h=0\) has nominal mass

$$
 A_0\cdot L K\asymp X^{1/2},
\tag{124.D17}
$$

exactly at the square target. The equal-mode shifted sector has phase

$$
 \Theta_{p,p,h}(k)
 =\sqrt{Mp}\{\sqrt{k+h}-\sqrt k\},
\tag{124.D18}
$$

and alias gradient of scale \(D|h|/K\). Since

$$
 \frac{DH_0}{K}\asymp\frac{D^2}{X^{1/2}L}\to\infty,
\tag{124.D19}
$$

it contains the shifted stationary crossings found in Round 123. The
unequal-mode sector has derivative scale \(D|p-q|/L\) but also crosses
many integers. Any proof must sum those crossings jointly rather than use
a uniform first-derivative gap.

## 5. Required outcome

First validate or repair (124.D3)--(124.D19), including all transition
and aggregate errors. Then seek one of:

1. the complete target bound;
2. a target-safe complete dual diagonal, equal-mode shifted sector, or
   unequal-mode sector with a strict reduction of the Round-123 survivor;
3. a fixed-power inverse theorem that localizes a violation to a smaller
   signed stationary lattice;
4. an exact proof that the complete stationary operation is an involution
   and that every available norm is overstrong, with the smallest live
   signed object stated explicitly.

Do not call (124.D14) a solution: product equality and derivative
resonance are different. Do not call (124.D12) a no-go without proving
the full inverse map and error ledger. Do not take absolute values over
\(p,q,h,j\) before the proposed cancellation has been tested. No result
may be promoted beyond the literal flat-smooth strict-UNBAL owner without
all graph bridges.
