# Round 187 power/literal-scope post-TeX-repair verification

## Verdict

**GREEN.**

The current candidate hashes to

c2f01f57a41695d73d0d1f9716a03328147dbe79f0fcdeb7e8e3465b29779b89,

exactly the expected repaired hash. The frozen pre-repair candidate
hash was

528c137d7da9dc4de2a892513ee2296ad0c25cbc119692db4575415adac15514.

Comparison with that frozen copy confirms that the sole candidate
change is the two requested TeX backslashes added before \qquad in
(187.K12). The formulas, summation domains, coefficient normalization,
and all mathematical text are otherwise unchanged. In particular,
this edit changes neither (187.K12) as an identity nor any use of it in
the exact partition.

The prior review now hashes to

470737a35629b58ae82753f67ce12f26c449619a6e8a6bdc4ea17d2642562d7d.

Its pre-repair hash was

de7a796957b6079b27fa783a723884a41e12bc12db893c12fd57ca69189c58f5.

The review delta is only the mechanical removal of the embedded
carriage return in \mathrm{odd} and restoration of that literal TeX
token. It changes no word, equation, test outcome, hypothesis,
argument, or recommendation.

## State effect

Retain the prior **GREEN** verdict without qualification: (187.K6),
(187.K7), (187.K22), the exact raw complement, prime-\(U\) self-return,
high-mode energy, literal endpoint/deletion scope, one-outer-real-part
placement, and downstream owner/exponent quarantine remain verified.
The reduction alone is promotable as proved_internal; (187.K8) and
all downstream owners remain open. No repeat mathematical review or
state change is warranted from these TeX-only repairs.
