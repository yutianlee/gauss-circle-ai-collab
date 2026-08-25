# Round 131 conductor controls

Campaign: `gc-w7-16-top-shell-determinant-residue-zero-mode-gate`

Starting graph SHA-256:
`23e7bfacbf6abc5582769fbe8d427cbca2379e1d265b99df21d93a65ec504825`

## Mathematical seam matrix

| Control | Exact test | Outcome |
|---|---|---|
| literal top-shell dictionary | Retain \(W,D,L,B\asymp D\), \(\kappa_1=1\), \(\kappa_2=4\), actual outer coefficients, thresholds, taper, stars, signs, cells, and owners before a norm. | Green. The conductor interface (131.C4) retains the literal data in the weighted amplitude. |
| physical Möbius reassembly | Compare the bare incidence identity with the \(\rho\)-dependent weighted atoms. | Green with mandatory scope correction. The stripped primitive support mask is exact after physical support is established; the bare \(\sum\mu\) identity does not factor profiles, stars, or owners. |
| fixed-lift arithmetic DFT | Recompute the M1 transform by CRT and the M2 transform by a reduced-residue sum. | Green. M1 is fixed-modulus-four Gauss\(\times\)Ramanujan; M2 is Ramanujan. Normalized Fourier \(\ell^1\) cost is divisor-sized. |
| primitive periods | Remove prime powers and then pull \(q\)-periods through \(n=aq-bp\). | Green correction. Minimal periods use radicals; \(4M\), \(|m|\), \(4|a|M\), and \(|a||m|\) are valid completion overperiods. |
| periodic/BV separation before Fourier | Shift \(n\) by \(4|a|\), test primitivity, then test determinant-order lift switching. | Common full-weight factorization fails. Primitivity changes and has linear BV if hidden in the envelope; weighted extension and cross-lift BV remain open. |
| shifted M1 mode | Evaluate \(k=0,M,3M\) in the exact DFT. | Green. Zero vanishes; \(M,3M\) have magnitude \(\varphi(M)/(2M)\) and give the two quarter frequencies. |
| M2 zero/shifted distinction | Compare fixed \(p\) with interlaced active \(p\), split odd/even \(b\). | Green. Fixed \(p\) has a nonzero \(q\)-arithmetic zero coefficient. Odd \(b\) plus fixed \(q\bmod4\) gives one interlaced shift; even \(b\) needs an extra potentially large two-adic coordinate. |
| M1 same denominator | Use \(q=0,p=-t,n=bt>0\), integral \(c/b\). | Green per-ray control. Taper mass \(D/(2W)+O(1)\); no family lower bound. |
| M2 positive numerator | Use \(q=0,p=-2j,n=2bj>0\), odd integral \(c/b\). | Green per-ray control. Phase and numerator-character product align; taper mass \(D/W+O(1)\). |
| M2 sign crossing | Put both numerators at top size with opposite signs. | Empty on the frozen top shell by the factor \(WL/D=Y^{5/48}\). The algebraic sign convention remains exact at the separately owned crossing. |
| determinant diagonal | Test \(p=q=n=0\) against the one-sided support. | The blind obstruction is rejected. The point is outside \(n>0\) and belongs to the separate target-safe equal-ray owner. Fourier \(k=0\) is not determinant \(n=0\). |
| resonant-window mass | Price one length-\(D/W\) packet and the \(O(1+WL/D)\) cover. | One packet has capacity \(Y^{30/48+o(1)}\); the cover recovers \(Y^{35/48+o(1)}\) only as a worst-case upper capacity, not proved occupied mass. |
| scalar versus positive energy | Replace the actual family scalar by a nonzero Fourier coefficient, Gram, or arbitrary direction. | Rejected. The incomplete weighted envelope and actual outer coefficients may cancel. |
| per-ray versus cross-ray capacity | Compare \(35/48,31/48,27/48,24/48\). | Green. Ideal full \(L\) per-ray gain reaches only the \(9/16\) persistence threshold; target requires a further cross-ray \(Y^{-1/16}\). |
| Salié identification | Search for a complete variable \(x\), unit inverse \(\bar x\), integral modulus phase, and boundary completion. | No-go. Only fixed-modulus-four linear Gauss\(\times\)Ramanujan arithmetic is exact. |
| no global or M9 promotion | Compare the complete exponent and graph dependencies. | Green. \(35/48\) remains; global \(1/3\), M9-M1, M9-M2, endpoint, M9, bridge, and quarter statuses do not change. |

## Post-unmask corrections

1. The blind \(p=q=n=0\) family is outside the frozen scalar and is
   superseded by the nonzero-determinant packets.
2. The blind \(4\mid|a|\) M2 subcase is inactive because the actual outer
   M2 numerator is odd.
3. The discovery full-weight periodic/BV statement is not promoted: its
   weighted Möbius factorization and complete-progression extension are open.
4. The conductor arithmetic periods are recorded as valid overperiods; the
   radical periods are the minimal ones.
5. Packet-cover capacity is not reclassified as occupied resonant mass or a
   lower bound.

## Validation record

The Round-131 State Patch validated and applied cleanly:

- created 2 obligations;
- updated 4 obligations;
- rejected 10 temporary claims;
- retained 7 downstream obligations unchanged;
- resulting graph SHA-256
  `328a885e71415a8e3509466c46849129248594334dc17df8940bbcd3f12a0fe9`.

Round-closing checks:

- graph validation: green;
- completed campaign validation: green;
- State Patch validation: green before application;
- JSON parsing for campaign, plan, patch, ledger, next-round plan, and
  validation matrix: green;
- six unit tests: six passed;
- source compilation for `math_collab` and `tests`: green;
- UTF-8/control/conflict scan: 18 Round-131/strategy/kernel artifacts green;
- `git diff --check`: green, with only repository line-ending warnings.

No numerical experiment or external source was used.
