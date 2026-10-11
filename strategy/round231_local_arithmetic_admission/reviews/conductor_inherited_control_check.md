# Conductor check of the inherited finite near-root control

## 1. Result

The explicit finite control in the already present local_global_bridge report is correct: a tuple in the actual coefficient support has a root difference below 1/T and a signed norm sum nonzero modulo 3. This checks one finite obstruction to a proposed deterministic implication. It is not an asymptotic counterexample family or a lower bound on the full moment.

## 2. Exact statement

Use A_+={11,22,33,55,110,165}, A_-={36,18,12,180,90,60}, m=1000, n_A=(Am)^2+1 and T=36*((180m)^2+1)=1166400000036. Then all twelve n_A are distinct squarefree represented integers exceeding Q=floor(T^(2/5))=67102. With six plus and six minus signs,

    |sum_+ sqrt(n_A)-sum_- sqrt(n_A)|<1/T,
    sum_+ n_A-sum_- n_A=-1820000000 = 1 mod 3.

Every first-harmonic mollifier factor is at least 1/2 for the fixed class of admissible mollifiers.

## 3. Derivation

Both A sums are 396 and both reciprocal sums are 1/5. The elementary Taylor remainder

    |sqrt(x^2+1)-x-1/(2x)|<=1/(8x^3)

therefore gives T|Delta|<=643431600019859/2662000000000000<1. Exact integer arithmetic gives the norm sum and its residue. Trial division, with all successive odd divisors up to the square root of the remaining factor, checks that every n_A is squarefree. The integer comparisons 67102^5<=T^2<67103^5 verify the exact floor. Each n_A is represented by (Am,1). Finally sqrt(n_A/T)<=1/6, and Psi(u)=integral rho(x)cos(2pi u x_1)dx>=cos(2pi u)>=1/2 for 0<=u<=1/6.

## 4. First unproved step and limitation

There is no remaining finite check. No claim is made of an arbitrarily large sequence of such squarefree tuples or of a particular sign of the Fourier window. A single finite example falsifies an unrestricted deterministic implication at these parameters; it does not refute a statement with an unspecified sufficiently-large threshold. It also does not obstruct use of a different, correctly proved arithmetic correlation theorem.

## 5. Controls and outcome

All arithmetic was independently rerun in controls/reproduce_continuation_controls.py, with exact integer/Fraction operations. All assertions pass; output is controls/continuation_exact_controls.json. The same script verifies complete residue-count tables at thirteen small odd moduli. These controls are diagnostic_only and certify no asymptotic estimate.

## 6. Provenance

Conductor, Round231 prelaunch continuation, 11 October 2026. Graph SHA256 a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b. Inputs: inherited reports/local_global_bridge.md and the newly written reproduction script. The inherited report predates these three resumed task reports and records matching complete-target and graph hashes. Its original isolation history is not re-certified by this continuation. Its bytes and the other inherited packet artifacts are preserved. Only the explicit self-contained finite assertion above is adopted here after independent checking.

## 7. State effect

Retain this finite diagnostic as scoped evidence. No graph mutation, accepted theorem promotion, actual full-moment lower bound or analytic campaign launch.
