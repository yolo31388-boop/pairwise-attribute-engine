"""属性引擎测试"""
import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.engine import AttributeEngine, Equipment, Affix

class TestCalc:
    def test_flat_and_percent_separate(self):
        ae = AttributeEngine()
        ae.base = {"str": 100}
        ae.equipped = [Equipment("e1", "e1", "rare", 1, [Affix("str", 10, "flat"), Affix("str", 0.1, "percent")])]
        result = ae.calculate()
        # 100+10=110, 110*1.1=121
        assert result["str"] == 121, f"百分比和固定混算: {result['str']}"

class TestUnique:
    def test_unique_checks_all_slots(self):
        ae = AttributeEngine()
        unique_eq = Equipment("u1", "UniqueSword", "legendary", 1, unique=True)
        ae.equipped = [unique_eq]
        ae.inventory = []
        assert not ae.can_equip(Equipment("u2", "UniqueSword", "legendary", 1, unique=True)), "唯一性未检查已装备"
