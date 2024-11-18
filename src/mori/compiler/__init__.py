# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024 Jayesh Badwaik <jayesh@ambhora.com>
# --------------------------------------------------------------------------------------------------

import enum


class TargetEnum(enum.Enum):
    html = "html"
    pdf = "pdf"


class PDFGeneratorEnum(enum.Enum):
    simpletex = "tex"


class HTMLGeneratorEnum(enum.Enum):
    html = "html"


class TargetGeneratorPair:
    def __init__(self, target, generator):
        self._target = target
        self._generator = generator

        if target not in target_generator_map:
            raise ValueError(f"Invalid target: {target}")

        if generator not in target_generator_map[target]:
            raise ValueError(f"Invalid generator {generator} for target {target}")

    def target(self):
        return self._target

    def generator(self):
        return self._generator


target_generator_map = {
    "pdf": [generator for generator in PDFGeneratorEnum],
    "html": [generator for generator in HTMLGeneratorEnum],
}


class CompileOption:
    def __init__(self, **kwargs):
        pass

def compile(input_dir, output_dir, param):
    pass
