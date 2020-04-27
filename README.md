# My_OBS_Script

## 概要
自作のOBS Studioで使用できるスクリプト

## ファイル説明
timeUpdate …… 特定のテキストソースを現在時間に更新するスクリプト

## 導入方法(Windows 64bit)
### 1.Pythonをインストール＆設定
#### 1.1 Pythonをインストール
以下のURLからWindows x86-64 embeddable zip fileをダウンロードし、  
適当なディレクトリに設置する。  
https://www.python.org/downloads/release/python-368/  
  
#### 1.2 OBS側にてPythonへのパスを設定する
メニューからTools(ツール)->Scripts(スクリプト)をクリック  
Python Settings(Pythonの設定)タブのBrowse(参照)をクリック [^1]  
設置したディレクトリを選択  
念のためOBSを再起動する  
[^1]: Python Install Pathの設定  

### 2.スクリプトの導入
#### 2.1 スクリプトファイルの設置
以下のディレクトリにファイルを置く  
<OBS Studioインストールディレクトリ>\data\obs-plugins\frontend-tools\scripts  
  
#### 2.2 OBSでのスクリプトを追加
メニューからTools(ツール)->Scripts(スクリプト)をクリック  
Scripts(スクリプト)タブの「＋」をクリック  
設置したファイルを選択  

