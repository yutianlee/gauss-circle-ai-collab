# Round 100 hostile and source audit of the coherent projection

## 1. Result

**Exact local-cross-projector reduction; no target-safe or obstructive actual-vector estimate.**  The \(q=8\) calculation survives the literal hard complement in a nonempty sense, but not in the form needed for either a positive square or a global lower bound.

On the exact conductor subfamily

\[
M=8r,\qquad r\ {\rm odd},
\]

the completed trace factors with no missing lift or normalization.  If
\(A\equiv B_2\equiv V\equiv2\pmod 8\), then

\[
 {\mathfrak T_M(u,A,B_2,V;K)\over M^2}
 ={c_8(u)\over8}
 {\mathfrak T_r(\bar8u,A_r,B_{2,r},V_r;\bar8K)\over r^2},                 \tag{1.1}
\]

where every barred \(8\) is inverted modulo \(r\).  Thus the normalized
local factor is \(+1/2\) for \(8\mid u\), \(-1/2\) for
\(u\equiv4\pmod8\), and zero otherwise.  The four allowed \(2\)-adic
bases form an exact order-four orbit.  Opening that orbit gives, for
two actual pair sequences \(F,G\),

\[
 \sum_{j\bmod4}F_j\overline{G_{j-1}}
 ={1\over4}\sum_{k\bmod4}i^k\widehat F_k\overline{\widehat G_k}.          \tag{1.2}
\]

This is a **cross-projection** on the generic hard CRT lifts.  It becomes
the proposed difference of squares only when the odd-cofactor labels
force \(G=F\):

\[
 \Re\sum_jF_j\overline{F_{j-1}}
 ={1\over4}\left(|\widehat F_0|^2-|\widehat F_2|^2\right).               \tag{1.3}
\]

That aligned slice is not hard.  Its two ordered pairs coalesce modulo
\(2r\), so its Round-88 coarse quotient is \(R_*=M/(2r)=4\); for large
\(X\), \(1<R_*\leq\rho_*\), and it is owned before the hard complement.
The generic odd CRT lifts used in the accepted \(q=8\) residual have
different pair functions and retain (1.2), not (1.3).

The hard indicator is outside the completed \(x\)-sum.  It therefore
preserves the four points of each retained local orbit, but it deletes
whole odd-cofactor cells according to the successive Round-87--89
owners.  Hence it fragments the family of local projectors and does not
produce one global eigenspace commuting with the complete hard operator.
The accepted high-degree \(q=8\) residual shows that the intersection
with the hard complement is nonempty; it does not show that every
\(q=8\) lift is hard.

All four actual \(I_b\)-rows occur in (1.1)--(1.2), but no selected
artifact proves that their fixed projection is nonzero, small by the
required \(J^{-1/6}\), or of one sign after odd-factor and conductor
summation.  Entry/exit and zero extension can annihilate individual
atoms.  Paired/backtracking words also survive conjugation closure in
ordinary trace moments, but their survival is a norm statement, not a
fixed-vector matrix coefficient.  The rigorous Round-100 output is
therefore the smaller scalar correlation in Section 2, retained as open.

## 2. Exact statement and hypotheses

For a modulus \(q\), write the completed trace with its \(K\)-parameter
visible as

\[
 \mathfrak T_q(u,A,B_2,V;K)
 =q\!\!\sum_{\substack{x\bmod q\\
 x,x-A,x-V,x-V-B_2\in(\mathbb Z/q\mathbb Z)^\times}}
 e_q\!\left(ux+K\Phi_{A,B_2,V}(x)\right).                               \tag{2.1}
\]

Assume \(M=8r\) with \(r\) odd.  Let \(\bar r_8r\equiv1\pmod8\) and
\(\bar8_r8\equiv1\pmod r\).  Reducing \(A,B_2,V\) modulo the two CRT
factors gives the exact factorization

