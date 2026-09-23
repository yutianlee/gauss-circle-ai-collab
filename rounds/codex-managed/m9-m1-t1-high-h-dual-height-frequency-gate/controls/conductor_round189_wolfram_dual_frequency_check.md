# Round 189 bounded Wolfram diagnostic

- Status: PASS (diagnostic only; no asymptotic theorem evidence)
- Script SHA-256:
  `481e7054cce6ad9922f818ff33d11c77265c653608acccbb380a804f34870fff`
- Wolfram engine: local `wolframscript`

The repaired exact finite check covered 3,420 tuples with odd
\(3\le q\le19\), odd \(m\in\{1,3,5\}\), \(U=mq\mid u\), selected
terminal and interior heights \(Y>m\), and all unit numerators. On the
complete interval of \(u\) consecutive integers, no instance exceeded
the deliberately loose bound \(2um/Y\) (rounded upward) for

\[
 \#\{v:(u,v)=1, |a\bar v|_q\le\lfloor mq/Y\rfloor\}.
\]

For every tested odd \(q\le31\) and unit \(b\), the diagnostic also
verified to 99-digit working precision

\[
 K_q(b)=\frac1q\sum_{d\mid q}\mu(q/d)dE_d(b).
\]

The original \(m=1\) normalization was sharpened before task restart:
the exact Fourier weight is \(m^{-1}c_q(a)\), so the maximal
coefficient-insensitive threshold is \(mq/Y=U/Y\), not \(q/Y\).

Finally, for primes
\(5,7,11,13,17,19,23,29,31\), the slope \(b=-2\) gave the exact
prefix sum \(-(p-1)/2\) over \(1\le h\le(p-1)/2\).  This falsifies a
uniform polylogarithmic prefix claim.  It does not prove literal mass,
the slow-sector estimate, or the Round-188 complement target.
