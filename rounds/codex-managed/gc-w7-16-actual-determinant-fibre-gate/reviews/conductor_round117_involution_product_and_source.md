# Conductor review: half-shift involution, product return, and source scope

Campaign: `gc-w7-16-actual-determinant-fibre-gate`

Decision: promote a scoped transform-and-norm obstruction, retain the
cellwise product representation as a qualified diagnostic, and import no
external determinant theorem.

## 1. Exact increment and half-shift chart

All three reports agree independently on

\[
 a'=a+p,\qquad b'=b+q,\qquad n=aq-bp,
\]

\[
 {cn\over\kappa_i b(b+q)}
 ={c\over\kappa_i}\left({a\over b}-{a+p\over b+q}\right).
\]

For M1, \(b,b'\) are odd, \(q=2r\), and the character product is
\((-1)^r\). For M2, \(a,a'\) are odd, \(p=2s\), and on a signed sector
the character product is \((-1)^s\) with the fixed sign of \(aa'\)
retained in the denominator. The clipped strip widths are

\[
 \#q\ll1+\min\left(B,{BD\over WL}\right),\qquad
 \#p\ll1+\min\left(A,{B\over W}\right),
 \quad A={LB\over D}.
\tag{117.I1}
\]

The blind report additionally proves that a fixed determinant gives a
progression of step \(2(a,b)\), hence only \(O(1)\) comparable-shell
points. The long character high-pass is transverse to determinant fibres;
it is not a long alternating sum after the determinant is fixed.

## 2. Two-dimensional self-return

For \(C=c/\kappa_i\), set

\[
 f(p,q)=C\left({a\over b}-{a+p\over b+q}\right).
\]

Writing \(x=b+q\), \(y=a+p\),

\[
 \det\nabla^2 f=-{C^2\over x^4}.
\]

For the Fourier convention \(e(f-up-vq)\), stationarity gives
\(u=-C/x\), \(v=Cy/x^2\), and the exact critical phase

\[
 f-up-vq={Ca\over b}+au+bv+{Cv\over u}.
\tag{117.I2}
\]

Thus the nonlinear dual is again a ratio phase. M2 shifts the dual
\(p\)-frequency to a half lattice; M1 shifts the dual \(q\)-frequency.
Neither removes the stationary family. At \(B\asymp\sqrt Y\), the Hessian
determinant and the two-dimensional stationary amplitude are both of
constant order. The \(B^2/W\) primal strip maps to the same number of dual
modes, so Cauchy, Plancherel, or a coefficient-blind large sieve after the
transform contains the diagonal

\[
 {B^2\over DL}{B^2\over W}={B^4\over DLW}=Y^{43/48}
\]

at minimax. A second transform inverts (117.I2) and restores the primal
ratio phase, parity, and strip boundary. This is a rigorous obstruction to
the named transform-followed-by-norm proof class, not a lower bound for the
actual signed correlation.

Even granting independently the full M2 \(p\)-length saving
\(Y^{1/16}\) and the formal M1 \(q\)-process saving \(Y^{1/6}\) leaves
\(Y^{2/3}\). They may not be multiplied as if they arose from independent
coordinates.

## 3. Qualified cellwise product return

Distributional numerator Poisson, with the literal endpoint convention
kept inside the operator, gives the two positive-frequency product
coefficients

\[
 B_1(s;y)=\sum_{d\mid s}\chi_4(d)F_1(dy,d),\qquad
 B_2(s;y)=\sum_{rd=s}\chi_4(r)F_2(4dy,d).
\tag{117.I3}
\]

The outer constants agree. Only after deleting every truncation, profile,
Vaaler factor, scale restriction, and endpoint atom do the positive
coefficients in (117.I3) both become
\(\sum_{d\mid s}\chi_4(d)=r_2(s)/4\). The two literal truncated
orientations are different. M1 also has an axial \(m=0\) mode; fixed-profile
character Abel owns its complete random-cell square mass by

\[
 O\left({D^2\over L^2W^2}+{D\over LW}\right)\le O(Y^{1/8}).
\]

The remaining hard profile/endpoint atoms must stay inside the exact
Poisson operator. Inverting it returns the full cell amplitude. It
preserves the full positive random-cell norm, not the one-sided
off-diagonal separately, and supplies no positivity for the literal
truncated coefficient. Record (117.I3) as a diagnostic representation,
not as the missing estimate.

## 4. Source and downstream scope

Bettin--Chandee and Dong--Robles--Zeindler concern separable bilinear or
trilinear inverse-modular Kloosterman-fraction forms. No literal reduction
was obtained from the real-centre ratio phase with a variable triangular
top, coupled two-ray coefficients, all determinants, hard endpoints, and
moving strata to their hypotheses. No source theorem is imported.

Popov's aggregate local discrepancy estimate remains a ceiling for the
full discrepancy; it cannot be reversed to bound a fixed positive block or
the prescribed-centre product wave.

Promote only the exact half-shift/Legendre chart and its scoped
transform-and-norm obstruction. Reject fixed-fibre long alternation,
residue-sector absolute values, multiplying the two one-variable gains,
clean literal \(r_2/4\) completion, product-wave positivity, and direct
Kloosterman-fraction transfer. No global exponent or M9 status changes.

Evidence:

- `reports/blind_determinant_fibre_rederivation.md`;
- `reports/determinant_fibre_hostile_source_audit.md`;
- `reports/actual_character_determinant_attack.md`;
- `reviews/hostile_round117_discovery_addendum.md`.
