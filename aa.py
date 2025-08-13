from redis import Redis
redis_cli = Redis(
    host="192.168.1.75",
    port=6379,
    db=0,

)
redis_cli.set("mingzhi","lvjialin")
print(redis_cli.get("mingzhi"))
print(type(redis_cli.get("mingzhi")))