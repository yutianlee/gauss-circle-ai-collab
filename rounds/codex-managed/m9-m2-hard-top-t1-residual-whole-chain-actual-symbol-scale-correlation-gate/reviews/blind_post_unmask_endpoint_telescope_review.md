# Round 175 blind post-unmask endpoint-telescope review

- Campaign: m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate
- Round: 175
- Role: post-unmask seam reviewer
- Starting graph: e40c214351d06bf05212e25fffbec0f1a4808be21cb9098ba25823f0d9bbf211
- Reviewed candidate: formalized_whole_chain_scale_telescope_obstruction.md
- Evidence status: independent review; no shared-state mutation

## 1. Verdict

**Verdict: REVISE, then retain only as a route-scoped obstruction.**

The endpoint-collapse conclusion is correct. Equations (175.C3)--(175.C7),
(175.C9)--(175.C11), and (175.C14)--(175.C15) have the correct constants
and signs once their implicit physical and ordinary-zero definitions are
made explicit. The possible strict terminal link is handled correctly.

There is one blocking displayed defect: (175.C8) is missing the plus sign
before its interior summation-by-parts term. As printed, it is not an
identity. Four precision repairs are also needed: display the physical
polynomial in (175.C3); define the collective zero-containing sector in
(175.C12); define \(B_{\mathrm{short}}\) and identify \(T_{26}\) exactly with
(165.K26); and state the lower-endpoint estimate

\[
 Q_{R_0}^*\ll_\varepsilon L^3X^\varepsilon.
\tag{175.V0}
\]

Because \(Q_{R_0}^*\ge0\), (175.V0) makes the frozen chain estimate
equivalent at target strength to

\[
 Q_M^*\ll_\varepsilon L^3X^\varepsilon.
\tag{175.V0a}
\]

The \(L^4\) calculation (175.C18)--(175.C20) is exact for the complete
physical parity-Fejer energy. It is not, without an additional realization
argument, an \(L^4\) lower bound for the isolated nonzero transformed
energy \(Q_M^*\). The candidate should state this distinction explicitly.

## 2. Exact audited statement and line verdicts

Put

\[
 A_{\epsilon,*}(\theta)
 :=\sum_{k\ {\mathrm{odd}}}\chi_4(k)
   \sum_{\ell\ne0}U_{k,\ell}^{(\epsilon)}(\theta),
 \qquad
 A_{\epsilon,0}(\theta)
 :=\sum_{k\ {\mathrm{odd}}}\chi_4(k)U_{k,0}^{(\epsilon)}(\theta).
\tag{175.V1}
\]

The exact transform identity needed in (175.C3) is

\[
\boxed{
 Z_\epsilon(\theta)
 :=\sum_N(-1)^{\epsilon N}z_Ne(N\theta)
 ={i\over2}\{A_{\epsilon,0}(\theta)+A_{\epsilon,*}(\theta)\}
 =Z_{\epsilon,0}(\theta)+Z_{\epsilon,*}(\theta).}
\tag{175.V2}
\]

The line verdicts are:

| Candidate equation | Verdict | Seam finding |
|---|---|---|
| (175.C3) | Correct constant; incomplete display | The sign \(+i/2\) is correct. Add the physical polynomial equality (175.V2), needed for Parseval and physical gaps. |
| (175.C4) | Pass | Zero and nonzero ordinary modes are split after full odd-character recombination. |
| (175.C5) | Pass | \(Q_R^*\ge0\) because \(F_R\ge0\). |
| (175.C6) | Pass | \(|i/2|^2=1/4\), followed by the parity factor \(1/2\), gives \(1/8\). |
| (175.C7) | Pass | The unweighted finite chain telescopes exactly. |
| (175.C8) | Fail as printed | Insert \(+\) before \(\sum_{j=1}^{K-1}(a_{j-1}-a_j)Q_{R_j}^*\). |
| (175.C9)--(175.C10) | Pass with stated scope | These are integer physical-gap coefficients after physical recombination, not weights of a fixed transformed tuple. |
| (175.C11) | Pass | This is the accepted absolute-site-parity energy. |
| (175.C12) | Correct idea; underdefined | Define \(\mathcal Z_{R,S}\) by (175.V9) below. |
| (175.C13) | Pass after that definition | The collective sector telescopes and its one endpoint is target-safe. |
| (175.C14) | Pass; underdefined | Restore the definitions in (175.V14) and state that \(T_{26}\) is exactly (165.K26). |
| (175.C15) | Pass | The sign and factor \(2\) are correct. |

If \(M=2R_{K-1}\), the final link is a doubling. It is strict only if
\(R_{K-1}<M<2R_{K-1}\). No audited equation assumes otherwise.

## 3. Independent derivation

### 3.1 Constants and factorization

