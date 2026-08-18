# QA report — Active Directory入門 2026年版 Part 1

## Structural QA: PASS

- 38 slides / 38 PDF pages
- 16:9 (`1.777733`)
- No shapes outside slide bounds
- Title slide contains the Ebi logo and original YouTube source URL
- Dark navy background; red is limited to the deletion warning element
- Final PDF and contact sheet regenerated from the final PPTX

## Fact QA: PASS

- Final slide-text SHA-256: `ee4dc9989b67789597bb094b0bf37c45502f0cf2117527267ceec8aaa534f1d6`
- Checked against the official Microsoft sources in `source_facts.md`
- Final targeted reruns: `事実誤認なし。`
- Important corrections include the role of CredSSP, DNS/DC Locator, site topology, Recycle Bin, FSMO, Global Catalog, and the 2026 Kerberos/LDAP transition

## Semantic QA: PASS

The independent review in `semantic-review.yaml` passed all five gates:

- source faithfulness
- Japanese clarity
- taxonomy challenge
- first-time teachback
- presenter usability

The reviewed SHA-256 matches the final slide text.

## Static visual review: PASS

- All 38 rendered slides were reviewed in sequence without speaker notes or audio
- No visible clipping, overlap, missing glyphs, or unreadable headline was found
- Detailed review covered the title, classification, GPO, Kerberos, FSMO, Global Catalog, 2026 changes, security transition, concept map, and source slides

## Human review: NOT YET PERFORMED

Before recording, perform one final full-screen run-through in the actual capture environment. The recording policy is BGM-free.
