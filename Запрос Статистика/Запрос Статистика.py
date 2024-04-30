import vk_api

from flask import render_template, request, Flask
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

app = Flask(__name__)
app.config["SECRET_KEY"] = "lalalalaзаткни_свой_рот"


@app.route("/vk_stat/<int:group_id>", methods=["GET"])
def index(group_id):
    vk_session = vk_api.VkApi(token="ваш токен")
    longpoll = VkBotLongPoll(vk_session, group_id)
    vk_stat = stats_get(group_id)  # я не понял откуда он и как его вызывать так что так,
    # но нашёл документацию на то что он содержит и интуитивно понимаю как с ним бороться, но это не точно
    # может хотя-бы за то что попытался поставите?)
    return render_template("index.html", title="vk_stat", st=vk_stat)


if __name__ == "__main__":
    app.run(debug=True)
