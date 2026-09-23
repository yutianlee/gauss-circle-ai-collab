# Round 187 final-kernel power/owner post-repair verification

## Verdict

**GREEN.**

The current durable kernel hashes exactly to

a9145455a872d57debaf0f91cc8a518f80acef4c1b1fb9115dc1851765a992f2.

The intermediate post-presentation-repair hash was

026b9709bba25251c4030bd8475a35710c8c1c25cd9d103e0172821bd694ce24.

The previously reviewed GREEN kernel hash was

b9119e5d11e78d6ae45eca461f4acb2cdd9f6c49611612ee45e9f32f5dc27c74.

Comparison with that frozen version confirms that the changes to the
mathematical text are presentation, explicit standard definitions, and
provenance/attribution only. Equations (K187.8)--(K187.27), their
hypotheses, and their implications are unchanged. The sole
026b... to a914... delta is the correction of the two diagnostic-control
hash strings identified below. Both now match their named files.

## Repair classification

The substantive additions relative to the b911... kernel are:

1. a campaign, round, starting-graph, source-candidate, reconciliation,
   evidence-status, and numerical-evidence header;
2. proper TeX delimiters and typography;
3. explicit standard definitions of \(e(x)\), least residues, modular
   inverse notation, \(\mathbb U(q)\), \(\tau\), and \(\mu\);
4. an explicit formula for the complete \(U=1\) contribution, identical
   to the contribution previously specified in prose;
5. a precise blind-report attribution sentence; and
6. paths and claimed hashes for the bounded diagnostic artifacts.

Items 1--5 change no carrier, coefficient, partition, count, estimate,
or owner. Item 6 is provenance only. Its two initially incorrect hash
values have now been repaired without changing mathematical content.

## Mathematical replay

### Exact complement and one outer real part

The \(U=1\) aggregate is now displayed explicitly but is the same sum
previously denoted \(\mathscr U_{1,Y}^{\sigma}\). For \(U>1\), the mode
sets remain exactly:

\[
\begin{aligned}
 \mathcal K_{\le Q}(U)
 &=\{k:q_U(k)\le Q\},\\
 \mathcal K_{\rm edge}(U)
 &=\{k:q_U(k)>Q,\ U\le4Q\ {\rm or}\ 0<|k|_U\le Q\},\\
 \mathcal K_{\rm high}(U)
 &=\{1\le k<U:U>4Q,\ q_U(k)>Q,\ |k|_U>Q\}.
\end{aligned}
\]

Because \(Q\ge1\), these sets are disjoint and exhaustive; \(k=0\)
belongs only to \(q=1\) in the first set. Thus (K187.8) has the same
exact complement as the b911... version. The single \(\Re\) is still
outside both orientations, all heights, primitive rows, modes, affine
sites, selector states, endpoints, and phases. No new definition moves
it inward.

### (K187.9) and (K187.10) powers

The power proof is unchanged. With \(u=gU\), live support gives
\(\kappa u\asymp L\), \(\kappa v\asymp L\), and \(h\ll U\). At fixed
\((\kappa,u,U)\), the complete atom count is \(O(UL)\). Hence:

| Piece | Fixed-label cost | Global cost |
|---|---:|---:|
| \(U=1\) | \(O(LX^\eta)\) | \(O(L^2X^\varepsilon)\) |
| exact \(q\le Q\) | \(O(Lq\log(2q)X^\eta)\) | \(O(L^2Q\log^{O(1)}(2LQ)X^\eta)\) |
| \(q>Q,\ U\le4Q\) | \(O(LU\log(2U)X^\eta)\) | \(O(L^2Q\log^{O(1)}(2LQ)X^\eta)\) |
| \(U>4Q,\ 0<|k|_U\le Q\) | \(O(LQX^\eta)\) | \(O(L^2Q\log^{O(1)}(2L)X^\eta)\) |

Only the fixed polylogarithmic \(Q\), divisor powers, and logarithms are
rebudgeted. No power of \(Y\) is absorbed. This is still (K187.9).

