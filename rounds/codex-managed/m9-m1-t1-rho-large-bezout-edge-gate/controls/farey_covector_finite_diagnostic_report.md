# Round 192 finite Farey-covector diagnostic

## Result

PASS, diagnostic only. WolframScript 1.12.0 checked the exact signed-inverse,
canonical-quotient, unimodular-covector, finite multiplicity, union-bound, and
small-modulus-coverage identities on 158 moduli, with no failure. It also
checked the sharp circular-pigeonhole coverage inequality on every unit row.
This finite check is not evidence for any asymptotic estimate or cancellation
theorem.

## Exact checks

For every modulus \(3\le U\le160\) and every unit
\(v_0\in\{1,\ldots,U-1\}\), the diagnostic chose the signed least inverse
\(\rho\) and put \(\beta=(\rho v_0-1)/U\). It checked

\[
 \rho v_0-\beta U=1,
 \qquad |\rho|\le \left\lfloor\frac{U-1}{2}\right\rfloor,
 \qquad \rho\beta\ge0,
 \qquad |\beta|\le|\rho|,
 \qquad (|\rho|,|\beta|)=1.
\]

For every primitive \(0\le d\le c\le\min(U-1,12)\), it checked

\[
 \ell=c\beta-d\rho,
 \qquad
 \rho(cv_0-dU)=c+U\ell\ne0.
\]

For each fixed \((U,c,d,\ell)\), the number of unit residue rows was compared
with the safe signed-divisor bound \(2\tau(|c+U\ell|)\). It also checked the
literal set-theoretic union bound for \(1\le T\le5\), the convention that the
\(T=0\) sector is empty, the exact inequality

\[
 \min_{(c,d)\in\mathcal F_A}|c\beta-d\rho|
 \le \left\lfloor\frac{|\rho|}{A+1}\right\rfloor,
\]

and the primitive zero covector
\((c,d)=(|\rho|,|\beta|)\) whenever \(U\le2A\).

## Counts

- unit rows: 7,804;
- covector-row identities: 365,696;
- fixed covector fibres: 305,844;
- small-modulus coverage rows: 462;
- circular-pigeonhole rows: 7,804;
- finite union bounds: 770;
- failures: 0.

## Reproduction

Program: controls/farey_covector_finite_diagnostic.wls.

Archived stdout: controls/farey_covector_finite_diagnostic_output.txt.

Run from the repository root with
wolframscript -file rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/controls/farey_covector_finite_diagnostic.wls.

## First unproved step

The diagnostic does not prove the uniform divisor estimate, the restoration
of the literal row/height/site/outer ledger, or any cancellation on the
badly-approximable core. Those are analytical obligations of Round 192.

## Scope control

No random coefficients, phases, carries, endpoint fields, or asymptotic
parameters were simulated. The computation cannot promote the full rho-large
remainder, original \(t=1\), M9-M1, M9-M2, a bridge, the target, or an
exponent.

## State effect

No graph change. Retain as a finite falsification and sign/floor control only.
