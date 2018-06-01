"""Classification task."""

import keras

from matchzoo import engine


class Classification(engine.BaseTask):
    """Classification task."""

    def __init__(self, num_classes: int = 2):
        super().__init__()
        if not isinstance(num_classes, int):
            raise TypeError
        if num_classes < 2:
            raise ValueError
        self._num_classes = num_classes

    @property
    def num_classes(self) -> int:
        return self._num_classes

    @classmethod
    def list_available_losses(cls) -> list:
        """Return a list of available losses."""
        return ['categorical_crossentropy']

    @classmethod
    def list_available_metrics(cls) -> list:
        """Return a list of available metrics."""
        return ['acc']

    def make_output_layer(self):
        return keras.layers.Dense(self._num_classes, activation='softmax')
