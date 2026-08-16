# Round 85 derivation packet: large dual-difference joint dispersion

Starting graph SHA-256:
`942453c8d45068875932507e8ca84ed87bcb2187ee141029a27eb0c0642bf60f`

## 1. Frozen scales and exact survivor

Put

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},\qquad B=C/T,
\]

and freeze

\[
 J^{13/18}<C\leq J^{3/4}.                              \tag{85.1}
\]

Fix one transition-flattened smooth nonaxial principal M1 component,
one compatible nonzero pair \(k=\rho\sigma>0\), one endpoint
orientation, and one local class

\[
 (g,M,K)\in\{(1,4b,k),(2,2b,2[k\bar4]_b),(4,b,[k\bar4]_b)\}.
                                                               \tag{85.2}
\]

Thus \(gM=4b\), \(M\asymp B\), and \((K,M)=O_k(1)\).  The
opposite orientation is the conjugate reflected component.

Round 84 proved that every

\[
 0<|d|\leq D_0,\qquad D_0:=\lfloor J^{17/30}\rfloor,   \tag{85.3}
\]

is target-safe.  The exact remaining smooth-principal object is

\[
 \boxed{
 \mathfrak Y_{>D_0}^{(\kappa,k)}
 ={1\over M^2}\sum_{b\asymp B}\sum_{|d|>D_0}\sum_{n\in\mathbb Z}
 A_{M,K,d}(n)I_b(n+d)\overline{I_b(n)},}                \tag{85.4}
\]

where \(M=M_{\kappa,b}\) inside the \(b\)-sum and

\[
 A_{M,K,d}(n)
 =S(n+d,K;M)\overline{S(n,K;M)}-c_M(d).                \tag{85.5}
\]

The target is

\[
 \mathfrak Y_{>D_0}^{(\kappa,k)}
 \ll_\varepsilon X^\varepsilon {J^2\over T}=X^\varepsilon J^{7/5}.
                                                               \tag{85.6}
\]

The two Fourier factors restrict the effective range to
\(|n|,|n+d|\asymp Q^2\), apart from already owned rapidly decaying
tails.  Negative differences and every nonzero \(d\equiv0\pmod M\)
remain in (85.4).

## 2. Accepted stationary and arithmetic interfaces

For orientation \(\eta\in\{1,-1\}\), the stationary sign is
\(\eta n>0\).  Writing \(m=\eta n>0\), the accepted exact normal form is

\[
 I_{b,\eta}(\eta m)
 =e\!\left(-\eta\lambda_b\sqrt m\right)\mathcal P_{b,\eta}(m),
 \qquad \lambda_b=\sqrt X+{\sqrt{\kappa k}\over b}.     \tag{85.7}
\]

The saddle is

\[
 x_{b,m}=\sqrt{{A_{\kappa,b}M\over gm}},\qquad
 A_{\kappa,b}=\left(\sqrt{bX}+\sqrt{\kappa k/b}\right)^2,\tag{85.8}
\]

and the leading Gaussian is \(e(-\eta/8)\).  On every progression
\(m=r+M\ell\), the phase-removed complete entry/interior/exit profile
has

\[
 \|\mathcal W_{b,\eta}\|_\infty+
 \operatorname {Var}_\ell\mathcal W_{b,\eta}
 \ll_\varepsilon X^\varepsilon H,qquad
 H={C\sqrt T\over J}=B J^{-1/10}.                       \tag{85.9}
\]

The Round-84 stationary errors and wrong-sign tails are summable in
the range (85.3).  For larger \(d\), a candidate must re-audit the
overlap of the two stationary supports and may not reuse the small-d
error statement outside its proved range.

The arithmetic coefficient is periodic modulo \(M\) and satisfies,
for every integer \(d\),

\[
 {1\over M^2}\sum_{r\bmod M}|A_{M,K,d}(r)|\leq2,
 \qquad \sum_{r\bmod M}A_{M,K,d}(r)=0.                 \tag{85.10}
\]

Its nonzero finite Fourier modes are

\[
 \widehat A_d(h)=M\mathcal C_{M,K}(d,h),               \tag{85.11}
\]

\[
 \mathcal C_{M,K}(d,h)=
 \sum_{\substack{y\bmod M\\(y(y+h),M)=1}}
 e_M\!\left(d(y+h)+K((y+h)^{-1}-y^{-1})\right),
 \quad h\not\equiv0\pmod M.                           \tag{85.12}
\]

Prime powers admit individual modes as large as
\(M^{2-1/(2\nu)}\) before normalization.  Therefore no
coefficientwise square-root estimate may be assumed.  Exact Parseval,
gcd-sensitive averaging, or the joint actual weight may still be used.

## 3. Physical-row interface that must be retained

Before the complete dual transform, the same object is the coherent
nonzero residue-offset energy of the exact physical rows

