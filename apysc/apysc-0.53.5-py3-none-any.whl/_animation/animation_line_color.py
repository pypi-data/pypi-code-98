"""Class implementation for the line color animation value.
"""

from typing import Generic
from typing import TypeVar
from typing import Union

import apysc as ap
from apysc._animation.animation_base import AnimationBase
from apysc._animation.easing import Easing
from apysc._color import color_util
from apysc._type.variable_name_interface import VariableNameInterface

_T = TypeVar('_T', bound=VariableNameInterface)
StrOrString = TypeVar('StrOrString', str, ap.String)


class AnimationLineColor(AnimationBase[_T], Generic[_T]):
    """
    The animation class for a line color.
    """

    _line_color: ap.String

    def __init__(
            self,
            target: _T,
            line_color: StrOrString,
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> None:
        """
        The animation class for a line color

        Parameters
        ----------
        target : VariableNameInterface
            A target instance of the animation target
            (e.g., `Rectangle` instance).
        line_color : str or String
            The final color (hex color code) of the animation.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.
        """
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=AnimationLineColor):
            from apysc._converter import to_apysc_val_from_builtin
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            variable_name: str = expression_variables_util.\
                get_next_variable_name(
                    type_name=var_names.ANIMATION_LINE_COLOR)
            line_color = color_util.complement_hex_color(
                hex_color_code=line_color)
            self._line_color = to_apysc_val_from_builtin.\
                get_copied_string_from_builtin_val(string=line_color)
            self._set_basic_animation_settings(
                target=target,
                duration=duration,
                delay=delay,
                easing=easing)
            super(AnimationLineColor, self).__init__(
                variable_name=variable_name)

    def _get_animation_func_expression(self) -> str:
        """
        Get a animation function expression.

        Returns
        -------
        expression : str
            Animation function expression.
        """
        from apysc._type import value_util
        line_color_str: str = value_util.get_value_str_for_expression(
            value=self._line_color)
        return f'\n  .stroke({line_color_str});'

    def _get_complete_event_in_handler_head_expression(self) -> str:
        """
        Get an expression to be inserted into the complete event
        handler's head.

        Returns
        -------
        expression : str
            An expression to be inserted into the complete event
            handler's head.
        """
        from apysc._display.line_color_interface import LineColorInterface
        expression: str = ''
        if isinstance(self._target, LineColorInterface):
            self._target._initialize_line_color_if_not_initialized()
            expression = (
                f'{self._target._line_color.variable_name} = '
                f'{self._line_color.variable_name};'
            )
        return expression
