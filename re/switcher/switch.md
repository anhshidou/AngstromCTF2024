![image](https://github.com/anhshidou/AngstromCTF2024/assets/120787381/5f746765-9f4e-4d9d-8eaa-6076d4305c74)

```
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  printf("Enter the password: ");
  fflush(stdout);
  fgets(s, 256, stdin);
  s[strcspn(s, "\n")] = 0;
  sub_5540(s);
  puts("That's not the password...");
  return 1LL;
}
```

Ở bài này, khi ta xem hàm main thì sẽ thấy được việc nó đang so sánh hàm s. Mà ngay ở dưới, ta biết được hàm s được gọi bởi hàm sub_5540. Vì vậy, ta xem hàm sub_5540

```
void __fastcall sub_5540(_BYTE *a1)
{
  _BYTE *v1; // rdi
  _BYTE *v2; // rdi
  _BYTE *v3; // rdi
  _BYTE *v4; // rdi
  _BYTE *v5; // rdi
  _BYTE *v6; // rdi
  _BYTE *v7; // rdi
  _BYTE *v8; // rdi
  _BYTE *v9; // rdi
  _BYTE *v10; // rdi
  _BYTE *v11; // rdi
  _BYTE *v12; // rdi
  _BYTE *v13; // rdi
  _BYTE *v14; // rdi
  _BYTE *v15; // rdi
  _BYTE *v16; // rdi
  _BYTE *v17; // rdi
  _BYTE *v18; // rdi
  _BYTE *v19; // rdi
  _BYTE *v20; // rdi
  _BYTE *v21; // rdi
  _BYTE *v22; // rdi
  _BYTE *v23; // rdi
  _BYTE *v24; // rdi
  _BYTE *v25; // rdi
  _BYTE *v26; // rdi
  _BYTE *v27; // rdi
  _BYTE *v28; // rdi
  _BYTE *v29; // rdi
  _BYTE *v30; // rdi
  _BYTE *v31; // rdi
  _BYTE *v32; // rdi
  _BYTE *v33; // rdi
  _BYTE *v34; // rdi
  _BYTE *v35; // rdi
  _BYTE *v36; // rdi

  if ( *a1 == 106 )
  {
    v36 = a1 + 1;
    if ( *v36 == 117 )
    {
      v35 = v36 + 1;
      if ( *v35 == 109 )
      {
        v34 = v35 + 1;
        if ( *v34 == 112 )
        {
          v33 = v34 + 1;
          if ( *v33 == 105 )
          {
            v32 = v33 + 1;
            if ( *v32 == 110 )
            {
              v31 = v32 + 1;
              if ( *v31 == 103 )
              {
                v30 = v31 + 1;
                if ( *v30 == 95 )
                {
                  v29 = v30 + 1;
                  if ( *v29 == 109 )
                  {
                    v28 = v29 + 1;
                    if ( *v28 == 121 )
                    {
                      v27 = v28 + 1;
                      if ( *v27 == 95 )
                      {
                        v26 = v27 + 1;
                        if ( *v26 == 119 )
                        {
                          v25 = v26 + 1;
                          if ( *v25 == 97 )
                          {
                            v24 = v25 + 1;
                            if ( *v24 == 121 )
                            {
                              v23 = v24 + 1;
                              if ( *v23 == 95 )
                              {
                                v22 = v23 + 1;
                                if ( *v22 == 116 )
                                {
                                  v21 = v22 + 1;
                                  if ( *v21 == 111 )
                                  {
                                    v20 = v21 + 1;
                                    if ( *v20 == 95 )
                                    {
                                      v19 = v20 + 1;
                                      if ( *v19 == 116 )
                                      {
                                        v18 = v19 + 1;
                                        if ( *v18 == 104 )
                                        {
                                          v17 = v18 + 1;
                                          if ( *v17 == 101 )
                                          {
                                            v16 = v17 + 1;
                                            if ( *v16 == 95 )
                                            {
                                              v15 = v16 + 1;
                                              if ( *v15 == 102 )
                                              {
                                                v14 = v15 + 1;
                                                if ( *v14 == 108 )
                                                {
                                                  v13 = v14 + 1;
                                                  if ( *v13 == 97 )
                                                  {
                                                    v12 = v13 + 1;
                                                    if ( *v12 == 103 )
                                                    {
                                                      v11 = v12 + 1;
                                                      if ( *v11 == 95 )
                                                      {
                                                        v10 = v11 + 1;
                                                        if ( *v10 == 111 )
                                                        {
                                                          v9 = v10 + 1;
                                                          if ( *v9 == 110 )
                                                          {
                                                            v8 = v9 + 1;
                                                            if ( *v8 == 101 )
                                                            {
                                                              v7 = v8 + 1;
                                                              if ( *v7 == 95 )
                                                              {
                                                                v6 = v7 + 1;
                                                                if ( *v6 == 98 )
                                                                {
                                                                  v5 = v6 + 1;
                                                                  if ( *v5 == 121 )
                                                                  {
                                                                    v4 = v5 + 1;
                                                                    if ( *v4 == 95 )
                                                                    {
                                                                      v3 = v4 + 1;
                                                                      if ( *v3 == 111 )
                                                                      {
                                                                        v2 = v3 + 1;
                                                                        if ( *v2 == 110 )
                                                                        {
                                                                          v1 = v2 + 1;
                                                                          if ( *v1 == 101 )
                                                                            sub_1200(v1 + 1);
                                                                        }
                                                                      }
                                                                    }
                                                                  }
                                                                }
                                                              }
                                                            }
                                                          }
                                                        }
                                                      }
                                                    }
                                                  }
                                                }
                                              }
                                            }
                                          }
                                        }
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

Ta thấy nó rất dài, dài vl. Nhưng mà sau khi để ý kĩ, ta thấy nó đang kiểm tra xem liệu string được nhập từ input có đúng với một dãy các kí tự không. 

Ở đây, trong bảng mã ascii, ta thấy rằng nó khi kết hợp vào sẽ được 1 string như sau:

![image](https://github.com/anhshidou/AngstromCTF2024/assets/120787381/f33dd17a-df99-4c98-86d0-168d9091106d)

**jumping_my_way_to_the_flag_one_by_one**

Vậy, thêm vào password dòng kia và ta sẽ được:

![image](https://github.com/anhshidou/AngstromCTF2024/assets/120787381/40a4b3f2-f2ab-4f52-9344-f8acc6b1dd97)


**Flag: actf{jumping_my_way_to_the_flag_one_by_one}**




