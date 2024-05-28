![image](https://github.com/anhshidou/AngstromCTF2024/assets/120787381/6eb619d0-1cfa-4a91-855c-3399204090b9)


Ta thử mở file:

![image](https://github.com/anhshidou/AngstromCTF2024/assets/120787381/4cbeb35d-f5ed-472f-b913-fcfba8f52e54)

Khi ta thử mở file, ta thấy rằng file không được support, vậy có lẽ đang có một lỗi gì đó trong file header hoặc ở trong hex của file ảnh này. Mình sử dụng hxd để kiểm tra

![image](https://github.com/anhshidou/AngstromCTF2024/assets/120787381/7702a513-67e0-483c-ad04-49354804dcf4)

Đây là dòng byte đầu. Sau khi kiểm tra file signature, rõ ràng đang có lỗi gì đó. Không hề có FD D8. Sau đó, mình kiểm tra những đoạn byte đầu của file jpg thì rõ ràng nó phải là **FF D8** chứ không phải **FD D8**. Vì vậy mình sửa lại đoạn này

``` FF D8 FF E0 00 10 4A 46 49 46 00 01 ```

![image](https://github.com/anhshidou/AngstromCTF2024/assets/120787381/08d1d9c5-230f-4335-8b5b-ada0296f08fe)

Sau khi sửa thì ta sẽ nhận được một bức ảnh như sau:

![image](https://github.com/anhshidou/AngstromCTF2024/assets/120787381/bf9240aa-c096-4c8a-8e64-22f6020e34ac)

**Flag: actf{build_the_snowman}**
