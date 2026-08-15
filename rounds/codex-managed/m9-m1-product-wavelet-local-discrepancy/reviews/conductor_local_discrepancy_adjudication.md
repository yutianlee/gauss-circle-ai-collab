# Conductor adjudication: Round 65

## Decision

Promote the corrected affine Abel reduction and the exact period-four
unmatched-crossing formula. Retain the weighted discrepancy estimate,
pointwise LCD, PSC, GAR, M9-M1, M9, and the Gauss-circle target open.

## Accepted kernel

For the Round-64 coefficient (A_{X,\Xi}), extend (A(n)=0) for
(n\leq0) and define the all-integer discrepancy by first difference
(D(n)-D(n-1)=A(n)-c_X), with (D(\lfloor X\rfloor)=0). Then

\[
 \sum_n A(n)K((n-X)/(2T))
 =\sum_nD(n)\{W_n-W_{n+1}\}.
\]

The affine extension is essential. The sampled zero mode removes the
linear main term exactly, and (c_X\ll X^{-1/2}).

For an integral positive displacement shorter than the supported
denominators, pairing the (1\) and (3\pmod4) legs leaves exactly the
signed symmetric difference of their crossing indicators, up to
(O_\Xi(1+v/\sqrt X)). The coefficients of the survivor are
(0,\pm1). Matched rows cancel; unmatched rows are not estimated.

## Why no bound is promoted

Both independent derivations and the hostile review locate the same
first missing input: a signed bound of size (X^{1/4+\varepsilon}) for
the unmatched crossings, either pointwise over a length-(T) interval or
after the exact wavelet difference weighting. Substitution of the
crossing formula into the Abel identity self-returns to the Round-64
product wavelet. At \(\nu=2/5\), the remaining gap is still
(X^{1/20}=H/L).

The primary-source review found no applicable theorem: audited short
divisor results average over centers or use complete coefficients;
character Voronoi formulas use complete convolutions; Kloosterman-
fraction estimates require modular inverses/coprimality; almost-all
short-interval theorems do not cover the prescribed center and moving
truncation.

## Controls

- Exact Abel sign and shift: green after affine correction.
- Sampled zero mode and main term: green.
- Thin crossing geometry and endpoint orientation: green.
- Period-four cutoff commutator: green.
- Exact products and perfect powers: scoped green; no generic
  irrationality shortcut.
- Target ledger: green, with no saving obtained.
- Clean independent algebraic rederivation: green via final agent verdict
  transcribed by conductor.
- Signed LCD/weighted theorem: open.
- Full saddle/cone implication: open.

## Round status

Round 65 closes as a useful exact reduction and method/source no-go. It
does not prove a radial interval or change an exponent.
