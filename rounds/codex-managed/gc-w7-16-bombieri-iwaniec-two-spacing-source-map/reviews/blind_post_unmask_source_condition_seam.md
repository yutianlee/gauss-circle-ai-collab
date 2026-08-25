# Round 133 post-unmask source-condition seam review

## 1. Result

The official v2 TeX has a genuine algebraic error in the sentence that substitutes the Case-A value of \(N\) into Lemma 4.1.  The exact source numbering is:

- Lemma 4.1's hypothesis is equation **(4.6)**;
- the Case-A/Case-B definition of \(N\) is equation **(4.8)**;
- the formula claimed to result from the substitution is equation **(4.9)**, not (4.8).

Equation (4.9) is not equivalent to (4.6).  Their admissible right sides after solving for the same power of \(H\) differ by

\[
\frac{T^2}{M^6}=\left(\frac{T}{M^3}\right)^2.
\]

The later final-range check, equation (5.23), does not prove the printed (4.9).  After the necessary correction \(H/M=T^x\) to the sign typo in (5.18), it is instead exactly the strict power form of the original Lemma-4.1 condition (4.6).  It holds throughout the final narrow range, with the endpoint \(q=4\) checked directly.  Therefore this seam can repair the final narrow circle/divisor argument by bypassing (4.9) and invoking (4.6) directly.  It is evidence of a source algebra/typographical error, not evidence that Lemma 4.1 or the final narrow exponent fails.  It does not, however, validate Theorem 4.2 with (4.9) as literally printed over every parameter range.

For the exponent audit,

\[
\Phi(-1/3)=\frac{29+5\sqrt{170}}{300}
=0.313973413506755\ldots .
\]

The conductor's radical formula is correct.  The blind report's \(377/1200=0.3141666\ldots\) is the legal but nonoptimal choice \(q=4\), not a competing value of \(\Phi(-1/3)\).

## 2. Exact source statements and hypotheses

The TeX uses `\numberwithin{equation}{section}`.  Counting the displayed equations in Section 4 gives the following exact source locations.

Lemma 4.1 states at (4.6):

\[
N^{6-q}\gg H^{2q-6}\left(\frac{M^3}{T}\right)^{4-q}.       \tag{4.6}
\]

The Case-A branch of (4.8) is

\[
N_A\sim H\left(\frac MH\right)^{41/25}T^{-49/100}
(\log T)^{969/14000}.                                      \tag{4.8A}
\]

Immediately after (4.8), the source says that in Case A, (4.6) “becomes”

\[
H^{(2q-6)/(6-q)+16/25}M^{34/25}
\ll T^{51/100}(\log T)^{969/14000}.                       \tag{4.9}
\]

Thus references to “the printed substitution (4.8)” conflate the input definition with the claimed output: the faulty substituted condition is (4.9).

In Section 5 the source literally prints

\[
H=MT^{-x}                                                        \tag{5.18}
\]

but immediately gives

\[
-\frac38<x\le-\theta^*\le-\frac{49}{164}.                    \tag{5.19}
\]

The literal minus in (5.18) is inconsistent with the earlier bound \(H/M\le T^{-\theta^*}\), with the range (5.19), and with every exponent obtained in (5.22).  Those formulas all require

\[
\frac HM=T^x.                                                   \tag{R133.7}
\]

With

\[
q=q_x=2+\frac{2}{5\sqrt{\frac{-1-8x}{2(1-14x)}}-1},            \tag{5.20}
\]

the later check is

\[
\frac{\frac7{25}x-\frac1{50}}
     {\frac{41}{25}x+\frac{49}{100}}
<\frac{q-2}{q-4}.                                               \tag{5.23}
\]

The source says (5.23) deduces (4.9).  The algebra below shows that it instead verifies (4.6).

## 3. Substitution algebra, inequality direction, and logarithms

Put

\[
\lambda=\frac{969}{14000},\qquad
A_q=\frac{34q-54}{25},\qquad
B_q=\frac{51q-106}{100}.
\]

Since

\[
N_A=H^{-16/25}M^{41/25}T^{-49/100}(\log T)^\lambda,
\]

the quotient of the two sides of (4.6) is

\[
\begin{aligned}
&\frac{N_A^{6-q}}
{H^{2q-6}(M^3/T)^{4-q}}\\
&\quad=
H^{(54-34q)/25}M^{(34q-54)/25}
T^{(106-51q)/100}(\log T)^{\lambda(6-q)}\\
&\quad=\left(\frac HM\right)^{-A_q}T^{-B_q}
(\log T)^{\lambda(6-q)}.
\end{aligned}                                                   \tag{R133.8}
\]

Therefore the exact substituted condition is

