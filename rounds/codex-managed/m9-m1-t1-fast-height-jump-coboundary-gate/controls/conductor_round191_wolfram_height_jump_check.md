# Round 191 Wolfram height-jump diagnostic

## Purpose

This finite check tests three algebraic controls only:

1. the canonical plus/minus anchor transport from height \(h\) to \(h-1\);
2. the sign in the zero-extended backward-difference Abel identity; and
3. the fact that the Abel representation retains full bounded-array
   capacity under phase dephasing.

It is diagnostic only and proves no asymptotic estimate for the literal
coefficient.

## Code and command

Code:
controls/height_jump_operator_check.wls.

Command:

    wolframscript -file rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/controls/height_jump_operator_check.wls

Runtime: WolframScript 1.12.0 for Microsoft Windows (64-bit).

## Parameters

- every odd \(3\le U\le31\);
- every \(1\le v<U\) with \((v,U)=1\);
- every \(1\le h\le3U\);
- affine indices \(-2\le t\le2\);
- symbolic Abel checks for zero-extended sequences of lengths \(1\) through
  \(13\);
- odd prime moduli \(q=5,7,11,13,17,19,23\), every unit \(a,v\bmod q\),
  both phase orientations, and length \(17\) dephased arrays.

## Exact identities tested

With \(r_v=\bar v_U\) and \(c_v=(r_vv-1)/U\), the plus anchors obey

\[
S_{0,+}(h-1)=S_{0,+}(h)-r_v+\delta_+(h)U,
\]

\[
w_{0,+}(h-1)=w_{0,+}(h)-c_v+\delta_+(h)v,
\]

where \(\delta_+(h)=1_{S_{0,+}(h)<r_v}\). The minus anchors obey

\[
S_{0,-}(h-1)=S_{0,-}(h)+r_v-\delta_-(h)U,
\]

\[
w_{0,-}(h-1)=w_{0,-}(h)+c_v-\delta_-(h)v,
\]

where \(\delta_-(h)=1_{S_{0,-}(h)+r_v\ge U}\). The corresponding
determinants and affine reindexings were checked.

For a finitely supported sequence,

\[
\sum_h\{W(h)-W(h-1)\}z^h
=(1-z)\sum_hW(h)z^h
\]

was checked symbolically.

For the capacity control, \(W(h)=\overline z^{\,h}\) on a length-\(17\)
interval makes both the original height sum and its Abel jump form equal
to \(17\), up to numerical roundoff. This refutes any gain for the class
of arbitrary bounded arrays; it is not a lower bound for the fixed literal
packet.

## Runtime output

    ROUND191_HEIGHT_JUMP_DIAGNOSTIC
    anchor_and_abel_checks=470029
    capacity_cases=2720
    max_capacity_error=ScientificForm[3.202372833989377*^-14, 6]
    failures=0
    interpretation=diagnostic_only

## Pass rule and outcome

Pass required zero exact anchor, determinant, transport, and symbolic Abel
failures, plus maximum numerical capacity error below \(10^{-10}\).

Outcome: PASS. There were 470,029 exact anchor/Abel checks before the final
capacity assertion, 2,720 dephased capacity cases, zero failures, and
maximum error \(3.21\times10^{-14}\).

## Limitations

The finite ranges cannot certify uniform asymptotics. The dephased arrays
need not be realizable by the selector-, endpoint-, profile-, and
phase-dependent literal coefficient. The check establishes only that Abel
summation and canonical anchor transport are exact rewritings and that an
actual coefficient-sensitive correlation theorem is indispensable.
