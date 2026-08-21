## 1. Result

**Exact full-two-adic actual-row reduction.**  Let a canonical M1 class
modulus be written

\[
 M=qN,\qquad q=2^\nu,\qquad (q,N)=1.
\]

If \(q\geq2\), a nonempty two-adic unit mask forces
\(A=2a\), \(B_2=2c\), and \(V=2v\) modulo \(q\).  Its odd bases are the
single orbit

\[
 x_j=1+2j,\qquad j\pmod L,\qquad L=q/2.
\]

After the exact CRT rescaling of \(u\) and \(K\), put

\[
 \phi_j=\Phi_{2a,2c,2v}(1+2j),\qquad
 w_j=e_q\!\left(u_2(1+2j)+K_2\phi_j\right).
\]

For the literal first and second actual pair rows \(F_j^a(y)\) and
\(G_{j-v}^c(y-V_N)\), the complete local coupling is

\[
 \mathcal C_q(y)=
 \sum_{j\bmod L}w_jF_j^a(y)
       \overline{G_{j-v}^c(y-V_N)}.                         \tag{1.1}
\]

With unnormalised DFTs \(\widehat H_r=\sum_{j\bmod L}e_L(-rj)H_j\),

\[
 \boxed{\quad
 \mathcal C_q(y)=\frac1{L^2}
 \sum_{k,l\bmod L}e_L(lv)\widehat w_{\,l-k}
 \widehat F_k^a(y)\overline{\widehat G_l^c(y-V_N)}.
 \quad}                                                     \tag{1.2}
\]

Equivalently, on unitary Fourier coordinates the matrix is

\[
 \mathsf A_{w,v}(l,k)=L^{-1}\widehat w_{\,l-k}e_L(lv).       \tag{1.3}
\]

It is unitarily equivalent to multiplication by the unimodular sequence
\(w\), followed by a cyclic shift.  Hence it has rank \(L\) and operator
norm one.  Exact period or Fourier-support sparsity only decomposes this
unitary into cyclic blocks; it is not an analytic saving.

The reciprocal part \(e_q(K_2\phi_j)\) has the guaranteed period

\[
 P_\nu=1\ (\nu\leq3),\qquad P_4=2,\qquad
 P_\nu=L/8\ (\nu\geq5),                                     \tag{1.4}
\]

not necessarily its fundamental period.  Precisely,
\(\phi_{j+P_\nu}=\phi_j\pmod q\) and
\(w_{j+P_\nu}=e_L(u_2P_\nu)w_j\).  Thus \(w\) is a character twist of a
shorter periodic weight.  Nonunit \(K\) can shorten the reciprocal period
further, but cannot be discarded.  Constant-character, extra lower-period,
aligned, reversal, and generic maximal-guaranteed-period convolutions are
exact subcases of (1.2), not separate estimates.

After the global \(u=0\) owner and the successive Round-87--89 owners,
the smallest lawful survivor is one scalar sum of (1.1), over the odd
cofactor labels and then the conductor rows, with every actual row,
class, sign, alias, reflection, transition, star, zero extension,
nonunit \(K\), and nonzero modulus multiple retained.  No
\(J^{-1/6}\) gain or other analytic saving is proved.

## 2. Exact statement and hypotheses

The accepted three-class dictionary is

\[
 (\kappa,M,K)\in
 \{(1,4b,k),\ (2,2b,2[k\bar4]_b),\ (4,b,[k\bar4]_b)\}.
                                                               \tag{2.1}
\]

Writing \(b=2^s b_{\rm odd}\), the literal valuations are

| class \(\kappa\) | \(M\) | \(\nu=v_2(M)\) | odd cofactor \(N\) | \(L\) when \(\nu\geq1\) |
|---|---:|---:|---:|---:|
| \(1\) | \(4b\) | \(s+2\) | \(b_{\rm odd}\) | \(2^{s+1}\) |
| \(2\) | \(2b\) | \(s+1\) | \(b_{\rm odd}\) | \(2^s\) |
| \(4\) | \(b\) | \(s\) | \(b_{\rm odd}\) | \(2^{s-1}\) if \(s\geq1\) |

