# Blind frequency phase diagram

## 1. Result

Write

\[
D=X^\delta,\qquad L=X^\ell,\qquad
\Omega=\left\{(\delta,\ell):
\frac14\le\delta\le\frac12,\quad
0\le\ell\le\delta-\frac14
\right\}. \tag{1.1}
\]

For a target block bound \(S_{2,L}\ll X^{\vartheta+\varepsilon}\), the accepted estimates give the following exponents:

\[
\begin{array}{c|c}
\text{estimate}&\text{all retained powers of }X\\ \hline
\mathrm{T2S}&1+X^{\delta-\ell}\\
\text{second derivative}
&X^{(1+\ell-\delta)/2}
+X^{(3\delta-1-\ell)/2}\\
\text{trivial}&X^\delta\\
\text{abstract exponent pair }(\kappa,\lambda)
&X^{\kappa(1+\ell-2\delta)+\lambda\delta}
+X^{2\delta-1-\ell}.
\end{array} \tag{1.2}
\]

No concrete exponent pair is promoted here, because the brief supplies no primary-source certificate for one.

At the conjectural target \(\vartheta=1/4\), the rigorously covered set is exactly

\[
\left\{(\delta,\ell)\in\Omega:\ell=\delta-\frac14\right\}
\ \cup\ \left\{\left(\frac12,0\right)\right\}. \tag{1.3}
\]

Thus the exact unresolved set is

\[
\begin{aligned}
\mathcal U_{1/4}
={}&
\left\{(\delta,\ell):
\frac14<\delta<\frac12,\quad
0\le\ell<\delta-\frac14\right\}\\
&{}\cup
\left\{\left(\frac12,\ell\right):
0<\ell<\frac14\right\}. 
\end{aligned} \tag{1.4}
\]

The terminal line \(L\asymp H_D=DX^{-1/4}\) is covered by T2S. The isolated unit-frequency point \((\delta,\ell)=(1/2,0)\) is covered by the full second-derivative estimate. Every remaining interior point in (1.4) is unresolved at the \(X^{1/4+\varepsilon}\) target by the accepted bounds.

## 2. Exact conversion of every accepted bound

Throughout, harmless logarithms are absorbed into \(X^\varepsilon\). The block has \(L\) positive frequencies of size \(h\asymp L\), each carrying \(|\beta_{h,H}|\ll1/L\).

### 2.1 T2S

The accepted swapped-sum estimate is

\[
|S_{2,L}|\ll_\varepsilon X^\varepsilon
\left(1+\frac DL\right). \tag{2.1}
\]

Its two powers are

\[
0,\qquad \delta-\ell. \tag{2.2}
\]

On \(\Omega\), one has \(\delta-\ell\ge1/4\), so the second term dominates. T2S reaches the target \(X^{\vartheta+\varepsilon}\) exactly on

\[
\mathcal C_{\mathrm T}(\vartheta)
=\left\{(\delta,\ell)\in\Omega:
\delta-\ell\le\vartheta\right\}
=\left\{(\delta,\ell)\in\Omega:
\ell\ge\delta-\vartheta\right\}. \tag{2.3}
\]

The constant term \(1\) is retained in (2.1), although it creates no extra restriction for \(\vartheta\ge0\).

### 2.2 Full two-term second-derivative estimate

For fixed \(h\asymp L\), the phase \(hX/(4d)\) has

\[
\left|\frac{d^2}{dd^2}\frac{hX}{4d}\right|
\asymp\frac{hX}{D^3}.
\]

The accepted second-derivative estimate, after summing the \(1/h\) coefficients over \(h\asymp L\), is

\[
|S_{2,L}|
\ll_\varepsilon X^\varepsilon
\left(
\sqrt{\frac{LX}{D}}
+\frac{D^{3/2}}{\sqrt{LX}}
\right). \tag{2.4}
\]

The two exponents are

\[
E_{2,1}=\frac{1+\ell-\delta}{2},
\qquad
E_{2,2}=\frac{3\delta-1-\ell}{2}. \tag{2.5}
\]

Both terms must meet the target:

