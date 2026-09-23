# Count, power, and masked-operator post-repair verification

- Campaign: m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate
- Round: 195
- Role: independent post-repair verification
- Final candidate SHA-256:
  cb1a4dec710b1c822d5fbb758bcab8ca39d31e26f08f2ca8ce7e0bd903a2fd17
- Prior candidate SHA-256:
  c2cb78666e5396260a6a1951aa77f37356190bad44b423d4f4779b7c744e3819

## 1. Result

**Verdict: PASS.**

The candidate changed in exactly the two requested places and nowhere
else.  Both changes are mathematically correct:

1. after (195.C15), the outer \(O(L^2X^\varepsilon)\) estimate is now
   explicitly identified as a count of the physical source before Fourier
   or Abel expansion, so it incurs no \(q/J\) factor; and
2. (195.C18) now evaluates the previous mask at the transported
   predecessor and writes it consistently as \(P_-^{\rm tr}\).

The large-\(\kappa\) fixed-packet and outer conclusions retain the PASS
verdict of the count/power/masked-operator seam review.

## 2. Exact statement and hypotheses

The theorem statement, primitive charts, physical mask,
\[
 P_{2,\ge D_L}
 =\mathbf1_{\{|d-gm|\le D_L\}}
  \mathbf1_{\{|d'-gm'|>D_L\}}
  \mathbf1_{\{\kappa\ge D_L\}},
\]
fixed-packet target
\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,\ge D_L}W)|
 \ll H_B\mathfrak m\kappa uX^\varepsilon,
\]
outer target
\[
 |\mathscr R_{{\rm core},Y,H_B}^\sigma(P_{2,\ge D_L}W)|
 \ll L^2X^\varepsilon,
\]
\(T=0/T\ge1\) conventions, exact complement \(P_{2,<D_L}\), method
boundary, downstream scope, and exponent quarantine are byte-identical to
the previously reviewed candidate.

## 3. Proof and verification

I reversed the two declared edits in memory, without writing a file.  Each
new block occurred exactly once.  The reconstructed bytes had SHA-256
\[
 \texttt{c2cb78666e5396260a6a1951aa77f37356190bad44b423d4f4779b7c744e3819},
\]
exactly the prior reviewed candidate hash.  This proves that there was no
third textual change.

The first repair makes the power ledger explicit.  The physical count is
\[
 D_L\sum_{\kappa\ge D_L}(1+L/\kappa)^2\ll L^2,
\]
and is applied directly to the unexpanded physical source.  The separate
fixed-packet argument still pays
\[
 (q/J)(uJ/q)D_L=D_Lu,
\]
then adds the accepted \(O(\kappa uX^\varepsilon)\) terminal and Fejer
terms.  Hence no \(q/J\) power is hidden.

For the second repair, if \(t+\nu_\omega(h)\) is the transported
predecessor, the identity is now literally
\[
 P_hB_h-\chi P_-^{\rm tr}B_-^{\rm tr}
 =P_h(B_h-\chi B_-^{\rm tr})
  +\chi(P_h-P_-^{\rm tr})B_-^{\rm tr}.
\]
Thus the physical-mask commutator, affine births and deaths, carries,
unequal endpoint translations, and zero extensions remain in the
recomputed core exactly as required.

## 4. First doubtful or unproved step

There is no doubtful or unproved step in the repaired
\(P_{2,\ge D_L}\) theorem.  The first open step remains the explicitly
quarantined coefficient-sensitive four-block Gram estimate on the exact
complement \(P_{2,<D_L}\); the repair makes no claim about it.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| exact two-change scope | PASS.  In-memory reversal reproduces the prior candidate hash exactly. |
| physical-before-Fourier outer count | PASS.  No Abel denominator enters the outer source count. |
| fixed-packet \(q/J\) ledger | PASS.  The candidate still pays and cancels \(q/J\) explicitly. |
| transported previous mask | PASS.  Both occurrences are \(P_-^{\rm tr}\). |
| physical-mask commutator | PASS.  The exact second term is retained. |
| both orientations and \(T\)-branches | PASS.  Their text and mathematics are unchanged. |
| outer \(L^2\) power | PASS.  The source and deletion-stable safe aggregate remain separately target-safe. |
| complement, scope, and exponents | PASS.  No statement or state effect changed. |

## 6. Exact dependencies and artifacts used

1. Repaired candidate:
   rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/candidates/formalized_hard_m1_t1_p2_large_kappa_sector.md —
   cb1a4dec710b1c822d5fbb758bcab8ca39d31e26f08f2ca8ce7e0bd903a2fd17.
2. Prior seam review:
   rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/reviews/count_power_masked_operator_seam_review.md —
   27a228df10fcd48bf6edadb27e75a2b686a88c10425259348ae5878b3751fc0b.
3. Prior candidate bytes were identified by their frozen SHA-256
   c2cb78666e5396260a6a1951aa77f37356190bad44b423d4f4779b7c744e3819
   and reconstructed exactly in memory.

No other artifact was edited or needed for this bounded post-repair check.

## 7. Recommended state effect

Pass the repaired candidate through the count/power/masked-operator gate
at final SHA-256
cb1a4dec710b1c822d5fbb758bcab8ca39d31e26f08f2ca8ce7e0bd903a2fd17.
Proceed only through the remaining declared Round-195 reviews.  This
verification changes no graph node, parent, bridge, theorem, or exponent.
