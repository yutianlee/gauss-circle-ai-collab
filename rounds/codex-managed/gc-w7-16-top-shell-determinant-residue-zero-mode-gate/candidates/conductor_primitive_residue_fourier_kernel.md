# Conductor candidate: primitive residue Fourier kernel and interlacing seam

Campaign: gc-w7-16-top-shell-determinant-residue-zero-mode-gate

Starting graph SHA-256:
23e7bfacbf6abc5582769fbe8d427cbca2379e1d265b99df21d93a65ec504825

Status: conductor candidate only; no proof state is changed.

## 1. Candidate result

Fix one primitive outer ray \(r=(a,b)\), one physical numerator increment
\(p\), put \(m=a+p\), and write \(b'=b+q\). Along this fixed-\(p\)
progression,

\[
 n=aq-bp,\qquad q={n+bp\over a}.
\]

After physical Mobius reassembly, the stripped primitive support-character
mask has an exact finite Fourier expansion. The displayed moduli below are
valid completion moduli set by the inner numerator \(m\), not generally the
minimal periods and not a factorization of the full weighted physical
coefficient.

For M1, put \(M=|m|_{\rm odd}\), the odd part of \(|m|\). Since
\(\chi_4(b')\) already vanishes for even \(b'\), the arithmetic factor is

\[
 w_{1,m}(q)=\chi_4(b+q)\mathbf 1_{(M,b+q)=1},
\]

which has minimal period \(4\operatorname{rad}(M)\) and admits the valid
completion modulus \(4M\). With normalized transform

\[
 \widehat w_{1,m}(k)
 ={1\over4M}\sum_{q\bmod4M}w_{1,m}(q)
 e\!\left(-{kq\over4M}\right),
\]

one has

\[
 \widehat w_{1,m}(k)
 ={e(kb/(4M))\over4M}\,
 G_{4,M}(k)c_M(k),
\]

where \(c_M(k)\) is the Ramanujan sum and

\[
 G_{4,M}(k)=
 \sum_{x\bmod4}\chi_4(x)
 e\!\left(-{k\over4}\overline M^{(4)}x\right).
\]

Thus \(G_{4,M}(k)=0\) for even \(k\), while
\(|G_{4,M}(k)|=2\) for odd \(k\). In particular,

\[
 |\widehat w_{1,m}(M)|
 =|\widehat w_{1,m}(3M)|
 ={\varphi(M)\over2M}.
\]

The naive M1 zero mode vanishes, but the two physical quarter modes have
natural size. Under \(q=(n+bp)/a\), the modes \(k=M,3M\) become the
frequencies \(1/(4a)\) and \(3/(4a)\) in \(n\), precisely the shifted
M1 carriers. The zero-extended fixed-\(p\) determinant progression admits
the valid completion period \(4|a|M\), and also contains the remaining odd
Ramanujan modes. Its minimal period uses \(\operatorname{rad}(M)\).

For M2, active \(m\) is odd and

\[
 w_{2,m}(q)=
 \epsilon_{\rm sgn}\chi_4(|m|)
 \mathbf 1_{(|m|,b+q)=1}.
\]

It has minimal period \(\operatorname{rad}(|m|)\) and admits the valid
completion modulus \(|m|\), with

\[
 \widehat w_{2,m}(k)
 ={\epsilon_{\rm sgn}\chi_4(|m|)\over |m|}
 e\!\left({kb\over |m|}\right)c_{|m|}(k).
\]

The fixed-\(p\), \(q\)-arithmetic zero coefficient is therefore

\[
 \widehat w_{2,m}(0)
 =\epsilon_{\rm sgn}\chi_4(|m|)
 {\varphi(|m|)\over |m|},
\]

which is generically nonzero and of natural arithmetic density. This is not
the determinant point \(n=0\), which is separately owned and excluded from
the one-sided off-diagonal scalar.

These identities prove a stripped support-mask computation, but not a
factorization or signed estimate for the weighted physical scalar. They also
show that an exact
\(4|a|\)-periodic Fourier expansion of the whole interlaced \(n\)-weight
is unavailable: \(m=a+p\), its primitivity modulus, and its Fourier
period vary with \(p\).

## 2. Exact hypotheses

The calculation uses only:

1. \((a,b)=1\);
2. the physical primitive condition \((m,b+q)=1\);
3. the literal M1 character \(\chi_4(b+q)\), or the literal M2 factor
   \(\epsilon_{\rm sgn}\chi_4(|m|)\);
4. one fixed physical \(p\)-progression.

No threshold, profile, taper, centre phase, or outer coefficient is
placed into the finite Fourier factor. Those terms remain in a separate
incomplete analytic envelope and must be controlled before the expansion
can be used in the full scalar.

Equivalently, after physical reassembly and a subsequent exact divisor
re-expansion, an M1 support component \(\rho\mid m\),
\(\rho\mid b+q\) has period \(\operatorname{lcm}(4,\rho)\) in \(q\),
hence \(|a|\operatorname{lcm}(4,\rho)\) in \(n\). Summing the support
components restores the periods displayed above; it does not factor the
original \(\rho\)-dependent profile, star, or owner data, and it does not
reduce every component to modulus \(4|a|\). For fixed-\(p\) M2 the weakest
divisor-atom determinant modulus is \(|a|\rho\), since there is no
denominator-quarter carrier.

## 3. Derivation

For M1, shift \(x=b+q\). Then

\[
\widehat w_{1,m}(k)
=e(kb/(4M)){1\over4M}
\sum_{\substack{x\bmod4M\\(x,M)=1}}
\chi_4(x)e(-kx/(4M)).
\]

Because \(M\) is odd, the Chinese remainder theorem identifies
\(\mathbb Z/(4M)\) with \(\mathbb Z/4\times\mathbb Z/M\).
The character and coprimality condition live in the two separate factors,
while the additive character factors using inverses of \(M\) modulo \(4\)
and of \(4\) modulo \(M\). The resulting product is the displayed
modulo-\(4\) Gauss factor times \(c_M(k)\). The two values \(x=1,3\)
show directly that the Gauss factor vanishes for even \(k\) and has
magnitude two for odd \(k\). Taking \(k=M\) or \(3M\) gives
\(c_M(k)=\varphi(M)\).

For M2, shifting \(x=b+q\) and summing over the reduced residue classes
modulo \(|m|\) gives the Ramanujan sum directly. At \(k=0\), this is
\(c_{|m|}(0)=\varphi(|m|)\).

The complete Fourier expansion itself costs no fixed power. From

\[
 c_M(k)=\sum_{d\mid(M,k)}d\,\mu(M/d)
\]

one obtains

\[
 \sum_{k\bmod M}|c_M(k)|
 \le \sum_{d\mid M}d\,{M\over d}
 =M\tau(M).
\]

Hence the normalized Fourier \(\ell^1\) mass is \(O_\varepsilon
(Y^\varepsilon)\). This fact licenses a componentwise fixed-\(p\)
expansion, but it supplies no saving because the natural shifted/zero
modes displayed in Section 1 remain.

Finally,

\[
 e(kq/R)
 =e\!\left({k(n+bp)\over aR}\right)
\]

for \(R=4M\) in M1 and \(R=|m|\) in M2. This proves the stated
determinant frequencies and periods.

## 4. First doubtful or unproved step

The first unproved step is not the arithmetic transform. It is a
uniformly useful separation of the complete interlaced \(n\)-weight.

On each fixed-\(p\) progression, the determinant taper and the physically
recombined denominator profile can be BV in the natural \(q\)-order.
But combining the progressions orders \(p\) through the permutation

\[
 p\equiv-\overline b\,n\pmod {|a|}.
\]

A numerator profile with total variation \(O(L^{-1})\) in natural
\(p\)-order can have determinant-order variation \(O(1)\): there are
\(\asymp L\) jumps, each potentially \(O(L^{-1})\). This erases the full
length-\(L\) Abel gain. Conversely, retaining the natural \(p\)-order
returns the product-window resonances already isolated in Round 130.

There is genuine arithmetic cancellation available only under an
unproved envelope hypothesis. Indeed

\[
 {\varphi(m)\over m}=\sum_{d\mid m}{\mu(d)\over d}
\]

and complete multiplicativity of \(\chi_4\) give

\[
 \sum_{m\le x}\chi_4(m){\varphi(m)\over m}
 =\sum_{d\le x}{\mu(d)\chi_4(d)\over d}
   \sum_{k\le x/d}\chi_4(k)
 \ll \log(2x).
\]

Thus a genuinely BV analytic envelope in natural \(m\)-order would
permit the ideal M2 length-\(L\) bank. The literal phase does not satisfy
that hypothesis uniformly. On the same-denominator packet
\(b'=b\), \(m=a-2j>0\), and \(c=(4h+1)b\),

\[
 e\!\left({c(ab'-mb)\over4bb'}\right)=(-1)^j,
 \qquad
 \chi_4(a)\chi_4(a-2j)=(-1)^j,
\]

so the physical carrier cancels the character alternation. This is a
literal per-ray control showing why the arithmetic partial-sum estimate
cannot be applied before the resonant analytic envelope is separated.
It is not a family-level lower bound.

Thus there is no proved simultaneous coordinate in which the numerator
profile has target-scale variation and the reciprocal/residue phase has a
single periodic mode. The required new statement is an actual
family-level correlation across the \(p\)-progressions and outer rays.

## 5. Controls

| Control | Outcome |
|---|---|
| physical Mobius reassembly | Pass only for the stripped support mask: the primitive indicator becomes a Ramanujan factor, while weighted \(\rho\)-dependent profiles and owners are not factorized. |
| naive modulus \(4|a|\) | Fails as an exact full-weight modulus: the inner modulus \(m=a+p\) varies. |
| shifted M1 resonant mode | Nonzero: \(k=M,3M\) have coefficient \(\varphi(M)/(2M)\). |
| M2 zero mode | Nonzero: coefficient \(\epsilon_{\rm sgn}\chi_4(|m|)\varphi(|m|)/|m|\). |
| Salie identification | Fails from this algebra: the exact complete factor is Gauss times Ramanujan, while the analytic phase contains the real reciprocal \(c/(b+q)\), not a modular inverse in a fixed complete sum. |
| same-denominator packet | Consistent: a natural shifted or zero arithmetic coefficient does not force cancellation. |
| scalar versus energy | Pass: no positive energy is introduced. |
| per-ray versus cross-ray capacity | Pass: the formulas are per progression and prove no outer-ray gain. |
| exponent ledger | No bank: \(35/48\) remains; even an ideal per-ray result would stop at \(27/48\). |

The nonzero arithmetic coefficient is not a lower bound for the
corresponding oscillatory incomplete sum.

## 6. Dependencies

This candidate uses the Round-131 statement-only packet and the exact
accepted scopes of:

- GC-W7-16-top-shell-determinant-residue-reindexing;
- GC-W7-16-post-inner-shell-support-refinement;
- GC-W7-16-direct-Stieltjes-birth-block-curvature-lemma; and
- GC-W7-16-post-inner-outer-energy-obstruction.

No external theorem or numerical experiment is used.

## 7. Candidate state effect

If independent reviews confirm the calculation, promote only the exact
fixed-\(p\) primitive arithmetic Fourier kernel and the scoped conclusion
that character periodicity does not produce the required residue saving.

Do not promote a lower bound from the fixed-\(p\) arithmetic \(k=0\)
coefficient: the analytic envelope,
real reciprocal phase, \(p\)-interlacing, and outer-ray sum may still
cancel. If no report proves their correlation, close Round 131 as
degenerate and park the internal graded lane, with the displayed
actual-vector cross-ray matrix coefficient as the first residual.

No complete fixed-block exponent, global exponent, M9 component,
endpoint theorem, bridge, or quarter theorem changes.