\[
\ell\le\delta+2\vartheta-1,
\qquad
\ell\ge3\delta-1-2\vartheta. \tag{2.6}
\]

Hence the exact covered region is

\[
\mathcal C_2(\vartheta)
=\left\{(\delta,\ell)\in\Omega:
3\delta-1-2\vartheta
\le\ell\le
\delta+2\vartheta-1
\right\}. \tag{2.7}
\]

The secondary term has not been dropped. On \(\Omega\),

\[
E_{2,1}-E_{2,2}=1+\ell-2\delta\ge0, \tag{2.8}
\]

so it is never larger than the first term. In particular, for \(\vartheta\ge1/4\), the lower inequality in (2.6) follows from the domain and the upper inequality; nevertheless (2.6)--(2.7) record it explicitly.

This estimate requires the denominator weight regularity under which the accepted van der Corput bound transfers by partial summation. It is not asserted for arbitrary independently phased denominator coefficients.

### 2.3 Trivial estimate

Absolute summation uses \(D\) denominators and total coefficient mass \(O(1)\) on a dyadic \(h\)-block:

\[
|S_{2,L}|\ll D=X^\delta. \tag{2.9}
\]

It covers exactly

\[
\mathcal C_0(\vartheta)
=\left\{(\delta,\ell)\in\Omega:\delta\le\vartheta\right\}. \tag{2.10}
\]

Although T2S is at least as strong on most of \(\Omega\), (2.9) is retained because it certifies the full left strip for targets \(\vartheta>1/4\) and handles \(L=1\) directly.

## 3. Rigorous union and exact complement

Without importing an uncertified exponent pair, the rigorous target region is

\[
\mathcal C_{\rm rig}(\vartheta)
=\mathcal C_{\mathrm T}(\vartheta)
\cup\mathcal C_2(\vartheta)
\cup\mathcal C_0(\vartheta). \tag{3.1}
\]

For an arbitrary target \(\vartheta\), its exact complement in \(\Omega\) is

\[
\begin{aligned}
\mathcal U_{\rm rig}(\vartheta)
=\{(\delta,\ell)\in\Omega:\;&
\delta>\vartheta,\quad
\ell<\delta-\vartheta,\\
&[\ \ell> \delta+2\vartheta-1
\ \text{or}\
\ell<3\delta-1-2\vartheta\ ]\}.
\end{aligned} \tag{3.2}
\]

For the relevant range \(1/4\le\vartheta<1/3\), (2.8) simplifies this to

\[
\mathcal U_{\rm rig}(\vartheta)
=\left\{(\delta,\ell)\in\Omega:
\delta>\vartheta,\quad
\delta+2\vartheta-1<\ell<\delta-\vartheta
\right\}. \tag{3.3}
\]

The domain condition \(\ell\ge0\) remains inclusive. Thus, if \(\delta+2\vartheta-1<0\), the point \(\ell=0\) belongs to (3.3); if \(\delta+2\vartheta-1=0\), it is covered by the second-derivative estimate and is not unresolved.

When \(\vartheta\ge1/3\), the T2S and second-derivative strips overlap because

\[
\delta+2\vartheta-1\ge\delta-\vartheta,
\]

and together with the trivial strip they cover all of \(\Omega\).

For a Li--Yang-scale target \(\vartheta=\vartheta_{\rm LY}\in(1/4,1/3)\), formula (3.3) is the exact remaining gap:

\[
\delta>\vartheta_{\rm LY},\qquad
\delta+2\vartheta_{\rm LY}-1
<\ell<
\delta-\vartheta_{\rm LY}. \tag{3.4}
\]

No decimal value of \(\vartheta_{\rm LY}\) is used, because none was source-certified in the statement-only brief.

## 4. Correctly normalized abstract exponent-pair condition

For fixed \(h\asymp L\) and \(d\asymp D\), set

\[
Y=\frac{hX}{D^2}. \tag{4.1}
\]

This is the first-derivative scale: for every fixed \(r\ge1\),

\[
\left|\frac{d^r}{dd^r}\frac{hX}{4d}\right|
\asymp YD^{1-r}. \tag{4.2}
\]

Thus the correctly normalized reciprocal-phase exponent-pair estimate is

