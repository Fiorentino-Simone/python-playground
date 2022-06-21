def main():
    message = '';
    listOfWords = [];
    interrogatives = ('how', 'what', 'when', 'where', 'who', 'why', 'which'); #usiamo la tuples cosi non si modifica
    while(message != '\end'):
        message = input('Enter a message: ');
        if(message.find('\end') != -1):
            message = message.replace("\end", "");
            break;
        elif((message.lower()).startswith(interrogatives)): 
            #se la stringa inizia con una parola interrogativa si usa il metodo startswith
            message += "?";
        else:
            message += ".";
        message = message.capitalize() + " ";
        listOfWords.append(message);
    # for i in range(len(listOfWords)):
    #     print(listOfWords[i]);
    print(" ".join(listOfWords)); # join the list of words into a string, in maniera molto più efficiente

main();