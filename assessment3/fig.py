from sys import argv

def fig2words(n: int) -> str:
    # YOUR CODE HERE
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    twentys = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['zero', 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if(n < 10):
        return ones[n]
    if(n > 10 and n < 20):
        return twentys[n-11]
    if (n < 100):
        if(n % 10 == 0):
            return tens[n//10]
        return tens[n//10] + " " + ones[n%10]
    s = ones[n//100] + " hundred"
    if(n % 100 == 0):
        return s
    return s + " and " + fig2words(n%100)
    
print (fig2words(int(argv[1])))
