# デモ用 Web ページ（HCCJP 第76回）

当日「壊す」対象になる 1 枚ペラ。**Windows か Linux かが一目で分かる**ことを最優先にしている
（配信画面で見た人が、どちらのサーバーの話をしているか迷わないため）。

| ファイル | 配置先 | 見た目 |
|---|---|---|
| `windows.html` | arcwin01 (IIS) → `C:\inetpub\wwwroot\index.html` | **青系**・Windows ロゴ風タイル・「Windows Server 2025」 |
| `linux.html` | arclnx01 (nginx) → `/var/www/html/index.html` | **オレンジ系**・Ubuntu の輪っか風・「Ubuntu 24.04 LTS」 |

どちらも「これは **オンプレミス** で動いている〜」の一文と、`SERVICE ONLINE` の緑ランプ（脈打つ）、
ホスト名 / Web サーバー / IP / Azure Arc の状態を出す。右下の時計は 1 秒ごとに動くので、
**キャッシュされた静止画ではなく今その瞬間に生きている**ことが画面だけで分かる。

外部リソースをひとつも参照していない（フォントも画像も CDN も使わない）。壊れた状態からの
復旧デモ中にネットワークがどうであっても、見た目が崩れない。

## 配布

```bash
./deploy.sh            # 両方
./deploy.sh windows    # Windows だけ
./deploy.sh linux      # Linux だけ
```

**配布は Azure Arc の Run Command 経由**で行う。SSH も RDP も使わない
（当日デモで見せる「誰もログインせずに操作する」経路を、そのまま準備にも使っている）。
Linux 側は nginx が無ければ導入する。Windows 側は既定ドキュメントの先頭に `index.html` を
差し込み、80/tcp を開ける。何度流しても同じ状態に収束する（冪等）。

前提: `az` が Azure MVP サブスクリプションにサインイン済みで、実行者に
`Azure Connected Machine Resource Administrator` 以上があること
（オンボード用サービスプリンシパルは最小権限なので、この操作はできない）。

## 実装メモ

- HTML は **base64 にしてから** Run Command へ渡す。生の HTML を埋め込むと、クォート・改行・
  日本語が bash / PowerShell / Azure の各層のどこかで壊れる。
- ペイロード（`deploy-windows.ps1` / `deploy-linux.sh`）は**別ファイル**にして、置換するのは
  `__HTML_B64__` だけにしている。シェルの変数展開でスクリプト本体が壊れるのを防ぐため
  （`$_` や `$(...)` がある PowerShell を bash の二重引用符に埋めると確実に壊れる）。
- `run-command create` は **PUT（upsert）**なので、同名が残っていてもそのまま上書きできる。
  先に `delete` すると、削除完了前に create のポーリングが走って `ResourceNotFound` で落ちる。

## 検証（2026-08-05 実測）

L1（Nested ホスト）から LabNAT 越しに取得し、**配信元のバイト列が原本と一致**することを確認済み。

```
arcwin01  HTTP 200  5795 bytes  sha256=602f811461343a3e...   (原本 windows.html と一致)
arclnx01  HTTP 200  5890 bytes  sha256=14fb455ac56203b1...   (原本 linux.html と一致)
```
