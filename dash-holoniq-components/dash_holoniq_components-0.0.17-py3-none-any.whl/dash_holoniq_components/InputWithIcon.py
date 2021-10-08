# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class InputWithIcon(Component):
    """An InputWithIcon component.
Adds a font awesome glyph and tooltip to the end of a standard
input box

Keyword arguments:

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- autoComplete (string; optional):
    This attribute indicates whether the value of the control can be
    automatically completed by the browser.

- autoFocus (string; optional):
    The element should be automatically focused after the page has
    loaded.

- bs_size (string; optional):
    Set the size of the Input. Options: 'sm' (small), 'md' (medium) or
    'lg' (large). Default is 'md'.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- debounce (boolean; default False):
    If True, changes to input will be sent back to the Dash server
    only when the enter key is pressed or when the component loses
    focus.  If it's False, it will sent the value back on every
    change.

- disabled (boolean; optional):
    Set to True to disable the Input.

- icon (string; optional):
    Font awesome glyph name, eg `fa fa-unlock`.

- inputMode (a value equal to: "verbatim", "latin", "latin-name", "latin-prose", "full-width-latin", "kana", "katakana", "numeric", "tel", "email", "url"; optional):
    The inputmode global attribute is an enumerated attribute that
    provides  a hint as to the type of data that might be entered by
    the user while  editing the element or its contents. It can have
    the following values.

- invalid (boolean; optional):
    Apply invalid style to the Input for feedback purposes. This will
    cause any FormFeedback in the enclosing FormGroup with valid=False
    to display.

- key (string; optional):
    A unique identifier for the component, used to improve performance
    by React.js while rendering components See
    https://reactjs.org/docs/lists-and-keys.html for more info.

- list (string; optional):
    Identifies a list of pre-defined options to suggest to the user.
    The value must be the id of a <datalist> element in the same
    document. The browser displays only options that are valid values
    for this input element. This attribute is ignored when the type
    attribute's value is hidden, checkbox, radio, file, or a button
    type.

- loading_state (dict; optional):
    Object that holds the loading state object coming from
    dash-renderer.

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- max (string | number; optional):
    The maximum (numeric or date-time) value for this item, which must
    not be less than its minimum (min attribute) value.

- maxLength (string; optional):
    If the value of the type attribute is text, email, search,
    password, tel, or url, this attribute specifies the maximum number
    of characters (in UTF-16 code units) that the user can enter. For
    other control types, it is ignored. It can exceed the value of the
    size attribute. If it is not specified, the user can enter an
    unlimited number of characters. Specifying a negative number
    results in the default behavior (i.e. the user can enter an
    unlimited number of characters). The constraint is evaluated only
    when the value of the attribute has been changed.

- min (string | number; optional):
    The minimum (numeric or date-time) value for this item, which must
    not be greater than its maximum (max attribute) value.

- minLength (string; optional):
    If the value of the type attribute is text, email, search,
    password, tel, or url, this attribute specifies the minimum number
    of characters (in Unicode code points) that the user can enter.
    For other control types, it is ignored.

- n_blur (number; default 0):
    Number of times the input lost focus.

- n_blur_timestamp (number; default -1):
    Last time the input lost focus.

- n_submit (number; default 0):
    Number of times the `Enter` key was pressed while the input had
    focus.

- n_submit_timestamp (number; default -1):
    Last time that `Enter` was pressed.

- name (string; optional):
    The name of the control, which is submitted with the form data.

- pattern (string; optional):
    A regular expression that the control's value is checked against.
    The pattern must match the entire value, not just some subset. Use
    the title attribute to describe the pattern to help the user. This
    attribute applies when the value of the type attribute is text,
    search, tel, url, email, or password, otherwise it is ignored. The
    regular expression language is the same as JavaScript RegExp
    algorithm, with the 'u' parameter that makes it treat the pattern
    as a sequence of unicode code points. The pattern is not
    surrounded by forward slashes.

- placeholder (string; optional):
    A hint to the user of what can be entered in the control . The
    placeholder text must not contain carriage returns or line-feeds.
    Note: Do not use the placeholder attribute instead of a <label>
    element, their purposes are different. The <label> attribute
    describes the role of the form element (i.e. it indicates what
    kind of information is expected), and the placeholder attribute is
    a hint about the format that the content should take. There are
    cases in which the placeholder attribute is never displayed to the
    user, so the form must be understandable without it.

- plaintext (boolean; optional):
    Set to True for a readonly input styled as plain text with the
    default form field styling removed and the correct margins and
    padding preserved.

- size (string; optional):
    The initial size of the control. This value is in pixels unless
    the value of the type attribute is text or password, in which case
    it is an integer number of characters. This attribute applies only
    when the type attribute is set to text, search, tel, url, email,
    or password, otherwise it is ignored. In addition, the size must
    be greater than zero. If you do not specify a size, a default
    value of 20 is used.

- step (string | number; optional):
    Works with the min and max attributes to limit the increments at
    which a numeric or date-time value can be set. It can be the
    string any or a positive floating point number. If this attribute
    is not set to any, the control accepts only values at multiples of
    the step value greater than the minimum.

- style (dict; optional):
    Defines CSS styles which will override styles previously set.

- tooltip (string; optional):
    tooltip to associate with glyph.

- type (a value equal to: "text", 'number', 'password', 'email', 'range', 'search', 'tel', 'url', 'hidden'; optional):
    The type of control to render.

- valid (boolean; optional):
    Apply valid style to the Input for feedback purposes. This will
    cause any FormFeedback in the enclosing FormGroup with valid=True
    to display.

- value (string | number; optional):
    The value of the Input."""
    @_explicitize_args
    def __init__(self, tooltip=Component.UNDEFINED, icon=Component.UNDEFINED, onClick=Component.UNDEFINED, id=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, key=Component.UNDEFINED, type=Component.UNDEFINED, value=Component.UNDEFINED, disabled=Component.UNDEFINED, autoComplete=Component.UNDEFINED, autoFocus=Component.UNDEFINED, inputMode=Component.UNDEFINED, list=Component.UNDEFINED, max=Component.UNDEFINED, maxLength=Component.UNDEFINED, min=Component.UNDEFINED, minLength=Component.UNDEFINED, step=Component.UNDEFINED, size=Component.UNDEFINED, bs_size=Component.UNDEFINED, valid=Component.UNDEFINED, invalid=Component.UNDEFINED, plaintext=Component.UNDEFINED, placeholder=Component.UNDEFINED, name=Component.UNDEFINED, pattern=Component.UNDEFINED, n_submit=Component.UNDEFINED, n_submit_timestamp=Component.UNDEFINED, n_blur=Component.UNDEFINED, n_blur_timestamp=Component.UNDEFINED, debounce=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'autoComplete', 'autoFocus', 'bs_size', 'className', 'debounce', 'disabled', 'icon', 'inputMode', 'invalid', 'key', 'list', 'loading_state', 'max', 'maxLength', 'min', 'minLength', 'n_blur', 'n_blur_timestamp', 'n_submit', 'n_submit_timestamp', 'name', 'pattern', 'placeholder', 'plaintext', 'size', 'step', 'style', 'tooltip', 'type', 'valid', 'value']
        self._type = 'InputWithIcon'
        self._namespace = 'dash_holoniq_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'autoComplete', 'autoFocus', 'bs_size', 'className', 'debounce', 'disabled', 'icon', 'inputMode', 'invalid', 'key', 'list', 'loading_state', 'max', 'maxLength', 'min', 'minLength', 'n_blur', 'n_blur_timestamp', 'n_submit', 'n_submit_timestamp', 'name', 'pattern', 'placeholder', 'plaintext', 'size', 'step', 'style', 'tooltip', 'type', 'valid', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(InputWithIcon, self).__init__(**args)
