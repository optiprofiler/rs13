# Third-Party Notices

## RS13 problem sources

`runtime/rs13pm/` contains the 502 Python problem drivers from the official
`rs13pm.zip` archive for the Rios-Sahinidis 2013 derivative-free optimization
test collection.

- Upstream archive: `rs13pm.zip`
- Download URL:
  `https://minlp-downloads.nyc3.cdn.digitaloceanspaces.com/testlibs/dfolibs/rs13pm.zip`
- Retrieved: 2026-07-19
- Archive SHA-256:
  `6ffd60081bf376ea25549f4c5a1a4e24721d44a14efac8ec09df1d7308031c31`
- Vendored files: 502 Python problem drivers
- Original project pages:
  `https://sahinidis.coe.gatech.edu/dfo` and
  `https://minlp.com/black-box-optimization-test-problems`

The archive did not contain a standalone license or per-file license headers.
Professor Nikolaos V. Sahinidis confirmed by email on 2026-06-27 that the
RS13 collection is in the open domain and may be used in the OptiProfiler
integration described to him. The vendored files are preserved as received;
the adapter parses them without importing or requiring BAM.

Please cite:

L. M. Rios and N. V. Sahinidis, *Derivative-free optimization: A review of
algorithms and comparison of software implementations*, Journal of Global
Optimization, 56, 1247-1293, 2013.
https://doi.org/10.1007/s10898-012-9951-y

The separate `rs13sols.zip` known-solution oracle and `problemdata.zip` audit
records are not included in this repository or distribution.
