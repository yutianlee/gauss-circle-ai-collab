# Round 121 derivation packet: one-count height kernel and character pair

Campaign: `m9-m1-global-lower-height-kernel-gate`

Starting graph SHA-256:
`54f1c4ffd3a4ec9f166773ddb5f013a2fc7028b0a2586709f7379116a92da974`

## 1. Sole remaining GAR owner

Round 120 proves the whole nonlower radial complement. Hence the only
unproved analytic child of the global angular-radial route is

\[
 G_{\rm low}(X)=\sum_{n\leq N_X}^{*}V_{\rm low}(n/Y)
 \mathcal C_X^*(n)n^{-3/4}e(\sqrt{Xn}),
 \qquad N_X=\lfloor16Y\rfloor.
\tag{121.1}
\]

The exact positive antecedent is

\[
 \mathcal B_{\rm low}^+
 =\sum_j\sum_{h\leq H_j}{\Phi(h/(H_j+1))\over h}
 \sum_{d\geq1}\chi_4(d)w_j(d)
 V_{\rm low}\!\left({4R^2h^2\over d^2}\right)e(hX/d).
\tag{121.2}
\]

The accepted positive-frequency transforms give

\[
 \mathcal B_{\rm low}^+
 ={e(1/8)\over i}R G_{\rm low}(X)+O_{s_0}(\log^2(2X)),
\tag{121.3}
\]

with the hard cotangent boundary retained. Thus the exact target is
\(\mathcal B_{\rm low}^+\ll RX^\varepsilon\). This round must not use
the proved nonlower theorem to estimate any part on which
\(V_{\rm low}\neq0\).

## 2. Exact profile-first aggregation

Set

\[
 a_j(h)={\bf1}_{h\leq H_j}\Phi(h/(H_j+1)),\qquad
 A_X(h,d)=\sum_j a_j(h)w_j(d),
\tag{121.4}
\]

where empty \(H_j=0\) scales are omitted before any quotient is formed.
Since the lower radial multiplier is independent of \(j\), finite
reordering gives

\[
 \mathcal B_{\rm low}^+
 =\sum_{h,d\geq1}{\chi_4(d)\over h}A_X(h,d)
 V_{\rm low}\!\left({4R^2h^2\over d^2}\right)e(hX/d).
\tag{121.5}
\]

This is the one-count object. The identity
\(w_j=E_j-E_{j+1}\) may be used only with the exact height differences
and both boundary owners; raw scale telescoping has already been proved
not to create cancellation.

## 3. Exact mod-four pairing

Define, with zero extension beyond every physical support edge,

\[
 b_X(h,d)=A_X(h,d)V_{\rm low}(4R^2h^2/d^2),\qquad
 F_X(d)=\sum_{h\geq1}{b_X(h,d)\over h}e(hX/d).
\tag{121.6}
\]

Then

\[
 \mathcal B_{\rm low}^+
 =\sum_{d\equiv1\ (4)}\{F_X(d)-F_X(d+2)\}.
\tag{121.7}
\]

For \(d\equiv1\pmod4\), put

\[
 \Delta_d={2X\over d(d+2)}={X\over d}-{X\over d+2}.
\tag{121.8}
\]

Adding and subtracting the \(d+2\) amplitude at phase \(e(hX/d)\)
gives the exact split

\[
 \begin{aligned}
 F_X(d)-F_X(d+2)
 &=\sum_h{b_X(h,d)-b_X(h,d+2)\over h}e(hX/d)\\
 &\quad+\sum_h{b_X(h,d+2)\over h}e(hX/d)
 \{1-e(-h\Delta_d)\}.
 \end{aligned}
\tag{121.9}
\]

The first line is the amplitude seam. Its conjectured polylogarithmic
bound must be proved with the hard jump, bottom edge, profile crossings,
height floors, and lower multiplier included. The second line is the
joint phase-increment height kernel. Taking
\(|1-e(-h\Delta_d)|\) and then summing in \(h\) is not an authorized
gain: the height sum must remain signed.

Equivalently, on odd \(d\), one may absorb the character into
\(e((d-1)/4)\). The combined phase is

\[
 g_h(d)={hX\over d}+{d-1\over4},\qquad
 g_h'(d)=-{hX\over d^2}+{1\over4}.
\tag{121.10}
\]

Any derivative or large-sieve argument must audit all discrete resonances
of \(2g_h'(d)\), not only the continuous stationary point.

## 4. Required comparison with accepted barriers

For fixed subcritical radial blocks through \(n\asymp X^{2/5}\), the
small-angle replacement produces the one-sided divisor cone

\[
 \sum_{q>4h}\chi_4(q)(hq)^{-3/4}V(hq/N)e(\sqrt{Xhq}).
\]

Appell completion, one-sided Poisson, inverse product-wavelet Poisson, and
one-variable crossing Fourier modes are accepted exact returns, not
estimates. Round 57 also proves that adjacent mod-four pairing on a
transformed two-point product row leaves unmatched rows and an unsaved
phase increment; local pairing alone supplies no outer square-root gain.
A Round-121 gain must therefore come from keeping the complete
profile-height aggregation or the paired height kernel jointly signed. If
the proposed pairing is merely another form of the same reciprocal cone,
the report must display the exact return and name its smallest survivor.

The full lower cutoff also contains the fixed range above the
small-angle replacement threshold. No proof below \(2/5\) may be promoted
as the global lower owner without a lawful complement estimate.

## 5. Exit gate

Accept one of:

1. the complete bound \(\mathcal B_{\rm low}^+\ll RX^\varepsilon\);
2. a strict target-safe package and a smaller literal survivor;
3. a new signed power saving with exact remaining capacity; or
4. a rigorous no-go showing that global profile recombination or
   denominator pairing is capacity-preserving.

Every result must state its implication scope. Even complete GAR is an
alternative theorem for the total active M1 aggregate; it does not prove
the two blockwise M9-M1 parents, M9-M2, endpoint uniformity, M9, or the
quarter theorem by itself.
