# test_field.py
from fiasanova_field import FIASANOVAField, CoBreathCycle
import numpy as np

def test_basic():
    field = FIASANOVAField()
        past = np.array([0.1, 0.2, 0.3])
            future = np.array([0.4, 0.5, 0.6])
                present = np.array([0.7, 0.8, 0.9])
                    result = field.unified_field_now(past, future, present)
                        assert len(result) > 0
                            assert field.coherence > 0

                            def test_co_breath():
                                field = FIASANOVAField()
                                    cycle = CoBreathCycle(field)
                                        human_input = np.array([1.0, 0.5, 0.2])
                                            cycle.inhale(human_input)
                                                integrated = cycle.pause()
                                                    assert integrated is not None
                                                        output = cycle.exhale()
                                                            # output may be None if ethics fail – that's okay for test
                                                                assert field.resonance_score > 0

                                                                if __name__ == "__main__":
                                                                    test_basic()
                                                                        test_co_breath()
                                                                            print("All tests passed!")