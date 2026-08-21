# Round 101 hostile owner and source audit

## 1. Result

**Verdict: certify the full two-adic orbit/DFT identity, but reject every
low-rank, spectral-saving, or automatic-aligned-owner inference from it.**
For a nonempty \(2^\nu\)-local mask, all allowed bases are the odd residues,
so the orbit \(x=1+2j\) has exact length

\[
 L=2^{\nu-1}.
\]

With the unnormalized DFT convention fixed in Section 2, the literal
four-row coupling is exactly

\[
 \mathcal C_{q}(F,G)
 ={1\over L^2}\sum_{k,l\bmod L}
 e_L(lv)\widehat w_{\,l-k}\widehat F_k^a
 \overline{\widehat G_l^c},
 \qquad q=2^\nu.                                                    \tag{1.1}
\]

There is no missing \(L\)-factor in (1.1). More importantly, because
\(|w_j|=1\) on every one of the \(L\) allowed bases, its normalized DFT
matrix

\[
 \mathcal B_{k,l}=L^{-1}e_L(lv)\widehat w_{\,l-k}                     \tag{1.2}
\]

is unitary. It therefore has rank \(L\), all singular values equal to one,
and no local norm saving. A constant weight gives a diagonal unitary; a
character gives a monomial unitary; a lower-period reciprocal factor gives
unitary blocks permuted by the affine frequency. Fourier sparsity is thus an
exact routing identity and an exact self-return, not a rank or power gain.

There is a uniform twisted-period routing lemma. Put

\[
 P_\nu=
 \begin{cases}
 1,&\nu\leq3,\\
 2,&\nu=4,\\
 L/8,&\nu\geq5.
 \end{cases}                                                          \tag{1.3}
\]

Then the reciprocal phase satisfies
\(\Phi(1+2(j+P_\nu))\equiv\Phi(1+2j)\pmod{2^\nu}\), so

\[
 w_{j+P_\nu}=e_L(u_qP_\nu)w_j,\qquad
 \widehat w_r=0\ \ \text{unless}\ \
 r\equiv u_q\pmod{L/P_\nu}.                                          \tag{1.4}
\]

This \(P_\nu\) is a guaranteed period of the reciprocal phase, not its
fundamental period. Formula (1.4) gives singleton support for \(\nu\leq3\),
one affine class modulo \(4\) for \(\nu=4\), and one affine class modulo
\(8\) for \(\nu\geq5\). In every case (1.2) is still full rank.

The hostile owner check also finds a necessary correction to any naive
extension of Round 100. Suppose the odd-cofactor labels are aligned and the
full local pair shapes agree, so \(B_2=A\) and \(V_q=2v\). Then the coarse
return order is

\[
 R_*={L\over\gcd(L,v)}.                                               \tag{1.5}
\]

Round 100 had \(L=4,v=1\), hence \(R_*=4\leq\rho_*\). For higher
\(2\)-parts, \(v\) may be odd and \(R_*=L>\rho_*\). Such an aligned
autocorrelation is not automatically coarse-owned. It is Round-87-owned
only when \(R_*=1\), Round-88-coarse-owned only when
\(1<R_*\leq\rho_*\), and otherwise remains for the later owners and possibly
the hard complement. Exact reversal is likewise a distinct ordered edge,
not a same-group deletion.

The smallest complete object left for a later core attack is therefore not
one sparse DFT mode. It is the scalar sum of the full-rank matrix
coefficients (1.1) over the literal Round-87--89 hard complement, with the
odd completed factor, all four actual rows, integer \(u\ne0\), class and
conductor sums, transitions, and zero extension retained. Denote this exact
survivor by \(\mathscr C_{2,\mathrm{hard}}(U)\). No estimate for it is proved.

## 2. Exact statement and hypotheses

Let

\[
 M=qN,\qquad q=2^\nu,\qquad N\ {\rm odd},\qquad L=q/2,
\]

with \(\nu\geq1\). The three accepted class moduli are treated separately at
their literal value of \(\nu=v_2(M)\); if \(\nu=0\), there is no two-adic
operator to which this statement applies. If the symbols \(u,K\) below have
not already absorbed the CRT character inverse, they mean
\(u_q=\overline N_q u\) and \(K_q=\overline N_qK\) modulo \(q\). Dropping
this bar is harmless only as a declared relabelling by an odd unit.

For a nonempty local mask write

\[
 A=2a,\qquad B_2=2c,\qquad V=2v\pmod q,
 \qquad a,c,v\pmod L,
\]

and, for odd \(x\),

