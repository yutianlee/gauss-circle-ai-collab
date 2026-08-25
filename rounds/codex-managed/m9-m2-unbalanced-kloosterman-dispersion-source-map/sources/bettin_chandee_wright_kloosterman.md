# Bettin--Chandee and Wright Kloosterman-fraction source card

Round: 135

Audit date: 2026-08-23

Scope: exact primary-source statements used to test the flat-smooth M2
strict-UNBAL prescribed-centre wave. This card certifies source text and
hypothesis matching; it does not certify the open quarter estimate.

## 1. Primary versions

1. Sandro Bettin and Vorrapan Chandee, *Trilinear forms with Kloosterman
   fractions*, arXiv:1502.00769v1, submitted 3 February 2015:
   <https://arxiv.org/html/1502.00769v1>.
2. Thomas Wright, *Trilinear Kloosterman fractions I: partially fixed
   moduli and unbalanced convolutions*, arXiv:2604.25177v2, revised
   7 August 2026: <https://arxiv.org/html/2604.25177v2>.
3. arXiv:2601.00292v2 is withdrawn and records a missing (L^2) factor:
   <https://arxiv.org/abs/2601.00292>. It is a negative bibliographic
   control and supplies no theorem.

## 2. Bettin--Chandee Theorem 1 and Remark 1

For arbitrary complex sequences on the integer points of

\[
 \mathcal A=[A/2,A],\qquad \mathcal M=[M/2,M],\qquad
 \mathcal N=[N/2,N],
\]

the source defines

\[
 \mathcal B(M,N,A)=
 \sum_{\substack{a\in\mathcal A,\,m\in\mathcal M,\,n\in\mathcal N\\
                  (m,n)=1}}
 \alpha_m\beta_n\nu_a
 e\!\left(\vartheta\frac{a\overline m}{n}\right).
\tag{S2.1}
\]

Theorem 1 states

\[
\begin{aligned}
 |\mathcal B(M,N,A)|
 &\ll \|\alpha\|_2\|\beta\|_2\|\nu\|_2
 \left(1+\frac{|\vartheta|A}{MN}\right)^{1/2}\\
 &\quad\times\left(
 (AMN)^{7/20+\varepsilon}(M+N)^{1/4}
 +(AMN)^{3/8+\varepsilon}(AN+AM)^{1/8}
 \right).
\end{aligned}
\tag{S2.2}
\]

There is no printed relative-size condition on (A,M,N). The absolute
value surrounds the complete signed trilinear form. The printed theorem
only says (\vartheta\ne0), but the proof uses gcds with (\vartheta) and
primes coprime to it; Wright v2 also restates this parameter as a nonzero
integer. The source-safe import is therefore
(\vartheta\in\mathbb Z\setminus\{0\}).

Remark 1 permits an added (C^1) real phase (f_{a,\vartheta}(x,y)) when

\[
 |\partial_xf|\ll \frac{Y}{x^2y},\qquad
 |\partial_yf|\ll \frac{Y}{xy^2},
\tag{S2.3}
\]

on (x\in\mathcal N,y\in\mathcal M). The factor in (S2.2) is then
replaced by

\[
 \left(1+\frac{|\vartheta|A+Y}{MN}\right)^{1/2}.
\tag{S2.4}
\]

The source contains harmless (x,y) and (\theta,\vartheta) notation
inconsistencies; the derivative and frequency requirements above are the
audited content.

## 3. Bettin--Chandee Corollary 1

For fixed nonzero integer determinant (\Delta_{\rm det}), four dyadic
supports, arbitrary (\alpha_{n_1},\beta_{n_2}), and smooth (f,g) with

\[
 f^{(j)}\ll\eta^jM_1^{-j},\qquad
 g^{(j)}\ll\eta^jM_2^{-j},
\]

the source studies

\[
 \mathcal T=
 \sum_{m_1n_2-m_2n_1=\Delta_{\rm det}}
 f(m_1)g(m_2)\alpha_{n_1}\beta_{n_2}.
\tag{S3.1}
\]

Its main term is

\[
 \sum_{(n_1,n_2)\mid\Delta_{\rm det}}
 \frac{(n_1,n_2)}{n_1n_2}\alpha_{n_1}\beta_{n_2}
 \int_{\mathbb R}
 f\!\left(\frac{x+\Delta_{\rm det}}{n_2}\right)
 g\!\left(\frac{x}{n_1}\right)\,dx,
\tag{S3.2}
\]

and its error is

\[
 O\!\left((\eta\mathcal A)^{3/2}\|\alpha\|_2\|\beta\|_2
 (N_1N_2)^{7/20}(N_1+N_2)^{1/4+\varepsilon}
 (M_1M_2)^\varepsilon\right),
\tag{S3.3}
\]

where

\[
 \mathcal A=\frac{M_1N_2}{M_2N_1}
 +\frac{M_2N_1}{M_1N_2}.
\tag{S3.4}
\]

