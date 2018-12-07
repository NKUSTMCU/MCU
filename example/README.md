# HC-SR04 example

## 接線
HC-SR04 VCC接pin2(+5V)，GND接pin6(GND)

HC-SR04 Trig/TX接Pin16(GPIO23)，Echo/RX接Pin18(GPIO24)



## HC-SR04有4個pin腳，說明如下：
VCC：接電源（範圍2.4V~5.5V）。

Trig/TX：UART 模式下，接外部電路UART 的TX 端；為GPIO模式時，為訊號發送端 Trigger。

Echo/RX：UART 模式下，接外部電路UART 的RX 端；為GPIO模式時，為訊號接收端 Echo 。

GND：接地。

## test
去同學家好不容易才借到螢幕
![image](https://github.com/NKUSTMCU/MCU/blob/master/img/s11.jpg)

## 結果如下

結果大致上正確，最遠距離大概50幾公分，應該堪用。
![image](https://github.com/NKUSTMCU/MCU/blob/master/img/s12.jpg)


