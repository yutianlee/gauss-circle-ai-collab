# Isolated round222 cross-modulus frequency statement

Read only protocol.md and this statement. Disclose reused-agent history.
No graph, manifest, strategy, application, source or sibling context.
Write seven numbered protocol sections only to
rounds/codex-managed/m9-m2-complete-unbalanced-vector/reports/blind_cross_modulus.md.

Let e(t)=exp(2pi i t), q,r>=2 integers, and A,B any integers, without
coprimality assumptions on A,q or B,r. Define

    S(A,h;q)=sum_(x modulo q, gcd(x,q)=1)
                   e((A inverse(x modulo q)+h x)/q).

Derive the exact complete common-period correlation over
0<=h<lcm(q,r) between S(A,h;q) and conjugate S(B,h;r).
In particular decide whether it vanishes for q!=r and identify the
diagonal in terms of the Ramanujan sum. Prove it directly, including
arbitrary inverse representatives and nonprimitive first arguments.

For any finitely supported complex sequence w(h), derive the exact
weighted correlation using D_w(t)=sum_h w(h)e(ht). Extend this to
different row weights u_q(h),v_r(h) and explain precisely why complete-
period orthogonality need not remain. Include a shifted integer interval
of length H, its exact geometric sum, the zero-frequency case and the
bound min(H,1/(2||t||)) up to a stated absolute constant.

Give an exact near-frequency control on DISTINCT ODD coprime moduli:
take odd q>=3, r=q+2, x=(q+1)/2, y=(r+1)/2. Check that x,y are units
and x/q-y/r=1/(qr). Compute the complete and length-H Gram inner
products of the two simple rows e(hx/q),e(hy/r), and prove a fixed
fraction of H survives when1<=H<=c qr for a sufficiently small
absolute c. These rows are single unit-frequency terms, NOT complete
Kloosterman rows. Do not transfer their lower bound to S(A,h;q) or
to any unspecified arithmetic vector.

Explain what multiplying rows by prescribed unit-modulus signs does
to this two-row Gram spectrum and an all-vector operator norm, and
why that fact alone says nothing about cancellation for a specified
coefficient vector. Empty windows, H=1 and repeated/equal moduli
must be treated explicitly. Zero experiments and no web.

Required output: result; exact hypotheses; proof; first unsupported
application step; exact controls/outcomes; dependencies/provenance;
recommended state effect. Stop after this assigned finite report.