\[
\sum_{D\le d<2D}w_D(d)e\!\left(\frac{hX}{4d}\right)
\ll_{\varepsilon}
X^\varepsilon\left(
Y^\kappa D^\lambda+Y^{-1}
\right), \tag{4.3}
\]

under the smooth/BV weight and derivative hypotheses of the relevant exponent-pair theorem. In original variables,

\[
Y^\kappa D^\lambda
=(hX)^\kappa D^{\lambda-2\kappa},
\qquad
Y^{-1}=\frac{D^2}{hX}. \tag{4.4}
\]

After summing the \(1/h\) coefficients over \(h\asymp L\), (4.3) becomes

\[
|S_{2,L}|
\ll_\varepsilon X^\varepsilon
\left[
\left(\frac{LX}{D^2}\right)^\kappa D^\lambda
+\frac{D^2}{LX}
\right]. \tag{4.5}
\]

Its two exact exponents are

\[
E_{\kappa,\lambda}
=\kappa(1+\ell-2\delta)+\lambda\delta,
\qquad
E_{\rm sec}=2\delta-1-\ell. \tag{4.6}
\]

Therefore a certified exponent pair covers exactly the points satisfying

\[
\boxed{
\kappa(1+\ell-2\delta)+\lambda\delta\le\vartheta,
\qquad
2\delta-1-\ell\le\vartheta.
} \tag{4.7}
\]

The second condition is retained. On \(\Omega\), \(2\delta-1-\ell\le0\), so it is automatic for every \(\vartheta\ge0\).

The normalization \(Y=hX/D^2\) is essential. Using the total phase variation \(hX/D\) directly as \(Y\) would insert an erroneous extra factor \(D^\kappa\).

For \(\kappa>0\), the main condition in (4.7) can be written

\[
\ell\le
2\delta-1+\frac{\vartheta-\lambda\delta}{\kappa}. \tag{4.8}
\]

For \(\kappa=0\), it is instead the vertical condition

\[
\lambda\delta\le\vartheta. \tag{4.9}
\]

Assume the standard exponent-pair range \(\lambda\ge\kappa\). For \(1/4\le\vartheta<1/3\), a single certified pair fills the entire rigorous gap (3.3) provided

\[
\boxed{
\frac{\lambda}{2}
+\kappa\left(\frac12-\vartheta\right)
\le\vartheta.
} \tag{4.10}
\]

Indeed, \(E_{\kappa,\lambda}\) increases with \(\ell\), so on the closure of (3.3) its worst upper boundary is \(\ell=\delta-\vartheta\). There it equals

\[
\kappa(1-\vartheta)+(\lambda-\kappa)\delta,
\]

which is maximal at \(\delta=1/2\) when \(\lambda\ge\kappa\), giving (4.10).

At the conjectural target \(\vartheta=1/4\), condition (4.10) becomes

\[
\boxed{\kappa+2\lambda\le1.} \tag{4.11}
\]

This is only an abstract requirement. No pair satisfying it is imported or asserted without a primary-source certificate.

## 5. Named \(D\)-scales and frequency endpoints

The exact exponents at the three named denominator scales are:

\[
\begin{array}{c|c|c|c|c}
\delta&0\le\ell\le\delta-\frac14
&E_{\mathrm T}
&E_{2,1}
&E_{2,2}
\\ \hline
\frac14&\ell=0
&\frac14
&\frac38
&-\frac18\\[2mm]
\frac38&0\le\ell\le\frac18
&\frac38-\ell
&\frac5{16}+\frac\ell2
&\frac1{16}-\frac\ell2\\[2mm]
\frac12&0\le\ell\le\frac14
&\frac12-\ell
&\frac14+\frac\ell2
&\frac14-\frac\ell2.
\end{array} \tag{5.1}
\]

The trivial exponent is \(E_0=\delta\) in every row.

### 5.1 Unit frequency \(L=1\)

Here \(\ell=0\). The exact exponents are

\[
E_{\mathrm T}=\delta,\qquad
E_{2,1}=\frac{1-\delta}{2},\qquad
E_{2,2}=\frac{3\delta-1}{2},\qquad
E_0=\delta. \tag{5.2}
\]

