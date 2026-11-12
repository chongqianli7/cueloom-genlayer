# Network evidence

Stable Studionet, chain ID 61999. [Contract](https://explorer-studio.genlayer.com/address/0x156876241289D62940B5a45677140E292DB6F3A6). The deployed source was retrieved with `getContractCode` and matched `contracts/cueloom.py` byte for byte. `protocol()` returned `cueloom-1`.

Deployment and authored example inputs are listed in [deployment.json](deployment.json). Raw transaction receipts are retained as gzip-compressed JSON in `evidence/`; decompress without altering their contents. These are authored subtitle examples, not evidence of a real film or professional translation. Majority agreement does not establish linguistic certainty or unanimous voting.

Local validation: eight Python mocked-host tests and four JavaScript tests. Tests cover complete ordered coverage, merging, uncertainty, missing text, reversal, unused-cell validator disagreement, owner/hash/path guards, terminal publication and timing/markup checks. They do not execute GenVM or live inference. `npm run build` succeeds; the generated JavaScript bundle exceeds Vite's advisory 500 kB chunk threshold.
