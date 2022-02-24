from typing import Dict


def decompress(string: str, table: Dict[str, str]) -> str:
    
    if string == "":
        return string
    
    if len(table) == 0:
        return string

    result = list(string)

    def helper(table, i):
        nonlocal result
        if i >= len(result):
            return 

        if result[i] in table:
            table_value = table[result[i]]

            if len(table_value) > 1:
    
                for j in range(len(table_value)):
                    if j == 0:
                        result[i] = table_value[j]
                    else:
                        result.insert(i + j, table_value[j])

            else:
                result[i] = table_value
                
            helper(table, 0)
        else:
            i += 1
            helper(table, i)

    helper(table, 0)
    
    return "".join(result)

#if __name__ == "__main__":
    # print(decompress('P%Bi/e$', {'$': 's',
    #          '%': 'y',
    #          '/': 't'
    #          }))

    # print(decompress('$3#', {'*': 'c',
    #          '#': '00',
    #          '$': '*y',
    #          }))