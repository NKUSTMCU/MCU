# object detect

## 製作動機

影片 : <https://www.youtube.com/watch?v=qj37CkcKWJ8>

交通事故中，常有追撞事件，何況是蓄意。因此有增加此功能之動機。

![image](https://github.com/NKUSTMCU/MCU/blob/master/software/server/Ver1.0/object%20detect/img/sc0.PNG)


![image](https://github.com/NKUSTMCU/MCU/blob/master/software/server/Ver1.0/object%20detect/img/sc1.PNG)


## 方案一 YOLO

在樹梅派加上鏡頭，以辨識後方來車。 
 
![image](https://github.com/NKUSTMCU/MCU/blob/master/software/server/Ver1.0/object%20detect/img/1545844909358.jpg)


 上次遇到未能使用即時影像的問題，後來打算寫一個程式，隔一段時間偵測一次。利用大小來判斷是否有高速接近之車輛，發出警報提早讓駕駛做出反應，讓騎車更安心。

![image](https://github.com/NKUSTMCU/MCU/blob/master/software/server/Ver1.0/object%20detect/img/1545844786149.jpg)

預計程式下次做，驅動的部分再試試看。


### 待解問題

1. 反應時間有點慢，可能下次會用其他輕量化的模型解決。

2. 驅動裝起來後，用即時辨識可能運行會更順暢。



## 方案二 Tensorflow Object Detection API
![image](https://github.com/NKUSTMCU/MCU/blob/master/software/server/Ver1.0/object%20detect/img/t1.PNG)

效果
![image](https://github.com/NKUSTMCU/MCU/blob/master/software/server/Ver1.0/object%20detect/img/t0.PNG)
Vedio : <https://youtu.be/bfkwJfo75A0>


### 待解問題
1. 還是卡~不過快很多了，好像還有救，那就再搶救一下

2. 日後會朝向加GPU的方式解決

## 方案三 google Cloud Vision API
![image](https://github.com/NKUSTMCU/MCU/blob/master/software/server/Ver1.0/object%20detect/img/c0.PNG)
![image](https://github.com/NKUSTMCU/MCU/blob/master/software/server/Ver1.0/object%20detect/img/c1.PNG)

### 待解問題
1. 要信用卡付費繳錢
2. 需要觀眾老爺斗內
3. 有機會做，將朝邊緣運算發展

