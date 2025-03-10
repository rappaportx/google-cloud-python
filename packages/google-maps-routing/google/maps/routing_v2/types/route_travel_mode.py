# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import MutableMapping, MutableSequence

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.maps.routing.v2",
    manifest={
        "RouteTravelMode",
    },
)


class RouteTravelMode(proto.Enum):
    r"""A set of values used to specify the mode of travel. NOTE: WALK,
    BICYCLE, and TWO_WHEELER routes are in beta and might sometimes be
    missing clear sidewalks, pedestrian paths, or bicycling paths. You
    must display this warning to the user for all walking, bicycling,
    and two-wheel routes that you display in your app.
    """
    TRAVEL_MODE_UNSPECIFIED = 0
    DRIVE = 1
    BICYCLE = 2
    WALK = 3
    TWO_WHEELER = 4


__all__ = tuple(sorted(__protobuf__.manifest))
