
https://cdnjs.com/libraries/jquery
https://cdnjs.com/libraries/bootstrap

# http://127.0.0.1:5000/

# @app.route("/")
# def index():
#     return "안녕하세요"

# CGI 방식
# @app.route("/")
# def index():
#     return """
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <meta charset="UTF-8">
#         <title>Title</title>
#     </head>
#     <body>
#         <p>안녕하세요</p>
#     </body>
#     </html>
#     """

'''
비동기 서비스, AJAX
하나의 서버가 클라이언트에게 제공을 했다면
원활하게 해결하기 위해

CDN Server (컨텐츠 전송 네트워크)
분산처리방식

bootstrap
* 1. html, css, js
* 2. CDN 을 이용

HTML
    화면을 구성하는 방법
    글자, 이미지 위치
    언어 구조

CSS
    디자인 요소

js
    정적인 화면이 아니라 계속 변화함
    동적인 환경을 변화시키는 요소
    요즘은 별거 다 할 수 있음
    크롬도 자바 스크립트로 만들어져 있음


jQuery
    https://cdnjs.com/libraries/jquery
    jquery 1. , 2. , 3. 다 다르게 개발은 됐지만 하위 버전을 다 커버함

    배포시(미니 파일)
    https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js
    개발시
    https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.js
    어차피 같은 내용이인데 가독성이 좋냐 안 좋냐만 차이 있음
    두번째거 copy script tag 복붙

'''


# 랜더 템플릿
# 폴더를 따로 만들어 두고 거기서 파일을 불러옴

# 2021.10.10
1. front
http://127.0.0.1:5000/

2. back(추론) API 역할
http://127.0.0.1:5000/
