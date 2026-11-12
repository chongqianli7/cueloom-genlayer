# CueLoom

[Open the worktable](https://chongqianli7.github.io/cueloom-genlayer/)

**Keep the meaning. Find its timing.** A bilingual subtitle alignment desk for short translations whose sentence boundaries differ from the source cues. Seal two tracks, inspect independently checked block relationships, publish a complete alignment and download the resulting WebVTT.

## What it does

A source says “Bring your own paper” and then “Ink is provided free of charge.” The translator joins both sentences into one Chinese line. Pairing by line number would leave a cue behind. CueLoom can join the two consecutive source cues into one translated cue while retaining their outer time boundaries. Removing the ink detail makes that match unsupported and blocks publication.

The guided example is an authored fixture with fixed labels; it makes no model calls. The on-chain worktable submits the actual input to an Intelligent Contract and reads its persisted result.

## Use

1. Explore **Guided example**, including **Remove the ink detail**.
2. Choose **On GenLayer → Read published example** to inspect a public finalized reel without a wallet.
3. For your own reel, connect an injected EVM wallet on Stable Studionet 61999, or use a disposable **browser test signer**. The latter keeps a test private key in browser local storage; never use it for assets.
4. Choose **Use signer as owner**, enter a new reel ID and edit the JSON tracks. Source cues use integer milliseconds. Each track accepts 1–4 units, each at most 240 plain-text characters.
5. **Validate draft → Seal two tracks → Recheck transaction**. After finalized successful execution and matching readback, choose **Compare & align**, then recheck again.
6. Inspect all semantic comparisons and the complete path. If more than one finest supported path exists, select one. **Publish selected path**, recheck, then **Download WebVTT** or export the record with its receipt.

Recheck never sends a transaction. Pending intent survives reload. An uncertain wallet response remains blocked until its exact hash is recovered; an explicit rejected signature releases the guard. Successful finality requires majority agreement, successful execution, receipt sender/contract/calldata identity and matching stored state. Once complete, the pending guard clears so another reel can be created.

## Why GenLayer

Source timing and target text are immutable inputs shared by collaborators. Leader and validators independently compare every candidate 1:1, 1:2 and 2:1 block, including candidates outside the selected path. Equivalence requires exact agreement on the complete E/N/U vector. Contract code then finds complete monotone paths, retains those with the largest number of blocks and permits publication only from that set. The model cannot skip a difficult line, reorder a track, invent timing or replace the translation.

A centralized editor can propose an alignment. CueLoom adds a shared independent acceptance boundary and enforces the resulting publication constraints in contract state. It cannot guarantee linguistic truth or honest source material.

## Boundaries

All text is public, including unpublished inputs. Do not submit private, confidential or unlicensed material. This is a bounded short-segment tool: no audio/video upload, transcription, translation generation, professional translation certification, speech synchronization, reading-speed checks or support for 2:2 and larger blocks. Merged cues inherit the first source start and last source end, including any gap. Check audiovisual timing and readability in a subtitle editor. A blocked input is immutable; corrected text needs a new reel ID. There is no global cap on the number of reels per owner.

## Build and test

Node.js 22+, Python 3.12+. `npm ci`, `npm test`, `python tests/contract_test.py`, `npm run build`. Serve `dist/` as static content; `docs/` contains the GitHub Pages build. No server, paid API key or backend-held user key is required. Local contract tests use a mocked host and model; live consensus is recorded separately in [EVIDENCE.md](EVIDENCE.md).

[Contract](contracts/cueloom.py) · [Protocol](PROTOCOL.md) · [Deployment](deployment.json) · [Evidence](EVIDENCE.md)
