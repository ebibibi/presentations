# presentations リポジトリ

胡田昌彦のプレゼンテーション資料管理リポジトリ。Marpを使用してMarkdownからスライドを生成する。

## ディレクトリの種類

### 1. HCCJP勉強会（HCCJP_XX）
- **主催**: ハイブリッドクラウド研究会（複数スピーカー、YouTubeライブ配信）
- **特徴**: オープニング、複数セッション、Q&A、クロージングの構成
- **ロゴ**: `../Images/hcc-logo02f.png` を使用

### 2. 個人勉強会（日付_テーマ名）
- **主催**: 胡田昌彦個人
- **特徴**: 単独発表、シンプルな構成
- **命名規則**: `YYYYMMDD_テーマ名`（例: `20260208_Gemini_VSCode_AIAgentDev`）

## Marpスライドの作成方法

### 基本構造

```markdown
---
marp: true
theme: gaia
paginate: true
backgroundColor: #fff
style: |
  section {
    font-family: 'Meiryo', 'Segoe UI', sans-serif;
    font-size: 36px;
  }
  h1 { color: #0078d4; font-size: 1.6em; }
  h2 { color: #0078d4; font-size: 1.4em; }
---

# タイトル

---

# 次のスライド
```

### スライド区切り

`---` で新しいスライドに分割する。

### クラス指定（スライドごとのスタイル）

```markdown
<!-- _class: lead -->
```

| クラス | 用途 |
|--------|------|
| `lead` | セクションタイトル（大きめフォント） |
| `small` | 情報が多いスライド（28px） |
| `x-small` | さらに小さい（24px） |
| `xx-small` | 最小（22px） |

### 背景画像

```markdown
![bg right:30% 80%](../Images/logo.png)
```

- `right:30%` / `left:30%`: 配置位置と幅
- `80%`: 画像サイズ

### よく使うカスタムCSS

```css
.speaker {
  font-size: 0.85em;
  color: #666;
}
```

スピーカー情報の表示に使用:
```markdown
<span class="speaker">所属・肩書き</span>
```

## 共有リソース

- `Images/`: 複数プレゼンテーションで共有するロゴ等
  - `hcc-logo02f.png`: HCCJPロゴ

## 出力形式

```bash
# HTML出力
npx @marp-team/marp-cli slides.md -o slides.html

# PDF出力（ローカル画像使用時）
npx @marp-team/marp-cli --pdf --allow-local-files slides.md -o slides.pdf

# PPTX出力
npx @marp-team/marp-cli --pptx --allow-local-files slides.md -o slides.pptx

# プレビュー
npx @marp-team/marp-cli --preview slides.md
```

## スライド編集の鉄則

### 毎回読み直してから修正（絶対守れ）

**胡田さんがスライドを手動で同時編集していることがある。** Edit する前に必ず最新の内容を Read で読み直す。古いキャッシュのまま Edit すると胡田さんの手動修正を上書きしてしまう。

```
❌ 悪い例: 読み込み → 修正A → 修正B → 修正C（途中で読み直さない）
✅ 良い例: 読み込み → 修正A → 読み込み → 修正B → 読み込み → 修正C
```

### アスキーアートの整列

日本語を含むアスキーアート図は、文字数ではなく**表示幅**（全角=2, 半角=1）で揃える。検証スクリプトで確認:

```bash
python3 ~/.claude/skills/ascii-art/scripts/check_ascii_art.py slides.md
```

### フォントサイズとテキスト量の目安

| クラス | フォント | 1行の目安（全角） | 行数の目安 |
|--------|----------|-------------------|------------|
| `lead` | 2.2em | ~20文字 | ~4行 |
| `point` | 42px | ~14文字 | ~8行 |
| （なし） | 36px | ~16文字 | ~12行 |
| `small` | 28px | ~21文字 | ~16行 |
| `x-small` | 24px | ~24文字 | ~20行 |

テキストが多い場合はクラスを `small` や `x-small` に変更する。テーブルがあるスライドは `small` 以下を推奨。

## 新規プレゼンテーション作成手順

1. ディレクトリ作成: `mkdir YYYYMMDD_テーマ名`
2. `slides.md` を作成（上記テンプレートを使用）
3. 必要に応じて `images/` サブディレクトリを作成
4. PPTXまたはPDFにエクスポート