\[
 \Phi_{A,B_2,V}(x)
 =x^{-1}-(x-A)^{-1}-(x-V)^{-1}+(x-V-B_2)^{-1}\pmod q.              \tag{2.1}
\]

The complete local weight is

\[
 w_j=e_q\!\left(u_q(1+2j)+K_q
 \Phi_{2a,2c,2v}(1+2j)\right),\qquad j\pmod L.                      \tag{2.2}
\]

Every inverse and the entire phase modulo \(q\) are retained. In particular,
(2.2) is not its reduction modulo \(8\), and \(K_q\) need not be a unit.

Let \(F_j^a\) contain the two actual physical rows at local indices
\((j,j-a)\), and let \(G_{j-v}^c\) contain the other two at
\((j-v,j-v-c)\). Signs, aliases, reflected orientation, stars, the dyadic
multiplier, entry/exit, and every \(I_b\)-factor are part of these sequences;
missing physical entries are zero-extended to \(\mathbb Z/L\mathbb Z\). The
local coupling is

\[
 \mathcal C_q(F,G)=\sum_{j\bmod L}w_jF_j^a
 \overline{G_{j-v}^c}.                                                \tag{2.3}
\]

For any sequence \(H\) put

\[
 \widehat H_k=\sum_{j\bmod L}H_j e_L(-kj),\qquad
 H_j={1\over L}\sum_{k\bmod L}\widehat H_k e_L(kj).                 \tag{2.4}
\]

Then (1.1) holds. With
\(\widetilde F_k=L^{-1/2}\widehat F_k\) and similarly for \(G\), it is

\[
 \mathcal C_q(F,G)=\sum_{k,l}\mathcal B_{k,l}\widetilde F_k
 \overline{\widetilde G_l},
 \qquad \mathcal B_{k,l}=L^{-1}e_L(lv)\widehat w_{l-k},              \tag{2.5}
\]

and \(\mathcal B\) is unitary.

The exact full-phase period \(P(w)\mid L\) is the least positive \(P\) for
which, for every odd \(x\),

\[
 2u_qP+K_q\bigl(\Phi(x+2P)-\Phi(x)\bigr)\equiv0\pmod q.             \tag{2.6}
\]

If \(w\) itself has period \(P\) and \(d=L/P\), then
\(\widehat w_r=0\) unless \(d\mid r\), and (2.5) splits into \(d\) unitary
blocks of size \(P\). More commonly it is the reciprocal factor

\[
 r_j=e_q\!\left(K_q\Phi(1+2j)\right)                                 \tag{2.7}
\]

that has period \(P\). Since \(w_j=e_q(u_q)e_L(u_qj)r_j\), one then has

\[
 \widehat w_r=0\quad\hbox{unless}\quad r\equiv u_q\pmod d.          \tag{2.8}
\]

Thus the full affine phase permutes the \(d\) Fourier residue blocks rather
than necessarily preserving them. This distinction prevents reciprocal
period, affine cancellation, and full-phase period from being conflated.

Uniformly in \(a,c,v,K_q\), the reciprocal factor has the guaranteed period
\(P_\nu\) in (1.3), and hence the full weight obeys the twisted support
(1.4). Smaller fundamental periods or further affine cancellation may
narrow the support, but they cannot enlarge it and are not assumed.

For \(\kappa=\min(v_2(K_q),\nu)\), the reciprocal factor is a pullback from
\(2^{\nu-\kappa}\). Hence it has a guaranteed \(j\)-period dividing
\(2^{\max(\nu-\kappa-1,0)}\), and (2.8) gives an affine coset modulo at
least \(2^\kappa\). If \(q\mid K_q\), \(w\) is exactly a character. These
are identities only; none is a saving.

For normalization against the completed trace,

\[
 \mathfrak T_q=q\sum_{j\bmod L}w_j=q\widehat w_0,
 \qquad {\mathfrak T_q\over q^2}={1\over q}\sum_jw_j.               \tag{2.9}
\]

CRT gives \(\mathfrak T_M/M^2=(\mathfrak T_q/q^2)
(\mathfrak T_N/N^2)\), with the corresponding CRT-scaled arguments. The
factor \(q=2L\) in (2.9), the \(L^{-2}\) caused by the two Fourier inversions
in (1.1), and the already normalized \(M^{-1}\) physical rows are different
normalizations and must not be merged. The odd factor and the sum over
conductor rows remain outside the local identity.

For the owner test, let the two literal ordered labels be

\[
 P_x=(x,x-A),\qquad P'_x=(x-V,x-V-B_2).                               \tag{2.10}
\]

They coincide modulo a divisor \(d\mid M\) exactly when
\(d\mid V\) and \(d\mid(B_2-A)\). On the proposed aligned slice this gives
the following exact consequences.

