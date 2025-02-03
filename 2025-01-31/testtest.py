from dotenv import load_dotenv
import os


load_dotenv()

token=os.getenv("TOKEN")
print(token)

# print(os.getenv("TOKEN"))
# print(os.getenv("LOGIN_ID"))

#라이브러리 사용방법 env 사용법 토큰을 깃에 올리지않고 쓸 수 있는법