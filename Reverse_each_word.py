# PROBLEM DEFINITION
# You are required to write a function which will generate the reverse of a given string according to the following rules.
# Reverse each word in the input string.
# The order of the words will be unchanged.
# A word could be made up of letters and/or numbers.
# Other characters (spaces, punctuation) will not be reversed.
#
#
# NOTES
#
# You are required to provide written test cases to verify correct implementation of this function.
# Report a potential bug. (This should not actually exist in your implementation but come up with a bug which could potentially exist in such a requirement and report it. )
# You are free to use any programming language of your choice to implement this code.
# The code should work with all types of possible inputs (alphanumeric, special characters, unicode characters etc.)
# Spaces, punctuation & other special characters should not be reversed.
# Write production quality code.
# The template below is in Python and working solution is preferred (assert in main() should succeed)
# Bonus points for good testcases.

def reverse_each_word(test_str):
    punct=['.',' ',',','!',':',';']
    str=''
    str1=''
    l=len(test_str)
    i=0
    while i<l:
        if test_str[i] in punct:
            if len(str1):
                str+=str1[::-1]
            str1=''
            str+=test_str[i]
            i+=1
            continue
        str1+=test_str[i]
        i+=1
    if len(str1):
        str+=str1[::-1]
    return str
test_str='String; 2be reversed...'

testcases={'String; 2be reversed...':'gnirtS; eb2 desrever...',
           'My NaMeis ; is . Abgt':'yM sieMaN ; si . tbA',
           '123t bdg- sdgk9;.':'t321 -gdb 9kgds;.'}
for testcase in testcases:
    try:
        assert(reverse_each_word(testcase))==testcases[testcase]
        print("Testcase verified:",testcase)
    except:
        print("Wrong Answer:",testcase)
assert(reverse_each_word(test_str))=="gnirtS; eb2 desrever..."
