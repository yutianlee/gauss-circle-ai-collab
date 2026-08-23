# Round 115 blind statement

Let \(L\ge 16\), let \(R\asymp L^3\), and let \(K/L\) lie in a fixed
compact interval. Let \(A(h,k)\) be a real smooth coefficient supported
on \(h\asymp L\), \(k\asymp K\), with uniformly bounded rescaled
derivatives. Put

\[
 a(h,k)=\chi_4(h)\,
 \eta\!\left({(h,k)\over \sqrt L/2}\right)A(h,k).
\]

The object supplied for independent analysis is

\[
 E_{\rm df}=
 \sum_{|r|>L}\sum_n e\!\left(R(\sqrt n-\sqrt{n+r})\right)
 \!\!\sum_{\substack{hk=n,\ h'k'=n+r\\|hk'-h'k|>L}}
 a(h,k)\overline{a(h',k')}.
\]

All variables are positive integers in the displayed support. The two
excluded corridors \(|r|\le L\) and \(|hk'-h'k|\le L\) have already been
proved to cost \(O_\varepsilon(L^3X^\varepsilon)\); do not count them as a
new saving. The required bound is

\[
 |E_{\rm df}|\ll_\varepsilon L^3X^\varepsilon.
\]

Derive independently:

1. the exact divisor-pair expression after setting \(k=n/h\) and
   \(k'=(n+r)/h'\), including the determinant gate;
2. the exact increment expression after setting \(h'=h+p\),
   \(k'=k+q\), including \(r\), the determinant, and
   \(\chi_4(h)\chi_4(h+p)\);
3. every zero-frequency or nonoscillatory main term in any proposed
   noninvertible transform;
4. the capacity of each branch at \(R\asymp L^3\).

An exact no-go or equal-capacity result is acceptable. Do not assume the
character creates cancellation after it has become constant on a shift,
and do not cite a generic shifted-divisor theorem without matching its
weight, conductor, shift range, and norm.
