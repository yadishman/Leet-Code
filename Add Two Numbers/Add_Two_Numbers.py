class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1=self.linkedtolist(l1)
        num2=self.linkedtolist(l2)
        summation=num1+num2
        linkedlist=self.listtolinked(summation)
        return linkedlist
    
    def linkedtolist(self,linked):
        temp=[]
        currentNode=linked
        while (True):
            if currentNode.next==None:
                temp.append(str(currentNode.val))
                break
            else:
                temp.append(str(currentNode.val))
                currentNode=currentNode.next
        final= self.number(temp)
        return final

    def number(self,mylist):
        number=0
        temp=""
        for i in range(len(mylist)-1,-1,-1):
            temp+=mylist[i]
        number=int(temp)
        return number
    def listtolinked(self,number):
        temp=str(number)
        reverse=""
        for i in range(len(temp)-1,-1,-1):
            reverse+=temp[i]
        if (len(reverse)==1):
            head=ListNode(int(reverse[0]))
            return head
        else:
            head=ListNode(int(reverse[0]))
            currentNode=head
            for i in range(1,len(reverse)):
                currentNode.next=ListNode(int(reverse[i]))
                currentNode=currentNode.next

            return head