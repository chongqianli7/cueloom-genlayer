# Protocol: cueloom-1

Stable Studionet 61999; RPC https://studio.genlayer.com/api. Constructor takes no arguments. Transactions use full consensus, `leaderOnly: false`, and zero attached value.

## State and permissions

Each reel is keyed by lowercase caller address and a 3–48 character lowercase slug. `seal(slug, raw)` fixes the input and SHA-256 commitment. Only that address can align and publish its reel. Anyone may `read(owner, slug)` or inspect `protocol()`.

`SEALED → ALIGNED → PUBLISHED`, or `SEALED → BLOCKED`. A blocked reel and a published reel are terminal. Input fields are title, source_language, target_language, source and target. Source cues contain start, end and text. Target is an ordered list of strings. Times are nonoverlapping and within one hour; markup, newlines and NUL are excluded.

## Semantic boundary

`align(slug)` enumerates candidates in source-index, target-index, then `(1,1), (1,2), (2,1)` order. It constructs the full concatenated source and target text for every candidate. E means complete meaning equivalence, N means different meaning, U means uncertainty. An independent validator runs the same task and requires exact equality of every label. Malformed output and failed model calls abort the transaction rather than persisting guessed labels.

The original text blocks are retained, so every E can be inspected against its exact input. There are no model-generated rewrites or claimed external sources. Consensus is not proof that a translation is correct.

## Deterministic alignment

The lattice begins at `(0,0)` and ends at `(source length,target length)`. A permitted edge consumes 1 or 2 adjacent units on one side and exactly 1 on the other. Only E edges authorize paths. Every complete path consumes all units once, in order, with no gaps. All complete paths are enumerated; those with the most blocks retain the finest allowed segmentation. Lexicographic edge-index ordering makes path indexes stable. `possible_paths` repeats the computation allowing U solely for diagnostics; it grants no publication rights.

`alignment_hash` commits to the input hash, full label vector and supported paths. `publish(slug, alignment_hash, path_index)` requires the current hash and a valid index in the stored supported paths. It stores the chosen path, WebVTT and its SHA-256 digest atomically. VTT text is assembled from exact target strings, with the outer source times of each block. No later edit or republish is allowed.

The UI verifies deployed source bytes and protocol, then checks finalized receipts and reads state. State reads use `latest-final`. A public example read does not by itself prove a specific transaction. The record export preserves the most recently inspected receipt and pending intent; complete lifecycle receipts are available separately in the repository evidence.
