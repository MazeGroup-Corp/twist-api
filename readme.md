# Twist API
## The API of the social network Twist

Example of code for print the username of a user :
```py
import twist

user_id = 1

api = twist.TwistAPI()
print(api.getUserInfo(user_id)[0]["username"])
```

Available get functions :
- `getUserInfo(id:int)` -> tuple(dict(informations), dict(request info))
- `getPostInfo(id:int)` -> tuple(dict(informations), dict(request info))
- `getInsightInfo(id:int)` -> tuple(dict(informations), dict(request info))
- `getLikeInfo(id:int)` -> tuple(dict(informations), dict(request info))
- `getFollowInfo(id:int)` -> tuple(dict(informations), dict(request info))
- `getUsersList()` -> tuple(dict(informations), dict(request info))
- `getPostsList()` -> tuple(dict(informations), dict(request info))
- `getInsightsList()` -> tuple(dict(informations), dict(request info))
- `getLikesList()` -> tuple(dict(informations), dict(request info))
- `getFollowsList()` -> tuple(dict(informations), dict(request info))
