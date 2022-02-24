from typing import Dict


def decompress(string: str, table: Dict[str, str]) -> str:
    
    if string == "":
        return
    
    if len(table) == 0:
        return

    result = list(string)

    def helper(table, i):
        nonlocal result
        if i >= len(result):
            return 

        if result[i] in table:
            result[i] = table[result[i]]
            helper(table, 0)
        else:
            i += 1
            helper(table, i)

    helper(table, 0)
    
    return "".join(result)

if __name__ == "__main__":
    # print(decompress('P%Bi/e$', {'$': 's',
    #          '%': 'y',
    #          '/': 't'
    #          }))

    print(decompress('cy300', {'*': 'c',
             '#': '00',
             '$': '*y',
             }))