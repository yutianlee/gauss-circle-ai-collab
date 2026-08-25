# Round 158 barrier packet

- Campaign: m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate
- Starting graph: 3acbfaf6fb95047babd19800dee4152fb60cb408197a8ceac93931a20c57491f
- Allocation: 100% analytic, algebraic, and primary-source work; 0%
  numerical

## Frozen open object

For \(q=4N\), \(c=q/d\), \(H=c/2\), and every odd \(d\mid N\), the
paired interior matrix is

\[
\begin{aligned}
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c
 \sum_{\substack{v\bmod H\\v\ne0,H/2}}
 \widehat B_j(2dv)K(-v^2,-j;c).
\end{aligned}
\tag{158.B1}
\]

Round 158 isolates only the moving-mask Abel trace in (158.B1). The
remaining profile-bulk differences are outside the target and remain
open even if the trace closes.

## Accepted closed controls

1. Complete \(v\)-resummation returns the physical quotient selector.
2. The entire \(v=0\) row is target-safe.
3. The unique \(v=H/2=N/d\) Nyquist row is target-safe.
4. The nonzero projection is centered by exactly \(1/(4N)\).
5. Complementary interior coefficients add and are not conjugates.
6. The selected support count is
   \(L(V)\ll_\varepsilon\min(M,V)X^\varepsilon\).
7. One-variable BV does not imply the required mixed absolute norm.
8. Ordinary centered completion, separated fixed-frequency placement,
   Fourier-\(L^1\), sampled Parseval, and generic nuclear transfer retain
   positive powers.
9. Current fixed-modulus and modulus-average sources do not directly
   match the full entrywise paired matrix.

## Exact trace that must be retained

For \(B_j(x)=\mathbf 1_{x\ge\lambda_\sigma(j)}F_j(x)\), with
\(\lambda_+(j)=j+1\) and \(\lambda_-(j)=-j\), use prefix Abel on the
positive block and suffix Abel on the negative block. The cell trace is

\[
\begin{aligned}
 \mathcal C_{+,d}
 &=\sum_jF_j(j+1)
 \sum_{\substack{v\bmod H\\v\ne0,H/2}}
 e_c(-2v(j+1))\sum_{s\le j}K(-v^2,-s;c),\\
 \mathcal C_{-,d}
 &=\sum_jF_j(-j)
 \sum_{\substack{v\bmod H\\v\ne0,H/2}}
 e_c(2vj)\sum_{s\ge j}K(-v^2,-s;c),
\end{aligned}
\tag{158.B2}
\]

with the exact signed-block endpoints printed in every report.

Full-frequency inversion turns (158.B2) into

\[
\begin{aligned}
 \mathcal C_+^{\mathrm{full}}
 &=\sum_jF_j(j+1)\sum_{s\le j}G_N((j+1)^2-s),\\
 \mathcal C_-^{\mathrm{full}}
 &=\sum_jF_j(-j)\sum_{s\ge j}G_N(j^2-s).
\end{aligned}
\tag{158.B3}
\]

The zero and Nyquist trace pieces must be bounded separately before
(158.B3) can replace the paired-interior trace.

## Frozen false gains

- The endpoint polynomials \(j^2+j+1\) and \(j^2-j\) represent only
  \(s=j\), not the strict prefix or suffix.
- \(N^\varepsilon\)-scale endpoint root multiplicity does not bound the
  whole trace.
- One selected residue \(s\) per fixed \(j\) does not imply cancellation
  over \(j\).
- The unsigned support count is not a signed square-root theorem.
- A target bound for a whole zero or fold row does not automatically
  bound an individual Abel piece.
- Full-frequency inversion is an identity, not a gain.
- A trace theorem does not close the profile bulk or the full paired
  matrix.

## Required controls

- arbitrary \(N\), every odd \(d\mid N\), \(c=4N/d\), and \(c=4\);
- both signed blocks and the exact prefix/suffix orientations;
- strict dyadic endpoints and all Abel boundary terms;
- exact complex residual phase and zero-extended profile transitions;
- zero and Nyquist trace subtractions;
- both complementary interior representatives;
- exact p-adic endpoint root tables, including \(p=2,3\);
- selected-coordinate uniqueness and unsigned-versus-signed scope;
- all restored \(N,M,V,d,c\) powers;
- primary-source hypotheses; and
- external scalar and downstream quarantine.

## Stop rule

Close only as paired_interior_cell_trace_target,
strict_paired_interior_cell_trace_range, or
paired_interior_cell_trace_no_go. A rigorous proof that the polynomial
endpoint route leaves a strict trace survivor is useful progress.
