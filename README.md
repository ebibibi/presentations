# Presentations

Marpを使用したプレゼンテーション資料の管理リポジトリです。

## 概要

このリポジトリは、[Marp](https://marp.app/) (Markdown Presentation Ecosystem) を使用して作成された胡田昌彦（ebibibi@gmail.com）のプレゼンテーション資料を管理するためのものです。各プレゼンテーションは独立したディレクトリで管理され、Markdownファイルからスライドを生成します。

## ディレクトリ構成

```
presentations/
├── README.md                 # このファイル
├── presentation-01/          # プレゼンテーション例1
│   ├── slides.md            # Marpスライド（Markdown）
│   ├── images/              # 画像素材
│   └── README.md            # プレゼンテーション概要
├── presentation-02/          # プレゼンテーション例2
│   ├── slides.md
│   ├── images/
│   └── README.md
└── ...
```

## 使い方

### 新しいプレゼンテーションの作成

1. 新しいディレクトリを作成
   ```bash
   mkdir presentation-name
   cd presentation-name
   ```

2. `slides.md`ファイルを作成し、Marp記法でスライドを記述
   ```markdown
   ---
   marp: true
   theme: default
   paginate: true
   ---
   
   # タイトル
   
   発表者名
   日付
   
   ---
   
   # スライド2
   
   内容...
   ```

3. 必要に応じて画像やその他のリソースを`images/`ディレクトリに配置

### スライドのプレビュー

#### VS Code拡張機能を使用する場合

1. [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode)をインストール
2. `slides.md`を開き、プレビューボタンをクリック

#### Marp CLIを使用する場合

最新のCLIの推奨利用方法に合わせて手順を更新しました（Node.js 18+が必要）。PDF / PPTX / 画像出力には Chrome / Edge / Firefox のいずれかのブラウザが必要です。

```bash
# 1) その場だけ使う（推奨）
npx @marp-team/marp-cli@latest slides.md          # HTMLに変換（同名.htmlを出力）
npx @marp-team/marp-cli@latest slides.md -o out.html

# 2) プロジェクトに導入して使う
npm i -D @marp-team/marp-cli
npx marp slides.md -o out.html

# 3) グローバルにインストールして使う（任意）
npm i -g @marp-team/marp-cli
marp slides.md -o out.html

# PDF への変換（ブラウザ必須）
marp --pdf slides.md               # または拡張子で判別: -o slides.pdf
marp slides.md -o slides.pdf

# ローカルファイル（画像等）をPDF/PPTX/画像出力で使う場合の注意
# セキュリティ保護のため既定ではローカルファイル参照がブロックされます。
# 必要な場合のみ --allow-local-files を付与してください。
marp --pdf --allow-local-files slides.md -o slides.pdf

# PowerPoint (PPTX) への変換（ブラウザ必須）
marp --pptx slides.md               # または: -o slides.pptx
marp slides.md -o slides.pptx

# ウォッチ（保存のたびに自動変換）
marp -w slides.md

# プレビューウィンドウを開く（自動ウォッチ有効）
marp --preview slides.md

# サーバーモード（ディレクトリを渡す）
# 例: カレントディレクトリを公開してライブプレビュー
marp -s .
# 必要に応じてポート指定
PORT=5000 marp -s .
```

参考: セキュリティの都合により、ブラウザを使う出力（PDF / PPTX / 画像）ではローカルファイル参照が既定で無効化されています。ローカル資産を使用したい場合のみ `--allow-local-files` を付けてください。

## Marpの主な機能

- **Markdownベース**: シンプルなMarkdown記法でスライドを作成
- **テーマ**: デフォルトテーマの他、カスタムテーマも利用可能
- **エクスポート**: HTML、PDF、PPTXなどさまざまな形式に出力
- **コードハイライト**: プログラミングコードの美しい表示
- **数式サポート**: LaTeX記法による数式の記述
- **画像の自動リサイズ**: Markdown記法で簡単に画像を配置

## 推奨される構成

各プレゼンテーションディレクトリには以下のファイルを含めることを推奨します：

- `slides.md` - メインのプレゼンテーションファイル
- `README.md` - プレゼンテーションの概要、発表日、対象者などの情報
- `images/` - スライドで使用する画像ファイル
- `assets/` - その他のリソース（動画、データファイルなど）

## 参考リンク

- [Marp公式サイト](https://marp.app/)
- [Marp Core Documentation](https://marpit.marp.app/)
- [Marp CLI](https://github.com/marp-team/marp-cli)
- [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode)

## トラブルシューティング（Docker）

- PPTX / PDF で日本語が表示されない
  - 原因: コンテナに日本語フォントが入っていないと、ヘッドレスブラウザ（Chrome）が字形をレンダリングできません。
  - 対応: Dockerfile に日本語フォント（Noto CJK / IPA）と fontconfig、ロケール設定を追加しました。コンテナを再ビルドしてください。
    - VS Code Dev Containers: コマンドパレットから「Dev Containers: Rebuild Container」
    - CLI: `docker build -t presentations:latest .`（使用環境に合わせて）
  - 補足: 画像などローカル資産を含む PDF/PPTX 変換は `--allow-local-files` が必要です（READMEのMarp CLIセクション参照）。