Since \(E_{2,1}\ge E_{2,2}\) on the domain, the best accepted unit-frequency exponent is

\[
\min\left\{\delta,\frac{1-\delta}{2}\right\}. \tag{5.3}
\]

At the three named scales it is respectively

\[
\frac14,\qquad \frac5{16},\qquad \frac14. \tag{5.4}
\]

Thus the \(X^{1/4+\varepsilon}\) target is covered at \(D=X^{1/4}\) and \(D=X^{1/2}\), but not at \(D=X^{3/8}\).

For a target \(\vartheta\in(1/4,1/3)\), unit frequency is covered exactly when

\[
\delta\le\vartheta
\quad\text{or}\quad
\delta\ge1-2\vartheta. \tag{5.5}
\]

The unresolved unit-frequency denominator range is

\[
\vartheta<\delta<1-2\vartheta. \tag{5.6}
\]

### 5.2 Terminal frequency \(L\asymp H_D\)

Here \(\ell=\delta-1/4\). The retained exponents are

\[
E_{\mathrm T}=\frac14,\qquad
E_{2,1}=\frac38,\qquad
E_{2,2}=\delta-\frac38,\qquad
E_0=\delta. \tag{5.7}
\]

T2S covers the entire terminal line pointwise at \(X^{1/4+\varepsilon}\), including all three named \(D\)-scales. The second-derivative main term is only \(X^{3/8+\varepsilon}\); its smaller secondary term must not be mistaken for the full estimate.

## 6. Controls and first unproved seam

### Secondary-term control

- T2S retains its constant \(1\).
- The second-derivative estimate retains \(X^{(3\delta-1-\ell)/2}\).
- The abstract exponent-pair estimate retains \(X^{2\delta-1-\ell}\).
- Each secondary term is shown explicitly before any domain-based redundancy is used.

### Endpoint control

- At \(\delta=1/4\), the allowed frequency interval collapses to \(L=1=H_D\), and T2S/trivial summation give exactly \(X^{1/4+\varepsilon}\).
- At \(\delta=3/8\), unit frequency has best accepted exponent \(5/16\), while the terminal block has exponent \(1/4\).
- At \(\delta=1/2\), the full second-derivative estimate gives \(X^{1/4+\varepsilon}\) only at \(L=1\), and T2S gives it only at \(L\asymp H_D\). The open interval \(0<\ell<1/4\) remains unresolved at target \(1/4\).

### Proves-too-much and source control

No exponent pair has been selected by name or used in the rigorous union. Formula (4.7) is conditional on a future primary-source certificate matching the normalization and weight hypotheses. The trivial estimate and the two accepted analytic estimates alone produce (3.1)--(3.4).

### First doubtful or unproved step

All region conversions from the displayed accepted bounds are algebraic identities. The first unproved step is any attempt to add an exponent-pair region to \(\mathcal C_{\rm rig}\) without auditing a primary theorem that yields (4.3), including its \(Y^{-1}\) term, derivative range, and weighted partial-summation hypotheses.

## 7. Dependencies and exact artifacts used

- rounds/codex-managed/m9-frequency-phase-diagram/briefs/blind_phase_diagram.md: parameter domain, required bounds, endpoint checks, and source restriction.
- The accepted T2S block estimate supplied for this assignment:
  \[
  |S_{2,L}|\ll_\varepsilon X^\varepsilon(1+D/L).
  \]
- The accepted full second-derivative estimate:
  \[
  |S_{2,L}|\ll_\varepsilon X^\varepsilon
  \left((LX/D)^{1/2}+D^{3/2}(LX)^{-1/2}\right).
  \]

No shared proof state, earlier phase diagram, or uncertified exponent-pair source was inspected.

## 8. Recommended state effect

**Promote:** the exponent table (1.2), rigorous union (3.1), exact complements (3.2)--(3.4), endpoint table (5.1), and conditional normalization (4.7). **Retain as unresolved:** the full set (1.4) at target \(1/4\), or (3.3) at a Li--Yang-scale target. **Do not promote:** any concrete exponent-pair coverage until its primary source and precise normalization have been audited.
