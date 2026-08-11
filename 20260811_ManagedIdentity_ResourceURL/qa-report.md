# QA report

対象: `マネージドIDのリソースURLを理解する.pptx`

## 構造・表示

- PASS: 18 slides、16:9（1.7778）
- PASS: タイトルスライドに出典URLとロゴ画像あり
- PASS: スライド外にはみ出した要素なし
- PASS: 全ページを画像化して目視し、文字切れ・重なりなし
- PASS: PDFは18ページ

## 事実確認

- PASS: Microsoft LearnおよびAzure SDK公式ソースとの照合で事実誤認なし
- 証跡: `fact-check-pass.log`

## セマンティックレビュー

- PASS: 出典忠実性、視覚的一貫性、物語の流れ、初学者への明瞭さ、登壇時の使いやすさ
- 証跡: `semantic-review.yaml`、`semantic-review-current.md`
- レビュー対象SHA-256: `b29e464ba74abd5ed1b2a1c36c61c6884ec71eb72caadfbba7b38ca6965695a5`

## 人間レビュー

- 未実施（動画収録前の最終読み合わせで実施）