In the displayed accepted notation, \(\bar4\pmod b\) is a literal modular
inverse, so the nonempty \(\kappa=2,4\) class domains necessarily have
\(b\) odd.  On that literal reading their actual two-parts are respectively
\(q=2,L=1\) and \(q=1\), while all higher two-parts occur in the
\(\kappa=1\) class.  If the brackets in (2.1) were intended to denote a
different convention for even \(b\), that convention is not present in
the supplied context; the general valuation row above shows exactly where
it would enter.

For \(q>1\), choose the CRT idempotent coefficients

\[
 \alpha N\equiv1\pmod q,\qquad \beta q\equiv1\pmod N,
\]

and reduce

\[
 u_2=\alpha u\pmod q,\quad K_2=\alpha K\pmod q,
 \qquad
 u_N=\beta u\pmod N,\quad K_N=\beta K\pmod N.                \tag{2.2}
\]

All physical shifts are reduced in both factors.  The notation \(u_2,K_2\)
is suppressed in (1.1) only after this rescaling; using the unscaled global
labels in the local additive character would be incorrect.  For \(q=1\)
the local factor is the one-point identity, and no fictitious value
\(L=1/2\) is introduced.

The odd-cofactor phase is retained separately:

\[
\begin{split}
 \phi_N(y)={}&\bar y-\overline{y-A_N}-\overline{y-V_N}
 +\overline{y-V_N-B_{2,N}}\pmod N,\\
 w_N(y)={}&e_N\!\left(u_Ny+K_N\phi_N(y)\right),              \tag{2.3}
\end{split}
\]

on the literal four-unit mask modulo \(N\).  Thus the full CRT weight at
\(X_j(y)\) is exactly \(w_jw_N(y)\); neither inverse phase is absorbed
into an owner or dropped.

For \(q\geq2\), the local mask

\[
 x,\quad x-A,\quad x-V,\quad x-V-B_2\quad\hbox{all odd}       \tag{2.4}
\]

is empty unless \(A,B_2,V\) are even; if they are even, every one of the
\(L\) odd residues occurs exactly once.  Set

\[
\begin{split}
 \phi_j={}&(1+2j)^{-1}-(1+2j-2a)^{-1}\\
          &-(1+2j-2v)^{-1}+(1+2j-2v-2c)^{-1}\pmod q.         \tag{2.5}
\end{split}
\]

For an odd residue \(y\pmod N\), let \(X_j(y)\pmod M\) be the CRT lift
of \((1+2j,y)\).  At row-function level the two sequences in (1.1) are
exactly the restrictions of

\[
 \mathcal R_{b,X_j(y)}\overline{\mathcal R_{b,X_{j-a}(y-A_N)}}
 \quad\hbox{and}\quad
 \mathcal R_{b,X_{j-v}(y-V_N)}
 \overline{\mathcal R_{b,X_{j-v-c}(y-V_N-B_{2,N})}},         \tag{2.6}
\]

with the accepted dyadic multiplier, signs, aliases, reflected
orientation, entry/exit, stars, and zero extension left in place.  After
Fourier expansion, their four coefficient slots are, in order,

\[
 I_b(n+d+u),\quad \overline{I_b(n)},\quad
 \overline{I_b(m+d)},\quad I_b(m),                            \tag{2.7}
\]

namely the literal symbol

\[
 \Omega_{b,d,u}(n,m)=I_b(n+d+u)\overline{I_b(n)}
 \overline{I_b(m+d)}I_b(m).                                  \tag{2.8}
\]

Thus \(F,G\) in (1.1) are not arbitrary coefficient sequences.

The normalisations agree in either order of expansion.  If
\(\mathfrak T_q=q\sum_{j\bmod L}w_j\) and
\(\mathfrak T_N=N\sum_y^{\rm odd\ mask}w_N(y)\), then

