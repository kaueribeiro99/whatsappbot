from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
count = 0


@app.route("/sms", methods=['POST'])
def reply():
    user_msg = request.form.get('Body').lower()
    response = MessagingResponse()
    message = response.message()
    responded = False

    if "hello" in user_msg:
        reply_msg = "Olá, eu sou CodeBot! \nSelecione a opção desejada: " \
                    "\n 1-Agendar Consulta \n 2-Preços \n 3-Retorno"
        message.body(reply_msg)
        responded = True

    if "1" in user_msg:
        option1 = "Meus horários disponiveis são - Terça-feira (10h00)\n" \
                  "Pressione 0 para voltar ao menu"
        message.body(option1)
        responded = True
    if "2" in user_msg:
        option2 = "Valor da Consulta: R$100,00"
        message.body(option2)
        responded = True
    if "3" in user_msg:
        option0 = "Os retornos estão disponiveis apenas para o próximo mês"
        message.body(option0)
        responded = True

    if "0" in user_msg:
        reply_msg = "Olá, eu sou CodeBot! \nSelecione a opção desejada: " \
                    "\n 1-Agendar Consulta \n 2-Preços \n 3-Retorno"
        message.body(reply_msg)
        responded = True

    if not responded:
        message.body("Opção inválida, por favor selecione um opção válida!")

    return str(response)


if __name__ == "__main__":
    app.run(debug=True)
