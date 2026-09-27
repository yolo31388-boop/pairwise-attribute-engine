"""属性计算引擎 - 带8个bug"""
from dataclasses import dataclass, field
import random

@dataclass
class Affix:
    name: str
    value: float
    attr_type: str  # flat/percent
    group: str = ""  # 互斥组

@dataclass
class Equipment:
    eid: str
    name: str
    rarity: str
    level: int
    affixes: list[Affix] = field(default_factory=list)
    unique: bool = False
    set_id: str = None

class AttributeEngine:
    def __init__(self):
        self.base = {"str": 10, "dex": 10, "int": 10}
        self.equipped: list[Equipment] = []
        self.inventory: list[Equipment] = []
        self.storage: list[Equipment] = []

    def calculate(self):
        # bug1: 四层全混在一起加
        result = dict(self.base)
        for eq in self.equipped:
            for af in eq.affixes:
                result[af.name] = result.get(af.name, 0) + af.value
        return result

    def generate_affix(self, pool, rarity):
        # bug3: 权重不按稀有度缩放
        return random.choice(pool)

    def check_set_bonus(self):
        # bug4: 只数数量不看ID
        count = len([e for e in self.equipped if e.set_id])
        return count >= 2

    def recalc(self):
        # bug5: 全量遍历
        return self.calculate()

    def can_equip(self, eq: Equipment):
        # bug6: 只检查背包
        if eq.unique:
            for e in self.inventory:
                if e.name == eq.name:
                    return False
        return True