\[
\left(\frac HM\right)^{A_q}T^{B_q}
\ll(\log T)^{\lambda(6-q)},                                    \tag{R133.9}
\]

or, because \(6-q>0\),

\[
\left(\frac HM\right)^{A_q/(6-q)}
\ll T^{(106-51q)/(100(6-q))}(\log T)^\lambda.                  \tag{R133.10}
\]

The logarithm has a positive exponent: \(\lambda(6-q)>0\) for \(4\le q\le4.5\).  In particular, equality of the power exponent would still satisfy the asymptotic lower condition; a strict positive power gives more than enough slack.

Raising the printed (4.9) to \(6-q\) gives instead

\[
H^{A_q}M^{34(6-q)/25}
\ll T^{51(6-q)/100}(\log T)^{\lambda(6-q)}.                    \tag{R133.11}
\]

Solving (R133.9) and (R133.11) for \(H^{A_q}\), the printed allowed right side divided by the correct one is

\[
T^{51(6-q)/100+B_q}
M^{-34(6-q)/25-A_q}=\frac{T^2}{M^6}.                           \tag{R133.12}
\]

Thus the formulas agree only on \(M^3\asymp T\).  For the Round-133 single-wave powers \(M=T^{1/2}\), this ratio is \(T^{-1}\): (4.9) is stronger and fails, while (4.6) holds.  Conversely, when \(M^3<T\), (4.9) can be weaker and need not imply (4.6), which is why Theorem 4.2 cannot simply be retained with its printed hypothesis.

Using the intended \(H/M=T^x\), (R133.8) becomes

\[
T^{E(x,q)}(\log T)^{\lambda(6-q)}\gg1,
\quad
E(x,q)=\frac{x(54-34q)}{25}+\frac{106-51q}{100}.               \tag{R133.13}
\]

Equivalently,

\[
100E(x,q)=(216x+106)-q(136x+51).                               \tag{R133.14}
\]

At \(x=-1/3\),

\[
E(-1/3,q)=\frac{102-17q}{300}
=\frac{17(6-q)}{300}>0                                        \tag{R133.15}
\]

throughout the source range \(4\le q\le4.5\).  This reproduces the direct slack found in the blind report, now against the official source text.

## 4. Final-range check and repair of the narrow theorem

On \(-3/8<x\le-\theta^*\), define

\[
a(x)=\frac7{25}x-\frac1{50},\qquad
b(x)=\frac{41}{25}x+\frac{49}{100}.
\]

Both \(a(x)\) and \(b(x)\) are negative, while \(q-4>0\) in the interior.  Multiplying (5.23) first by \(b(x)<0\) reverses the inequality; multiplying next by \(q-4>0\) preserves it.  Hence

\[
a(x)(q-4)>b(x)(q-2).
\]

Clearing the denominators gives exactly

\[
(216x+106)-q(136x+51)>0,                                     \tag{R133.16}
\]

which is \(E(x,q)>0\) in (R133.14).  It is not the printed condition (4.9), which still has an independent \(M\)-power after \(H/M=T^x\) is inserted.

The validity of (R133.16) over the final interval can also be checked without relying on the source's verbal claim.  Let

\[
s=\sqrt{\frac{-1-8x}{2(1-14x)}},\qquad q=2+\frac2{5s-1}.
\]

All quantities by which one multiplies are positive on the interior.  After one safe squaring, (R133.16) is equivalent to

\[
P(x):=6064x^2+11148x+2859<0.                                \tag{R133.17}
\]

