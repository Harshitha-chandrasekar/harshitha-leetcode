class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        news = ""
        for i in range(len(address)):
            if address[i] == '.':
                news = news + "[.]"
            else:
                news = news + address[i]

        return news