With \(e(t)=e^{2\pi it}\),

\[
\begin{aligned}
 \sum_{k\ {\mathrm{odd}}}\chi_4(k)e(-kx/4)
 &=\{e(-x/4)-e(-3x/4)\}\sum_{a\in\mathbb Z}e(-ax)\\
 &=-2i\sum_{d\ {\mathrm{odd}}}\chi_4(d)\delta(x-d).
\end{aligned}
\tag{175.V3}
\]

Ordinary Poisson in \(y\), the disjoint cardinal cells, and
\(\varphi(0)=1\) sample the literal coefficient. Since \(d\) is odd,
\(m=N/d\) and \(N\) have the same parity. Multiplication by \(i/2\)
therefore proves (175.V2), including its sign.

Since \(Z_{\epsilon,*}=(i/2)A_{\epsilon,*}\),

\[
\begin{aligned}
 Q_S^*-Q_R^*
 &={1\over2}\sum_{\epsilon=0}^1\int_0^1
 B_{R,S}|Z_{\epsilon,*}|^2\,d\theta\\
 &={1\over8}\sum_{\epsilon=0}^1\int_0^1
 B_{R,S}|A_{\epsilon,*}|^2\,d\theta\\
 &=\mathcal N_{R,S}.
\end{aligned}
\tag{175.V4}
\]

The last equality expands the square into all
\(k,k'\) odd and \(\ell,\ell'\ne0\), with one outer real part. Thus
(175.C6) is exact. The prose should say that \(|i/2|^2=1/4\) and the
parity average gives the total \(1/8\), rather than calling \(1/8\) the
“squared constant.”

### 3.2 Unweighted and weighted scale Abel

Writing \(Q_j=Q_{R_j}^*\),

\[
 \sum_{j=0}^{K-1}(Q_{j+1}-Q_j)=Q_M^*-Q_{R_0}^*.
\tag{175.V5}
\]

For arbitrary scalars \(a_j\), the corrected identity is

\[
\boxed{
 \sum_{j=0}^{K-1}a_j\mathcal N_{R_j,R_{j+1}}
 =a_{K-1}Q_M^*-a_0Q_{R_0}^*
 +\sum_{j=1}^{K-1}(a_{j-1}-a_j)Q_{R_j}^*.}
\tag{175.V6}
\]

The plus sign before the interior sum is mandatory. Setting \(a_j=1\)
recovers (175.C7); any nonconstant weighting changes the frozen target
and introduces intermediate endpoint energies.

From (175.C16)--(175.C17),

\[
 Q_{R_0}^*
 \ll_\varepsilon R_0L^2X^\varepsilon
 \ll_\varepsilon L^3X^\varepsilon.
\tag{175.V7}
\]

Hence

\[
 Q_M^*-Q_{R_0}^*\ll_\varepsilon L^3X^\varepsilon
 \quad\Longleftrightarrow\quad
 Q_M^*\ll_\varepsilon L^3X^\varepsilon.
\tag{175.V8}
\]

For the forward implication use
\(Q_M^*=(Q_M^*-Q_{R_0}^*)+Q_{R_0}^*\) and (175.V7). For the reverse
implication use \(Q_{R_0}^*\ge0\). This endpoint equivalence is absent
from the candidate and should be added.

The derivation uses only \(R_K=M\), so it retains either the exact final
doubling or the possible strict terminal link.

### 3.3 Physical gaps versus fixed transformed tuples

Let \(f_R(r)=(1-|r|/R)_+\). For an integer physical gap,

\[
 f_S(r)-f_R(r)=
 \begin{cases}
 |r|(R^{-1}-S^{-1}),&0<|r|<R,\\
 1-|r|/S,&R\le |r|<S,\\
 0,&r=0\ {\mathrm{or}}\ |r|\ge S.
 \end{cases}
\tag{175.V8a}
\]

These nonnegative coefficients sum to (175.C10).

For a fixed transformed tuple
\(\alpha=(\epsilon,k,k',\ell,\ell')\), the only exact assertion is

