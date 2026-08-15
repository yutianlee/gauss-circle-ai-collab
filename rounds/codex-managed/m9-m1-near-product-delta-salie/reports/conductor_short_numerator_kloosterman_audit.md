# 1. Result

The exact \(s\)-wavelet forces any Farey/delta decomposition into a
short-numerator Kloosterman regime. This supplies a rigorous scoped
no-go for the most direct completion-plus-Weil route.

More precisely, if \(K=\widehat g\) with \(g\) fixed, smooth, compactly
supported, and separated from zero, then the circle variable is supported
at distance \(\asymp T^{-1}\) from an integer. In a Farey dissection of
natural level \(C\leq J\), a contributing reduced fraction \(a/c\) has

\[
 c\gtrsim T,\qquad
 \min(a,c-a)\ll {c\over T}.
\]

At the benchmark \(T=X^{3/10}>J^{1/2}=X^{1/4}\), this numerator interval
has length \(c/T<\sqrt c\) for every \(c\leq J\). After two residue-class
sums the inverse phase is indeed Kloosterman, but completing its
\(a\)-sum and applying a square-root Weil bound is weaker than the
trivial bound for the actual short numerator. Any successful delta or
Kuznetsov argument must therefore gain jointly over moduli and dual
variables; termwise Kloosterman completion cannot supply the missing
\(X^{1/20}\).

# 2. Exact statement and hypotheses

Let \(N=\lfloor X\rfloor\), \(\vartheta=X-N\), and assume

\[
 K(x)=\int_{\mathbb R}g(t)e(-tx)\,dt,
 \qquad
 \operatorname{supp}g\subset[-B,-b]\cup[b,B]
\]

for fixed \(0<b<B\). This is the fixed wavelet class in the Round-70
packet; finite fixed sums and rapidly decaying Fourier tails are treated
identically. Define

\[
 \mathscr P_T(\alpha)=
 \sum_{s\in\mathbb Z}K\!\left({s-\vartheta\over T}\right)e(-\alpha s).
\]

The localization statement below is exact. The complete-sum identity is
stated for an odd modulus \(c\), \((a,c)=1\), and the convention

\[
 \mathfrak C_{c,a}(h,k)=
 \sum_{x\bmod c}\sum_{y\bmod 4c}
 \chi_4(y)e_c(x(ay+h))e_{4c}(ky).
\]

It reads

\[
 \mathfrak C_{c,a}(h,k)=
 \begin{cases}
 2ic\,\chi_4(kc)
 e_c(\lambda_c kh\overline a),&k\ \mathrm{odd},\\
 0,&k\ \mathrm{even},
 \end{cases}
 \qquad \lambda_c={c^2-1\over4}.
 \tag{2.1}
\]

This report makes no claim that odd moduli alone form a complete delta
symbol. Equation (2.1) is the exact odd-modulus local factor that every
such construction must contain.

# 3. Proof or derivation

Poisson summation in \(s\) gives

\[
 \mathscr P_T(\alpha)=
 T\sum_{\ell\in\mathbb Z}
 e(-\vartheta(\ell+\alpha))
 \widehat K(T(\ell+\alpha)).
 \tag{3.1}
\]

Since \(\widehat K(t)=g(-t)\) under the stated convention, (3.1) vanishes
unless

\[
 {b\over T}\leq\|\alpha\|\leq {B\over T}.
 \tag{3.2}
\]

Insert the exact circle identity

\[
 \mathbf1_{mn=N+s}=\int_0^1e(\alpha(mn-N-s))\,d\alpha.
\]

Thus summing the \(s\)-wavelet before absolute values restricts the
entire circle integral to (3.2). Suppose this arc is dissected at Farey
level \(C\) into neighborhoods of reduced \(a/c\), \(c\leq C\), of
radius \(O((cC)^{-1})\). If such a neighborhood meets (3.2), then

\[
 \min(a,c-a)\ll {c\over T}+{1\over C}.
 \tag{3.3}
\]

Except for the separate \(0/1\) arc, a contributing numerator therefore
forces \(c\gg T\) and occupies only \(O(1+c/T)\) residue classes.

For (2.1), summing \(x\) first imposes

\[
 ay+h\equiv0\pmod c.
\]

Let \(y_0\equiv-\overline a h\pmod c\). The four lifts modulo \(4c\)
give

