# Isolated finite quadratic transform task

Round231 prelaunch admission, 2026-10-11. Statement-only independent analyst. Context is ONLY protocol.md, this statement and your task message; do not read graph, other briefs/reports, history or web. Starting graph identifier (provenance only): a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.

For an arbitrary odd prime p, define e_p(t)=exp(2pi i t/p),

    nu_p(n)=#{(x,y) in F_p^2 : x^2+y^2=n},
    L_p(n)=nu_p(n)/p,
    f_p(n)=L_p(n)-1,
    Q_(a,b)=p^-1 sum_(n modp)L_p(n)e_p(a n^2+b n),
    W_(a,b)=p^-1 sum_(n modp)f_p(n)e_p(a n^2+b n).

Determine exactly Q and W for every a,b, including a=0, both prime congruence classes, and the row Gram matrix sum_b W_(a,b) conjugate(W_(c,b)). Does quadratic demodulation create orthogonal, or parametrically decorrelated, centered arithmetic rows as a varies? Separate any common row component from the remaining matrix, and quantify both (including their row energies and Gram off-diagonals). Identify what additional owner is introduced by deleting a common component. Prove your conclusions from elementary finite-field algebra, treating Gauss-sum phase and normalization explicitly. A finite check on small odd primes is permitted but not required, and not a proof.

No asymptotic theorem about the circle discrepancy is part of this task. Avoid extending a statement about these finite matrices to incomplete arithmetic sums without a proved bridge. Seven protocol sections, exact result or no-go, first gap, diagnostic control, dependency list, scope/state recommendation. Write ONLY strategy/round231_quadratic_signed_admission/reports/blind_quadratic_rows.md. Return its SHA256 and stop.