\[
 \mathfrak T_M=\mathfrak T_q\mathfrak T_N,
 \qquad
 \frac{\mathfrak T_M}{M^2}
 =\frac{\mathfrak T_q}{q^2}\frac{\mathfrak T_N}{N^2},
 \qquad
 M^{-5}\mathfrak T_M=M^{-4}\sum_{x\bmod M}^{\rm mask}w_x.  \tag{2.9}
\]

The four canonical rows \(\mathcal R_{b,x}=M^{-1}\sum_n I_b(n)
e_M(nx)e(n\theta)\) supply exactly the same \(M^{-4}\).  Formula (1.2)
introduces only \(L^{-2}\); there is no extra or missing \(q\), \(N\),
\(L\), or four-independent-lifts factor.

## 3. Proof or derivation

CRT factorisation of the unit mask, inversion, and additive character gives

\[
 e_M(z)=e_q(\alpha z_q)e_N(\beta z_N).
\]

Multiplying the two complete factors, including their leading \(q\) and
\(N\), gives the leading \(M=qN\) in \(\mathfrak T_M\), which proves
(2.9).  Condition (2.4) follows because subtracting a shift preserves odd
parity exactly when that shift is even.  The map \(j\mapsto1+2j\) is a
bijection from \(\mathbb Z/L\mathbb Z\) to the odd residues modulo \(q\),
so the orbit has length exactly \(L\), even when some actual rows vanish by
zero extension.

Fourier inversion gives

\[
 w_j=L^{-1}\sum_r e_L(rj)\widehat w_r,\quad
 F_j=L^{-1}\sum_k e_L(kj)\widehat F_k,\quad
 \overline{G_{j-v}}=L^{-1}\sum_l e_L(-l(j-v))
 \overline{\widehat G_l}.
\]

The sum over \(j\) imposes \(r+k-l=0\), proving (1.2).  If
\(\widetilde F=L^{-1/2}\widehat F\) and
\(\widetilde G=L^{-1/2}\widehat G\), (1.2) is the coefficient of the
matrix (1.3).  The circulant matrix \(L^{-1}\widehat w_{l-k}\) is the
Fourier conjugate of multiplication by \(w_j\), and
\(e_L(lv)\) is a unitary diagonal shift factor.  Since \(|w_j|=1\),
\(\mathsf A_{w,v}\) is unitary and full rank.

There is a useful exact refinement of the local period.  Write

\[
 z_j=e_q(K_2\phi_j),\qquad
 w_j=e_q(u_2)e_L(u_2j)z_j.                                   \tag{3.1}
\]

For \(q=4,8\), every odd residue is self-inverse, and direct substitution
in (2.5) gives

\[
 \phi_j\equiv2(a-c)\pmod q.                                  \tag{3.2}
\]

For \(q=16\), shifting \(x\) by four gives

\[
 (x+4)^{-1}-x^{-1}=-4[x(x+4)]^{-1}\equiv-4\pmod {16}
\]

for every odd \(x\); the four signed copies cancel, so \(\phi_{j+2}
=\phi_j\).  For \(q=2^\nu\), \(\nu\geq5\), put \(h=q/8\).  Then

\[
 (x+h)^{-1}-x^{-1}=-h[x(x+h)]^{-1}\pmod q.                   \tag{3.3}
\]

Only the bracket modulo eight matters.  It is constant for odd \(x\): it
is \(5\pmod8\) when \(q=32\), and \(1\pmod8\) when \(q\geq64\).
Again the coefficients \(1,-1,-1,1\) cancel.  Since an \(x\)-shift by
\(q/8\) is a \(j\)-shift by \(q/16=L/8\),

\[
 \phi_{j+L/8}=\phi_j\pmod q\qquad(q\geq32).                  \tag{3.4}
\]

Let \(h_K\) be the least divisor \(h\mid L\) such that

\[
 K_2(\phi_{j+h}-\phi_j)\equiv0\pmod q\quad\hbox{for every }j.\tag{3.5}
\]

Then \(h_K=1\) for \(q\leq8\), \(h_K\leq2\) for \(q=16\), and
\(h_K\leq L/8\) for \(q\geq32\).  Fourier orthogonality applied to the
\(h_K\)-periodic sequence \(z\) yields

