# Round 133 blind statement packet

This packet is statement-only.  It supplies a corrected conditional source
interface and a literal target scalar.  It makes no applicability claim.

## A. Corrected Li--Yang/Bombieri--Iwaniec source interface

Let \(T,M\) be large, \(H\ge1\), let \(g,G\) be bounded-variation
functions on \([1,2]\) with fixed bounded norms, and let
\(F\in C^3[1,2]\).  Define

\[
 S=\sum_{H\le h\le2H}g(h/H)
   \sum_{M\le m\le2M}G(m/M)
   e\!\left({hT\over M}F(m/M)\right).                    \tag{133.S1}
\]

The phase hypotheses are the two separate conditions

\[
 C_r^{-1}\le |F^{(r)}(z)|\le C_r\quad(r=1,2,3),           \tag{133.S2}
\]

and

\[
 |F'(z)F'''(z)-3F''(z)^2|\ge C_4^{-1}                    \tag{133.S3}
\]

for every \(z\in[1,2]\), with fixed constants.

The source separates two second-spacing regimes.  The corrected Case A
conditions are

\[
\begin{cases}
H\ge M^{-9}T^4(\log T)^{171/140},&M<T^{7/16},\\
H\ge M^{11}T^{-6}(\log T)^{171/140},&M>T^{9/16},\\
H\le MT^{-49/164},
\end{cases}                                               \tag{133.S4}
\]

where the positive \(7/16\) is the audited correction.  Case B requires

\[
 M\le C_5T^{1/2},\qquad
 H\le\min\{M^{35/69}T^{-2/23},B_0M^{3/2}T^{-1/2}\}.       \tag{133.S5}
\]

For \(4\le q\le4.5\), set

\[
 N_A\asymp H(M/H)^{41/25}T^{-49/100}
               (\log T)^{969/14000},                     \tag{133.S6}
\]

and

\[
 N_B\asymp\min\{M^{7/8}T^{-3/20}H^{-29/40}
                      (\log T)^{969/5600},
                  M^2H^{-1/3}T^{-2/3}\}.                 \tag{133.S7}
\]

The conditional estimate also requires

\[
 N^{6-q}\gg H^{2q-6}(M^3/T)^{4-q}.                       \tag{133.S8}
\]

The source **prints** the claim that substituting \(N=N_A\) gives

\[
 H^{(2q-6)/(6-q)+16/25}M^{34/25}
 \ll T^{51/100}(\log T)^{969/14000}.                     \tag{133.S9}
\]

The algebraic equivalence of (133.S9) and (133.S8) is not granted in this
packet; it is part of the required source-interface check.

Under the full audited hypotheses, including a valid condition that implies
(133.S8), the intended source conclusion is

\[
\begin{split}
{S\over H}\lesssim_\varepsilon T^\varepsilon
&\left({H\over M}\right)^{-8/25+36/(25q)
             +7(q-4)/(25q(q-2))}\\
&\times T^{51/200+29/(100q)-(q-4)/(50q(q-2))}\\
&\times\left(1+left({H\over M}\right)^{14/(25(q-2))-24/25}
T^{-1/(25(q-2))-47/200}\right)^{1/q}.                   \tag{133.S10}
\end{split}
\]

In the printed Case-B reduction one additionally sees

\[
 M^{-27/23}T^{53/92}<H<M^{-9}T^4(\log T)^{171/140}.       \tag{133.S11}
\]

The audited general interface must retain a missing logarithm in the lower
comparison when the second branch of \(N_B\) is used:

\[
 H>M^{-27/23}T^{53/92}(\log T)^{2907/12880}.              \tag{133.S12}
\]

The source's printed general first-spacing proposition also needs the full
small-cap range, including \(\beta_2\ge0\); this is not implied by all of
its printed tuples.  Any use of (133.S10) must either verify that condition
directly or remain in a separately audited restricted range.

The internal Bombieri--Iwaniec parameters are

\[
 R\asymp(M^3/(NT))^{1/2},\quad
 R\le Q\le3H\le {3N\over64C_2},                          \tag{133.S13}
\]

\[
 L_{\rm BI}\asymp{HQ\over R^2},\qquad
 K_{\rm BI}\asymp{NQ\over R^2},\qquad
 \eta\asymp{R^2\over NH},                               \tag{133.S14}
\]

with \(L_{\rm BI}\le K_{\rm BI}\le\eta^{-1}le
K_{\rm BI}L_{\rm BI}\).  The first-spacing vector is

\[
 y(k,l)=(k,lk,l\sqrt{k},l/\sqrt{k}),                     \tag{133.S15}
\]

and its mean-value norm is denoted \(G_q\).  After the double large sieve
and the source second-spacing estimate,

\[
 S\lesssim_\varepsilon T^\varepsilon
 \max_{R\le Q\lesssim Q_2}
 \left({R\over Q}\right)^{3-6/q}
 {MR\over N}\left({H\over R}\right)^{22/(17q)}G_q.      \tag{133.S16}
\]

