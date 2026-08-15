# Endpoint exact-square diagnostic

## Purpose

Falsify or support only the finite hypothesis that \(X=4D^2\) makes a fixed
smooth endpoint block coherently attain the second-derivative scale
\(\sqrt{DL}\). This is diagnostic evidence, never theorem evidence.

## Command

Run the Python interpreter at
C:/Users/yutia/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe
on
rounds/codex-managed/m9-endpoint-fixed-profile-attack/controls/endpoint_square_diagnostic.py.

## Parameters

- \(D=2^{10},\ldots,2^{15}\).
- \(X=4D^2\).
- \(H=\lfloor\sqrt{D/2}\rfloor\).
- Dyadic positive-frequency blocks \(h\in[L,2L)\), with both frequency
  signs paired exactly through the cosine formula.
- Actual finite Vaaler amplitude
  \(-\Phi(h/(H+1))\chi_4(h)/(\pi h)\).
- Fixed nonnegative profile
  \(W(u)=\sin^2(\pi(u-1))\) on \(1\le u\le2\).
- Standard double precision; no conclusion depends on numerical precision.

## Output summary

Across all tested blocks,

\[
\frac{|B_L|}{\sqrt D}\le 0.077,\qquad
\frac{|B_L|}{\sqrt{DL}}\le0.039.
\]

The largest displayed \(|B_L|/\sqrt D\) is approximately \(0.0763\) at
\((D,L)=(16384,4)\). The exact-square test therefore falsifies the proposed
finite coherent-growth pattern on these parameters; it does not establish
uniform cancellation.

## Limitations

- The profile is one convenient smooth test profile, not the final
  telescoping profile from the normalization certificate.
- Only exact square \(X\) and modest sizes are tested.
- The result cannot prove an asymptotic bound or exclude rare resonances.
- The direct endpoint report analytically shows that nearby real \(X\) can
  change local stationary patches, so exact-square behavior is explicitly
  non-uniform.