\[
\begin{aligned}
 &\sum_{j=0}^{K-1}{1\over8}\Re\int_0^1
 B_{R_j,R_{j+1}}\chi_4(k)\chi_4(k')
 U_{k,\ell}^{(\epsilon)}
 \overline{U_{k',\ell'}^{(\epsilon)}}\,d\theta\\
 &\quad={1\over8}\Re\int_0^1
 (F_M-F_{R_0})\chi_4(k)\chi_4(k')
 U_{k,\ell}^{(\epsilon)}
 \overline{U_{k',\ell'}^{(\epsilon)}}\,d\theta .
\end{aligned}
\tag{175.V8b}
\]

No sign, vanishing, or \(\beta\ge1/2\) statement for that transformed
tuple follows. The candidate's distinction after (175.C10) is correct.

### 3.4 Collective ordinary-zero restoration

The missing exact definition is

\[
\boxed{
 \mathcal Z_{R,S}:={1\over2}\sum_{\epsilon=0}^1\int_0^1
 B_{R,S}
 \left\{|Z_{\epsilon,0}|^2+
 2\Re(Z_{\epsilon,0}\overline{Z_{\epsilon,*}})\right\}\,d\theta .}
\tag{175.V9}
\]

This counts the \((0,0)\), \((0,*)\), and \((*,0)\) pieces once, after
all odd-character frequencies are recombined. Expanding
\(|Z_{\epsilon,0}+Z_{\epsilon,*}|^2\) proves (175.C12). Define
\(\mathcal Z_{R_0,M}\) by the same formula with
\(B_{R_0,M}=F_M-F_{R_0}\); this is an endpoint kernel, not an adjacent
link. Then

\[
 \sum_j\mathcal Z_{R_j,R_{j+1}}=\mathcal Z_{R_0,M}.
\tag{175.V10}
\]

Using

\[
 |Z_{\epsilon,0}|^2+
 2\Re(Z_{\epsilon,0}\overline{Z_{\epsilon,*}})
 =2\Re(Z_{\epsilon,0}\overline{Z_\epsilon})
 -|Z_{\epsilon,0}|^2
\]

and the accepted estimates

\[
 \|F_M-F_{R_0}\|_\infty\le M+R_0,\quad
 \|Z_\epsilon\|_2=D_L^{1/2},\quad
 \|Z_{\epsilon,0}\|_2\le
 \|Z_{\epsilon,0}\|_\infty
 \ll_\eta {L^2\over J}X^\eta,
\]

one gets

\[
 |\mathcal Z_{R_0,M}|
 \ll (M+R_0)
 \left(D_L^{1/2}{L^2\over J}+{L^4\over J^2}\right)X^{O(\eta)}
 \ll_\varepsilon L^3X^\varepsilon.
\tag{175.V11}
\]

This validates (175.C13) collectively and gives no termwise zero-mode
estimate.

### 3.5 Once-only short correction and K26

Let

\[
 A_r:=\Re\sum_Nz_{N+r}\overline{z_N}.
\tag{175.V12}
\]

The accepted parity identity gives

\[
 \mathfrak E_R^{(2)}
 =D_L+2\sum_{\substack{0<r<R\\2\mid r}}
 \left(1-{r\over R}\right)A_r.
\tag{175.V13}
\]

Thus

\[
\begin{aligned}
 B_{\mathrm{short}}
 &:=\sum_{\substack{0<r<R_0\\2\mid r}}
 r\left({1\over R_0}-{1\over M}\right)A_r,\\
 T_{26}
 &:=\sum_{\substack{R_0\le r<M\\2\mid r}}
 \left(1-{r\over M}\right)A_r\\
 &={1\over2}\{\mathfrak E_M^{(2)}
 -\mathfrak E_{R_0}^{(2)}\}-B_{\mathrm{short}}.
\end{aligned}
\tag{175.V14}
\]

This \(T_{26}\) is exactly the left side of (165.K26), with \(M=M_L\).
Also
\(|B_{\mathrm{short}}|\le R_0D_L\ll_\varepsilon L^3X^\varepsilon\).
It is paid once.

From (175.C12) and (175.V10),

\[
 \mathfrak E_M^{(2)}-\mathfrak E_{R_0}^{(2)}
 =\sum_j\mathcal N_{R_j,R_{j+1}}+\mathcal Z_{R_0,M}.
\tag{175.V15}
\]

Combining (175.V14)--(175.V15) gives (175.C15) exactly:

\[
 \sum_j\mathcal N_{R_j,R_{j+1}}
 =2(T_{26}+B_{\mathrm{short}})-\mathcal Z_{R_0,M}
 =2T_{26}+O_\varepsilon(L^3X^\varepsilon).
\tag{175.V16}
\]

Therefore the Round-175 target and (165.K26) are equivalent as one-sided
upper bounds at target strength. This proves neither estimate.

## 4. Defects, precise repairs, and first doubtful step

1. **Blocking equation defect:** replace (175.C8) by (175.V6). The missing
   operator is \(+\), and the interior coefficient is
   \(a_{j-1}-a_j\).

2. **Physical-transform seam:** replace (175.C3) by (175.V2). Replace the
   normalization prose before (175.C6) by
   “\(|i/2|^2=1/4\), and the parity average gives \(1/8\).”

3. **Ordinary-zero ownership:** insert (175.V9), and define the endpoint
   notation \(\mathcal Z_{R_0,M}\) explicitly. This prevents double
   counting or an illicit termwise use of the zero-mode estimate.

4. **K26 ownership:** insert (175.V12)--(175.V14), or cite
   (172.K5)--(172.K6) and (165.K26) at (175.C14). Say “equivalent
   one-sided upper bounds,” not merely “equivalent.”

5. **Lower endpoint:** add (175.V7)--(175.V8). This confirms, rather than
   rejects, the other reviews' point: the chain target is equivalent to
   \(Q_M^*\ll L^3X^\varepsilon\).

6. **Diagnostic scope:** after (175.C20), say explicitly that the example
   is a positive translate and diagnoses the complete physical
   \(\mathfrak E^{(2)}\), not an \(L^4\) lower bound for the literal
   \(Q^*\) sector.

After these repairs, no further defect was found in (175.C3)--(175.C15).
The first genuinely unproved step toward the target is the literal-symbol
upper-endpoint estimate (175.V0a), equivalently K26 modulo the complete
target-safe seams.

## 5. Controls and outcomes

1. **Constants and parity:** (175.V3)--(175.V4) confirm \(+i/2\),
   \(|i/2|^2/2=1/8\), both parity branches, and one outer real part. Pass.
2. **Nonzero factorization:** the square is formed only after all signed
   odd-character and nonzero ordinary-frequency sums. Pass.
3. **Weighted scale Abel:** correct only after inserting the missing plus.
   Repair required.
4. **Physical versus transformed diagonal:** (175.V8a) and (175.V8b) are
   distinct. Pass.
5. **Terminal link:** exact doubling and possible strict terminal link are
   both retained. Pass.
6. **Collective ordinary zero:** (175.V9)--(175.V11) restores the sector
   once and collectively. Pass after definition repair.
7. **Short correction:** (175.V14) pays it once and at target scale. Pass.
8. **K26 strength:** (175.V16) verifies the sign, factor \(2\), and
   one-sided equivalence. Pass.
9. **Lower endpoint:** \(Q_{R_0}^*\ll R_0L^2X^\varepsilon\ll
   L^3X^\varepsilon\), so (175.V8) holds. Pass.
10. **Exact \(L^4\) diagnostic:** for \(L=2n\), \(P=n^2\),
    \(M=4P=L^2\), and \(z_N=1\) on the \(2P\) even sites of a positive
    \(M\)-site interval,

    \[
    \mathfrak E_M^{(2)}
    =2P+{1\over P}\sum_{t=1}^{2P-1}t^2
    ={8P^2+1\over3}.
    \]

    Since \(R_0D=4n^3\),

    \[
    \mathfrak E_M^{(2)}-\mathfrak E_{R_0}^{(2)}
    -{L^4\over12}
    ={4\over3}n^3(n-3)+{1\over3}\ge0.
    \]

    With \(X=L^8\), \(J=L^4\), and \(H=L^2\), the parameter range is
    admissible, and \(L^4/(L^3X^{\varepsilon_0})
    =L^{1-8\varepsilon_0}\to\infty\) for
    \(0<\varepsilon_0<1/8\). The arithmetic is exact. Pass with the
    physical-versus-\(Q^*\) scope restriction.

No numerical experiment or external theorem was used.

## 6. Dependencies and exact artifacts used

The review used only:

1. protocol.md;
2. state/proof_obligations.yml, for the active accepted statuses and scope;
3. state/active_campaign.yml;
4. strategy/round175_m2_hard_top_t1_residual_whole_chain_actual_symbol_strategy.md;
5. proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md;
6. proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md;
7. proofs/kernels/m9_m2_hard_top_t1_residual_maximal_fejer_dyadic_positive_transform_obstruction.md; and
8. rounds/codex-managed/m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate/candidates/formalized_whole_chain_scale_telescope_obstruction.md.

No Round-175 sibling report or review, shared synthesis, proof draft, source
card, web source, or numerical output was used.

## 7. Recommended state effect and scope

Do not promote the candidate verbatim. Apply the six repairs in Section 4,
then retain it under the terminal label

\[
 \texttt{whole\_chain\_actual\_symbol\_capacity\_or\_self\_return\_no\_go}.
\]

The durable conclusion is only that the unweighted nonzero stopped chain
is the endpoint difference \(Q_M^*-Q_{R_0}^*\), its lower endpoint is
already target-safe, scalar scale reweighting creates no independent
factor-\(L\) resource, and the complete target is still exactly K26
modulo the collective zero-containing sector and the once-only short
correction.

This is an obstruction with no implication edge. K26, \(Q_M^*\), and the
complete residual scalar remain open. There is no conclusion for full
\(t=1\), another hard-TOP channel, complete hard TOP, BAL, UNBAL,
M9--M2, either M1 route, endpoint uniformity, M9, a bridge, the quarter
theorem, or an exponent.

