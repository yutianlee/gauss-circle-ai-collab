# Conductor candidate: dual gcd progressions and the parity-resonance frontier

## 1. Result

The literal incidence equation

\[
 d'm'-dm=r,\qquad 1\le r<R=\lceil L\rceil,
\]

has two multiplicity-one gcd normal forms.  The divisor-gcd form freezes
the complete \(\chi _4(d')\chi _4(d)\) sign along each short arithmetic
row.  The cofactor-gcd form shows an exact parity dichotomy: after imposing
that both character-bearing divisors are odd, the character product is
constant along every even-shift row and alternates along every odd-shift
row.  Thus the effective row phase is

\[
 \Psi(k)+{(r\bmod 2)k\over2}.
\]

The real first derivative has size \(J(r/s)/L\) in the cofactor-gcd form,
but its required distance from integers (or half-integers for odd \(r\))
is uncontrolled.  The classical real second-derivative estimate is
strictly worse than the trivial row bound throughout the inherited range.
Moreover, the residual selector and squarefree masks may jump at every row
point.  Consequently, gcd reparametrization, large real derivative, local
\(\chi _4\) alternation, or shiftwise coefficient energy alone cannot
prove the \(L^2X^\varepsilon\) aggregate target.  The exact normal forms
nevertheless isolate the remaining arithmetic-resonance theorem without
discarding the aggregate real part.

## 2. Exact statement and hypotheses

Use all notation and every zero-extension convention of (164.K10)--
(164.K11).  In particular, \(d,d'\) are odd, both products lie in the
literal \(N\)-shell, and the coefficient masks include squarefreeness,
both residual selectors, both parity branches, all profiles, and all hard
values.

### Divisor-gcd normal form

For a literal tuple put

\[
 g=(d,d'),\qquad d=gu,\qquad d'=gv,
 \qquad (u,v)=1.
\tag{165.C1}
\]

Then \(g,u,v\) are odd and

\[
 g\mid r,\qquad r=gh,\qquad vm'-um=h.
\tag{165.C2}
\]

For any one integral solution \((m_0,m'_0)\), all integral solutions are

\[
 m=m_0+vt,\qquad m'=m'_0+ut,\qquad t\in\mathbb Z.
\tag{165.C3}
\]

Writing

\[
 A=gu m_0,\qquad K=guv={dd'\over g},
\tag{165.C4}
\]

one has

\[
 N(t)=A+Kt,\qquad N(t)+r=A+r+Kt,
 \qquad \chi _4(d')\chi _4(d)=\chi _4(uv).
\tag{165.C5}
\]

The literal support deletes points from a consecutive \(t\)-interval of
length

\[
 O(1+M_L/K)=O(1+g),
\tag{165.C6}
\]

because \(M_L\asymp L^2\), \(d,d'\asymp L\), and
\(K=dd'/g\asymp L^2/g\) whenever both physical legs are nonzero.

### Cofactor-gcd normal form

Put

\[
 s=(m,m'),\qquad m=su,\qquad m'=sv,
 \qquad (u,v)=1.
\tag{165.C7}
\]

Then

\[
 s\mid r,\qquad r=sh,\qquad vd'-ud=h.
\tag{165.C8}
\]

For one solution \((d_0,d'_0)\), all solutions are

\[
 d=d_0+vt,\qquad d'=d'_0+ut.
\tag{165.C9}
\]

The simultaneous oddness of \(d,d'\) restricts \(t\) to one parity, so
write \(t=t_0+2k\).  Then

\[
 d=D_0+2vk,\qquad d'=D'_0+2uk,
\tag{165.C10}
\]

and, with \(N_0=mD_0\) and \(K_s=2suv=2mm'/s\),

\[
 N(k)=N_0+K_sk,\qquad N(k)+r=N_0+r+K_sk.
\tag{165.C11}
\]

On every supported squarefree row,

\[
 \chi _4(d(k))\chi _4(d'(k))
 =\sigma_0(-1)^{(r\bmod2)k},
 \qquad \sigma_0\in\{-1,1\}.
\tag{165.C12}
\]

Again the literal support deletes points from an interval of length
\(O(1+s)\).

For either normal form, let \(K\) denote the actual product increment when
the chosen integer row parameter increases by one (thus \(K=guv\) for
(165.C3), and \(K=K_s=2suv\) for (165.C10)).  Write the unshifted product
as \(x=A+Kk\) in that row parameter and put

\[
 \Psi(k)=J(\sqrt{x+r}-\sqrt x).
\tag{165.C13}
\]

In the cofactor-gcd form, where \(K\asymp L^2/s\) and \(r=sh\),

\[
\begin{aligned}
 \Psi'(k)
 &= {JK\over2}\{(x+r)^{-1/2}-x^{-1/2}\},\\
 \Psi''(k)
 &= {JK^2\over4}\{x^{-3/2}-(x+r)^{-3/2}\},\\
 \Psi'''(k)
 &= {3JK^3\over8}\{(x+r)^{-5/2}-x^{-5/2}\}.
\end{aligned}
\tag{165.C14}
\]

Uniformly on a fixed enlarged physical box,

\[
 |\Psi'(k)|\asymp {Jh\over L},\qquad
 \Psi''(k)\asymp {Jh\over sL},\qquad
 |\Psi'''(k)|\asymp {Jh\over s^2L}.
\tag{165.C15}
\]

The exact aggregate may therefore be written as a multiplicity-one sum of
actual row weights \(B_{s,h,u,v}(k)\) against

\[
 e\!\left(\Psi(k)+{(r\bmod2)k\over2}\right),
\tag{165.C16}
\]

with the Fejer weight \(1-sh/R\) outside and with no modulus around an
individual row or shift.  Here \(B\) retains every literal arithmetic and
profile factor; it is zero off the exact row domain.

## 3. Proof or derivation

Equations (165.C1)--(165.C5) follow by dividing
\(d'm'-dm=r\) by \(g=(d,d')\).  Bezout's theorem gives (165.C3), and
substitution gives (165.C5).  Since \(g,u,v\) are odd,
\(\chi _4(g)^2=1\), proving the character identity.  Intersecting the
linear product progression with the consecutive shell proves (165.C6);
every remaining literal restriction only deletes row points.

The same argument with \(s=(m,m')\) proves (165.C7)--(165.C11).  It
remains to prove (165.C12).  If \(r\) is odd, the products \(dm\) and
\(d'm'\) have opposite parity.  Hence \(m,m'\), and therefore \(u,v\),
have opposite parity.  In (165.C10), exactly one of the increments
\(2u,2v\) is \(2\pmod4\), while the other is \(0\pmod4\).  Exactly one
of the two \(\chi _4\)-factors changes sign when \(k\) increases by one.

If \(r\) is even, the two products have the same parity.  When they are
odd, \(m,m'\), hence \(u,v\), are odd.  When they are even and
squarefree, their common factor \(s\) contains the unique factor \(2\),
and the coprime quotients \(u,v\) are again odd.  Thus both character
factors change sign under \(k\mapsto k+1\), and their product is fixed.
This proves (165.C12).  Direct differentiation gives (165.C14), and
\(x\asymp L^2\), \(K\asymp L^2/s\), \(r=sh\) give (165.C15).

## 4. First doubtful or unproved step

No bound of the form

\[
 \Re\mathfrak C_{R,J,L}^{\rm rem}
 \ll_\varepsilon L^2X^\varepsilon
\tag{165.C17}
\]

has been proved.  The missing step is an aggregate theorem for the actual
row weights in (165.C16).  Large \(|\Psi'|\) is irrelevant without
control of

\[
 \left\|\Psi'(k)+{r\bmod2\over2}\right\|_{\mathbb R/\mathbb Z}.
\tag{165.C18}
\]

Even on common smooth physical cells, the squarefree masks and the
\(N\)-dependent residual selectors inside \(B(k)\) can jump at every
integer.  Hence neither an \(O(1)\) variation claim for the complete row
weight nor an automatic adjacent-term cancellation is available.

## 5. Required controls and outcomes

- **Multiplicity:** both gcd maps and their inverse progressions are
  bijective after a base solution is fixed.  Outcome: pass.
- **Parity:** odd shifts add exactly a half-frequency; even shifts add no
  half-frequency.  Outcome: pass.
- **Large-derivative false gain:** since \(s< R\asymp L\) and
  \(J\gg L^2\), (165.C15) gives \(\Psi''\gg1\).  The classical real
  second-derivative estimate
  \(T\sqrt\lambda+\lambda^{-1/2}\), with
  \(T\ll s\) and \(\lambda\asymp Jh/(sL)\), is worse than the trivial
  \(T\)-bound.  Outcome: the second-derivative route is vacuous, not a
  disproof of all higher-order or arithmetic methods.
- **Shiftwise modulus:** Cauchy on each shift gives
  \(\sum_N|c_{N+r}^{\rm rem}c_N^{\rm rem}|
  \ll_\varepsilon L^2X^\varepsilon\); summing \(R\asymp L\) shifts
  restores \(L^3X^\varepsilon\).  Outcome: exact missing factor \(L\).
- **Actual coefficient:** the selector and squarefree masks remain inside
  \(B\).  Outcome: no arbitrary-array or smooth-weight substitution.
- **Geometry:** (165.C1)--(165.C16) concern the additive product shift and
  do not invoke the multiplicative character-Poisson collar.  Outcome:
  pass.
- **Scope:** even a proof of (165.C17) would close only the residual
  \(t=1\) scalar through the accepted Fejer connector.  Outcome: no
  downstream transfer.

## 6. Dependencies and exact artifacts used

- `state/active_campaign.yml`;
- `proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md`;
- `proofs/kernels/m9_m2_hard_top_t1_close_opposite_prime_exchange_sector.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/candidates/conductor_round165_short_shift_seed.md`.

No numerical experiment and no external theorem is used.

## 7. Recommended state effect

Retain as a candidate exact reduction.  Promote only after independent
seam review verifies the squarefree even-even parity case, row
multiplicity, support length, phase derivatives, and the precise scope of
the first/second-derivative no-go.  Do not change the residual target, any
parent, any downstream theorem, or either exponent.
