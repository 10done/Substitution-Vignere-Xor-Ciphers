from collections import Counter
import os

def frequency_table(file_path, case_sensitive=False):
    try:
        # Read the content of the file
        with open(file_path, 'r') as file:
            content = file.read()

        # If not case-sensitive, convert the content to lowercase
        if not case_sensitive:
            content = content.lower()

        # Count the frequency of each character
        frequency = Counter(content)

        # Sort the dictionary by frequency in descending order
        sorted_frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))

        # Return the sorted frequency dictionary
        return sorted_frequency

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}


def replace_characters(file_path, char_map, output_file):
    try:
        # Read the content of the file
        with open(file_path, 'r') as file:
            content = file.read()

        # Replace characters based on the mapping
        replaced_content = ''.join(char_map.get(char, char) for char in content)

        # Write the replaced content to a new file
        with open(output_file, 'w') as file:
            file.write(replaced_content)

        print(f"Replaced content written to '{output_file}'")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_file.txt' with the path to your text file
file_path = 'encrypted_text.txt'
case_sensitive = True  # Set to True if you want case sensitivity
frequency = frequency_table(file_path, case_sensitive)
print(frequency)

char_map = {
    'W': ' ', # correct
    '6': 'E',#done
    '3': 'A',#done
    '#': 'T',#done
    '}': 'H',#done
    '.':'N',#done
    '"':'R',#done
    '>':'F',#done
    '$':'Y',#done
    'a':'M',#done
    "\\":'J',#done
     'y':'?',#done
    'k':'P',#done
    '%':'D',#done
    'g':'Q',#done
    'R':'S',#done
    'A':'V',#done
    '5':'B',#done
    'V':'X',#done
    'D':'W',#done
    'n':'I',#done
    'w':'L',#done
    'p':'C',#done
    'm':'O',#done
    '[':'U',#done
    '{':'G',#done
    'z':'',#done
    's':'Z',#done
    'D':'W',#done
    'F':'P',#done
    'i':'H',#done
    'e':'N',#done
    's':'S',#done
    '!':'L',#done
    'x':'K',#done
    'O':"'",#done
    '*':'K',#done
    '7':'T',#done
    '9':'M',#done
    '8':'!',#done
    'M':'O',#done
    '?':'U',#done
    'X':'R',#done
    'I':'(',#done
    '@':')',#done
    '<':'A',#done
    'l':':',#done
    '=':'D',#done
    'K':'V',#done
    'v':'J',#done U3?R6#}
    '+':',',#done
    'u':'I',#done
    '|':'B',#done
    'C':'Y',#done
    'U':'C',#done
    '/':'F',#done
    '~':'G',#done








    ';':'\n',
    'J':'\n',
    'c':'\n',

    # 'v':'0',
    # "0":'"',
    # " ":'z',
    # '6':'P',
    # '|':"[",
    # ')':"]",
    
    
    
    # 'P':'(',
    # "w":")",
    # 'K':'2',
    # '2':':',
    # "(":"9",
    # '8':'3',
    # 'y':'5',
    # 'T':'6',
    # 'E':'7',
    # '5':'8',
    # 'G':'a',
    # 'F':'m',
    # '@':'n',
    # '^':'I',
    # '"':'u',
    # '*':'C',
    # '.':'E',
    # '/':'x',
    # 'j':"T",
    # 'X':'b',
    # '3':'M',
    # '`':'D',
    # "p":'F',
    # "$":',',
    # "'":'-',
    # 'O':'U',
    # "N":'@',
    # ':':'y',
    # 'C':'{',
    # 'B':'}',
    # '!':'S',
    # ']':'N',
    # 'q':'p',
    # '&':'g',
    # 'o': 'r',
    # '>': 's',
    # 'h': '.',
    # '}': 'c',
    # '{': 'd',
    # 'd':'k',
    # ';':'g',
    # 'f':'R',
    # '~':'v',
    # 'V':'A',
    # 'k':'l',
    # 'A':'W',
    # 'R': 'h',
    # 'b': 'f',
    # ',': 'w',
    # '+':'q',
    # '_':'j'
}
output_file = 'decrypted_text.txt'
if os.path.exists(output_file):
    # Delete the file
    os.remove(output_file)
replace_characters(file_path, char_map,output_file)