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
    #if(len(context.args) != target_args):
    #    send_message_chunked(update, context, "Error: Refer to /help.")
    #    return False
    send_message_chunked(update, context, message)

def giris_handler(update, context):
    GRS_MSG = "🇹🇷 Corona Telegram botuna hoşgeldiniz.\nBilgi için /yardim yazınız."

    assert_args_and_send(update, context, GRS_MSG)

def yardim_handler(update, context):
    YRD_MSG = """Aşağıdaki komutlarla bilgilere erişebilirsiniz:
    /rakam - 🚑 Toplam vaka, ölüm ve iyileşme sayılarını gösterir.
    /vaka - 🦠 Toplam vaka sayısını gösterir.
    /iyilesen - 💉 Toplam iyileşen sayısını gösterir.
    /olum - 💀 Toplam ölüm sayısını gösterir."""

    assert_args_and_send(update, context, YRD_MSG)

def vaka_handler(update, context):
    assert_args_and_send(update, context, parse_api_data(coronaapi.fetch_vaka(), "kişi hastalığa yakalandı"), target_args=1)

def iyilesen_handler(update, context):
    assert_args_and_send(update, context, parse_api_data(coronaapi.fetch_iyilesen(), "kişi hastalığı atlattı"), target_args=1)

def olum_handler(update, context):
    assert_args_and_send(update, context, parse_api_data(coronaapi.fetch_olum(), "kişi öldü"),target_args=1)

def rakam_handler(update, context):
    vaka_handler(update, context)
    iyilesen_handler(update, context)
    olum_handler(update, context)