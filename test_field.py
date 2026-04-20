import numpy as np

from fiasanova_field import CoBreathCycle, FIASANOVAField


def test_unified_field_now_creates_output():
    field = FIASANOVAField()
    past = np.array([0.1, 0.2, 0.3])
    future = np.array([0.4, 0.5, 0.6])
    present = np.array([0.7, 0.8, 0.9])

    result = field.unified_field_now(past, future, present)

    assert result.shape == present.shape
    assert np.all(np.isfinite(result))
    assert field.coherence >= 0


def test_co_breath_cycle_returns_exhaled_signal():
    field = FIASANOVAField()
    cycle = CoBreathCycle(field)
    human_input = np.array([1.0, 0.5, 0.2])

    cycle.inhale(human_input)
    integrated = cycle.pause()
    output = cycle.exhale()

    assert integrated is not None
    assert output is not None
    assert output.shape == integrated.shape
    assert field.resonance_score > 0