\[
 R_b(r)=\sum_{\substack{c\asymp C\\c\equiv r\ (4b)}}
 V_{b,c,k}^{(\kappa)}e\!\left(\pm{A_{\kappa,b}\over c}\right).
                                                               \tag{85.13}
\]

The accepted reciprocal estimate gives, uniformly on every admissible
row and proper transition-flattened subinterval,

\[
 |R_b(r)|\ll_\varepsilon X^\varepsilon TQ^{-5/24}.      \tag{85.14}
\]

Consequently the same-residue term and each one fixed nonzero residue
offset are target-safe, while absolute summation of all offsets costs

\[
 X^\varepsilon{C^3\over TQ^{5/12}}.                    \tag{85.15}
\]

A genuine whole-offset gain \(B^{-\delta}\) in (85.15) reaches

\[
 C\leq J^{(13/6-3\delta/5)/(3-\delta)}.                 \tag{85.16}
\]

Thus \(\delta=1/2\) reaches \(C\leq J^{56/75}\), and
\(\delta=5/9\) closes (85.1).  These endpoints are only a capacity
ledger.  Neither gain is accepted.

Round 85 must preserve both (85.7)--(85.12) and the inherited physical
row saving (85.14).  A derivation that discards \(Q^{-5/24}\) and then
recovers only a generic square-root estimate has not improved the
accepted bound.

## 4. Candidate joint mechanisms and exact warnings

On \(n=r+M\ell\), the stationary product phase is

\[
 \Psi_{b,d}(n)=-\lambda_b(\sqrt{n+d}-\sqrt n).           \tag{85.17}
\]

For \(|d|=o(Q^2)\),

\[
 |\partial_\ell^2\Psi_{b,d}|\asymp {M^2|d|\over J}.     \tag{85.18}
\]

Round 84 used (85.18) only through (85.3).  Beyond that range, the
number of integral first-derivative crossings grows, the supports move,
and a fixed-\(d\) second-derivative bound can revert to trivial size.

The allowed question is whether one can couple \((d,b,r)\) before
absolute values.  Lawful possibilities include:

1. a dyadic \(d\)-dispersion or large-sieve inequality using the exact
   zero mean (85.10) and the actual stationary profile;
2. a physical/dual uncertainty inequality simultaneously keeping the
   row estimate (85.14) and the deletion (85.3);
3. a gcd-sensitive decomposition of (85.12), with every bad
   prime-power and modulus-multiple mode retained;
4. a new exact range deletion for a dyadic family \(D<|d|\leq2D\).

The following are not gains:

- completing all \(d\), \(h\), or residue variables and returning to
  (85.13);
- applying van der Corput to the entire dual sum while paying the full
  prefactor \(Q^2/D\) and not proving the resulting correlation bound;
- a coefficientwise trace estimate contradicted by prime-power modes;
- an arbitrary-weight large sieve which discards the actual symbol;
- a pointwise fixed-\(d\) estimate whose sum loses (85.14).

Perfect-square/fourth-power phases and exact integer derivatives are
adversarial controls, not deletable terms.  A rigorous counterexample
must use the actual symbol and all cutoffs; an arbitrary coefficient
model proves only a route-specific no-go.

## 5. Promotion and exit rule

A Round-85 report succeeds if it does one of the following, with all
classes, orientations, errors, and owners retained:

1. proves (85.6) on a nonempty new conductor interval;
2. proves a genuine \(B^{-\delta}\), \(\delta>0\), improvement while
   retaining the factor \(Q^{-5/12}\) from the physical-row energy;
3. removes a nonempty uniform large-difference shell above \(D_0\)
   target-safely and states the exact new survivor;
4. isolates a strictly smaller exact joint signed correlation or proves
   a rigorous actual-symbol no-go that changes the next mechanism.

No conclusion may promote \(C>J^{3/4}\), raw transition or axis terms,
cone edges, other radial sectors, full `M9-M1`, `M9`, endpoint
uniformity, or the Gauss-circle exponent.

## 6. Required controls

- exact \(M^{-2}\) normalization and target capacity;
- all three local classes and both endpoint orientations;
- inherited \(Q^{-5/24}\) physical-row saving;
- literal \(d=0\) and \(0<|d|\leq D_0\) removed exactly once;
- negative \(d\), support edges, and differences comparable with \(Q^2\);
- nonzero \(d\equiv0\pmod M\), Ramanujan subtraction, and gcd modes;
- prime-power large Fourier modes and squarefree comparison;
- actual stationary symbol, entry/exit, and aggregate errors;
- integer derivative, perfect-square, and fourth-power controls;
- any \(d\)-differencing prefactor and diagonal term;
- complete-transform and physical/dual self-return;
- current primary-source hypotheses at the literal scales;
- transition, axis, endpoint, radial-sector, and downstream ownership.