\[
\begin{split}
 \mathfrak T_M(u,A,B_2,V;K)
={}&\mathfrak T_8(\bar r_8u,A_8,B_{2,8},V_8;\bar r_8K)\\
 &\times
 \mathfrak T_r(\bar8_ru,A_r,B_{2,r},V_r;\bar8_rK).                       \tag{2.2}
\end{split}
\]

When \(A_8=B_{2,8}=V_8=2\), the first factor is

\[
 \mathfrak T_8(\bar r_8u,2,2,2;\bar r_8K)
 =8c_8(\bar r_8u)=8c_8(u),                                               \tag{2.3}
\]

independently of whether \(K\) is a unit.  With
\(\kappa_q=\mathfrak T_q/q^2\), (2.2) is exactly (1.1), and

\[
 {c_8(u)\over8}=
 \begin{cases}
  +\tfrac12,&8\mid u,\\
  -\tfrac12,&u\equiv4\pmod8,\\
  0,&4\nmid u.
 \end{cases}                                                            \tag{2.4}
\]

Consequently the literal \(q=8\) part of the hard energy is the following
strict subcorrelation of the canonical coefficient:

\[
\begin{split}
 \mathscr C_8(U)={}&
 \sum_{b\asymp B}
 \sum_{\substack{\sigma\in\mathscr H_{b,U}\\
                   v_2(M)=3\\
                   A\equiv B_2\equiv V\equiv2\ (8)}}
 \sum_{\substack{0<|u|<U\\4\mid u}}(U-|u|)
 \sum_{d,n,\ell}^{\rm deep}
 {\Omega_{b,d,u}(n,\ell)\over M^3}
 e_M(dV+nA-\ell B_2)\\
 &\hspace{18mm}\times {c_8(u)\over8}
 {\mathfrak T_r(\bar8_ru,A_r,B_{2,r},V_r;\bar8_rK)\over r^2}.           \tag{2.5}
\end{split}
\]

There is no omitted power of \(8\), \(r\), or \(M\): the identity
\(M^{-5}\mathfrak T_M=M^{-3}\kappa_M\) turns the canonical normalization
directly into (2.5).  The desired package estimate would be

\[
 |\mathscr C_8(U)|
 \ll_\varepsilon X^\varepsilon {U\over B}J^{14/5}.                       \tag{2.6}
\]

Neither (2.6) nor a reverse lower bound follows from the local factor
\(|c_8(u)|/8=1/2\).

For the physical form of the same identity, set

\[
 \delta=2r\bar r_8\pmod M.
\]

Then \(\delta\equiv2\pmod8\), \(\delta\equiv0\pmod r\), and
\({\rm ord}_{\mathbb Z/M\mathbb Z}(\delta)=4\).  For an allowed odd
base \(\xi\pmod8\) and \(t\pmod r\), put
\(x_j={\rm CRT}(\xi+2j,t)\).  If

\[
 A={\rm CRT}(2,a),\quad B_2={\rm CRT}(2,\beta),\quad
 V={\rm CRT}(2,v),
\]

the four row locations for base \(x_j\) have \(2\)-adic indices
\(j,j-1,j-1,j-2\) and odd coordinates
\(t,t-a,t-v,t-v-\beta\).  Define the actual, already localized pair
sequences

\[
\begin{aligned}
 F_{j,t}&=f_{b,(\,{\rm CRT}(\xi+2j,t),
                    {\rm CRT}(\xi+2j-2,t-a)\,),U},\\
 G_{j,t}&=f_{b,(\,{\rm CRT}(\xi+2j,t-v),
                    {\rm CRT}(\xi+2j-2,t-v-\beta)\,),U}.
\end{aligned}                                                            \tag{2.7}
\]

The local base sum is, up to the sign \(c_8(u)/4\in\{+1,-1\}\),
\(\sum_jF_{j,t}\overline{G_{j-1,t}}\).  With the unnormalized transform
\(\widehat F_k=\sum_jF_j i^{-kj}\), it is exactly (1.2).  The formula
retains the two physical pairs and all four actual rows.

## 3. Proof or derivation

For CRT residues \(z_8,z_r\), the additive character satisfies

