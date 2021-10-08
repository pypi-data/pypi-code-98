# Base file for all codegen-related imports
# All integrations should have a line in the import section like this
#
# >>> import esphome.codegen as cg
#
# Integrations should specifically *NOT* import directly from the
# other helper modules (cpp_generator etc) directly if they don't
# want to break suddenly due to a rename (this file will get backports for features).

# pylint: disable=unused-import
from esphome.cpp_generator import (  # noqa
    Expression,
    RawExpression,
    RawStatement,
    TemplateArguments,
    StructInitializer,
    ArrayInitializer,
    safe_exp,
    Statement,
    LineComment,
    progmem_array,
    static_const_array,
    statement,
    variable,
    new_variable,
    Pvariable,
    new_Pvariable,
    add,
    add_global,
    add_library,
    add_build_flag,
    add_define,
    get_variable,
    get_variable_with_full_id,
    process_lambda,
    is_template,
    templatable,
    MockObj,
    MockObjClass,
)
from esphome.cpp_helpers import (  # noqa
    gpio_pin_expression,
    register_component,
    build_registry_entry,
    build_registry_list,
    extract_registry_entry_config,
    register_parented,
)
from esphome.cpp_types import (  # noqa
    global_ns,
    void,
    nullptr,
    float_,
    double,
    bool_,
    int_,
    std_ns,
    std_string,
    std_vector,
    uint8,
    uint16,
    uint32,
    uint64,
    int32,
    const_char_ptr,
    NAN,
    esphome_ns,
    App,
    Nameable,
    Component,
    ComponentPtr,
    PollingComponent,
    Application,
    optional,
    arduino_json_ns,
    JsonObject,
    JsonObjectRef,
    JsonObjectConstRef,
    Controller,
    GPIOPin,
)
