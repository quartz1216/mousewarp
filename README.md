# MouseWarpについて
![](icon.ico)

[**Mousewarp V3 for Windowsをダウンロード**](https://github.com/quartz1216/mousewarp/releases/download/V3/mousewarp.exe) 

署名してないからダウンロード時と起動時に警告が出ると思います。信用できなかったらコード見るか、自分でビルドしてちょ


このプログラムは、Alt+Tabでウィンドウを切り替えた時、切り替え先のウィンドウの中心にカーソルを移動させる、ユーティリティです。
3画面以上のマルチモニターでマウスの移動距離が長い場合に便利かも?

自分用に作ったよ

## 開発用の環境構築(自分用メモ)(同じ手順でビルドできるよ)

リポジトリをクローン
`git clone https://github.com/quartz1216/mousewarp.git`

Pythonの仮想環境の構築
`python -m venv mousewarp`

仮想環境の有効化
`.\mousewarp\Scripts\Activate.ps1`

pyinstallerのインストール
`pip install pyinstaller`

pywin32のインストール
`pip install pywin32`

.exeファイルのビルド
`pyinstaller .\mousewarp.py -F -w --add-data "icon.ico;." --add-data "icon.ico;." --clean --icon=icon.ico --hidden-import plyer.platforms.win.notificationo`


# About MouseWarp
![](icon.ico)

[**Download Mousewarp V3 for Windows**](https://github.com/quartz1216/mousewarp/releases/download/V3/mousewarp.exe) 

Maybe it is not signed, so you may get a warning when downloading or starting. If you don't trust it, look at the code or build it yourself.


This program moves the mouse cursor to the selected window when AltTab is pressed.


## Setup Dev Environment (Note)

Clone this Repository
`git clone https://github.com/quartz1216/mousewarp.git`

Add python venv
`python -m venv mousewarp`

Activate venv
`.\mousewarp\Scripts\Activate.ps1`

install pyinstaller
`pip install pyinstaller`

install pywin32 
`pip install pywin32`

Build execute file
`pyinstaller .\mousewarp.py -F -w --add-data "icon.ico;." --add-data "icon.ico;." --clean --icon=icon.ico --hidden-import plyer.platforms.win.notificationo`