\[
 \widehat w_r=0\quad\text{unless}\quad
 r\equiv u_2\pmod{L/h_K}.                                   \tag{3.6}
\]

This gives the exact symbol classification:

- **constant weight:** \(h_K=1\) and \(u_2\equiv0\pmod L\);
- **nonconstant pure character:** \(h_K=1\) and
  \(u_2\not\equiv0\pmod L\); (1.3) is a monomial unitary;
- **extra lower-period convolution:** \(1<h_K<h_0\), where
  \(h_0=2\) for \(q=16\) and \(h_0=L/8\) for \(q\geq32\);
- **generic full two-adic convolution:** \(h_K=h_0\), with no further
  collapse; its Fourier kernel is supported on at most \(h_0\) cyclic
  diagonals but the matrix is still full rank.

For orientation-preserving alignment one first needs the full physical
condition \(B_2=A\), not merely \(c=a\pmod L\).  The second pair is then a
translate of the first by \(V\), with full return order

\[
 R_{\rm al}^{\rm full}
 =\operatorname{lcm}\!\left(
 {L\over\gcd(L,v)},{N\over\gcd(N,V_N)}\right).               \tag{3.7}
\]

Only when the odd labels themselves align, so \(B_{2,N}=A_N\) and
\(V_N=0\), do the actual orbit families satisfy \(G=F\) at the same odd
base and (3.7) reduce to the local quotient.  In that subcase

\[
 \mathcal C_q=\sum_jw_jF_j\overline{F_{j-v}}.                 \tag{3.8}
\]

The local return length is exactly

\[
 R_{\rm al}=\operatorname{ord}_{\mathbb Z/L\mathbb Z}(v)
 =\frac L{\gcd(L,v)}.                                        \tag{3.9}
\]

When \(w\) is constant, (3.8) diagonalises to
\(L^{-1}w_0\sum_ke_L(kv)|\widehat F_k|^2\); for nonconstant \(w\) it is
still the full cross-frequency coefficient (1.2).  Physical reversal first
requires \(B_2=-A\).  Its full return order is

\[
 R_{\rm rev}^{\rm full}
 =\operatorname{lcm}\!\left(
 {L\over\gcd(L,v-a)},{N\over\gcd(N,V_N-A_N)}\right).          \tag{3.10}
\]

Only when \(B_{2,N}=-A_N\) and \(V_N=A_N\) does this reduce to the local
odd-label reversal \(c\equiv-a\pmod L\), in which case

\[
 G_{j-v}^{-a}=\overline{F_{j-v+a}^{a}},\qquad
 \mathcal C_q=\sum_jw_jF_jF_{j-(v-a)},                        \tag{3.11}
\]

with local return length \(R_{\rm rev}=L/\gcd(L,v-a)\).  Its DFT is the
Hankel-type identity

\[
 \mathcal C_q=L^{-2}\sum_{k,l}\widehat w_{-k-l}
 e_L(-l(v-a))\widehat F_k\widehat F_l,                        \tag{3.12}
\]

not a positive square.

Finally apply ownership before naming a survivor.  For the exact canonical
index set \(\mathscr U_{b,U}\), let

\[
 \mathscr H_{b,U}=\{u\ne0\}\cap\mathscr U_{b,U}
 \setminus(\mathscr O_{87}\sqcup\mathscr O_{88,c}
 \sqcup\mathscr O_{88,g}\sqcup\mathscr O_{89}),              \tag{3.13}
\]

where each owner is taken on the successive complement.  Same-group
aligned or reversal terms are first tested against \(\mathscr O_{87}\).
On its complement, a fully aligned term with
\(R_{\rm al}^{\rm full}\leq\rho_*\), or a fully reversed term with
\(R_{\rm rev}^{\rm full}\leq\rho_*\), is coarse-owned.  The local
quotients (3.9) and its reversal analogue may be used for that test only
under the stated exact odd-label conditions.  A lower-period symbol is
Round-89-owned only when its complete cell or summable union satisfies the
accepted directed-degree threshold; period alone does not own it.  The
good-prime and remaining certified cell owners are then applied in their
accepted order.

