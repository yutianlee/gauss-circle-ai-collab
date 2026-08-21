# Round 99 conductor review: normalization and local controls

## Normalization

The conductor reproduced the trace opening directly.  The outer \(M\) in
\(\mathfrak T_M\) changes \(M^{-5}\) to \(M^{-4}\), and the four normalized
physical rows contribute exactly four factors \(M^{-1}\).  No report is
allowed to credit another modulus power after opening the trace.

The accepted capacity and target are

\[
 \mathsf C_{\rm Gram}={U\over B}B^6T^4Q^{-5/6},\qquad
 \mathsf T_{\rm Gram}={U\over B}J^{14/5}.
\]

Their ratio is \(J^{11/15}B^{-6}\), equal at
\(B=J^{3/20}\) to \(J^{-1/6}=B^{-10/9}\).  The discovery, hostile, and
statement-only reports all use this target normalization.

## Change of variables

With \(r=n+d+u\), \(s=m+d\), direct expansion gives

\[
 ux+dV+nA-mB_2
 =rx+n(A-x)+s(V-x)+m(x-V-B_2).
\]

The inverse map is \(d=s-m\), \(u=r-s+m-n\), so the lattice Jacobian is one.
This reproduces all four actual rows without discarding an alias, sign,
reflection, or support convention.

## Two-adic control

For odd \(x\) modulo \(8\), \(\bar x=x\).  When all four shifted points are
units, \(A,B_2,V\) are even and

\[
 \Phi(x)\equiv A-B_2\pmod8.
\]

Thus

\[
 \mathfrak T_8=8e_8(K(A-B_2))c_8(u).
\]

The conductor checked \(c_8(0)=4\), \(c_8(4)=-4\), and all other parity
bands vanish.  The nonzero \(u=4\) mode is therefore retained after the one
global \(u=0\) owner.  It is an exact coherent local mode but does not by
itself give a lower bound for the global actual vector.

## Verdict

The normalization, lattice map, and \(q=8\) control pass.  The Frobenius
\(B^{-1}\) versus \(B^{-10/9}\) comparison is retained only conditionally,
because no report proves comparable nonzero archimedean entries on a dense
literal hard block.
