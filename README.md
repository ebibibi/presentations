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

```bash
# インストール
npm install -g @marp-team/marp-cli

# HTMLへの変換
marp slides.md -o slides.html

# PDFへの変換
marp slides.md -o slides.pdf

# サーバーモードで起動（ライブプレビュー）
marp -s slides.md
```

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
