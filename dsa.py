# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(message, K):
    # write your code in Python 3.6

    messageList = message.split(" ")
    characters_remaining = K
    keep_counting = True
    cropped_string = ''

    print(messageList)
    for i in messageList:
        if (len(i) <= characters_remaining):
            cropped_string+= f"{i} "
            print(cropped_string)
            characters_remaining -= len(i) +1
            print(characters_remaining)
        else:
            break
    
    print(cropped_string.strip())
    print(len(cropped_string))


mm = 'The quick brown fox jumps over the lazy dog'
k = 39

solution(message=mm, K=k)