No average over determinant levels is included in the corollary.

## 4. Wright Theorem 2.1

To avoid collisions, write (A_0,M_0,N_0) for source lengths and
\(R_0\) for the fixed denominator factor. Wright considers

\[
 \mathcal B(M_0,N_0,A_0;R_0)=
 \sum_{\substack{a\sim A_0,\,m\sim M_0,\,n\sim N_0\\
                  (m,nR_0)=1}}
 \alpha_m\beta_n\nu_a
 e\!\left(\vartheta\frac{a\overline m}{nR_0}\right),
\tag{S4.1}
\]

with arbitrary complex sequences and integral
(\vartheta\ne0). If (M_0\ll N_0^2) and (R_0\ll M_0^C) for a fixed
polynomial-growth exponent (C), Theorem 2.1 prints

\[
\begin{aligned}
 |\mathcal B|
 &\ll M_0^\varepsilon\|\alpha\|_2\|\beta\|_2\|\nu\|_2
 (A_0M_0N_0)^{1/2}R_0^{1/4}
 \left(1+\frac{|\vartheta|A_0}{M_0N_0}\right)^{1/4}\\
 &\quad\times\left(
 N_0^{-1/8}
 +\frac{R_0^{1/8}N_0^{1/8}}{M_0^{1/4}}
 +\frac{M_0^{1/10}}{R_0^{3/20}A_0^{1/20}N_0^{3/20}}
 +\frac{N_0^{3/20}}{A_0^{3/20}M_0^{1/5}}
 +\frac{N_0^{3/8}}{M_0^{1/2}}
 \right).
\end{aligned}
\tag{S4.2}
\]

The last displayed proof bound has (A_0^{-3/10}), rather than the
printed (A_0^{-1/20}), in the third term. This card uses the weaker
printed theorem. The decisive fifth term agrees in the statement and proof.
There is no printed analogue of Bettin--Chandee Remark 1.

## 5. Wright dispersion corollary

Corollary 2.2 bounds a sum over (q\sim Q) of the individual absolute
discrepancies for (mn\equiv a\pmod q), after subtracting the
reduced-residue principal term. It requires a fixed nonzero integer residue
with ((a,q)=1), divisor-bounded coefficients, a Siegel--Walfisz condition
on one sequence, (M,N\ge2), (MN/2\le Y\le4MN), and one of the three
printed size regimes. In particular, the modulus absolute values occur
inside the outer (q)-sum. The project fixed-centre wave has neither this
independent convolution nor this absolute-value structure, so the
corollary is not imported as an estimate.

## 6. Exact project dictionaries and outcomes

Write the project centre as (X=N+\xi), (N=\lfloor X\rfloor), and absorb
(e(\xi k/r)) into the uniformly smooth flat coefficient tensor. This
makes all source frequencies below integral without changing norms.

| Route | Exact dictionary | Audited outcome |
|---|---|---|
| Direct Bettin--Chandee | (a=k,m=1,n=r,\vartheta=N), lengths ((K,1,R)) | Legal for all real (X); both terms exceed the existing (\Delta=R/K) capacity by fixed powers. |
| Direct Wright | Same, (R_0=1) | Legal after coefficient absorption; fifth term (R^{11/8}F^{1/4}) is non-saving. A growing (R_0) is impossible because (M_0=1). |
| Square connector | (a=j^2,j=m=k,n=r), using (m^2\overline m\equiv m\pmod r) | Legal on coprime strata; sharp diagonal projective norm is (\asymp1), but all source bounds remain worse than (\Delta). |
| Smooth-weight-first completion | Fourier-expand the original (k)-weight before inversion | Complete inverse-only sum is Ramanujan; exact gcd summation returns (\Delta X^\varepsilon). |
| Inverse-selector-first completion | Reindex (m=\overline k), then Fourier-expand the rough (m)-weight | Gives genuine (S(N,h;r)) with a joint coefficient matrix and positive cost (R\sqrt\Delta X^\varepsilon). |
| Physical Wright dispersion | (s=N+t), so (t\equiv-N\pmod r) | Fixed residue is exact but not uniformly coprime; convolution, coefficient, range, principal-term, and absolute-value hypotheses fail. |
| Fixed determinant | ((m_1,n_2,m_2,n_1)=(d,r,1,N)), determinant \(dr-N\) | Corollary 1 is legal. Main terms aggregate to (\Delta X^\varepsilon); error is (X^{3/5}R^{17/20+\varepsilon}) per nonzero level. |

Here (R=X/D), (K=XL/D^2), (\Delta=R/K=D/L), and
(F=XK/R=XL/D).

## 7. Source decision

The two primary papers are valid external dependencies for the exact
statements above. Their literal direct, square-connector, completion,
dispersion, and determinant interfaces do not prove a strict improvement
of the accepted flat-wave envelope or the quarter target. This is a scoped
source-interface result only. It does not rule out a new theorem for the
project's joint (\chi_4)-signed coefficient matrix.
