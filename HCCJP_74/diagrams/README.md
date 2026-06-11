# 図の再現方法

アーキテクチャ図・ネットワーク図は SVG を Python(cairosvg) で描画し PNG 化している。
AI 生成イラストではなく決定論的なベクター作図なので、構成変更時はスクリプトを直して再生成する。

```bash
pip install cairosvg pillow   # Noto Sans CJK JP フォントが必要
python3 diagrams/build_arch.py   # -> images/arch.png
python3 diagrams/build_net.py    # -> images/net.png
```

- `build_arch.py` … 3層アーキテクチャ図（L0/L1/L2 + 制御VM + 経路）
- `build_net.py`  … バス型ネットワーク図（CtrlNAT / LabNAT、L1=デュアルホームのルータ）

正本の値は hyperv-nestlab の README / docs/access-guide.md（接続マトリクス）に紐づく。
