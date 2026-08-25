# Round 163 conductor seed: exact one-toggle and complement geometry

- Campaign: `m9-m2-hard-top-t1-near-square-divisor-involution-gate`
- Starting graph:
  `700182f4dcf805e7f5ae74ca8ac49e88e4025471d9def1746a832c45fb6d2358`
- Status: candidate seed only

## Exact product grouping

Putting $N=d_1d_2$ in the literal $t=1$ scalar is bijective because
$d_1,d_2$ are squarefree and coprime. The cone
$d_2\le d_1\le4d_2$ becomes
$\sqrt N\le d_1\le2\sqrt N$, and

\[
 W\!\left(\sqrt{\frac{q_Xd_1}{4d_2}}\right)
 =W\!\left(\frac{\sqrt{q_X}\,d_1}{2\sqrt N}\right).
\]

This yields the exact coefficient stated in the strategy, including the
odd divisor and even-$N$ branch.

## Single sign-reversing toggle

Let $p\equiv3\pmod4$ be an odd prime divisor of squarefree $N$. Pair a
divisor $d$ not containing $p$ with $pd$. The characters are opposite.
If $A_N(d)$ denotes the literal profile times the indicator of the upper
near-square interval, then exactly

\[
 b_{L,X}(N)=
 \sum_{\substack{d\mid N/p\\d\ {\rm odd}}}
 \chi_4(d)\{A_N(d)-A_N(pd)\}.
\]

But the two supports are disjoint: if $d\in[\sqrt N,2\sqrt N]$, then
$pd>2\sqrt N$; if $pd\in[\sqrt N,2\sqrt N]$, then
$d<\sqrt N$. Therefore the difference above is all leakage, not a thin
boundary correction. The involution preserves $N$ and its phase, but it
does not preserve the physical cone.

If $\mathcal P_3(N)=\{p\mid N:p\equiv3\pmod4\}$, summing the preceding
identity over all $p\in\mathcal P_3(N)$ appears to self-return exactly:

\[
 |\mathcal P_3(N)|b_{L,X}(N)
 =\sum_{p\in\mathcal P_3(N)}
   \sum_{\substack{d\mid N/p\\d\ {\rm odd}}}
   \chi_4(d)\{A_N(d)-A_N(pd)\}.
\]

Indeed, for a fixed active divisor $r$, a prime $p\nmid r$ contributes
$\chi_4(r)A_N(r)$ through the first term, whereas $p\mid r$ contributes
$-\chi_4(r/p)A_N(r)=\chi_4(r)A_N(r)$ through the second. Thus averaging
the one-prime boundary identities reinforces every physical term. This
sign check remains a candidate until independently reviewed.

## Complement

The map $d\mapsto N/d$ sends the upper window to
$[\sqrt N/2,\sqrt N]$. For odd $N$ it gives the exact identity

\[
 b_{L,X}(N)=\chi_4(N)
 \sum_{\substack{e\mid N, e\ {\rm odd}\\
                  \sqrt N/2\le e\le\sqrt N}}
 \chi_4(e)A_N(N/e),
\]

which is a swapped lower-window coefficient, not cancellation inside the
physical sum.

For even squarefree $N=2M$, $M$ odd, the physical factor complement
$N/d$ is even. The character-preserving complement on the odd divisor
lattice is $e=M/d=N/(2d)$ and gives

\[
 b_{L,X}(2M)=\chi_4(M)
 \sum_{\substack{e\mid M\\e\ {\rm odd}\\
                  \sqrt N/4\le e\le\sqrt N/2}}
 \chi_4(e)A_N\!\left(\frac{N}{2e}\right).
\]

This lies still farther below the physical upper window. Thus neither
the even physical complement nor the odd-part character complement is a
second character-supported physical leg.

## Unresolved possibility

A two-prime exchange can have ratio close to one and may preserve the
window. If it exchanges primes from opposite residue classes modulo four,
it reverses the character. The seed does not decide whether such
exchanges admit a global matching, whether unmatched divisors are small,
or whether literal profiles destroy the pairing. This is the main
discovery question; no single-toggle no-go may be promoted as a no-go for
all divisor involutions.

## Power warning

The positive coefficient capacity remains $L^{2+o(1)}$, so a useful
matching or leakage theorem must recover $L^{1/2-o(1)}$ after every
unmatched term and profile difference is restored. Constant-weight
semiprimes may falsify a claimed pointwise cancellation but are not a
physical lower bound.