For each short interval, a reduced derivative approximant
\(a_{\rm BI}/r_{\rm BI}\) is introduced.  Its second-spacing vector is

\[
 x_{a/r}=\left({\bar a\over r},{\bar a c_0\over r},
 {1\over\sqrt{\mu r^3}},{\kappa_0\over\sqrt{\mu r^3}}\right),              \tag{133.S17}
\]

where

\[
 a\bar a\equiv1\pmod r,\quad
 \mu={1\over2}{T\over M^3}F''(m_0/M),                   \tag{133.S18}
\]

\[
 \nu={{T\over M^2}F'(m_0/M)-a/r\over2\mu},\quad |\nu|\le1,               \tag{133.S19}
\]

and \(c_0\), \(\kappa_0\) are respectively the integer and fractional
parts of

\[
 r{T\over M}F(m_0/M)-\mu\nu^2.                           \tag{133.S20}
\]

The second spacing problem counts pairs of reduced approximants satisfying

\[
\left\|{\bar a\over r}-{\bar a_1\over r_1}\right\|
 \lesssim (K_{\rm BI}L_{\rm BI})^{-1},                   \tag{133.S21}
\]

\[
\left\|{\bar a c_0\over r}-{\bar a_1c_1\over r_1}\right\|
 \lesssim L_{\rm BI}^{-1},                               \tag{133.S22}
\]

\[
\left|{1\over\sqrt{\mu r^3}}-{1\over\sqrt{\mu_1r_1^3}}\right|
 \lesssim (L_{\rm BI}\sqrt{K_{\rm BI}})^{-1},           \tag{133.S23}
\]

\[
\left|{\kappa_0\over\sqrt{\mu r^3}}
      -{\kappa_1\over\sqrt{\mu_1r_1^3}}\right|
 \lesssim {\sqrt{K_{\rm BI}}\over L_{\rm BI}}.         \tag{133.S24}
\]

For the source circle application, the required final output is

\[
 {S\over H}\lesssim_\varepsilon T^{\theta+\varepsilon}. \tag{133.S25}
\]

## B. Literal project target

Let

\[
 W=Y^{7/16},\qquad D=Y^{1/2},\qquad L=Y^{1/6},qquad c\asymp Y.
\]

For \(i=1,2\), with \(\kappa_1=1\), \(\kappa_2=4\), the first open
top-shell object is

\[
 \mathfrak O_{i,D}^{+}(c)
 =\sum_{r=(a,b)}^{\rm lit} A_i(r)
   \sum_{r'=(a',b')}^{\rm lit}B_i(r,r')
   e\!\left({ca\over\kappa_i b}-{ca'\over\kappa_i b'}\right),             \tag{133.P1}
\]

where \(|a|,|a'|\asymp L\), \(b,b'\asymp D\),

\[
 n=ab'-a'b>0,\qquad n\lesssim{\kappa_i bb'\over W},       \tag{133.P2}
\]

and \(B_i(r,r')\) includes the taper
\(1-Wn/(\kappa_i bb')\) and every physical primitive-lift selector,
Stieltjes/Mobius profile, threshold, M1 quarter or M2 \(\chi_4\) carrier,
reciprocal alias, star, cell, sign, and owner.  The coefficient is joint in
the two rays.  It is not supplied as
\(g(a/L)G(b/D)\overline{g'(a'/L)G'(b'/D)}\).

The outer data include

\[
 \sum_r|A_i(r)|\lesssim D,\qquad
 \sum_r|A_i(r)|^2\lesssim D/L.                            \tag{133.P3}
\]

For fixed outer ray and determinant, the number of literal primitive lifts
is \(O(1)\).  The accepted complete upper bound is

\[
 |\mathfrak O_{i,D}^{+}(c)|
 \lesssim_\varepsilon Y^{35/48+\varepsilon}.             \tag{133.P4}
\]

The ideal one-term-per-ray persistence threshold and determinant target are

\[
 Y^{27/48+\varepsilon},\qquad Y^{24/48+\varepsilon}.      \tag{133.P5}
\]

The candidate map for one **unrestricted single wave** is

\[
 h=a,\quad m=b,\quad H=L,\quad M=D,\quad
 T=c/\kappa_i,\quad F(z)=1/z.                             \tag{133.P6}
\]

It reproduces \(e(ca/(\kappa_i b))\) after sign and dyadic splitting.  The
task is to decide whether (133.P6) extends legally to the joint,
determinant-restricted, owner-dependent scalar (133.P1), or whether the
source variables, weights, spacing vectors, or norm direction first fail.

The same-denominator controls have

\[
 b'=b,\qquad m_\Delta=a-a'={n\over b},\qquad
 1\le m_\Delta\lesssim D/W=Y^{3/48};                      \tag{133.P7}
\]

at \(c=\kappa_i b^2\) their displayed geometric phase is one.  This is a
local control, not a lower bound for the full physical scalar.

No positive large-sieve energy, arbitrary coefficient norm, averaged
centre, or theorem for one separably weighted \(S\) may be substituted for
the literal signed scalar without an explicit connector and its full cost.
