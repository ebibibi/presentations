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
  h1 {
    color: #0078d4;
    font-size: 1.6em;
  }
  h2 {
    color: #0078d4;
    font-size: 1.4em;
  }
  h3 {
    font-size: 1.2em;
  }
  .speaker {
    font-size: 0.85em;
    color: #666;
  }
  table {
    font-size: 0.75em;
  }
  th {
    background-color: #0078d4;
    color: white;
  }
  code {
    font-size: 0.9em;
  }
  li {
    font-size: 0.95em;
  }
  /* コンテンツが多いスライド用のクラス */
  section.small {
    font-size: 28px;
  }
  section.small h1 {
    font-size: 1.3em;
  }
  section.small h2 {
    font-size: 1.1em;
  }
  section.small code {
    font-size: 0.85em;
  }
  /* さらに小さいスライド用のクラス */
  section.x-small {
    font-size: 24px;
  }
  section.x-small h1 {
    font-size: 1.2em;
  }
  section.x-small h2 {
    font-size: 1.0em;
  }
  section.x-small code {
    font-size: 0.6em;
  }
  section.x-small li {
    font-size: 0.9em;
  }
  /* さらにほんの少し小さいスライド用のクラス */
  section.xx-small {
    font-size: 22px;
  }
  section.xx-small h1 {
    font-size: 1.2em;
  }
  section.xx-small h2 {
    font-size: 1.0em;
  }
  section.xx-small code {
    font-size: 0.6em;
  }
  section.xx-small li {
    font-size: 0.88em;
  }
  /* leadクラス用の大きめのフォント */
  section.lead h1 {
    font-size: 2.0em;
  }
  section.lead h2 {
    font-size: 1.6em;
  }
  section.lead .speaker {
    font-size: 1.0em;
  }
---

<!-- _class: lead -->

![bg right:30% 80%](../Images/hcc-logo02f.png)

# HCCJP 第65回勉強会

## ハイブリッドクラウド研究会

**2025年9月12日（金）14:00開始**

---

# 本日のテーマ

## 📦 ファイルサーバー運用の新時代！<br>Azure FilesとArc拡張の最前線

- Azure Files 最新アップデートと活用ポイント
- Arc拡張対応で進化した Azure File Sync 管理（GA）
- Kerberos認証と Entra ID Kerberos によるハイブリッド展開
- Microsoft "Adaptive Cloud" 最新動向

---

<!-- _class: lead -->

![bg right:30% 80%](../Images/hcc-logo02f.png)

# オープニング

**司会：胡田 昌彦**
<span class="speaker">日本ビジネスシステムズ株式会社<br>Microsoft MVP for Azure Hybrid, Windows Server</span>

---

# タイムテーブル

| 時刻 | 時間 | セッション | スピーカー |
|------|------|------------|------------|
| 14:00 | 5分 | オープニング | 胡田 昌彦 |
| 14:05 | 40分 | ファイルサーバー運用の新時代！Azure FilesとArc拡張の最前線 | 胡田 昌彦（日本ビジネスシステムズ / Microsoft MVP） |
| 14:45 | 10分 | Q&A | 匿名で何でも質問できます！ |
| 14:55 | 20分 | Microsoft "Adaptive Cloud" Updates | 高添 修 氏（日本マイクロソフト） |
| 15:15 | 10分 | Q&A | 何でも質問できます！ |
| 15:25 | 5分 | クロージング | 胡田 昌彦 |

---

![bg right:20% 60%](../Images/hcc-logo02f.png)

# HCCJPとは

## ハイブリッドクラウド研究会

- 毎月第2金曜日 14時から開催
- Azure + ハイブリッドクラウド関連の最新情報をお届け
- オンライン配信（YouTube HCCJPチャンネル）

📺チャンネル登録お願いします！
https://www.youtube.com/channel/UCrf4bEl7yJnkGYo3F67gA7w

---

# 本日の注意事項

- 📹 配信は録画されています（アーカイブ視聴可）
- 💬 質問・コメント大歓迎！
- 📝 Q&Aセッションでまとめてお答えします

---

<!-- _class: x-small -->

# 質問・コメント方法

## 💬 YouTubeチャットで質問・コメント大歓迎！

- 右側のライブチャット欄から投稿してください
- セッション中でもお気軽にどうぞ
- 固定コメントに各種リンクを掲載します

---

<!-- _class: lead -->

# セッション①

## ファイルサーバー運用の新時代！<br>Azure FilesとArc拡張の最前線

**スピーカー：胡田 昌彦**
<span class="speaker">日本ビジネスシステムズ株式会社<br>Microsoft MVP for Azure Hybrid, Windows Server</span>

⏱️ 14:05 - 14:45（40分）

---

<!-- _class: lead -->

# Q&Aセッション

## 💬 質問にお答えします！

- どんな質問でも大歓迎です

⏱️ 14:45 - 14:55（10分）

---

<!-- _class: lead -->

# セッション②

## Microsoft "Adaptive Cloud" Updates

**スピーカー：高添 修 氏**
<span class="speaker">日本マイクロソフト株式会社</span>

⏱️ 14:55 - 15:15（20分）

---

<!-- _class: lead -->

# Q&Aセッション

## 💬 質問にお答えします！

- どんな質問でも大歓迎です

⏱️ 15:15 - 15:25（10分）

---

<!-- _class: lead -->

![bg left:28% 82%](../Images/hcc-logo02f.png)

# クロージング

## 本日のご参加ありがとうございました！

- アーカイブはYouTubeチャンネルから視聴可能
- 資料は後日公開予定
- ハッシュタグは **#HCCJP**

---

<!-- _class: lead -->

# 次回予告

## 📅 2025/10/10 14:00〜

# Microsoft Connected Cache
WSUSを使わないWindows Update配信で使える新キャッシュサービス！

最新情報は YouTube チャンネル・X（旧Twitter）でお知らせ！
https://www.youtube.com/channel/UCrf4bEl7yJnkGYo3F67gA7w

---

<!-- _class: lead -->

![bg left:28% 82%](../Images/hcc-logo02f.png)

# ご参加ありがとうございました！

## また次回お会いしましょう！

📧 お問い合わせ: ebibibi@gmail.com

