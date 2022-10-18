import speech_recognition as sr

def reconheceraudiomicrofone(reconhecedor, microfone):

    with microfone as somprincipal:
        reconhecedor.adjust_for_ambient_noise(somprincipal)

        audio = reconhecedor.listen(somprincipal)

    response = {
        "sucesso": True,
        "erro": None,
        "transcricao": None
    }

    try:
        response["transcricao"] = reconhecedor.recognize_google(audio, language='pt-BR')

    except sr.RequestError:
        response["sucesso"] = False
        response["erro"] = "API não disponível"

    except sr.UnknownValueError:
        response["erro"] = "# Não entendi a sua fala"
    
    return response 

# Môdulo Principal #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    reconhecedor = sr.Recognizer()
    microfone = sr.Microphone()

    NFALA = 2
    NSEMFALA = 3

    print('\n### PROGAMA FUNCIONANDO ###')

    for i in range(NFALA):

        for j in range(NSEMFALA):
            print('\nTESTE {} - Fale no microfone!\n'.format(i+1))

            somteste = reconheceraudiomicrofone(reconhecedor, microfone)

            if somteste['transcricao']:
                break
            
            if not somteste['sucesso']:
                break
            print("# Eu não entendi. Repita, por favor\n")

        if somteste['erro']:
            print("ERRO: {}\n".format(somteste["erro"]))
            break
        
print("#Você disse: {}".format(somteste["transcricao "]))






