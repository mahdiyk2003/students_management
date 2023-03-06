import sys


class Students(object):
    def __init__(self, name, lastName, fatherName, birthDate, certificateNum, codeMelli, number, phoneNumber):
        self.name = name
        self.lastName = lastName
        self.fatherName = fatherName
        self.birthDate = birthDate
        self.certificateNum = certificateNum
        self.codeMelli = codeMelli
        self.number = number
        self.phoneNumber = phoneNumber
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):

    elements = []

    # Function to insert a node
    def insert_node(self, root, student):
        self.elements = []
        # Find the correct location and insert the node
        if not root:
            return Students(student.name, student.lastName,
                            student.fatherName, student.birthDate,
                            student.certificateNum, student.codeMelli,
                            student.number, student.phoneNumber)
        elif student.codeMelli < root.codeMelli:
            root.left = self.insert_node(root.left, student)
        else:
            root.right = self.insert_node(root.right, student)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if student.codeMelli < root.left.codeMelli:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if student.codeMelli > root.right.codeMelli:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def search(self, root, codeMelli):
        self.elements = []
        if not root:
            return
        if root.codeMelli == codeMelli:
            s = root
        elif root.codeMelli < codeMelli:
            s = self.search(root.right, codeMelli)
        elif root.codeMelli > codeMelli:
            s = self.search(root.left, codeMelli)
        return s

    # Function to delete a node

    def delete_node(self, root, student):
        # Find the node to be deleted and remove it
        if not root:
            return root
        elif student.codeMelli < root.codeMelli:
            root.left = self.delete_node(root.left, student)
        elif student.codeMelli > root.codeMelli:
            root.right = self.delete_node(root.right, student)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.codeMelli = temp.codeMelli
            root.name = temp.name
            root.lastName = temp.lastName
            root.fatherName = temp.fatherName
            root.birthDate = temp.birthDate
            root.certificateNum = temp.certificateNum
            root.number = temp.number
            root.phoneNumber = temp.phoneNumber
            root.right = self.delete_node(root.right,
                                          temp)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factore of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def preOrder(self, root):
        if not root:
            return
        self.elements.append(root)
        self.preOrder(root.left)
        self.preOrder(root.right)
        return self.elements

    def inOrder(self, root):
        if not root:
            return []
        self.inOrder(root.left)
        self.elements.append(root)
        self.inOrder(root.right)
        return self.elements

    def postOrder(self, root):
        if not root:
            return []
        self.postOrder(root.left)
        self.postOrder(root.right)
        self.elements.append(root)
        return self.elements

    def get_elements(self, order="pre"):
        self.elements = []
        if(order == "post"):
            list_elements = myTree.postOrder(root)
        elif(order == "in"):
            list_elements = myTree.inOrder(root)
        else:
            list_elements = myTree.preOrder(root)
        return list_elements



myTree = AVLTree()
root = None
#dummy data
s1 = Students('test1', "1test", "fatherTest1",
              "2022-01-08", "123", 4890, "26453", "910068")
s2 = Students('test2', "2test", "fatherTest2",
              "2202-07-21", "456", 4780, "26445", "935841")
s3 = Students('test3', "3test", "fatherTest3",
              "1258-06-20", "789", 4650, "26741", "912548")
s4 = Students('test4', "4test", "fatherTest4",
              "2012-01-08", "147", 4112, "28951", "910548")
s5 = Students('test5', "5test", "fatherTest5",
              "1952-05-18", "258", 6580, "21459", "902448")
s6 = Students('test6', "6test", "fatherTest6",
              "1850-03-02", "369", 9815, "21456", "915324")
s7 = Students('test7', "7test", "fatherTest7",
              "1850-03-02", "159", 5968, "28459", "789654")
s8 = Students('test8', "8test", "fatherTest8",
              "1850-03-02", "856", 8462, "26458", "123654")
s9 = Students('test9', "9test", "fatherTest9",
              "1850-03-02", "245", 7826, "21851", "741258")
s10 = Students('test10', "10test", "fatherTest10",
               "1850-03-02", "753", 7415, "26984", "965412")
sts = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
for s in sts:
    root = myTree.insert_node(root, s)