If \(\mathfrak a_\lambda\) denotes the exact remaining Fejer weight,
dyadic multiplier, signs, aliases, reflections, and canonical scalar
prefactor for a tuple \(\lambda\), the smallest complete survivor is

\[
 \boxed{
 \mathscr S_{2\text{-adic}}(U)=
 \sum_{b\asymp B}\ \sum_{\lambda\in\mathscr H_{b,U}}
 \mathfrak a_\lambda
 \sum_{y\bmod N_\lambda}^{\rm odd\ mask}
 w_{N_\lambda,\lambda}(y)\,
 \mathcal C_{q_\lambda,\lambda}(y).
 }                                                            \tag{3.14}
\]

Here \(\mathfrak a_\lambda\) omits none of the canonical factors and
\(\mathcal C\) uses the four normalised rows (2.6), so their \(M^{-4}\)
is already present.  Equivalently one may use unnormalised row numerators
and place exactly one \(M^{-4}\) in \(\mathfrak a_\lambda\).  The
conductor sum in (3.14) is taken before the absolute value.  Equations
(3.6)--(3.12) label disjoint algebraic subcases inside (3.14); they do not
permit any of them to be deleted unless (3.13) assigns an accepted owner.

## 4. First doubtful or unproved step

There is no doubtful step in the finite CRT, orbit, DFT, period, or
normalisation identities above.  The first genuinely unproved step is an
estimate for the fixed actual-vector scalar (3.14), after summing the odd
cofactor labels and conductor rows and before taking absolute value.  The
unitary local matrix has no norm gap, so (1.2) alone cannot supply the
required top \(J^{-1/6}\).

There is also one explicit typing seam for the conductor to resolve in any
durable statement: (2.1) does not separately state the admissible parity of
\(b\) in the \(\kappa=2,4\) classes.  If \(\bar4\) has its standard
meaning, \(b\) is necessarily odd and the specialisation stated after the
table is forced.  If a nonstandard bracket convention is intended, its
definition is required before claiming different two-adic valuations for
those two classes.  This does not affect the general \(M=2^\nu N\)
identity.

## 5. Required control test and outcome

All controls were exact finite-algebra checks; no floating-point or
asymptotic computation was used.

- **Full power, nonempty mask, and orbit — pass.**  Parity proves the mask
  is empty unless \(A,B_2,V\) are even, and otherwise the orbit has exactly
  \(L=q/2\) points.  The \(q=1\) class is handled separately.
- **Local phase and higher resonance — pass.**  At \(q=32\), take
  \((a,c,v)=(1,2,0)\).  Then
  \(\phi_j=22,30,22,30,\ldots\pmod {32}\).  Both values are
  \(6\pmod8\), so a mod-eight quotient sees a constant phase while the
  full power sees a genuine two-step weight.  For odd \(K\),
  \(\widehat w\) lies on the two frequencies
  \(r\equiv u_2\pmod8\).  This directly rejects the Round-100 mod-eight
  shadow for higher \(\nu\).
- **DFT normalisation — pass.**  Three inverse transforms and one
  \(j\)-orthogonality sum give \(L^{-2}\), while unitary Fourier
  coordinates give exactly the matrix factor \(L^{-1}\).  Direct
  conjugation to multiplication by \(w\) verifies rank \(L\) and norm one.
- **Round-100 recovery — pass.**  For \(q=8\) and
  \(a=c=v=1\), \(\phi_j=0\).  If \(4\mid u\), (1.2) reduces to
  \(\frac14\sum_ke_4(k)\widehat F_k\overline{\widehat G_k}\).
  The scalar trace factor is \(+1/2\) for \(8\mid u\) and \(-1/2\) for
  \(u\equiv4\pmod8\), exactly as in Round 100.  Alignment has
  \(R_{\rm al}=4\), hence is the accepted coarse-owned slice.
- **Actual four rows, entry/exit, and zero extension — pass.**  The four
  slots (2.7) occur once.  Zeros in an actual row merely set entries of
  \(F\) or \(G\) to zero and do not shorten the unit orbit or license
  deletion of transition terms.
