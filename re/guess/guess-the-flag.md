# Guess the flag - 20 pts

![image](https://github.com/anhshidou/AngstromCTF2024/assets/120787381/e11a911c-5c7d-4378-aa7c-5a053c14ea3c)

```
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char *v3; // rbx
  char _0[72]; // [rsp+0h] [rbp+0h] BYREF
  unsigned __int64 vars48; // [rsp+48h] [rbp+48h]

  vars48 = __readfsqword(0x28u);
  puts("Go ahead, guess the flag: ");
  v3 = _0;
  fgets(_0, 63, stdin);
  while ( strlen(_0) > v3 - _0 )
    *v3++ ^= 1u;
  if ( !strcmp(_0, secretcode) )
    puts("Correct! It was kinda obvious tbh.");
  else
    puts("Wrong. Not sure why you'd think it'd be that.");
  if ( vars48 != __readfsqword(0x28u) )
    start();
  return 0;
}
```

Ta sử dụng IDA để disassemble file. Sau khi xem pseudocode của bài, ta thấy có mốt số thứ cần để ý sau:

```  puts("Go ahead, guess the flag: "); ```

**Ở đoạn này, ta thấy rằng, khi chạy file, ta sẽ xuất hiện 1 dòng đoán flag như trên:**

![image](https://github.com/anhshidou/AngstromCTF2024/assets/120787381/07ef046a-0f8e-4072-ad4f-46b65d576c5c)


``` if ( !strcmp(_0, secretcode) )
    puts("Correct! It was kinda obvious tbh.");
  else
    puts("Wrong. Not sure why you'd think it'd be that."); ```

Khi mà stringcmp so sánh với secretcode mà đúng thì nó sẽ nhả flag, còn nếu không thì sẽ là dòng dưới. Vì vậy, ta xem hàm secretcode là gì.

```

![image](https://github.com/anhshidou/AngstromCTF2024/assets/120787381/50db3b1b-ce6b-4f2f-9828-99e9031b0cf8)



Lúc này, ta biết được rằng đoạn string này đang được xor từng từ với 1. Vì vậy nên ta cần phải đảo lại cái đoạn xor này bằng đoạn code nhỏ.


**Flag: actf{committed_to_the_least_significant_bit}**
