def main():
    # Define la ruta del archivo
    path_to_file = "/home/mariomck/workspace/github.com/USERNAME/bookbot/books/frankenstein.txt"

    # Abre el archivo usando un bloque 'with'
    with open(path_to_file, "r") as f:  # "r" indica que estamos abriendo el archivo en modo de lectura
        file_contents = f.read()  # Lee el contenido completo del archivo

    # Divide el string en palabras usando split() y cuenta las palabras
    word_count = len(file_contents.split())

    # Llama a la función count_characters para contar los caracteres
    char_counts = count_characters(file_contents)

    # Genera y muestra el reporte
    print_report(path_to_file, word_count, char_counts)


def count_characters(text):
    # Convertir todo el texto a minúsculas
    text = text.lower()

    # Crear un diccionario vacío para almacenar los conteos
    char_counts = {}

    # Recorrer cada carácter en el texto
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


def print_report(file_path, word_count, char_counts):
    # Imprime la cabecera del reporte
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print()

    # Ordena los caracteres por la cantidad de apariciones (de mayor a menor)
    sorted_char_counts = sorted(
        char_counts.items(), key=lambda item: item[1], reverse=True
    )

    # Imprime los caracteres y sus conteos
    for char, count in sorted_char_counts:
        # Ignorar caracteres que no son letras
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")

    # Imprime el cierre del reporte
    print("--- End report ---")


# Ejecuta la función principal
if __name__ == "__main__":
    main()