For the raw complement, the full \(O(\log(2U))\) Fourier mass and
\(U\ll L/(\kappa g)\) give

\[
 L^2\log(2L)X^\eta
 \sum_{Y<h\le2Y}
 \sum_{\kappa g\ll L/h}{1\over\kappa g}
 \ll YL^2X^\varepsilon.
\]

The full \(Y\) remains, so (K187.10) is unchanged and still does not
prove (K187.11).

### Centering, prime return, energy, and literal scope

The trace identity

\[
 K_q(b)+K_q(-b)={2\mu(q)\over q}
\]

and the complete divisor cancellation
\(\sum_{q\mid U}\mu(q)=0\) still give (K187.25) before the outer real
part. For prime \(U=p\), \(K_p^\circ(b)=E_p(b)\) remains the exact
self-return. For odd \(U>4Q\), the two retained central modes
\(k=(U\pm1)/2\) still give at least \(8/\pi^2\) of Fourier energy.

Every selector, squarefree/coprimality deletion, profile, floor, star,
half-weight, hard sample, crossing, endpoint, conjugation, Fejer factor,
phase, sign, and zero extension remains inside
\(B_{\mathfrak f,\omega}^{\sigma}\). The new definitions do not replace
the literal coefficient by an ambient one. The adversarial and energy
controls remain mechanism tests only and imply no literal lower mass.

### First open relation and owner scope

The first open relation remains exactly

\[
 \Re\mathscr R_{Y,Q}^{\sigma}
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\]

Even its proof would close only the exact original-\(t=1\) residual
through the Round-184/185 connectors. Every original \(t\ge2\)
small-\(G\) incidence, the large-\(G\) near-resonant complement, both M1
parents, GAR, all M2 parents, endpoint uniformity, M9, both bridges, the
quarter target, and every exponent remain open. The \(t=1\)-only and
exponent quarantines are unchanged.

## Exact provenance repair verification

At hash 026b..., the kernel recorded these two incorrect diagnostic
hashes:

- conductor_round187_wolfram_inverse_residue_check.md:
  032d8039636b0e4e2040caed7c0d2ade570761812aed85711930ba37300b176a;
- inverse_residue_exact_check.wls:
  e818367a710c4051f9259966133ca48b9496dfc3d5b8b18d559072cfac4a7d83.

Direct SHA-256 hashing of the named files gives:

- conductor_round187_wolfram_inverse_residue_check.md:
  032d8039636b0e4e2040caed7c0d2ade507d111a7f966b9b40f03676fadd1113;
- inverse_residue_exact_check.wls:
  e818367a710c4051f9259966133ca48b94810a55544b4b0ec3d3fbab15a06bcd.

The a914... kernel now records exactly these latter values. Comparison
of the 026b... and a914... versions confirms that these two string
replacements are the sole delta. No equation, hypothesis, carrier,
power ledger, complement, scope statement, or evidence interpretation
changed.

The other newly stated provenance hashes do match:

| Artifact | Verified SHA-256 |
|---|---|
| source candidate | c2f01f57a41695d73d0d1f9716a03328147dbe79f0fcdeb7e8e3465b29779b89 |
| conductor reconciliation | b3de83554db114db91b33a8e994f0daa3cd9d9c41550eceabd575fbca1250705 |
| prior final power/owner review | 06b78ac063a5c2f0886b0ca5315f6e931143c48cf5a8428878e422823f8bb301 |

## Recommended state effect

Retain the prior mathematical **GREEN** verdict for
(K187.8)--(K187.27), including (K187.9)/(K187.10), the exact
complement, one outer real part, centered trace, prime self-return,
high-mode energy, literal scope, first-open (K187.11), \(t=1\)-only
scope, and exponent quarantine.

Bind the final durable kernel to
a9145455a872d57debaf0f91cc8a518f80acef4c1b1fb9115dc1851765a992f2.
No further power, owner-scope, or provenance repair is required. No
graph, owner, theorem, bridge, or exponent change beyond promotion of
this strict reduction follows from this review.