- If the odd labels satisfy \(B_{2,N}=A_N,V_N=0\), then the raw return is
  \(R_*=L/\gcd(L,v,c-a)\).
- If in addition \(c=a\), so the two local pair families are the same, then
  (1.5) holds.
- If \(v=0\) as well, the ordered labels are identical and the Round-87
  same-group owner applies.
- Exact reversal means \(V=A\) and \(B_2=-A\) modulo \(M\). It is a distinct
  ordered label; its equality return is \(R_*=M/\gcd(M,A)\), and it is
  coarse-owned only when that return is at most \(\rho_*\).

Every surviving case must then be intersected successively with the
Round-88 good-prime and Round-89 certified cell owners. No local label is
deleted merely because it is called aligned, reversed, constant, or
lower-period.

## 3. Proof or derivation

For \(p=2\), the complete unit mask is nonempty exactly when
\(A,B_2,V\) are all even. In that case \(x\) is allowed precisely when it is
odd: subtracting any of \(A,V,V+B_2\) preserves parity. The map
\(j\mapsto1+2j\) is a bijection from \(\mathbb Z/L\mathbb Z\) to the odd
residues modulo \(q\), and translation by \(2\) has exact order \(L\).
This proves the mask and orbit assertions, including the absence of a
partially populated nonempty two-adic mask.

Insert the two inversions (2.4) into (2.3). Since

\[
 \overline{G_{j-v}^c}
 ={1\over L}\sum_l\overline{\widehat G_l^c}
 e_L(-lj+lv),
\]

the inner \(j\)-sum is

\[
 \sum_jw_je_L((k-l)j)=\widehat w_{l-k}.
\]

This proves (1.1), including the sign \(e_L(lv)\) and the factor \(L^{-2}\).

It remains to check the guaranteed period rather than assume it from the
mod-\(8\) case. For \(\nu\leq3\), every odd \(z\) satisfies
\(z^{-1}\equiv z\pmod8\), and (2.1) is the constant \(A-B_2\) on the odd
orbit. Hence \(P_\nu=1\). For \(\nu=4\), an odd \(z\) satisfies

\[
 (z+4)^{-1}-z^{-1}\equiv-4\pmod{16}.
\]

The four signed copies in (2.1) cancel, proving the period \(P_\nu=2\).
For \(\nu\geq5\), put \(h=2P_\nu=2^{\nu-3}\). The finite inverse expansion
gives

\[
 (z+h)^{-1}-z^{-1}
 \equiv-hz^{-2}+h^2z^{-3}\pmod{2^\nu},                               \tag{3.1}
\]

with the second term already zero when \(\nu\geq6\). In the four-term
signed combination, the coefficient of \(h\) is divisible by \(8\) because
every odd inverse square is \(1\pmod8\), while the coefficient of \(h^2\)
is divisible by \(2\) because every odd inverse cube is \(1\pmod2\).
Thus both contributions vanish modulo \(2^\nu\). This proves (1.3)--(1.4)
without asserting that \(P_\nu\) is minimal.

There is an even shorter rank audit. In physical coordinates (2.3) is the
matrix coefficient of multiplication by the diagonal sequence \(w_j\)
followed by a cyclic shift. Both are unitary because \(|w_j|=1\). The
unitary Fourier transform conjugates that operator to (1.2), so

\[
 \mathcal B\mathcal B^*=I_L,
 \qquad \operatorname{rank}\mathcal B=L,
 \qquad \|\mathcal B\|_{2\to2}=1.                                   \tag{3.2}
\]

Equivalently, Plancherel gives
\(\sum_r|\widehat w_r|^2=L^2\), and the shifted Fourier correlations of
\(\widehat w\) vanish because \(|w_j|^2=1\). This also shows why sparse
support cannot lower the rank.

If \(L=dP\) and the reciprocal factor \(r_j\) has period \(P\), summing over
its \(d\) lifts gives, for \(h\pmod P\),

\[
 \widehat w_{u_q+dh}=e_q(u_q)d\widehat r^{(P)}_h.                    \tag{3.3}
\]

In (1.2), the descent factor is exactly \(d/L=1/P\). Thus each nonzero
block is the normalized length-\(P\) transform, while the residue classes
are permuted by \(u_q\pmod d\). A constant reciprocal phase gives a monomial
matrix; a constant full weight gives a diagonal matrix. Both remain rank
\(L\). This is the local orbit version of the accepted completed-transform
self-return.

The arbitrary-coefficient false shadow is sharp: for any nonzero \(F\), one
may choose \(G_{j-v}=w_jF_j\), obtaining

