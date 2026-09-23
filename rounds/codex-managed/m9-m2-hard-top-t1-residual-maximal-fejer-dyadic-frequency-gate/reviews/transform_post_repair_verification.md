# Round 172 post-repair transform verification

Campaign: m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate  
Role: post-repair independent verification  
Verdict: **GREEN**

## 1. Result

The repaired discovery and hostile reports now agree at every assigned
transform seam.  Equations (172.D13)--(172.D15) are the exact literal
common-frequency transform with constants \(i/2\) and \(1/8\);
(172.D18)--(172.D20) pay the ordinary-zero sector only after its complete
signed character-frequency recombination; (172.D23) is correctly identified
as the first open analytic seam; and the repaired in-range control
(172.H15) attains \(MD_L/8\asymp L^4\).

No further repair is required in the assigned scope.

## 2. Exact statement and hypotheses

For the finite residual opening

\[
 c_N^{\rm rem}=\sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)\lambda_N(d),\qquad N=dm,
\]

take a cardinal bump
\(\varphi\in C_c^\infty((-1/2,1/2))\), \(\varphi(0)=1\), and form
\(\mathcal B_{\epsilon,\theta}\) as in (172.D13).  Then

\[
 Z_\epsilon(\theta)=\frac i2
 \sum_{k\ {\rm odd}}\chi_4(k)\sum_{\ell\in\mathbb Z}
 \widetilde{\mathcal B}_{\epsilon,\theta}(k/4,\ell),
\]

and the parity-averaged bandpass square has coefficient \(1/8\), exactly
as in (172.D15).

## 3. Verification

The support of \(\varphi\) makes the interpolation exact at every integer
pair, and the physical map \((d,m)\mapsto N=dm\) counts each ordered
divisor incidence once.  Since \(d\) is odd,
\((-1)^{\epsilon N}=(-1)^{\epsilon m}\), so both product parities remain.

With \(\widehat f(\xi)=\int f(x)e(-\xi x)\,dx\),

\[
 \sum_n\chi_4(n)f(n)
 =\frac i2\sum_{k\ {\rm odd}}\chi_4(k)\widehat f(k/4).
\]

Ordinary Poisson in the second variable introduces no additional
constant.  Squaring contributes \(1/4\), and the two-peak parity average
contributes \(1/2\), proving the \(1/8\) in (172.D15).

For the ordinary zero mode, the full signed sum over odd \(k\) recombines
to

\[
 Z_{\epsilon,0}(\theta)
 =\sum_d\chi_4(d)\int\mathcal B_{\epsilon,\theta}(d,y)\,dy.
\]

Cellwise integration by parts gives
\(\|Z_{\epsilon,0}\|_\infty\ll_\varepsilon L^2J^{-1}X^\varepsilon\).
Consequently the **combined** contribution with
\(\ell=0\) or \(\ell'=0\) is

\[
 \ll_\varepsilon (U+V)
 \left(D_L^{1/2}\frac{L^2}{J}+\frac{L^4}{J^2}\right)X^\varepsilon
 \ll_\varepsilon L^3X^\varepsilon.
\]

This is not a fixed-\(k\), \(\ell^1_k\), or positive \(k\)-square bound.
The repaired hostile report states this scope explicitly.

Finally, for \(M=4P\) and \(z_N=1\) on the \(2P\) sites of one absolute
parity class in an \(M\)-site interval,

\[
 D_L=2P,\qquad
 \Delta_{2P,4P}=P^2=\frac{MD_L}{8}.
\]

Thus (172.H15) is support-compatible, lies on the legitimate maximal
doubling link, and sharply restores the \(L^4\) coefficient-uniform
capacity.

## 4. First remaining doubt

The first remaining unproved statement is precisely (172.D23): the one-real-
part, fully signed aggregate over
\(k,k'\) odd and \(\ell,\ell'\ne0\), with both Fejer peaks, all cross terms,
selectors, endpoints, and transition cells retained before positivity.

No dual diagonal may be deleted.  Taking a modulus or positive norm before
proving (172.D23) returns \((U+V)D_L\asymp L^4X^\varepsilon\).

## 5. Control outcomes

| Seam | Outcome |
|---|---|
| Character-Poisson constant \(i/2\) | **PASS** |
| Ordinary-Poisson normalization | **PASS** |
| Squared parity-bandpass constant \(1/8\) | **PASS** |
| Collective ordinary-zero interpretation | **PASS** |
| Ordinary-zero restored power | **PASS** at \(L^3X^\varepsilon\) |
| First-open seam (172.D23) | **PASS** |
| In-range dechirped control (172.H15) | **PASS**, exactly \(MD_L/8\) |
| Scope of the positive-transform no-go | **PASS**: coefficient-uniform only |

## 6. Dependencies

This verification used only the repaired discovery report, the repaired
hostile report, and
reviews/literal_common_frequency_transform_review.md in this campaign.
No state, synthesis, proof-draft, web, or computational artifact was used.

## 7. Recommended state effect

Treat the repaired transform, collective ordinary-zero estimate, and
in-range \(L^4\) control as GREEN candidate evidence.  Retain (172.D23),
(165.K26), and the residual scalar as open.  The supported route label
remains maximal_fejer_dyadic_character_poisson_no_go, scoped to exact
transform followed by coefficient-uniform positive dual/cell control.
