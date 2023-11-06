#!/usr/bin/env python3

from myhdl import bin
from bits import vm_test
import os
import math

import pytest
import yaml

try:
    from telemetry import telemetryMark

    pytestmark = telemetryMark()
except ImportError as err:
    print("Telemetry não importado")


def source(name):
    dir = os.path.dirname(__file__)
    src_dir = os.path.join(dir, ".")
    return os.path.join(src_dir, name)


SP = 0
STACK = 256
TEMP = {0: 5, 1: 6, 2: 7, 3: 8, 4: 9, 5: 10, 6: 11, 7: 12}


def init_ram():
    ram = {0: 256}
    return ram


@pytest.mark.telemetry_files(source("abs/abs.vm"))
def test_abs_positivo():
    ram = init_ram()
    ram[TEMP[0]] = 6
    tst = {TEMP[0]: 6}
    assert vm_test(os.path.join("abs"), ram, tst, 5000)


@pytest.mark.telemetry_files(source("abs/abs.vm"))
def test_abs_negativo():
    ram = init_ram()
    ram[TEMP[0]] = -2
    tst = {TEMP[0]: 2}
    assert vm_test(os.path.join("abs"), ram, tst, 5000)


@pytest.mark.telemetry_files(source("fact/fact.vm"))
def test_fact_zero():
    ram = init_ram()
    ram[TEMP[0]] = 0
    tst = {TEMP[0]: 1}
    assert vm_test(os.path.join("fact"), ram, tst, 50000)


@pytest.mark.telemetry_files(source("fact/fact.vm"))
def test_fact_one():
    ram = init_ram()
    ram[TEMP[0]] = 1
    tst = {TEMP[0]: 1}
    assert vm_test(os.path.join("fact"), ram, tst, 50000)


@pytest.mark.telemetry_files(source("fact/fact.vm"))
def test_fact_three():
    ram = init_ram()
    x = 3
    ram[TEMP[0]] = x
    tst = {TEMP[0]: math.factorial(x)}
    assert vm_test(os.path.join("fact"), ram, tst, 50000)


@pytest.mark.telemetry_files(source("fact/fact.vm"))
def test_fact_generic():
    ram = init_ram()
    x = 6
    ram[TEMP[0]] = x
    tst = {TEMP[0]: math.factorial(x)}
    assert vm_test(os.path.join("fact"), ram, tst, 50000)


@pytest.mark.telemetry_files(source("isEven/isEven.vm"))
def test_isEven_true():
    ram = init_ram()
    ram[TEMP[0]] = 13
    tst = {TEMP[0]: -1}
    assert vm_test(os.path.join("isEven"), ram, tst, 50000)


@pytest.mark.telemetry_files(source("isEven/isEven.vm"))
def test_isEven_false():
    ram = init_ram()
    ram[TEMP[0]] = 22
    tst = {TEMP[0]: 0}
    assert vm_test(os.path.join("isEven"), ram, tst, 50000)


@pytest.mark.telemetry_files(source("max/max.vm"))
def test_max_arg0():
    ram = init_ram()
    arg0 = 3
    arg1 = 2
    arg2 = 1
    ram[TEMP[0]] = arg0
    ram[TEMP[1]] = arg1
    ram[TEMP[2]] = arg2
    tst = {TEMP[0]: arg0}
    assert vm_test(os.path.join("max"), ram, tst, 50000)


@pytest.mark.telemetry_files(source("max/max.vm"))
def test_max_arg1():
    ram = init_ram()
    arg0 = 1
    arg1 = 3
    arg2 = 2
    ram[TEMP[0]] = arg0
    ram[TEMP[1]] = arg1
    ram[TEMP[2]] = arg2
    tst = {TEMP[0]: arg1}
    assert vm_test(os.path.join("max"), ram, tst, 50000)


@pytest.mark.telemetry_files(source("max/max.vm"))
def test_max_arg2():
    ram = init_ram()
    arg0 = 1
    arg1 = 2
    arg2 = 3
    ram[TEMP[0]] = arg0
    ram[TEMP[1]] = arg1
    ram[TEMP[2]] = arg2
    tst = {TEMP[0]: arg2}
    assert vm_test(os.path.join("max"), ram, tst, 50000)


@pytest.mark.telemetry_files(source("max/max.vm"))
def test_max_eq():
    ram = init_ram()
    arg0 = 2
    arg1 = 3
    arg2 = 3
    ram[TEMP[0]] = arg0
    ram[TEMP[1]] = arg1
    ram[TEMP[2]] = arg2
    tst = {TEMP[0]: arg2}
    assert vm_test(os.path.join("max"), ram, tst, 50000)
