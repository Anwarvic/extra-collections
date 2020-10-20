import random
import pytest

class Helper:
    @staticmethod
    def get_int(a=-1000, b=1000):
        return random.randint(a, b)

    @staticmethod
    def get_pos_int(a=1, b=1000):
        return random.randint(a, b)

    @staticmethod
    def get_neg_int(a=-1000, b=-1):
        return random.randint(a, b)

    @staticmethod
    def get_float(a=-1000, b=1000):
        return random.uniform(a, b)

    @staticmethod
    def get_pos_float(a=1, b=1000):
        return random.uniform(a, b)

    @staticmethod
    def get_neg_float(a=-1000, b=-1):
        return random.uniform(a, b)

    @staticmethod
    def get_string(length=5):
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        s = [ALPHABET[Helper.get_pos_int(b=length)] for _ in range(length)]
        return "".join(s)

    @staticmethod
    def get_value():
        func = random.choice(
            [Helper.get_int, Helper.get_float, Helper.get_string]
        )
        return func()

    @staticmethod
    def get_list(length=5, _type=None):
        if _type is None:
            return [Helper.get_value() for _ in range(length)]
        elif _type == int:
            return [Helper.get_int() for _ in range(length)]
        elif _type == float:
            return [Helper.get_float() for _ in range(length)]
        elif _type == str:
            return [Helper.get_string() for _ in range(length)]


    @staticmethod
    def verify_bst_rules(start_node):
        """
        This is a helpful function to check if the BST rule is applied over all
        nodes of the tree. By the BST rule, I mean that each subtree on the left
        is lower than the parent; and the subtree on the right is greater than the
        parent
        """
        if start_node is None:
            return True
        left_child = start_node.get_left()
        right_child = start_node.get_right()
        if not (
            left_child is None or left_child.get_data() < start_node.get_data()
        ) or not (
            right_child is None or right_child.get_data() > start_node.get_data()
        ):
            return False
        return (
            Helper.verify_bst_rules(left_child)
            and Helper.verify_bst_rules(right_child)
        )

    @staticmethod
    def verify_min_heap(start_node):
        if start_node is None:
            return True
        left_child = start_node.get_left()
        right_child = start_node.get_right()
        if not (
            left_child is None or left_child.get_data() >= start_node.get_data()
        ) or not (
            right_child is None or right_child.get_data() >= start_node.get_data()
        ):
            return False
        return (
            Helper.verify_min_heap(left_child)
            and Helper.verify_min_heap(right_child)
        )

    @staticmethod
    def verify_max_heap(start_node):
        if start_node is None:
            return True
        left_child = start_node.get_left()
        right_child = start_node.get_right()
        if not (
            left_child is None or left_child.get_data() <= start_node.get_data()
        ) or not (
            right_child is None or right_child.get_data() <= start_node.get_data()
        ):
            return False
        return (
            Helper.verify_max_heap(left_child)
            and Helper.verify_max_heap(right_child)
        )

    @staticmethod
    def verify_treap_priority(start_node):
        if start_node is None:
            return True
        left_child = start_node.get_left()
        right_child = start_node.get_right()
        if not (
            left_child is None
            or left_child.get_priority() <= start_node.get_priority()
        ) or not (
            right_child is None
            or right_child.get_priority() <= start_node.get_priority()
        ):
            return False
        return (
            Helper.verify_treap_priority(left_child)
            and Helper.verify_treap_priority(right_child)
        )

    @staticmethod
    def verify_skiplist(skiplist):
        for level in range(skiplist.get_height()):
            curr_node = skiplist._level_lists[level]._head
            if curr_node.get_data() != float("-inf"):
                return False
            while curr_node.get_next() is not None:
                next_node = curr_node.get_next()
                if curr_node.get_data() >= next_node.get_data():
                    return False
                if not (
                    curr_node.get_down() is None
                    or curr_node.get_down().get_data() == curr_node.get_data()
                ):
                    return False
                curr_node = next_node
        return True


@pytest.fixture
def helper():
    return Helper