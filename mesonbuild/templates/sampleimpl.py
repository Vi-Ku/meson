# Copyright 2019 The Meson development team

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import annotations

import typing as T

if T.TYPE_CHECKING:
    from ..minit import Arguments


class SampleImpl:

    def __init__(self, args: Arguments):
        self.name = args.name
        self.version = args.version

    def create_executable(self) -> None:
        raise NotImplementedError('Sample implementation for "executable" not implemented!')

    def create_library(self) -> None:
        raise NotImplementedError('Sample implementation for "library" not implemented!')
