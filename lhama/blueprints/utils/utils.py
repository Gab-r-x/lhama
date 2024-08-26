from datetime import datetime

def get_current_datetime_formatted():
    # Obtém a data e hora atuais
    now = datetime.now()

    # Extrai e formata os componentes individuais
    formatted_datetime = now.year, now.month, now.day, now.hour, now.minute, now.second

    return formatted_datetime

if __name__ == "__main__":
    # Chama a função e imprime o resultado quando o script é executado diretamente
    formatted_datetime = get_current_datetime_formatted()
    print(formatted_datetime)