Here \(P'(x)=12128x+11148>0\) on \([-3/8,-0.3144]\), and the source states \(\theta^*>0.3144\).  Therefore

\[
P(x)\le P(-0.3144)=-46.52080896<0
\]

on the required range.  At the excluded quotient endpoint \(x=-3/8\), the source choice is \(q=4\), so (5.23) has a zero denominator and must be interpreted by a limit.  Directly, (R133.14) equals \(25>0\), or \(E=1/4\), so (4.6) still holds there.

The repair is consequently local and exact:

1. use (5.23), with (R133.7), to establish the original (4.6) directly;
2. invoke Lemma 4.1 to obtain (4.7);
3. insert the actual \(N_A\) from (4.8) into the conclusion (4.7), giving the displayed final-form estimate (4.10), with logarithms absorbed into \(T^\varepsilon\);
4. in the source's Case-B reduction, use \(N_B>N_A\) and \(6-q>0\) to transfer (4.6) from \(N_A\) to \(N_B\), exactly as the monotonicity discussion after Lemma 4.1 requires.

Thus the final narrow application does not need (4.9).  This review certifies the repair of this condition seam only; it is not a fresh audit of every other hypothesis in the Li--Yang theorem.

## 5. Audit of \(\Phi(-1/3)\)

The exponent function intended by the source's defining equation (1.1) and final equation (5.28) is

\[
\Phi(x)=-\frac8{25}x+\frac{51}{200}
-\frac1{200}\left(\sqrt{2(1-14x)}-5\sqrt{-1-8x}\right)^2.     \tag{R133.18}
\]

The intermediate equation (5.27) literally prints \(\sqrt{-1-14x}\) in its second radical.  That is a local typo: the preceding algebra (5.25), the following equation (5.28), and the defining equation (1.1) all have \(\sqrt{-1-8x}\).

At \(x=-1/3\), (R133.18) gives

\[
\begin{aligned}
\Phi(-1/3)
&=\frac8{75}+\frac{51}{200}
-\frac1{200}\left(\sqrt{\frac{34}{3}}-5\sqrt{\frac53}\right)^2\\
&=\frac8{75}+\frac{51}{200}
-\frac1{200}\left(53-\frac{10}{3}\sqrt{170}\right)\\
&=\frac{29+5\sqrt{170}}{300}
=0.313973413506755\ldots .
\end{aligned}                                                   \tag{R133.19}
\]

The associated source choice is

\[
\frac2{q_*-2}=5\sqrt{\frac5{34}}-1,
\qquad
q_*=\frac{250+10\sqrt{170}}{91}=4.180044\ldots .              \tag{R133.20}
\]

Substitution of \(q_*\) into the blind report's exact function

\[
p(q)=\frac{217q^2-616q+500}{600q(q-2)}
\]

gives (R133.19).  By contrast, the blind report intentionally used the simpler legal endpoint \(q=4\), for which

\[
p(4)=\frac{377}{1200},\qquad
p(4)-\Phi(-1/3)=\frac{261-20\sqrt{170}}{1200}>0.               \tag{R133.21}
\]

Therefore there is no mathematical inconsistency between the conductor and blind artifacts: they use different \(q\).  The actual source inconsistency is the `14` versus `8` typo in (5.27).

## 6. First doubtful step, controls, and dependencies

The first invalid source step is the exact sentence after (4.8) asserting that substituting \(N_A\) makes (4.6) become (4.9).  Equations (R133.8)--(R133.12) refute that assertion with all inequality directions and logarithmic powers retained.

The controls give the following outcomes:

- **Equation-number control:** passed after correction: (4.8) defines \(N\); (4.9) is the faulty claimed substitution.
- **Sign control:** (5.23) must be multiplied through using \(b(x)<0\), which reverses the inequality.  The result is (R133.16), exactly the original condition.
- **Log control:** the factor is \((\log T)^{\lambda(6-q)}\) before taking the \((6-q)\)-th root and \((\log T)^\lambda\) afterward; both exponents are positive.
- **Endpoint control:** (5.23) is singular at \(q=4\), but (4.6) has the direct positive exponent \(E=1/4\).
- **Exponent control:** the optimized \(\Phi(-1/3)\) and the blind \(q=4\) exponent differ for the lawful reason shown in (R133.21).
- **Scope control:** repairing the external narrow source condition does not supply a coefficient-preserving connector to the literal Round-133 pair scalar.  The no-go conclusion of the blind report is unchanged.

This review used only:

1. `rounds/web-research-test/Li-Yang-arXiv-2308.14859v2.tex`;
2. `rounds/codex-managed/gc-w7-16-bombieri-iwaniec-two-spacing-source-map/candidates/conductor_single_wave_bi_parameter_map.md`;
3. `rounds/codex-managed/gc-w7-16-bombieri-iwaniec-two-spacing-source-map/reports/blind_double_large_sieve_feasibility.md`.

No proof graph, sibling report, web source, or shared synthesis was read or changed.

## 7. Recommended state effect

**Revise** the source-condition record as follows:

1. identify Lemma 4.1's original condition as (4.6), the definition of \(N\) as (4.8), and the erroneous substituted condition as (4.9);
2. mark (4.9) as an algebraic source typo/false normal form, not as a hypothesis equivalent to (4.6);
3. retain the final narrow Li--Yang condition path only through the direct implication (5.23) \(\Rightarrow\) (4.6), with the \(q=4\) endpoint checked separately;
4. correct the intended relation in (5.18) to \(H=MT^x\) and the second radical in (5.27) to \(\sqrt{-1-8x}\);
5. retain the conductor value \(\Phi(-1/3)=(29+5\sqrt{170})/300\), and retain the blind \(q=4\) value only as a nonoptimal diagnostic bound.

Classify this seam as **repairable source error, not final narrow-theorem failure**, while declining any broader certification of Theorem 4.2 as literally printed.  Make no project-exponent or literal-scalar promotion from this review.
