import pytest
from Node import Node


def test_node_stores_value():
    n = Node(10)
    assert n.value == 10


def test_node_next_defaults_to_none():
    n = Node(5)
    assert n.next is None


def test_node_next_can_be_set_at_init():
    second = Node(2)
    first = Node(1, next=second)
    assert first.next is second


def test_node_value_can_be_mutated():
    n = Node(42)
    n.value = 99
    assert n.value == 99


def test_node_next_can_be_mutated():
    n = Node(1)
    n.next = Node(2)
    assert n.next.value == 2


def test_node_chain():
    c = Node(3)
    b = Node(2, next=c)
    a = Node(1, next=b)
    assert a.next.next.value == 3


def test_node_value_none():
    n = Node(None)
    assert n.value is None


def test_node_value_string():
    n = Node("hello")
    assert n.value == "hello"


def test_node_self_reference():
    n = Node(1)
    n.next = n
    assert n.next is n