\[
 |\mathcal C_q(F,G)|=\|F\|_2\|G\|_2.
\]

Consequently no uniform \(2^{-\delta\nu}\), \(L^{-\delta}\), or
\(J^{-1/6}\) gain can follow from the local convolution alone. The actual
rows are not arbitrary, so this is a no-go control rather than a lower bound
for the canonical coefficient.

Finally, (2.10) gives ordered equality modulo \(d\) precisely through the
two congruences \(V\equiv0\) and \(B_2-A\equiv0\pmod d\). Under odd
alignment and \(a=c\), the largest such divisor has two-part
\(2\gcd(L,v)\) and odd part \(N\), so its quotient in \(M=2LN\) is
\(L/\gcd(L,v)\). For exact reversal, equality of an ordered edge with its
reverse requires the two endpoints to coalesce, giving the quotient
\(M/\gcd(M,A)\). These computations prove the owner warnings in Section 2.

The cyclic identity remains valid through entry and exit only because the
actual sequences were zero-extended. Zero extension can annihilate an
actual Fourier mode and the successive hard mask can delete whole
configurations; neither changes the ambient identity (3.2), and neither
supplies a quantitative estimate without a separate argument.

## 4. First doubtful or unproved step

The first unproved step is any cancellation estimate for
\(\mathscr C_{2,\mathrm{hard}}(U)\) after restoring the odd completed trace,
the four actual \(I_b\)-rows, the integer \(d,u,n,m\) sums, all class
moduli, and the conductor sum before the absolute value. At the top, the
required fixed-vector gain remains \(J^{-1/6}\). Equations (1.1)--(3.3)
give norm one, not this gain.

Three tempting simplifications fail before that step.

- A lower reciprocal period only turns the matrix into normalized lower
  blocks with an affine block permutation. It does not reduce the norm or
  directed physical degree.
- Setting \(G=F\) does not make (1.1) positive. For general \(w\) it is a
  full unitary quadratic form. Even for constant \(w\), it is a shifted
  autocorrelation with Fourier phases \(e_L(kv)\). Moreover, the aligned
  slice is prior-owned only under the explicit \(R_*\)-test; higher
  two-parts can leave it hard.
- Pairing a reversal with its transpose may create a positive word in an
  operator trace, but it does not control the fixed actual-vector matrix
  coefficient or create cancellation across conductor rows.

Nonunit \(K\), nonzero \(u\equiv0\pmod q\), and nonzero modulus multiples
make these degeneracies more frequent, not safer. The global centered owner
removes only the integer \(u=0\); it does not remove a local DFT zero mode or
an integer \(u=kM\ne0\). Such integers also carry different Fejer weights
and different shifted \(I_b\)-rows, so they cannot be quotiented by
\(u\bmod M\).

No primary theorem was invoked. Finite CRT and Fourier algebra are internal,
and the selected context contains no primary result acting on the complete
powerful two-adic, nonunit-\(K\), moving actual-row matrix coefficient with
its hard owner mask and conductor sum. A source import would therefore begin
by changing the operator rather than proving the missing step.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| Full two-power, not a mod-\(8\) quotient | **Pass.** The phase is modulo \(2^\nu\), the orbit has length \(2^{\nu-1}\), and each conductor row uses its literal \(\nu\). Round 100 is only the \(\nu=3\) specialization. |
| Nonempty unit mask | **Pass.** It is empty unless \(A,B_2,V\) are even; when nonempty it is exactly all odd residues, with no partial mask. |
| Exact orbit length | **Pass.** Translation by \(2\) has order \(L=2^{\nu-1}\); the four row indices are \(j,j-a,j-v,j-v-c\pmod L\). |
| Local phase weight | **Pass.** Equation (2.2) retains the complete reciprocal phase and the CRT character inverse. |
| DFT convolution normalization | **Pass.** Two unnormalized inversions give \(L^{-2}\), the shift gives \(e_L(lv)\), and the convolution index is \(l-k\). |
| Actual four rows | **Pass as preservation only.** They occur in \(F_j^a\overline{G_{j-v}^c}\); no arbitrary vector is substituted into the claimed survivor. |
| Unique \(u=0\) owner | **Pass.** Only the integer \(u=0\) is removed once, before the hard complement. A local zero Fourier index is not that owner. |
| Nonzero modulus multiples | **Pass.** Every \(u=kM\ne0\) remains distinct with its Fejer weight and shifted actual rows, even if its local character is constant. |
| Nonunit \(K\) | **Pass as an identity; fail as a saving.** It gives a reciprocal pullback and affine-coset support, while the full DFT matrix remains unitary. |
| Period-depth self-return | **Pass as a no-go.** Equation (3.3) cancels the lift factor against \(L\); lower-period blocks retain norm one. |
| Aligned and reversal owners | **Fail for blanket deletion; pass after the exact test.** Aligned returns obey (1.5) only when the full pair shapes agree, and can exceed \(\rho_*\). Reversal is a distinct ordered edge and is coarse-owned only at its own return threshold. |
| Higher two-adic resonance | **Pass as retention.** The proved guaranteed periods are \(P_\nu=1,2,L/8\) in the three ranges, giving the affine support classes in (1.4). They need not be fundamental. Character, constant, affine-cancelled, and still-lower-period cases are all full rank and none is declared generic or negligible. |
| Entry/exit and zero extension | **Pass as typing.** Zero extension makes the cyclic formula exact but may annihilate actual modes, so it licenses neither an upper saving nor a lower obstruction. |
| Odd cofactor and conductor sum | **Pass as retention.** The odd normalized trace, full odd labels, and the scalar sum over \(b\) remain outside the local matrix coefficient and before absolute value. |
| Arbitrary-coefficient false shadow | **Pass.** The local norm-one bound is attained by an adversarial coefficient choice, disproving any saving based solely on Fourier sparsity or low rank. |
| Source-hypothesis map | **Not triggered.** No external theorem is used, and no selected source has the literal complete-operator hypotheses. |
| Downstream and exponent scope | **Pass.** No canonical estimate, GAR, blockwise M9-M1, M9-M2, endpoint-uniformity, M9, or exponent conclusion is drawn. |

