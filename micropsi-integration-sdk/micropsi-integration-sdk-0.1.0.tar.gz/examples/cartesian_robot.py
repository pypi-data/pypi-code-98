from typing import Optional

import numpy as np

from micropsi_integration_sdk import CartesianRobot, HardwareState


class MyCartesianRobot(CartesianRobot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__connected = False
        self.__ready_for_control = False
        self.__controlled = False
        self.__joint_positions = np.zeros(3)

    @staticmethod
    def get_supported_models() -> list:
        return ["MyRobot Cartesian"]

    def get_joint_count(self) -> int:
        return 3

    def get_joint_speed_limits(self) -> np.array:
        return np.array([.2, .2, .2])

    def get_joint_position_limits(self) -> np.array:
        return np.array([[-.5, .5], [-.5, .5], [-.5, .5]])

    def connect(self) -> bool:
        self.__connected = True
        return True

    def disconnect(self) -> None:
        self.__connected = False

    def prepare_for_control(self) -> None:
        self.__ready_for_control = True

    def is_ready_for_control(self) -> bool:
        return self.__ready_for_control

    def take_control(self) -> None:
        self.__controlled = True

    def release_control(self) -> None:
        self.__controlled = False
        self.__ready_for_control = False

    def get_hardware_state(self) -> Optional[HardwareState]:
        return HardwareState(
            joint_positions=np.copy(self.__joint_positions),
            joint_speeds=None,
            raw_wrench=None,
            joint_temperatures=None
        )

    def clear_cached_hardware_state(self) -> None:
        pass

    def forward_kinematics(self, *, joint_positions: np.array) -> np.array:
        matrix = np.identity(4)
        matrix[:3, 3] = joint_positions
        return matrix

    def send_goal_pose(self, *, goal_pose: np.ndarray, step_count: int) -> None:
        assert goal_pose.shape == (4, 4)
        self.__joint_positions = goal_pose[:3, 3]

    def command_move(self, *, joint_positions: np.array) -> None:
        self.__joint_positions = np.copy(joint_positions)

    def command_stop(self) -> None:
        pass
