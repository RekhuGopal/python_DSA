def reverseWords(s):
        """
        :type s: str
        :rtype: str
        """
        splited = s.split()

        n =  len(splited)
        i =  0
        while i <= ((n//2)-1) :
            splited[i] , splited[n-i-1] = splited[n-i-1] , splited[i]
            i +=1
                

        return " ".join(splited)

print(reverseWords("a good   example"))