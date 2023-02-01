
def DecimaltoBinaryConv(n):
    assert int(n) == n, 'The parameter must be Integer number'
    if n == 0:
        return 0;
    else:
        return n%2 + 10 * DecimaltoBinaryConv(int(n/2))


print(DecimaltoBinaryConv(19));

#Divide the number by 2
#Get the Integer Quotient for next iteration
#Get the reminder for the binary digit
#Repeat the steps until the quotient is equal to 0;
#f(n) = n % 2 + 10 * f(n/2)