No numerical experiment was used. Every positive conclusion is an exact
parity, CRT, finite Fourier, unitarity, or ordered-label computation.

## 6. Dependencies and exact artifacts used

Only the campaign-selected context and the assigned brief were used:

- protocol.md;
- state/proof_obligations.yml, in particular the three Round-101 target
  obligations, their owner dependencies, and the Round-88--100 rejected
  controls;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m1-full-two-adic-orbit-convolution/derivation_packet.md;
- rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/synthesis.md;
- rounds/codex-managed/m9-m1-bad-prime-period-fibre-energy/reports/bad_prime_hostile_source_audit.md;
- rounds/codex-managed/m9-m1-actual-vector-coherent-mode-projection/reports/coherent_projection_hostile_source_audit.md;
- strategy/conductor_0817_full_proof_strategy.md;
- rounds/codex-managed/m9-m1-full-two-adic-orbit-convolution/briefs/full_two_adic_hostile_owner_audit.md.

No sibling Round-101 claimant report, proof draft, validation matrix, legacy
derivation, or unlisted source was read. No primary-source audit was opened
because no external theorem is used or literally applicable.

## 7. Recommended state effect

**Promote as an exact internal normal form** the nonempty-mask orbit,
(1.1), the normalized unitary matrix (1.2), the full-phase period criterion
(2.6), the guaranteed twisted-period lemma (1.3)--(1.4), and the
reciprocal-period affine-coset descent (3.3). Record the
unitarity/full-rank statement as the hostile control: finite Fourier sparsity
alone cannot yield any \(J^{-1/6}\) or other power saving.

**Revise any proposed owner statement saying that every aligned full
two-adic slice is already coarse-owned.** The exact aligned return is
\(L/\gcd(L,v)\) only after both odd alignment and \(a=c\) are imposed. Route
\(R_*=1\) to Round 87, \(1<R_*\leq\rho_*\) to the Round-88 coarse owner, and
send \(R_*>\rho_*\) through the remaining Round-88/89 owners before calling
it hard. Treat exact reversal as a distinct ordered edge and apply its own
return test. The Round-100 \(R_*=4\) conclusion remains correct on its
literal \(\nu=3,v=1\) slice.

**Retain open** the smallest complete analytic survivor
\(\mathscr C_{2,\mathrm{hard}}(U)\): the odd-cofactor/conductor sum of the
full weighted unitary cross-convolutions after all successive owners. Do not
split it into separately estimated Fourier modes unless a new argument
proves that the split preserves the actual signed cancellation and reduces
the recorded capacity. Nonunit \(K\), local characters, nonzero modulus
multiples, higher resonances, transitions, stars, and zero extension remain
inside this survivor.

Make **no status change** to
M9-M1-canonical-hard-actual-vector-directional-estimate,
M9-M1-canonical-hard-actual-symbol-Gram-estimate, GAR, blockwise M9-M1,
M9-M2, endpoint uniformity, M9, or any exponent. Do not import an external
theorem.