- **Unique \(u=0\) owner and modulus multiples — pass.**  Equation (3.13)
  removes only the integer \(u=0\).  A nonzero \(u\) with
  \(u_2=0\), including a nonzero multiple of \(q\) or \(M\), remains.
  Local constancy is therefore not confused with the global owner.
- **Nonunit \(K\), period depth, and self-return — pass.**  Definition
  (3.5) includes all \(K\), including \(K=0\pmod{2^t}\).  A shorter
  period changes the support coset (3.6), but the exact Fourier matrix
  remains unitary and full rank.
- **Aligned and reversal owners — pass.**  The exact full return quotients
  are (3.7) and (3.10).  They are removed only if the
  successive Round-87--89 owner tests say so; long-return aligned or
  reversal terms remain in (3.14).  Reversal gives (3.12), not a positive
  square.
- **Odd cofactor and conductor sum — pass.**  CRT coefficients \(\alpha\)
  and \(\beta\), the odd mask, the literal odd inverse weight (2.3), and
  all three class valuations are explicit.  The scalar in (3.14) takes
  the conductor sum before absolute value.
- **Arbitrary-coefficient false shadow — pass as a no-go control.**  For
  arbitrary \(F,G\), the local operator already has norm one.  Hence local
  Fourier sparsity cannot prove an arbitrary-vector gain; any future gain
  must use the literal four rows jointly with odd and conductor
  cancellation.
- **Downstream scope — pass.**  No canonical Gram estimate, GAR,
  blockwise M9-M1, M9-M2, endpoint-uniformity statement, M9, or exponent is
  inferred.

## 6. Dependencies and exact artifacts used

The derivation uses only the following assigned artifacts:

- `protocol.md` for the report contract, owner discipline, and
  nonpromotion rule;
- `state/proof_obligations.yml`, specifically the accepted
  `M9-M1-q8-actual-vector-cross-projection-reduction`, the accepted
  `M9-M1-bad-prime-cellwise-period-graph-bound`, and the open
  `M9-M1-canonical-hard-actual-vector-directional-estimate`;
- `state/active_campaign.yml` for the frozen Round-101 target and controls;
- `rounds/codex-managed/m9-m1-full-two-adic-orbit-convolution/derivation_packet.md`
  for the full local weight, mask, mandatory owners, and scope;
- `rounds/codex-managed/m9-canonical-core-formalization/candidates/conductor_canonical_core_statements.md`
  for the three class moduli, canonical rows, fourfold symbol,
  normalisation, and owner order;
- `rounds/codex-managed/m9-m1-bad-prime-period-fibre-energy/synthesis.md`
  for the cellwise period/degree threshold and the prohibition on turning
  period depth into a union estimate;
- `rounds/codex-managed/m9-m1-actual-vector-coherent-mode-projection/candidates/conductor_q8_actual_vector_cross_projection.md`
  and
  `rounds/codex-managed/m9-m1-actual-vector-coherent-mode-projection/synthesis.md`
  for the \(q=8\) normalisation, cross-projection, aligned owner, and
  downstream scope.

No external theorem or web source is used.  All new claims are finite CRT
and Fourier algebra.

## 7. Recommended state effect

**Promote** a scoped reduction, “full two-adic actual-row orbit
convolution,” consisting of (1.1)--(1.3), the class-valuation and CRT
normalisations (2.1)--(2.9), the exact character-twisted period support
(3.1)--(3.6), and the successive owner/survivor formula
(3.13)--(3.14).  Treat the existing \(q=8\) node as its \(\nu=3\)
specialisation, not as a quotient of the higher two-parts.

**Retain open** the fixed actual-vector directional estimate and every
analytic or downstream parent.  In particular, do not promote a low-rank,
operator-norm, period-depth, aligned-square, reversal-square, or
arbitrary-coefficient claim.  The next core task, if selected by the
conductor, is to estimate precisely the scalar (3.14), with the residual
constant-character, certified/un-certified lower-period, long-return
aligned/reversal, and generic maximal-period pieces all present exactly
once.
