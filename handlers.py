import coronaapi

def parse_api_data(data, status):
    try:
        final = ""
        for i in data:
            final = "[{date}] : {val} {status}.\n".format(date=i["Date"].split('T')[0], val=i["Cases"], status=status)
        return final
    except:
        return "Error: Could not parse API data."

def send_message_chunked(update, context, message):
    msgs = [message[i:i + 4096] for i in range(0, len(message), 4096)]
    for text in msgs:
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def assert_args_and_send(update, context, message, target_args=0):
    if(len(context.args) != target_args):
        send_message_chunked(update, context, "Error: Refer to /help.")
        return False
    send_message_chunked(update, context, message)

def giris_handler(update, context):
    GRS_MSG = "Corona botuna hoşgeldiniz.\nBilgi için /bilgi yazınız."

    assert_args_and_send(update, context, GRS_MSG)

def yardim_handler(update, context):
    YRD_MSG = """Aşağıdaki komutlarla bilgilere erişebilirsiniz:
    /rakam Toplam vaka, ölüm ve iyileşme sayılarını gösterir.
    /vaka COUNTRYHERE - Returns a list of confirmed cases for country COUNTRYHERE.
    /iyilesme COUNTRYHERE - Returns a list of recovered cases for country COUNTRYHERE.
    /olum COUNTRYHERE - Returns a list of deaths for country COUNTRYHERE."""

    assert_args_and_send(update, context, YRD_MSG)

def vaka_handler(update, context):
    assert_args_and_send(update, context, parse_api_data(coronaapi.fetch_confirmed(context.args[0].lower()), "confirmed"), target_args=1)

def iyilesme_handler(update, context):
    assert_args_and_send(update, context, parse_api_data(coronaapi.fetch_recovered(context.args[0].lower()), "recovered"), target_args=1)

def olum_handler(update, context):
    assert_args_and_send(update, context, parse_api_data(coronaapi.fetch_deaths(context.args[0].lower()), "deaths"),target_args=1)

def rakam_handler(update, context):
    confirmed_handler(update, context)
    recovered_handler(update, context)
    deaths_handler(update, context)