\[
 \mathfrak C_{c,a}(h,k)
 =c e_{4c}(ky_0)
 \sum_{t\bmod4}\chi_4(y_0+ct)e_4(kt).
\]

For even \(k\) the last sum is zero. For odd \(k\), changing variables
modulo \(4\) and using

\[
 \sum_{z\bmod4}\chi_4(z)e_4(kcz)=2i\chi_4(kc)
\]

gives

\[
 \mathfrak C_{c,a}(h,k)
 =2ic\chi_4(kc)
 e_c(\lambda_c kh\overline a),
\]

because \((c^2-1)/4=\lambda_c\in\mathbb Z\). This proves (2.1).

The delta phase also contains \(e_c(-a(N+s))\). Consequently, after the
\((x,y)\) residue sums, the \(a\)-variable has the inverse phase

\[
 e_c(-aN+\lambda_c kh\overline a)
\]

but is weighted by

\[
 \sum_sK\!\left({s-\vartheta\over T}\right)e_c(-as).
\]

Formula (3.1) makes this weight negligible unless
\(\min(a,c-a)\ll c/T\). Thus the apparent complete Kloosterman sum is in
fact a short-numerator Kloosterman segment.

For every natural modulus \(c\leq J\), the benchmark inequality

\[
 T>\sqrt J\geq\sqrt c
\]

implies

\[
 {c\over T}<\sqrt c.
 \tag{3.4}
\]

The trivial number of actual \(a\)-terms in (3.3) is therefore smaller
than the square-root size of a completed Kloosterman sum. Completion plus
a termwise Weil bound cannot be the missing saving.

# 4. First doubtful or unproved step

The argument does not exclude cancellation jointly across \((c,h,k)\), nor
does it audit a spectral theorem for the resulting family. The first
genuinely open transformed assertion is a large-sieve or Kuznetsov bound
for short-numerator Kloosterman segments with

\[
 T\lesssim c\lesssim J,qquad
 a\asymp c/T,qquad
 \lambda_c={c^2-1\over4},
\]

coupled to the actual one-sided ratio symbol and dual Poisson weights.
No such estimate is proved here. Choosing moduli \(c>J\) also lies
outside the scoped no-go; in that range both original variables are
shorter than the modulus and the full dual-length cost must be audited.

# 5. Required controls and outcomes

- **Real centre:** passed; \(\vartheta=X-\lfloor X\rfloor\) remains in
  (3.1).
- **Signed wavelet first:** passed; the \(s\)-sum is transformed before
  absolute values.
- **Zero mode:** passed; support of \(g\) away from zero removes the
  literal circle zero mode.
- **Modulus/numerator geometry:** passed in the natural range \(c\leq J\);
  contributing nonzero fractions have \(c\gtrsim T\) and \(a\ll c/T\).
- **Character complete sum:** passed for odd \(c\); \(\chi_4\) becomes
  the exact factor \(\chi_4(kc)\), and even \(k\) vanishes.
- **Inverse phase:** passed; it is
  \(e_c(-aN+\lambda_c kh\overline a)\).
- **Weil capacity:** fails as a closure; \(c/T<\sqrt c\), so termwise
  completion loses rather than saves.
- **Diagnostic check:** (2.1) was checked exhaustively for
  \(c=3,5,7,9,11\), all reduced \(a\), all \(h\bmod c\), and all odd
  \(k\bmod4c\). This finite computation is diagnostic only; the displayed
  algebra is the proof.
- **Downstream scope:** no bound for (70.1), full cone, M9--M1, M9, or an
  exponent is claimed.

# 6. Dependencies and exact artifacts used

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-near-product-delta-salie/derivation_packet.md`;
- the Round-69 synthesis and conductor adjudication.

No external theorem is imported. The circle identity, Poisson formula,
four-lift character sum, and power comparison were derived locally. The
bounded residue computation used Python only as a diagnostic control.

# 7. Recommended state effect

Promote the exact circle localization (3.1)--(3.3) and the odd-modulus
complete-sum identity (2.1) as a scoped reduction/no-go. Reject the claim
that completing each resulting \(a\)-sum and applying a termwise Weil
bound closes (70.1). Retain the signed product-wavelet estimate open; its
new transformed survivor is a joint-modulus estimate for incomplete
Kloosterman segments, not an individual complete-sum bound.
