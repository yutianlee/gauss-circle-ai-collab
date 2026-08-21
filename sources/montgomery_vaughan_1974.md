# Source Card: Montgomery--Vaughan Hilbert inequality

## Bibliographic data

H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*, Journal of
the London Mathematical Society (2) 8 (1974), 73--82.

## URL

- DOI: https://doi.org/10.1112/jlms/s2-8.1.73
- Author-hosted scan:
  https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf

## Exact theorem audited

Theorem 2, equation (1.6), treats a finite family of distinct real
frequencies \(\lambda_r\), real-line separation

\[
 \delta=\min_{r\ne s}|\lambda_r-\lambda_s|>0,
\]

and arbitrary complex coefficients. It gives the Hilbert-kernel estimate
used to deduce

\[
 \int_I\left|\sum_r c_re(\lambda_rt)\right|^2dt
 \leq (|I|+\delta^{-1})\sum_r|c_r|^2
\]

under the project convention \(e(x)=e^{2\pi ix}\). This is the real-line
Theorem 2, not the modulo-one spacing statement in Theorem 1.

## Project use

Round 93 groups equal rational M2 frequencies before applying separation.
The resulting reduced frequencies are distinct and
\(\gg D^{-2}\)-separated, so the theorem applies literally. The blind
Round-93 report also proves the needed continuous inequality
self-containedly by a triangular majorant. Consequently this source is
corroborating evidence, not a graph dependency.

## Audit status

Primary theorem and normalization audited by the Round-93 hostile/source
gate on 2026-08-17.