\[
 e_{8r}(z)=e_8(\bar r_8z_8)e_r(\bar8_rz_r).                              \tag{3.1}
\]

Every unit condition in (2.1), every inverse in \(\Phi\), and the base
sum factor independently under CRT.  The two local completed traces
contribute outer factors \(8\) and \(r\), whose product is the single
outer factor \(M\).  This proves (2.2), including its multiplicity and
normalization.

For an odd residue \(x\pmod8\), \(x^{-1}\equiv x\pmod8\).  Therefore,
when \(A_8=B_{2,8}=V_8=2\),

\[
 \Phi(x)\equiv x-(x-2)-(x-2)+(x-4)\equiv0\pmod8.                         \tag{3.2}
\]

The allowed bases are precisely the four odd residues.  Summing their
linear characters gives \(c_8(\bar r_8u)=c_8(u)\), because multiplication
by the odd unit \(\bar r_8\) permutes the units modulo \(8\).  This proves
(2.3)--(2.4), including independence from nonunit \(K\).

The CRT lift \(\delta\) has
\(\gcd(8r,\delta)=2r\), hence order four.  Translation by \(\delta\)
cycles the four odd \(2\)-adic bases and fixes the odd base \(t\).  The
pair \(P=(x,x-A)\) becomes the \(j,j-1\) edge, while
\(P'=(x-V,x-V-B_2)\) becomes the \(j-1,j-2\) edge.  Fourier inversion on
\(\mathbb Z/4\mathbb Z\) gives

\[
\begin{split}
 \sum_jF_j\overline{G_{j-1}}
 &={1\over16}\sum_{j,k,h}\widehat F_k\overline{\widehat G_h}
 i^{kj-h(j-1)}\\
 &={1\over4}\sum_ki^k\widehat F_k\overline{\widehat G_k},
\end{split}                                                              \tag{3.3}
\]

which proves (1.2).  If \(\beta=a\) and \(v=0\), then \(G=F\), and
taking real parts proves (1.3).  In that aligned case the two ordered
pairs agree modulo \(r\) and, since all four local entries are odd, agree
modulo \(2\).  They therefore coalesce modulo \(2r\).  The Round-89
coarse-quotient convention gives \(R_*=M/(2r)=4\), so the aligned square
is taken by \(\mathscr O_{88,c}\) once \(\rho_*>4\).  Generic hard odd
labels do not coalesce; (3.3) then contains
\(\widehat F_k\overline{\widehat G_k}\), and conjugation pairing does not
delete the \(k=1,3\) terms or make the \(k=0,2\) terms positive.

The owner placement is also exact.  In the canonical formula the
indicator \(\sigma\in\mathscr H_{b,U}\) is applied before
\(\mathfrak T_M\), and the base \(x\) is summed only inside
\(\mathfrak T_M\).  Hence a retained \(\sigma\) retains all four points
of its \(\delta\)-orbit; no point of that orbit is counted by a second
owner.  On the other hand, membership in the successive complement
depends on the full odd labels and all prime-power cells.  Some lifts
are in \(\mathscr O_{87},\mathscr O_{88,c},\mathscr O_{88,g}\), or the
certified \(\mathscr O_{89}\) cells, and only their complement occurs in
(2.5).  Thus the hard mask commutes with the local base translation for
each fixed surviving tuple, but not with a tensor-product projector that
would average over all odd CRT labels.

The compulsory exceptional cases do not repair this loss.

- The unique global owner removes only the integer \(u=0\).  Formula
  (2.5) keeps \(u\equiv4\pmod8\) and every nonzero \(u\equiv0\pmod8\).
  In particular, \(u=kM\ne0\) belongs to the \(+1/2\) local branch; it
  must not be reintroduced through a square containing \(u=0\), nor
  discarded as a local zero frequency.
- Nonunit \(K\) does not change (3.2), but it remains inside the odd
  trace in (2.5).  Odd conductor descent can enlarge rather than save
  the completed trace, so the constant \(1/2\) local factor is not a
  power gain.
- If \(v_2(M)<3\), there is no \(q=8\) factor.  If \(v_2(M)=\nu>3\),
  \(8\) and \(M/8\) are not coprime CRT factors.  One must factor the
  **full** \(2^\nu\)-part from the odd part.  Translation by \(2\) then
  has order \(2^{\nu-1}\), not four, and (3.2) modulo \(8\) does not
  determine the phase modulo \(2^\nu\).  The selected \(q=64\) control,
  where different \(V\)-lifts have different exact periods, is a direct
  warning.  Thus (2.5) is an exact nonempty \(v_2(M)=3\) package, not a
  surrogate for the full two-part.
- Every \(F,G\) in (2.7) contains the accepted \(I_b\), stationary
  support, signs, aliases, reflections, entry/exit, dyadic multiplier,
  and zero extension.  These features preserve the algebraic identity
  but can make a projected component zero.  No lower norm for any
  \(\widehat F_k\) or \(\widehat G_k\) has been proved.

Finally, conjugation closure of the hard set preserves formal
backtracking.  A fixed configuration atom has the rank-one form
\(A_c=f_c\otimes g_c^*\); pairing it with its adjoint gives
\(A_cA_c^*=\|g_c\|^2f_cf_c^*\), so the paired word survives in an
ordinary even trace.  Its fixed-vector coefficient is instead

\[
 p^*A_cq=\langle p,f_c\rangle\langle g_c,q\rangle,                        \tag{3.4}
\]

which can vanish or cancel between configurations and conductor rows.
Thus the paired projector is a valid high-trace obstruction but not an
actual-vector lower bound or upper bound.

## 4. First doubtful or unproved step

The first unproved step is any estimate of the scalar (2.5) after the
odd trace, actual pair projections, hard odd-label mask, and conductor
sum are retained.  The local identity supplies only
\(|c_8(u)|/8=1/2\), whereas the top normalized target requires a power
\(J^{-1/6}\).  There is no proved cancellation in

\[
 \sum_{b\asymp B}\sum_{\text{hard odd labels}}
 {c_8(u)\over8}\,\kappa_r(\bar8u,A_r,B_{2,r},V_r;\bar8K)
 \widehat F_{b,k}\overline{\widehat G_{b,k}}                             \tag{4.1}
\]

after the remaining \(d,u,n,\ell\) sums and weights are restored.

The first invalid simplification is to set \(G=F\) in (1.2).  The exact
label alignment that forces this identity lies in the prior coarse
owner; the generic hard lifts give a cross matrix coefficient.  Even
for a residual global translate of one pair family, the odd translation
introduces further indefinite Fourier phases and does not give a
positive quantity.  Taking absolute values in (4.1) returns the Schur
capacity, while assuming phase alignment would assert precisely the
unproved dense-plateau/global-lower-bound claim.

There is likewise no proved implication from paired mass in
\({\rm Tr}(K^*K)^s\) to \(p^*Kq\).  Equation (3.4) is the missing seam.
The conductor operator is a direct sum in \(b\); norms and trace moments
cannot create mixed-\(b\) cancellation.  Any useful conductor
cancellation must be proved in the scalar sum (4.1) before its absolute
value is taken.

The primary-source search found no theorem with the literal hypotheses.
The closest result with arbitrary fixed vectors and arbitrary composite
modulus is Blomer--Pascadi, Theorem 1.1, but its matrix is the single
Kloosterman kernel \(S(am,n;c)\) with unit \(a\), two separated interval
sequences, a fixed modulus, and a coprimality condition.  The canonical
matrix has a varying modulus, a four-pole/four-unit completed trace,
nonunit \(K\), four coupled \(I_b\)-rows, the Fejer and hard-owner masks,
and moving entry/exit.  There is no literal substitution.  Pascadi's
earlier composite-modulus theorem has the same single-kernel limitation.
Fouvry--Kowalski--Michel is a prime-field bounded-conductor sheaf theorem;
its normal-tuple hypothesis explicitly excludes the paired \(h=0\)
words, for which it instead produces a main term.  Lin--Michel's
composite trace-function theorems require a prime CRT factor, prescribed
sheaf tensors and smooth automorphic coefficients, not this fixed
four-row physical symbol.  Consequently no external theorem can be
imported into (2.6).

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| Literal fixed actual vector | **Pass as preservation; estimate open.** Equation (2.5) retains \(\Omega_{b,d,u}=I_b(n+d+u)\overline{I_b(n)}\overline{I_b(\ell+d)}I_b(\ell)\). No arbitrary coefficients replace it, but no nonzero or \(J^{-1/6}\)-small projection is proved. |
| CRT normalization and lift multiplicity | **Pass for \(v_2(M)=3\).** Equations (2.2)--(2.5) include the additive-character inverses, the four local bases, both outer completion factors, and \(M^{-5}\mathfrak T_M=M^{-3}\kappa_M\). |
| \(q=8\) as a local factor | **Pass only on the exact \(M=8r\), \(r\) odd subfamily.** It is false as a coprime factor when \(v_2(M)>3\), and absent when \(v_2(M)<3\). |
| Unique \(u=0\) owner | **Pass.** The integer \(u=0\) is absent from (2.5). No positive square is used to restore it. |
| Nonzero \(u=4\) and modulus multiples | **Pass.** The \(-1/2\) branch is \(u\equiv4\pmod8\); the \(+1/2\) branch contains all nonzero \(8\mid u\), including \(u=kM\ne0\). These branches are not conflated. |
| All four rows and both physical pairs | **Pass algebraically.** The four locations \(j,j-1,j-1,j-2\) and odd labels \(t,t-a,t-v,t-v-\beta\) appear in (2.7). This proves formal four-row coupling, not nonvanishing. |
| Hard-owner one-count | **Pass with a fragmentation warning.** A surviving tuple retains its whole local orbit because the hard indicator is outside the base sum. The \(q=8\) congruence alone does not certify hard membership; all prior owners are intersected first. |
| Aligned autocorrelation | **Fail as a hard package.** The forced \(F=G\) slice has \(R_*=4\le\rho_*\) and is already in the Round-88 coarse owner. Generic hard lifts obey the cross formula (1.2). |
| Paired/backtracking cycles | **Pass as a norm obstruction only.** Conjugation closure retains adjoint pairs and positive backtracking words, but (3.4) leaves the actual-vector projection uncontrolled. |
| Nonunit \(K\) | **Pass locally; no saving.** The \(8\)-part is independent of \(K\), including nonunits. The odd nonunit trace remains literal and can be degenerate. |
| Full two-part | **Fail for any extrapolation from \(8\).** Higher \(2^\nu\) factors require their complete lift; a mod-\(8\) quotient does not factor or classify them. |
| Entry/exit, aliases, stars and zero extension | **Pass as retention; lower bound fails.** They remain inside \(I_b\) and the pair functions and may annihilate a projected mode. |
| Conductor summation | **Pass as typing.** The modulus is taken only after the scalar sum over \(b\); a direct-sum norm supplies no conductor cancellation, and local signs supply no lower bound across \(b\). |
| Local trace versus global projection | **Fail for the proposed inference.** The local normalized eigenvalue \(1/2\) is a constant factor. Odd traces, actual row projections and hard cells can cancel. |
| Dense plateau/global lower bound | **Conditional only.** No positive proportion of complete hard entries or noncancelling archimedean projection has been proved. |
| Source-hypothesis map | **Fail literally.** The audited theorems cover a single Kloosterman matrix, a prime-field bountiful sheaf, or a prescribed composite trace tensor; none accepts (2.5). |
| Downstream and exponent scope | **Pass.** No full canonical estimate, GAR, blockwise M9-M1, M9-M2, endpoint uniformity, M9, or exponent is inferred. |

No numerical experiment was used.  Every positive statement above is an
exact CRT, finite Fourier, owner-placement, or rank-one identity.

## 6. Dependencies and exact artifacts used

Only the campaign-selected repository context was used:

- protocol.md;
- state/proof_obligations.yml (the three selected Round-100 obligations and relevant rejected controls);
- state/active_campaign.yml;
- rounds/codex-managed/m9-m1-actual-vector-coherent-mode-projection/derivation_packet.md;
- rounds/codex-managed/m9-canonical-core-formalization/candidates/conductor_canonical_core_statements.md;
- rounds/codex-managed/m9-m1-bad-prime-period-fibre-energy/reports/bad_prime_hostile_source_audit.md;
- rounds/codex-managed/m9-m1-joint-four-row-spectral-gap/reports/joint_gram_source_hostile_audit.md;
- strategy/conductor_0817_full_proof_strategy.md.

The following primary sources were checked against the literal fixed-vector
and composite-trace hypotheses:

- Valentin Blomer and Alexandru Pascadi, [*Bilinear forms with Kloosterman sums via quadratic characters*](https://arxiv.org/html/2607.24311), Theorem 1.1.  It permits arbitrary complex coefficient vectors and all integer moduli, but only for the single kernel \(S(am,n;c)\), unit \(a\), interval supports and its stated coprimality convention.
- Alexandru Pascadi, [*Non-abelian amplification and bilinear forms with Kloosterman sums*](https://arxiv.org/html/2511.08445), Theorems 1.1--1.2.  It is likewise a fixed-modulus, single-Kloosterman-matrix operator theorem.  Its discussion of other Möbius kernels and joint Kloosterman--archimedean bounds is explicitly prospective, not a theorem.
- Étienne Fouvry, Emmanuel Kowalski and Philippe Michel, [*A study in sums of products*](https://arxiv.org/html/1405.2293v2), Theorem 1.5 and Corollaries 1.6--1.7.  It assumes a prime field and a bounded-conductor bountiful sheaf; paired/non-normal zero-twist tuples carry a main term rather than square-root cancellation.
- Yongxiao Lin and Philippe Michel, [*On algebraic twists with composite moduli*](https://arxiv.org/abs/2304.08149) and [*On algebraic twists with composite moduli, II*](https://arxiv.org/abs/2605.06363).  Their modulus has a designated coprime prime factor and their trace functions are prescribed sheaf tensors against smooth automorphic coefficients.  They do not accept the full powerful two-part, nonunit four-pole trace, hard mask, or four coupled stationary rows in (2.5).

No source states a fixed-vector estimate for the literal moving composite
trace (2.5), and no source card is recommended for import.

## 7. Recommended state effect

**Retain the directional estimate and the full canonical hard estimate as
open.**  Record (2.2)--(2.5) as an exact local CRT and one-count reduction
on the nonempty \(v_2(M)=3\) hard subfamily.  It isolates the strictly
smaller scalar \(\mathscr C_8(U)\) without claiming its target bound.

**Reject the difference-of-squares argument as a hard-owner mechanism.**
The identity (1.3) is correct, but its structurally aligned odd lift has
\(R_*=4\) and is already coarse-owned.  The literal generic hard object is
the cross-projection (1.2), with the odd trace and actual row symbols still
attached.  Also reject treating a mod-\(8\) quotient as the full
\(2\)-adic factor, deleting nonzero local-zero or modulus-multiple shifts,
or converting paired trace mass into a fixed-vector coefficient.

**Retain the local coherent mode and paired words as controls, not lower
bounds.**  The hard mask preserves each surviving four-cycle and
conjugation preserves backtracking, but the odd-label mask, entry/exit,
and conductor scalar sum leave their actual-vector coupling unproved.
Dense-plateau and global-lower-bound claims remain conditional.

**Do not import an external theorem.**  The strongest composite-modulus
fixed-vector sources found concern a single Kloosterman matrix and fail
the literal kernel, owner, nonunit, full-two-part, and conductor-sum
hypotheses.  Make no change to the unique \(u=0\) owner, the Round-87--89
owners, GAR, M9-M1, M9-M2, endpoint uniformity, M9, or any exponent.
