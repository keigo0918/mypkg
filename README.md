# ros2_ws

[![test](https://github.com/keigo0918/ros2_ws/actions/workflows/test.yml/badge.svg)](https://github.com/keigo0918/ros2_ws/actions/workflows/test.yml)

このリポジトリは千葉工業大学先進工学部未来ロボティクス学科2023年度ロボットシステム学の講義にて作成したリポジトリです。

# talker
# listener
![test]

## ダウンロード

```
$ git clone https://github.com/keigo0918/ros2_ws.git
```

```
$ cd ros2_ws
```

## 実行手順と実行結果

*talkerの使い方
単体で動作させる際は、下記のコマンドを打ち込んでください。
```
$ ros2 run mypkg talker
#画面には何も表示されません
```

*listenerの使い方
単体で動作させる際は、下記のコマンドを打ち込んでください。
```
$ ros2 run mypkg listener
[INFO] [1703314540.253223410] [listener]: Listen: 0
[INFO] [1703314540.732753899] [listener]: Listen: 1
[INFO] [1703314541.231645432] [listener]: Listen: 2
・・・
```

*launchの使い方
```
$ ros2 launch mypkg talk_listen.launch.py 
[listener-2] [INFO] [1703315431.311982248] [listener]: Listen: 0
[listener-2] [INFO] [1703315431.792204733] [listener]: Listen: 1
[listener-2] [INFO] [1703315432.292378318] [listener]: Listen: 2
・・・
```



## テスト環境

* Ubuntu 22.04

## ライセンス

* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを本人の許可を得て自身の著作として改変したものです.
  * [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)

© 2023 Keigo Shishido  
