# Round232 control record

Campaign `gc-upper-tail-separated-products`; conductor reproduction2026-10-12 Asia/Shanghai. Evidence level: `diagnostic_only`. Planned analytical/algebraic allocation95 percent, numerical experimentation at most5 percent; all substantive proofs and reviews were analytical. The sole finite reproduction checks integer/rational algebra and cannot certify any asymptotic claim.

Command from repository root:

    python rounds/codex-managed/gc-upper-tail-separated-products/controls/exact_controls.py

Code: `exact_controls.py`. Recorded output: `exact_controls.json`. Arithmetic uses exact integers and rational fractions, with a rational enclosure of beta checked by squaring; no floating-point tolerance is used for pass/fail. Pass requires every explicit assertion to hold. The archived run passed.

| Control | Cases | Outcome and scope |
|---|---:|---|
| Negative close-band quadratic form | 1 | Exact value-2; excludes universal PSD |
| Multiples in arbitrary real intervals | 376 | Endpoint and ordered-distinct-pair bounds pass |
| Gcd pairs versus enlarged common-divisor count | 144 | Upper enlargement and diagonal exclusion pass |
| Actual small-gcd character/product identity | 3131 | Odd T101..301, u3..33; gcd1, equal character and difference8u-16 pass |
| Rational exponent ledger | fixed expressions | Near-3/250, high-gcd-9/500, both strictly below-a*, spacing503/500 pass |

The real-interval cases use starts1,7/2,51,201/2 and lengths1/2,3/2,4,17/2,23,81/2. The exact rational margins are retained in the output. The finite small-gcd loop checks only the algebraic identities; it does not assert that every finite pair satisfies the asymptotic separation or lies in the actual exceptional set. The analytic smooth-component construction and its limitation are independently reviewed in `reviews/independent_separated_attack_review.md`.

The blind report separately supplies exact PSD, zero-band, remote-block, growing-width and aligned-family controls without computation. `reviews/conductor_blind_band_review.md` verifies them algebraically. The high-gcd review explicitly pays atomic local tails and all mixed products, independently of the packet's internal signs.

No random simulation, sampled tail probability, fitted exponent, source theorem, or full-wave lower bound is used. The required complete signed estimate remains open after these controls.
