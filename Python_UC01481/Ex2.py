
def calcular_valor_chave(chave: str) -> int:
   
    return sum(ord(c) for c in chave)

def criptografar(mensagem: str, chave: str) -> list[int]:
    if not chave:
        raise ValueError("A chave não pode estar vazia!")
    
    soma_chave = calcular_valor_chave(chave)
    resultado = []
    
    for char in mensagem:
        
        val_original = ord(char)
    
        novo_val = ((val_original - 32 + soma_chave) % 95) + 32
        resultado.append(novo_val)
        
    return resultado

def descriptografar(codigos: list[int], chave: str) -> str:
    if not chave:
        raise ValueError("A chave não pode estar vazia!")
    
    soma_chave = calcular_valor_chave(chave)
    mensagem_original = ""
    
    for codigo in codigos:

        original_val = ((codigo - 32 - soma_chave) % 95) + 32
        mensagem_original += chr(original_val)
        
    return mensagem_original

def menu():
    while True:
        print("\n--- Sistema de Criptografia ASCII ---")
        msg = input("Introduza a mensagem: ")
        chave = input("Introduza a chave (string): ")
        
        if not chave:
            print("Erro: A chave não pode ser vazia. Tente novamente.")
            continue
            
        codigos = criptografar(msg, chave)
        print(f"\nMensagem Criptografada (Valores): {codigos}")
        
        texto_cifrado = "".join(chr(c) for c in codigos)
        print(f"Mensagem Criptografada (Texto): {texto_cifrado}")
        
        decifrado = descriptografar(codigos, chave)
        print(f"Mensagem Descriptografada: {decifrado}")
        
        break

if __name__ == "__main__":
    menu()