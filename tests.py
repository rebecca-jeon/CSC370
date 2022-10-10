# Test cases for ImplementMe class.
# The mocked objects (and therefore expected output) may change
# at the point of evaluation, including into a more complex object,  
# and the functionality tested by each test case may increase in difficulty.
# Your implementation should anticipate ways in which these mocks
# or tests could be more complex, as well as design mocks
# for some disclosed but not written test cases.

import unittest
import time
import timeout_decorator
from node import *
from index import *
from implement_me import ImplementMe


# Insert into an empty tree
class TestCase01(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        root = Node()
        btree = Index( root )

        key = 99

        newRoot = Node(\
            KeySet([99,None]),\
            PointerSet([None]*Index.FAN_OUT))
        expected_output = Index( newRoot )

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert existing key
class TestCase02(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        root = Node(\
            KeySet([99,None]),\
            PointerSet([None]*Index.FAN_OUT))
        btree = Index( root )

        key = 99

        newRoot = Node(\
            KeySet([99,None]),\
            PointerSet([None]*Index.FAN_OUT))
        expected_output = Index( newRoot )

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert into existing node that is not full
class TestCase03(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        root = Node(\
            KeySet([87, None]),\
            PointerSet([None]*Index.FAN_OUT))
        btree = Index( root )

        key = 66

        newRoot = Node(\
            KeySet([66, 87]),\
            PointerSet([None]*Index.FAN_OUT))
        expected_output = Index( newRoot )

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert into full node.
class TestCase04(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        root = Node(\
            KeySet([66, 99]),\
            PointerSet([None]*Index.FAN_OUT))
        btree = Index( root )

        key = 87

        leaf1 = Node(\
            KeySet([87, 99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([66, None]),\
            PointerSet([None, None, leaf1]))
        newRoot = Node(\
            KeySet([87, None]),\
            PointerSet([leaf0, leaf1, None]))
        expected_output = Index( newRoot )

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert into full node with full parent, causing root split.
# Not shown. To be designed by student.
class TestCase05(unittest.TestCase):
    @timeout_decorator.timeout(25)
    def test_insertion(self):
        leaf3 = Node(KeySet([18, 20]))
        leaf2 = Node(KeySet([12, 14]), PointerSet([None, None, leaf3]))
        leaf1 = Node(KeySet([2, 4]), PointerSet([None, None, leaf2]))
        root = Node(KeySet([12, 18]), PointerSet([leaf1, leaf2, leaf3]))
        btree = Index(root)

        key = 99

        newleaf4 = Node(KeySet([20, 99]))
        newleaf3 = Node(KeySet([18, None]), PointerSet([None, None, newleaf4]))
        newleaf2 = Node(KeySet([12, 14]), PointerSet([None, None, newleaf3]))
        newleaf1 = Node(KeySet([2, 4]), PointerSet([None, None, newleaf2]))
        parent1 = Node(KeySet([12, None]), PointerSet([newleaf1, newleaf2, None]))
        parent2 = Node(KeySet([20, None]), PointerSet([newleaf3, newleaf4, None]))
        newroot = Node(KeySet([18, None]), PointerSet([parent1, parent2, None]))
        expected_output = Index(newroot)
    
        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert into full node with full parent, but does not cause a root split.
class TestCase06(unittest.TestCase):
    @timeout_decorator.timeout(25)
    def test_insertion(self):

        leaf4 = Node(\
            KeySet([97,99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf3 = Node(\
            KeySet([87, None]),\
            PointerSet([None,None,leaf4]))
        leaf2 = Node(\
            KeySet([66,None]),\
            PointerSet([None,None,leaf3]))
        leaf1 = Node(\
            KeySet([27,None]),\
            PointerSet([None,None,leaf2]))
        leaf0 = Node(\
            KeySet([7,9]),\
            PointerSet([None,None,leaf1]))
        parent1 = Node(\
            KeySet([97,None]),\
            PointerSet([leaf3,leaf4,None]))
        parent0 = Node(\
            KeySet([27,66]),\
            PointerSet([leaf0,leaf1,leaf2]))
        root = Node(\
            KeySet([87,None]),\
            PointerSet([parent0,parent1,None]))
        btree = Index(root)

        key = 5

        newLeaf5 = Node(\
            KeySet([97,99]),\
            PointerSet([None]*Index.FAN_OUT))
        newLeaf4 = Node(\
            KeySet([87, None]),\
            PointerSet([None,None,newLeaf5]))
        newLeaf3 = Node(\
            KeySet([66,None]),\
            PointerSet([None,None,newLeaf4]))
        newLeaf2 = Node(\
            KeySet([27,None]),\
            PointerSet([None,None,newLeaf3]))
        newLeaf1 = Node(\
            KeySet([7,9]),\
            PointerSet([None,None,newLeaf2]))
        newLeaf0 = Node(\
            KeySet([5,None]),\
            PointerSet([None,None,newLeaf1]))
        newParent2 = Node(\
            KeySet([97,None]),\
            PointerSet([newLeaf4,newLeaf5,None]))
        newParent1 = Node(\
            KeySet([66,None]),\
            PointerSet([newLeaf2,newLeaf3,None]))
        newParent0 = Node(\
            KeySet([7,None]),\
            PointerSet([newLeaf0,newLeaf1,None]))
        newRoot = Node(\
            KeySet([27,87]),\
            PointerSet([newParent0,newParent1,newParent2]))
        expected_output = Index(newRoot)


        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insertion causes splits that propagates at least three times
class TestCase07(unittest.TestCase):
    @timeout_decorator.timeout(25)
    def test_insertion(self):
        leaf6 = Node(KeySet([59, 69]))
        leaf5 = Node(KeySet([45, None]), PointerSet([None, None, leaf6]))
        leaf4 = Node(KeySet([39, 41]), PointerSet([None, None, leaf5]))
        leaf3 = Node(KeySet([22, 26]), PointerSet([None, None, leaf4]))
        leaf2 = Node(KeySet([16, 19]), PointerSet([None, None, leaf3]))
        leaf1 = Node(KeySet([4,8]), PointerSet([None, None, leaf2]))
        leaf0 = Node(KeySet([2, None]), PointerSet([None, None, leaf1]))
        parent0 = Node(KeySet([4, None]), PointerSet([leaf0, leaf1, None]))
        parent1 = Node(KeySet([22, 39]), PointerSet([leaf2, leaf3, leaf4]))
        parent2 = Node(KeySet([59, None]), PointerSet([leaf5, leaf6, None]))
        root = Node(KeySet([16, 45]), PointerSet([parent0, parent1, parent2]))

        btree = Index(root)

        key = 23

        newleaf7 = Node(KeySet([59, 69]))
        newleaf6 = Node(KeySet([45, None]), PointerSet([None, None, newleaf7]))
        newleaf5 = Node(KeySet([39, 41]), PointerSet([None, None, newleaf6]))
        newleaf4 = Node(KeySet([23 ,26]), PointerSet([None, None, newleaf5]))
        newleaf3 = Node(KeySet([22, None]), PointerSet([None, None, newleaf4]))
        newleaf2 = Node(KeySet([16, 19]), PointerSet([None, None, newleaf3]))
        newleaf1 = Node(KeySet([4, 8]), PointerSet([None, None, newleaf2]))
        newleaf0 = Node(KeySet([2, None]), PointerSet([None, None, newleaf1]))
        newparent00 = Node(KeySet([4, None]), PointerSet([newleaf0, newleaf1, None]))
        newparent01 = Node(KeySet([22, None]), PointerSet([newleaf2, newleaf3, None]))
        newparent02 = Node(KeySet([39, None]), PointerSet([newleaf4, newleaf5, None]))
        newparent03 = Node(KeySet([59, None]), PointerSet([newleaf6, newleaf7, None]))
        newparent10 = Node(KeySet([16, None]), PointerSet([newparent00, newparent01, None]))
        newparent11 = Node(KeySet([45, None]), PointerSet([newparent02, newparent03, None]))
        newroot = Node(KeySet([23, None]), PointerSet([newparent10, newparent11, None]))

        expected_output = Index(newroot)

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Boundary case: lookup smallest key in tree
class TestCase08(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):

        leaf1 = Node(\
            KeySet([87, 99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([66, None]),\
            PointerSet([None, None, leaf1]))
        root = Node(\
            KeySet([87, None]),\
            PointerSet([leaf0, leaf1, None]))
        btree = Index( root )

        key = 66

        expected_output = True

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )


# Boundary case: lookup largest key in tree
# Fake data in first node to test complexity
class TestCase09(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):

        leaf1 = Node(\
            KeySet([87, 99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([66, None]),\
            PointerSet([None, None, leaf1]))
        root = Node(\
            KeySet([87, None]),\
            PointerSet([leaf0, leaf1, None]))
        btree = Index( root )

        key = 99

        expected_output = True

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )


# Lookup key outside range of tree's keys
# Fake data in middle leaf to test complexity
class TestCase10(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):

        leaf1 = Node(\
            KeySet([87, 99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([66, None]),\
            PointerSet([None, None, leaf1]))
        root = Node(\
            KeySet([87, None]),\
            PointerSet([leaf0, leaf1, None]))
        btree = Index( root )

        key = 42

        expected_output = False

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )


# Lookup key within tree's range but not in tree
# Fake data in one leaf to test complexity
class TestCase11(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):

        leaf1 = Node(\
            KeySet([87, 99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([41, None]),\
            PointerSet([None, None, leaf1]))
        root = Node(\
            KeySet([87, None]),\
            PointerSet([leaf0, leaf1, None]))
        btree = Index( root )

        key = 66

        expected_output = False

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )

# Lookup key strictly within the tree's range
class TestCase12(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):

        leaf1 = Node(\
            KeySet([87, 99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([41, 66]),\
            PointerSet([None, None, leaf1]))
        root = Node(\
            KeySet([87, None]),\
            PointerSet([leaf0, leaf1, None]))
        btree = Index( root )

        key = 66

        expected_output = True

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )


# Range query fully contained in one leaf node
class TestCase13(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_range(self):

        leaf1 = Node(\
            KeySet([87, 99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([41, 68]),\
            PointerSet([None, None, leaf1]))
        root = Node(\
            KeySet([87, None]),\
            PointerSet([leaf0, leaf1, None]))
        btree = Index( root )

        lower_bound = 42
        upper_bound = 66

        expected_output = []

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Range query half-open to the left
class TestCase14(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_range(self):

        leaf1 = Node(\
            KeySet([87, 99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([41, 68]),\
            PointerSet([None, None, leaf1]))
        root = Node(\
            KeySet([87, None]),\
            PointerSet([leaf0, leaf1, None]))
        btree = Index( root )

        lower_bound = 0
        upper_bound = 42

        expected_output = [41]

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Range query half-open to the right
class TestCase15(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_range(self):

        leaf1 = Node(\
            KeySet([87, 99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([41, 68]),\
            PointerSet([None, None, leaf1]))
        root = Node(\
            KeySet([87, None]),\
            PointerSet([leaf0, leaf1, None]))
        btree = Index( root )

        lower_bound = 42
        upper_bound = 1024

        expected_output = [68,87,99]

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Range query with matching upper and lower bound
class TestCase16(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_range(self):

        btree = Index()

        lower_bound = 7
        upper_bound = 7

        expected_output = []

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Multi-leaf range query in middle of tree
class TestCase17(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_range(self):

        btree = Index()

        lower_bound = 42
        upper_bound = 87

        expected_output = []

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Lookup recently added key
class TestCase18(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_unknown(self):

        btree = Index()

        key = 12

        expected_output = True

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex(\
        ImplementMe.InsertIntoIndex( btree, key ), key ) )



# Lookup range that includes recently added key
class TestCase19(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_unknown(self):

        leaf4 = Node(\
            KeySet([97,99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf3 = Node(\
            KeySet([87, None]),\
            PointerSet([None,None,leaf4]))
        leaf2 = Node(\
            KeySet([66,None]),\
            PointerSet([None,None,leaf3]))
        leaf1 = Node(\
            KeySet([27,None]),\
            PointerSet([None,None,leaf2]))
        leaf0 = Node(\
            KeySet([7,9]),\
            PointerSet([None,None,leaf1]))
        parent1 = Node(\
            KeySet([97,None]),\
            PointerSet([leaf3,leaf4,None]))
        parent0 = Node(\
            KeySet([27,66]),\
            PointerSet([leaf0,leaf1,leaf2]))
        root = Node(\
            KeySet([87,None]),\
            PointerSet([parent0,parent1,None]))
        btree = Index(root)

        key = 5
        lower_bound = 1
        upper_bound = 68

        expected_output = [5,7,9,27,66]

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex(\
        ImplementMe.InsertIntoIndex( btree, key ), lower_bound, upper_bound ) )


# Lookup range with nearly matching lower and upper bound equal to recently added key
class TestCase20(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_unknown(self):

        btree = Index()

        key = 12
        lower_bound = 12
        upper_bound = 13

        expected_output = [12]

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex(\
        ImplementMe.InsertIntoIndex( btree, key ), lower_bound, upper_bound ) )


# Run all unit tests above.
unittest.main(argv=[''],verbosity=2, exit=False)
