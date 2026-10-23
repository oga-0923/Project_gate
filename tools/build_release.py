#!/usr/bin/env python3
"""開発用の dev.html から、一般公開用の index.html（ユーザー画面のみ）を作る。

使い方：python3 tools/build_release.py
- dev.html の `const BUILD = 'dev';` を `'release'` に書き換えて index.html に保存する
- release では設定画面に「ユーザー／開発者」の切り替えが出ず、開発者機能はすべて無効になる
- index.html は毎回この方法で作り直すので、直接編集しない（編集は dev.html で行う）
"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
src = (root / 'dev.html').read_text(encoding='utf-8')
marker = "const BUILD = 'dev';"
if src.count(marker) != 1:
    raise SystemExit('dev.html に BUILD の行が見つかりません')
out = src.replace(marker, "const BUILD = 'release';")
out = out.replace('<html lang="ja">', '<html lang="ja">\n<!-- 自動生成ファイル：編集は dev.html で行い、tools/build_release.py で作り直す -->', 1)
(root / 'index.html').write_text(out, encoding='utf-8')
print('index.html を作成しました（release）')
